BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"username"	varchar(20) NOT NULL UNIQUE,
	"email"	varchar(25) UNIQUE,
	"password"	varchar(30) NOT NULL,
	PRIMARY KEY("username")
);
CREATE TABLE IF NOT EXISTS "blog_comment" (
	"comment_id"	INTEGER NOT NULL,
	"comment_author"	varchar(20),
	"user"	varchar(20),
	"post_id"	INTEGER,
	"comment"	varchar(30) NOT NULL,
	"created_date"	datetime,
	PRIMARY KEY("comment_id")
);
CREATE TABLE IF NOT EXISTS "drafts" (
	"draft_id"	INTEGER,
	"user"	varchar(20),
	"author_name"	varchar(20),
	"title"	varchar(20) NOT NULL,
	"draft"	varchar(200) NOT NULL,
	"created_date"	datetime,
	PRIMARY KEY("draft_id")
);
CREATE TABLE IF NOT EXISTS "contact" (
	"user_id"	varchar(20) NOT NULL,
	"phone_number"	varchar(10) NOT NULL,
	"email"	varchar(20) NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "user"("username")
);
CREATE TABLE IF NOT EXISTS "blog_post" (
	"post_id"	INTEGER UNIQUE,
	"post"	varchar(200) NOT NULL,
	"author_name"	varchar(20),
	"user"	varchar(20),
	"title"	varchar(40) NOT NULL,
	"created_date"	datetime,
	"published_date"	datetime,
	FOREIGN KEY("user") REFERENCES "user"("username") ON DELETE CASCADE,
	PRIMARY KEY("post_id")
);
COMMIT;
