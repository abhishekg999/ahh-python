def sudo_setattr(obj, attr, value):
    """
    Sets the value of the specified attribute on the given object.

    Args:
        obj: The object on which to set the attribute.
        attr: The name of the attribute to set.
        value: The value to set for the attribute.

    Returns:
        None
    """
    (vars(obj) == type('', (), {'__eq__': lambda s,o:o})())[attr] = value