# topostats gui

This is an unofficial gui for the TopoStats software, intended to act as a user-friendly and less intimidating way to interact with the software, without having to use the command-line (aside from starting the program).

I have designed this to act as a wrapper for TopoStats, not editing any of TopoStats' code, so it should be compatible with any TopoStats version, or at least easy to update.

It uses Flask as a python back-end, to handle navigating the directory structure of your system, creating folders and config files, and also running shell scripts to run TopoStats.

The back-end communicates with the front-end webpage via asynchronous AJAX GET/POST requests, transferring data in the JSON format.

It also utilises Jinja2 and JQuery for easier web-page structuring and rendering.
