DROP DATABASE IF EXISTS omapeli; 
CREATE DATABASE omapeli; 
use omapeli; 

DROP TABLE IF EXISTS TalkingItem; 
DROP TABLE IF EXISTS OpeningItem; 
DROP TABLE IF EXISTS Item; 
DROP TABLE IF EXISTS Container; 
DROP TABLE IF EXISTS Connect; 
DROP TABLE IF EXISTS NPC; 
DROP TABLE IF EXISTS Player; 
DROP TABLE IF EXISTS Room; 

CREATE TABLE Room(
PositionID INT(12) NOT NULL, 
RoomN VARCHAR(20), 
RoomDescr VARCHAR(8000),
PRIMARY KEY (PositionID));

CREATE TABLE Player(
PlayerID INT(12),
PositionID INT(12) NOT NULL, 
PlayerN VARCHAR(20), 
PRIMARY KEY (PlayerID),
FOREIGN KEY (PositionID) REFERENCES Room(PositionID)); 

CREATE TABLE NPC(
NPCID INT(12), 
isAlive INT(5), 
NPCN VARCHAR(20), 
PositionID INT(12), 
PRIMARY KEY (NPCID),
FOREIGN KEY (PositionID) REFERENCES Room(PositionID)); 

CREATE TABLE Connect(
Direction VARCHAR(20),
isLocked INT(5), 
RoomFrom INT(12), 
RoomTo INT(12), 
FOREIGN KEY (RoomTo) REFERENCES Room(PositionID), 
FOREIGN KEY (RoomFrom) REFERENCES Room(PositionID)); 

CREATE TABLE Container(
ContainerID INT(12),
ContainerN VARCHAR(20), 
ContainerDescr VARCHAR(8000),
ContainerPosition INT(12), 
PRIMARY KEY (ContainerID),
FOREIGN KEY (ContainerPosition) REFERENCES Room(PositionID));

CREATE TABLE Item(
ItemID INT(12), 
NPCID INT(12),
ContainerID INT(12), 
ItemPosition INT(12),
PlayerID INT(12), 
ItemN VARCHAR(20), 
ItemDescr VARCHAR(8000), 
PRIMARY KEY (ItemID), 
FOREIGN KEY (NPCID) REFERENCES NPC(NPCID),
FOREIGN KEY (ContainerID) REFERENCES Container(ContainerID), 
FOREIGN KEY (ItemPosition) REFERENCES Room(PositionID), 
FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID)); 

CREATE TABLE OpeningItem(
ItemID INT(12), 
ContainerID INT(12), 
FOREIGN KEY (ItemID) REFERENCES Item(ItemID), 
FOREIGN KEY (ContainerID) REFERENCES Container(ContainerID));

CREATE TABLE TalkingItem(
NPCID INT(12), 
ItemID INT(12), 
FOREIGN KEY (NPCID) REFERENCES NPC(NPCID), 
FOREIGN KEY (ItemID) REFERENCES Item(ItemID)); 

INSERT INTO Room VALUES (212, "Library", "The library is furnished in a very old classical style. It has a couple of leather sofas and a black grand piano.");
INSERT INTO Room VALUES (213, "Clothing Room", "The clothing room has a lot of shelves and clothes hanging."); 
INSERT INTO Room VALUES (222, "Corridor", "The corridor has a dark purple carpet goes all the way across the hallway. The corridor has multiple lit candles that create a dim and warm lighting. ");
INSERT INTO Room VALUES (223, "Tim's Bedroom", "The bedroom contains a window that the light shines through, a desk and a bed."); 
INSERT INTO Room Values (231, "Guard Tower", "The guard tower’s walls are made of rock and have a couple of torches lighting it up. One of the guard towers walls has a small crack."); 
INSERT INTO Room VALUES (232, "2nd floor stairs", "The stairs are wooden and have a golden colored railing."); 
INSERT INTO Room VALUES (111, "Horse Stable", "The horse stable had a horse, but for one reason or another it is not there anymore. There is a stool next to the wall."); 
INSERT INTO Room VALUES (112, "Living Room", "Living room has a few large couches and a huge table that is used for dining. There is also a fireplace that is empty, and on top of the fireplace is a painting of uncle Stephenson the puzzle maker."); 
INSERT INTO Room VALUES (113, "Storage Room", "Storage room used to have all kinds of foods and steam powered equipment in it, but now it seems empty. There is only a hole on the wall, that is probably made by a mouse or a rat."); 
INSERT INTO Room VALUES (121, "Front Yard", "The front yard is a large, barely maintained piece of grassfield. The gate is located on the west side of it, and it needs the gate key to be opened."); 
INSERT INTO Room VALUES (122, "Hall", "The hall has a high ceiling, big windows and a stone flooring. The hall is lit up by a big copper chandelier with candles that is hanging from the ceiling."); 
INSERT INTO Room VALUES (123, "Kitchen", "Kitchen is a room where Tim wasn’t allowed to go alone. There was too many sharp objects that could hurt the young boy, but now it didn’t seem to have much left in it. There is only a butter knife on the table, and a closed shelf that he cannot reach."); 
INSERT INTO Room VALUES (132, "1st floor stairs", "The stairs are wooden and have a golden colored railing."); 

