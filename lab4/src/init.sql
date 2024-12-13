create schema if not exists ocr;


create table if not exists ocr.user_requests (
    mytable_key serial primary key,
    user_id integer not null,
    hash_value varchar,
    text_result varchar,
    created_at timestamp without time zone not null default (current_timestamp at time zone 'utc')
);