# Uniform tropical phase and logarithmic-abundance laws near a cubic sphere-flow heteroclinic cycle

## Finding
For every fixed \(a,b,c>0\), consider the cubic Kolmogorov vector field on the unit sphere
\[
\dot x=x(ay^2-bz^2),\qquad
\dot y=y(-ax^2+cz^2),\qquad
\dot z=z(bx^2-cy^2).
\]
In any open sign octant, put \(u=x^2\), \(v=y^2\), \(w=z^2\) and \(H=u^cv^bw^a\). Let \(S=a+b+c\) and \(H_*=(c/S)^c(b/S)^b(a/S)^a\). Each level \(H=h\) for \(0<h<H_*\) is one periodic orbit per octant; let \(T_h\) denote its minimal period in the displayed physical time. Set \(L=\log(1/h)\), \(P=S/(2abc)\), and
\[
V_u=(0,0,1/a),\qquad V_w=(0,1/b,0),\qquad V_v=(1/c,0,0).
\]
Let \(\Gamma:[0,P]\to\mathbb R^3\) be the oriented closed broken line, parameterized linearly on its three edges by
\[
\Gamma(s)=\begin{cases}
(0,2as,1/a-2bs),&0\le s\le1/(2ab),\\
(2b(s-1/(2ab)),1/b-2c(s-1/(2ab)),0),&1/(2ab)\le s\le1/(2ab)+1/(2bc),\\
(1/c-2a(s-1/(2ab)-1/(2bc)),0,2c(s-1/(2ab)-1/(2bc))),&1/(2ab)+1/(2bc)\le s\le P.
\end{cases}
\]
Fix any sufficiently small \(\delta>0\), and choose the time origin at the unique forward crossing of \(u=1-\delta\) with \(\dot u>0\). For the logarithmic-abundance vector
\[
E_h(t)=\frac1L\big(-\log u(t),-\log v(t),-\log w(t)\big),
\]
there are constants \(h_0,C>0\), depending on the fixed coefficients and \(\delta\), such that for every \(0<h<h_0\),
\[
\boxed{\quad\sup_{0\le\theta\le1}\left\|E_h(\theta T_h)-\Gamma(\theta P)\right\|_\infty\le\frac C{\log(1/h)}.\quad}
\]
The already-known period estimate \(T_h=P\log(1/h)+O(1)\) supplies the physical-time normalization; the new assertion is **uniform convergence of the entire phase-resolved logarithmic orbit, with a quantitative rate**.

