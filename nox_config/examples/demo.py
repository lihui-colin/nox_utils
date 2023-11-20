import _init_path  # noqa F401
from pathlib import Path
from config import Config

data_dir = Path(__file__).parent
cfg = Config.fromfile(
    data_dir / "configs" / "hv_pointpillars_secfpn_sbn_2x16_2x_waymoD5-3d-3class.py"
)
print(cfg)
