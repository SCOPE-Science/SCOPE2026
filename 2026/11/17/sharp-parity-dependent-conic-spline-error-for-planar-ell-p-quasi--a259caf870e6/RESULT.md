# Sharp parity-dependent conic-spline error for planar \(\ell_p\) quasi-norms

## Finding
Fix \(0<p<1\). Let
\[
q_p(x,y)=(|x|^p+|y|^p)^{1/p},\qquad
f_p(\theta)=q_p(\cos\theta,\sin\theta).
\]
For each integer \(N\ge2\), take the \(2N\) equally spaced unit rays at angles \(jh\), \(h=\pi/N\), and let \(Q_{p,N}\) be the unique continuous, positively homogeneous function that agrees with \(q_p\) on those rays and is linear on every intervening cone. Write
\[
E_{p,N}=\sup_{\theta\in\mathbb R}
|Q_{p,N}(\cos\theta,\sin\theta)-f_p(\theta)|.
\]
Then the exact leading coefficients **depend on the parity of \(N\)**:
\[
\boxed{\lim_{\substack{N\to\infty\\N\,\mathrm{even}}}\frac{E_{p,N}}{h^p}
=\frac{1-p}{p}\,p^{p/(1-p)}}\qquad\text{and}\qquad
\boxed{\lim_{\substack{N\to\infty\\N\,\mathrm{odd}}}\frac{E_{p,N}}{h^p}
=\frac{1}{p\,2^p}.}
\]
The second number is strictly greater than the first. For even \(N\), the leading extremal error is **underinterpolation**, occurring a distance asymptotic to \(p^{1/(1-p)}h\) from a coordinate axis. For odd \(N\), the leading extremal error is **overinterpolation**, at the two axes located halfway between consecutive rays. Thus the normalized error has two different subsequential limits even though both meshes are uniform.

There is a consistent endpoint statement: at \(p=1\), the sampled conic interpolant is exact for every even \(N\), whereas for every odd \(N\) its uniform angular error is **exactly** \(\tan(h/2)\). In particular the odd-grid coefficient tends to \(1/2\) as \(p\uparrow1\), but the even-grid coefficient tends to zero.

## Assumptions and scope
The exponent \(p\) is fixed in \((0,1)\) while the positive integer \(N\) increases. The interpolation scheme and node normalization coincide with the sampled planar conic B-splines of Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines*, Section 5.2 and Appendix B.2. On each sector \(\theta=jh+sh\), \(0\le s\le1\), it has the explicit angular representation
\[
I_{p,N}(\theta)=
\frac{\sin((1-s)h)f_p(jh)+\sin(sh)f_p((j+1)h)}{\sin h}.
\tag{1}
\]
This is *conic* (piecewise Cartesian-linear) interpolation, not ordinary linear interpolation in the angular coordinate. The absolute error is measured on the Euclidean unit circle; positive homogeneity then controls errors on arbitrary Euclidean spheres. No uniformity as \(p\downarrow0\) or \(p\uparrow1\) is asserted.

## Proof
**Step 1: Local shape of each singularity.** The profile is \(\pi/2\)-periodic and smooth away from the four coordinate axes. Writing \(d(\theta)\) for distance to the nearest axis, elementary expansion at an axis \(\alpha\) gives, for fixed \(p\in(0,1)\),
\[
f_p(\alpha+t)=1+\frac{|t|^p}{p}+o(|t|^p)\quad(t\to0).
\tag{2}
\]
The local error is therefore controlled by the interpolation of \(g_p(u)=|u|^p\). More quantitatively, on an axis-free interval at angular distance \(d>0\), direct differentiation gives
\[
|f_p''(\theta)|\le C_p(1+d(\theta)^{p-2}).\tag{3}
\]
The constant can depend on \(p\), but not on \(N\). The bound follows by differentiating the defining powers on each quadrant, using \(f_p(\alpha+t)=1+|t|^p/p+O_p(|t|^{2p}+t^2)\) with corresponding derivative bounds, and compactness away from the axes.

**Step 2: Angular conic interpolation reduces to ordinary linear interpolation.** For \(s\in[0,1]\), uniformly in \(s\),
\[
\frac{\sin((1-s)h)}{\sin h}=(1-s)+O(h^2),\qquad
\frac{\sin(sh)}{\sin h}=s+O(h^2).
\]
Because \(f_p\) is bounded, replacing (1) by the ordinary angular chord incurs an error \(O_p(h^2)=o(h^p)\). For a cell near a fixed axis \(\alpha\), whose left endpoint is \(\alpha+uh\) with fixed \(u\), (2) gives uniformly in \(s\)
\[
h^{-p}\,[f_p(\alpha+(u+s)h)-I_{p,N}(\alpha+(u+s)h)]
\longrightarrow\frac1p\big(|u+s|^p-(1-s)|u|^p-s|u+1|^p\big).
\tag{4}
\]
The sign is retained in this formula.

**Step 3: Localization is exhaustive.** If the whole cell is at least \(Kh\) from every axis, the ordinary interpolation remainder and (3) bound its absolute error by
\[
C_p h^2\big(1+(Kh)^{p-2}\big)
\le C'_p(h^2+K^{p-2}h^p).
\tag{5}
\]
For fixed large \(K\) and small \(h\), this is negligible compared with \(h^p\), with coefficient \(O_p(K^{p-2})\). The cells within \(Kh\) of an axis form a bounded number of scaled integer (or half-integer) intervals, to which (4) applies uniformly. Taking first \(N\to\infty\), then \(K\to\infty\), reduces the whole-sphere supremum to the one-dimensional chord-error problem for \(g_p\). This is not an extrapolation from a finite scan of intervals.

