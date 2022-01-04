--Create a model with any parts you'd like to copy in it.
--Place this script within that model, then in Studio, test the game.
--Copy the output from the console and trim off any junk from the edges. 
--You should have "Block","Cube", or "Cylinder" at the front, and a ";" at the end of the output for the parser to work correctly.
--Note that it is a house of cards and will probably break if the input is not correctly sanitized -- if something goes wrong, it's probably caused by a misformatted input.
local things = script.Parent:GetDescendants()
local parts = {}
for ind, thing in ipairs(things) do
	if thing:IsA("Part") and thing.Name ~= "Terrain" then
		table.insert(parts,thing)
	end
end
local OutStr = ""
for ind, thing in ipairs(parts) do
	OutStr = OutStr .. string.sub(tostring(thing.shape),15) .. "," .. tostring(math.round(thing.color.R*255)) .. "," .. tostring(math.round(thing.color.G*255)) .. "," .. math.round(thing.color.B*255) .. "," .. tostring(math.round(thing.position.X*100)/100) .. "," .. tostring(math.round(thing.position.Y*100)/100) .. "," .. tostring(math.round(thing.position.Z*100)/100) .. "," .. tostring(math.round(thing.size.X*100)/100) .. ",".. tostring(math.round(thing.size.Y*100)/100) .. ",".. tostring(math.round(thing.size.Z*100)/100) .. "," .. tostring(math.round(thing.Orientation.X*100)/100) .. "," .. tostring(math.round(thing.Orientation.Y*100)/100) .. "," .. tostring(math.round(thing.Orientation.Z*100)/100) .. "," .. tostring(math.round(thing.transparency*100)/100) .. "," .. tostring(math.round(thing.reflectance*100)/100) .. ";"
end
print(OutStr)