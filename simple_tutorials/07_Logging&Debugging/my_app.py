# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import logging

from omegaconf import DictConfig

import hydra

# A logger for this file
log = logging.getLogger(__name__)


@hydra.main()
def my_app(_cfg: DictConfig) -> None:
    log.info("Info level message")
    log.debug("Debug level message")


if __name__ == "__main__":
    my_app()
    
"""설명
* logger만 세팅하면 됨.
  * 실제 logging되는 파일이나 방식에 대한 관리는 hydra를 통해 정의 가능함.
* hydra는 configuration에 대한 효과적인 debugging을 위해서 configuration을 print하는 기능을 제공함.
  * --cfg, -c는 실제 프로세스 수행은 하지 않고, 해당 application에 적용된 configuration만 살펴보는 기능임.
    * --cfg job (내가 정의한 configuration), --cfg hydra (hydra 관련 configuration), --cfg all (두 configuration을 union한 결과)
  * --package, -p는 configuration에서 특정 패키지에 대한 부분만 살펴볼 수 있음.
  * --resolve라는 flag는 interpolations를 resolve한 config를 보여줌.
* --info 
  * --info all: Default behavior, prints everything
  * --info config: Prints information useful to understanding the config composition: Config Search Path, Defaults Tree, Defaults List and the final config.
  * --info defaults: Prints the Final Defaults List
  * --info defaults-tree: Prints the Defaults Tree
  * --info plugins: Prints information about installed plugins
"""