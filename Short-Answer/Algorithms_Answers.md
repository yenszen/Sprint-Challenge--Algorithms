#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
This algorithm has a Linear O(n) runtime complexity, because the number of operations always increases directly by n as input size increase, since you only need to add the value of N-squared by N times to equal the value of N-cubed.

b)

This algorithm has a Linearithmic O(n log(n)) runtime complexity, because although the outer for loop operation increases directly proportional to an increase in input size N, the inner while loop increases by slightly more than N for each outer loop operation, as the number of times j has to be multiplied by 2 to equal or surpass the value of N increases by slightly less than N times.

c)

This algorithm has a Linear O(n) runtime complexity, because for each additional bunny (i.e. input size) the total number of bunny ears always increases by 2, hence the number of operations always increases by 2 for each additional input.

## Exercise II

With an n-story building, we first go to the midpoint between the bottom and top floors of the building.
We then drop an egg off this floor.
If the egg breaks, we then go to another floor that is the midpoint between the bottom and current floor, since all the higher floors will also result in a dropped egg breaking.
If the egg does not break, we then go to another floor that is the midpoint between the current and top floor, since all the floors below our lower floors will also result in a dropped egg not breaking.
Once we moved to the new midpoint floor, we repeat the process of dropping an egg and checking if it breaks, then moving to the corresponding new midpoint floor to further repeat the process.
Eventually, we will arrive to a final floor with no further midpoint floor to be travelled to, and we will have the lowest floor for which an egg dropped will break.

This process will minimise the amount of eggs needing to be dropped and broken to arrive at the final lowest floor value.

Since what is described is a binary searching algorithm, it has a Logarithmic O(log n) runtime complexity.
