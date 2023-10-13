SELECT TOP 10
    HomeTeam,
    SUM(home_yellow_cards) AS total_home_yellow_cards
FROM (
    SELECT HomeTeam, home_yellow_cards
    FROM laliga
    UNION ALL
    SELECT HomeTeam, home_yellow_cards
    FROM epl
) AS all_teams
GROUP BY HomeTeam
ORDER BY total_home_yellow_cards DESC
