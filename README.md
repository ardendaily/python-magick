magick tools in python
======================

essential tools for networked witchery, consisting mostly of some verbs and nouns.
all can be chained together for cyber-spellcraft.

sigilcraft.py
-------------
construct cryptographic hash-digests of intention, to file or stdout.

chant.py
--------
emits message from file via UDP on specified port and adapter at specified interval 

burn.py
-------
drags specified file back to chaos by writing pseudo-random bytestream to it, and then unlinks given file from filesystem

shred.py
--------
cuts file in half horizontally, then cuts resulting files in half vertically. it repeats this process N times.

sacrifice.py
------------
bleeds bytes from file to stdout until bytes are exhausted. file then unlinked from filesystem.

chalice.py
----------
holds bytestream from stdin or given file until killed. if given a file, file unlinked from filesystem after collecting its contents.

grimoire 
========

a simple sigil enchantment
--------------------------
+ clear your mind and minimize distraction windows. this is a good time to light candles, burn incense, and skype others in your coven.

+ launch a terminal. execute `python sigilcraft.py --outfile myfirst.sigil`. 
	+ follow the prompts; they are written to clarify your intention.
	+ your intentions are outputted as a SHA-512 cryptographic hash in `myfirst.sigil`.

+ execute `python chant.py --file myfirst.sigil --interval 3 --port 5005`. 
	+ **optional**: change the port number and interval if specific numerology aligns with your intention.
	+ continue to focus on your intention.
	+ your computer is broadcasting your sigil every 3 seconds on port 5005. optionally verify this with `netcat -ul 5005`. 
	+ kill the chant with `CTRL+C` when satisfied

+ execute `python burn.py --file myfirst.sigil` to destroy the sigil and complete the spell.