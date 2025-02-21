# A. Yan in the Gym
<table border="1">
  <tr>
    <td>Time limit per test</td>
    <td>0.1 second</td>
  </tr>
  <tr>
    <td>Memory limit per test</td>
    <td>20Mb</td>
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

In a gym, $N$ free treadmills are arranged in a row. Yan and $K$ of his friends decided to work out today. To avoid disturbing each other, they agreed to occupy treadmills as far apart as possible. Each person chooses a treadmill in the center of the largest available free segment. Since everyone takes a different amount of time to prepare, they occupy the treadmills one by one.

Each person selects a treadmill that maximizes the minimum distance to the nearest occupied treadmills on the left and right. If multiple treadmills meet this condition, one is chosen randomly by Yan. However, if the edge treadmills are still free, they are given priority.

Unfortunately, Yan is slow to get ready and arrives last at the gym (he takes a long time to change). Given $N$ and $K$, determine how many free treadmills remain on both sides of Yan after he occupies his treadmill as the ($K+1$ th) person.

### Input
The program takes two natural numbers as input $N$ and $K$, where $1 \leq K < N \leq 10^{18}$

### Output
The program should output two natural numbers in non-decreasing order, representing the number of free treadmills on both sides of Yan.

### Example 1
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
7 0
</pre>
</td>
    <td>
<pre>
0 6
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
7 1
</pre>
</td>
    <td>
<pre>
0 5
</pre>
    </td>
  </tr>
</table>

### Example 3
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
8 2
</pre>
</td>
    <td>
<pre>
2 3
</pre>
    </td>
  </tr>
</table>

### Example 4
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
8 3
</pre>
</td>
    <td>
<pre>
1 1
</pre>
    </td>
  </tr>
</table>

### Notes
In the first example, Yan occupied the outermost treadmill. There were no treadmills on one side, while N − 1 treadmills remained on the other.

In the second example, Yan again occupied the outermost treadmill, but on the opposite side.

In the third example, Yan chose one of two treadmills with an equal total distance to the occupied treadmills on the left and right.

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

You need to develop an algorithm for a new robot vacuum cleaner. You have been provided with an apartment of size N x M cells (width x height) as a testing ground. The apartment contains walls and furniture, which are impassable for the robot. The robot itself occupies one cell.

Write a program that allows the robot to complete its task as quickly as possible, given that it takes x seconds to move to an adjacent cell and y seconds to clean one cell.

### Input
The input consists of a single line containing four integers: N, M, x, y. Then, a two-dimensional array is provided, where 0 - represents free space, 1 - represents an obstacle wall or furniture.

### Output
Output a single integer - the minimum time required to clean the apartment.

### Example 1
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
5 4 1 3
11111
10001
10001
11111
</pre>
</td>
    <td>
<pre>
23

<br>

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
7 5 2 2
1111111
1001001
1000001
1001001
1111111
</pre>
</td>
    <td>
<pre>
50
<br>

<br>
</pre>
    </td>
  </tr>
</table>

### Notes
1. You can use any free cell as the starting position for the robot.
2. It is guaranteed that every free cell is reachable.


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
<table border="1">
  <tr>
    <td>Time limit per test</td>
    <td>5 second</td>
  </tr>
  <tr>
    <td>Memory limit per test</td>
    <td>244.224609375Mb</td>
  </tr>
  <tr>
    <td>Input</td>
    <td>Standart input</td>
  </tr>
  <tr>
    <td>Output</td>
    <td>Standart output</td>
  </tr>
</table>

You are an analyst for a flower recognition application. Your task is to evaluate the quality of the classifier. The classifier processes pre-cropped images, each expected to contain 1 flower species. However, cropping errors may result in images that do not contain flowers at all.

You need to calculate the proportion of correctly recognized flowers among all input images that actually contained flowers, taking into account the distribution of flower species among users.

You have two files:
1. The number of flowers of each type as recognized by the algorithm. Automatically obtained from the application logs over the past month. detection_count.csv with columns: detected_name - flower name as recognized by the classifier, count - number of flowers of this type
2. Results of manual data labeling on a sample (from a different period). Each row represents an expert validation of the recognition, assigning the correct flower type. detection_quality.csv with columns: detected_name - flower name as recognized by the classifier, human_name - flower name according to manual data labeling (considered the ground truth)

In addition to flower names, the columns detected_name and human_name may contain the entry not_a_flower, indicating that either the algorithm or the human annotator determined that the image does not contain a flower.

You need to reweight the quality assessment results from detection_quality.csv, taking into account the actual class distribution from detection_count.csv.

However, for some flower types, we have very few or no samples at all. In such cases, certain assumptions will need to be made. You will need to perform calculations according to the algorithm outlined below.
1. Classify flowers into three groups:
    * not_a_flower - handled separately
    * popular flowers - those with 10 or more samples where the classifier's prediction matched the human label.
    * other flowers - those with fewer than 10 samples where the classifier's prediction matched the human label. These are grouped based on the detected flower type
2. For each group, calculate the average probability that an actual flower was provided as input but the classifier misclassified it into the given group.
3. Next, calculate the average probability of correct classification. For flowers in the popular group, compute this probability individually for each type. For the other flowers and not_a_flower, compute the average probability across the entire group.
4. Reweight the monthly classification statistics: consider the probability that a non-flower was provided as input (this should decrease all group probabilities), and factor in the classifier’s accuracy. Compute the final weighted quality score for the user

From last month’s results [detection_count_previous.csv](https://github.com/Smipe-a/contests/blob/main/young_%26%26_yandex/internship_spring_summer_analytics_2025/detection_count_previous.csv), the classifier’s quality score was 0.8613 (use this for debugging).

What will be the weighted quality score for this month (detection_quality.csv remains the same, but the distribution of detected flower frequencies in detection_count.csv is different)?

Write a program that reads [detection_quality.csv](https://github.com/Smipe-a/contests/blob/main/young_%26%26_yandex/internship_spring_summer_analytics_2025/detection_quality.csv) and [detection_count.csv](https://github.com/Smipe-a/contests/blob/main/young_%26%26_yandex/internship_spring_summer_analytics_2025/detection_count.csv), then prints the score with an accuracy of 4 decimal places, without any additional output.

### Input
month_detected.csv with fields
* detected_name 
* count

human_classification.csv with fields
* detected_name
* human_name

### Output
Print the metric rounded to 3 decimal places (rounded to the nearest value).
For example: 0.123 (instead of 0.122987).
