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

INSERT INTO Room VALUES (212, "LIbrary", "The library is furnished in a very old classical style. It has a couple of leather sofas and a black grand piano.");
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

INSERT INTO NPC VALUES (1, 1, "Rat", 113); 

INSERT INTO Container VALUES (1, "Top shelf in the kitchen", "A closed shelf that Tim cannot reach without help, or a stool.", 123); 
INSERT INTO Container VALUES (2, "A crack in the guard tower", "One of the guard towers walls has a small crack that Tim can examine and reach with a stool.", 231); 
INSERT INTO Container VALUES (3, "A hay stack in the horse stable", "There is a hay stack in the corner of the horse stable", 111); 

