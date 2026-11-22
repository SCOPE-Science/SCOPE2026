# Independent mathematical audit

## correctness

PASS

For q>=4, excitation states at times t and t+2 cannot recur at one vertex, so the ancestry walk of an excitation never immediately reverses; any such walk in a tree is a simple path and has length at most diameter D=3. This limits last time of state 1 to t<=3 and last nonzero time to q+1, thus all rest by q+2. A t=3 excitation necessarily traverses a leaf-hub-hub-leaf path. The initial upstream hub must be 0 and upstream leaf shore has a 1; downstream hub initially 0 with no adjacent leaf initially 1, or q-1; downstream leaves include a color in {0,q-2,q-1}. These precise alternatives give L(a)R(b); opposite orientation is disjoint, giving the sum. All a,b positive makes count nonzero. Divide by q^(a+b+2); both L/q^m,R/q^m approach 1 giving 2/q^2. Independent all-state simulations verified q=4 a,b among (1,1),(2,2),(2,3),(3,3), q=5 (1,2),(2,2), q=6 (1,1).

## originality

PASS

Natural all-parameter labelled double-star last extinction shell for q>=4; prior 3-color arbitrary graph and q-state one-dimensional analyses cover structural ingredients but not the branching count.

## value

PASS

An all-branch-size exact natural extremal basin mass, with nonzero asymptotic probability 2/q^2 under growing branching, captures a meaningful finite-time delay phenomenon not determined by general extinction theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
