from typing import TypeAlias, Literal

ReplaceStrModes: TypeAlias = Literal['-', '_']


def normalize_image_name(image_name: str, remove_namespace: bool = True, replace_char: ReplaceStrModes = '_') -> str:
    """
    Normalize the image name by either removing the part before '/' or replacing '/' with a specified character.

    :param image_name: The original image name.
    :param remove_namespace: 是否移除镜像名前缀, 例如leo03w/ubuntu:20.04中的 leo03w.
    :param replace_char: The character to replace '/' with if method is 'replace'.
    :return: The normalized image name.

    >>> normalize_image_name('leo03w/ubuntu:20.04')
    'ubuntu:20.04'
    >>> normalize_image_name('leo03w/ubuntu:20.04', remove_namespace=False)
    'leo03w-ubuntu:20.04'
    >>> normalize_image_name('leo03w/ubuntu:20.04', remove_namespace=False, replace_char='_')
    'leo03w_ubuntu:20.04'
    """
    if '/' in image_name:
        if remove_namespace:
            return image_name.split('/')[-1]
        else:
            return image_name.replace('/', replace_char)
    return image_name
