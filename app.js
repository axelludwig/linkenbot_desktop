// const ioHook = require('iohook');
// "use strict";

// ioHook.on('mousemove', event => {
//   console.log(event); // { type: 'mousemove', x: 700, y: 400 }
// });

// Register and start hook
// ioHook.start();

// Alternatively, pass true to start in DEBUG mode.
// ioHook.start(true);


try {
    const ioHook = require("iohook");

} catch (error) {
    console.log(error);
}

let keystrokes = "Keystrokes start now : ";
ioHook.on("keydown", (event) => {
    keystrokes += String.fromCharCode(event.rawcode);
    console.log(keystrokes);
});
ioHook.start();