In particular, sampling one orbital phase uniformly in the original physical time gives a log-abundance probability law \(\mu_h\) satisfying
\[
\boxed{\quad W_1(\mu_h,\mu_\infty)\le \frac{C'}{\log(1/h)},\qquad
\mu_\infty=\frac cS\,\operatorname{Unif}[V_u,V_w]+\frac aS\,\operatorname{Unif}[V_w,V_v]+\frac bS\,\operatorname{Unif}[V_v,V_u].\quad}
\]
Here \(W_1\) is 1-Wasserstein distance for Euclidean cost and \(\operatorname{Unif}[A,B]\) is normalized arclength measure on the indicated straight segment. Its three one-coordinate marginals are exactly
\[
\begin{aligned}
-\log u/L &: \quad (c/S)\,\delta_0+((a+b)/S)\,\operatorname{Unif}[0,1/c],\\
-\log v/L &: \quad (b/S)\,\delta_0+((a+c)/S)\,\operatorname{Unif}[0,1/b],\\
-\log w/L &: \quad (a/S)\,\delta_0+((b+c)/S)\,\operatorname{Unif}[0,1/a].
\end{aligned}
\]
In the symmetric case \(a=b=c=1\), each marginal has the limiting law \((1/3)\delta_0+(2/3)\operatorname{Unif}[0,1]\). All statements hold identically in every open sign octant.

## Assumptions and scope
Coefficients \(a,b,c\) are arbitrary fixed positive real numbers. The parameter \(h\downarrow0\) means the conserved orbit label tends to zero while coefficients remain fixed. Define the positive simplex \(\{u,v,w>0:u+v+w=1\}\). All logarithms are natural logarithms of its strictly positive coordinates; there is no log of zero at any finite positive \(h\). The sign octants are invariant, and the squared-coordinate dynamics are identical in all of them. The reference triangle lies in \(\{(p,q,r)\ge0:cp+bq+ar=1\}\). The normalized time parameter \(\theta=t/T_h\) uses original physical time, not an accelerated time variable. The crossing convention selects phase uniquely for sufficiently small \(h\). Pointwise boundary equilibria are excluded from the periodic orbit family.

## Proof
**1. Periodic foliation and the exact log constraint.** Direct differentiation under
\[
\dot u=2u(av-bw),\qquad\dot v=2v(-au+cw),\qquad\dot w=2w(bu-cv)
\]
gives \(\dot u+\dot v+\dot w=0\) and \(d(\log H)/dt=0\). On the simplex, \(c\log u+b\log v+a\log w\) is strictly concave, reaches the unique maximum \(\log H_*\) at \((c,b,a)/S\), and tends to \(-\infty\) at its boundary. Hence every \(0<h<H_*\) level is a compact smooth simple closed curve, with no stationary point because the only interior equilibrium is \((c,b,a)/S\). It is therefore one periodic orbit. The exact identity
\[
c\frac{-\log u}L+b\frac{-\log v}L+a\frac{-\log w}L=1
\]
places \(E_h\) on the stated closed triangle for every \(h\); since at least one of \(u,v,w\) is at least \(1/3\), the smallest logarithmic coordinate of \(E_h\) is at most \(\log3/L\).

**2. Three vertex passages, including uniform errors at intermediate times.** Choose \(\delta\) small enough that \(u>1-\delta\) implies \((\log v)'\le-a<0\) and \((\log w)'\ge b>0\). On any sufficiently low level \(H=h\), its intersection with \(\{u\ge1-\delta\}\) is one passage. At the entering section \(u=1-\delta\), one has \(v=\delta+o(1)\), \(w=o(1)\), and at exit \(v=o(1)\), \(w=\delta+o(1)\). These claims follow from strict monotonicity of \(v\) and \(w\) inside the neighborhood and the two solutions of \((1-\delta)^cv^bw^a=h\), \(v+w=\delta\). In the passage, \(v\) decreases exponentially from at most \(\delta\), while \(w\) increases exponentially to at most \(\delta\); hence
\[
\int_{\{u\ge1-\delta\}}(v+w)\,dt=O_{a,b,c,\delta}(1).
\]
Letting \(\tau\) be time since its entry, the exact differential identities
\[
(\log v)'=-2a+2av+2(a+c)w,\qquad
(\log w)'=2b-2(b+c)v-2bw
\]
therefore imply, **uniformly for every time inside that passage**,
\[
\log u=O(1),\qquad\log v=-2a\tau+O(1),\qquad
\log w=-L/a+2b\tau+O(1).
\]
The exit condition \(v=h^{1/b}O(1)\) gives the passage duration \(L/(2ab)+O(1)\). Thus the logarithmic vector over the entire passage differs by at most \(O(1/L)\) from the affine path \((0,2a\tau/L,1/a-2b\tau/L)\).

Repeat cyclically at \(w\ge1-\delta\): the coordinate \(u\) decreases with \((\log u)'=-2b+O(u+v)\), the coordinate \(v\) grows with \((\log v)'=2c+O(u+v)\), and the integrated perturbation is \(O(1)\). This yields passage time \(L/(2bc)+O(1)\) and affine logarithmic path \((2b\tau/L,1/b-2c\tau/L,0)+O(1/L)\). At \(v\ge1-\delta\), the passage time is \(L/(2ac)+O(1)\), and its affine path is \((1/c-2a\tau/L,0,2c\tau/L)+O(1/L)\). All errors here are uniform in passage time, not merely endpoint estimates.

**3. Transition arcs and the whole-orbit estimate.** Between successive vertex neighborhoods the level curves converge, by the conserved-product equation, to compact subarcs of the three open simplex edges; on these subarcs the vector field has nonzero limiting speed. Their total physical traversal time is therefore \(O_{a,b,c,\delta}(1)\). Every logarithmic derivative \((\log u)'\), \((\log v)'\), \((\log w)'\) is bounded in absolute value by a coefficient-dependent constant on the entire simplex. It follows that, along each bounded-time transition arc, \(E_h\) changes by at most \(O(1/L)\). This also matches the adjacent affine passage endpoints at the appropriate vertex, with \(O(1/L)\) discrepancy. Adding the three passages and three connecting arcs recovers
\[
T_h=L\left(\frac1{2ab}+\frac1{2bc}+\frac1{2ac}\right)+O(1)=LP+O(1),
\]
consistent with the previously published physical-time coefficient. The cumulative boundaries of all six arcs differ by \(O(1)\) from their prescribed multiples of \(L\). Since \(T_h=LP+O(1)\), for \(t=\theta T_h\) the parameter \(t/L\) differs uniformly by \(O(1/L)\) from \(\theta P\). The three affine paths have uniformly bounded slopes. Combining this timing discrepancy with the passage and transition errors proves the claimed global supremum bound.

**4. The explicit time-sampling law.** Let \(\Theta\) be uniform on \([0,1]\). Couple \(E_h(\Theta T_h)\) with \(\Gamma(\Theta P)\) using the same \(\Theta\). Their Euclidean expected distance is at most \(\sqrt3\,C/L\); by the coupling characterization of \(W_1\), the desired rate follows. The three intervals of the parameter \(s\in[0,P]\) have lengths \(1/(2ab)\), \(1/(2bc)\), \(1/(2ac)\). Dividing by \(P\) gives edge probabilities \(c/S\), \(a/S\), \(b/S\). Since \(\Gamma\) moves affinely at a constant speed along each segment, its conditional law is normalized arclength there. Projecting to any coordinate yields a point mass when that coordinate vanishes on one edge, and a uniform interval law on each of the other two edges. Their mixture yields precisely the three displayed marginal formulas. This finishes the proof.

## Verification
The standalone finite numerical checker `check_tropical_phase.py` integrates the logarithmic differential equations in original time and identifies the first full return to the increasing section \(u=1-\delta\). It compares the period with \(P\log(1/h)\) and the entire sampled normalized phase with \(\Gamma\). For \((a,b,c)=(1,1,1)\) at \(h=10^{-8}\), it gives period approximately \(27.631022549\) versus leading \(27.631021116\), and a normalized sup-error approximately \(0.122042\). For \((a,b,c)=(2,3,1)\) at \(h=10^{-11}\), it gives period approximately \(12.664218018\) versus leading \(12.664218011\), and sup-error approximately \(0.140716\). The checker prints `TROPICAL_KOLMOGOROV_LOG_PHASE_CHECK_OK` if those finite checks pass. These computations check normalization and consistency only; they do not establish convergence or the uniform all-coefficient theorem, whose proof is analytic above.

## Relationship to prior work
Benny, Jana and Sarkar, arXiv:2310.14238v1, §3 and §5, classify cubic Kolmogorov vector fields on the sphere and discuss invariant-circle and phase-portrait questions. Their full text does not state this rescaled log-composition orbit law or its time-sampling distribution. The separate published result *Sharp long-period tails on cubic Kolmogorov sphere flows* addresses **exactly this family** and already proves \(T_h=P\log(1/h)+O(1)\), along with an exponential period-tail cutoff under random spherical surface-area sampling. That period result is used as prior knowledge, not claimed as new. Its period tail concerns an ensemble of initial orbit energies, whereas this theorem concerns the phase-resolved trajectory and its time distribution on **one orbit at fixed small \(h\)**; its conclusions do not provide the present uniform logarithmic phase bound and explicit coordinate-mixture laws. Another published study, *Sharp logarithmic phase and time statistics in a cubic global center*, analyzes a different planar polynomial system; no equivalence of those phase variables or physical times was established. General zero-sum replicator recurrence theory provides a qualitative framework but no identical quantitative theorem in the inspected sections.

## Limitations
All parameters must be strictly positive and held fixed while \(h\to0\). No coefficient-uniform constant near \(a=0\), \(b=0\) or \(c=0\) is asserted. The error rate is an upper bound, not a claimed optimal constant. The probability convergence is in \(W_1\), **not** total variation: a two-dimensional edge-supported limit cannot have total-variation proximity to most finite-\(h\) continuously supported orbit curves. The theorem does not claim a law for randomly selected orbital energies or an infinite-time limit along one nonperiodic orbit. Precise equivalent singular-cycle laws in unindexed literature remain a priority risk; the bibliographic comparison is not an independent certification.

## References
1. J. Benny, S. Jana and S. Sarkar, *Invariant circles and phase portraits of cubic vector fields on the sphere*, arXiv:2310.14238v1, first posted 2023-10-22; especially Corollary 3.3 and §5. https://arxiv.org/html/2310.14238v1.
2. *Sharp long-period tails on cubic Kolmogorov sphere flows*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-long-period-tails-on-cubic-kolmogorov-sphere-flows--a0c0ec439f33/ . Its period law and sampling cutoff are prior mathematics here.
3. *Sharp logarithmic phase and time statistics in a cubic global center*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-logarithmic-phase-and-time-statistics-in-a-cubic-global-ce--35ffbf168a22/ . The object is a different planar cubic center.
4. V. Boone and G. Piliouras, *From Darwin to Poincaré and von Neumann: Recurrence and Cycles in Evolutionary and Algorithmic Game Theory*, arXiv:1910.01334 (2019), for qualitative replicator recurrence context.
