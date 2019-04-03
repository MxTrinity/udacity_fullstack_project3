# Python 3.7.2

article_query = '''
SELECT q.title, q.views FROM(
	SELECT 
		SUM(
			CASE
				WHEN log.path = '/article/goats-eat-googles' 
				THEN 1 
				ELSE 0 
			END
		) AS "Goats eat Google's lawn", 
		SUM(
		CASE
			WHEN log.path = '/article/balloon-goons-doomed' 
			THEN 1 
			ELSE 0 
		END
		) AS "Balloon goons doomed", 
		SUM(
			CASE
				WHEN log.path = '/article/trouble-for-troubled' 
				THEN 1 
				ELSE 0 
			END
		) AS "Trouble for troubled troublemakers", 
		SUM(
			CASE
				WHEN log.path = '/article/candidate-is-jerk' 
				THEN 1 
				ELSE 0 
			END
		) AS "Candidate is jerk, alleges rival", 
		SUM(
			CASE
				WHEN log.path = '/article/bears-love-berries' 
				THEN 1
				ELSE 0
			END
		) AS "Bears love berries, alleges bear", 
		SUM(
			CASE
				WHEN log.path = '/article/bad-things-gone' 
				THEN 1
				ELSE 0
			END
		) AS "Bad things gone, say good people", 
		SUM(
			CASE
				WHEN log.path = '/article/so-many-bears' 
				THEN 1 
				ELSE 0 
			END
		)AS "There are a lot of bears", 
		SUM(
			CASE
				WHEN log.path = '/article/media-obsessed-with-bears' 
				THEN 1
				ELSE 0
			END
		) AS "Media obsessed with bears" 

	FROM 
		log
) AS temp JOIN LATERAL (
	VALUES
	('Goats eat Google''s lawn', temp."Goats eat Google's lawn"), 
	('Balloon goons doomed', temp."Balloon goons doomed"), 
	('Trouble for troubled troublemakers', temp."Trouble for troubled troublemakers"), 
	('Candidate is jerk, alleges rival', temp."Candidate is jerk, alleges rival"), 
	('Bears love berries, alleges bear', temp."Bears love berries, alleges bear"), 
	('Bad things gone, say good people', temp."Bad things gone, say good people"), 
	('There are a lot of bears', temp."There are a lot of bears"), 
	('Media obsessed with bears', temp."Media obsessed with bears")) 
	AS q(title, views) 
	
ON TRUE 
ORDER BY 
	q.views DESC
LIMIT 3;
'''

author_query = '''
SELECT ar.name, SUM(q.views::INT) as totals FROM(
	SELECT 
		SUM(
			CASE
				WHEN log.path = '/article/goats-eat-googles' 
				THEN 1 
				ELSE 0 
			END
		) AS "Goats eat Google's lawn", 
		SUM(
		CASE
			WHEN log.path = '/article/balloon-goons-doomed' 
			THEN 1 
			ELSE 0 
		END
		) AS "Balloon goons doomed", 
		SUM(
			CASE
				WHEN log.path = '/article/trouble-for-troubled' 
				THEN 1 
				ELSE 0 
			END
		) AS "Trouble for troubled troublemakers", 
		SUM(
			CASE
				WHEN log.path = '/article/candidate-is-jerk' 
				THEN 1 
				ELSE 0 
			END
		) AS "Candidate is jerk, alleges rival", 
		SUM(
			CASE
				WHEN log.path = '/article/bears-love-berries' 
				THEN 1
				ELSE 0
			END
		) AS "Bears love berries, alleges bear", 
		SUM(
			CASE
				WHEN log.path = '/article/bad-things-gone' 
				THEN 1
				ELSE 0
			END
		) AS "Bad things gone, say good people", 
		SUM(
			CASE
				WHEN log.path = '/article/so-many-bears' 
				THEN 1 
				ELSE 0 
			END
		)AS "There are a lot of bears", 
		SUM(
			CASE
				WHEN log.path = '/article/media-obsessed-with-bears' 
				THEN 1
				ELSE 0
			END
		) AS "Media obsessed with bears" 

	FROM 
		log
) AS temp JOIN LATERAL (
	VALUES
	('Goats eat Google''s lawn', temp."Goats eat Google's lawn"), 
	('Balloon goons doomed', temp."Balloon goons doomed"), 
	('Trouble for troubled troublemakers', temp."Trouble for troubled troublemakers"), 
	('Candidate is jerk, alleges rival', temp."Candidate is jerk, alleges rival"), 
	('Bears love berries, alleges bear', temp."Bears love berries, alleges bear"), 
	('Bad things gone, say good people', temp."Bad things gone, say good people"), 
	('There are a lot of bears', temp."There are a lot of bears"), 
	('Media obsessed with bears', temp."Media obsessed with bears")
) AS q(title, views) 
	
ON TRUE 

INNER JOIN articles a ON a.title = q.title
INNER JOIN authors ar ON ar.id = a.author

GROUP BY ar.name
ORDER BY 
	totals DESC;
'''

log_query = '''
SELECT z.day, cast(q.err as decimal) / z.ok AS ratio
FROM (
	SELECT 
	    date_trunc('day',time) as day, status as stat1, COUNT(*) as OK
	FROM
	    log 
	WHERE
		status = '200 OK'
	GROUP BY
	    day, stat1
) AS z
JOIN (
	SELECT 
    	date_trunc('day',time) as day, status as stat2, COUNT(*) as err
	FROM
    	log 
    WHERE
		status = '404 NOT FOUND'
	GROUP BY
    	day, stat2
) AS q ON z.day = q.day 
WHERE cast(q.err as decimal) / z.ok >= 0.01;
'''