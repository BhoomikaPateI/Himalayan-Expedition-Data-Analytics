CREATE TABLE `Dim_Peaks` (
  `peakid` varchar(255) PRIMARY KEY,
  `pkname` varchar(255),
  `location` varchar(255),
  `heightm` float,
  `heightf` float,
  `himal` varchar(255),
  `region` varchar(255),
  `open` boolean,
  `unlisted` boolean,
  `phost` varchar(255),
  `pstatus` varchar(255),
  `pyear` int,
  `pseason` varchar(255)
);

CREATE TABLE `Dim_Expeditions` (
  `expid` varchar(255) PRIMARY KEY,
  `year` int,
  `season` varchar(255),
  `host` varchar(255),
  `route1` varchar(255),
  `nation` varchar(255),
  `leaders` varchar(255),
  `sponsor` varchar(255),
  `agency` varchar(255),
  `peakid` varchar(255)
);

CREATE TABLE `Fact_Expeditions` (
  `expid` varchar(255),
  `year` int,
  `season` varchar(255),
  `himal` varchar(255),
  `region` varchar(255),
  `nation` varchar(255),
  `Sum_totmembers` int,
  `Sum_smtmembers` int,
  `Sum_mdeaths` int,
  `Avg_Success_Rate` float,
  `Avg_Death_Rate` float,
  `Avg_smtdays` float,
  `Avg_totdays` float,
  `Avg_heightm` float,
  `Count` int,
  `Max_mhighpt` varchar(255)
);

CREATE TABLE `Dim_Members` (
  `id` varchar(255) PRIMARY KEY,
  `expid` varchar(255),
  `membid` varchar(255),
  `fname` varchar(255),
  `lname` varchar(255),
  `sex` varchar(255),
  `yob` int,
  `citizen` varchar(255),
  `residence` varchar(255),
  `occupation` varchar(255),
  `Member_Role` varchar(255)
);

ALTER TABLE `Dim_Expeditions` ADD FOREIGN KEY (`peakid`) REFERENCES `Dim_Peaks` (`peakid`);

ALTER TABLE `Fact_Expeditions` ADD FOREIGN KEY (`expid`) REFERENCES `Dim_Expeditions` (`expid`);

ALTER TABLE `Dim_Members` ADD FOREIGN KEY (`expid`) REFERENCES `Dim_Expeditions` (`expid`);
