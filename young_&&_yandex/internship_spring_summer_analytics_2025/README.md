# A. Yan in the Gym

# B. Computer Game
<table border="1">
<tr>
    <td></td>
    <td>All languages</td>
    <td>Python 3.9 (PyPy 7.3.16)</td>
  </tr>
  <tr>
    <td>Time limit per test</td>
    <td>1 second</td>
    <td>1.5 second</td>
  </tr>
  <tr>
    <td>Memory limit per test</td>
    <td>64Mb</td>
    <td>1524Mb</td>
  </tr>
  <tr>
    <td>Input</td>
    <td colspan="2">Standart input or input.txt</td>
  </tr>
  <tr>
    <td>Output</td>
    <td colspan="2">Standart output or output.txt</td>
  </tr>
</table>

Polycarp received an exciting computer game as a birthday gift.

The game consists of $N$ levels. Some levels are connected by $M$ transitions, forming a directed acyclic graph. Completing a level grants a certain non-negative amount of experience points. Some levels have no outgoing transitions - these are the final levels. The game ends when Polycarp completes a final level.

Polycarp is confident that he can reach any level in the game, but he doesn't know the maximum number of experience points he can accumulate before the game ends. Help him determine the answer to this question.

### Input
The first line contains two integers $N$ and $M$ $(1 \leq N \leq 10^5,~N-1 \leq M \leq 10^6)$ - the number of levels and the number of transitions between them, respectively.

The second line contains $N$ integers $a_i$ $(1 \leq i \leq N,~0 \leq a_i \leq 10^6)$ - the amount of experience points awarded for completing the $i$-th level.

The next $M$ lines describe the transitions between levels in the form of pairs $u_i, v_i$ $(1 \leq u_i, v_i \leq N, u_i \neq v_i)$ - meaning that the $i$-th transition leads from level $u_i$ to level $v_i$.

It is guaranteed that every level in the game is reachable from level 1.

### Output
Output a single integer - the maximum amount of experience Polycarp can accumulate while playing the game.

### Example 1
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
1 0
1
</pre>
</td>
    <td>
<pre>
1

</pre>
    </td>
  </tr>
</table>

### Example 2
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
5 5
1 2 3 5 4
1 2
1 3
2 4
3 4
3 5
</pre>
</td>
    <td>
<pre>
9
<br>

<br>

</pre>
    </td>
  </tr>
</table>

### Notes
In the first example, the game consists of only one level, so we complete it and immediately finish the game.

In the second example, the optimal order of completing levels is 1, 3, 4. The total experience gained is 1 + 3 + 5 = 9 points.

# C. Curd Bar Day

As is well known, on Wednesdays, Yandex offices have the so-called 'Curd Bar Day', when various flavored curd bars are placed at coffee points. Perfectionist Vasya, while walking around the floor, noticed that a small coffee point had 9 curd bars, 4 of which contained condensed milk, while the remaining did not. Vasya then reached the large coffee point and was shocked to find that only 5 bars remained there, with just 2 containing condensed milk. To restore order, Vasya quickly ran back to the small coffee point, grabbed 2 bars, and brought them to the large coffee point, placing them among those already there.

Feeling a sense of accomplishment, Vasya returned to his workplace. However, after a moment of thought, he realized that his actions might have disrupted the "correctness" of the situation, at least from the perspective of his colleague Petya. Petya prefers curd bars with condensed milk but always selects them randomly. At that very moment, Petya set out to pick a bar from the large coffee point.

Now, Vasya is plagued by doubt, as he does not remember exactly which two bars he transferred from one coffee point to the other. To find clarity, he is asking for your help in answering the following probability questions:

1. What is the probability that Petya, selecting a random curd bar, will get one with condensed milk, assuming no one else visited the large coffee point between Vasya and Petya?
2. What is the probability that Vasya, in his rush, transferred both bars with condensed milk, given that the bar Petya took was with condensed milk (assuming no one else visited the large coffee point between Vasya and Petya)?
3. What is the probability that Petya, selecting a random curd bar, will get one with condensed milk, given that exactly one person visited the large coffee point between Vasya and Petya and took exactly one bar?

### Output
In each line of the output, print a single number - the answer rounded to four decimal places according to standard mathematical rounding rules. Decimal fractions must be separated by a dot.

Example output:<br>
0.0123<br>
0.3456<br>
0.6789

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

Campaign `1` was in rejection from 2025-01-03 01:12:32 to 2025-01-03 05:10:38, and campaign `2` was in rejection from 2025-01-02 14:28:10 to 2025-01-03 00:47:40. That is, we calculate the waiting time from the last 'No' to the next 'Yes', if it exists.
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
