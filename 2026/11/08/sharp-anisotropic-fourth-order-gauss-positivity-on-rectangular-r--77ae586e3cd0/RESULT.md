# Sharp anisotropic fourth-order Gauss positivity on rectangular rook graphs

## Finding

**Theorem (exact all-step endpoint positivity).** Let integers \(p,q\ge2\) and real \(a,b>0\) be arbitrary. Form the symmetric graph Laplacian
\[
L=aL(K_p)\otimes I_q+bI_p\otimes L(K_q),
\]
where all edges changing the first coordinate have conductance \(a\) and all edges changing the second have conductance \(b\). Apply the *completed endpoint* of the two-stage, order-four Gauss–Legendre Runge–Kutta method to \(u'=-Lu\):
\[
T(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\quad h\ge0.
\]
Set \(P=pa\), \(Q=qb\), \(r=P/Q\), and \(\phi(k)=(\sqrt{4k-3}-1)/2\). Then
\[
\boxed{T(h)\text{ is entrywise nonnegative for every }h\ge0
\quad\Longleftrightarrow\quad
\phi(p)\le r\le\frac1{\phi(q)}.}
\]
Whenever the inequalities hold, **every entry of \(T(h)\) is strictly positive for every finite \(h>0\)**. Whenever either inequality fails, an off-diagonal transition is negative for every sufficiently large \(h\). No restriction on intermediate Runge–Kutta stage vectors is asserted.

There exists *some* positive rate ratio \(a/b\) satisfying these inequalities exactly for the five unordered shapes
\[
\boxed{\{p,q\}\in\{\{2,2\},\{2,3\},\{2,4\},\{2,5\},\{3,3\}\}.}
\]
Thus, for the ten-vertex graph \(K_2\square K_5\), equal edge conductances fail for large steps, but choosing \(a/b=25/16\) makes the endpoint strictly positive at **every positive step**. This is the largest rectangular rook-graph order for which positive directional weighting can restore all-step positivity. The square \(K_3\square K_3\) permits it only at \(a=b\).

## Assumptions and scope

The graph is finite, undirected, connected, with at least two vertices in each factor. No degree normalization is applied. The factor weights \(a,b\) are positive and uniform *within* each coordinate direction; no claim is made for independently heterogeneous individual edges. The time step \(h\) ranges over all nonnegative real numbers. Positivity means preservation of the coordinatewise nonnegative cone by the completed endpoint map; it is exactly matrix entrywise nonnegativity. The method is not claimed to preserve positivity for arbitrary nonnegative generators or at internal stages.

## Proof

Write \(E_p=J_p/p\), \(H_p=I_p-E_p\), and analogously for \(q\). Since \(L(K_p)=pH_p\), the four orthogonal projectors \(E_p\otimes E_q\), \(H_p\otimes E_q\), \(E_p\otimes H_q\), \(H_p\otimes H_q\) have eigenvalues respectively \(0,P,Q,P+Q\). Therefore
\[
T=E_p\otimes E_q+F(hP)H_p\otimes E_q+F(hQ)E_p\otimes H_q+F(h(P+Q))H_p\otimes H_q.
\]
In particular \(T\boldsymbol1=\boldsymbol1\). Its diagonals are positive because \(F(z)>0\) for every \(z\ge0\): the numerator equals \((z-3)^2+3\), the denominator equals \((z+3)^2+3\), and the spectral projectors give a positive-definite real symmetric \(T\).

For an off-diagonal pair that differs only in the second coordinate, \(pq\) times its matrix entry is
\[
A_p(h)=1-F(hQ)+(p-1)\bigl(F(hP)-F(h(P+Q))\bigr).
\]
For a pair differing only in the first coordinate, the analogous expression is \(A_q(h)\) obtained by simultaneously interchanging \(p,P\) with \(q,Q\). For a pair differing in both coordinates, \(pq\) times its entry is
\[
C(h)=1-F(hP)-F(hQ)+F(h(P+Q)).
\]
Let \(D_h(x)=h^2x^2+6hx+12>0\), and put \(\Delta=D_h(P)D_h(Q)D_h(P+Q)\). Direct expansion using \(F(hx)=1-12hx/D_h(x)\) gives
\[
A_p(h)=\frac{12h}{\Delta}\,N_p(h),
\]
where the exact polynomial is
\[
\begin{aligned}
N_p(h)={}&144pQ+72Q(2P+pQ)h\\
&+12Q\bigl((6-p)P(P+Q)+pQ^2\bigr)h^2\\
&+6PQ(P+Q)\bigl(2P-(p-2)Q\bigr)h^3\\
&+PQ(P+Q)\bigl(P(P+Q)-(p-1)Q^2\bigr)h^4.
\end{aligned}
\]
Similarly
\[
C(h)=\frac{12h^2PQ}{\Delta}\left[
 h^3(P+Q)(P^2+PQ+Q^2)+12h^2(P+Q)^2+72h(P+Q)+144
\right]>0\quad(h>0).
\]
The leading coefficients of \(N_p\), \(N_q\) prove necessity: if \(P(P+Q)<(p-1)Q^2\), then \(A_p(h)<0\) for all sufficiently large \(h\), and the symmetric statement holds if \(Q(P+Q)<(q-1)P^2\). Thus simultaneous all-step positivity requires
\[
P(P+Q)\ge(p-1)Q^2,\qquad Q(P+Q)\ge(q-1)P^2.
\]
Dividing by \(Q^2\), respectively \(P^2\), proves precisely \(\phi(p)\le r\le1/\phi(q)\).

It remains to show these *necessary* conditions are sufficient, including equality. The interval is nonempty exactly when \(\phi(p)\phi(q)\le1\). The function \(\phi\) is strictly increasing, and \(\phi(3)=1\), \(\phi(4)>1\), \(\phi(2)\phi(5)<1<\phi(2)\phi(6)\). This gives exactly the five unordered shapes listed above. In every feasible pair, \(p,q\le5\). For every integer \(2\le k\le5\),
\[
\phi(k)\ge(k-2)/2
\]
(as follows on squaring from \(k^2-6k+4\le0\)). Hence the required \(r\ge\phi(p)\) ensures \(2P-(p-2)Q\ge0\), while \(p\le5\) ensures \((6-p)P(P+Q)+pQ^2>0\). All other coefficients of \(N_p\) are positive apart from the allowed zero leading coefficient. Consequently \(N_p(h)>0\) for every \(h>0\). By the reciprocal inequality and the same argument, \(N_q(h)>0\). Along with \(C(h)>0\) and positive diagonals, this proves strict entrywise positivity at every positive finite step, completing the equivalence.

For the example \((p,q)=(2,5)\), \(a/b=25/16\) yields \(r=5/8\), and the exact nonempty interval is
\[
\frac{\sqrt5-1}{2}\le r\le\frac{\sqrt{17}+1}{8}.
\]
Both inequalities are strict at \(5/8\); in contrast, equal weights give \(r=2/5\), below the lower endpoint, and thus eventual negativity. At \((p,q)=(3,3)\) the interval collapses to \(r=1\), which is equivalent to \(a=b\).

## Verification

The standalone Python 3 checker `verify.py` performs exact Fraction-arithmetic inversion of the Padé denominator and matches the resulting complete transition matrices against the four-projector formula. It also checks the polynomial numerator identities, selected edge and interior cases, the exact rational anisotropic rescue, and an independent finite enumeration of possible factor orders. The checker printed `VERIFY_OK 2135` when executed from the packaged source; the first-principles algebraic proof above establishes the infinite parameter claim, and finite tests are not used as a substitute for that proof.

## Relationship to prior work

The two-stage Gauss–Legendre method and absolute-monotonicity/SSP limitations belong to classical implicit Runge–Kutta theory; these general results do not imply this particular network-dependent positivity criterion. Horváth's general positivity-threshold theorems apply to broad IVP classes and invariant positive cones, and do not compute the endpoint sign pattern for this fixed rook family. Butcher's review discusses Gauss-based implicit schemes, and Ketcheson, Macdonald and Gottlieb study the (stronger, universal) SSP requirements rather than the present single-graph endpoint question. General graph-Laplacian positive integrators of Blanes, Iserles and Macnamara are different schemes, not a classification of the completed Gauss endpoint. The equal-conductance classification for products of complete graphs is an existing overlap boundary: no novelty is asserted for its recovered \(a=b\) specialization. The newly isolated issue is how independent *directional* rates change the possible shapes and produce the sharp rescue window for \(K_2\square K_5\).

## Limitations

The theorem is restricted to two complete-graph factors with uniform positive conductances inside each direction and to the completed Gauss endpoint. It does not determine all finite-step positivity windows outside the all-step domain. No independent mathematical audit or exhaustive publication-priority search of unindexed literature has been performed; a specialized older graph-filter treatment could contain an equivalent result. The source date in the metadata is the verified online-publication day of the focal Runge–Kutta reference, not a priority claim for this theorem. A related 2008-dated manuscript was inspected, but its earliest public-release day was not established.

## References

- J. C. Butcher, “Practical Runge–Kutta methods for scientific computation,” *The ANZIAM Journal* 50 (2009), DOI: 10.21914/anziamj.v50i0.2315. Online publication date 2009-11-19: https://journal.austms.org.au/ojs/index.php/ANZIAMJ/article/view/2315.
- D. I. Ketcheson, C. B. Macdonald, S. Gottlieb, “Optimal Implicit Strong Stability Preserving Runge–Kutta Methods,” *Applied Numerical Mathematics* 59 (2009), 373–392, DOI: 10.1016/j.apnum.2008.03.034. Author manuscript dated 2008-02-21: https://www.davidketcheson.info/assets/papers/implicit_ssp_postprint.pdf.
- Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* 53 (2005), 341–356, DOI: 10.1016/j.apnum.2004.08.026. Available online 2004-10-27.
- S. Blanes, A. Iserles, S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” *ESAIM: Mathematical Modelling and Numerical Analysis* 56 (2022), 1843–1870, DOI: 10.1051/m2an/2022042. https://opus.lib.uts.edu.au/bitstream/10453/170552/2/m2an210193.pdf.
