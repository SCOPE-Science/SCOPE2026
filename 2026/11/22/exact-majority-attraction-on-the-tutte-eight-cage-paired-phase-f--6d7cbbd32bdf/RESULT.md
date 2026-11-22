# Exact majority attraction on the Tutte eight-cage: paired phase fibers and a four-update clock

## Finding

On the thirty-vertex Tutte–Coxeter graph, synchronous binary open-neighbor majority has exactly **2,386 fixed configurations** and **2,845,305 primitive temporal two-cycle orbits**. Its global update map satisfies the sharp identity
\[
F^{6}=F^{4},\qquad F^{5}\ne F^{3}.
\]
The complete attraction-basin distribution is determined by the nine paired shore-fiber types in the table below. In particular, **240 fixed configurations have basin size 836**, because their point and line phase fibers have unequal sizes 22 and 38 in opposite orientations. The largest primitive two-cycle basin has size **38,579,328** and occurs exactly once.

Write \((a,b;m)\) for \(m\) phase labels with point-shore fiber weight \(a\) and corresponding line-shore fiber weight \(b\):

| \(a\) | \(b\) | \(m\) |
|---:|---:|---:|
| 1 | 1 | 144 |
| 3 | 3 | 720 |
| 5 | 5 | 720 |
| 6 | 6 | 360 |
| 22 | 38 | 120 |
| 38 | 22 | 120 |
| 42 | 42 | 180 |
| 58 | 58 | 20 |
| 4392 | 4392 | 2 |

More precisely, index these nine rows by \(r\), and write their entries \((a_r,b_r,m_r)\). Define the two polynomials
\[
\begin{aligned}
B_1(z)&=\sum_r m_r z^{a_r b_r},\\
B_2(z)&=\sum_r\binom{m_r}{2}z^{2a_rb_r}
       +\sum_{r<s}m_rm_s z^{a_rb_s+a_sb_r}.
\end{aligned}
\]
Then the coefficient of \(z^k\) in \(B_1\) (respectively \(B_2\)) is exactly the number of fixed points (respectively primitive two-cycle orbits) whose **entire attraction basin** contains \(k\) labelled initial configurations. Thus the table and the two displayed finite polynomials specify every individual basin-size multiplicity without a large list of special cases.

The complete first-periodic-entry census, counting initial states by their smallest \(t\) for which \(F^t\) is periodic, is:

| \(t\) | Number of states |
|---:|---:|
| 0 | 5,692,996 |
| 1 | 276,815,868 |
| 2 | 352,934,400 |
| 3 | 180,687,360 |
| 4 | 257,611,200 |

The five counts sum to \(2^{30}=1,073,741,824\).

## Assumptions and scope

Let \(X=\{0,1,2,3,4,5\}\). The fifteen **duads** are the two-element subsets of \(X\); the fifteen **synthemes** are the partitions of \(X\) into three duads. Connect a duad to a syntheme exactly when the duad is one of its three constituent pairs. This is the classical thirty-vertex cubic Tutte eight-cage (the Levi graph of the generalized quadrangle of order \((2,2)\)). Each vertex has three neighbors. There are no loops or self-votes. At each simultaneous update, the new value at a vertex is one if and only if at least two of its three neighbors presently have value one. No ties occur.

All configurations are **labelled** with the lexicographic duad and syntheme conventions in the accompanying programs. A primitive temporal orbit is counted once up to cyclic rotation, but no spatial automorphism or bit complementation is quotiented out. The basin of a periodic orbit consists of *all* initial states eventually entering that orbit, including periodic states themselves.

For a set of selected duads \(U\), define \(\Phi(U)\) to be the synthemes containing at least two members of \(U\). For a set of selected synthemes \(V\), define \(\Psi(V)\) to be the duads belonging to at least two members of \(V\). On the two shores the full synchronous update is
\[
F(U,V)=(\Psi(V),\Phi(U)).
\]
Define the shore maps \(P=\Psi\circ\Phi\) and \(Q=\Phi\circ\Psi\), each acting on exactly \(2^{15}=32,768\) binary inputs.

## Proof

**1. Exact shore exhaustion.** The duads and synthemes above are constructed without external graph tables: enumerate the fifteen two-subsets and the fifteen perfect matchings of six symbols. Each duad lies in precisely three synthemes and each syntheme contains precisely three duads. For every fifteen-bit input \(u\), evaluate the two incidence-majority maps using the three-neighbor rule. The two standalone exhaustive certificates apply this rule to *all* \(32,768\) inputs on each shore and verify
\[
P^3(u)=P^2(u),\qquad Q^3(u)=Q^2(u).
\]
These are finite universal equalities established by full enumeration, not interpolated from samples. The same exhaustive checks determine the fixed-point sets \(R=\operatorname{Fix}(P)\) and \(S=\operatorname{Fix}(Q)\), each of size exactly 2,386, and the nine paired fiber types in the Finding. The displayed numbers are independently recomputed by both certificate programs, one by bitwise Boolean truth tables and the other by direct neighbor sums and a separately generated incidence representation.

**2. Periodic phases.** From \(F^2(U,V)=(P(U),Q(V))\) and the finite equalities, \(F^6=F^4\). Every state is therefore periodic by four updates, and the full periodic configuration set is \(R\times S\). Indeed, an element of this product obeys \(F^2(U,V)=(U,V)\), and no state outside it is already periodic. On \(R\), the map \(\Phi\) is a bijection to \(S\) with inverse \(\Psi\): if \(U\in R\), then \(\Psi\Phi(U)=U\); if \(V\in S\), then \(\Phi\Psi(V)=V\). Consequently each periodic state has a unique representation \((U,\Phi(W))\), where \(U,W\in R\), and its next state is \((W,\Phi(U))\). This swaps two labels from an alphabet of size 2,386, yielding exactly \(2,386\) fixed points and \(\binom{2386}{2}=2,845,305\) primitive two-cycle orbits, with no other periods.

