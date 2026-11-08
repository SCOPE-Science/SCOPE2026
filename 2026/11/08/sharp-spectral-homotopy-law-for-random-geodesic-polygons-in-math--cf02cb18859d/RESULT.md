# Sharp spectral homotopy law for random geodesic polygons in \(\mathbb{RP}^{d-1}\)

## Finding
For integers \(d\ge3\), \(m\ge3\), choose \(m\) points independently under normalized Riemannian volume on the round real projective space \(\mathbb{RP}^{d-1}\). Join consecutive points, including the last to the first, by their (almost surely unique) shortest geodesic arcs. Denote by \(q_{d,m}\) the probability that the resulting closed loop represents the nonzero element of \(\pi_1(\mathbb{RP}^{d-1})\cong\mathbb Z/2\mathbb Z\).

Set
\[
\lambda_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
h_{d,l}=\frac{(2l+d-2)(l+d-3)!}{l!(d-2)!},
\qquad a_{d,j}=\lambda_d(-1)^j\frac{(1/2)_j}{((d+1)/2)_j}.
\]
Here \((u)_j=u(u+1)\cdots(u+j-1)\) is the rising factorial, with \((u)_0=1\). Then the **complete polygon homotopy law** is the absolutely convergent series
\[
\boxed{q_{d,m}=\frac12\left(1-\sum_{j=0}^{\infty}h_{d,2j+1}a_{d,j}^{m}\right).}
\]
For every permitted \(m\), the leading term has a uniform explicit error estimate:
\[
\boxed{\left|q_{d,m}-\left(\frac12-\frac d2\lambda_d^m\right)\right|
\le\frac{1-d\lambda_d^2}{2}\left(\frac{\lambda_d}{d+1}\right)^{m-2}.}
\]
For each fixed \(d\), there is the sharper two-eigenvalue asymptotic as \(m\to\infty\):
\[
\boxed{q_{d,m}=\frac12-\frac d2\lambda_d^m
-\frac{(d+4)d(d-1)}{12}\left(-\frac{\lambda_d}{d+1}\right)^m
+O_d\!\left(\left(\frac{3\lambda_d}{(d+1)(d+3)}\right)^m\right).}
\]
The second correction alternates with the parity of the number of vertices. In particular, the topological parity becomes asymptotically fair exponentially quickly, with an exact leading decay rate and coefficient.

## Assumptions and scope
The metric is the standard constant-curvature-one quotient metric of the unit sphere \(S^{d-1}\) by the antipodal map, not an extrinsic chord metric. Each point is independent and uniform under the invariant probability measure. Antipodal or perpendicular lift configurations, for which a shortest arc can be ambiguous, have probability zero. The restriction \(d\ge3\) ensures \(\pi_1(\mathbb{RP}^{d-1})=\mathbb Z/2\mathbb Z\) and the sphere is the universal cover. Polygons may cross themselves; only the free homotopy class of the specified closed piecewise geodesic loop is counted.

## Proof
**1. Deck transformation from signs.** Let \(X_1,\ldots,X_m\) be independent Haar-uniform lifts in \(S^{d-1}\), and \(X_{m+1}=X_1\). Put \(\varepsilon_i=\operatorname{sgn}(X_i\cdot X_{i+1})\). The lift of the unique shortest projective geodesic from \([X_i]\) beginning at the chosen lift \(X_i\) ends at \(\varepsilon_iX_{i+1}\). Successively lifting all edges therefore ends at \((\prod_i\varepsilon_i)X_1\). Since the sphere is the universal cover, the projective polygon is noncontractible exactly when \(\prod_i\varepsilon_i=-1\). Thus
\[
q_{d,m}=\frac12\left[1-\mathbb E\prod_{i=1}^{m}\operatorname{sgn}(X_i\cdot X_{i+1})\right].
\]
**2. A spherical integral operator.** Let \(\mu\) be invariant probability measure on \(S^{d-1}\), and define \(T:L^2(\mu)\to L^2(\mu)\) by
\[
(Tf)(x)=\int_{S^{d-1}}\operatorname{sgn}(x\cdot y)f(y)\,d\mu(y).
\]
The bounded symmetric kernel makes \(T\) self-adjoint and Hilbert--Schmidt, with \(\|T\|_{\mathrm{HS}}^2=1\). For \(m\ge3\), composition of kernels and Fubini give
\[
\mathbb E\prod_{i=1}^{m}\operatorname{sgn}(X_i\cdot X_{i+1})
=\operatorname{tr}(T^m).
\]
Here \(T^m\) is trace class and its eigenvalue series converges absolutely by the Hilbert--Schmidt bound.

