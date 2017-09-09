## desktop idle
> [![Build status](https://ci.appveyor.com/api/projects/status/gwlnytjjw4ju3vs0?svg=true)](https://ci.appveyor.com/project/bithavoc/node-desktop-idle)
> [![Build Status](https://travis-ci.org/bithavoc/node-desktop-idle.svg?branch=master)](https://travis-ci.org/bithavoc/node-desktop-idle)

Node/Electron module to detect idle desktop user (OSX, Windows and Linux).

### Installation
```
npm install --save desktop-idle
# or yarn
yarn add desktop-idle
```

### Cross-Platform Support
* **Windows:** [GetLastInputInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms646302(v=vs.85).aspx), see `src/win/idle.cc`.
* **Mac(OSX):** [CoreGraphics Event Source](https://developer.apple.com/documentation/coregraphics/1408790-cgeventsourcesecondssincelasteve), see `src/mac/idle.cc`.
* **Linux:** [X Screensaver](https://linux.die.net/man/3/xscreensaverqueryinfo), see `src/linux/idle.cc`.

### Usage
```
var desktopIdle = require('desktop-idle');
console.log(desktopIdle.getIdleTime());
```

### Test

```
yarn test
```

### License

> MIT - Bithavoc<im@bithavoc.io>