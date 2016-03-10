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