magick tools in python
======================

essential tools for networked witchery, consisting mostly of some verbs and nouns.
all can be chained together for cyber-spellcraft.

this is //very much a work in progress//. it will likely end up a library. use carefully.

sigilcraft.py
-------------
construct cryptographic hash-digests of intention, to file or stdout. interactive.

`python sigilcraft.py --file myfirst.sigil`

`python sigilcraft.py --stdout | some_other_process`

chant.py
--------
emits message from file via UDP on specified port and adapter at specified interval

`python chant.py --file magicwords.txt`

`some_other_process | python chant.py --stdin`

burn.py
-------
drags specified file back to chaos by writing pseudo-random bytestream to it until indecipherable, and then unlinks given file from filesystem

`python burn.py --file effigy.jpg`

`some_other_process | python burn.py --stdin`

shred.py
--------
cuts file in half horizontally, then cuts resulting files in half vertically. it repeats this process N times.

`python shred.py --file myfirst.sigil --iterations 4`

`some_other_process | python shred.py --stdin --iterations 2`

sacrifice.py
------------
bleeds bytes from file to stdout until bytes are exhausted. file then unlinked from filesystem. **note**: this is messy and might require a `reset` if not piped elsewhere.

`python sacrifice.py --file goat.png`

`some_other_process | python sacrifice.py --stdin`

chalice.py
----------
holds bytestream from stdin or given file until killed. if given a file, file unlinked from filesystem after collecting its contents.

`python chalice.py --file wine.jpg`

`some_other_process | python chalice.py --stdin`
