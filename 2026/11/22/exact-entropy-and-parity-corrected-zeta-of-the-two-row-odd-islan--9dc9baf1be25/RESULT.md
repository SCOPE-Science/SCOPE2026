# Exact entropy and parity-corrected zeta of the two-row odd-island shift

## Finding

Let \(Y\subset(\{0,1\}^2)^{\mathbb Z}\) consist of binary configurations on the infinite two-row ladder in which every **finite** connected component of occupied cells has odd cardinality; connectivity uses vertical rung edges and horizontal edges in each row. Let \(\sigma\) shift one column to the left. The exact Artin–Mazur zeta function is

\[
\zeta_Y(z)=\frac{(1+z)(1+z^2)}{(1+z-z^2)(1-4z+3z^2-5z^3+2z^4+z^5)},
\]
The accompanying horizontal entropy \(h_{\mathrm{top}}(Y,\sigma)=\log\lambda\) and the seven-state parity matrix also occur in the companion two-rail enumeration [4]; they are included for context, not claimed as new. Here \(\lambda\approx3.49756499717934\) is the Perron root of
\[
\lambda^5-4\lambda^4+3\lambda^3-5\lambda^2+2\lambda+1=0.
\]
In particular, if \(P_n=|\operatorname{Fix}(\sigma^n)|\), the complete periodic-point census follows from
\[
P_n=\operatorname{tr}(M^n)-\operatorname{tr}(W^n)\quad(n\ge1),
\]
for the explicit integer matrices in the proof. The correction term is essential: the right-resolving presentation has two state cycles for some horizontally infinite islands and none for others, even though all those occupied configurations are admissible.

## Assumptions and scope

At each integer column \(j\) the symbol is one of \(E=00\), \(T=10\), \(B=01\), or \(D=11\), with the first bit recording the upper row. Horizontal adjacency joins occupied cells in consecutive columns of the same row; vertical adjacency joins the two occupied cells of a \(D\) column. A connected component infinite in at least one horizontal direction is unrestricted. The system is the horizontal subshift obtained from the planar odd-component shift by requiring all rows outside two neighboring rows to be empty. There is **no** vertical periodic boundary condition. This paper computes invariants of this strip system, not the entropy or soficity of the unrestricted planar or higher-dimensional odd shift.

The zeta function is interpreted as a formal power series
\[
\zeta_Y(z)=\exp\!\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right).
\]

## Proof

**1. Seven-state parity presentation.** The active frontier of any column contains either no occupied cell (state \(E\)) or exactly one connected occupied component, because a \(D\) column connects the two rows. If its visible shape is \(T\), \(B\), or \(D\), retain the parity of the number of occupied cells in the component accumulated since its most recent left boundary, with subscript \(0\) for even and \(1\) for odd. For a component continuing indefinitely from the left, choose an initial parity; if that component ends, its parity must be odd. Thus the seven states are ordered
\[
(E,T_0,T_1,B_0,B_1,D_0,D_1).
\]
An edge is labelled by its new column. It is allowed precisely when a component cut off on the left has odd size, and then its new state is determined uniquely by the old state and column. The resulting unlabelled adjacency matrix (one edge per permitted label) is
\[
M=\begin{pmatrix}
1&0&1&0&1&1&0\\
0&0&1&0&0&1&0\\
1&1&0&0&1&0&1\\
0&0&0&0&1&1&0\\
1&0&1&1&0&0&1\\
0&0&1&0&1&1&0\\
1&1&0&1&0&0&1
\end{pmatrix}.
\]
For example, \(T_0\) can be followed by \(T\) (flipping parity to \(T_1\)) or by \(D\) (adding two cells without changing parity). It cannot be followed by \(E\) or \(B\), which would leave an even finite component. From \(T_1\), all four column labels are allowed, and a transition to \(B\) starts a new odd component.

Every bi-infinite labelled path satisfies the odd-finite-component rule. Conversely, consider any admissible infinite strip configuration. At a left endpoint of an occupied component, initialize the parity by the cells in its first column, update it along the component, and reset after its (necessarily odd) terminal column. A component infinite to the left may be initialized in whichever parity permits a finite right endpoint; a component unbounded in both directions admits either initialization. An \(E\) column and a \(T\)-to-\(B\) or \(B\)-to-\(T\) adjacency separate components. Since at most one component crosses any single column, these assignments give a bi-infinite state path. The labelled graph therefore presents exactly \(Y\).

**2. Entropy.** The graph is right-resolving: once a starting state and the next visible column are fixed, there is at most one outgoing edge. All seven states communicate (each reaches \(E\), and all are reachable from \(E\)); the loop \(E\to E\) makes \(M\) primitive. If \(p_Y(n)\) is the number of distinct length-\(n\) column words and \(S_n\) the total number of length-\(n\) graph paths, then
\[
S_n/7\le p_Y(n)\le S_n.
\]
Indeed, each visible word has between one and seven lifts (one per initial state). Perron–Frobenius theory yields \(\lim_{n\to\infty}n^{-1}\log S_n=\log\rho(M)\). Direct determinant expansion gives
\[
\det(tI-M)=(t^2+t-1)(t^5-4t^4+3t^3-5t^2+2t+1).
\]
The primitive Perron eigenvalue is the positive dominant root \(\lambda\) of the quintic, yielding the entropy formula.

