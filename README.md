ClearDirtyFlag
==============

Sublime Text 3 plugin to clear the dirty flag (a.k.a. the "unsaved" round dot in
the tab) on any view that has identical content to the on-disk version.

Sublime Text will mark a file as dirty if you edit it, even if you end up
changing the content back to what is the on disk version.  Similarly, if you
switch back and forwards between git branches, lots of files will be potentially
marked as dirty even though they're what you want.

If you ever find youself wondering "is this file really changed?" then this
plugin is for you.

## Usage

Execute the "Clear Dirty Flag" command from the command pallet.  All views that
have the dirty flag set will have it cleared if the file on disk matches what's
in the view.

## Author

Written by Mark Fowler mark@twoshortplanks.com

http://github.com/2shortplanks/ClearDirtyFlag