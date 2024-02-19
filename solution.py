def is_bulky(width: int, hegiht: int, length: int):
    """
    Returns whether a package is bulky (its volume is greater than or equal to
    10 ^ 6 cubic centimeters), or where one dimension is greater than or equal
    to 150 cm).

    :param width: Width of the package, in centimeters.
    :type width: int
    :param height: Height of the package, in centimeters.
    :type height: int
    :param length: Length of the package, in centimeters.
    :type length: int
    :returns: The input package is bulky.
    :rtype: boolean
    """
    pass

def is_heavy(mass: int):
    """
    Categorizes packages as heavy (its mass is greater than or equal to 20 kg).

    :param mass: Mass of the package, in kilograms.
    :type mass: int
    :returns: The input package is heavy.
    :rtype: boolean
    """
    pass

def sort(width: int, height: int, length: int, mass: int):
    """
    Sorts packages based on width, height, length, and mass.

    :param width: Width of the package, in centimeters.
    :type width: int
    :param height: Height of the package, in centimeters.
    :type height: int
    :param length: Length of the package, in centimeters.
    :type length: int
    :param mass: Mass of the package, in kilograms.
    :type mass: int
    :returns: The classification of the package.
    :rtype: "STANDARD" or "SPECIAL" or "REJECTED"
    :raises ValueError: If any input is not a positive integer.
    """
    # Check whether the input values are non-negative integers, and raise if
    # not.
