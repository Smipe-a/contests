# A. In vino veritas (15 points)
<p align="center">
  <img src=../../../img/a_in_vino_veritas.png/>
</p>
During the reign of Emperor Trajan, the Roman Empire reached its greatest territorial expansion. The economy of that time was highly developed, supported by advanced infrastructure and an extensive network of roads and maritime trade routes. Trade played a key role in ensuring the prosperity of the empire. At urban markets, silk, spices, oil, and other goods from around the world were sold, including products from India, China, Egypt, and other regions. Two tables of Roman merchants from the time of Trajan's reign have been discovered by scholars. Unfortunately, the column titles were lost. Your task is to use the provided data to conduct a statistical analysis, identify patterns, and determine the correct order of the columns in the tables. Based on this, you will be able to answer a series of questions.
<br><br>
You are reliably informed of the following facts, which may assist you in solving the task:
<br><br>         

<b>Here is what is known about the currency exchange rate table at</b> [roman_exchange_rates_1729253897.csv](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/semi_final/roman_exchange_rates_1729253897.csv)
<br>
<list>

* At that time, Roman merchants used three types of coins of different values in their transactions - gold, silver, and bronze. The most valuable coin was the one whose name derived from the Latin word for "gold"
* The gold coin could be exchanged for two other, less valuable coins. The exchange rate of the gold coin was set by the Senate daily and recorded in the table that was later discovered by scholars. The columns of the first table reflect the daily exchange rates of bronze and silver coins in relation to the gold coin. For example, on one day, the exchange rate was as follows: `1 gold = 40 silver = 70 bronze`
* It is reliably known that the `denarius` coin, during the period described in the ancient tables, had a trend of depreciation relative to the gold coin
</list>

<b>Here is what is known about the table with trading operations at</b>
[roman_transactions_1729253897.csv](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/semi_final/roman_transactions_1729253897.csv)
<br>
<list>

* It is known that the table with trading operations contained the following columns:
* `Year`
* `Month`
* `Day`
* `Product` - the name of the product (it is encrypted, and you will need to decrypt it in order to solve the task)
* `Currency` - currency of the transaction
* `Quantity` - the number of units of the product sold in the transaction
* `Price` - the price per unit of the product at the time of the transaction in the specified currency
* `Index` - the index of the gods favor
</list>

<br>
It is also known the following facts to establish the correct order of the columns and decrypt the product names:
<br>
<list>

* The `quantity` of `silk` sold was distributed exponentially, while the quantity of `grain` was distributed uniformly. The quantity of the product sold is considered for each transaction
* In one of the years, a severe drought occurred, which caused a significant spike in the average `price` of `oil` for several months, while the average `price` of `spices`, on the contrary, fell
* The favor of the gods was determined daily in the Temple of Jupiter by tossing 12 fair coins
</list>

### Input (Example)
Table 1
<table border="1">
  <tr>
    <td>col_0</td>
    <td>col_1</td>
    <td>col_2</td>
  </tr>
  <tr>
    <td>LXX</td>
    <td>XXXIV-XII-XXIV</td>
    <td>XL</td>
  </tr>
  <tr>
    <td>LXX</td>
    <td>XXXIV-XII-XXV</td>
    <td>XXXIX</td>
  </tr>
  <tr>
    <td>LXX</td>
    <td>XXXIV-XII-XXVI</td>
    <td>XL</td>
  </tr>
  <tr>
    <td>LXX</td>
    <td>XXXIV-XII-XXVII</td>
    <td>XL</td>
  </tr>
  <tr>
    <td>LXXI</td>
    <td>XXXIV-XII-XXVIII</td>
    <td>XLI</td>
  </tr>
</table>

Table 2
<table border="1">
  <tr>
    <td>col_0</td>
    <td>col_1</td>
    <td>col_2</td>
    <td>col_0</td>
    <td>col_1</td>
    <td>col_2</td>
    <td>col_0</td>
    <td>col_1</td>
  </tr>
  <tr>
    <td>Muniv</td>
    <td>XXXIX</td>
    <td>VIII</td>
    <td>XXXI</td>
    <td>Quinarius</td>
    <td>VIII</td>
    <td>XXIX</td>
    <td>CXXIX</td>
  </tr>
  <tr>
    <td>Murytub</td>
    <td>XXXIX</td>
    <td>IX</td>
    <td>CXXI</td>
    <td>Quinarius</td>
    <td>V</td>
    <td>VIII</td>
    <td>CXXV</td>
  </tr>
  <tr>
    <td>Murytub</td>
    <td>XL</td>
    <td>VIII</td>
    <td>CXVII</td>
    <td>Aureus</td>
    <td>V</td>
    <td>XXI</td>
    <td>V</td>
  </tr>
  <tr>
    <td>Atamora</td>
    <td>XXXVII</td>
    <td>VIII</td>
    <td>XII</td>
    <td>Quinarius</td>
    <td>V</td>
    <td>VI</td>
    <td>MCCCXXXVII</td>
  </tr>
  <tr>
    <td>Murytub</td>
    <td>XL</td>
    <td>XII</td>
    <td>CXL</td>
    <td>Denarius</td>
    <td>VII</td>
    <td>III</td>
    <td>DXLIX</td>
  </tr>
