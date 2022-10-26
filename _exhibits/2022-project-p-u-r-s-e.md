---
# note: title, description, image are used for SEO

title: "Project P.U.R.S.E."
slug: project-p-u-r-s-e
permalink: /exhibits/project-p-u-r-s-e/
exhibit-id: 22-113
exhibit-zone: "Opportunity"
space-number: "OC13"
description: "Programmable Unattended Retrieval and Storage Experience.
An open source storage system for makers!"
description-long: "Every maker ends up with extras after a project. Like hotdogs and hotdog buns, there always seem to be some spares left over. Over time, these spares piled up and I started buying parts I already had simply because I forgot I already had them. I tried many different approaches to organization from shoe boxes to storage totes, divider bins to tackle boxes. Finally, I decided I had to make my own storage system inspired by the best available: a purse.

I needed a system that allowed me to have removable bins to store any small items I wanted. It needed to allow me to easily find any stored item knowing that I&#039;d always forget both where I stored it and what it was called. Finally, it had to be simple to put new items into the system. 

Everything started in CAD. First task was to design a series of bins that are easy and fast to 3d print. These bins are in a range of sizes - 1x1, 1x2, 2x2, etc.This allows you to use the right size bin with no wasted space. These bins have a little tab for a barcode label as well - this is important later.

Now that we have our bins, we have to put them somewhere. Solving this involved creating a large cabinet with drawers sized to fit all the various bins. With that done, we have bins in drawers but none of the secret sauce that really makes it work.

I never remember where I put things so I need a computer to help me: a Raspberry Pi in this case. The Pi can’t do much on its own though so we need an application. I wrote a Java database application (open source of course) that understands the concept of items, tags, bins, and drawers. Items are what you want to store. Tags are simply “terms” you associate with items so you can search for them. Bins are where you put the items and drawers are where you put the bins. Bins have a label on them so they can be identified. The bins in drawers have a location defined by row and column that indicates the position. 

At this point, the application knows that bin 18 contains 2” long 4-40 socket cap screws and is located in drawer A at row 5, column 12. This would work and you could stop here but this is brittle in practice. If you take out a bin and put it back in the wrong place everything falls apart.

Fixing this problem is where the project starts going over the top. I want the application to know where the bins are located even when I put them back in the wrong place. I want things to “just work” for me. To fix this, we need the application to be able to determine the bin location on its own. This means computer vision. I ended up choosing ESP32-CAM as the basis for this based on simplicity and price. 

First off, we need a way to move the camera back and forth over the drawers. One option is for the camera itself to transit over the entire drawer; left to right, front to back. This makes for a bit more complex assembly overally. Another option is for the camera to move left and right and for the drawer itself to move in and out. This second option makes for less moving parts which keeps things a bit simpler. I settled on ACME lead screws, A4988 stepper drivers, and NEMA 17 stepper motors. All of these are off-the-shelf 3d printer parts and readily available. To control the motors I chose ESP32 boards, again for simplicity and price. 

So now we have the camera able to “see” everything in the drawer via a combination of the drawer and camera moving. How do we get the camera to recognize a bin? We use that barcode label on the bins we talked about earlier. 

At this point we’re done! Kinda. The controller application on the Raspberry Pi needs to be able to actually control everything. I decided to have the controller be all the brains and the ESP32s are only used to take a photo and for motion. The Pi acts as a WIFI hotspot and all the remote microcontrollers connect to it. Each ESP32 has an application on it that exposes a REST interface that can be used to ask it to home an axis and to move to a given location. The ESP32-CAM exposes an endpoint to take a photo. 

The controller now has all it needs to know what item is where and, most importantly, to audit everything stored inside. To find something you want, you use the UI to search for it. You get a list of everything matching your search and can even see a picture of what is in the bin. Once you pick what you want, the drawer you need opens and you grab the part or bin and get to work. When you are ready, you can ask the system what spots are empty for a given bin or you can just throw it anywhere you want and tell the system to run an audit.

