# A fixed-point entropy rebound in generalized Petersen majority dynamics

## Finding

For every integer \(n\ge7\), consider the cubic generalized Petersen graphs \(GP(n,k)\) with inner steps \(k=1,2,3\), carrying synchronous binary open-neighbor majority dynamics. Let \(F_k(n)\) denote the number of labelled one-step fixed configurations (no quotient by graph symmetries or spin complementation). The three fixed-point populations have exponential growth constants \(\alpha_k\) satisfying the **strict, nonmonotone order**

\[
1.56485<\alpha_2<1.56486
<1.5965<\alpha_3<1.5966
<\alpha_1=\frac{1+\sqrt5}{2}.
\]

More precisely, \(F_k(n)\sim\alpha_k^n\) as \(n\to\infty\). Consequently \(F_3(n)/F_2(n)\to\infty\) but \(F_3(n)/F_1(n)\to0\): increasing the inner edge stride from one to two reduces equilibrium entropy, and increasing it again to three partially restores it. All three graph families have the same number \(2n\) of vertices and are cubic.

The new exact all-circumference stride-three census is

\[
F_3(n)=3+\sum_{P_{32}(\lambda)=0}\lambda^n+
\sum_{P_{33}(\mu)=0}\mu^n\qquad(n\ge7),
\]

with complex roots counted according to algebraic multiplicity. The integer polynomials \(P_{32},P_{33}\) are uniquely specified by the following coefficient vectors in **descending** order, including zeros:

```text
P32 = [1,0,-1,-2,-2,0,1,1,0,1,4,7,0,0,0,0,6,3,-7,-7,-8,-8,0,-1,-2,-3,-6,-2,0,-1,0,-1,-1]
P33 = [1,-1,1,-3,4,-4,5,-6,5,-1,-1,-1,1,-2,-4,4,-4,1,4,0,1,2,0,-1,-3,1,-3,-2,0,1,-1,1,0,1]
```

Equivalently, for \(d\in\{32,33\}\), if the corresponding vector is \((c_0,\ldots,c_d)\), then \(P_d(t)=\sum_{j=0}^d c_jt^{d-j}\). The spatial generating function is rational:

\[
\sum_{n\ge1}F_3(n)z^n
=\frac{3z}{1-z}-z\frac{d}{dz}\log\left(z^{65}P_{32}(1/z)P_{33}(1/z)\right).
\]

The displayed root-sum formula applies to actual simple generalized Petersen graphs at \(n\ge7\); formal coefficients at smaller \(n\) are not asserted as graph counts.

## Assumptions and scope

The simple graph \(GP(n,k)\) has outer vertices \(a_i\), inner vertices \(b_i\), and edges \(a_ia_{i+1}\), \(a_ib_i\), and \(b_ib_{i+k}\), with every index modulo \(n\). Here \(n>2k\), so the three neighbors of each vertex are distinct. Each vertex has a bit in \(\{0,1\}\) and, simultaneously at each step, adopts the strict majority among its three neighbors. A configuration is *fixed* if this update leaves all bits unchanged. These are dynamical equilibria, not all recurrent states or attraction basins.

A cubic-graph configuration is fixed precisely when every vertex has **at most one neighbor of the opposite bit**. Thus its bichromatic edge cut is a matching; two monochromatic configurations are included. This equivalence motivates studying an exact matching-cut count, rather than only the existence of a nontrivial cut.

Define equilibrium entropy per vertex as \(h_k=\lim_{n\to\infty}\log F_k(n)/(2n)=\tfrac12\log\alpha_k\).

## Proof

**1. Exact spatial transfer.** Put \(c_i=(a_i,b_i)\in\{0,1\}^2\), encoded by the four digits \(0,1,2,3\), with the low bit recording \(a_i\) and high bit recording \(b_i\). For each \(k\), form the directed graph \(\mathcal T_k\) on all \(4^{2k}\) words \((c_0,\ldots,c_{2k-1})\). Its edge from a word to its left-shifted successor with appended \(c_{2k}\) is present exactly when the center column \(c_k\) obeys both local fixed-point conditions:

\[
(a_{k-1}+a_{k+1}+b_k\ge2)\iff(a_k=1),
\qquad
(b_0+b_{2k}+a_k\ge2)\iff(b_k=1).
\]

Here both inequalities compare ordinary integer sums. Denote the adjacency matrix by \(T_k\). Every length-\(n\) closed walk, indexed starting at column zero, is in exact bijection with a fixed binary coloring on \(GP(n,k)\) for \(n>2k\): the overlapping windows enforce consistency, and every center constraint is checked once. Consequently

\[
F_k(n)=\operatorname{tr}(T_k^n),\quad n>2k.
\]

**2. Recurrent components and exact characteristic polynomials.** All graph vertices outside directed cycles contribute zero to every positive trace. Direct exhaustive construction of the finite transfer graphs gives, for \(k=1,2,3\), respectively, the numbers of directed vertices \(16,256,4096\) and edges \(20,320,5120\). Their cyclic strongly connected component sizes are, respectively, \((4,1,1)\), \((24,1,1)\), and \((124,1,1)\). Each singleton contributes a \(1\times1\) matrix \((1)\).

The exact characteristic polynomial of the main component, including all zero factors, is

\[
\begin{aligned}
k=1:&\quad (t^2-t-1)(t^2-t+1),\\
k=2:&\quad t^6Q_+(t)Q_-(t),\\
k=3:&\quad t^{58}(t-1)P_{32}(t)P_{33}(t),
\end{aligned}
\]

where

\[
\begin{aligned}
Q_+(t)&=t^9-t^8-t^7-t^4+2t^3+1,\\
Q_-(t)&=t^9-t^8-t^7+2t^6-t^4-1.
\end{aligned}
\]

