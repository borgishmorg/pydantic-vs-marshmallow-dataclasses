Сравнение времени сериализации/десериализации pydantic и marshmallow

```bash
$ python -m pydantic_vs_marshmallow_dataclasses.my_pydantic
pydantic load time: 6.99063s
pydantic dump time: 3.23448s
pydantic dump (no model) time: 2.73132s

$ python -m pydantic_vs_marshmallow_dataclasses.my_marshmallow
marshmallow load time: 52.085s
marshmallow dump time: 19.8456s

$ python -m pydantic_vs_marshmallow_dataclasses.my_marshmallow_over_pydantic
marshmallow over pydantic load time: 6.91634s
marshmallow over pydantic dump time: 19.1957s
```
