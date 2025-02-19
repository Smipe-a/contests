# A. Yan in the Gym

# B. Computer Game

# C. Curd Bar Day

# D. Robot Vacuum Cleaner

# E. Waiting Time
<table border="1">
  <tr>
    <td>Time limit per test</td>
    <td>1 second</td>
  </tr>
  <tr>
    <td>Memory limit per test</td>
    <td>64Mb</td>
  </tr>
  <tr>
    <td>Input</td>
    <td>Standart input or input.txt</td>
  </tr>
  <tr>
    <td>Output</td>
    <td>Standart output or output.txt</td>
  </tr>
</table>
Analyst Ivan works in an ad campaign moderation service. The automated system sends verdicts: Yes (approval) and No (rejection). If a campaign is rejected, the client can file a complaint with support. The campaign may be unblocked if the automation made a mistake.

<br>

Ivan wants to analyze the average waiting time for campaign approval by day. For example, campaign `5012025` received a rejection on `2024-10-07 12:46:29` and was later approved on `2024-10-07 15:12:49`. The waiting time is 2 hours, 26 minutes, and 20 seconds.
<br>

Ivan has a table named `logs` with the following structure:

```sql
logs (
    campaign_id INTEGER NOT NULL,
    verdict TEXT NOT NULL,
    verdict_time TEXT NOT NULL
);
```
Where `campaign_id` - identifier of the advertising campaign, `verdict` - moderation verdict, can only be 'Yes' or 'No', and `verdict_time` - timestamp of the verdict in the format `YYYY-MM-DD hh:mm:ss`

Let's consider an example:
<table border="1">
  <tr>
    <td><b>campaign_id</b></td>
    <td><b>verdict</b></td>
    <td><b>verdict_time</b></td>
  </tr>
  <tr>
    <td>2</td>
    <td>No</td>
    <td>2025-01-02 14:28:10</td>
  </tr>
  <tr>
    <td>1</td>
    <td>No</td>
    <td>2025-01-02 18:52:57</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Yes</td>
    <td>2025-01-03 00:47:40</td>
  </tr>
  <tr>
    <td>1</td>
    <td>No</td>
    <td>2025-01-03 01:12:32</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Yes</td>
    <td>2025-01-03 05:10:38</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Yes</td>
    <td>2025-01-03 09:19:44</td>
  </tr>
  <tr>
    <td>2</td>
    <td>No</td>
    <td>2025-01-04 11:49:49</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Yes</td>
    <td>2025-01-04 13:29:01</td>
  </tr>
  <tr>
    <td>2</td>
    <td>No</td>
    <td>2025-01-04 16:01:37</td>
  </tr>
  <tr>
    <td>1</td>
    <td>No</td>
    <td>2025-01-04 20:35:31</td>
  </tr>
</table>

Campaign `1` was in rejection from 2025-01-03 01:12:32 to 2025-01-03 05:10:38, and campaign `2` was in rejection from 2025-01-02 14:28:10 to 2025-01-03 00:47:40. That is, we calculate the waiting time from the last 'No' to the next 'Yes', if it exists
<br>

Write an SQLite query that calculates the average waiting time (in minutes) per day. The result should be a table with two columns: `field_date` and `avg_wait_time` (of type REAL, rounded to the nearest whole number). The output table should be sorted in ascending order by `field_date`
<br>

For the example above, the output will be the following table:
<table border="1">
  <tr>
    <td><b>field_date</b></td>
    <td><b>avg_wait_time</b></td>
  </tr>
  <tr>
    <td>2025-01-02</td>
    <td>619.0</td>
  </tr>
  <tr>
    <td>2025-01-03</td>
    <td>238.0</td>
  </tr>
</table>

# F. Which Flower?
