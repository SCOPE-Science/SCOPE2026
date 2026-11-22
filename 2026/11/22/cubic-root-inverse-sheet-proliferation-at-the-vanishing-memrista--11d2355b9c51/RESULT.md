# Cubic-root inverse-sheet proliferation at the vanishing-memristance boundary

## Finding

Consider the real-plane map introduced in [1],
\[
F_{\alpha,\beta}(x,y)=\bigl(\alpha\cos x+\beta(y^2-1)x,\ y+x\bigr),
\qquad \alpha>0,\quad\beta>0.
\]
Fix \(\alpha>0\) and a target \((u,v)\in\mathbb R^2\) with \(q=u/\alpha\notin\{-1,1\}\). Write \(\operatorname{cbrt}\) for the real cube root, and put
\[
R=(\alpha/\beta)^{1/3},\qquad
 a=\operatorname{cbrt}(q-1),\qquad b=\operatorname{cbrt}(q+1),\qquad L(q)=b-a>0.
\]
Let \(N_{\alpha,\beta}(u,v)\) be the number of **distinct real** solutions of \(F_{\alpha,\beta}(x,y)=(u,v)\), without counting algebraic multiplicity. As \(\beta\downarrow0\),
\[
\boxed{N_{\alpha,\beta}(u,v)=\frac{L(q)}{\pi}\left(\frac{\alpha}{\beta}\right)^{1/3}+O_{\alpha,u,v}(1).}
\]
The remainder is uniform as \((q,v)\) ranges over any fixed compact subset of \((\mathbb R\setminus\{-1,1\})\times\mathbb R\), with fixed \(\alpha\). All but \(O(1)\) preimages are regular, i.e. have nonzero Jacobian determinant.

More strongly, the empirical measure on rescaled preimages,
\[
\mu_{\alpha,\beta;u,v}=\frac1{N_{\alpha,\beta}(u,v)}
\sum_{F_{\alpha,\beta}(x,y)=(u,v)}\delta_{(x/R,y/R)},
\]
converges to uniform measure on the anti-diagonal segment \(\{(t,-t):a\le t\le b\}\). In Euclidean Wasserstein-\(1\) distance, this has the quantitative bound
\[
\boxed{W_1\bigl(\mu_{\alpha,\beta;u,v},\; (t\mapsto(t,-t))_*\operatorname{Unif}[a,b]\bigr)
=O_{\alpha,u,v}(R^{-1}),}
\]
again uniformly for the stated compact target sets.

For every \(\beta>0\), the map is proper, onto and has Brouwer topological degree \(+1\); it has no fixed points. At \(\beta=0\), its image is exactly the strip \([-\alpha,\alpha]\times\mathbb R\), each target in that strip has infinitely many preimages, and each target outside it has none. Thus a proper, finite-sheeted-on-each-fiber map develops a nonproper, infinite-fiber limit, with a target-dependent cubic-root divergence that remains present even for targets outside the limiting image. For each regular target at \(\beta>0\), the numbers of orientation-preserving and orientation-reversing preimages differ by exactly one.

## Assumptions and scope

The domain and codomain are the entire real plane, with no clipping or bounded observation region. The forcing \(\alpha>0\) is fixed as \(\beta\downarrow0\). The target \((u,v)\) is fixed or varies over a fixed compact family such that \(u/\alpha\) stays a positive distance from \(\pm1\); the two edge targets \(u=\pm\alpha\) are deliberately excluded from the quantitative asymptotics, but not from the properness and zero-coupling statements. The limits are real, not complex inverse counts. The normalized Wasserstein distance uses Euclidean distance in \(\mathbb R^2\), and each distinct preimage receives one unit of mass. The result concerns **one-step inverse fibers**, not the forward-orbit stability or an invariant physical measure.

## Proof

