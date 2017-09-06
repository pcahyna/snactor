_REGISTERED_ACTORS = {}


def _instantiate_actor(data):
    if not data:
        return None
    return data[1](data[0])


def get_registered_actors():
    return _REGISTERED_ACTORS


def get_actor(actor):
    return _instantiate_actor(_REGISTERED_ACTORS.get(actor))


def must_get_actor(actor):
    return _instantiate_actor(_REGISTERED_ACTORS[actor])


def actor_names_by_tags(tags, names=()):
    if names == ():
        return [name for name, a in _REGISTERED_ACTORS.items() if a[0].tags.intersection(tags)]
    else:
        return [name for name, a in _REGISTERED_ACTORS.items() if a[0].tags.intersection(tags) and name in names]


def register_actor(name, definition, executor):
    if name in _REGISTERED_ACTORS:
        raise LookupError("Actor '{}' has been already registered previously".format(name))
    _REGISTERED_ACTORS[name] = (definition, executor)


def _clear_actors():
    _REGISTERED_ACTORS.clear()
