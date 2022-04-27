# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(config_path=".", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
    
"""설명
* config_path, config_name을 통해 hydra app에 필요한 configuration을 config 파일로 관리할 수 있다.
* config.yaml은 application을 실행할 때, 자동으로 로딩됨.
* +을 빼고 파라미터를 넘기면 config의 value를 overwrite할 수 있음.
* ++를 사용하면, config가 있는 경우 overwrite를 하고, 없는 경우 새로 생성 후 값을 넘길 수 있음.
"""

""" config.yaml을 정의 후, python 파일을 실행.
>>> python my_app.py

db:
  driver: mysql
  user: omry
  password: secret
"""

""" config.yaml을 변수를 overwrite를 하기.
>>> python my_app.py db.user=root db.password=1234

db:
  driver: mysql
  user: omry
  password: secret
"""

""" ++를 활용하여 변수를 overwrite하기.
>>> python my_app.py ++db.password=1234

db:
  driver: mysql
  user: omry
  password: secret

>>> python my_app.py ++db.timeout=5

db:
  driver: mysql
  user: omry
  password: secret
  timeout: 5
"""