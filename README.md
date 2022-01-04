# RobloxToBlend
A somewhat easy method for converting Roblox builds (consisting of simple primitives) to Blender files, WHILE PRESERVING TRANSPARENCY, REFLECTANCE, AND INDIVIDUAL BLOCKS. Basically, it takes a Roblox build, and converts it into Blender primitives. This can be useful for making pretty renders of Roblox worlds.

If you just need to export a model without transparency or reflectance, you can already export it using existing tools. Note that unlike the tool, you won't be able to manipulate individual blocks upon import.

Currently supports importing blocks, spheres, and cylinders.
Works with transparency, reflectance, and color, but NOT MATERIALS (at least not yet.)


--------

This software is free to use, distribute, modify, etc.
I don't mind

--------

Disclaimer:
By using this code, you (and/or any collaborators that knowingly work alongside you using this code) agree that I, the original creator of this code, and/or the one providing the source code for this code, do not take any responsibility for anything relating to this code, its use, and its outputs, and that anything relating to but not limited to the aforementioned things are your (and/or any collaborators that knowingly work alongside you using this code's) responsibility alone, and not anyone else's. You (and/or any collaborators that knowingly work alongside you using this code) agree that by using this code, you (and/or any collaborators that knowingly work alongside you using this code) become the sole owner of the instance of the code that you use, and that you (and/or any collaborators that knowingly work alongside you using this code) take full responsibility for any behavior or events, including but not limited to damages, disputes, or lawsuits, towards anything including but not limited to you (and/or any collaborators that knowingly work alongside you using this code) or anyone else's person, or any belongings, or any being, or any existing or future concept, or anything, in relation to or as a direct or indirect result this code. By using this code, you (and/or any collaborators that knowingly work alongside you using this code) agree you (and/or any collaborators that knowingly work alongside you using this code) will not use this code for illegal or generally nefarious/detestable purposes. By using this code, you agree you become an independent sole owner and proprietor of the used code.

Use at your own risk.

--------

TUTORIAL:

1) Open a roblox world you own; or perhaps an older public uncopylocked world that you feel quite nostalgic about. This tool is NOT used for copying copylocked worlds, and it is NOT meant to be used for nefarious purposes. Please be respectful while using this tool, especially when using it on another's work. I don't necessarily reccomend copying Roblox worlds for use in projects outside of Blender, since I do not know how Roblox itself will react to that. Using this on something like Roblox's Crossroads is likely okay (don't take my word on this), but you should ask for permission to use this tool for smaller uncopylocked worlds you are not yourself associated with.

2) Create a model; any parts you would like to copy should be inside that model somewhere before you use the tool.

3) Create a new script within the model. In the script, paste the code from Roblox_PartGetter.lua, and hit "Run" or "Start". Make sure to read the script in its entirety, including the comments, before running the world.

4) Once the world is run: Look at the Developer console, and find the big block of text with lots of commas and stuff (You'll know what I mean when you see it), originating from the script you've just created. This is a converted form of your model showing types, positions, orientations, colors, etc. of all the parts you'll be importing into Blender; this will act as a sort of middleman allowing conversion.

5) Copy that block of text that was printed; the one you just found. When pasting it, make sure to format it correctly, so that only the printed block of text, and not anything else, is used as input.
Here is an example of how to format the output correctly:
>The raw output "  00:55:03.335  Block,13,105,172,-176,1,-31,6,1.2,6,0,0,0,0,0;Block,196,40,28,54,1,129,6,1.2,6,0,0,0,0,0;  -  Server - Script:12" should become "Block,13,105,172,-176,1,-31,6,1.2,6,0,0,0,0,0;Block,196,40,28,54,1,129,6,1.2,6,0,0,0,0,0;"
To clarify, you should delete the information about the time from the front, and the positional data at the back, and remove any spaces.

6) Optionally, save that formatted block of text to a text file so that it can be used again. By doing this, you won't have to repeat the former steps in case you lose your progress later on.

7) Open a new Blender project and delete everything in the default scene.

8) In Blender, open up a text editor window (Shift-F11). Click New and create a new text file.

9) Paste the code from Blender_Converter.py into the new text file.

10) On the fifth line, where it says 'inputText = ""', paste the block of text from earlier in between the parenthesis. Make sure to read the script in its entirety, including the comments, before running the code.

11) Hit the arrow button at the top of the screen while in the text editor (looks like >) to run the code. This may take a while for larger builds.

12) Once it finishes, return to the viewport (Shift-F5 by default). The Roblox world should be successfully imported; assuming all the steps were done correctly. It could take a few tries to get it just right.

13) You might need to zoom out. Assuming you see your creation in the viewport, you're done! Switch to the Cycles engine (By clicking the camera looking thingy in the properties menu and changing from Eevee to Cycles) if your imported creation includes transparent or reflective blocks, to see the transparency or reflection.
