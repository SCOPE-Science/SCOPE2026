# Smooth convex bodies invisible to every one-direction support-jet law at fixed area and perimeter

## Finding

There is a continuum of pairwise noncongruent, centrally symmetric, strictly positively curved \(C^\infty\) planar convex bodies that all have **the same area, perimeter, and distribution of every finite support-function jet at a uniformly random normal direction**. Consequently their complete unlabeled projection-width distributions agree. Even the distributions of these finite jets under boundary-arclength sampling agree. A two-direction support covariance separates particular members, exhibiting exactly the directional information lost by all of those one-point laws.

Explicitly, put \(\delta=\pi/100\), \(\varepsilon=\delta^2/1000\), and let \(b:\mathbb R\to[0,1]\) be the smooth \(\pi\)-periodic function defined on \((-\pi/2,\pi/2]\) by
\[
 b(t)=\begin{cases}\exp\!\left(-\frac1{1-(t/\delta)^2}\right),&|t|<\delta,\\0,&|t|\ge\delta.\end{cases}
\]
For each \(\alpha\in[\pi/4,\pi/2]\) the \(\pi\)-periodic function
\[
 h_\alpha(\theta)=1+\varepsilon\bigl(b(\theta)+b(\theta-\alpha)\bigr)
\]
is the support function of a body \(K_\alpha\) having all the properties above. Distinct parameters in the stated interval give noncongruent bodies.

## Assumptions and scope

