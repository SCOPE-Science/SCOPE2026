# Sharp Lipschitz variance and Hilbert rank collapse in cyclic five-point metrics

## Finding

For each real \(1\le t\le2\), let \(X_t=\mathbb Z/5\mathbb Z\) have uniform probability and the cyclic two-distance metric
\[
d_t(i,j)=\begin{cases}0,&i=j,\\1,&i-j\equiv\pm1\pmod5,\\t,&i-j\equiv\pm2\pmod5.\end{cases}
\]
For a one-Lipschitz map \(f:X_t\to E\) into a real Hilbert space (including \(E=\mathbb R\)), write
\[
\mathcal V(f)=\frac15\sum_{j=0}^4\|f(j)-\bar f\|^2,
\qquad \bar f=\frac15\sum_{j=0}^4f(j).
\]
The exact scalar and unrestricted Hilbert constants are
\[
\boxed{S(t)=\max_{f:X_t\to\mathbb R}\mathcal V(f)=\frac{6-4t+4t^2}{25},}
\]
\[
\boxed{H(t)=\max_{f:X_t\to E,\ \dim E\ge4}\mathcal V(f)
=\min\left\{\frac{1+t^2}{5},\frac{5+\sqrt5}{10}\right\}.}
\]
Here and below the maxima are over one-Lipschitz maps. Set \(\varphi=(1+\sqrt5)/2\). For \(1<t\le2\), precisely the negatives and cyclic shifts of the function with cyclic values \((0,1,t,1,0)\) maximize the scalar variance, up to additive constants. At \(t=1\), all scalar maximizers are the balanced two-level maps, with two points on one level and three on the other, where the levels differ by one.

For \(1\le t<\varphi\), every Hilbert maximizer is an isometric embedding of all ten pairwise distances of \(X_t\). It has affine span dimension exactly four, hence cannot live in a Hilbert space of dimension below four. For \(\varphi\le t\le2\), all Hilbert maximizers, up to ambient isometry and translation, are the planar regular pentagon with unit sides. In particular the optimizer's required affine dimension jumps from four to two at \(\varphi\).

Both \(H(t)-S(t)\) and \((H(t)-S(t))/H(t)\) have a unique maximum at \(t=\varphi\), where
\[
\boxed{H(\varphi)-S(\varphi)=\frac\varphi5=\frac{1+\sqrt5}{10},
\qquad \frac{H(\varphi)-S(\varphi)}{H(\varphi)}=\frac1{\sqrt5}.}
\]

## Assumptions and scope

The five points carry the uniform mass \(1/5\). The metric obeys the triangle inequalities precisely in the stated range of interpolating parameters \(1\le t\le2\) relevant here. All maps have Lipschitz constant at most one for the *specified pairwise metric*, and the variance uses the probability normalization \(1/5\), not an unnormalized sum of squared deviations. The Hilbert formula and equality classification are asserted for real Hilbert target dimension at least four; the scalar formula is for dimension one. The exact transition includes its endpoint.

## Proof

**1. Scalar reduction to finite exact optimization.** Fix \(f(0)=0\) to quotient constants, and write \(x_j=f(j)\) for the remaining four variables. The feasible convex polytope in \(\mathbb R^4\) is defined by all ten constraints \(|x_i-x_j|\le d_t(i,j)\). Its variance is
\[
V(x)=\frac15\sum_jx_j^2-\left(\frac15\sum_jx_j\right)^2
=\frac1{25}\sum_{0\le i<j\le4}(x_i-x_j)^2.
\]
It is strictly convex on the gauge-fixed four-dimensional subspace, so every maximizer must be a polytope vertex. At a vertex the graph of saturated pair constraints is connected: otherwise shifting all values on a non-root connected component by a sufficiently small common amount in either direction would preserve every constraint, contradicting extremality. Hence every vertex is represented by some spanning tree on the five labeled vertices, with a choice of sign on each of its four saturated edges. Conversely, testing the entire set of such trees and signs against the original ten constraints suffices to find *all* vertices.

