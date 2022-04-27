# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(config_path="conf")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
    
"""설명
* conf_path -> configuration의 root path?
* `conf/*` -> *에 포함되는 directory들은 config package라고 함.
   * 본 예제에서 config package는 db
* 디테일한 값들은 override를 통해 변경 가능함.
"""


""" Group config file과 overriding을 함께 사용하기
>>> python my_app.py +db=postgresql db.timeout=20

db:
  driver: postgresql
  pass: drowssap
  timeout: 20
  user: postgres_user
"""