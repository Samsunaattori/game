CREATE DATABASE omapeli; 
use omapeli; 
CREATE TABLE Room(
PositionID INT(12) NOT NULL, 
RoomN VARCHAR(20), 
RoomDescr VARCHAR(MAX),
PRIMARY KEY (PositionID));

CREATE TABLE Player(
PlayerID INT(12),
PositionID INT(12) NOT NULL, 
PlayerN VARCHAR(20), 
PRIMARY KEY (PlayerID),
FOREIGN KEY (PositionID) REFERENCES TO Room(PositionID)); 

CREATE TABLE NPC(
NPCID INT(12), 
isAlive INT(5), 
NPCN VARCHAR(20), 
PositionID INT(12), 
PRIMARY KEY (NPCID),
FOREIGN KEY (PositionID) REFERENCES TO Room(PositionID)); 

CREATE TABLE Connection(
Direction VARCHAR(20),
isLocked INT(5), 
RoomFrom INT(12), 
RoomTo INT(12), 
FOREIGN KEY (RoomTo) REFERENCES TO Room(PositionID), 
FOREIGN KEY (RoomFrom) REFERENCES TO Room(PositionID)); 

CREATE TABLE Container(
ContainerID INT(12),
ContainerN VARCHAR(20), 
ContainerDescr VARCHAR(MAX),
ContainerPosition INT(12), 
PRIMARY KEY (ContainerID),
FOREIGN KEY (ContainerPosition) REFERENCES TO Room(PositionID));

CREATE TABLE Item(
ItemID INT(12), 
NPCID INT(12),
ContainerID INT(12), 
ItemPosition INT(12),
PlayerID INY(12), 
ItemN VARCHAR(20), 
ItemDescr VARCHAR(MAX), 
PRIMARY KEY (ItemID), 
FOREIGN KEY (NPCID) REFERENCES TO NPC(NPCID),
FOREIGN KEY (ContainerID) REFERENCES TO Container(ContainerID), 
FOREIGN KEY (ItemPosition) REFERENCES TO Room(PositionID), 
FOREIGN KEY (PlayerID) REFERENCES TO Player(PlayerID)); 

CREATE TABLE OpeningItem(
ItemID INT(12), 
ContainerID INT(12), 
FOREIGN KEY (ItemID) REFERENCES TO Item(ItemID), 
FOREIGN KEY (ContainerID) REFERENCES TO Container(ContainerID));

CREATE TABLE TalkingItem(
NPCID INT(12), 
ItemID INT(12), 
FOREIGN KEY (NPCID) REFERENCES TO NPC(NPCID), 
FOREIGN KEY (ItenID) REFERENCES TO Item(ItemID));



