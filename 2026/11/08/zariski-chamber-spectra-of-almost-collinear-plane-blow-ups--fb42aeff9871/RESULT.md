# Zariski chamber spectra of almost-collinear plane blow-ups

## Finding
Let \(n\geq3\), and let \(X_n\) be the blow-up of \(\mathbb P^2_{\mathbb C}\) at \(n+1\) distinct points, of which \(p_1,\ldots,p_n\) lie on a single line \(\ell\) and \(p_*\notin\ell\). If \(z_j(X_n)\) counts the Zariski chambers of the big cone whose negative parts have exactly \(j\) irreducible components, with the nef chamber contributing \(z_0=1\), then their complete support polynomial is
\[
\begin{aligned}
Z_n(t)&=\sum_{j\geq0} z_j(X_n)t^j\\
&=(1+2t)^n+t(1+t)^n\\
&\quad+t\sum_{k=0}^{n-2}\binom nk t^k(1+t)^{n-k}
+t^2\sum_{k=0}^{n-2}\binom nk t^k.
\end{aligned}
\]
In particular, for every integer \(n\geq3\),
\[
 z(X_n)=Z_n(1)=2\cdot3^n+2\cdot2^n-3n-2.
\]
The maximum negative-support size is \(n+1\), and precisely \(2^n-n\) chambers attain it. The first three support polynomials (for \(n=3,4,5\)) have respective coefficient vectors
\[(1,8,22,23,5),\quad(1,10,37,66,54,12),\quad(1,12,56,135,180,122,27).\]
Thus these surfaces have arbitrarily large Picard number but finitely many chambers, with chamber totals asymptotic to \(2\cdot 3^n\).

## Assumptions and scope
The ground field is \(\mathbb C\). The points are distinct, no three-point general-position assumption is made beyond the stated common-line condition, and there are exactly \(n+1\) blow-up centers. Write \(H\) for the pullback of a line and \(E_i,E_*\) for the exceptional curves. Set
\[
R=H-\sum_{i=1}^nE_i,\qquad L_i=H-E_i-E_*.
\]
The notation \(R\) and \(L_i\) denotes the corresponding strict-transform curves as well as their divisor classes. The support polynomial refers to the negative part in Zariski decompositions of big real divisor classes on the smooth blow-up, not to Mori chambers or to a singular contraction.

## Proof
**(1) Exhaustion of negative curves.** The curves \(E_1,\ldots,E_n,E_*\) and \(L_1,\ldots,L_n\) have self-intersection \(-1\), while \(R^2=1-n\). They are all irreducible. Suppose another irreducible curve \(C\) on \(X_n\) had negative self-intersection. Its plane image is an irreducible plane curve of degree \(d\geq1\), distinct from \(\ell\) and from every line \(p_ip_*\), with multiplicities \(m_i\) at \(p_i\) and \(m_*\) at \(p_*\). Bézout's theorem applied to \(\ell\) and to each line \(p_ip_*\) yields
\[
\sum_{i=1}^nm_i\leq d,\qquad m_i+m_*\leq d\quad(1\leq i\leq n),\qquad 0\leq m_*\leq d.
\]
Consequently,
\[
\sum_{i=1}^nm_i^2\leq(d-m_*)\sum_{i=1}^nm_i\leq d(d-m_*),
\]
and therefore
\[
C^2=d^2-m_*^2-\sum_{i=1}^nm_i^2\geq m_*(d-m_*)\geq0,
\]
a contradiction. Thus these \(2n+2\) curves are the complete negative-curve list for all \(n\geq3\).

**(2) Intersection-graph restriction.** Among the \((-1)\)-curves, the only nonzero intersections between distinct curves are
\[
 E_i\cdot L_i=1,\qquad E_*\cdot L_i=1\quad(1\leq i\leq n).
\]
Also \(R\cdot E_i=1\), while \(R\cdot E_*=R\cdot L_i=0\). A negative-definite collection of \((-1)\)-curves must be pairwise disjoint, since two intersecting \((-1)\)-curves give a singular \(2\times2\) intersection minor. Conversely, any disjoint collection has intersection matrix \(-I\). If a collection contains \(R\) and its other curves are pairwise disjoint, let \(k\) be the number of selected \(E_i\) for \(1\leq i\leq n\). The Schur complement of the \(-I\) block in the intersection matrix is \(-(n-1)+k\). The whole matrix is negative definite exactly when \(k\leq n-2\).

