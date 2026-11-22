# A sharp diameter-contact and rare-chord transition for a one-turn circular helix

## Finding
Let \(L=2\pi\), \(c\ge0\), and let the finite circular helix be
\[
\Gamma_c=\{\gamma_c(t)=(\cos t,\sin t,ct):0\le t\le L\}.
\]
Independently choose \(U,V\) uniformly with respect to arclength on \(\Gamma_c\); this is equivalent to independently uniform parameters on \([0,L]\), because the speed is the constant \(\sqrt{1+c^2}\). Write \(X_c=|\gamma_c(U)-\gamma_c(V)|\) and let \(D(c)\) be the Euclidean diameter of \(\Gamma_c\).

There is a unique \(\xi\in(\pi,\rho)\), where \(\rho\in(\pi,3\pi/2)\) is the unique root of \(\rho\cos\rho-\sin\rho=0\), satisfying
\[
2(1-\cos\xi)+(L^2-\xi^2)\frac{\sin\xi}{\xi}=0.
\]
Define
\[
c_*=\sqrt{\frac{2(1-\cos\xi)}{L^2-\xi^2}}=0.378586747112271\ldots,
\qquad \xi=3.700677245123620\ldots.
\]
For every \(0\le c<c_*\), the diameter is attained precisely by pairs separated by \(s_c\in[\pi,\xi)\), the unique root of \(\sin s_c+c^2s_c=0\) in that range (with \(s_0=\pi\)); thus \(D(c)=\sqrt{2(1-\cos s_c)+c^2s_c^2}\). For \(c>c_*\), the only diametral unordered pair is the two endpoints, and \(D(c)=cL\). At \(c=c_*\), the interior separation \(\xi\) and the endpoint pair both attain diameter. The diameter function is continuous but has a strict first-derivative jump at \(c_*\): its left and right derivatives are \(\xi^2/L\) and \(L\).

The random-chord upper tail changes its exponent at this contact transition. For fixed \(0\le c\le c_*\), let \(s_c=\xi\) when \(c=c_*\), and put
\[
C(c)=\frac{4(L-s_c)}{L^2}\sqrt{\frac{2D(c)}{-\cos s_c-c^2}}.
\]
Then, as \(\varepsilon\downarrow0\),
\[
\Pr\{X_c\ge D(c)-\varepsilon\}=C(c)\sqrt\varepsilon+o_c(\sqrt\varepsilon).
\]
In particular \(C(0)=2/\pi\) and \(C(c_*)=0.680010892323401\ldots\). For every fixed \(c>c_*\),
\[
\Pr\{X_c\ge D(c)-\varepsilon\}=\frac{\varepsilon^2}{c^2L^2}+o_c(\varepsilon^2).
\]
The singular transition admits a moving-parameter law: for every fixed real \(\lambda\), set \(c_\varepsilon=c_*+\lambda\varepsilon\), which is nonnegative for all sufficiently small \(\varepsilon\), and \(J=(L^2-\xi^2)/L=4.10355644012597\ldots\). Then
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr\{X_{c_\varepsilon}\ge D(c_\varepsilon)-\varepsilon\}}{\sqrt\varepsilon}
=C(c_*)\sqrt{[1-J\max(\lambda,0)]_+},\qquad [x]_+=\max\{x,0\}.
\]
This square-root crossover vanishes exactly from \(\lambda\ge1/J\) onward.

There are also complete leading conditional endpoint laws. For fixed \(0\le c\le c_*\), conditioned on \(X_c\ge D(c)-\varepsilon\), the pair
\[
\left(\frac{|U-V|-s_c}{\sqrt\varepsilon},\min(U,V)\right)
\]
converges in distribution to the product of the uniform distributions on \([-b_c,b_c]\) and \([0,L-s_c]\), with
\(b_c=\sqrt{2D(c)/(-\cos s_c-c^2)}\). For fixed \(c>c_*\), the endpoint gaps \((\min(U,V),\,L-\max(U,V))/\varepsilon\), conditioned on the same event, converge to uniform area measure on the triangle \(\{(x,y):x,y\ge0,\ x+y\le 1/c\}\). In both cases the orientation of the ordered sample pair is an independent fair sign.

## Assumptions and scope
The helix has unit horizontal radius and exactly one full parameter revolution. The pitch parameter \(c\) is the axial rise per radian divided by the radius, and the full axial rise is \(2\pi c\). Sampling is independent and uniform in **arclength along the curve**, not uniform on the bounding cylinder. At \(c=0\), the endpoints coincide geometrically but independent continuous sampling and the chord law remain well-defined. A diameter is the maximum Euclidean distance between any two points of the continuous arc; no discretization is assumed. All asymptotics concern \(\varepsilon>0\) tending to zero, with \(c\) fixed unless a moving parameter is explicitly specified.

