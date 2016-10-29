Drop table sentiment;
CREATE TABLE sentiment (
  index varchar(5) NOT NULL,
  name varchar(80) NOT NULL,
  sentiment char(15) NOT NULL,
  PRIMARY KEY (name)
);
COPY sentiment FROM '/Users/almcmoran1/DSCI6007-student/Data_Engineering_Project/data/pitchers_2016_06_26_sentiment.csv' (FORMAT csv);

COPY sentiment FROM '/Users/almcmoran1/DSCI6007-student/Data_Engineering_Project/data/batters_2016_06_26_sentiment.csv' (FORMAT csv);


drop table dk_stats;
CREATE TABLE dk_stats (
  position varchar(5) NOT NULL,
  name varchar(80) NOT NULL,
  salary bigint NOT NULL,
  game_info varchar(80),
  avg_pts_per_game real,
  team_abbrv varchar(5),
  PRIMARY KEY (name)
);
COPY dk_stats FROM '/Users/almcmoran1/DSCI6007-student/Data_Engineering_Project/data/DKSalaries_2016_06_26.csv' CSV HEADER;
DROP TABLE pitcher_stats;
CREATE TABLE pitcher_stats (
  index bigint NOT NULL,
  name varchar(80) NOT NULL,
  team varchar(5) NOT NULL,
  games smallint,
  innings_pitched real,
  starts smallint,
  qual_starts smallint,
  qual_starts_percent real,
  k_to_bb real,
  k_to_9_ip real,
  bb_to_9_ip real,
  hr_9_ip real,
  bat_avg_balls_ip real,
  strand_rate real,
  fb_vlo real,
  era real,
  fid real,
  PRIMARY KEY (name, team)
  );
  
  
  COPY pitcher_stats FROM '/Users/almcmoran1/DSCI6007-student/Data_Engineering_Project/data/pitchers_2016_06_26_clean.csv' CSV HEADER;
  
DROP TABLE batter_stats;
CREATE TABLE batter_stats (
  index bigint NOT NULL,
  name varchar(80) NOT NULL,
  team varchar(5) NOT NULL,
  position varchar(5),
  games smallint,
  abs smallint,
  pitches_per_ab real,
  bunts smallint,
  hit_into_dp smallint,
  int_walks smallint,
  walks smallint,
  strike_outs smallint,
  walk_rate real,
  w2so_ratio real,
  contact_rate real,
  stolen_base_o real,
  avg real,
  avg_on_bip real,
  PRIMARY KEY (name, team)
  );
COPY batter_stats FROM '/Users/almcmoran1/DSCI6007-student/Data_Engineering_Project/data/batters_2016_06_26_clean.csv' CSV HEADER;  
select count(*) from sentiment;
select * from dk_stats;

select batters.*, dk.salary, dk.avg_pts_per_game, sent.sentiment from batter_stats as batters left outer join dk_stats as dk on batters.name = dk.name left outer join sentiment as sent on batters.name = sent.name;

select pitchers.*, dk.salary, dk.avg_pts_per_game, sent.sentiment from pitcher_stats as pitchers left outer join dk_stats as dk on pitchers.name = dk.name left outer join sentiment as sent on pitchers.name = sent.name;