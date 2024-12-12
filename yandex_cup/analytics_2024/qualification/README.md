# A. Searching in the Dark (6 points)

In Ancient Egypt, the sun god Ra embarks on a daily journey across the sky in his sacred barque. Every morning, Ra sets sail across the sky on a gleaming boat, and in the evening, he descends into the underworld. The people of Egypt believe that throughout the night, Ra battles the treacherous god Apophis, defeats him, and rises again in the morning to sail across the sky.

Apophis is a fearsome and dangerous god, hunting the barque to prevent Ra from illuminating the earth, plunging the world into darkness. One day, Apophis attacked Ra, captured his sacred barque, and hid it in one of his two caves. Ra searches for his barque, but the sky is clouded, and it is impossible to see where the barque is hidden. The probability that the barque is in the first cave is 0.65, and the probability of finding the barque in the darkness is 0.44. Ra has already searched the first cave three times and the second cave seven times, but the search has been unsuccessful

1. Find the probability that the rook is in the first cave, given the unsuccessful attempts by God to find it
2. Determine the minimum difference in the number of unsuccessful attempts in the first and second caves required for the probability from the first part to be less than 0.5?

### Notes
Round the answer to part 1 to two decimal places. Use a dot (".") as the decimal separator

Use a space to separate the two answers

# B. Merchant and Coin (7 points)
In the ancient city of Al-Jabr, renowned for its sages and merchants, there lived a merchant named Zarifus, the keeper of a mysterious artifact - the Eye of Knowledge.

Zarifus offered travelers to play the sacred game of fate for the right to possess the Eye of Knowledge. The rules of the game were as follows:
1. The merchant would take out from his magical pouch a sacred coin with the image of the two-faced god Janus. The coin was always balanced and had an equal chance of landing on either side.
2. The seeker of truth was required to toss the coin, trying to get two faces of Janus (eagle) consecutively.
3. If the opposite side of the coin (tails) landed, the required number of Janus faces increased by one.
4. The game continued until the seeker managed to get the required number of consecutive Janus faces.
5. However, Zarifus had a condition - the traveler could only make 10 tosses in total.
6. If the seeker managed to complete the challenge, Zarifus would give the Eye of Knowledge. If not, the traveler would go to the sacred mountain near Al-Jabr and continue testing his luck with coin tosses.

The sages of the city pondered this game for a long time, trying to understand whether it was worth the risk in search of sacred knowledge. They sought to calculate the expected probability of winning this game using ancient probability and expectation formulas, but they could not agree on the result. They asked you to help them with these calculations in exchange for 7 local coins.

Your task - calculate the mathematical expectation of winning in this game.

### Output
A number in the range [0,1], rounded to 4 decimal places, with '.' as the separator. Examples: 0.0000 0.1234 0.9876 1.0000

# C. Unknown Civilizations (9 points)
The scientists have come into possession of very valuable data - the names of the most significant representatives of several ancient civilizations that existed in different parts of the universe in various eras, along with the connections between these representatives. Help the scientists answer the question - how many civilizations are represented by this data? The scientists know in advance that any representative of a civilization is connected to another representative of the same civilization through a series of 'handshakes'

### Input
A list of all known representatives and a list of pairs $person_x - person_y$, where each pair corresponds to the existence of a connection between representatives $person_x$ and $person_y$

Representatives: [persons.txt](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/qualification/persons.txt)<br>
Connections: [pairs.txt](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/qualification/pairs.txt)

# D. Dice Game (15 points)
The inhabitants of the ancient civilization of Norte-Chico loved two things: building pyramids and throwing dice. The ruler's favorite game was 1000. He really disliked losing, so he decided to gather his smartest subjects to come up with an optimal strategy for him. The winner is the one who, after summing up all the points from their turns, reaches 1000 points or more.

Your task is to determine the minimum number of points per turn after which to stop, in order to have the highest probability of winning when you have all 5 dice.

The process of the game: the player rolls 5 dice, then records the combination of dice that scores points for that round, while removing the dice that formed the combination. The player may then reroll the remaining dice. If, after a roll, no combination is formed, all accumulated points for that turn are lost and the turn passes to the next player.

A combination is considered when 3 to 5 (n) dice show the same number (v), with the following scoring table:
<table border="1">
  <tr>
    <td>v↓ n→</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
  </tr>
  <tr>
    <td>1</td>
    <td>100</td>
    <td>300</td>
    <td>1200</td>
  </tr>
  <tr>
    <td>2</td>
    <td>20</td>
    <td>60</td>
    <td>240</td>
  </tr>
  <tr>
    <td>3</td>
    <td>30</td>
    <td>90</td>
    <td>360</td>
  </tr>
  <tr>
    <td>4</td>
    <td>40</td>
    <td>120</td>
    <td>480</td>
  </tr>
  <tr>
    <td>5</td>
    <td>50</td>
    <td>150</td>
    <td>600</td>
  </tr>
  <tr>
    <td>6</td>
    <td>60</td>
    <td>180</td>
    <td>720</td>
  </tr>
</table>

If none of the combinations above were rolled, then the combination consists of all the rolled 1s and 5s, with each 1 being worth 10 points and each 5 worth 5 points

