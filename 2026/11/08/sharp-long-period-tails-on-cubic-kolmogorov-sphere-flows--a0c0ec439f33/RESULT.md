# Sharp long-period tails on cubic Kolmogorov sphere flows

## Finding
Let \(a,b,c>0\). On the unit sphere in \(\mathbb R^3\), consider the cubic vector field
\[
\dot x=x(ay^2-bz^2),\qquad
\dot y=y(-ax^2+cz^2),\qquad
\dot z=z(bx^2-cy^2).
\]
Set \(u=x^2\), \(v=y^2\), \(w=z^2\), \(S=a+b+c\), and
\[
H=u^cv^bw^a,\qquad H_*=(c/S)^c(b/S)^b(a/S)^a.
\]
For every \(h\in(0,H_*)\), each connected component of \(\{H=h\}\) in an open coordinate octant is a periodic orbit, with a common least period \(T(h)\). Its exact logarithmic growth is
\[
T(h)=\frac{a+b+c}{2abc}\log\frac1h+O_{a,b,c}(1)
\qquad(h\downarrow0).
\]
Select an initial point uniformly according to normalized Euclidean surface area on the sphere and let \(\mathcal T\) denote its least period, defined almost everywhere. Write \(m=\max\{a,b,c\}\). Then
\[
\boxed{\lim_{t\to\infty}\frac1t\log\Pr\{\mathcal T>t\}
=-\frac{abc}{(a+b+c)m}.}
\]
Moreover, for every \(s\ge0\),
\[
\boxed{\mathbb E[e^{s\mathcal T}]<\infty\ \Longleftrightarrow\ 0\le s<\frac{abc}{(a+b+c)m}.}
\]
The borderline exponential moment diverges. For \(a=b=c=1\), the tail's logarithmic rate is \(-1/3\), and the exact moment threshold is \(1/3\).

## Assumptions and scope
All parameters are positive and finite. Physical time is the original time in the displayed cubic vector field; no orbital time change is permitted. The initial distribution is normalized spherical surface area, not Lebesgue measure on the squared-coordinate simplex. Coordinate planes and the finitely many equilibrium points have zero surface area and are excluded when defining \(\mathcal T\). The result holds uniformly across all eight sign octants because signs are invariant and the squared-coordinate equations agree.

## Proof
**First integral and periodic foliation.** Differentiate \(u+v+w\) and \(\log H\) under
\[
\dot u=2u(av-bw),\quad \dot v=2v(-au+cw),\quad \dot w=2w(bu-cv).
\]
The two derivatives vanish identically. On \(u,v,w>0\) and \(u+v+w=1\), the function \(\log H=c\log u+b\log v+a\log w\) is strictly concave, has its unique maximum at \((c,b,a)/S\), and tends to minus infinity along the simplex boundary. Hence each regular level \(H=h\) in the open simplex is a smooth simple closed curve bounding a strictly convex superlevel set. The vector field has no equilibrium on such a curve: its only interior equilibrium solves \(av=bw\), \(au=cw\), giving \((u,v,w)=(c,b,a)/S\). A nowhere-zero tangent vector field on a compact circle has a finite minimal period, denoted \(T(h)\). Squaring is a smooth bijection from each sign octant on the sphere onto the open simplex, so this is also the original sphere-flow period.

**Sharp physical-time divergence.** Let \(L=-\log h\). Fix a sufficiently small \(\delta>0\) and intersect the level curve with the three vertex neighborhoods \(U_u=\{u>1-\delta\}\), \(U_v=\{v>1-\delta\}\), \(U_w=\{w>1-\delta\}\). Each neighborhood contains one connected passage of the periodic orbit for sufficiently small \(h\). In \(U_u\), the flow enters near \((u,v,w)=(1-\delta,\delta,0)\) and leaves near \((1-\delta,0,\delta)\). On entering, \(v=\delta+o(1)\); on leaving, the invariant \(H=h\) yields \(\log v=-L/b+O_\delta(1)\). Furthermore,
\[
\frac d{dt}\log v=-2a+2av+2(a+c)w.
\]
For sufficiently small fixed \(\delta\), \(v\) decreases exponentially and \(w\) increases exponentially throughout this passage: their logarithmic rates are bounded away from zero with the indicated signs. Therefore \(\int_{U_u\text{-passage}}(v+w)\,dt=O_\delta(1)\), independent of \(h\). Integrating the displayed identity gives passage time \(L/(2ab)+O_\delta(1)\). The analogous analysis at \(U_v\) gives \(L/(2ac)+O_\delta(1)\) and at \(U_w\) gives \(L/(2bc)+O_\delta(1)\). The remaining three arcs tend to compact subarcs of the boundary heteroclinic connections away from the vertices, where the flow has nonzero speed, so their total passage time is \(O_\delta(1)\). Adding proves
\[
T(h)=\left(\frac1{2ab}+\frac1{2ac}+\frac1{2bc}\right)L+O(1)
=\frac{S}{2abc}L+O(1).
\]
For any fixed \(h>0\), the period is finite. It remains bounded as \(h\uparrow H_*\), since the linearization at the center has nonzero imaginary eigenvalues \(\pm2i\sqrt{abc/S}\); in fact \(T(h)\to\pi\sqrt{S/(abc)}\).