**3. Basin weights and paired asymmetry.** Because \(P^3=P^2\), define the point-fiber weight \(w_D(U)=|\{u:P^2(u)=U\}|\) for \(U\in R\). Similarly define \(w_M(V)=|\{v:Q^2(v)=V\}|\) for \(V\in S\). The full enumeration gives precisely the nine triples \((w_D(U),w_M(\Phi(U));\text{multiplicity})\) above; in particular 120 labels have ordered weights \((22,38)\) and another 120 have \((38,22)\). These weights describe different **sets of initial shore states** and need not coincide even though the underlying graph is self-dual.

The \(F^2\)-basin of a periodic state \((U,\Phi(W))\) is the Cartesian product of the corresponding shore fibers, of size \(w_D(U)w_M(\Phi(W))\). A fixed point uses \(U=W\), so its basin size is \(a_U b_U\). A primitive two-cycle with distinct phase labels \(U,W\) consists of the two disjoint \(F^2\)-fixed states \((U,\Phi(W))\) and \((W,\Phi(U))\); its basin size is
\[
a_Ub_W+a_Wb_U.
\]
Grouping unordered pairs by the nine finite types yields exactly \(B_1\) and \(B_2\). The weighted sum of all their coefficients is
\[
B_1'(1)+B_2'(1)=\left(\sum_U a_U\right)\left(\sum_U b_U\right)
=32,768^2=2^{30},
\]
so every labelled initial state is accounted for. The fixed basin 836 comes from both orientations of \(22\cdot38\), and the unique largest two-cycle basin is \(2\cdot4392^2=38,579,328\).

**4. Sharp entrance times.** Since membership in the periodic set means that each shore coordinate is fixed under its two-step map, separability of \(F^t\) lets us count the states already periodic at each \(t\) by multiplying two independently enumerated fifteen-bit counts. The counts through times zero to four are, respectively,
\[
2386^2,\quad16808^2,\quad25208^2,\quad28568^2,\quad32768^2.
\]
Successive differences give the entrance table. Sharpness is witnessed by the labelled state with point-shore mask 106 and line-shore mask zero. Its evolution includes \((72,0)\) at time two, \((0,1024)\) at time three and \((0,0)\) at time four, so time three is still transient. Therefore \(F^5\ne F^3\), completing the proof.

## Verification

`check_primary.py` enumerates all binary inputs on each fifteen-vertex shore, constructs the two exact majority tables and their compositions, asserts the universal power identities, determines all paired fiber weights, evaluates the two basin polynomials and computes all periodic-entry layers. Run `python3 check_primary.py`. Its expected machine-readable output is `primary_results.json`.

`check_scalar.py` separately constructs the fifteen synthemes from permutations of six symbols, computes the majority rule using integer neighbor sums, enumerates the full shore spaces and obtains the same nine paired weights and the complete basin census by traversing phase-label pairs. It also checks actual thirty-vertex trajectories including the sharp witness. Run `python3 check_scalar.py`; its expected output is `scalar_results.json`. Both programs were executed successfully with all assertions active. Neither output file substitutes for source code or a mathematical proof; the finite exhaustion plus the exact shore factorization establishes the claim.

## Relationship to prior work

Coxeter's 1958 paper identifies the Tutte eight-cage with the duad–syntheme incidence graph; that geometry is classical and is not claimed as new. Goles and Olivos (1980) establish eventual period at most two for symmetric threshold networks. Kuhlman, Mortveit, Murrugarra and Kumar (arXiv:1108.2974, 2011) give a broader threshold-network setting and its period-two limit. Adam, Dahleh and Ozdaglar (arXiv:1211.0654, 2012) discuss bipartite expansions, general convergence bounds and complexity of counting recurrent threshold states. None of these general results supplies the actual nine paired fibers or any exact basin count on the present thirty-vertex graph.

The previously published Heawood graph census uses a related bipartite phase-swap method, but its seven-point Fano incidence geometry has a one-step idempotent shore map, only 58 phase labels and balanced phase weights. It does not imply the present fifteen-vertex shore classifications, two-step projection, or unequal corresponding phase weights. The new mathematical content is specifically the exact doily shore-fiber classification, the resulting all-orbit basin polynomial and the sharp entry clock, not the generic phase-swap argument.

## Limitations

This is a finite exact result for the thirty-vertex Tutte–Coxeter graph and the stated synchronous, binary, open-neighbor threshold-two rule. It does not assert a universal formula over all generalized quadrangles, bipartite cubic graphs, or other update schemes. The finite enumeration is exhaustive by the program loops and independently checked code paths, but no external mathematical audit has been performed. A literature/database search cannot exclude unindexed or differently phrased prior exact tabulations; the historical-priority assessment is qualified accordingly.

## References

1. H. S. M. Coxeter, *The Chords of the Non-Ruled Quadric in PG(3,3)*, Canadian Journal of Mathematics 10 (1958), 484–488, https://doi.org/10.4153/CJM-1958-047-0 . Open full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6942435F6DBABA34132E1B56A3D2A44B/S0008414X0004551Xa.pdf/the-chords-of-the-non-ruled-quadric-in-pg3-3.pdf .
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
3. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974, first public preprint 2011-08-15, https://arxiv.org/abs/1108.2974 .
4. E. M. Adam, M. A. Dahleh and A. Ozdaglar, *On Threshold Models over Finite Networks*, arXiv:1211.0654, first public preprint 2012-11-04, https://arxiv.org/html/1211.0654v2 .
5. *A two-step majority projection and exact attraction basins on the Heawood graph*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 .
