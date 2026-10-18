# Exact edgewise heat-envelope domination on equilateral pumpkin quantum graphs
## Finding
Let \(P_{N,\ell}\) be the compact metric graph consisting of \(N\ge2\) parallel edges of common length \(\ell>0\) joining two vertices, equipped with the standard continuity–Kirchhoff Laplacian, and let \(e\) be any edge. For the Harrell–Maltsev edgewise spectral heat envelope \(\widehat p_{P_{N,\ell}}(t,e)\), for every \(t>0\) one has the basis-independent exact identity \[\widehat p_{P_{N,\ell}}(t,e)=\frac{1}{N\ell}+\frac{2}{\ell}\sum_{m=1}^{\infty}\exp\!\left(-\left(\frac{m\pi}{\ell}\right)^2t\right).\] Consequently, if \(\widehat p_e(t,e)\) denotes the decoupled Neumann-edge envelope of Harrell–Maltsev, then \[\widehat p_e(t,e)-\widehat p_{P_{N,\ell}}(t,e)=\frac{N-1}{N\ell}>0\] for every \(t>0\). Thus the strict domination conjectured in their Remark 2.1 holds on every equilateral pumpkin, with a time-independent sharp gap; all positive-frequency edgewise \(L^\infty\)-spectral weight is exactly the same as on one decoupled Neumann edge, and the entire deficit comes from the zero mode.

## Assumptions and scope
The graph \(P_{N,\ell}\) has exactly two vertices and \(N\ge2\) parallel edges, each identified with \([0,\ell]\) in the same orientation. The operator is \(-d^2/dx^2\) on every edge, with continuity of function values and Kirchhoff sum-of-outgoing-derivatives conditions at both vertices. No potential is present. The heat envelope is precisely the quantity introduced by Harrell and Maltsev,
\[
\widehat p_\Gamma(t,e)=\frac1{|\Gamma|}+\sum_{j\ge1}e^{-\lambda_j t}\|\phi_j\|_{L^\infty(e)}^2,
\]
for an \(L^2(\Gamma)\)-orthonormal eigenbasis, with the zero eigenfunction represented by the separate constant term. The assertion is for every \(N\ge2\), every \(\ell>0\), every edge \(e\), and every \(t>0\).

## Proof
Fix a positive eigenvalue \(k^2\). On edge \(j\), write an eigenfunction as
\[
u_j(x)=a_j\cos(kx)+b_j\sin(kx).
\]
Continuity at the initial vertex forces all \(a_j=a\). Kirchhoff there gives \(\sum_j b_j=0\). Continuity at the terminal vertex says that \(a\cos(k\ell)+b_j\sin(k\ell)\) is independent of \(j\), and the terminal Kirchhoff condition, using \(\sum_jb_j=0\), gives \(Na k\sin(k\ell)=0\). If \(\sin(k\ell)\ne0\), then \(a=0\), terminal continuity forces all \(b_j\) equal, and \(\sum_jb_j=0\) forces the zero function. Hence every positive eigenvalue has
\[
k=\frac{m\pi}{\ell},\qquad m=1,2,\ldots.
\]
At such a level the eigenspace consists of one symmetric cosine direction and an \(N-1\)-dimensional sine space:
\[
u_j(x)=a\cos\left(\frac{m\pi x}{\ell}\right)+b_j\sin\left(\frac{m\pi x}{\ell}\right),\qquad \sum_{j=1}^N b_j=0.
\]
The zero eigenspace is one-dimensional and constant, so its normalized edgewise squared supremum is \(1/(N\ell)\).

It remains to compute the total edgewise squared-supremum weight of a positive eigenspace without choosing a preferred basis. For the displayed \(m\)-eigenspace,
\[
\|u\|_2^2=\frac{\ell}{2}\left(N|a|^2+\sum_j|b_j|^2\right).
\]
On a fixed edge \(e\), the interval of phase \(m\pi x/\ell\) has length at least \(\pi\), so
\[
\|u\|_{L^\infty(e)}^2=|a|^2+|b_e|^2.
\]
Summing this quadratic form over any orthonormal basis of the eigenspace is basis independent. In the natural orthogonal splitting into the symmetric cosine line and the coefficient hyperplane \(\mathbf 1^\perp\), the cosine contribution is \(2/(N\ell)\). The orthogonal projector onto \(\mathbf 1^\perp\subset\mathbb R^N\) is \(I-N^{-1}\mathbf 1\mathbf 1^T\), whose diagonal entries are \(1-1/N\). Therefore the sine contribution on edge \(e\) is
\[
\frac{2}{\ell}\left(1-\frac1N\right),
\]
and the total contribution of every positive eigenspace is exactly \(2/\ell\).