## Proof
**Step 1: Exact reduction and sampling density.** A pair at parameter separation \(s=|u-v|\in[0,L]\) has squared Euclidean distance
\[
f_c(s)=2(1-\cos s)+c^2s^2.
\]
The separation of two independent uniform points on \([0,L]\) has density \(w(s)=2(L-s)/L^2\) for \(0<s<L\). Therefore the entire geometric optimization and stochastic tail reduce to the one-variable function \(d_c(s)=\sqrt{f_c(s)}\) with this explicit nonuniform weight.

**Step 2: Uniqueness of the critical contact.** For \(0<s<L\), define
\[
h(s)=\frac{2(1-\cos s)}{L^2-s^2}.
\]
Then \(f_c(s)-f_c(L)=(L^2-s^2)(h(s)-c^2)\). On \((0,\pi)\), the numerator strictly increases and the positive denominator decreases, so \(h\) strictly increases. For \(\pi<s<L\), set \(z=s^2\) and \(q(z)=2(1-\cos\sqrt z)\). Direct differentiation yields
\[
q'(z)=\frac{\sin s}{s},\qquad q''(z)=\frac{s\cos s-\sin s}{2s^3}.
\]
The function \(s\cos s-\sin s\) has derivative \(-s\sin s>0\) on \((\pi,L)\) and changes sign exactly once at \(\rho\in(\pi,3\pi/2)\). The derivative of \(h(\sqrt z)\) has the sign of
\[
B(z)=q'(z)(L^2-z)+q(z),\qquad B'(z)=q''(z)(L^2-z).
\]
Here \(B(\pi^2)=4>0\), \(B(L^2)=0\), and \(B\) is strictly increasing on \((\rho^2,L^2)\); consequently \(B<0\) throughout that interval. On \((\pi^2,\rho^2)\), \(B\) is strictly decreasing, hence has exactly one zero, \(\xi^2\). Since \(h(s)\to0\) as \(s\uparrow L\) and \(h(0)=0\), \(\xi\) is its unique global maximizer. Differentiation at its maximum also gives \(c_*^2=h(\xi)=-\sin\xi/\xi\).

