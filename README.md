# RobloxToBlend
A somewhat easy method for converting Roblox builds (consisting of simple primitives) to Blender files, WHILE PRESERVING INDIVIDUAL BLOCKS. This can be useful for making pretty renders of Roblox worlds.

If you just need the model, you can already export it using existing tools -- this is useful for when you would like to manipulate individual blocks after import.

Currently supports importing blocks, spheres, and cylinders.
Works with transparency, reflectance, and color, but not materials (at least not yet.)


--------


--------


--------

TUTORIAL:

1) Open a roblox world you own; or perhaps an older public uncopylocked world that you feel quite nostalgic about. This tool is NOT used for copying copylocked worlds, and it is NOT meant to be used for nefarious purposes. Please be respectful while using this tool, especially when using it on another's work. I don't necessarily reccomend copying Roblox worlds for use in projects outside of Blender, since I do not know how Roblox itself will react to that. Using this on something like Roblox's Crossroads is likely okay (don't take my word on this), but you should ask for permission to use this tool for smaller uncopylocked worlds you are not yourself associated with.

2) Create a model; any parts you would like to copy should be inside that model somewhere before you use the tool.

3) Create a new script within the model. In the script, paste the code from Roblox_PartGetter.lua, and hit "Run" or "Start". Make sure to read the script in its entirety, including the comments, before running the world.

4) Once the world is run: Look at the Developer console, and find the big block of text with lots of commas and stuff (You'll know what I mean when you see it), originating from the script you've created. This is a converted form of your model showing types, positions, orientations, colors, etc. of all the parts you'll be importing into Blender; a middleman.

5) Copy that block of text that was printed; the one you just found. When pasting it, make sure to format it correctly, so that only the printed block of text, and not anything else, is used as input.
Here is an example of how to format the output correctly:
>Raw output "  00:55:03.335  Block,13,105,172,-176,1,-31,6,1.2,6,0,0,0,0,0; Block,196,40,28,54,1,129,6,1.2,6,0,0,0,0,0;  -  Server - Script:12"
 VVVVVV becomes
>Useable input "Block,13,105,172,-176,1,-31,6,1.2,6,0,0,0,0,0; Block,196,40,28,54,1,129,6,1.2,6,0,0,0,0,0;"
Basically, just delete the information about the time from the front, and the positional data at the back, and remove any spaces.

6) Optionally, save that formatted block of text to a text file so that it can be used again. By doing this, you won't have to repeat the former steps in case you lose your progress later on.

7) Open a new Blender project and delete everything in the default scene.

8) In Blender, open up a text editor window (Shift-F11). Click New and create a new text file.

9) Paste the code from Blender_Converter.py into the new text file.

10) On the fifth line, where it says 'inputText = ""', paste the block of text from earlier in between the parenthesis. Make sure to read the script in its entirety, including the comments, before running the code.

11) Hit the arrow button (looks like >) to run the code. This may take a while for larger builds.

12) Once it finishes, return to the viewport (Shift-F5 by default). The Roblox world should be successfully imported; assuming all the steps were done correctly. It could take a few tries to get it just right.

13) Assuming you see your creation, you're done! Switch to the Cycles engine (By clicking the camera looking thingy in the properties menu and changing from Eevee to Cycles) if your imported creation includes transparent or reflective blocks, to see the transparency or reflection.