There are \(5^{5-2}2^4=2000\) signed spanning-tree candidates by the Prüfer enumeration. Each candidate, normalized by \(x_0=0\), has entries affine in \(t\) with integral coefficients. For each candidate, the ten Lipschitz constraints determine a closed rational feasibility interval, possibly a singleton, inside \([1,2]\), and its variance is a quadratic polynomial with rational coefficients. The included stand-alone `CHECK.py` enumerates all 2000 cases, deduplicates the 310 feasible affine candidate families, and **checks the continuum** of parameter values by minimizing the difference between the claimed sharp polynomial and each candidate's variance polynomial on its entire feasible interval. The minimum is computed exactly, at interval endpoints and (when applicable) the rational critical point; no sampling assumption is used.

For \(1<t<2\), the 70 distinct feasible vertices split into five dihedral-and-sign orbits. Writing each orbit's variance as the polynomial in the second column divided by \(25\), their sizes and polynomials are

| Orbit size | Variance numerator |
|---:|---|
| 20 | \(10-10t+6t^2\) |
| 20 | \(14-14t+6t^2\) |
| 10 | \(6-8t+6t^2\) |
| 10 | \(6-4t+4t^2\) |
| 10 | \(6\) |

The fourth orbit is strictly best for every \(1<t<2\): its differences from the other four numerators are \(2(t-1)(2-t)\), \(2(t-1)(4-t)\), \(2t(2-t)\), and \(4t(t-1)\), all strictly positive. This orbit is exactly the signed cyclic shifts of \((0,1,t,1,0)\), modulo constants. At \(t=1\) the exact endpoint check gives 30 distinct feasible vertices and 20 maximizers, exactly the balanced two-level maps; at \(t=2\), 30 distinct vertices and 10 maximizers, the same signed-shift family. This proves the scalar assertion and all scalar equality cases.

**2. Universal Hilbert upper bounds.** For any Hilbert-valued map \(z\), the pairwise identity reads
\[
\mathcal V(z)=\frac1{25}\sum_{i<j}\|z_i-z_j\|^2.
\]
Exactly five unordered pairs are sides of the cycle and exactly five are diagonals. Therefore \(\mathcal V(z)\le(1+t^2)/5\). Independently, the unnormalized five-cycle Laplacian has first nonzero eigenvalue \(\lambda_1=(5-\sqrt5)/2\). Its exact Poincaré inequality, valid componentwise in any real Hilbert space, yields
\[
\sum_j\|z_j-\bar z\|^2\le\lambda_1^{-1}\sum_j\|z_{j+1}-z_j\|^2
\le 5/\lambda_1.
\]
After division by five this gives \(\mathcal V(z)\le\lambda_1^{-1}=(5+\sqrt5)/10\). Thus the proposed formula is an upper bound.

**3. Attainment and classification of Hilbert equality.** Define \(A=(5-\sqrt5)/2\) and \(B=(5+\sqrt5)/2\). For \(1\le t\le\varphi\) put
\[
\alpha^2=\frac{Bt^2-A}{B^2-A^2},\qquad
\beta^2=\frac{B-At^2}{B^2-A^2},
\]
and define, for \(j\in\mathbb Z/5\mathbb Z\),
\[
z_j=\alpha\big(\cos(2\pi j/5),\sin(2\pi j/5)\big)
\oplus\beta\big(\cos(4\pi j/5),\sin(4\pi j/5)\big).
\]
Both squared coefficients are nonnegative throughout this parameter interval. The first harmonic has squared side chord \(A\) and diagonal chord \(B\), and the second harmonic exchanges these values. Direct substitution gives \(A\alpha^2+B\beta^2=1\) and \(B\alpha^2+A\beta^2=t^2\). Thus the map realizes *every* prescribed pairwise distance, attaining the first Hilbert upper bound. For \(t<\varphi\), both coefficients are positive, so its centered Gram matrix has rank four. Any Hilbert maximizer must saturate each of the ten pairwise distance upper bounds, since their nonnegative squared deficits sum to zero. These distances determine its centered Gram matrix through double centering and hence determine its congruence class, forcing affine rank four.