### Notes
* The ruler always goes first.
* There are 2 players in the game.
* You can stop rolling and record the accumulated points at any time.
* We are not asking about decisions made with fewer dice in hand.
* Example of dice rolls in one turn:
You roll 5 dice, 44415 is worth 40 points, and three dice are removed. You then roll the remaining 2 dice, and 51 appears, so you add 15 more points, and both dice are removed. Since all dice formed a combination, you get all 5 dice back. In total, you now have 5 dice and 55 points accumulated. You roll again and get 23466, which is not a valid combination, so the points for this turn (55) are lost, and the turn passes to the opponent.
* If you roll 11111 - you win immediately.
* In the answer, we are asked how many points you should accumulate in one turn before stopping in order to maximize your chances of winning (not every number is physically possible to achieve in the game).

# E. Digitization of Surveys (13 points)
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
In Ancient Rome, legislative power was divided between the magistrates, the Senate, and the assemblies (comitia). The legislative process was as follows: first, a magistrate would introduce a bill to the Senate, where it would be discussed and necessary amendments would be made. Afterward, the revised bill was put to a vote in the assemblies, and once passed, it would acquire the status of law.

Archaeologists and researchers of Ancient Rome, during their excavations, discovered a vast archive containing voting ballots from the assemblies, covering almost the entire duration of their existence! This discovery was a significant find, but it also posed a large volume of meticulous and labor-intensive work. To accelerate the process, the researchers approached Yandex with a request to digitize these ballots. In response, Yandex formed a team of analysts, of which you have the honor of being a part. You have been tasked with developing a system that reads responses from these ballots.

Task description:<br>
⬜⬜⬜⬜⬜⬜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 0 0 0<br>
⬜⬛⬛⬛⬛⬜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1 1 0<br>
⬜⬛⬜⬜⬛⬜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 0 0 1 0<br>
⬜⬛⬜⬜⬛⬜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 0 0 1 0<br>
⬜⬛⬛⬛⬛⬜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 1 1 1 1 0<br>
⬜⬜⬜⬜⬜⬜&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 0 0 0

There is an image represented as a matrix of 0 and 1, obtained by scanning one of the answer fields from the ballot. It is assumed that each valid field forms a continuous square on a white background, within which the respondent can place a cross.

It is assumed that there is no noise in the image. Write a program that finds the square in this matrix, and then determines whether it has been marked or not. The thickness of the square's lines and the cross is 1 pixel. The cross consists of two straight lines that connect opposite corners of the square

### Input
The size of the array (width and height) - integers < 10000. Then, an array of the specified size consisting of 0 and 1 without spaces is provided

### Output
The following outcomes are possible:
<list>
* `Marked`, if the square exists and the cross is marked
* `Not marked`, if the square is found, but there is no cross or it is incomplete. A cross is considered present if there is a continuous line between the bottom-right and top-left corners, as well as between the bottom-left and top-right corners
* `Printing error`, if there is no closed square
</list>

### Example 1
<table border="1">
  <tr>
    <td><b>Input</b></td>
    <td><b>Output</b></td>
  </tr>
  <tr>
    <td>
<pre>
11 9
11111111000
10000011000
10100101000
10011001000
10011001000
10100001000
11000011000
11111111000
00000000000
</pre>
</td>
    <td>
<pre>
Not marked

<br>
<br>
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
11 9
00000000000
00011111111
00011000011
00010100101
00010011001
00010011001
00010100101
00011000011
00011111111
</pre>
</td>
    <td>
<pre>
Marked

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
12 12
001111111111
001100000011
001010000101
001001001001
001000110001
001000110001
001001001000
001010000101
000100000010
001111111111
000000000000
000000000000
</pre>
</td>
    <td>
<pre>
Printing error
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

### Notes
1. A valid square cannot be degenerate, so its minimum size is 5x5
2. The square is always aligned parallel to the sides of the image, and checking the equality of the sides is not required

# F. Trade Operations of Phoenicia (10 points)

The Phoenicians were known for their active trade across the Mediterranean. However, what is even more remarkable is that by the X century AD, Phoenician traders were documenting all their transactions, keeping records of the operations conducted, and reporting to local authorities. Archaeologists have discovered numerous pieces of evidence of such records in various parts of the Mediterranean - in Morocco, Lebanon, Spain, Sicily, and other locations. We have gathered all available data on these operations and transformed it into a table for further analysis

Table transactions (trade operations):
<list>
* logid - event identifier
* date - event time
* countertype - event type, can be 'sell' (sale) or 'buy' (purchase)
* citizenid - identifier of the citizen who performed the transaction
* marketid - identifier of the market where the transaction took place
* merchantid - identifier of the merchant with whom the transaction was conducted
* cost - money spent on the transaction
* model_cost - estimated forecast value of the transaction
* fraudbits - whether the transaction is fraudulent or not (0 - no, 1 - yes)
</list>

Table merchants (merchants):
<list>
* merchantid - identifier of the merchant with whom the transaction was made
* guild - merchant's guild
* coef - merchant's amnesty coefficient
</list>
1. Determine the guild of merchants with the highest efficiency for the day. Efficiency is defined as the product of:<br>
Ratio of sales events to purchase events $\frac{sell}{buy}$<br>
Average amnesty per transaction. Amnesty is calculated as: $\frac{|cost-model\_cost|}{coef}$
2. The efficiency of this guild
3. Determine the hour during which the members of this guild made the highest number of sales

Only data that is not marked as fraudulent (fraudbits = 0) should be considered<br>
Data: [merchants.xlsx](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/qualification/merchants.xlsx) and [transactions.xlsx](https://github.com/Smipe-a/contests/blob/main/yandex_cup/analytics_2024/qualification/transactions.xlsx)

### Output
Round the efficiency to two decimal places. Example of the answer:<br>
`Guild of Bakers 12.34 15`