CREATE TABLE IF NOT EXISTS task
(
    task_id     serial PRIMARY KEY,
    name        varchar,
    description varchar,
    dates       varchar not null
);

INSERT INTO task(name, description, dates)
VALUES ('name1', 'description1', '["2023-10-25T00:00:00Z", "2023-10-25T02:00:00Z", "2023-10-25T03:00:00Z", "2023-10-25T05:00:00Z"]'),
       ('name2', 'description2', '["2023-10-26T08:00:00Z", "2023-10-26T12:00:00Z", "2023-10-26T13:00:00Z", "2023-10-26T18:00:00Z"]');