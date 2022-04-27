### Structured Configs use Python dataclasses to describe your configuration structure and types.
- Runtime type checking as you compose or mutate your config
- Static type checking when using static type checkers (mypy, PyCharm, etc.)

### Structured Configs supports
- Primitive types (int, bool, float, str, Enums)
- Nesting of Structured Configs
- Containers (List and Dict) containing primitives or Structured Configs
- Optional fields

### Structured Configs Limitations
- Union types are not supported (except Optional)
- User methods are not supported

> 뭔가 configuration에 대한 정교한 type checking이 필요하면 구현하는 것이 필요할 수 있으나(API 개발), 단순히 딥러닝 실험을 관리하는 케이스에서는 약간은 over engineering이 될 수도 있겠다는 생각. 그러므로 본 part는 우선 패스
