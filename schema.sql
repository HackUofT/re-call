drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	event_title text not null,
	event_time text not null,
	event_reminder_time text not null,
	event_reminder_num text not null
);