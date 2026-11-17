# Exact majority-fixed census and entropy on triangular cylindrical strips

## Finding

For every integer \(n\ge3\), let \(F_n\) be the number of configurations fixed after one synchronous majority update on \(C_n\square K_3\), where ties preserve the vertex's present binary opinion. Define \(S_h(n)=\sum_{h(\alpha)=0}\alpha^n\), counting polynomial roots with their algebraic multiplicities, and
\[
\begin{aligned}
 p(X)&=X^3+X+1,\\
 q(X)&=X^3-X^2-1,\\
 r(X)&=X^3-2X^2+X+1,\\
 s(X)&=X^4+X^2-3X-3.
\end{aligned}
\]
Then the exact labelled fixed-state census is
\[
\boxed{F_n=3^n+1+(-1)^n+2S_p(n)+S_q(n)+2S_r(n)+S_s(n).}
\]
All roots of these four polynomials have absolute value strictly below two. Consequently,
\[
 F_n=3^n+O(2^n),\qquad
 \lim_{n\to\infty}\frac{\log F_n}{3n}=\frac{\log3}{3},\qquad
 \frac{F_n}{2^{3n}}\sim\left(\frac38\right)^n.
\]
In particular, the exact exponential fixed-state growth base per three-vertex column is three.

## Assumptions and scope

The graph is the simple Cartesian graph product of a cycle \(C_n\), labelled cyclically by \(\mathbb Z/n\mathbb Z\), and the complete graph \(K_3\) labelled by \(\{0,1,2\}\). There is an edge between \((i,r)\) and \((i\pm1,r)\), and between \((i,r)\) and \((i,t)\) for each \(t\ne r\). Each vertex has four distinct neighbors for \(n\ge3\). At each time, if at least three neighbors are in state one then the vertex becomes one; if at most one is in state one it becomes zero; if exactly two are in state one the previous state is preserved. The count includes all vertex-labelled initial configurations satisfying one-step invariance; it does not count merely eventual fixed states or configurations in two-cycles.

## Proof

Encode the three bits in column \(i\) as an integer \(b_i\in\{0,1,\ldots,7\}\), with \(b_{i,r}\in\{0,1\}\) its bit \(r\). Define
\[
 v_r(a,b,c)=a_r+c_r+b_{r+1\bmod3}+b_{r+2\bmod3}.
\]
The central column \(b\) is unchanged after one update precisely when, simultaneously for \(r=0,1,2\),
\[
 [b_r=1\implies v_r(a,b,c)\ge2],\qquad
 [b_r=0\implies v_r(a,b,c)\le2].
\]
Write \(L(a,b,c)\) for the conjunction of these six inequalities. Index a finite integer matrix \(T\) by the 64 ordered pairs \((a,b)\in\{0,\ldots,7\}^2\). Set
\[
 T_{(a,b),(b',c)}=\begin{cases}
 1,&b=b'\text{ and }L(a,b,c),\\0,&\text{otherwise.}
 \end{cases}
\]
A closed walk of length \(n\) in this directed pair graph records exactly one cyclic column sequence \((b_0,\ldots,b_{n-1})\) satisfying all local fixed-state tests; conversely each such sequence yields one closed walk with the same initial pair. Hence \(F_n=\operatorname{tr}(T^n)\) for every \(n\ge3\). The matrix has exactly 182 nonzero entries.

Direct integer computation of this explicitly specified matrix gives the following identity in \(\mathbb Z[X]\):
\[
 \det(XI_{64}-T)=X^{42}(X-3)(X-1)(X+1)p(X)^2q(X)r(X)^2s(X).
\]
The included `check_transfer.py` constructs every entry from the preceding inequalities, computes this characteristic polynomial using exact symbolic arithmetic, and asserts the factorization. Since the trace of a matrix power is the sum of the corresponding powers of its eigenvalues counted with algebraic multiplicity, the claimed formula for \(F_n\) follows, regardless of diagonalizability.

For the root bound, substitute \(X=2z\) in each of \(p,q,r,s\). Apply the strict Schur reduction to a real polynomial \(h(z)=a_dz^d+\cdots+a_0\): if \(|a_0|<|a_d|\), all its zeros lie in the open unit disk if and only if the same holds for
\[
 h_*(z)=\frac{a_dh(z)-a_0z^dh(1/z)}{z},
\]
which has degree \(d-1\), up to a nonzero scalar. The following pairs \((a_d,a_0)\) occur successively after removal of common integer factors:
\[
\begin{array}{c|l}
 p &(8,1),(63,16),(79,-2)\\
 q &(8,-1),(63,-4),(59,-32)\\
 r &(8,1),(21,8),(29,-22)\\
 s &(16,-3),(247,-96),(51793,17044),(3623,150).
\end{array}
\]
Each pair satisfies \(|a_0|<|a_d|\); the last reduction is a nonzero constant. The attached checker verifies every pair using integer polynomial arithmetic. Every root of each original polynomial therefore lies in \(|X|<2\). The dominant eigenvalue 3 has multiplicity one and all other eigenvalues have modulus at most two, giving the claimed error estimate and entropy and density limits.

## Verification

`check_transfer.py` (Python with SymPy) recomputes the 64-state matrix, the 182 transition count, its complete characteristic polynomial factorization, the strict Schur reductions, and the exact trace values through \(n=11\). `check_direct.py` (Python standard library) independently implements the synchronous majority update and exhaustively enumerates all \(2^{3n}\) configurations for each \(3\le n\le7\). The computations agree, giving \(F_3,\ldots,F_{11}\) as \(32,94,218,712,2234,6550,19670,59560,177812\). The direct enumeration checks 2,396,672 states in total. Both scripts and captured outputs are provided verbatim and can be rerun. This finite check is not an infinite proof; the transfer-matrix identity and Schur reduction supply the all-size argument.

## Relationship to prior work

Agur, Fraenkel and Klein (1988) enumerated fixed points for the one-dimensional majority rule on a single cycle, with self-inclusive local voting. Nakar and Ron (2022) describe periodic configurations in one-dimensional cyclic majority cellular automata. Neither model contains the coupled triangular three-vertex column and four-neighbor tie-retaining condition above. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014, first public preprint) establish periodicity and disagreement results for majority dynamics on general graphs, without a graph-family-specific fixed-point count. In particular, the eventual-period-at-most-two theorem does not yield the number of initial fixed configurations. The present exact spectral identity therefore resolves an additional finite-graph counting question not implied by those results.

## Limitations

The formula counts one-step fixed points only, not primitive two-cycles, transient basins or their attraction times. It assumes labelled vertices, \(n\ge3\), and a zero-tie-change rule. This analysis does not establish priority against all unpublished or unindexed transfer enumerations of the same graph. The general historical existence of majority transfer methods does not itself establish the particular polynomial factors without calculation. The numeric checking range does not independently certify all graph sizes.

## References

- Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302. DOI: 10.1016/0012-365X(88)90005-2. Open full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (11 May 2014). https://arxiv.org/pdf/1405.2486
- Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (2022). https://arxiv.org/pdf/2205.08972