Since the eigenvalue at level \(m\) is \((m\pi/\ell)^2\), summing the heat weights gives
\[
\widehat p_{P_{N,\ell}}(t,e)=\frac1{N\ell}+\frac2\ell\sum_{m=1}^\infty e^{-(m\pi/\ell)^2t}.
\]
Harrell and Maltsev's decoupled Neumann edge has
\[
\widehat p_e(t,e)=\frac1\ell+\frac2\ell\sum_{m=1}^\infty e^{-(m\pi/\ell)^2t}.
\]
Subtracting proves the claimed constant gap \((N-1)/(N\ell)\).

## Verification
The accompanying `verify.py` checks with exact rational arithmetic that the projector \(I-N^{-1}\mathbf1\mathbf1^T\) is idempotent and has diagonal \(1-1/N\), and hence that the positive-level weight is exactly \(2/\ell\) for several values of \(N\) and rational \(\ell\). It then independently evaluates truncated heat sums for several \(N,\ell,t\) and checks that the decoupled-edge difference is \((N-1)/(N\ell)\). It also checks the associated finite-energy step count at several exact eigenvalue thresholds. Running the file prints `VERIFY_OK`.

## Relationship to prior work
Harrell and Maltsev define the edgewise envelope and the decoupled Neumann-edge theta-function envelope in their equations (5) and (6), prove a coarser graph-wide comparison in Theorem 2.1, and in Remark 2.1 conjecture strict edgewise domination by the decoupled edge for every finite metric graph more complicated than a single edge. Their worked strict example is a regular tetrahedral graph; their full text contains no pumpkin or parallel-edge specialization. The present formula verifies their conjectured comparison exactly on the full equilateral-pumpkin family and identifies the entire slack.

Kennedy and Rohleder study equilateral pumpkin graphs for a different question, namely extrema of first nontrivial eigenfunctions. Their Example 3.3 gives the first positive eigenspace: one common cosine mode and \(N-1\) vertex-vanishing directions, and Proposition 4.2 uses this to locate hot spots. Their paper does not study the Harrell–Maltsev heat envelope; a full-text search contains no occurrence of “heat kernel”. That first-eigenspace description is consistent with, but does not state, the all-level basis-independent envelope identity proved here.

Published-record searches for equivalent formulations under “pumpkin”, “dipole”, “parallel edges”, “heat envelope”, “theta function”, “edgewise spectral function”, and \(L^\infty\)-eigenfunction terminology returned no statement implying the formula. The closest retrieved record concerned an unrelated compact-cube spectral-gap comparison.

## Limitations
The proof uses equal edge lengths essentially. For non-equilateral pumpkins, the positive spectrum no longer collapses to one arithmetic progression and the exact cancellation with a single Neumann edge need not persist in this form. The result concerns the free standard Laplacian and the Harrell–Maltsev spectral envelope, not pointwise domination of the full heat kernel. No claim is made for potentials, other vertex couplings, or infinite graphs. Although the motivating conjecture is broader, only this equilateral-pumpkin family is proved here.

## References
1. E. M. Harrell II and A. V. Maltsev, *Localization and landscape functions on quantum graphs*, arXiv:1803.01186v2; Trans. Amer. Math. Soc. 373 (2020), DOI 10.1090/tran/7908. The edgewise envelope and Neumann-edge formula are equations (5)–(6), and the domination conjecture is Remark 2.1.
2. J. B. Kennedy and J. Rohleder, *On the hot spots of quantum graphs*, arXiv:2003.14335v4; Commun. Pure Appl. Anal. 20 (2021), DOI 10.3934/cpaa.2021095. See Example 3.3 and Proposition 4.2 for equilateral pumpkins.
