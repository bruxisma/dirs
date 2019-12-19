# Overview

---
![PyPI - Python Version][versions]
![PyPI - License][license]
![PyPI - Package][package]
![Code style: black][style]

`dirs` is a small python library in the spirit of appdirs[1] and other XDG
focused directory libraries. However, there are several that I've
identified with these other libraries:

1. Overengineered solutions to get a few simple paths
2. When Windows support is available, it reads from the registry, rather than
   using the recommended approach of using `KnownFolderID`.
3. No memoization of results. This can be costly when repeatedly working with
   filesystem paths
4. None of these libraries return a `pathlib.Path` object
5. None of these libraries use the `typing` module for better static analysis
   tooling
6. None of these libraries use `dataclasses` or `attrs` to prevent overwriting
   internals or "changing" state on the fly.

`dirs` tries to solve all of this by using `ctypes` under Windows for initial
calls, `functools.lru_cache` for an alternative API, lazy generation of
`config_dirs` and `data_dirs` on all platforms, and many others. Proper
documentation will be uploaded at some point, but the code is fairly readable
and easy to understand.

## Example Use

```py
from dirs import User, Site # Using `*` is also permitted

app = User('app-name')
print(app.config) # prints a joined path with User.config_home() and 'app-name'
print(User.config_home()) # This returns the Path as-is
for path in Site.config_dirs(): # This is a generator, so it's iterable
  print(f'{path} exists: {path.exists()}')
```

[versions]: https://img.shields.io/pypi/pyversions/dirs?style=for-the-badge
[license]: https://img.shields.io/pypi/l/dirs?style=for-the-badge
[package]: https://img.shields.io/pypi/v/dirs?style=for-the-badge
[style]: https://img.shields.io/badge/code%20style-black-000000.svg

[1]: https://github.com/ActiveState/appdirs
