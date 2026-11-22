# A nine-versus-seven majority clock on a cospectral cubic pair of order fourteen

## Finding

There are two connected, nonisomorphic, adjacency-cospectral cubic graphs \(G\) and \(H\) on fourteen vertices, specified exactly below, whose synchronous binary open-neighborhood majority maps have different complete recurrent and transient censuses. Every state of either map reaches a fixed point or a primitive two-cycle. The precise totals are:

| Quantity | \(G\) | \(H\) |
|:--|--:|--:|
| Fixed configurations | 18 | 14 |
| Primitive two-cycle orbits | 201 | 75 |
| Initial states eventually reaching a fixed configuration | 3,504 | 4,036 |
| Sharp largest first-periodic-entry time | 9 | 7 |

Thus the graph with more equilibria has the smaller collective fixed-point basin. This separation occurs within the minimum possible order for a pair of nonisomorphic cospectral cubic graphs, a minimum established in the spectral-graph literature [1]. It is an exact finite statement, not an asymptotic or general theorem about all cospectral graphs.

## Assumptions and scope

Both undirected graphs have the labelled vertex set \(V=\{0,1,\ldots,13\}\). Let \(C=\{0,1,2,3\}\) and \(D=\{4,5,6,7,8,9\}\). The subset \(C\) is independent. In \(G\), the six vertices of \(D\), in ascending order, have their respective neighbors in \(C\) given by the six pairs
\[
\{0,1\},\quad \{0,2\},\quad \{0,3\},\quad
\{1,2\},\quad \{1,3\},\quad \{2,3\}.
\]
In \(H\), each such pair is replaced by its complement in \(C\). The graphs otherwise have exactly the same nine edges:
\[
\{4,10\},\{5,11\},\{6,12\},\{7,13\},\{8,13\},\{9,13\},
\{10,11\},\{10,12\},\{11,12\}.
\]
There are no additional edges. Every vertex has degree three; both graphs are connected.

For a configuration \(x\in\{0,1\}^{V}\), define \(F_Q(x)\), where \(Q\in\{G,H\}\), by
\[
F_Q(x)_v = \begin{cases}
1,&\sum_{u\sim_Q v}x_u\ge 2,\\
0,&\sum_{u\sim_Q v}x_u\le 1.
\end{cases}
\]
There are no ties, since every vertex has three neighbors; no self-vote is counted. For \(x\), its *first-periodic-entry time* \(d_Q(x)\) is the smallest \(t\ge0\) such that \(F_Q^t(x)\) lies on a recurrent orbit; \(p_Q(x)\) is the least period of that recurrent orbit. The basin of fixed configurations consists of \(\{x:p_Q(x)=1\}\).

## Proof

**Graph structure.** In each graph, the first four vertices are independent, each of the next six has two neighbors in \(C\), and the remaining four have none. Each member of \(C\) is incident to three of the six \(C\)-\(D\) edges. Complementing each two-element neighborhood in \(C\) preserves every degree and every edge not meeting \(C\). Thus the pair is cubic. Write \(A_G\) and \(A_H\) for their adjacency matrices in label order and define
\[
Q=\operatorname{diag}\bigl(\tfrac12J_4-I_4,I_{10}\bigr).
\]
As \(Q^2=I_{14}\) and each \(C\)-\(D\) incidence column contains exactly two ones, direct block multiplication gives \(QA_GQ=A_H\). Therefore their adjacency characteristic polynomials coincide. In fact, direct exact arithmetic gives the common polynomial
\[
z(z-3)(z+1)^2(z^3-3z+1)^2
(z^4+z^3-9z^2-5z+16).
\]

For nonisomorphism, each graph has exactly one triangle, \(\{10,11,12\}\). Its three respective external neighbors are \(4,5,6\). In \(G\), these three vertices have common neighbor \(0\); in \(H\), they have no common neighbor. This graph-isomorphism invariant separates the pair.

**Dynamical finite proof.** The entire binary configuration space has \(2^{14}=16,384\) states. The files `direct_checker.py` and `functional_checker.py` are complete, independently structured enumerators of that space. The first explicitly constructs both edge lists and traces each starting state until its first repeated value, recording the first cycle position and least cycle length. The second independently constructs the graphs from the switching rule, evaluates the transition map with neighbor bit masks, removes transient states by indegree peeling, identifies every residual directed cycle and propagates period and depth backward over the removed states. Both calculate the period and first-entry time **for each of the 16,384 initial states on each graph**, and their period-depth vectors agree in SHA-256 digest for both graphs (see Verification). The algorithms use integer operations only; the finite-state proof relies on no floating-point approximation or sampling.