**3. Exact eigenvalues.** The Funk--Hecke principle diagonalizes \(T\) on degree-\(l\) spherical harmonics, whose multiplicity is \(h_{d,l}\) above. With \(P_l\) the normalized Gegenbauer polynomial \(P_l(1)=1\), its eigenvalue is
\[
\eta_l=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}
\int_{-1}^{1}\operatorname{sgn}(t)P_l(t)(1-t^2)^{(d-3)/2}\,dt.
\]
Parity gives \(\eta_{2j}=0\). For odd \(l\), the Gegenbauer differential equation yields
\[
\frac{d}{dt}\big[(1-t^2)^{(d-1)/2}P_l'(t)\big]
=-l(l+d-2)(1-t^2)^{(d-3)/2}P_l(t).
\]
Integrating over \([0,1]\) and using \(d\ge3\) gives
\[
\eta_l=\frac{2\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}\frac{P_l'(0)}{l(l+d-2)}.
\]
From the degree-one polynomial \(P_1(t)=t\), \(\eta_1=\lambda_d\). For \(l=2j+1\), the coefficient of the linear term in the standard finite Gegenbauer expansion gives
\[
\frac{\eta_{2j+3}}{\eta_{2j+1}}=-\frac{2j+1}{d+2j+1}.
\]
Consequently, \(\eta_{2j+1}=a_{d,j}\), and substitution into the trace proves the exact series.

**4. Uniform finite-length error.** In particular, \(\eta_3=-\lambda_d/(d+1)\) and, by the strict eigenvalue-ratio inequality, \(|\eta_{2j+1}|\le|\eta_3|\) for \(j\ge1\). Parseval for the kernel gives
\[
\sum_{j=0}^{\infty}h_{d,2j+1}|\eta_{2j+1}|^2=1,
\qquad h_{d,1}=d.
\]
Therefore
\[
\left|\sum_{j\ge1}h_{d,2j+1}\eta_{2j+1}^m\right|
\le|\eta_3|^{m-2}(1-d\lambda_d^2),
\]
proving the stated inequality. Removing the \(j=1\) term and applying the same estimate to \(j\ge2\), where \(|\eta_5|=3\lambda_d/[(d+1)(d+3)]\), gives the two-eigenvalue asymptotic with \(h_{d,3}=(d+4)d(d-1)/6\). Since \(0<|\eta_3|<\lambda_d<1\), the first correction is strictly dominant. This proves the asserted decay rate, coefficient, and alternating next correction.

## Verification
A separate standard-library Python checker evaluates the absolutely convergent series, compares the three-vertex specialization with a separate one-dimensional integral, verifies the explicit finite-length remainder inequality over multiple dimensions and lengths, and tests the full cyclic sign-product definition by Monte Carlo on independent Gaussian sphere lifts. The checker reports `PROJECTIVE_POLYGON_SPECTRAL_PARITY_OK 330000` after \(330{,}000\) simulated polygons. These finite checks corroborate but do not replace the analytical proof. Representative values are \(q_{3,4}\approx0.4052847346\), \(q_{3,5}\approx0.4532271344\), and \(q_{4,4}\approx0.4346545170\).

## Relationship to prior work
A July 20, 2001 calculation by Robin Chapman, preserved in D. Eppstein's *Geometry Junkyard*, already establishes \(q_{3,3}=1/\pi\) for **three** random points of the projective plane; this classical three-vertex result is explicitly excluded from the novelty claim. Rabei, Arvind, Mukunda, and Simon (1999) describe the connection between geodesic polygons and cyclic Bargmann invariants in complex ray geometry; that connection and the sign/deck-lifting idea are background, not claimed discoveries. Finch and Jones (2010) study random triangles on the ordinary sphere. The spectral diagonalization principle is classical. The claim here concerns the all-\(d\), all-\(m\) exact **real-projective polygon homotopy probability**, its finite-length bound, and its sharp two-mode asymptotic. The checked primary texts do not state these results. Existing general harmonic-operator theory may make the conclusions accessible by a calculation; publication priority has not been independently established.

## Limitations
The theorem is limited to round real projective spaces of dimension at least two and independent volume-uniform vertices, in the stated cyclic order. It does not describe alternative polygonal paths, arbitrary projective metrics, or the full integer winding law of \(\mathbb{RP}^{1}\). The bound does not claim finite-\(m\) monotonicity. Numerical verification is not an infinite proof. Related harmonic-operator and random-polygon literature may contain equivalent results not recovered by the searches; independent historical and mathematical review remains necessary.

## References
1. Robin Chapman, *Random projective triangles*, reply to Bill Taylor, sci.math, July 20, 2001, archived by David Eppstein at https://www-dev.ics.uci.edu/~eppstein/junkyard/contractible-probability.html (prior exact triangle probability).
2. E. M. Rabei, Arvind, N. Mukunda, R. Simon, *Bargmann Invariants and Geometric Phases -- a Generalised Connection*, arXiv:quant-ph/9907080v1, July 26, 1999 (background geodesic and cyclic invariant framework).
3. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329v1, September 27, 2010 (distinct spherical-triangle distributions).
4. Funk--Hecke diagonalization and Gegenbauer polynomial differential identities (classical spherical-harmonic tools; applied explicitly in the proof).