INSERT INTO Player VALUES (1, 223, "Tim"); 

INSERT INTO NPC VALUES (1, 1, "rat", 113); 

INSERT INTO Container VALUES (1, "shelf", "A closed shelf that Tim cannot reach without help, or a stool.", 123); 
INSERT INTO Container VALUES (2, "crack", "One of the guard towers walls has a small crack that Tim can examine and reach with a stool.", 231); 
INSERT INTO Container VALUES (3, "haystack", "There is a hay stack in the corner of the horse stable", 111); 

INSERT INTO Item VALUES (1, null, null, 212, null, "book", "There is a thick and old looking book on the piano of the library. It appears to be written by a man named Stephenson."); 
INSERT INTO Item VALUES (2, null, null, 213, null, "sword", "Between the clothes there is a small silver colored sword."); 
INSERT INTO Item VALUES (3, null, 2, null, null, "potion", "A magic potion that allows the user to speak to animals");
INSERT INTO Item VALUES (4, null, null, 111, null, "stool", "A small wooden stool."); 
INSERT INTO Item VALUES (5, null, 3, null, null, "needle", "A small metallic needle"); 
INSERT INTO Item VALUES (6, null, null, 112, null, "painting", "There is a painting with copper colored frames hanging on one of the walls in the living room. It appears to portray a man named mr. Stephenson."); 
INSERT INTO Item VALUES (7, null, 1, null, null, "cheese", "A piece of cheese."); 
INSERT INTO Item VALUES (8, null, null, 123, null, "knife", "An ordinary butter knife."); 
INSERT INTO Item VAlues (9, 1, null, null, null, "drink", "A magic drink that the rat gave Tim."); 
INSERT INTO Item VALUES (10, 1, null, null, null, "key", "This key will open the front gate of the castle's yard."); 


INSERT INTO TalkingItem VALUES (1, 3); 
INSERT INTO OpeningItem VALUES (4, 1); 
INSERT INTO OpeningItem VALUES (4, 2); 

INSERT INTO Connect VALUES ("s", null, 212, 222); 
INSERT INTO Connect VALUES ("e", null, 222, 223); 
INSERT INTO Connect VALUES ("n", null, 222, 212); 
INSERT INTO Connect VALUES ("s", null, 222, 232); 
INSERT INTO Connect VALUES ("n", null, 223, 213); 
INSERT INTO Connect VALUES ("w", null, 223, 222); 
INSERT INTO Connect VALUES ("s", null, 213, 223); 
INSERT INTO Connect VALUES ("w", null, 232, 231); 
INSERT INTO Connect VALUES ("d", null, 232, 132); 
INSERT INTO Connect VALUES ("n", null, 232, 222); 
INSERT INTO Connect VALUES ("e", null, 231,232); 

INSERT INTO Connect VALUES ("u", null, 132,232); 
INSERT INTO Connect VALUES ("n", null, 132, 122); 
INSERT INTO Connect VALUES ("n", null, 122, 112); 
INSERT INTO Connect VALUES ("e", null, 122, 123); 
INSERT INTO Connect VALUES ("w", 1, 122, 121); 
INSERT INTO Connect VALUES ("s", null, 122, 132); 
INSERT INTO Connect VALUES ("n", null, 123, 113); 
INSERT INTO Connect VALUES ("w", null, 123, 122); 
INSERT INTO Connect VALUES ("s", null, 113, 123); 
INSERT INTO Connect VALUES ("s", null, 112, 122);
INSERT INTO Connect VALUES ("n", null, 121, 111); 
INSERT INTO Connect VALUES ("e", 1, 121, 122); 
INSERT INTO Connect VALUES ("s", null, 111, 121); 

