# The sharp ten-parameter failure of unimodality for two-order singleton disagreement spectra

## Finding
In the countable homogeneous structure with two independent linear orders, fix any finite, individually named parameter structure with \(n\) points. Every complete nonalgebraic singleton type specifies a gap in each order. The **disagreement grade** of a type is the number of parameters which lie on opposite sides of the new point in the two orders. Let \(c_k(\pi)\) count types of grade \(k\), where the base permutation \(\pi\in S_n\) records the second order relative to the first.

**Sharp finite threshold and classification.** For all permutations on at most nine points, the complete grade coefficient sequence \((c_0(\pi),\ldots,c_n(\pi))\) is unimodal. At ten points, exactly **32** of the \(10!\) labelled base permutations have a nonunimodal sequence. These 32 permutations are precisely five disjoint symmetry orbits, of sizes \(8,8,8,4,4\), under inversion and reversal of either order. The lexicographically selected orbit representatives below are given in *zero-based* one-line notation:

| Representative \(\pi\) | Orbit size |
|---|---:|
| \((1,3,0,9,2,8,7,6,5,4)\) | 8 |
| \((1,4,5,6,7,8,0,9,2,3)\) | 8 |
| \((2,1,4,0,9,8,7,6,5,3)\) | 8 |
| \((2,3,0,1,9,8,7,6,5,4)\) | 4 |
| \((2,4,5,6,7,8,0,9,1,3)\) | 4 |

The fourth representative has the complete grade sequence
\[
(c_0,\ldots,c_{10})=(3,8,16,20,19,20,15,8,6,4,2).
\]
In particular \(c_3=20>19=c_4<20=c_5\), a strict internal valley.

**Every larger order.** The same nonunimodality occurs for some base permutation of every length \(n\ge10\). Indeed, adding a new point which is last in *both* orders preserves all existing internal strict valleys, as quantified below.

## Assumptions and scope
An \(n\)-point parameter set has first-order positions \(0,\ldots,n-1\), and \(\pi(a)\) is the second-order position of parameter \(a\). A type is **nonalgebraic** if the new point is distinct from each parameter. In the homogeneous generic permutation structure, every ordered pair of open insertion gaps is consistent and realized; distinct gap pairs give distinct complete types. No parameters are identified or quotiented by automorphisms.

For \(0\le i,j\le n\), define the first-order initial segment \(A_i=\{0,\ldots,i-1\}\) and second-order initial segment \(B_j=\{a:\pi(a)<j\}\). Define
\[
 d_\pi(i,j)=|A_i\mathbin{\triangle}B_j|,\qquad
 c_k(\pi)=\#\{(i,j)\in\{0,\ldots,n\}^2:d_\pi(i,j)=k\}.
\]
All coefficients are nonnegative integers and \(\sum_{k=0}^n c_k(\pi)=(n+1)^2\). The sequence is **unimodal** if some \(m\in\{0,\ldots,n\}\) satisfies \(c_0\le\cdots\le c_m\ge\cdots\ge c_n\); plateaus are allowed. This concerns the coefficient profile and not real-rootedness or log-concavity.

## Proof
**1. Type–distance bijection.** The age of the generic two-order structure contains every finite permutation: insert a distinct new point between any adjacent parameters (or beyond either end) independently in each order. Homogeneity identifies complete singleton types with these quantifier-free gap pairs. Exactly the parameters in the symmetric difference of the two initial segments have opposite comparisons to the new point. Thus the displayed \(d_\pi\) and \(c_k\) represent the claimed logical types. With
\[
 R_\pi(i,j)=\#\{a<i:\pi(a)<j\},
\]
ordinary set cardinality gives the independent counting identity
\[
 d_\pi(i,j)=i+j-2R_\pi(i,j).
\]

**2. Exhaustive exact cutoff and orbit classification.** The attached deterministic standard C++17 checker enumerates *all* \(n!\) permutations for each integer \(1\le n\le10\), using lexicographic successor generation from the identity. On every permutation it calculates the \(n+1\) coefficients by two different exact methods: (a) Hamming distances of bitmasks of the two chains of initial segments, and (b) the foregoing rectangle-count formula computed through the inverse permutation. It asserts equality of the two full profiles and that the coefficient sum is \((n+1)^2\). It recognizes unimodality with a single pass, recording every failure.

