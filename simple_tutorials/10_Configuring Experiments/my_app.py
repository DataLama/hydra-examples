# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()

"""설명
* 다양한 실험 관리를 위해서 master config와 experiment를 분리하여 overriding을 통해 실행함.
* conf path 바로 아래가 global.
  * 근데 저거보다 1 depth가 더 들어갈 경우에는 # @package _global_ 을 통해 global로 취급해줄 수 있음.
* addition을 통해 구현
"""

"""python my_app.py --multirun +experiment=aplite,nglite

[2022-04-27 01:29:39,238][HYDRA] Launching 2 jobs locally
[2022-04-27 01:29:39,238][HYDRA]        #0 : +experiment=aplite
db:
  name: sqlite
server:
  name: apache
  port: 8080

[2022-04-27 01:29:39,365][HYDRA]        #1 : +experiment=nglite
db:
  name: sqlite
server:
  name: nginx
  port: 8080
"""

"""python my_app.py --multirun '+experiment=glob(*)'
[2022-04-27 01:29:18,929][HYDRA] Launching 2 jobs locally
[2022-04-27 01:29:18,930][HYDRA]        #0 : +experiment=aplite
db:
  name: sqlite
server:
  name: apache
  port: 8080

[2022-04-27 01:29:19,050][HYDRA]        #1 : +experiment=nglite
db:
  name: sqlite
server:
  name: nginx
  port: 8080
"""