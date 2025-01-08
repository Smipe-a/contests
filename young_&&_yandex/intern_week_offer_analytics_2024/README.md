# A. Beads
Lera is making jewelry for her friends for New Year’s. To ensure no one feels left out, the jewelry will be identical

For her crafting project, Lera ordered 1150 beads. Since this is not her first time making jewelry, she knows that not all beads will be perfect: some will have defects, and some will arrive broken. To account for this, she ordered 15% more beads than the required amount

When Lera received the package, she wanted to check if she had enough quality beads to make the gifts. She decided to randomly select a bead from the package, check its quality, and then return it to the package. She repeated this process K times, and each time the bead turned out to be of good quality

What is the minimum value of K that guarantees Lera will have enough quality beads to make the jewelry with at least a 95% probability, assuming the proportion of quality beads follows a uniform distribution?

### Input
Provide the answer as an integer

### Notes
You have 2 attempts<br>
The verdict (whether the problem is solved correctly or not) is NOT shown

# B. Bus Arrival
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
Oleg lives across from the bus station and enjoys watching buses arrive. Each day, the station receives <i>n</i> buses. Based on the given schedule of bus arrivals, help Oleg determine the minimum time between the arrivals of two different buses

### Input
The first line contains an integer <i>n</i> $(1 \leq n \leq 2*10^4)$ - the number of buses<br>
The second line contains <i>n</i> moments of time in the format HH:MM $(0 \leq HH \leq 23,~0 \leq MM \leq 59)$ separated by spaces

### Output
Output a single integer - the minimum time in minutes between the arrivals of two different buses

### Example 1
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
2
23:59 00:00
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
3
00:00 23:59 00:00
</pre>
</td>
    <td>
<pre>
0

</pre>
    </td>
  </tr>
</table>

# C. Time for Vacation
<table border="1">
  <tr>
    <td>Time limit per test</td>
    <td>0.3 second</td>
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

Dasha and her dog Avi are deciding on the best time to travel to a new country. Dasha considers the vacation to be great if the temperature in the country increases during the trip. The greater the temperature rise by the departure day compared to the arrival day, the better

A weather forecast is provided for several days in advance. Determine the temperature change for the best period for Dasha and Avi, as well as the optimal arrival and departure days. If there are multiple best options, select the shortest trip with the earliest departure date

### Input
Integers separated by spaces

### Output
3 numbers separated by spaces: the temperature change over the optimal period, the arrival day index, and the departure day index. The days are numbered starting from 0

# D. Mysterious Letter
Nikolay sent his friend Ismagil a file with encrypted content and a request to decrypt it

Along with the file, there was an encrypted message of the following form: “уцмуьмвя ъэуопшйв ъэуеэвййацчуь цуцчуач ь чуй, щчу аё ужаоиа мшьузйулму ъэшюневювчд“

### Output
The response should include the decryption of the short message. All letters in the message must be lowercase

### Notes
The encrypted message [encoded.txt](https://github.com/Smipe-a/contests/blob/main/young_and_yandex/intern_week_offer_analytics_2024/encoded.txt)<br>
You have 2 attempts<br>
The verdict (whether the problem is solved correctly or not) is NOT shown

# E. Stay after class
<table border="1">
  <tr>
    <td>Time limit per test</td>
    <td>4 second</td>
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

Lera and Sonya were left in class after the lesson. To avoid wasting time, the girls decided to play an interesting game

First, they write <i>n</i> numbers on the board in a row. On each turn, a player can choose from one to <i>m</i> numbers <b>from the beginning of the sequence</b> and erase them. The player earns points equal to the sum of the erased numbers. The game continues until there are no numbers left on the board

The goal of the game - to end with a sum of points greater than the opponent's sum. Lera and Sonya take turns, with Lera going first. Both players play optimally. It is guaranteed that a tie is impossible

### Input
The input consists of two lines. In the first line, the numbers <i>n</i> $(4 \leq n \leq 50000)$ and <i>m</i> $(3 \leq m \leq 100)$ are given. In the second line, <i>n</i> numbers are provided - the numbers written on the board. Each number in the second line does not exceed 1000 in absolute value

### Output
Output 1 if Lera wins, otherwise output 0

### Example 1
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
4 3
1 2 3 9
</pre>
</td>
    <td>
<pre>
0

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
4 3
1 2 3 -4
</pre>
</td>
    <td>
<pre>
1

</pre>
    </td>
  </tr>
</table>