# Sharp angular-knot law for quasi-triangle moduli of sampled planar \(\ell_p\) conic splines

## Finding
Let \(0<p<1\). Interpolate the planar quasi-norm
\[
q_p(x_1,x_2)=(|x_1|^p+|x_2|^p)^{1/p}
\]
by a continuous conic spline \(Q_{\mathcal F,p}\) on any finite complete centrally symmetric planar fan \(\mathcal F\) containing the four coordinate-axis rays. On each two-dimensional cone, the spline is linear, and on every generating ray it agrees with \(q_p\).

Write \(\Theta_{\mathcal F}\) for the angles of all generating rays and
\[
\delta_{\mathcal F}=\min_{\theta\in\Theta_{\mathcal F}}\min_{k\in\mathbb Z}
\big|\theta-\tfrac\pi4-k\tfrac\pi2\big|\in[0,\pi/4].
\]
The optimal quasi-triangle constant, defined with an infimum over constants valid for every pair in the plane, is exactly
\[
\begin{split}
C(Q_{\mathcal F,p})
&=\sup_{x,y\ne0}\frac{Q_{\mathcal F,p}(x+y)}{Q_{\mathcal F,p}(x)+Q_{\mathcal F,p}(y)}\\
&=F_p(\delta_{\mathcal F}),\\
F_p(\delta)
&=\frac{\big[\cos^p(\pi/4-\delta)+\sin^p(\pi/4-\delta)\big]^{1/p}}
{\cos(\pi/4-\delta)+\sin(\pi/4-\delta)}.
\end{split}
\]
This function decreases strictly from \(F_p(0)=2^{1/p-1}\) to \(F_p(\pi/4)=1\). Thus the sampled conic spline preserves the sharp modulus of its \(\ell_p\) target **if and only if** one sampled ray has \(|x_1|=|x_2|>0\). When a fan approaches such a ray, the exact deficit has the universal sharp expansion
\[
2^{1/p-1}-C(Q_{\mathcal F,p})
=2^{1/p-1}\frac{1-p}{2}\,\delta_{\mathcal F}^{2}+O_p(\delta_{\mathcal F}^{4}).
\]
The formula depends only on the nearest ray to a coordinate diagonal, independently of the number, spacing, or placement of all other rays.

## Assumptions and scope
A finite complete planar fan is a cyclic collection of nonzero rays with successive opening angles strictly below \(\pi\), covering the whole plane; the cones are the positive spans of consecutive rays. Central symmetry means antipodal rays occur in pairs. The four rays \((\pm1,0)\) and \((0,\pm1)\) must belong to the fan. The spline is the unique continuous positively homogeneous function which is linear on each closed cone and has the specified nodal values. All statements concern real \(\mathbb R^2\), not arbitrary higher-dimensional triangulations. The exponent satisfies \(0<p<1\). The quasi-triangle constant here is the **smallest** \(C\ge1\) satisfying \(Q(x+y)\le C[Q(x)+Q(y)]\) for all \(x,y\in\mathbb R^2\).

## Proof
**1. Axis-aligned interpolation comparison.** Every cone lies within one closed coordinate quadrant because the axis rays themselves occur as knots. Within such a cone, \(\|x\|_1=|x_1|+|x_2|\) is linear. Since \(0<p<1\), the sampled values satisfy \(q_p(r)\ge\|r\|_1\) for every ray \(r\). Let
\[
M=\max_{r\in\mathcal F^{(1)}}\frac{q_p(r)}{\|r\|_1}.
\]
The two generating rays of a cone are a nonnegative linear basis for that cone. Interpolating the two nodal inequalities by nonnegative coefficients yields, for **every** \(x\in\mathbb R^2\),
\[
\|x\|_1\le Q_{\mathcal F,p}(x)\le M\|x\|_1.
\]
In particular \(Q\) is positive definite, continuous and absolutely homogeneous (the opposite nodal values agree), hence is a quasi-norm. The \(\ell_1\) triangle inequality implies
\[
Q_{\mathcal F,p}(x+y)\le M(\|x\|_1+\|y\|_1)
\le M(Q_{\mathcal F,p}(x)+Q_{\mathcal F,p}(y)).
\]

