# InfoTags - Turning information into easily recognizable images
On a warehouse's storage floor there are many robots that use image recognition on April Tags or QR codes, and I wondered if there was any way I could create one of these custom images myself.

I created a list of the things a robot needs to know while on the production floor about any given package:
- The object/object genre
- Location to where the object needs to go within the factory
- Arrival YMD
- Arrival HMS
- How many minutes until departure

And perhaps the directions to the desined location

To do this I needed to create a formatting system for this information with 0's and 1's, and then convert that binary string into an image

There are a few possible formats for this image, and I will need to do some troubleshooting to find which one is the best
 
