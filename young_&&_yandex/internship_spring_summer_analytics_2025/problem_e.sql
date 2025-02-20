-- SQLite 3.31.1
CREATE TABLE logs (
    campaign_id INTEGER,
    verdict TEXT,
    verdict_time TIMESTAMP
);

INSERT INTO logs (campaign_id, verdict, verdict_time) VALUES
(2, 'No', '2025-01-02 14:28:10'),
(1, 'No', '2025-01-02 18:52:57'),
(2, 'Yes', '2025-01-03 00:47:40'),
(1, 'No', '2025-01-03 01:12:32'),
(1, 'Yes', '2025-01-03 05:10:38'),
(1, 'Yes', '2025-01-03 09:19:44'),
(2, 'No', '2025-01-04 11:49:49'),
(1, 'Yes', '2025-01-04 13:29:01'),
(2, 'No', '2025-01-04 16:01:37'),
(1, 'No', '2025-01-04 20:35:31');

SELECT field_date,
       ROUND(AVG(avg_wait_time), 0) AS avg_wait_time
FROM
    (SELECT DATE(verdict_time) field_date,
            CAST(strftime('%s', next_verdict_time) - strftime('%s', verdict_time) AS REAL) / 60 avg_wait_time
    FROM
        (SELECT verdict, verdict_time,
                LEAD(verdict) OVER (PARTITION BY campaign_id ORDER BY verdict_time) next_verdict,
                LEAD(verdict_time) OVER (PARTITION BY campaign_id ORDER BY verdict_time) next_verdict_time
        FROM logs)
    WHERE verdict = 'No' AND next_verdict = 'Yes')
GROUP BY field_date
ORDER BY field_date;