# Independent mathematical audit

## correctness

PASS

Only the four monochromatic-part corners can be recurrent; from each noncorner there is positive probability of reaching a corner in one update, uniformly over the finite state space for the fixed sizes. In a single-tie state only the opposite part draws a binomial; the transition into any mixed strict state costs exactly one residual step. For a double tie the independent draws give the product corner probability uv and return-to-double-tie probability pq, yielding the stated 3x3 system. If a size is odd, the only possible tie randomizes that odd part and cannot regenerate a tie, giving expectation at most 2. Independently enumerated the product binomial outcomes into the two single-tie classes, double tie, corners and mixed strict states, then solved (I-Q)H=1+Pr(mixed strict) by exact Fraction elimination for each of the 400 even pairs. Among all 1200 tie values the only maxima were the double ties at (2,6),(6,2), with values 7/3, 13/6, 79/27 at (2,6). Checked 8*C(42,21)=4306062995520<4398046511104=2^42; the central-binomial probability decreases. The ordered vector (11/5,13/5,41/15) solves the artificial larger-tie no-corner Bellman equations and satisfies the derivative sign and coordinate-order tests; iteration from zero under the actual nonnegative transition operator proves the strict tail bound. Source scripts inspected, not executed.

## originality

FAIL

The earlier Resultary record f53926f40d07 expressly proves the same expected entrance-time law (every coloring), recurrent-class census, 79/27 bound and exclusive equality case under identical independence, synchrony and tie hypotheses. It also gives the full time generating functions and terminal-class probabilities. A different cutoff certificate does not make the theorem new.

## value

FAIL

The sharp biclique threshold is a meaningful scientific benchmark in its earlier publication, but the frozen claim repeats that result and offers no new useful invariant. The replacement proof uses a larger grid and weaker tail cutoff than the earlier nine-pair certificate, with no demonstrated downstream benefit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
