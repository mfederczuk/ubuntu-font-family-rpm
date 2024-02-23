<!--
  Copyright (c) 2024 Michael Federczuk
  SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Ubuntu Font Family RPM #

## About ##

This is a simple RPM package that supplies the [Ubuntu font family].

[Ubuntu font family]: <https://font.ubuntu.com/>

## Download ##

A pre-built binary RPM file for Fedora 39 can be downloaded from the [GitHub releases].

```sh
dnf install 'https://github.com/mfederczuk/ubuntu-font-family-rpm/releases/download/0.83-1/ubuntu-fonts-0.83-1.fc39.noarch.rpm'
```

For other other versions of Fedora or other RPM-based Linux distrobutions, the RPM file should be built manually,
though because this is such a simple package, the pre-built file *should* work on any system.

[GitHub releases]: <https://github.com/mfederczuk/ubuntu-font-family-rpm/releases/tag/0.83-1>

## Building ##

To build the RPM file, the programs `rpmlint`, `rpmdev-setuptree` and `rpmbuild` are required.

The script [`build`](./build) is used to lint and fully build the binary RPM file and place it into the repository root.

## Contributing ##

Read through the [Contribution Guidelines](CONTRIBUTING.md) if you want to contribute to this project.

## License ##

For information about copying and licensing, see the [`COPYING.txt`](COPYING.txt) file.
