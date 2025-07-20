SELECT table_schema || '.' || table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');

Select * from blogger_post;
Select * from blogger_author;
select * from django_migrations;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE';
  
  
SELECT * FROM AUTH_PERMISSION;
SELECT * FROM AUTHTOKEN_TOKEN;
SELECT * FROM AUTH_USER;
delete from blogger_post where id=1;

-- SQL to manually create the 'blogger_author' table
CREATE TABLE blogger_author (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email_id VARCHAR(254) NOT NULL UNIQUE, -- Assuming email_id should be unique
    address VARCHAR(255) NOT NULL
);

-- SQL to manually create the 'blogger_post' table
CREATE TABLE blogger_post (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    slug VARCHAR(250) NOT NULL,
    body TEXT NOT NULL,
    publish TIMESTAMPTZ NOT NULL DEFAULT NOW(), -- Sets default to current timestamp with timezone
    created TIMESTAMPTZ NOT NULL DEFAULT NOW(), -- Sets default to current timestamp with timezone
    updated TIMESTAMPTZ NOT NULL DEFAULT NOW(), -- Sets default to current timestamp with timezone
    status VARCHAR(2) NOT NULL,
    author_id BIGINT NOT NULL, -- This column will store the foreign key to blogger_author
    -- Add the foreign key constraint
    CONSTRAINT blogger_post_author_id_fk FOREIGN KEY (author_id) REFERENCES blogger_author (id) ON DELETE CASCADE
);

-- SQL to add indexes for 'blogger_post'
-- This index matches `ordering = ['-publish']` and `indexes = [models.Index(fields=['-publish'])]`
CREATE INDEX blogger_post_publish_idx ON blogger_post (publish DESC);

-- For `slug = models.SlugField(max_length=250, unique_for_date='publish')`
-- Django creates a unique constraint on (slug, the date part of publish).
-- Manually, this is slightly complex but typically looks like this for PostgreSQL:
CREATE UNIQUE INDEX blogger_post_slug_publish_date_uniq
ON blogger_post (slug, DATE_TRUNC('day', publish));


for post in posts:
print(f"ID: {post.id}")
print(f"Title: {post.title}")
print(f"Content: {post.body}") 
print(f"Created at: {post.created}")
print(f"Publish at: {post.publish}")
print(f"Slug for: {post.slug}")
print(f"Updated for: {post.updated}")
print(f"Status for: {post.status}")	
print('---------------------------')