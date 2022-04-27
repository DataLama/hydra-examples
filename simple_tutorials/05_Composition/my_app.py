# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
    
"""설명
* config package에 package별로 다양한 기능들을 configuration을 만든 뒤, 번갈아 끼우는 방식으로 configuration을 세팅할 수 있음.
* multi-run
  * multi-run 기능을 통해 미리 정의한 다양한 configuration을 한번에 실행 가능함.
  * 더 자세한 것은 sweep을 참조
"""