For \(n=1,\ldots,9\), the recorded failure count is zero. For \(n=10\), it is exactly 32. The checker then closes each of the five displayed permutations under the three elementary symmetries: reversing positions, complementing values, and inversion. Their generated orbit sizes are exactly \(8,8,8,4,4\); the orbits are disjoint; and their union equals the *entire* recorded set of 32 failures, not a sample or subset. The checker separately asserts the indicated full eleven-coefficient witness profile. Thus the finite claims are established by a bounded exhaustive certificate with explicit domains, algorithms and recomputable output.

The symmetries really do preserve the property. Reversing either one of the two linear orders replaces the symmetric-difference size \(d\) with \(n-d\), reversing the coefficient list. Swapping the orders leaves \(d\) unchanged, up to interchanging the gaps. Reversal of a finite sequence preserves unimodality and nonunimodality. Hence the generated orbit description is mathematically appropriate.

**3. Persistence without further finite enumeration.** Let \(\pi^+\in S_{n+1}\) be obtained from \(\pi\in S_n\) by appending the new largest value at the last position of both orders. Existing \((n+1)^2\) gap pairs retain their grades. The two new border strips of gap pairs (last gap in exactly one order) each contain exactly one type at every grade \(1,\ldots,n+1\). Their intersection (last gap in both orders) contributes one grade-zero type. Therefore the new full profile is exactly
\[
 c_0(\pi^+)=c_0(\pi)+1,\qquad
 c_k(\pi^+)=c_k(\pi)+2\quad(1\le k\le n),\qquad
 c_{n+1}(\pi^+)=2.
\]
The strict valley at grades \(3,4,5\) of the ten-point witness remains a strict valley after each append. Induction proves existence for every \(n\ge10\).

## Verification
The complete standalone source `checker.cpp` and its generated output `check_output.txt` are included. To reproduce the census on a standard environment:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic checker.cpp -o checker
./checker
```

The output is deterministic and ends in `TOTAL_CHECKED=4037913` and `VERIFY_OK`. An assertion failure instead exits with a nonzero status and a `VERIFY_FAILURE` message. It checks all \(\sum_{n=1}^{10}n!=4,037,913\) permutations, every coefficient by two implementations, all orbit representatives, the exact smallest witness and the analytic append formula for a selection of appended orders through length 25. The infinite persistence is proved above; finite append tests are supplementary consistency checks and are not used to prove the infinite statement.

## Relationship to prior work
Cameron's *Homogeneous Permutations* (published 31 October 2002) classifies the relevant Fraïssé permutation classes and supplies the homogeneous context, not the present type-distance coefficient classification. Brignall–Ruškuc–Vatter's *Simple extensions of combinatorial structures* concerns how many points are required to extend a permutation to a simple one; it does not determine the present disagreement-grade distribution. Known formulas for total singleton types and individual-grade extremal bounds do not determine the simultaneous coefficient-shape property. The symmetric-difference interpretation is equivalent to the distance enumerator between two maximal chains of the Boolean lattice, so priority searches should include that terminology as well as two-order and permutation terminology.

## Limitations
The result classifies the *first* nonunimodal order and all its labelled examples, not all nonunimodal permutations at larger orders. It deals only with nonalgebraic singleton types and exactly two independent linear orders. The full finite certificate has been checked computationally; it is not replaced with a short conceptual classification proof. A plausible equivalent result under another name might not be indexed, and independent mathematical validation has not been performed.

## References
1. Peter J. Cameron, *Homogeneous Permutations*, *Electronic Journal of Combinatorics* **9**(2) (2002), R2. Published 2002-10-31. DOI: https://doi.org/10.37236/1674 ; https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i2r2
2. Robert Brignall, Nik Ruškuc and Vincent Vatter, *Simple extensions of combinatorial structures*, arXiv:0911.4378, first posted 2009-11-23; *Mathematika* **57** (2011), 193–214. https://arxiv.org/abs/0911.4378 ; https://doi.org/10.1112/S0025579310001518
