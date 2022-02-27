# stunning-octo-winner
two-third average problem

From wiki - In game theory, "guess 2/3 of the average" is a game where several people guess what 2/3 of the average of their guesses will be, and where the numbers are restricted to the real numbers between 0 and 100, inclusive. The winner is the one closest to the 2/3 average. In this game there is no strictly dominant strategy. However, there is a unique pure strategy Nash equilibrium. This equilibrium can be found by iterated elimination of weakly dominated strategies. Guessing any number that lies above 66+2/3 is weakly dominated for every player since it cannot possibly be 2/3 of the average of any guess. These can be eliminated. Once these strategies are eliminated for every player, any guess above 44+4/9 is weakly dominated for every player since no player will guess above 66+2/3, and 2/3 of 66+2/3 is 44+4/9. This process will continue until all numbers above 0 have been eliminated. All players selecting 0 also happens to be the Pareto optimal solution. This game illustrates the difference between perfect rationality of an actor and the common knowledge of rationality of all players. Even perfectly rational players playing in such a game should not guess 0 unless they know that the other players are rational as well and that all players' rationality is common knowledge. If a rational player reasonably believes that other players will not follow the chain of elimination described above, it would be rational for him/her to guess a number above 0. We can suppose that all the players are rational, but they do not have common knowledge of each other's rationality. Even in this case, it is not required that every player guess 0, since they may expect each other to behave irrationally. When performed among ordinary people it is usually found that the winner's guess is much higher than 0: the winning value was found to be 21.6 in a large online competition organized by the Danish newspaper Politiken. 19,196 people participated and the prize was 5000 Danish kroner.

The non-zero winner's guess is due to the irrationality of some people. 

The way to approach this problem is to think how irrationally others might think. The more rational you are, the smaller your answer would be as it converges to zero.

Thus, we create different orders starting from the zeroth order to the n-th order where the zeroth order to n-th order thinker thinks as shown below:

0th: The zeroth order thinker guesses randomly returning 1/2 on average
1st: First order thinker guesses 2/3 of zeroth order thinkers (2/3 * 1/2 = 1/3)
2nd: Second order thinker guesses 2/3 of first order thinkers ((2/3)^2 * 1/2 = 2/9)
...
nth: nth order thinker guesses 2/3 of (n-1)th order thinkers ((2/3)^n * 1/2 = ...) 

Clearly, this is a geometric series where a = 1/2 and r = 2/3.

To guess the winning answer, one can simply take the average of this geometric series. In fact, when one takes the sum from 0th to 3rd order, one would return a value of ~0.20. However, as n approaches infinity, the geometric sum converges, and it's average approaches 0.

Assuming that there is an even distribution of people with varying rationalities (assuming there is an equal amount of thinkers in each order) explains that.

As such, a skewed normal distribution is taken and we are able to obtain a winning guess of 0.17 when we set the average/peak of the normal distribution to the 1.5-th order (most people are a 1.5-th order thinker). This value is close to experimental value of 0.216.

In this script, we plot the graph of Guess vs Order as well as the distribution of the thinkers. 2 ways are also used to determine x_sum: 1 being iteration and another being recursion through fold.

![image](https://user-images.githubusercontent.com/64541670/155877279-50015685-91f2-4a4a-836d-710ff912e80c.png)
![image](https://user-images.githubusercontent.com/64541670/155877296-526079b0-ce18-4e6b-82de-dfed2aae74e9.png)