The arrays above give the two previously unspecified polynomials. This proves the exact stride-three root-sum formula and independently reconstructs the comparison strata. The stride-one eigenvalues give \(F_1(n)=L_n+2+2\cos(n\pi/3)\), where \(L_n\) is the usual Lucas number. The stride-two spectrum agrees with the previously reported ninth-degree factors; it is comparison material, not claimed as a new census.

**3. Rigorous growth constants.** The main cyclic component for each stride is irreducible and contains a self-loop, hence primitive. The Perron–Frobenius eigenvalue is therefore simple, positive, and strictly greater in modulus than its other eigenvalues. For stride one, it is the golden ratio. For strides two and three, let \(A\) denote the respective main-component adjacency and \(\mathbf1\) its all-ones column vector. Exact integer inequalities for \(v=A^{38}\mathbf1\) (stride two) and \(v=A^{37}\mathbf1\) (stride three) give, coordinatewise,

\[
\begin{aligned}
1.56485v_i&<(Av)_i<1.56486v_i &&(k=2),\\
1.5965v_i&<(Av)_i<1.5966v_i &&(k=3).
\end{aligned}
\]

All coordinates of both \(v\) are positive. The Collatz–Wielandt bounds prove the claimed strict intervals; \(\varphi>1.6\) supplies the remaining inequality. Primitivity and simplicity yield \(F_k(n)\sim\alpha_k^n\), with leading coefficient one. This completes the entropy-rebound proof.

## Verification

`check_transfer.py` reconstructs all three directed graphs from the stated local constraints, identifies cyclic components, forms the exact integer adjacency matrices, checks each symbolic characteristic polynomial against the displayed factors and coefficient arrays, checks the interval root allocation for the stride-three factors, reproduces the small counts using Newton power sums, and verifies the integer Perron inequalities. It uses Python 3, SymPy and NetworkX with versions in `requirements.txt`.

`direct_check.cpp` is independent of the transfer method: it enumerates all \(2^{2n}\) binary colorings and tests both local strict-majority conditions at every column on each \(GP(n,k)\), for \(7\le n\le11\) and \(1\le k\le3\). Compile with `g++ -O3 -std=c++17 direct_check.cpp -o direct_check`, then run `./direct_check`. The saved `transfer_output.txt` and `direct_output.txt` are exact outputs from replayed checks.

| \(n\) | \(F_1(n)\) | \(F_2(n)\) | \(F_3(n)\) |
|---:|---:|---:|---:|
| 7 | 32 | 32 | 32 |
| 8 | 48 | 48 | 72 |
| 9 | 76 | 76 | 52 |
| 10 | 124 | 118 | 124 |
| 11 | 202 | 158 | 224 |
| 12 | 326 | 242 | 236 |

The small census is a check only; the all-size conclusion rests on the finite symbolic transfer proof, not extrapolation from numerical examples.

## Relationship to prior work

Classical majority-update dynamics and finite-graph eventual periods are established by Goles and Olivos (1980) and by later graph-based majority studies. The present contribution is an exact *population* and a nonmonotone *entropy comparison* for the generalized Petersen inner strides one, two, three, not general convergence to period two.

Existing ninth-degree strata for \(GP(n,2)\) already determine the stride-two equilibrium entropy and are used as comparison data; they do **not** determine the stride-three spectral factors. Karami's 2020 full-text classification of perfect two-colorings of \(GP(n,3)\) concerns equitable partitions, in which all vertices of a given color have exactly the same opposite-color degree. Most matching cuts need not satisfy that uniformity. For example, at \(n=8\), the fixed coloring with outer and inner binary words `00000011` and `01001011` (written most-significant bit first, vertex indices in increasing order from the right) has opposite-color degrees \(0\) and \(1\) among its zero vertices, so is not equitable. The published equitable-coloring parameter table therefore does not count all these equilibria.

Work on deciding matching-cut existence, including Gomes–Sau, is not by itself an exact fixed-point census on this family. The supporting references are not being presented as discoveries of the new recurrence or entropy ordering.

## Limitations

The theorem is restricted to **one-step fixed configurations** of ordinary three-regular \(GP(n,k)\) with \(k\in\{1,2,3\}\); it does not enumerate primitive two-cycles, transient attraction basins, graph-isomorphism orbits, or general inner strides. The equality with matching cuts includes two monochromatic assignments. The exact root-sum formula for stride three is valid only for \(n\ge7\), where the graph is simple cubic with the required neighborhood pattern.

The finite algebraic calculations are reproducible and internally checked but have not been independently audited externally. Historical priority may be affected by unindexed matching-cut enumerations or other unpublished records. No claim of unique historical priority is made.

## References

1. Goles, E.; Olivos, J. *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1
2. Mossel, E.; Neeman, J.; Tamuz, O. *Majority Dynamics and Aggregation of Information in Social Networks*, original public preprint 2012-07-04. https://arxiv.org/abs/1207.0893
3. Benjamini, I.; Chan, S.-O.; O'Donnell, R.; Tamuz, O.; Tan, L.-Y. *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, initial preprint 2014-05-11. https://arxiv.org/abs/1405.2486
4. Karami, H. *Perfect 2-colorings of the generalized Petersen graph GP(n,3)*, original preprint 2020-09-15. https://arxiv.org/abs/2009.07120
5. Gomes, G. C. M.; Sau, I. *Finding cuts of bounded degree: complexity, FPT and exact algorithms, and kernelization*, initial preprint 2019-05-08. https://arxiv.org/abs/1905.03134
6. Alaeiyan, M.; Karami, H. *Perfect 2-colorings of the generalized Petersen graph*, Proceedings of the Indian Academy of Sciences – Mathematical Sciences 126 (2016), 289–294. https://doi.org/10.1007/s12044-016-0285-4