**Step 4: Axis-aligned grids.** When \(N\) is even, \(\alpha/h\in\mathbb Z\) for every axis \(\alpha\). Each scaled cell is an integer translate of \([0,1]\). On \([k,k+1]\) for integer \(k\ge0\), concavity gives the nonnegative chord deficit
\[
e_k(s)=(k+s)^p-(1-s)k^p-s(k+1)^p.
\]
For each fixed \(s\), this deficit is nonincreasing as \(k\) increases: differentiation with respect to \(k>0\) gives the Jensen deficit of the *convex* function \(t\mapsto p t^{p-1}\), hence \(\partial_k e_k(s)\le0\). Reflection handles negative integer cells. Thus its largest value occurs on \([0,1]\), where \(e_0(s)=s^p-s\). The unique interior maximizer is \(s_*=p^{1/(1-p)}\), and
\[
\max_{k\in\mathbb Z,\,0\le s\le1}e_k(s)
=\max_{0\le s\le1}(s^p-s)
=(1-p)p^{p/(1-p)}.\tag{6}
\]
Combining (4)--(6) gives the even-grid limit and the stated location and positive sign of the leading error.

**Step 5: Midpoint-straddling grids.** The elementary \(p\)-Hölder inequality
\[
\big||x|^p-|y|^p\big|\le |x-y|^p
\]
implies for every real \(u\) and every \(s\in[0,1]\) that
\[
\begin{aligned}
&\left||u+s|^p-(1-s)|u|^p-s|u+1|^p\right|\\
&\quad\le(1-s)s^p+s(1-s)^p
\le[2s(1-s)]^p\le2^{-p}.
\end{aligned}\tag{7}
\]
The middle inequality is Jensen's inequality for the concave function \(t^p\), with weights \(1-s,s\). Equality in the final bound is realized at \(u=-1/2,s=1/2\): the center is the cusp, with interpolant \(2^{-p}\) and true value zero. When \(N\) is odd, the axes at \(\pi/2\) and \(3\pi/2\) are exactly such cell midpoints. Equation (7), localization, and this witness prove the odd-grid limit and the negative sign of \(f_p-I_{p,N}\).

**Step 6: Strict phase separation.** The universal upper bound in (7) is strict on each aligned integer cell, since equality requires a centered cusp and the aligned cells have their singularities at endpoints. Alternatively (6) and (7) directly imply \((1-p)p^{p/(1-p)}<2^{-p}\). This proves distinct limits.

**Step 7: The endpoint \(p=1\).** Now \(q_1(x,y)=|x|+|y|\) is linear on each quadrant. For even \(N\), every axis lies on the ray grid, hence conic interpolation reproduces \(q_1\) exactly. For odd \(N\), only sectors centered at the axes \(\pi/2\) and \(3\pi/2\) fail to lie inside one quadrant. On such a sector the interpolant is \((1+\tan(h/2))|y|\) in suitable rotated/sign coordinates, while the true function is \(|x|+|y|\). Their absolute difference increases from zero at either endpoint to \(\tan(h/2)\) at the middle axis, establishing the exact claim.

## Verification
A reproducible standalone diagnostic script, `verify_conic.py`, evaluates the conic formula (1) independently on every cell of representative meshes, checks the expected error sign in both parity classes, compares scaled errors with the two analytic limits, checks the exact \(p=1\) endpoint, and checks the interior power-cusp maximum algebraically. It completed 117 finite assertions. These tests sample cell interiors and do not establish a continuum supremum or any infinite-\(N\) limit; Steps 1--7 supply those proofs.

## Relationship to prior work
Unser, arXiv:2611.06212v1 (2026-11-04), constructs exactly the interpolant (1). Appendix B.2, Proposition B.3, proves \(E_{p,N}=\Theta_p(h^p)\) for \(0<p<1\), but does not determine the sharp leading coefficients, a parity distinction, the sign of the dominant error, or the exact \(p=1\) endpoint. Section 5.2 gives the sine-hat representation and addresses bounded-Hessian-variation profiles, an assumption not satisfied by these cusps.

A published mathematical result titled *Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks* (2026-11-08) analyzes a related singular-axis phase phenomenon for convex \(\ell_p\) balls in the **different range \(1<p<2\)**, with Euclidean Hausdorff polygon error rather than the uniform conic-interpolation error of quasi-norms. Its full available result was compared: the exponent range and the geometric quantity differ, so it does not logically imply the formulas here. Both results are manifestations of scalar cusp interpolation, an acknowledged mathematical proximity rather than an independence claim.

Classical work of Schoenberg on trigonometric spline interpolation provides the broader interpolation framework. The present proof does not claim to invent that framework or general Hölder interpolation estimates; it isolates precise constants for the non-Lipschitz quasi-norm test class arising in the recent conic-spline work.

## Limitations
The result holds for each fixed \(0<p<1\) and prescribed **unrotated** uniform polar rays. It does not optimize over rotated or nonuniform grids, establish a uniform bound as \(p\) approaches the endpoints, or extend to higher-dimensional fans. The exact sharp constants are an asymptotic statement, not a finite-mesh equality except at \(p=1\). Earlier general-purpose local cusp interpolation results might supply equivalent estimates and remain a publication-priority risk; no independent originality certification is claimed.

## References
1. M. Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines*, arXiv:2611.06212v1, publicly submitted 2026-11-04, particularly Section 5.2 and Appendix B.2, https://arxiv.org/html/2611.06212v1.
2. *Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks*, published mathematical research record dated 2026-11-08; related range \(1<p<2\) and Hausdorff metric, not an implication for the present theorem.
3. I. J. Schoenberg, *On trigonometric spline interpolation*, Journal of Mathematics and Mechanics 13 (1964), 795--825.