**(3) Count every possible support.** The negative-definite-support correspondence identifies these collections, together with the empty support, with Zariski chambers [BFN, Proposition 1.1]. Supports not containing \(R\) split into those without \(E_*\), with three alternatives (none, \(E_i\), \(L_i\)) at each \(i\), and those with \(E_*\), where only \(E_i\) can be added. They contribute \((1+2t)^n+t(1+t)^n\). Supports containing \(R\) without \(E_*\) have \(k\) selected \(E_i\), then an arbitrary selection of \(L_i\) at the other \(n-k\) indices; the restriction is \(0\leq k\leq n-2\). They contribute \(t\sum_{k=0}^{n-2}\binom nk t^k(1+t)^{n-k}\). Supports containing both \(R\) and \(E_*\) cannot contain any \(L_i\) and contribute \(t^2\sum_{k=0}^{n-2}\binom nk t^k\). Adding all four disjoint cases proves the polynomial.

At \(t=1\), the two truncated sums equal \(3^n-2n-1\) and \(2^n-n-1\). Therefore the chamber total is \(2\cdot3^n+2\cdot2^n-3n-2\). The largest supports have \(n+1\) curves: one is \(E_*+E_1+\cdots+E_n\), and the others are \(R\) plus one of \(E_i,L_i\) for every \(i\), excluding the \(n+1\) choices with at least \(n-1\) of the \(E_i\). Hence the top coefficient is \(1+(2^n-n-1)=2^n-n\).

## Verification
Run `python3 verification/check.py` using only the Python standard library. The standalone finite verifier builds the full integral intersection matrix, applies the exact Bareiss determinant algorithm and Sylvester's criterion to **every** subset of its \(2n+2\) negative curves for \(n=3,4,5\), independently tests the combinatorial characterization, and compares the enumerated support polynomial with the closed formula. It also checks the binomial formula through \(n=10\). The recorded execution is in `verification/output.txt`. Exhaustive finite checks verify only their stated values; the all-\(n\) theorem follows from the Bézout and Schur-complement proof above.

## Relationship to prior work
Bauer, Funke and Neumann [BFN] prove the correspondence between chambers and negative-definite curve supports and calculate chamber numbers for smooth del Pezzo surfaces with general centers; that correspondence is used here, not claimed as new. Bauer and Schmitz [BS] develop efficient enumeration for high-Picard-number examples, particularly lines on a quartic K3 surface. Bauer, Pokora and Schmitz [BPS] analyze negative curves and Zariski denominators when **all** points lie on a line; their special configuration has a different intersection graph from the added off-line point here. The new assertion is the complete \(n\)-parameter support polynomial for the almost-collinear configuration, based on its complete negative-curve classification and Schur-bound. These antecedents should be consulted in independent priority evaluation.

## Limitations
The result covers only distinct centers with all but one collinear and only over \(\mathbb C\). It does not compute chamber volumes, the nef cone's entire face lattice, or denominators of individual Zariski decompositions. The result is proved, but its historical novelty has not been independently audited; unlocated specialized examples may exist. Computational verification is exhaustive only for \(n=3,4,5\), not for arbitrary \(n\).

## References
[BFN] T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958, first posted 2009-12-04. https://arxiv.org/abs/0912.0958

[BS] T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373, first posted 2012-04-19. https://arxiv.org/abs/1204.4373

[BPS] T. Bauer, P. Pokora, D. Schmitz, *On the boundedness of the denominators in the Zariski decomposition on surfaces*, arXiv:1411.2431, first posted 2014-11-10, especially Example 3.4. https://arxiv.org/abs/1411.2431