**3. Periodic-point correction.** For a cyclic length-\(n\) sequence of visible columns, call a junction a *break* if one column is \(E\), or if it switches directly between \(T\) and \(B\). When there is a break, every occupied component of the repeated infinite strip is bounded by breaks and is finite. Its parity states are therefore uniquely determined by their initial columns. Consequently, an admissible cyclic visible word with a break has exactly one length-\(n\) state cycle in the seven-state graph, while an inadmissible word has none.

A cyclic visible word without a break uses only \(T,B,D\) and never switches directly between \(T\) and \(B\). It describes an occupied component spanning infinitely many columns, so it is **always admissible**. Let \(k\) be the number of \(T\) or \(B\) columns per period. Traversing the period changes frontier parity by \(k\bmod2\), since each \(D\) contributes two cells. Accordingly, such a visible word has two length-\(n\) state cycles if \(k\) is even and none if \(k\) is odd. Its correct contribution to \(P_n\) is one in both cases. Hence the needed difference from \(\operatorname{tr}(M^n)\) is \(-(-1)^k\).

The signed transfer matrix for no-break words is
\[
W=\begin{pmatrix}
-1&0&1\\
0&-1&1\\
-1&-1&1
\end{pmatrix},
\]
with row/column order \(T,B,D\), where a destination singleton column has sign \(-1\) and a destination double column has sign \(+1\). Every length-\(n\) closed walk in this matrix is precisely a cyclic no-break word, and its weight is \((-1)^k\). Thus
\[
P_n=\operatorname{tr}(M^n)-\operatorname{tr}(W^n).
\]
For any integer matrix \(A\), the formal identity \(\exp(\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n)=\det(I-zA)^{-1}\) follows from the formal logarithmic derivative. Here exact determinant calculations give
\[
\det(I-zW)=(1+z)(1+z^2),
\]
\[
\det(I-zM)=(1+z-z^2)(1-4z+3z^2-5z^3+2z^4+z^5).
\]
Their quotient is the asserted rational zeta function. This completes the proof.

## Verification

The standalone standard-library script `check.py` constructs the parity automaton, verifies both characteristic polynomials by exact integer arithmetic, and independently enumerates all \(4^n\) visible column words for each \(1\le n\le8\). It checks both the finite odd-component counts and the periodic-point counts by a component-graph search, with periodic words independently unfolded five times to detect their infinite components. Run `python3 check.py` in this package directory.

It performs 174,760 component admissibility decisions, and verifies the following exact initial period counts:
\[
(P_1,P_2,P_3,P_4,P_5,P_6,P_7,P_8)
=(4,14,40,158,514,1844,6374,22446).
\]
The script is a finite consistency check; it does not replace the infinite-language presentation, the Perron–Frobenius argument, or the all-period signed-cycle proof above.

## Relationship to prior work

Callard, *Soficity of multidimensional subshifts* (2025), Section 7.1, identifies the planar odd shift as the system whose finite occupied connected components have odd cardinality and describes its known soficity. Motivated by this concrete example, the present calculation concerns the first strip width permitting vertical connections, and determines its horizontal entropy and all-period dynamical zeta function, neither of which is calculated in the inspected thesis discussion. Hochman's problem note records the original planar odd-versus-even component question, but does not give strip counts.

The two-rail enumeration [4] gives the identical seven-state adjacency matrix (with different shape symbols), the same entropy, and the generating function of closed finite-ladder words with no wraparound. Those finite counts are not the periodic-point counts: for example there are three admissible closed one-column words but four period-one points. No precedence between the two computations of the entropy is asserted. The distinct result here is the all-period fixed-point and zeta formula. The additional step identifies precisely the periodic labels with zero or two lifts and sums their signed contributions. No novelty is claimed for general transfer-matrix or sofic zeta techniques.

## Limitations

The result is specific to an infinite **two-row** ladder with nearest-neighbor adjacency and odd finite connected components. It does not decide the unrestricted two-dimensional odd shift's soficity, supply a formula at arbitrary strip width, or imply a formula for the full spatial entropy in two dimensions. Published or unpublished equivalent exact strip computations may exist beyond the literature inspected; the present priority assessment is provisional. The script verifies finite cases, not an independent formal proof.

## References

1. A. Callard, *Soficity of multidimensional subshifts* (PhD thesis, defended publicly 2025-06-24), Section 7.1, p. 54. https://www.acallard.net/publications/thesis.pdf
2. M. Hochman, *Is the multidimensional odd shift sofic?* (problem note). https://math.huji.ac.il/~mhochman/problems/multidimensional-odd-shift.pdf
3. R. Pavlov, *Approximating the Hard Square Entropy Constant with Probabilistic Methods*, arXiv:1011.1983 (strip entropy as a related, different setting). https://arxiv.org/abs/1011.1983
4. *Exact two-rail entropy and closed-island counts for the odd-component shift*, Finding, Proof §1 and Limitations, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-two-rail-entropy-and-closed-island-counts-for-the-odd-comp--a2dd499263a3/RESULT.md
