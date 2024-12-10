# A. In vino veritas (15 points)
<p align="center">
  <img src=../../../img/a_in_vino_veritas.png/>
</p>
During the reign of Emperor Trajan, the Roman Empire reached its greatest territorial expansion. The economy of that time was highly developed, supported by advanced infrastructure and an extensive network of roads and maritime trade routes. Trade played a key role in ensuring the prosperity of the empire. At urban markets, silk, spices, oil, and other goods from around the world were sold, including products from India, China, Egypt, and other regions. Two tables of Roman merchants from the time of Trajan's reign have been discovered by scholars. Unfortunately, the column titles were lost. Your task is to use the provided data to conduct a statistical analysis, identify patterns, and determine the correct order of the columns in the tables. Based on this, you will be able to answer a series of questions.
<br><br>
You are reliably informed of the following facts, which may assist you in solving the task:
<br><br>
<b>Here is what is known about the currency exchange rate table at</b>

`roman_exchange_rates_1729253897.csv`
<br>
<list>

* At that time, Roman merchants used three types of coins of different values in their transactions - gold, silver, and bronze. The most valuable coin was the one whose name derived from the Latin word for "gold"
* The gold coin could be exchanged for two other, less valuable coins. The exchange rate of the gold coin was set by the Senate daily and recorded in the table that was later discovered by scholars. The columns of the first table reflect the daily exchange rates of bronze and silver coins in relation to the gold coin. For example, on one day, the exchange rate was as follows: `1 gold = 40 silver = 70 bronze`
* It is reliably known that the `denarius` coin, during the period described in the ancient tables, had a trend of depreciation relative to the gold coin
</list>

<b>Here is what is known about the table with trading operations at</b>
`roman_transactions_1729253897.csv`
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

# C. From Basra to Damascus (12 points)
<p align="center">
  <img src=../../../img/c_drone_of_cleopatras_tomb.png/>
</p>

# D. From Basra to Damascus (15 points)
<p align="center">
  <img src=../../../img/d_the_mosque_opening.png/>
</p>