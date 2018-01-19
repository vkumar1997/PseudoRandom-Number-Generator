# PseudoRandom-Number-Generator
Generates biased and unbiased random numbers (xorshift* algo)

## How to use
1. Run `rand.py` using Python 2.7 
2. The code os built to perform any of the following tasks
    a. Generate an unbiased random number
    b. Generate a biased random number with 73% preference to the second half
    c. Generate a list of unbiased random numbers in a given range for accuracy check
    d. Generate a list of biased random numbers in a given range for accuracy check
    
    
## How does it work
1. `rand.py` uses system time to generate a unique number within a very short time but that dosen't give us true randomness.
2.  Instead, we use the system time as a seed for a preudo random number generator (xorshift* algorithm) which generates           numbers at uniformly distributed randomess and fast speeds(described below).
3.  Even though xorshift* is used to generate numbers with uniform distribution, to create a biased generator, weights were         used in the code
    a.  Generate a number from 1 to 10000 using the xorshift* algo and system time.
    b.  Now, suppose we need to create a 73% bias in favor of upper half. So, if the number generated > 270,  use                     xorshift* algorithm to create a random number from just the upper range. Otherwise, it creates a number from the             lower range.
    c.  This ensures that the accuracy is maintained for any size of the list and any range of numbers.
    

## XorShift* Algorithm
A detailed explanarion of the application can be found [here](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjGuvSF0uTYAhWKKY8KHSmaAJYQ0gIIMCgCMAA&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FXorshift%23xorshift*&usg=AOvVaw39J8b0f91qCAuuZiK0VTSE)

Xorshift generators are among the fastest non-cryptographically-secure random number generators, requiring very small code and state. Although they do not pass every statistical test without further refinement, this weakness is well-known and easily amended (as pointed out by Marsaglia in the original paper) by combining them with a non-linear function, resulting e.g. in a xorshift+ or xorshift* generator.

A xorshift* generator takes a xorshift generator and applies an invertible multiplication (modulo the word size) to its output as a non-linear transformation, as suggested by Marsaglia. The following 64-bit generator with 64 bits of state has a maximal period of 2^64 − 1 and fails only the MatrixRank test of BigCrush

XorShift algorithm is a combination of XOR and SHIFT operations.
1. There are four parameters used in this algorithm and the randomness of the algorithm can be tweaked by these parameters      and the operators used along- seed, a, b, c
2. First we generate the seed using the system time which is a good and universal way to generate a new seed
3. The operations used in this algorithm (for 64 bit unsigned numbers) are as follows
      seed  = seed ^ seed >> a
      seed = seed ^ seed << b
      seed = seed ^ seed >> c
   The tweaking of a,b,c and the shilft operators is important to create maximum randomness with long periods.
      
4. In xorshift*, we also use a modulo to combine it with a non linear operation (max size of 64 bit unsigned).
5. This gives a random number which can further be used as a seed for next iteration
    
## Advantages
1. Generates 1,00,000 in a space of a second
2. No pattern is observed in the generated numbers
3. Comparable to Mersenne Twister algo and comparitvely better performance-wise than Linear Congruence Algorithm etc.
4. For length of list above 500, the bias of produced results have minimal error(around 0.56%)

# Limitations
1. The start and the end digits specified by user should be integers
2. The bias though stay between 71% and 75% for produced results, in some rare cases, it may wander off to 65% or 80%(usually    when length of list<100)
