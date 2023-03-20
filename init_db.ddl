CREATE EXTENSION "uuid-ossp";

CREATE TABLE IF NOT EXISTS slot (
    id uuid primary key default uuid_generate_v4(),
    name text not null,
    temperature int not null
);

INSERT INTO slot (name, temperature) VALUES ('freezer', -16), ('fridge', 4);

CREATE TABLE IF NOT EXISTS shelf (
    id uuid primary key default uuid_generate_v4(),
    slot_id uuid references slot
);

INSERT INTO shelf (slot_id) SELECT id FROM slot WHERE name='freezer';
INSERT INTO shelf (slot_id) SELECT id FROM slot WHERE name='fridge';
INSERT INTO shelf (slot_id) SELECT id FROM slot WHERE name='fridge';

CREATE TABLE IF NOT EXISTS products (
    id uuid primary key default uuid_generate_v4(),
    name text not null,
    expires date,
    price float,
    shelf_id uuid references shelf
);