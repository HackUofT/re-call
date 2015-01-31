drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	eventTitle text not null,
	eventTime text not null,
	eventReminderTime text not null,
	eventReminderNum text not null
);