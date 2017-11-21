CREATE DATABASE omapeli; 
use omapeli; 
CREATE TABLE Room(
PositionID INT(12) NOT NULL, 
RoomN VARCHAR(20), 
RoomDescr VARCHAR(20),
PRIMARY KEY (PositionID));

CREATE TABLE Player(
PositionID INT(12) NOT NULL, 
PlayerN VARCHAR(20), 
FOREIGN KEY (PositionID) REFERENCES TO Room(PositionID)); 

CREATE TABLE NPC(
NPCID INT(12), 
isAlive INT(5), 
NPCN VARCHAR(20), 
PositionID INT(12), 
FOREIGN KEY (PositionID) REFERENCES TO Room(PositionID)); 