**2. Exact attainment.** Choose a sampled ray \(r=(a,b)\) maximizing the nodal ratio. Set \(x=(a,0)\), \(y=(0,b)\). At the axis knots and their scalar multiples, \(Q(x)=|a|\) and \(Q(y)=|b|\), while the interpolation condition gives \(Q(x+y)=q_p(r)\). Thus the quotient equals \(M\), proving \(C(Q)=M\), including the axis-only fan (where \(M=1\)). Note that the upper bound in Step 1 alone would not prove optimality; this axis decomposition does.

**3. Maximizing angle.** By invariance under sign changes and coordinate interchange, the nodal quotient depends only on \(t=\min(|a|,|b|)/\max(|a|,|b|)\in[0,1]\), and is
\[
R_p(t)=\frac{(1+t^p)^{1/p}}{1+t}.
\]
For \(0<t<1\),
\[
\frac{d}{dt}\log R_p(t)
=\frac{t^{p-1}-1}{(1+t^p)(1+t)}>0.
\]
The maximum therefore comes from a ray nearest a diagonal modulo a quarter-turn, giving the stated function \(F_p(\delta_{\mathcal F})\) and exact criterion for retaining \(2^{1/p-1}\).

**4. Sharp angular defect.** Put \(\theta=\pi/4-\delta\), and let \(G(\delta)=\log F_p(\delta)\). Direct differentiation of
\[
G(\delta)=p^{-1}\log(\cos^p\theta+\sin^p\theta)
-\log(\cos\theta+\sin\theta)
\]
gives \(G(0)=(1/p-1)\log2\), \(G'(0)=0\) and \(G''(0)=p-1\). Symmetry \(G(-\delta)=G(\delta)\) makes all odd Taylor coefficients vanish near zero. Smoothness there implies
\[
F_p(\delta)=2^{1/p-1}\big[1-(1-p)\delta^2/2+O_p(\delta^4)\big],
\]
with a strictly positive quadratic coefficient for the defect. This is an equality asymptotic, not merely a rate bound.

## Verification
The included standalone `CHECK.py` uses standard-library arithmetic to exercise nonuniform centrally symmetric fans, boundary rays, optimizer witnesses, the global quasi-triangle inequality on sampled pairs, the nodal upper/lower comparisons, an exact rational diagonal case, and the quadratic defect. It reports `CONIC_SPLINE_MODULUS_CHECK_OK 12722`. This is supplementary finite evidence; Steps 1–4 are the proof for every admissible fan and exponent. The proof and checker require no external data files.

## Relationship to prior work
Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines* (2026), provides the general class of conic-spline quasi-norms, the trigonometric nodal interpolation formula and sharp approximation rates; these are credited and not claimed as new. The classical \(\ell_p\) sharp quasi-triangle factor is also established mathematics. Qadri and Mehmood (2018) discuss geometric constants of quasi-Banach spaces and the modulus of concavity. The present claim singles out the **optimal constant of the interpolant**, its exact dependence on the nearest sampled diagonal, and the sharp quadratic loss for arbitrary nonuniform axis-aligned fans; these are different questions from approximation error of the radial profile or bounds for a general quasi-norm.

## Limitations
The result assumes all four coordinate axes are knots; without this restriction the global comparison with \(\ell_1\) and the equality witness need not hold. It does not classify arbitrary positive conic splines, higher-dimensional fans or sampling schemes without the axis rays. The quadratic expansion is for fixed \(p\) and \(\delta_{\mathcal F}\to0\), not a bound uniform as \(p\to0\). Exact novelty relative to inaccessible or unindexed older literature cannot be guaranteed from literature searches alone; no independent mathematical validation is claimed.

## References
1. Michael Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines*, arXiv:2611.06212v1, submitted 4 November 2026. https://arxiv.org/abs/2611.06212 . Relevant: Section 2 and Section 5 (conic interpolation and planar nodal representation), Appendix B (classical \(\ell_p\) comparison).
2. Hussain Minhaj Uddin Ahmad Qadri and Qaisar Mehmood, *On Moduli and Constants of quasi-Banach Spaces*, Open Journal of Mathematical Sciences 2 (2018), 122–133, https://doi.org/10.30538/oms2018.0022 . Relevant: Section 2 (definition of the quasi-triangle concavity modulus).