**1. Exact inverse reduction, properness and degree.** Fix the target \((u,v)\). The second output equation forces \(y=v-x\), so inverse points are in bijection with real roots of
\[
H_R(x)=\cos x+\frac{P_v(x)}{R^3}-q=0,
\qquad P_v(x)=x(x-v)^2-x=x^3-2vx^2+(v^2-1)x.
\tag{1}
\]
For \(\beta>0\), the unnormalized first output \(x\mapsto\alpha\cos x+\beta P_v(x)\) tends to negative and positive infinity at the respective ends, establishing surjectivity. If the output remains in a compact set, its second component makes \(v=x+y\) bounded; the cubic leading term in the first component then forces \(x\) bounded and hence \(y\) bounded. Thus the map is proper. Its inverse fibers are finite, because their real-analytic scalar equation has isolated roots in a compact interval and cannot vanish identically. In oriented coordinates \((x,v)=(x,x+y)\), the map is triangular, \((x,v)\mapsto(\alpha\cos x+\beta P_v(x),v)\). The first component crosses from \(-\infty\) to \(+\infty\), so at any regular target the signed sum of scalar crossing derivatives equals \(+1\). Since the coordinate change preserves orientation, the proper map has degree \(+1\); equivalently \(N_+-N_-=1\). A fixed point would force \(x=0\) from the second equation, then \(x'=\alpha\ne0\), a contradiction.

**2. Localization to a target-dependent expanding interval.** Let \(z=x/R\). Equation (1) reads
\[
H_R(Rz)=\cos(Rz)+Q_R(z)-q,\quad
Q_R(z)=z^3-\frac{2v}{R}z^2+\frac{v^2-1}{R^2}z.
\tag{2}
\]
The only possible limiting positions satisfy \(q-1\le z^3\le q+1\), namely \(a\le z\le b\). Because \(q\ne\pm1\), both \(a\) and \(b\) are nonzero. The cubic \(Q_R\) converges to \(z^3\) in \(C^2\) on compact sets, and its derivative is bounded away from zero in fixed neighborhoods of \(a\) and \(b\). The implicit function theorem applied to the two level equations \(Q_R(z)=q-1\) and \(Q_R(z)=q+1\) gives their boundary roots as \(z=a+O(R^{-1})\) and \(z=b+O(R^{-1})\). The cubic's positive leading coefficient, together with the absence of other large roots of these level equations, yields a fixed \(D>0\) such that, for all sufficiently large \(R\):

- every zero of \(H_R\) lies in \([aR-D,bR+D]\);
- for every \(x\in[aR+D,bR-D]\), one has \(\lvert q-P_v(x)/R^3\rvert\le1-c/R\) for a constant \(c>0\);
- on \([aR-D,bR+D]\), \(\lvert P_v'(x)/R^3\rvert\le C/R\) and \(\lvert P_v''(x)/R^3\rvert\le C/R^2\).

For clarity about the middle assertion when \(a<0<b\), any local nonmonotonicity of the cubic lies in \(x=O_{v}(1)\), where \(P_v(x)/R^3=O(R^{-3})\) and \(q\) lies strictly between \(-1\) and \(1\). Elsewhere the cubic is increasing. The constants \(D,c,C\) can be chosen uniformly on any compact family of \((q,v)\) avoiding \(q=\pm1\), because the endpoint derivatives \(3a^2\) and \(3b^2\) have a positive uniform lower bound.

**3. Exactly one simple inverse per full cosine half-period.** On any interval \([k\pi,(k+1)\pi]\) wholly within \([aR+D,bR-D]\), the endpoint values of \(H_R\) have opposite signs, since \(\lvert q-P_v/R^3\rvert<1\). A zero therefore exists. At each such zero,
\[
|\sin x|=\sqrt{1-(q-P_v(x)/R^3)^2}\ge\sqrt{c/R},
\quad |P_v'(x)/R^3|\le C/R.
\]
For sufficiently large \(R\), the derivative \(H_R'(x)=-\sin x+P_v'(x)/R^3\) has the sign of \(-\sin x\) at every zero. That sign is constant over the open half-period. Two distinct zeros would necessarily include a crossing in the opposite direction or a multiple zero, which is impossible. Hence every wholly contained half-period has exactly one **simple** zero.

The two discarded edge strips have fixed total length \(4D\). To bound their zeros independently of \(R\), divide each into intervals with endpoints at multiples of \(\pi/4\). On each such cell, either \(|\sin x|\ge 1/\sqrt2\) throughout or \(|\cos x|\ge 1/\sqrt2\) throughout. For large \(R\), the first case makes \(H_R'\) of constant sign (at most one root), while the second makes \(H_R''=-\cos x+P_v''/R^3\) of constant sign (at most two roots). Thus the edge strips contain only \(O(1)\) zeros, with uniform constants on the stated compact target sets. The number of complete \(\pi\)-cells in the inner interval is \((b-a)R/\pi+O(1)\). This proves the displayed count, including the assertion that only \(O(1)\) roots can be nonregular.

**4. Quantitative inverse-location distribution.** The unique root of each complete half-period differs from that cell's midpoint by at most \(\pi/2\). The midpoint grid, after division by \(R\), is a Riemann-sum discretization of uniform measure on \([a,b]\); its Wasserstein-\(1\) error is \(O(R^{-1})\). The \(O(1)\) edge roots contribute at most \(O(R^{-1})\) of total normalized mass and remain in a uniformly bounded rescaled region. The second source coordinate obeys \(y/R=v/R-x/R\), so replacing it by \(-x/R\) costs another \(O(|v|/R)\). The triangle inequality for couplings proves the quantitative Wasserstein bound and the uniformity assertion.

**5. The singular decoupled limit.** At \(\beta=0\), the map becomes \((x,y)\mapsto(\alpha\cos x,y+x)\). Any \(u\in[-\alpha,\alpha]\) has infinitely many solutions \(x\) of \(\cos x=u/\alpha\), each with \(y=v-x\), whereas \(|u|>\alpha\) has none. This proves the final limiting image and fiber assertions.

## Verification

The accompanying standalone script `checks/verify_inverse.py` checks the exact scalar inverse identity, Jacobian identity, signs at representative regular preimages, and numerical root-count examples at several target positions and cubic scales. Those finite checks exercise the formulas but **do not certify** the asymptotic assertions. The complete count, properness, degree and distribution conclusions follow from the inequalities and inverse reduction proved above.

## Relationship to prior work

Almatroud and Pham [1] introduce precisely the cosine–quadratic-memristance map (their equation (5)) and investigate simulated bifurcations, Lyapunov exponents and implementation. Their accessible full article does not derive one-step inverse multiplicities, a properness transition, an inverse scaling limit, or the target-dependent cubic-root coefficient. A closely related published mathematical analysis of **the same map**, *A sharp two-cycle fold and a three-halves onset law for a fixed-point-free memristor map* [2], concerns solutions of the second iterate and the existence of two-cycles for \(1<\beta\le2\); neither its statement nor its inverse-elimination argument covers the one-step \(\beta\downarrow0\) fiber census. A distinct cosine-memristive Chialvo map [3] has infinitely many inverse images already at nonzero coupling because its nonlinear part decays at infinity, whereas the present cubic map is proper for every \(\beta>0\). General noninvertible-map critical-curve theory [4] supplies background terminology but not the particular scaling coefficient or equidistribution. These comparisons support a provisional originality assessment, not absolute publication priority.

## Limitations

The asymptotic formula and Wasserstein estimate exclude the two resonant target lines \(u=\pm\alpha\). Constants in the remainder may deteriorate as a target approaches those lines or as \(\alpha\to0\); no uniformity in such joint limits is asserted. No statement about complex inverse points, higher iterates, attractors, invariant measures, ergodicity, numerical cryptographic quality, or conditioning of the full inverse map is made. The uniform inverse-sheet distribution is an empirical distribution across **all preimages of one target**, not a time-stationary distribution. Publication-priority comparisons remain subject to unavailable or unindexed literature; independent scientific validation has not occurred.

## References

1. O. A. Almatroud and V.-T. Pham, *Building Fixed Point-Free Maps with Memristor*, Mathematics **11** (2023), 1319, public 2023-03-09. https://doi.org/10.3390/math11061319 ; https://www.mdpi.com/2227-7390/11/6/1319 .
2. *A sharp two-cycle fold and a three-halves onset law for a fixed-point-free memristor map*, public research record 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-two-cycle-fold-and-a-three-halves-onset-law-for-a-fixed--3b64e28eaf02 .
3. *Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map*, public research record 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-singular-zero-to-infinite-inverse-valence-transition-in-a-cosine--8b96b0ec53ba .
4. C. Mira, *Noninvertible maps*, Scholarpedia **2** (2007), 2328. https://www.scholarpedia.org/article/Noninvertible_maps .