**Step 3: Complete diameter classification.** By the comparison identity, if \(c^2>c_*^2\), \(f_c(L)>f_c(s)\) for all \(s<L\); equality occurs only at \(c=c_*\), \(s=\xi\). If \(c<c_*\), there exists an interior separation exceeding the endpoint distance. The stationarity equation is \(\sin s+c^2s=0\). On \((\pi,L)\), \(g(s)=-\sin s/s\) increases strictly to its unique maximum at \(\rho\), then decreases strictly to zero. Because \(c_*^2=g(\xi)<g(\rho)\), for \(0<c\le c_*\) the smaller root \(s_c\in(\pi,\rho)\) is a strict local maximum of \(f_c\), while any second root is a local minimum. For \(c=0\), \(s_0=\pi\) is the unique interior maximum. Thus there can be no other global interior maximum. At \(c=c_*\), the endpoint and \(s_c=\xi\) tie. Differentiating the interior branch of \(D(c)\) via the envelope theorem gives \(D'_-(c_*)=c_*\xi^2/D(c_*)=\xi^2/L\), whereas the endpoint branch \(cL\) has derivative \(L\). This proves the strict corner.

**Step 4: Interior upper tails.** At \(s=s_c\), stationarity and the local maximum imply \(-\cos s_c-c^2>0\) (equivalently \(s_c g'(s_c)>0\)). Differentiating the square root at the stationary point gives
\[
d_c(s_c+x)=D(c)-\frac{-\cos s_c-c^2}{2D(c)}x^2+O_c(|x|^3).
\]
The event \(d_c(s)\ge D(c)-\varepsilon\) near \(s_c\) therefore occupies an interval whose scaled endpoints tend to \(\pm b_c\). Integrating the continuous positive separation density at \(s_c\) gives \(2b_cw(s_c)\sqrt\varepsilon=C(c)\sqrt\varepsilon\). At \(c=c_*\) there is also an endpoint-maximizing branch, but its probability is only \(O(\varepsilon^2)\), so it does not affect the leading square-root coefficient.

**Step 5: Endpoint upper tails.** If \(c>c_*\), only \(s=L\) is maximizing. Writing \(s=L-h\), we have \(D(c)=cL\), \(d'_c(L)=c\), and hence \(D(c)-d_c(L-h)=ch+O_c(h^2)\). The event is \(0\le h\le\varepsilon/c+O_c(\varepsilon^2)\). Integrating \(w(L-h)=2h/L^2\) produces \(\varepsilon^2/(c^2L^2)+o_c(\varepsilon^2)\).

**Step 6: Moving-parameter crossover.** The strict interior critical point persists smoothly for \(c\) near \(c_*\); call its distance \(D_{\mathrm{int}}(c)\). At \(c_*\), \(D_{\mathrm{int}}(c_*)=c_*L\) and
\[
\frac{d}{dc}\left[cL-D_{\mathrm{int}}(c)\right]_{c=c_*}
=L-\frac{\xi^2}{L}=J>0.
\]
Thus for \(c=c_*+\lambda\varepsilon\), the difference between the global maximum and the local interior maximum is \(\varepsilon[J\lambda]_++o(\varepsilon)\). Combining this with the uniform quadratic expansion near \(\xi\) gives an interior interval of width \(2b_{c_*}\sqrt{[1-J\max(\lambda,0)]_+}\sqrt\varepsilon+o(\sqrt\varepsilon)\). Endpoint contributions are \(O(\varepsilon^2)\), and no other separated region approaches the global maximum; compactness supplies the required uniform gap away from the two contact sets. This proves the crossover, including the zero value at and beyond its cutoff.

**Step 7: Conditional geometries.** On the ordered region \(U<V\), the joint density is constant and the coordinate change \((U,V)\mapsto(U,V-U)\) has Jacobian one. Consequently, at an interior maximum, the basepoint is asymptotically uniform on \([0,L-s_c]\), independent of the centered, rescaled separation, which is uniform on \([-b_c,b_c]\). At an endpoint maximum, the change \((U,V)\mapsto(U,L-V)\) likewise has unit Jacobian and converts the leading event to \(c(U+L-V)\le\varepsilon\), yielding a uniform triangular law after scaling. Restoring the two possible sample orders gives an independent fair sign.

## Verification
The included `CHECKER.py` uses Python 3 standard-library arithmetic, bisection, exact integration of the triangular separation density over numerically located level sets, and parameter grids. Run `python3 CHECKER.py` from the extracted artifact directory. Its 28,036 deterministic assertions reproduce the critical values, compare the proposed diameter with dense feasible competitors, and check fixed-parameter and moving-parameter upper-tail laws against unexpanded chord distances. These finite numerical diagnostics are not a substitute for Steps 1–7, which supply the infinite statements.

## Relationship to prior work
A. T. Ali's 2011 general-helix paper gives Frenet and standard-frame representations, including the classical circular helix (its Lemmas 3.2 and 4.3); it does not optimize two-point diameter over a fixed finite turn or derive a stochastic chord tail. Starostin and van der Heijden's 2014 cylindrical-curve characterization gives moving-frame tests for a curve to lie on a cylinder, rather than two-point extremal geometry. Olsen and Bohr's 2012 geometric study of tubular helices analyzes interpoint-distance stationary conditions for *shortest* self-contact and packing, rather than the *largest* distance over a one-turn finite arc. Luo's 2026 work treats the closest point from an arbitrary fixed point to a circular helix, including Kepler-equation root counts, but not the diametral-pair switch or the independent two-point upper-tail distribution. A published one-turn-helix random-tetrahedron study concerns an orientation determinant of four sample points, not pair distances. Known general near-diameter limit principles do not alone determine the pitch threshold, explicit coefficients, or moving-parameter crossover established here. The present result should not be construed as rediscovering the classical helix parametrization or its distance formula.

## Limitations
The classification concerns exactly one full turn at fixed unit horizontal radius; no general multi-turn, unequal-speed, variable-pitch, or nonuniform-sampling claim is made. The displayed upper tails are leading-order laws, not full finite-threshold distributions. The moving-parameter limit is on the scale \(c-c_*=O(\varepsilon)\) and does not claim a uniform fixed-parameter error estimate across all positive pitches. Numerical constants are approximations to explicitly characterized exact roots, not independently certified rational intervals. Comprehensive historical novelty is not established by a finite literature search, and an independent mathematical audit has not been performed.

## References
- A. T. Ali, *Position Vectors of General Helices in Euclidean 3-Space*, Bulletin of Mathematical Analysis and Applications **3** (2011), 198–205; first published 2011-04-02, primary classification 53A04. https://www.kurims.kyoto-u.ac.jp/EMIS/journals/BMAA/repository/docs/BMAA3-2-19.pdf
- E. L. Starostin and G. H. M. van der Heijden, *Characterisation of cylindrical curves*, first published 2014-12-05, Monatshefte für Mathematik **176** (2015), 481–491. https://pmc.ncbi.nlm.nih.gov/articles/PMC4372181/
- K. Olsen and J. Bohr, *Geometry of the toroidal N-helix: optimal-packing and zero-twist*, New Journal of Physics **14** (2012), 023063; published 2012-02-29. https://doi.org/10.1088/1367-2630/14/2/023063
- P. Luo, *Closest Points on a Circular Helix and Kepler's Equation: Exact Counting, Focal Surfaces, and the Principal-Branch Minimizer*, first public preprint 2026-08-18, later published in Mathematics 14 (2026), 3674. https://www.preprints.org/manuscript/202608.1202
- *A quartic orientation-reversal transition for random points on a circular helix*, publicly available research record dated 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-quartic-orientation-reversal-transition-for-random-points-on-a--1f7e1ed69262
