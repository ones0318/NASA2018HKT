# Go! polar bears!
## Concept

Global warming has had a huge impact on the environment, climate, and ecology of the North Pole.

---

## Level Design
In the game, you can become a polar bear of different ages as you go on various quests to explore the Arctic of 2010 to 2018.
### Level 1
#### Level Background
The ecological system is balance and stable.  Arctic Circle is full of sea ice and various creatures.  Polar bears live in excellent condition and stand on top of the food chain here.
#### Game Play
Player acts as a baby polar bear.  Just walk around to explore the fascinating polar nature spectacle.  Don't leave mother bear too far away, and you'll complete this level.

### Level 2
#### Level Background
Global warming has changed the environment of the polar circle dramatically.  Polar bears' activities are restricted by the decreasing sea ice.  It is full of hunger adults who will even hunt the helpless youngs in the polar bear group now.
#### Game Play
Player acts as a mother polar bear.  You not only must hunt seals to feed bady bear, but also protect baby bear from other hungry adults.  Baby bear is hard to survive in the difficult situation.  Once the baby bear is gone, you'll enter the final level!!!

### Level 3
#### Level Background
The living condition is getting worse continually.  A few years later, there's only one polar bear lives in the area.
#### Game Play
Player acts a lonely, hungry, and elderly polar bear.  The sky is same as its childhood, but everything else has changed ...

---

## Real World Scene Selection
We choose a bay located in North-West Canada as the region that we present in the game.
https://polarbearsinternational.org/climate-change/status-endangered-polar-bears/
We learned that the polar bear population is declining in 3 areas of Arctic, including Baffin Bay, Kane Basin and S.Beaufort Sea.

We picked some area on the map randomly and dumped historical images in EOSDIS Worldview.  We also noticed the location is perfect to present the changement of climate, ice-free & land ratio.

The region, which we present in the game is in the square of (69.6939, -122.5727) and (72.4091, -128.5392).

![](https://)




## landscape model
pick 3~4 years to demostrate here

To perform different age of polar bears and environment change, we selectd aerial photo map of year 2000, 2006, 2010, 2016 as different game level's terrain and landscape.


To generate the landscape model for 3D program (for example: Unity)
We have to transform the DEM or image into support format. 

For DEM (GeoTiff) file transform into STL file, you can reference this repo:


For areial photo image transform into gaming terrain object, you can reference this repo design and implement by our team：

this could help you transform image file (jpg/png) into gradient raw file and import to Unity terrain object.

The generated terrain package file is in the folder: 
    assets/terrains/arctic/year_map.raw
    





## Polar bear distribution
For polar bear distribution, we can reference following information to estimate how much polar bear will appear in the area.

* Polarbears International https://polarbearsinternational.org/
* IUCN PBSG (PolarBear Specialist Group) http://pbsg.npolar.no/

The reference data of polar bear's population could be found in following page
http://pbsg.npolar.no/en/status/populations/southern-beaufort-sea.html

Per our design, the region we selected is in Southern Beaufort Sea area, 
where the population includes 1,526 polar bears in 2016, but 907 in 2010, and removal 83 per year between 2010 to 2014.


For overall polar bear status of different area in Arctic are present in following page: 
PBSG - Polar Bear Population Map : http://pbsg.npolar.no/en/status/population-map.html
Map of Life - Species Distribution Map : https://mol.org//species/Ursus_maritimus


## Other Species Distribution
The polar cycle's ecology system can be found in this website. 

To implement complete food chain for polar bear, 
We import/modified following 3D models into the game:
* Seal (Ringed Seal)
* Cow 
* Deer 
* Whale
* Fish

When hunting is good and a polar bear's body is in good condition, the bear may eat only the seal's blubber and skin.
Therefore, we also survey the Ringed Seal's population in S.Beaufult Sea Area, is also declining.

* Marine Mammal Laboratory - Polar Ecosystems Program: Ice Seal Distribution Data
https://www.afsc.noaa.gov/NMML/polar/research/ice_seal_distribution.php

NOAA Fishers - Marine Mammal Stock Assessment Reports by Species/Stock
https://www.fisheries.noaa.gov/national/marine-mammal-protection/marine-mammal-stock-assessment-reports-species-stock#pinnipeds---phocids-(earless-seals-or-true-seals)



Beside the marine mammal species, we also suggested to implement the vegetation distribution
We found NASA have simple data of telemetry:

https://www.nasa.gov/feature/goddard/2016/nasa-studies-details-of-a-greening-arctic

The data could be implement as texture of terrain models, or generating gameobject by script.
