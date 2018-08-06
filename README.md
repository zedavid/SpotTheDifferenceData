# Spot The Difference Data

Beta release of the dataset with data and annotations as described in the the LREC paper below. Access to video and/or audio could be granted upon agreement with the responsible for the corpus maintenance (jdlopes@kth.se).

[LREC 2018 paper](https://github.com/zedavid/SpotTheDifferenceData/blob/master/lrec2018.pdf). 

## Session Naming

<ID_instruction_giver>\_<ID_instruction_follower>\_0\_<id_set_of_secenes>

### Scenes per set

* Set 1: winter, beach and farm
* Set 2: city, church and jungle
* Set 3: sheep, house and ser

### Subjects and conditions

Subjects U1*, U2*, U3*, U4*, U5* and U6* did each set with a different partner.

Subjects U7*, U8*, U9*, U10*, U11* and U12* did all sets with the same partner.

## Files & Code

`sptd.json`: Json file with all sessions a avialable.


`pics`: Pictures used and their respective xml definition.

`src`

  |
 
  +- `picdef.xsd`: XSD definition of the xml picture files
 
  |
  
  +- `picdef.py`: Python class to parse the picture xml files