</table>

### Output
As the answer, please provide answers to the following questions, each on a new line:
1. The decrypted column names in the order they appeared in the original table. List the column names with a capital letter, separated by commas, and without spaces

<b>Example:</b> `Year,Month,Day,Quantity,Currency,Product,Price,Index`

2. The decrypted and translated product names in Russian, sorted by descending sales turnover (sales turnover = price × quantity). The names of four products have already been mentioned in the task. To determine the name of the last product, you will need to decipher the code of the ancient merchants. List the product names in the nominative case, with a capital letter, and no spaces between them, separated by commas

<b>Example:</b> `Silk,Oil,Grain,Spices,Anonymous`

### Output format
`Year,Month,Day,Quantity,Price,Index,Currency,Product`<br>
`Silk,Oil,Grain,Spices,Cheese`


# B. From Basra to Damascus (18 points)
<p align="center">
  <img src=../../../img/b_from_basra_to_damascus.png/>
</p>

Caravans in the Middle East played a key role in trade, connecting cities and oases along dangerous routes. A group of archaeologists discovered a map used by one of the ancient caravans. It was carrying a valuable cargo from the city of Basra - barrels of medicinal spices and herbs, highly sought after in Damascus.

According to the map, the caravan started from Basra and had to travel a long journey through the desert and mountain passes until it reached Damascus. But the caravan's path was full of dangers: it was threatened by bandits who coordinated their actions and exchanged signals about the caravan's movements.

The map shows possible locations for bandit attacks on the caravan, with the probability of an attack at each location depending on the terrain’s difficulty and the distance from nearby settlements.

The route from Basra to Damascus is branched, giving the caravan the option to choose between safer or riskier paths. Your task, as an expert in probability theory, is to calculate the route with the highest probability of successfully delivering the cargo to Damascus, avoiding attacks and passing through safe areas.

Route characteristics indicated in the map legend:
<list>

* Each object marked on the map has its own probability of a bandit attack.
* The probability of an attack may change depending on information the bandits pass about the caravan.
* The caravan cannot visit the same place twice.
* The caravan can fend off no more than three bandit attacks before its guards are killed, and the caravan is raided.
</list>

Input data: [A map of the road network between Basra and Damascus, with the probabilities of bandit attacks at intermediate points along the route. The connections between the attack probabilities are represented by pairs of objects on the map, along with a fractional number - if an attack happens at the first location, this number is added to the probability of an attack at the second location](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/semi_final/map.txt)

Output data: The maximum probability of successfully traveling from Basra to Damascus, presented as a decimal number rounded to 2 decimal places (e.g., 0.95).

### Notes
The connections in the data are one-way

# C. Drone of Cleopatra's Tomb (12 points)
<p align="center">
  <img src=../../../img/c_drone_of_cleopatras_tomb.png/>
</p>

Over the past few years, a variety of robots and drones of different designs have been created: wheeled, tracked, anthropomorphic, quadrupedal, quadcopters, snake robots, pneumatic mechanisms, and many others. They are increasingly used for practical tasks, including archaeological excavations.

In 2024, archaeologist Kathleen Martinez discovered a tunnel in Egypt that researchers believe may lead to the long-lost tomb of Cleopatra. However, access to the tunnel is difficult: part of it is flooded with water, there are blockages and collapses in some areas, and there are also rises and descents, creating additional challenges and safety threats for the researchers. Therefore, it was decided to use drones of various types to explore the tunnel.

Your task - determine the optimal strategy for using drones to discover the maximum number of valuable artifacts

### Input format
The input provides data for several tests, each simulating the deployment of drones in a tunnel. Each test consists of one line containing two integers `N` and `M` `(1 ≤ N, M ≤ 1000)` - the number of robots and the number of attempts in the current test, respectively. The probability of finding an artifact for each robot is unknown. In each test (drone deployment), the number of robots, attempts, and the probabilities of the drones are different.

