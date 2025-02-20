**1. What is the probability that Petya, selecting a random curd bar, will get one with condensed milk, assuming no one else visited the large coffee point between Vasya and Petya?**

The probability of transferring $k$ curd bars with condensed milk:

$$P(X=k)=\frac{C_5^{2-k} \cdot C_4^k}{C_9^2}, \quad k=0,1,2$$
$$X~-~the~number~of~curd~bars~with~condensed~milk~transferred$$

The probability that a randomly selected curd bar at the large coffee point is with condensed milk, given that $k$ curd bars with condensed milk were transferred:

$$P(Y~|~X=k)=\frac{2+k}{7}, \quad k=0,1,2$$
$$Y~-~the~event~that~Petya's~randomly~chosen~curd~bar~is~with~condensed~milk$$

The final probability:

$$P(Y)=\sum_{k~=~0}^2 P(X=k) \cdot P(Y~|~X=k)=\frac{10}{126} + \frac{15}{63} + \frac{4}{42} \approx 0.4127$$

**2. What is the probability that Vasya, in his rush, transferred both bars with condensed milk, given that the bar Petya took was with condensed milk (assuming no one else visited the large coffee point between Vasya and Petya)?**

The probability that Vasya transferred 2 curd bars with condensed milk and Petya took a curd bar with condensed milk:

$$P(X=2,~Y)=P(X=2)~P(Y~|~X=2)=\frac{4}{42}$$

The final probability:

$$P=\frac{P(X=2,~Y)}{P(Y)}=\frac{4}{42} \cdot \frac{126}{52} \approx 0.2308$$

**3. What is the probability that Petya, selecting a random curd bar, will get one with condensed milk, given that exactly one person visited the large coffee point between Vasya and Petya and took exactly one bar?**

The probability distribution when a person randomly picks a curd bar at the large coffee point:

$$P(X=k,~T=0)=\frac{3+2-k}{7} \quad \quad \quad P(X=k,~T=1)=\frac{2+k}{7}$$
$$T=0~-~a~regular~curd~bar~is~randomly~taken$$
$$T=1~-~a~curd~bar~with~condensed~milk~is~randomly~taken$$

The probability that Petya selects a curd bar with condensed milk, considering that one curd bar was already taken:

$$P(Y~|~X=k,~T=0)=\frac{3+2-k}{7} \cdot \frac{2+k}{6} \quad \quad \quad P(Y~|~X=k,~T=1)=\frac{2+k}{7} \cdot \frac{1+k}{6}$$
The final probability:

$$P(Y)=\sum_{k~=~0}^2P(X=k) \sum_{j=0}^1 P(Y~|~X=k,~T=j)=\frac{60}{756}+\frac{90}{378}+\frac{24}{252} \approx 0.4127$$

