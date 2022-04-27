# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import os

from omegaconf import DictConfig

import hydra


@hydra.main()
def my_app(_cfg: DictConfig) -> None:
    print(f"Working directory : {os.getcwd()}")


if __name__ == "__main__":
    my_app()

    
"""설명
* hydra는 multi-run을 효과적으로 지원하기 위해서 각각의 프로세스가 실행되는 working directory가 새로 생성되고 그 위에서 코드가 실행됨.
  - Store the output for the application (For example, a database dump file)
  - Store the Hydra output for the run (Configuration, Logs etc)
* 로그파일이 있는 경로에 .hydra라는 이름의 configuration들을 dump해놓은 파일이 존재함.
* python my_app.py ++hydra.output_subdir=null 으로 실행하면 .hydra라는 파일을 생성하지 않게 지정할 수 있음. or 다른 경로로 저장되도록 지정할 수 있음.
"""