For each test, you need to simulate the selection of robots - sequentially, print the index `i` `(0 ≤ i < N)` of the robot you are sending to search for artifacts. After sending the index, you will receive a number 0 or 1, depending on whether the robot found an artifact or not. Based on this, your algorithm can make the next decision.

The input format is specified in the example code.

The last line of input contains two zeros (0 and 0), indicating the end of the input

### Input format
For each test case, your program should output `M` lines, each containing a single integer `a` `(0 ≤ a < N)` - the index of the selected robot.

Once your program receives the line ""0 0"", it should terminate and output no further data

### Notes
To use third-party libraries (numpy, scipy, pandas), you need to select the Python 3.8 compiler (Handbook DS)

<b>Scoring:</b><br>
The score for the solution is the fraction of artifacts found by your program out of the number of artifacts found by the most optimal solution (i.e., the robot with the highest probability). For example, for a test case where:
<list>

* The number of robots is 3
* The number of attempts is 10
* The maximum probability of a robot is 0.8
* You found 4 artifacts
</list>
The score for this solution will be calculated as:
$$\frac{4}{0.8*10}=0.5$$
You are not able to view your score for the solution. The passing score for this task - <b>0.95</b>. If the score is ≥ 0.95, the verdict will be OK; otherwise, the verdict will be WA (Wrong Answer)

<b>Example code</b><i> (the score for this solution is about 0.56)</i><br>
```python
import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break  
        num_robots_and_steps = line.strip()
        num_robots, num_steps = map(int, num_robots_and_steps.split())
        if num_robots == 0 and num_steps == 0:
            break  
        num_robots = int(num_robots)
        num_steps = int(num_steps)

        for step in range(num_steps):
            # In the baseline solution, the first robot is always selected
            chosen_robot = 0
            # Sending the selected robot
            print(chosen_robot)
            sys.stdout.flush() 
            # Receiving data on whether we found an artifact or not (0 or 1)
            reward_line = sys.stdin.readline()
            reward = int(reward_line.strip())

    sys.exit()

if __name__ == "__main__":
    main()
```

# D. The Mosque Opening (15 points)
<p align="center">
  <img src=../../../img/d_the_mosque_opening.png/>
</p>
<table border="1">
  <tr>
    <td>Time limit per test</td>
    <td>6 second</td>
  </tr>
  <tr>
    <td>Memory limit per test</td>
    <td>5Mb</td>
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

In the VII century, Islam began to spread into Ethiopia through trade links between the Arabian Peninsula and the Horn of Africa. Initially, it was spread by Islamic merchants and communities settled in coastal cities such as Zeila and along important trade routes connecting the region with other parts of the world. These merchants not only conducted trade but also shared their religious knowledge with the local population.

By the early Middle Ages, many rulers of the region began to actively support the spread of Islam in their territories. While in the VI century only one mosque, Quba, was built in Ethiopia, by the XVI century, the city of Harar alone had several dozen mosques and became known as the city of 99 mosques.

Your task - determine the area of a large Ethiopian city where a new mosque should be built to maximize its attendance.

The city is represented as a rectangle of size m × n (m, n < 1000), consisting of 1 × 1 squares. It is divided into districts, with all squares of a district connected by shared sides. Each square of the city belongs to a particular district.

The population of each district and the number of mosques operating in each district are known. Residents attend one of the mosques in their district 5 times a week (the choice of mosque is random). The average weekly attendance of a resident at one of the mosques in any other district is calculated by the formula 1 / max(0.25, ln(r)), where r - minimum distance between districts, defined as the Euclidean distance between the closest squares of the districts.

The input data describes the city as follows:

    1. The dimensions of the rectangle (city)
    2. The rectangle itself (district number for each square)
    3. Information about each district: district number, population, and the number of active mosques

### Example 1

<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
2 2
1 1
1 2
1 150 2
2 300 0
</pre>
</td>
    <td>
<pre>
2
<br>
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
4 2
2 2
3 2
1 5
1 4
1 1101 25
2 1032 14
3 784 6
4 3365 9
5 1982 15
</pre>
</td>
    <td>
<pre>
3
<br>
<br>


<br>
<br>
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
4 5
1 1 2 3 4
1 2 2 5 6
1 5 5 5 6
7 8 8 6 6
1 100 2
2 130 3
3 50 6
4 40 1
5 200 10
6 170 8
7 30 2
8 110 4
</pre>
</td>
    <td>
<pre>
4
<br>
<br>
<br>
<br>
<br>
<br>
</pre>
    </td>
  </tr>
</table>