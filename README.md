# Simple YAML Config Manager

<p align="center">
<a href=https://t.me/lumintoch><img src=https://img.shields.io/badge/Sponsored%20by-Luminto-purple?style=for-the-badge&logo=githubsponsors&logoColor=white></a>
<img src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white" alt="Badge">
<img src="https://img.shields.io/badge/Ruff-FFC131?style=for-the-badge&logo=ruff&logoColor=white" alt="Badge">
<img src="https://img.shields.io/badge/Uv-FFC131?style=for-the-badge&logo=astral&logoColor=white" alt="Badge">
</p>

Simple python library to use yaml config files with dot notation access (e.g. `cfg.bot.token`).

## Installation

Install via pip:
```bash
pip install sycm
```

Or using `uv`:
```bash
uv add sycm
```

## Usage

```yaml
bot:
  token: 123abcde
```

```python
from sycm import ConfigManager

cfg = ConfigManager("config.yaml")
print(cfg.bot.token)  # 123abcde
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.