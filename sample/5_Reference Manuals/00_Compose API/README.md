## Compose API는 언제 쓰는가?


## Compose API를 사용하면 잃는 것은 무엇인가?
- Tab completion (필요 없음.)
- Multirun (ray같은 다른 모듈에 맡기면 됨.)
- Working directory management, Logging management and more (ray같은 다른 모듈에 맡기면 됨.)

> 순수하게 configuration에 대한 구조적 관리가 필요하고 그 이상에 대한 기능이 필요 없을 경우에는 그냥 compose api를 사용하는 것이 좋을 듯.
> 특히 jupyter를 주요 개발 IDE를 사용하는 나 같은 경우는 compose api가 더 맞는듯.