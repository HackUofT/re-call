drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  audioFile text not null,
  text text not null,
  eventTime text not null,
  eventDate text not null,
  reminderTime text not null,
  reminderDate text not null
);
