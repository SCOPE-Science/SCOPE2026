# An edge-addition entropy jump for majority fixed points on three-row cylinders

## Finding

For each integer \(n\ge3\), let \(G_n=C_n\square P_3\) be the simple three-row square cylindrical strip, with a binary state at each vertex. Apply synchronous open-neighbor majority: a state changes only when a strict majority of its neighbors favors the opposite state, and otherwise remains unchanged. Let \(F_n\) denote the number of **labelled configurations fixed after one update**. For a monic polynomial \(h\), write \(S_h(n)\) for the sum of the \(n\)th powers of its roots, with algebraic multiplicity. Define
\[
 p(X)=X^3-2X^2-1,\quad q(X)=X^3-X^2+X+1,\quad r(X)=X^5-2X^4+3X^3-3X^2-1.
\]
Then, for **all** \(n\ge3\),
\[
 \boxed{F_n=5+2(-1)^n+S_p(n)+S_q(n)+S_r(n).}
\]
The polynomial \(p\) has a unique real root \(\rho>2\), and
\[
 2.2055<\rho<2.2056,\qquad F_n=\rho^n+O(2^n),\qquad
 \lim_{n\to\infty}\frac{\log F_n}{3n}=\frac{\log\rho}{3}.
\]
An additional edge within each three-vertex column transforms \(C_n\square P_3\) into \(C_n\square K_3\). The previously established fixed-state count \(H_n\) on the latter graph obeys \(H_n=3^n+O(2^n)\). Therefore the exact asymptotic comparison is
\[
 \boxed{\frac{F_n}{H_n}\sim\left(\frac{\rho}{3}\right)^n.}
\]
Thus this natural edge addition **increases** the fixed-configuration exponential growth base from \(\rho\) to three; it is not an assertion of monotonicity for arbitrary edge additions.

## Assumptions and scope

Vertices are pairs \((j,i)\) with \(j\in\mathbb Z/n\mathbb Z\) and \(i\in\{0,1,2\}\). Neighbors are \((j-1,i)\), \((j+1,i)\), and \((j,i\pm1)\) when the latter row index exists. The cycle is simple and has distinct left and right neighbors for \(n\ge3\). The outer rows have degree three, and the middle row has degree four. Vertices and configurations are labelled; no quotient by symmetry is taken. At equality of the numbers of neighbors in the two states, the present state is retained. This theorem counts one-step fixed configurations, not eventual fixation basins or primitive two-cycles.

## Proof

Encode a column by a three-bit word \(b\in\{0,\ldots,7\}\), whose row bits are \(b_i\). For consecutive columns \((a,b,c)\), let
\[
 s_i(a,b,c)=a_i+c_i+\mathbf1_{i>0}b_{i-1}+\mathbf1_{i<2}b_{i+1},
 \qquad d_i=2+\mathbf1_{i>0}+\mathbf1_{i<2}.
\]
The middle column remains unchanged precisely when, for each row \(i\),
\[
 b_i=1\implies 2s_i\ge d_i,\qquad b_i=0\implies 2s_i\le d_i.
\]
Call this finite predicate \(L(a,b,c)\). On 64 states indexed by ordered column pairs, define the integral transfer matrix
\[
 T_{(a,b),(u,c)}=\mathbf1_{b=u}\,\mathbf1_{L(a,b,c)}.
\]
It has exactly 110 nonzero entries. There is a bijection between a cyclic string of \(n\) columns satisfying all majority-fixed predicates and a length-\(n\) closed walk in the pair-state graph, including its specified starting index. Hence \(F_n=\operatorname{tr}(T^n)\).

The explicit finite matrix, whose entries are fully determined above, satisfies the exact integer identity
\[
 \det(XI_{64}-T)=X^{46}(X-1)^5(X+1)^2p(X)q(X)r(X).
\]
The standalone standard-library program `verify.py` constructs all 64 rows from the predicate and proves this identity by exact integer characteristic-polynomial calculations on the strongly connected components, using Newton identities. This computation is finite and exhaustive; the mathematical statement for all \(n\) follows from the transfer-matrix bijection, not from extrapolating finite lengths. The trace of a matrix power equals the sum of the powers of its algebraic eigenvalues regardless of diagonalizability. The displayed formula for \(F_n\) follows.

For the error estimate, \(p'(X)=X(3X-4)\), and the two real critical values of \(p\) are negative. Thus \(p\) has exactly one real root \(\rho\), which lies in \((2,3)\) since \(p(2)=-1\) and \(p(3)=8\). Its other two roots have squared modulus \(1/\rho<1\), by their product and their conjugacy. Every root of \(q\) and \(r\) has modulus strictly smaller than two: apply the strict Schur reduction to the polynomials after substituting \(X=2z\). At each reduction, the absolute constant coefficient is smaller than the absolute leading coefficient. The exact integer certificates are given and independently reconstructed in `verify.py`. The roots \(\pm1\) are smaller as well. Consequently \(F_n=\rho^n+O(2^n)\).

The published triangular-cylinder formula on \(C_n\square K_3\) has simple leading eigenvalue three and every other root strictly below modulus two. Its \(H_n=3^n+O(2^n)\) identity therefore yields \(F_n/H_n\sim(\rho/3)^n\). This comparison holds with the same site count and identical tie-retaining rule.

## Verification

Run `python3 verify.py` using only the Python standard library. It constructs the exact 64-state integer matrix, tests its 110 allowed transitions, recomputes its characteristic polynomial via 20-state and singleton strongly connected components, and checks the claimed factorization. It verifies strict Schur certificates for \(q\) and \(r\), the trace counts for lengths three through twelve, and **independently** enumerates all \(2^{3n}\) vertex configurations for each \(n=3,4,5,6\). Both methods give \(F_3=8\), \(F_4=36\), \(F_5=78\), and \(F_6=146\). Further transfer counts are \(F_7=260\), \(F_8=572\), \(F_9=1304\), \(F_{10}=2848\), \(F_{11}=6058\), and \(F_{12}=13218\). Direct enumeration checks finite cases only; the transfer construction and exact polynomial factorization establish all lengths.

## Relationship to prior work

Agur, Fraenkel and Klein's 1988 study treats a one-dimensional majority cellular automaton and does not give the three-row coupled-strip spectrum. Benjamini, Chan, O'Donnell, Tamuz and Tan (first public arXiv posting May 11, 2014) establish general period-at-most-two behavior for finite symmetric majority, not a specialized fixed-configuration enumeration of cylindrical strips. The published *Exact majority-fixed census and entropy on triangular cylindrical strips* calculates \(H_n=3^n+O(2^n)\) for \(C_n\square K_3\), where all three rows form a triangle. Here the transversal graph is the path \(P_3\), which has different degree and tie structure. Its prior spectrum does not imply the new transfer polynomial or coefficient sequence; the old result is used only for the explicitly credited edge-addition comparison.

## Limitations

The theorem says nothing about basins, transient lengths, two-cycle counts, arbitrary strip widths, or universal monotonicity under graph edge additions. The exact characteristic factorization is a reproducible finite integer computation, not a hand-derived symbolic closed form; its full input and deterministic verification procedure are included. Literature searches and inspection cannot establish absolute historical priority against an unindexed equivalent enumeration. No independent external mathematical audit is asserted.

## References

1. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), 295–302. DOI: `10.1016/0012-365X(88)90005-2`. Lawful full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted May 11, 2014, https://arxiv.org/pdf/1405.2486.
3. *Exact majority-fixed census and entropy on triangular cylindrical strips*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-majority-fixed-census-and-entropy-on-triangular-cylindrica--874a8ff5f9e5.
