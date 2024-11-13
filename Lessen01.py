import inspect


def introspection_info(obj):
    result = dict()
    result['type'] = type(obj).__name__  # Тип объекта
    try:
        at = list(obj.__dict__.keys())
    except AttributeError:
        at = list()
    result['attributes'] = at  # Атрибуты объекта
    result['methods'] = [x for x in dir(obj) if x not in at]  # Методы объекта
    result['module'] = inspect.getmodule(introspection_info).__name__  # Модуль, к которому объект принадлежит
    return result


number_info = introspection_info(42)
print(number_info)
