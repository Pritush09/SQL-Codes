# From lucid hart

#CREATE TABLE `Customer` (
#  `Cid` integer,
#  `name` varchar(255),
#  `email` varchar(255),
#  `phone` varchar(10),
#  PRIMARY KEY (`Cid`)
#);

#CREATE TABLE `Food` (
#  `fid` integer,
#  `name` varchar(255),
#  `price` integer,
#  `type` boolean,
#  PRIMARY KEY (`fid`)
#);

#CREATE TABLE `Restruants` (
#  `Rid` integer,
#  `name` varchar(255),
#  `rating` decimal,
#  `address` text,
#  PRIMARY KEY (`Rid`)
#);

#CREATE TABLE `Orders` (
#  `Oid` integer,
#  `Cid` integer,
# `Rid` integer,
#  `time` datetime,
#  PRIMARY KEY (`Oid`),
#  FOREIGN KEY (`Rid`) REFERENCES `Customer`(`Cid`)
#);