For \(t\ge\varphi\), the unit-side regular planar pentagon is admissible because its diagonals have length exactly \(\varphi\le t\). It saturates the cycle spectral-gap bound. Conversely, equality in that bound forces every side length to be one and each centered coordinate of the map to be in the first two real Fourier modes of the five-cycle Laplacian. Write \(z_j=u\cos(2\pi j/5)+v\sin(2\pi j/5)\) for target vectors \(u,v\). Constancy of the five side-length squares implies \(\|u\|=\|v\|\) and \(\langle u,v\rangle=0\), because the five phase angles separate the second harmonic. The resulting five points form a planar regular pentagon of unit side, proving every equality case.

**4. The unique gap maximum.** Let \(G=H-S\). For \(1\le t\le\varphi\),
\[
G'(t)=\frac{2t+4}{25}>0.
\]
For \(\varphi\le t\le2\), \(G'(t)=-(8t-4)/25<0\). For the relative gap, minimize \(S/H\): on the first branch
\[
\frac{d}{dt}\frac{S}{H}=\frac{4(t^2-t-1)}{5(1+t^2)^2}<0\qquad(1\le t<\varphi),
\]
while on the second branch \(S/H\) increases strictly. Substitution at \(t=\varphi\) gives the stated absolute and relative maxima.

## Verification

`CHECK.py` is self-contained Python using only the standard library, run as `python CHECK.py` with assertions enabled. Its execution produced:

```
PRUFER_SIGN_CASES_EXHAUSTIVE 2000
ALL_FEASIBLE_AFFINE_VERTEX_FAMILIES 310
INTERIOR_VERTEX_ORBIT_SIZES [10, 10, 10, 20, 20]
ALL_CONTINUUM_SCALAR_VARIANCE_INEQUALITIES_EXACT
ENDPOINT_AND_INTERIOR_OPTIMIZER_COUNTS_EXACT
C5_SCALAR_CERTIFICATE_PASSED
```

The finite exact certificate is exhaustive for the scalar polytope **and for all real parameters on the stated interval**, because every vertex is in its spanning-tree enumeration and all interval polynomial inequalities are checked without rounding. The Hilbert part is established analytically by the pairwise-distance identity, cycle spectrum, explicit Fourier construction, and equality analysis. No claim about optimal constants for intermediate target dimensions two or three below the transition is made.

## Relationship to prior work

Alon, Boppana and Spencer introduced the scalar *spread* constant for general finite metric spaces and established broad product-space consequences, including a connected-tight-edge argument in the graph-metric case. Addario-Berry, Janson and McDiarmid investigated graph spread in random graph families. Naor's work treats nonlinear metric spectral gaps and Hilbert embeddability in considerably broader settings. None of the inspected relevant statements supplies this exact continuous five-point cyclic metric scalar-Hilbert phase diagram, its equality classification, or its unique maximizing relative gap. The integer graph-distance endpoint \(t=2\) is a known five-cycle spread special case and is not separately claimed as original. The geometric deformation, exact parameter law, rank transition and gap comparison are the contribution here.

## Limitations

The measures are uniform and the metric has exactly five labeled cyclic points, two symmetric pairwise distances, and \(1\le t\le2\). The Hilbert classification for \(t<\varphi\) needs a Hilbert space of dimension at least four; this result does not determine sharp maxima for dimensions two and three there. No conclusion is asserted for arbitrary five-point metric perturbations, nonuniform probability measures, other target Banach geometries, or analogous even cycles. Although the closest primary sources and searchable mathematical records were compared, an equivalent unindexed prior calculation cannot be logically excluded by search alone.

## References

1. N. Alon, R. Boppana and J. Spencer, *An asymptotic isoperimetric inequality*, original mathematical paper (1998), publicly accessible author-hosted PDF: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf . Section 1.1 defines spread for a finite metric space; Section 2.1 studies graph-metric optimal potentials.
2. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first submitted 2009-02-06: https://arxiv.org/abs/0902.1156 .
3. A. Naor, *Comparison of metric spectral gaps*, arXiv:1308.2851, first submitted 2013-08-13: https://arxiv.org/abs/1308.2851 .
