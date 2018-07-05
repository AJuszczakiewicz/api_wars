CREATE TABLE users (
id serial NOT NULL PRIMARY KEY,
username text,
password text
);

CREATE TABLE planet_votes (
id serial NOT NULL PRIMARY KEY,
planet_id integer,
planet_name text,
user_id integer ,
submission_time integer
);

ALTER TABLE ONLY planet_votes
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);