The ambient space is \(\mathbb R^2\) with its Euclidean metric. A support function \(h_K(\theta)\) gives the distance from the origin to the supporting line with outward unit normal \(u_\theta=(\cos\theta,\sin\theta)\). Its derivative jet of order \(k\) is \(J^k h=(h,h',\ldots,h^{(k)})\), differentiated with respect to the normal angle. Uniform normal sampling means that \(\Theta\) is uniform on \([0,\pi)\); antipodal symmetry makes this equivalent to uniform sampling on \([0,2\pi)\). Boundary-arclength sampling weights each normal by the curvature radius \(\rho=h+h''\).

This is a statement of equality of **one-direction marginals for each finite order**, not of the jointly observed stochastic processes over multiple directions. The bodies are not claimed to be real analytic. The two-angle comparison below is for angles measured in an arbitrary fixed normal coordinate system and is invariant under shifting the common random base angle.

## Proof

**1. Smoothness and positive curvature.** The classical compactly supported exponential bump is \(C^\infty\) and is flat at both endpoints. Its periodized copies have no overlap for the stipulated \(\alpha\), since \(2\delta<\pi/4\) and \(2\delta<\pi-\pi/2\). The support functions are therefore \(C^\infty\), strictly positive, and \(\pi\)-periodic.

For \(|s|<1\) put \(q=1-s^2\) and \(f(s)=\exp(-1/q)\). Direct differentiation gives
\[
 f''(s)=f(s)\left(\frac{4s^2}{q^4}-\frac2{q^2}-\frac{8s^2}{q^3}\right).
\]
Using \(s^2\le1\) and the elementary bound \(\sup_{y\ge1}y^j e^{-y}=j^j e^{-j}\) for \(j=2,3,4\), we obtain
\[
 |b''(t)|\le\delta^{-2}\bigl(4\cdot4^4e^{-4}+8\cdot3^3e^{-3}+2\cdot2^2e^{-2}\bigr)<31\delta^{-2}.
\]
At most one bump is nonzero at any angle. Hence the curvature radius satisfies
\[
 \rho_\alpha(\theta)=h_\alpha(\theta)+h_\alpha''(\theta)>1-\frac{32}{1000}=\frac{121}{125}>0.
\]
The normal parametrization \(x_\alpha(\theta)=h_\alpha u_\theta+h_\alpha' u_\theta^\perp\) has derivative \(x_\alpha'=\rho_\alpha u_\theta^\perp\). Thus it is the smooth strictly positively curved boundary of a strictly convex body. Since \(h_\alpha(\theta+\pi)=h_\alpha(\theta)\), this body is centrally symmetric about the origin.

**2. Exact joint jet distribution.** Let \(B_\delta=(-\delta,\delta)\). For any integer \(k\ge0\) and any bounded Borel \(F:\mathbb R^{k+1}\to\mathbb R\), decomposition of \([0,\pi)\) into the two disjoint bump supports and their complement gives
\[
\begin{split}
 \mathbb E F(J^k h_\alpha(\Theta))={}&\left(1-\frac{4\delta}{\pi}\right)F(1,0,\ldots,0)\\
 &+\frac2\pi\int_{-\delta}^{\delta}
 F\bigl(1+\varepsilon b(t),\varepsilon b'(t),\ldots,\varepsilon b^{(k)}(t)\bigr)\,dt.
\end{split}
\]
This expression contains no \(\alpha\). Therefore the **full joint law** of every finite derivative jet is independent of \(\alpha\), not merely the separate marginal laws of its components. Since the projection width is \(w_\alpha(\theta)=h_\alpha(\theta)+h_\alpha(\theta+\pi)=2h_\alpha(\theta)\), every unlabelled width law agrees. The normal-angle curvature-radius variable \(\rho_\alpha=h_\alpha+h_\alpha''\) is another jet observable. Moreover for a boundary point sampled uniformly by arclength, the expectation of any such test function is
\[
\frac1{P_\alpha}\int_0^{2\pi} F(J^k h_\alpha(\theta))\rho_\alpha(\theta)\,d\theta,
\]
which is also independent of \(\alpha\), since the numerator is the integral of a function of a finite jet (of order at least \(\max\{k,2\}\)) and the denominator is independent of \(\alpha\) by the next step.

**3. Exactly equal area and perimeter.** Define the finite bump integrals
\[
 B=\int_{-\delta}^{\delta}b(t)\,dt,\qquad
 C=\int_{-\delta}^{\delta}\bigl(b(t)^2-b'(t)^2\bigr)\,dt.
\]
The standard support-function formulas \(P=\int_0^{2\pi}h\) and \(A=\frac12\int_0^{2\pi}(h^2-(h')^2)\) give, by disjoint supports and \(\pi\)-periodicity,
\[
 \boxed{P(K_\alpha)=2\pi+4\varepsilon B},\qquad
 \boxed{A(K_\alpha)=\pi+4\varepsilon B+2\varepsilon^2 C}.
\]
Both are exactly constant across the family. Here disjointness is essential: no cross term between the two bump locations survives in the quadratic area functional.

**4. Noncongruence.** The set where \(h_\alpha>1\) consists of two open arcs of length \(2\delta\) on the circle of normal directions modulo \(\pi\), with midpoint separation \(\alpha\). Any isometry between two centrally symmetric bodies must map their unique symmetry centers to each other, and so has zero translation in the chosen centered coordinates. Rotation or reflection preserves the smaller angular separation \(\min\{\alpha,\pi-\alpha\}\), which equals \(\alpha\) on the selected parameter interval. Hence distinct \(\alpha\) produce noncongruent bodies, yielding an uncountable family.

**5. A separating two-direction statistic.** For each \(t\), put
\[
 R_\alpha(t)=\frac1\pi\int_0^\pi\bigl(h_\alpha(\theta)-1\bigr)\bigl(h_\alpha(\theta+t)-1\bigr)\,d\theta.
\]
At angular separation \(t=\pi/3\), the supports give
\[
 \boxed{R_{\pi/3}(\pi/3)=\frac{\varepsilon^2}{\pi}\int_{-\delta}^{\delta}b(t)^2\,dt>0},\qquad
 \boxed{R_{\pi/2}(\pi/3)=0}.
\]
The difference confirms that one-point jet laws discard nontrivial geometric information retained by two-direction correlations.

## Verification

The companion `verify_jet_width.py` uses midpoint quadrature and discrete angular sampling to check the finite-area/perimeter formulas, positive curvature, equality of sampled support/first-derivative/radius histograms, and the two-angle correlation difference for \(\alpha=\pi/3\) and \(\alpha=\pi/2\). Run with `python3 verify_jet_width.py` from the package directory. The expected first line begins `VERIFY_OK shapes=2 normal_samples_per_shape=120000`. The continuum theorem and equality for every jet order are proved above analytically; finite sampling is not used to infer them.

## Relationship to prior work

Kim, Yaskin, and Zvavitch proved in Proposition 2 of arXiv:1512.07289 (2015) that two origin-symmetric planar bodies can have identical unlabeled projection distributions **but different areas**. They use a deliberately nonpreserving derivative-energy rearrangement. The present result shows nonidentifiability **after fixing area and perimeter** and even after giving the entire joint one-direction jet law of every finite order. The distinction is in their precise statements and implications, not just the choice of example.

Geiger and Kogan (arXiv:1912.09597) exhibit noncongruent plane curves with identical Euclidean differential-signature sets and discuss rearrangements of curved pieces. That addresses a related failure of pointwise local-invariant recognition, but their inspected setup is based on curvature-signature sets and signature paths; it does not state equality of all normal-sampled support jets, the two fixed intrinsic quantities, and the positive-curvature centrally symmetric convex family given here. Local-piece rearrangement remains a substantive historical-priority risk.

A reported inverse classification of unlabeled widths for centrally symmetric tangential polygons establishes noncongruence within a polygonal class; its summary does not imply the present smooth positive-curvature, all-jet, fixed-area result. The full text of that record was not available for direct comparison.

## Limitations

Equality of all **single normal** jets does not mean equality of two-normal statistics, as explicitly disproved. The family has positive curvature and is \(C^\infty\), but its compactly supported nonzero bumps are not real analytic. The construction does not establish nonuniqueness under a continuously oriented record of the entire width function, nor does it address higher-dimensional bodies. No claim of independent scientific validation or established historical priority is made.

## References

1. J. Kim, V. Yaskin, A. Zvavitch, *Distribution Functions of Sections and Projections of Convex Bodies*, arXiv:1512.07289v1, 2015-12-22, Proposition 2 and Section 3, https://arxiv.org/pdf/1512.07289.
2. E. Geiger, I. A. Kogan, *Non-congruent non-degenerate curves with identical signatures*, arXiv:1912.09597v4, Sections 1 and 4--5, https://arxiv.org/pdf/1912.09597.
3. *Inverse classification of projection-width distributions for tangential symmetric polygons*, result record `2026/10/11/SCOPE-inverse-classification-of-projection-width-distributions-for-tan--2ee871113939`; summary-level comparison only.
