# Unconditional Radau IIA positivity on Hamming graphs: the exact dimension–alphabet frontier

## Finding
Let \(H(d,q)=K_q^{\square d}\) be the unweighted Hamming graph with integers \(d\geq1\) and \(q\geq2\), and let \(L_{d,q}\) be its combinatorial Laplacian. Apply the unmodified two-stage, third-order Radau IIA Runge–Kutta method to \(u'=-L_{d,q}u\). Its completed step is \(T_{d,q}(h)=R(hL_{d,q})\), with
\[
R(x)=\frac{6-2x}{x^2+4x+6}.
\]
Then the following classification is exact:
\[
T_{d,q}(h)\text{ is entrywise nonnegative for every }h\ge0
\quad\Longleftrightarrow\quad
\begin{cases}
d=1,\;2\le q\le11,\\
d=2,\;q=2\text{ or }3,\\
d=3,\;q=2.
\end{cases}
\]
For every permitted pair, all entries are strictly positive at every \(h>0\). In every other pair there exists a positive timestep at which an entry is negative. The transitions retain unit row sums for all \(h\ge0\), whether or not entrywise positivity holds.

## Assumptions and scope
Graphs are finite, simple, undirected, unweighted Cartesian powers of a complete graph; \(H(d,q)\) has \(q^d\) vertices and diameter \(d\). No restriction is placed on \(h\ge0\). The assertion concerns the completed Runge–Kutta end-step, not positivity of its internal stages, generic right-hand sides or all graph topologies. At \(h=0\), \(T_{d,q}(0)=I\), so strict positivity is asserted only for positive steps.

## Proof
### Exact radial spectral projectors
Write \(E_0=J_q/q\) and \(E_1=I_q-J_q/q\), the projections onto constant and mean-zero vectors in one coordinate. Since \(L(K_q)=qE_1\), the commuting Cartesian-sum Laplacian has the exact expansion
\[
T_{d,q}(h)=\sum_{S\subseteq[d]}R(q|S|h)
\bigotimes_{i=1}^d E_{\mathbf 1_{i\in S}}.
\]
An entry depends only on the Hamming distance \(r\) between its two vertices. Denote this entry by \(K_r^{(d,q)}(h)\). For \(0\le r\le d\), its explicit formula is
\[
K_r^{(d,q)}(h)=q^{-d}\sum_{k=0}^{d}R(qkh)
\sum_{j=\max(0,k-d+r)}^{\min(r,k)}
(-1)^j\binom rj\binom{d-r}{k-j}(q-1)^{k-j}.
\tag{1}
\]
All denominators \(q^2k^2h^2+4qkh+6\) are positive for \(h\ge0\). For the diagonal, putting \(p=(q-1)/q\) gives
\[
K_0^{(d,q)}(h)=\sum_{k=0}^d\binom dk p^k(1-p)^{d-k}R(qkh).
\tag{2}
\]
Also \(R(0)=1\), so \(T_{d,q}(h)\mathbf1=\mathbf1\).

### All-time positive cases
For \(d=1\), the diagonal and off-diagonal entries are, respectively, \([1+(q-1)R(qh)]/q\) and \([1-R(qh)]/q\). For \(x\ge0\),
\[
R(x)+\frac1{10}=\frac{(x-8)^2+2}{10(x^2+4x+6)}>0,
\qquad 1-R(x)=\frac{x(x+6)}{x^2+4x+6}>0\quad(x>0).
\]
Thus the diagonal and off-diagonal entries are strictly positive at positive steps for all \(q\le11\).

For the remaining permitted pairs, direct substitution into (1) yields the exact radial numerators below, with common denominator in each case. Every displayed denominator is positive for \(h\ge0\).

For \((d,q)=(2,2)\), set \(D=(2h^2+4h+3)(8h^2+8h+3)\). Then
\[
K_0=\frac{4h^4+2h^3+17h^2+18h+9}{D},\quad
K_1=\frac{h(2h+3)}{8h^2+8h+3},\quad
K_2=\frac{h^2(4h^2+18h+9)}{D}.
\]

For \((d,q)=(2,3)\), set \(D=(3h^2+4h+2)(6h^2+4h+1)\). Then
\[
\begin{aligned}
K_0&=\frac{2h^4-4h^3+3h^2+4h+2}{D},\\
K_1&=\frac{h(2h^3+4h^2+5h+2)}{D},\\
K_2&=\frac{2h^2(h^2+3h+1)}{D}.
\end{aligned}
\]
The only numerator with a negative coefficient remains positive, since \(2h^4-4h^3+3h^2=h^2(2(h-1)^2+1)\).

For \((d,q)=(3,2)\), set \(D=(2h^2+4h+3)(6h^2+4h+1)(8h^2+8h+3)\). Then
\[
\begin{aligned}
K_0&=\frac{12h^6-14h^5+22h^4+83h^3+98h^2+45h+9}{D},\\
K_1&=\frac{h(12h^5+42h^4+92h^3+95h^2+45h+9)}{D},\\
K_2&=\frac{h^2(12h^4+58h^3+76h^2+45h+9)}{D},\\
K_3&=\frac{3h^3(4h^3+22h^2+18h+3)}{D}.
\end{aligned}
\]
The quadratic \(12h^2-14h+22\) has negative discriminant, so the leading three terms of \(K_0\)'s numerator are \(h^4(12h^2-14h+22)>0\) for \(h>0\); all other terms are nonnegative. This proves every permitted case.

### Failure in all other cases
When \(d=1\) and \(q\ge12\), take \(h=8/q\). Since \(R(8)=-5/51\), the diagonal is \((56-5q)/(51q)<0\).

When \(d=2\) and \(q\ge4\), take \(h=6/q\) and \(p=(q-1)/q\ge3/4\). By (2), using \(R(6)=R(12)=-1/11\), the diagonal equals
\[
F_2(p)=1-\frac{24p}{11}+\frac{12p^2}{11}.
\]
Its derivative is \(24(p-1)/11\le0\) on \([3/4,1]\), and \(F_2(3/4)=-1/44\), giving strict negativity.

When \(d=3\) and \(q\ge3\), choose \(h=3/q\), so \(p\in[2/3,1)\). Here \(R(0),R(3),R(6),R(9)\) equal \(1,0,-1/11,-4/41\). Put \(v=3p-2\in[0,1)\). Expressing \(F_3(p)=K_0^{(3,q)}(3/q)\) in Bernstein basis \(\binom 3jv^j(1-v)^{3-j}\), the four coefficients are
\[
-\frac{131}{4059},\quad-\frac{340}{4059},\quad-\frac{43}{451},\quad-\frac4{41}.
\]
They are all negative, so \(F_3(p)<0\).

When \(d=4\) and \(q\ge2\), choose \(h=4/q\), so \(p\in[1/2,1)\). The values \(R(0),R(4),R(8),R(12),R(16)\) are \(1,-1/19,-5/51,-1/11,-13/163\). With \(v=2p-1\in[0,1)\), the five Bernstein coefficients of \(F_4(p)=K_0^{(4,q)}(4/q)\) are
\[
-\frac{8765}{579139},\quad-\frac{50619}{579139},\quad-\frac{8221}{91443},\quad-\frac{153}{1793},\quad-\frac{13}{163}.
\]
Hence every such graph has a negative diagonal entry at this explicit step.

Finally, for every \(d\ge5\) and \(q\ge2\), choose two vertices at distance five. The Taylor expansion is
\[
R(x)=1-x+\frac{x^2}{2}-\frac{x^3}{6}+\frac{x^4}{36}+\frac{x^5}{108}+O(x^6).
\]
For their matrix entry, all lower powers of \(L\) vanish by graph distance, and \((L^5)_{xy}=-5!\), since there are exactly \(5!\) shortest walks changing each differing coordinate once. Thus
\[
[T_{d,q}(h)]_{xy}=-\frac{10}{9}h^5+O(h^6)<0
\]
for all sufficiently small positive \(h\). These cases exhaust the complement.

## Verification
The standalone standard-library script `verify.py` independently recomputes formula (1), checks all ten positive-case rational identities by polynomial cross-multiplication, checks the exact Bernstein coefficients and rational negative witnesses, and verifies the Taylor coefficient and fifth-distance obstruction. Running `python3 verify.py` yields `VERIFY_OK`. A separate direct matrix-resolvent check on representative positive and negative instances independently agreed with the formulas and unit row sums. These are corroborative calculations; the argument above proves the infinite classification.

## Relationship to prior work
General Runge–Kutta absolute-monotonicity results identify stability-function conditions sufficient for positivity on broad differential-equation classes, not this exact all-steps criterion indexed by the dimension and alphabet of a Cartesian-product graph. Horváth–Song–Terlaky’s general polyhedral-invariance Theorem 3.12 supplies a sufficient scalar absolute-monotonicity-based step bound for a fixed system; the relevant author-uploaded full-text section does not give an exact Hamming-family classification. In fact, the Radau IIA scalar function in this theorem has no positive real pole and therefore zero scalar absolute-monotonicity radius, so such a sufficient bound does not explain the nontrivial positive Hamming cases. Known path/cycle and multipartite special-case results also cover some individual Hamming graphs (for instance, \(H(1,q)\) and \(H(2,2)\)) but not the full classification. The novelty claim is the complete dimension–alphabet frontier, not the generic distance-five obstruction or those individual special cases.

## Limitations
The graph class is the homogeneous unweighted Hamming family, and the conclusion is only about completed linear end-steps. No assertion is made for anisotropic product edge weights, generic finite graphs or internal-stage positivity. Searches and available primary-source inspection cannot exclude all unindexed or differently formulated prior literature; independent mathematical audit and publication-priority confirmation are still outstanding.

## References
- L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1 (first public 2013-03-26), https://arxiv.org/html/1303.6651v1 .
- Z. Horváth, Y. Song, and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755v1 (first public 2014-06-26), https://arxiv.org/abs/1406.6755 ; journal DOI https://doi.org/10.3934/dcds.2015.35.2997 .
- Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026 .
