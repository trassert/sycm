from pathlib import Path

import yaml

__version__ = "0.1.0"
__all__ = ["ConfigManager", "ConfigSection"]


class ConfigSection(dict):
    def __init__(self, data, default=None):
        super().__init__(data)
        self._default = default or {}
        for k, v in data.items():
            self[k] = (
                ConfigSection(v, self._default.get(k))
                if isinstance(v, dict)
                else [ConfigSection(i) if isinstance(i, dict) else i for i in v]
                if isinstance(v, list)
                else v
            )

    def __getattr__(self, key):
        if key in self:
            return self[key]
        if key in self._default:
            v = self._default[key]
            return ConfigSection(v) if isinstance(v, dict) else v
        msg = f"'{type(self).__name__}' has no attribute '{key}'"
        raise AttributeError(msg)


class ConfigManager:
    def __init__(self, path: str | Path, defaults: str | Path | None = None):
        """
        Initialize the ConfigManager with a path to the config file and optional defaults.

        Args:
            path (str | Path): Path to the config file.
            defaults (str | Path | None): Path to the defaults config file.

        Raises:
            ValueError: If the config file is missing and no defaults are provided.

        Example:
            ```path/to/config.yaml
            some_value: "i am steve"
            ```
            >>> config = ConfigManager("path/to/config.yaml", "path/to/defaults.yaml")
            >>> print(config.some_value)
            "i am steve"
        """
        path, defaults = Path(path), Path(defaults) if defaults else None
        default_data = (
            yaml.safe_load(defaults.read_text())
            if defaults and defaults.exists()
            else None
        )
        if not path.exists():
            if not defaults:
                msg = "defaults required when config file is missing"
                raise ValueError(msg)
            path.write_text(defaults.read_text())
        self._data = ConfigSection(
            yaml.safe_load(path.read_text()) or {}, default_data
        )

    def __getattr__(self, key):
        return getattr(self._data, key)