**Spherical area and the sharp tail.** Normalized spherical area, conditional on any octant, pushes forward under \((x,y,z)\mapsto(x^2,y^2,z^2)\) to the Dirichlet distribution with three parameters \(1/2\). Its simplex density is \((2\pi)^{-1}(uvw)^{-1/2}\). Thus for \(q\ge0\),
\[
\mathbb E[H^{-q}] =
\frac{\Gamma(3/2)}{\Gamma(3/2-qS)}
\frac{\Gamma(1/2-qc)\Gamma(1/2-qb)\Gamma(1/2-qa)}{\Gamma(1/2)^3}
\quad\text{if }q<\frac1{2m}.
\]
If \(q\ge1/(2m)\), the corresponding beta integral diverges near the face of the variable with maximal exponent, so \(\mathbb E[H^{-q}]=\infty\). Put \(\kappa=S/(2abc)\) and \(\gamma=1/(2m\kappa)=abc/(Sm)\). The period asymptotic implies that for all sufficiently small \(H\), the ratio \(e^{s\mathcal T}/H^{-s\kappa}\) stays between two strictly positive constants depending on \(s,a,b,c\). Away from \(H=0\), the period is bounded. Consequently \(\mathbb E[e^{s\mathcal T}]<\infty\) precisely when \(s\kappa<1/(2m)\), including strict divergence at equality. Finally, for each \(0<s<\gamma\), Markov's inequality yields \(\Pr(\mathcal T>t)\le C_s e^{-st}\). For \(s>\gamma\), the converse logarithmic bound follows from the Dirichlet small-\(H\) exponent: \(\lim_{h\downarrow0}(\log\Pr\{H<h\})/(\log h)=1/(2m)\). To see this last equality, the negative moments give an upper bound for every exponent below \(1/(2m)\), and restricting the other two simplex coordinates to a fixed positive interval while letting a maximal-weight coordinate approach zero supplies the matching lower bound. Combining with \(\mathcal T=\kappa\log(1/H)+O(1)\) gives the claimed tail limit.

## Verification
The standalone checker evaluates the exact algebraic first-integral cancellation, the linearized center frequency, the Dirichlet negative-moment threshold, and numerical return times at decreasing energy for two parameter triples. Numerical return-time approximations check normalization of the theoretical coefficient but cannot prove its all-parameter asymptotics. The analytic passage-time estimates and Dirichlet integral provide the proof for arbitrary positive coefficients.

## Relationship to prior work
Benny, Jana and Sarkar classify cubic Kolmogorov vector fields on the sphere, identify the sign regime with interior equilibria, and discuss phase portraits and center/focus conditions; their preprint does not state the spherical-area long-period law or the exact exponential-moment cutoff. Standard zero-sum rock–paper–scissors replicator theory already supplies periodicity and conservation of a weighted product; these are used, not claimed as new. Classical slowing near a heteroclinic cycle motivates the calculation, but the stated formula combines the actual cubic-flow time, all three unequal coefficients and the surface-area sampling law. The paper by Boone and Piliouras concerns general recurrence/periodicity of zero-sum replicator dynamics rather than this period distribution. See references.

## Limitations
The statement is a logarithmic tail exponent, not an asymptotic equivalent with a prefactor. The period coefficient is specific to the original cubic-flow time. The measure threshold is for surface-area sampling; a different law on the simplex changes the endpoint exponents. The theorem does not claim to resolve period monotonicity for all parameters, and does not cover sign regimes without a positive interior equilibrium. Equivalent detailed calculations could exist in unindexed literature; independent mathematical validation remains open.

## References
- J. Benny, S. Jana, and S. Sarkar, *Invariant circles and phase portraits of cubic vector fields on the sphere*, arXiv:2310.14238, first posted 2023-10-22, especially §5, equations (5.1)–(5.5).
- V. Boone and G. Piliouras, *From Darwin to Poincaré and von Neumann: Recurrence and Cycles in Evolutionary and Algorithmic Game Theory*, arXiv:1910.01334 (2019).
- M. W. Hirsch, S. Smale, and R. L. Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos*, for standard planar periodic-flow and center theory.