So there you have it, how I built a P.U.R.S.E. 
"
image: /assets/images/exhibit-images/22-113-exhibit-project-p-u-r-s-e-title-shot-large.jpg
image-primary: 
  small: /assets/images/exhibit-images/22-113-exhibit-project-p-u-r-s-e-title-shot-small.jpg
  medium: /assets/images/exhibit-images/22-113-exhibit-project-p-u-r-s-e-title-shot-medium.jpg
  large: /assets/images/exhibit-images/22-113-exhibit-project-p-u-r-s-e-title-shot-large.jpg
  full: /assets/images/exhibit-images/22-113-exhibit-project-p-u-r-s-e-title-shot-full.jpg
additional-images: 
  - 1:
    small: /assets/images/exhibit-images/22-113-exhibit-addl1-project-p-u-r-s-e-basic-wiring-diagram-small.JPG
    medium: /assets/images/exhibit-images/22-113-exhibit-addl1-project-p-u-r-s-e-basic-wiring-diagram-medium.JPG
    large: /assets/images/exhibit-images/22-113-exhibit-addl1-project-p-u-r-s-e-basic-wiring-diagram-large.JPG
    full: /assets/images/exhibit-images/22-113-exhibit-addl1-project-p-u-r-s-e-basic-wiring-diagram-full.JPG
  - 2:
    small: /assets/images/exhibit-images/22-113-exhibit-addl2-project-p-u-r-s-e-bin-drawing-small.JPG
    medium: /assets/images/exhibit-images/22-113-exhibit-addl2-project-p-u-r-s-e-bin-drawing-medium.JPG
    large: /assets/images/exhibit-images/22-113-exhibit-addl2-project-p-u-r-s-e-bin-drawing-large.JPG
    full: /assets/images/exhibit-images/22-113-exhibit-addl2-project-p-u-r-s-e-bin-drawing-full.JPG
  - 3:
    small: /assets/images/exhibit-images/22-113-exhibit-addl3-project-p-u-r-s-e-bin-group-small.JPG
    medium: /assets/images/exhibit-images/22-113-exhibit-addl3-project-p-u-r-s-e-bin-group-medium.JPG
    large: /assets/images/exhibit-images/22-113-exhibit-addl3-project-p-u-r-s-e-bin-group-large.JPG
    full: /assets/images/exhibit-images/22-113-exhibit-addl3-project-p-u-r-s-e-bin-group-full.JPG
  - 4:
    small: /assets/images/exhibit-images/22-113-exhibit-addl4-project-p-u-r-s-e-design-progress-small.jpg
    medium: /assets/images/exhibit-images/22-113-exhibit-addl4-project-p-u-r-s-e-design-progress-medium.jpg
    large: /assets/images/exhibit-images/22-113-exhibit-addl4-project-p-u-r-s-e-design-progress-large.jpg
    full: /assets/images/exhibit-images/22-113-exhibit-addl4-project-p-u-r-s-e-design-progress-full.jpg
website: "https://github.com/mikegrundvig/ProjectPurse"
maker: 
  name: "Michael Grundvig"
  description: "I have always enjoyed making things. As a kid, it was model rockets and taking broken appliances apart. When I became an adult, it was radio controlled helicopters, drones and 3D printing. I love the intersection of software, electronics, and mechanics. These days my projects are usually quirky while still serving some sort of real-world purpose."
  image-primary: /assets/images/exhibit-images/22-113-maker-project-p-u-r-s-e-family-at-craters-medium.jpg
categories: 
  - slug: automation
    name: Automation
  - slug: engineering
    name: Engineering
  - slug: invention
    name: Invention
  - slug: raspberry-pi
    name: Raspberry Pi
  - slug: tools
    name: Tools
created-jotform: "2022-08-31 01:00:49"
last-modified-jotform: "2022-10-24 21:21:12"
last-exported: "2022-10-25 06:31:29"
sitemap: false

---
