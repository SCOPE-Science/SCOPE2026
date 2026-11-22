# Exact entropy of the first genuinely nonliteral binary \(2\)-Abelian-square restriction

## Finding
Let \(a_n\) count binary words of length \(n\) having **no contiguous factor of length eight whose two length-four halves are \(2\)-Abelian equivalent**. Then \(A(z)=\sum_{n\ge0}a_nz^n=N(z)/P(z)\), where the exact integer coefficient arrays of \(P\) and \(N\) (in ascending powers of \(z\)) are:

```text
P = [1,0,0,-1,-2,-5,-8,-11,-13,-16,-19,-20,-26,-24,-26,-23,-15,-7,6,15,19,19,14,5,0,-6,-8,-4,-3,1,2,1,1]
N = [1,2,4,7,12,19,30,49,65,90,113,140,150,162,166,171,163,151,132,79,33,-47,-108,-155,-162,-130,-72,-12,41,67,56,39,3,-16,-16,-14,-4]
```

In particular, \((a_0,\ldots,a_{16})=(1,2,4,8,16,32,64,128,236,448,848,1610,3052,5794,10994,20858,39568)\). For \(n\to\infty\), \(a_n\sim C\lambda^n\), with \(C>0\) and \(1.897140076437<\lambda<1.897140076440\). This is strictly below the growth rate \(1.92756197548\ldots\) when only literal period-four squares are forbidden.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); a length-four word \(u\) is \(2\)-Abelian equivalent to \(v\) when their one-letter and ordered adjacent-pair multiplicities agree. Only squares with half-length **exactly four** are forbidden. Squares of any other period, including period one, may occur. The count is for ordinary linear, not circular, words and includes the empty word.

## Proof
For a length-four word, the initial symbol and the four ordered bigram counts determine its equivalence class (the terminal symbol and single-letter counts follow from the directed incidence balance). A direct classification of the sixteen blocks gives twelve singleton classes and exactly two two-element classes, \(\{0010,0100\}\) and \(\{1011,1101\}\). Therefore exactly twenty length-eight blocks are forbidden: the sixteen ordinary squares \(uu\) and the four extra blocks `00100100`, `01000010`, `10111101`, `11011011`.

Let the states be the 128 binary seven-bit words, indexed by their binary integer values \(0\) through \(127\). Define the integral \(128\times128\) matrix \(T\) with \(T_{s,t}=1\) when \(t\) is obtained by left-shifting \(s\) by one bit, appending \(b\in\{0,1\}\), retaining seven bits, and the resulting eight-bit window is not among the twenty forbidden words. All other entries are zero. Exactly 236 edges remain. For \(n\ge7\),

\[
a_n=\boldsymbol{1}^{\mathsf T}T^{n-7}\boldsymbol{1},\qquad a_n=2^n\quad(0\le n\le7).
\]

Write \(p_j\) for the coefficient of \(z^j\) in the displayed \(P(z)\), and \(v_j=\boldsymbol 1^{\mathsf T}T^j\). An **exact integer vector identity**, verified over all 128 coordinates by `verify_transfer.py`, is

\[
\sum_{j=0}^{32}p_jv_{33-j}=\boldsymbol0.
\]

Right multiplication by arbitrary powers of \(T\) proves the same identity at all later indices. Consequently \(P(z)A(z)\) is a polynomial of degree at most 39. Direct exact multiplication with the initial 40 counts gives precisely the displayed polynomial \(N(z)\) (whose coefficients in degrees 37 through 39 vanish). This proves the rational formula for **every** \(n\), not merely the tested lengths.

The directed 128-state graph is strongly connected, and the gcd of its directed cycle lengths is one, as certified by exhaustive forward/reverse reachability and an integral distance-gcd computation. Perron–Frobenius therefore gives a simple dominant positive eigenvalue \(\lambda\), with positive leading constant. A 500-step positive-vector Collatz–Wielandt calculation bounds it by the quoted strict rational endpoints, entirely by integer comparisons. The literal-square-only graph has all 240 possible edges except the sixteen literal squares; it is strongly connected and strictly contains the 236-edge graph. Strict spectral-radius monotonicity for irreducible nonnegative matrices shows its growth rate is strictly larger. The comparator's displayed decimal is obtained from its finite-state transfer calculation.

## Verification
Run `python3 verify_transfer.py` and `python3 verify_independent.py` in the same directory. The former independently constructs the forbidden-block set from the formal equivalence relation, checks all 128 coordinates of the annihilating identity, checks the generating-function numerator, strong connectivity, aperiodicity, and rigorous rational Perron bounds. The latter independently computes the word counts by brute-force checking all binary words through length 15 and compares them with a separate suffix-dynamic-programming implementation.

## Relationship to prior work
Huova and Karhumäki (2011) introduced the relevant equivalence and characterized its classes; Rao and Rosenfeld (2015) studied avoidance of long \(k\)-Abelian repetitions, emphasizing infinite words and avoidance indices. These results motivate the **first** half-length at which \(2\)-Abelian square avoidance differs from literal-square avoidance: no nonliteral equivalent pair exists below length four. Neither inspected full text contains the exact period-four binary avoidance enumerator or its entropy. The stated claim concerns a fixed, single period only; it neither implies nor is implied by the existence of globally square-free words. An unindexed equivalent enumeration remains a priority risk.

## Limitations
The method gives an exact finite-type language and exponential rate, not a theorem about avoidance at multiple periods or global \(2\)-Abelian-square freeness. Numerical Perron bounds are reproducible exact-integer certificates but not a closed radical expression. The finite brute-force checks alone do not prove the infinite formula; that proof relies on the vector annihilation identity. Historical priority is not independently established beyond the documented literature and database comparisons.

## References
1. M. Huova and J. Karhumäki, *Observations and Problems on k-abelian avoidability* (first public version 2011-04-21), https://arxiv.org/abs/1104.4273.
2. M. Rao and M. Rosenfeld, *Avoidability of long k-abelian repetitions* (first public version 2015-07-09), https://arxiv.org/abs/1507.02581. Mathematics of Computation **85** (2016), 3051–3060, https://doi.org/10.1090/mcom/3085.
