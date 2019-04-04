# Python 3.7.2

article_query = '''
 WITH p AS(
 SELECT regexp_replace(path, '/article/', '') as titles
 FROM log
 )

 SELECT articles.title, COUNT(articles.slug)
 FROM p JOIN articles ON p.titles = articles.slug
 GROUP BY articles.title
 ORDER BY COUNT(articles.slug) DESC
 LIMIT 3;
'''

author_query = '''
 WITH p AS(
 SELECT regexp_replace(path, '/article/', '') as titles
 FROM log
 )

 SELECT authors.name, COUNT(articles.slug)
 FROM p JOIN articles ON p.titles = articles.slug
 JOIN authors ON articles.author = authors.id
 GROUP BY authors.name
 ORDER BY COUNT(articles.slug) DESC;
'''

log_query = '''
 SELECT z.day, cast(q.err as decimal) / (z.ok + q.err) AS ratio
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
        status <> '200 OK'
    GROUP BY
        day, stat2
 ) AS q ON z.day = q.day
 WHERE cast(q.err as decimal) / (q.err + z.ok) >= 0.01;
'''
