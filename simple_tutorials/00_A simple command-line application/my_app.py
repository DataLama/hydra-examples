# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra

@hydra.main()
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
    
"""설명
* hydra의 main함수로 wrapping 후 실행하면 hydra를 통해 dynamic하게 configuration을 수행할 수 있음.
* outputs/{%Y-%m-%d}/{%H-%M-%S}/my_app.log에 프로그램 실행 관련 로그가 저장됨.
"""
    
""" python으로 실행하기
>>> python my_app.py

my_app.py:6: UserWarning: 
config_path is not specified in @hydra.main().
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_hydra_main_config_path for more information.
  @hydra.main()
{}

"""

""" command line으로 dynamic하게 config value를 추가하기.
>>> python my_app.py +db.driver=mysql +db.user=omry +db.password=secret

my_app.py:6: UserWarning: 
config_path is not specified in @hydra.main().
See https://hydra.cc/docs/next/upgrades/1.0_to_1.1/changes_to_hydra_main_config_path for more information.
  @hydra.main()
db:
  driver: mysql
  user: omry
  password: secret

"""