Their common exact census follows. Every omitted entry is zero.

| First entry \(t\) | \(G:p=1\) | \(G:p=2\) | \(H:p=1\) | \(H:p=2\) |
|--:|--:|--:|--:|--:|
| 0 | 18 | 402 | 14 | 150 |
| 1 | 394 | 2,990 | 458 | 2,754 |
| 2 | 1,160 | 4,400 | 1,248 | 5,184 |
| 3 | 1,008 | 2,304 | 1,104 | 1,752 |
| 4 | 576 | 1,416 | 660 | 1,416 |
| 5 | 288 | 552 | 468 | 612 |
| 6 | 60 | 444 | 84 | 420 |
| 7 | 0 | 264 | 0 | 60 |
| 8 | 0 | 96 | 0 | 0 |
| 9 | 0 | 12 | 0 | 0 |
| **Total** | **3,504** | **12,880** | **4,036** | **12,348** |

At entry time zero, each primitive two-cycle contributes exactly two states. The cycle totals are therefore \(402/2=201\) and \(150/2=75\). Since the sum of the two period columns for each graph is exactly 16,384 and the enumerators classify all possible input words, the table excludes every other recurrent period and proves the claimed maximal entry-time upper bounds. Their sharpness is witnessed by the labelled initial bitmasks 3482 on \(G\) and 1245 on \(H\), which reach their eventual two-cycles for the first time at steps nine and seven respectively. The full witness trajectories are reproduced in Verification.

## Verification

With Python 3, execute the following commands in the directory containing the standalone files:

```sh
python3 direct_checker.py > direct_recomputed.json
python3 functional_checker.py > functional_recomputed.json
cmp direct_recomputed.json functional_recomputed.json
cmp direct_recomputed.json direct_output.json
```

Both independent programs have been executed and their JSON outputs agreed byte-for-byte. The associated statewise period/depth digests are:

- \(G\): `a3f0f53509bb55025eeb957bdc84ad7cc290b5ef2c91c911aa8060e78cbabf10`.
- \(H\): `21340a7eb526c4436ba4799764212dc6fc55f52ba13e4237209bd66632865cb5`.

The two distinct algorithms share only the explicit graph definition and the mathematical meaning of the update rule. For the switching/cospectral and nonisomorphism arguments, exact adjacency construction and elementary neighborhood intersections suffice. The polynomial factorization is ancillary and is not needed for the dynamical counts.

## Relationship to prior work

Godsil and McKay [1] construct nonisomorphic cospectral graphs through local switching, including pairs of cubic graphs on fourteen vertices, and prove that no smaller cospectral cubic pair exists. That paper establishes graph construction and adjacency spectral equivalence, **not** a majority-dynamics time/basin census. Goles and Olivos [2] prove eventual period one or two for symmetric binary threshold systems, but that general result does not determine the two graphs' individual orbit counts or sharp entry-time values. Kaaser, Mallmann-Trenn and Natale [3] treat voting-time upper bounds, computational hardness and graph modules, not the explicit cospectral-pair census here. Other publicly indexed work compares majority dynamics on the distinct sixteen-vertex Shrikhande–rook cospectral pair [4]; those values do not imply the new fourteen-vertex counts. These are comparisons of actual conclusions, not novelty deductions based only on different titles.

## Limitations

The theorem is finite and exact only for the two explicitly defined graphs, not a bound for every graph on fourteen vertices or every switching pair. The extremal clocks are first entry into a recurrent orbit, not time to unanimous consensus; some states never become unanimous. Exact computation over a finite space is exhaustive here, but does not prove an infinite-graph generalization. Equivalent historical enumerations may exist outside the indexed sources inspected. The graph construction and its cospectrality were known; no claim to their priority is made. There is no independent external audit or machine-verified formal proof; the two replayable implementations are computational evidence subject to normal software-verification limitations.

## References

[1] C. D. Godsil and B. D. McKay, *Constructing cospectral graphs*, Aequationes Mathematicae 25 (1982), 257–268. https://users.cecs.anu.edu.au/~bdm/papers/GodsilMcKayCospectral.pdf , DOI: 10.1007/BF02189621.

[2] E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics 3 (1981), 93–105. https://doi.org/10.1016/0166-218X(81)90034-2 .

[3] D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, public version dated 2015-08-14. https://arxiv.org/abs/1508.03519 .

[4] *Spectral twins separate under majority dynamics: exact Shrikhande–rook attraction censuses*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-spectral-twins-separate-under-majority-dynamics-exact-shrikhande--a7ee2eb89698 .
