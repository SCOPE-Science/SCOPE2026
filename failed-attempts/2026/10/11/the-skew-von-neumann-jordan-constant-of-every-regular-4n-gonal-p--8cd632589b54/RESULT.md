# The skew von Neumann–Jordan constant of every regular \(4n\)-gonal plane
## Finding
For every integer \(n\ge 1\), let \(X_{4n}\) be the real two-dimensional Banach space whose closed unit ball is a Euclidean regular \(4n\)-gon inscribed in the Euclidean unit circle. Define the skew von Neumann–Jordan constant by
\[
C_{\mathrm{NJ}}[X]=\sup_{0\le t\le1}\frac{E[t,X]}{2(1+t^2)},
\qquad
E[t,X]=\sup_{x,y\in S_X}\bigl(\|x+ty\|^2+\|tx-y\|^2\bigr).
\]
Then
\[
C_{\mathrm{NJ}}[X_{4n}]=\sec^2\!\left(\frac{\pi}{4n}\right).
\]
Moreover, the outer supremum is attained at the symmetric parameter \(t=1\). Thus, on this entire polygonal family, allowing the skew parameter does not increase the optimum beyond the symmetric endpoint.

## Assumptions and scope
The result concerns real two-dimensional spaces. The regular \(4n\)-gon is centered at the origin and scaled so that its vertices lie on the Euclidean unit circle; scaling does not affect the normed-space isometry class or the constant. Put \(\theta=\pi/(4n)\). The restriction to a multiple of four is used in the lower-bound construction: the directions of the sum and difference of a symmetric adjacent vertex pair are both facet-normal directions.

## Proof
Choose the orientation in which two adjacent vertices are
\[
x=(\cos\theta,\sin\theta),\qquad y=(\cos\theta,-\sin\theta).
\]
Every facet of the regular polygon is tangent to the Euclidean circle of radius \(\cos\theta\). Hence the Euclidean unit disk contains the polygon, while the polygon contains the Euclidean disk of radius \(\cos\theta\). For every vector \(z\), the corresponding Minkowski functional therefore satisfies
\[
\|z\|_2\le \|z\|_{X_{4n}}\le \sec\theta\,\|z\|_2.
\]
Consequently the identity isomorphism between \(X_{4n}\) and \(\ell_2^2\) has distortion at most \(\sec\theta\). Fu, Yang, Liu and Li proved that isomorphic Banach spaces satisfy
\[
C_{\mathrm{NJ}}[X]\le d(X,Y)^2 C_{\mathrm{NJ}}[Y].
\]
Since \(C_{\mathrm{NJ}}[\ell_2^2]=1\), this gives
\[
C_{\mathrm{NJ}}[X_{4n}]\le\sec^2\theta.
\]

For the reverse inequality, the displayed adjacent vertices lie on \(S_{X_{4n}}\). Their sum is \(x+y=(2\cos\theta,0)\). The positive horizontal ray meets the polygon at the midpoint of the facet joining \(x\) and \(y\), whose Euclidean radius is \(\cos\theta\); hence \(\|x+y\|_{X_{4n}}=2\). Their difference is \(x-y=(0,2\sin\theta)\). Because \(4n\) is divisible by four, the vertical direction is also a facet-normal direction, so the polygon again has radial value \(\cos\theta\) there. Thus
\[
\|x-y\|_{X_{4n}}=2\tan\theta.
\]
At \(t=1\), the normalized skew expression therefore equals
\[
\frac{\|x+y\|^2+\|x-y\|^2}{4}
=1+\tan^2\theta
=\sec^2\theta.
\]
This matches the upper bound and proves the claim for every \(n\ge1\).

## Verification
The proof is analytic and covers the infinite family; no finite enumeration is used as a substitute for the quantifiers. The bundled script `verify.py` independently reconstructs the regular-polygon gauge from its facet normals and checks the norm sandwich and the adjacent-vertex equalities numerically for \(1\le n\le64\). Those finite checks are only regression tests for the formulas used in the proof.

## Relationship to prior work
Fu, Yang, Liu and Li introduced \(E[t,X]\) and \(C_{\mathrm{NJ}}[X]\), proved the Banach–Mazur comparison used above, and computed three particular examples, including a regular hexagonal norm; their paper does not state a regular \(4n\)-gonal formula. The regular-octagon literature gives exact values for several related von Neumann–Jordan-type constants, including the generalized constant \(C_{\mathrm{NJ}}^{(p)}\) and the two-parameter unit-sphere constant \(L'_{YJ}\), so the cases \(n=1\) and \(n=2\) are not presented as new isolated polygon computations. The finding here is the dimension-two infinite-family formula and the fact that its skew optimum always collapses to \(t=1\).

## Limitations
The argument uses the simultaneous facet-normal directions available for regular \(4n\)-gons and does not claim the same formula for regular polygons with other numbers of sides. It gives the exact scalar constant but not the full parameter profile \(E[t,X_{4n}]\). The literature comparison found exact regular-octagon results and no broader regular \(4n\)-gonal theorem for this skew constant; an unindexed older source treating the same infinite family remains a residual novelty risk.

## References
1. Y. Fu, Z. Yang, Q. Liu, Y. Li, *On Some Skew Constants in Banach Spaces*, Kyungpook Mathematical Journal 63 (2023), 199–223. DOI: 10.5666/KMJ.2023.63.2.199.
2. C. Yang, T. Wang, *Generalized von Neumann-Jordan constant \(C_{NJ}^{(p)}(X)\) for the regular octagon space*, Mathematical Inequalities & Applications 20 (2017), 483–490. DOI: 10.7153/mia-20-32.
3. X. Yang, H. Li, C. Yang, *On the \(L_{YJ}(\lambda,\mu,X)\) constant for the regular octagon space*, Filomat 38 (2024), 1583–1593. DOI: 10.2298/FIL2405583Y.
