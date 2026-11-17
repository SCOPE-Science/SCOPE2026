# Sharp predator-invasion gap on a Ricker two-cycle with an interior coexistence equilibrium

## Finding

For the discrete Kolmogorov predator–prey model of Niu and Wang, a positive coexistence equilibrium can exist at the same parameters as a **hyperbolic attracting predator-free primitive two-cycle**. This is not an assertion of coexistence of two attractors: the interior equilibrium is required only to exist. The overlap has a sharp, explicit parameter interval and a strictly positive first-order width at the prey flip boundary.

Write \(\beta=cb_0\) and \(h(z)=z/(1+\gamma z)\). For \(r>2\), let \(t>0\) be the unique solution of \(r=t\coth(t/2)\), and define \(u=r-t\), \(v=r+t\), \(h_u=h(u)\), \(h_v=h(v)\). The two thresholds are
\[
\beta_{\mathrm{eq}}=\frac{(1-s)(1+\gamma r)}{r},\qquad
\beta_{\mathrm{cyc}}=\frac{-s(h_u+h_v)+\sqrt{s^2(h_u+h_v)^2+4h_uh_v(1-s^2)}}{2h_uh_v}.
\]
For all admissible parameters, \(\beta_{\mathrm{eq}}<\beta_{\mathrm{cyc}}\). The interior equilibrium exists precisely above the first threshold, while predator transverse attraction of the boundary two-cycle holds precisely below the second. If additionally \(|(1-u)(1-v)|<1\), the cycle is a hyperbolic sink for the full planar map on that overlap. Such values of \(r\) form a nonempty interval immediately above \(2\).

For fixed \(s,\gamma\), the threshold gap has the sharp expansion
\[
\beta_{\mathrm{cyc}}-\beta_{\mathrm{eq}}
=\frac{3(1-s)(4\gamma+1-s)}{8(1+2\gamma)}(r-2)+O((r-2)^2).
\]

## Assumptions and scope

Consider the forward map of the nonnegative quadrant
\[
F(x,y)=\left(\frac{xe^{r-x}}{1+cy},\quad sy+\frac{b_0cxy}{(1+\gamma x)(1+cy)}\right),
\]
with \(r>2\), \(s,c\in(0,1)\), and \(b_0,\gamma>0\). Initial states with \(x,y>0\) remain strictly positive at each finite iterate. The assertion concerns the unique *positive, nonconstant* two-cycle on the invariant predator-free axis, its transverse linearization and the existence of an interior equilibrium. It does not assert stability of the interior equilibrium or global predator extinction.

## Proof

**1. Exact prey-only two-cycle.** On \(y=0\), the map reduces to \(f(x)=xe^{r-x}\). If distinct positive \(u<v\) satisfy \(f(u)=v\), \(f(v)=u\), taking logarithms yields \(v-u=2\log(v/u)\) and \(u+v=2r\). Thus with \(t=(v-u)/2>0\),
\[
u=r-t=\frac{2t}{e^t-1},\qquad
v=r+t=\frac{2te^t}{e^t-1},\qquad
r=t\coth(t/2).
\]
The last expression increases strictly from \(2\) to \(+\infty\) because its derivative has the sign of \(\sinh t-t>0\). Conversely these formulas give a valid primitive two-cycle. Uniqueness follows.

**2. Floquet eigenvalues.** At \((x,0)\), \(DF\) is upper triangular with diagonal entries \(e^{r-x}(1-x)\) and \(q(x)=s+\beta h(x)\). The two multipliers of \(DF^2(u,0)\) are
\[
\lambda_x=(1-u)(1-v),\qquad
\lambda_y=q(u)q(v)=s^2+s\beta(h_u+h_v)+\beta^2h_uh_v.
\]
The first equality uses \(e^{r-u}e^{r-v}=1\). Since \(\lambda_y\) is strictly increasing from \(s^2<1\) to infinity as \(\beta>0\) varies, the positive solution of \(\lambda_y=1\) is exactly \(\beta_{\mathrm{cyc}}\). Hence \(\lambda_y<1\) if and only if \(0<\beta<\beta_{\mathrm{cyc}}\). Since \(\lambda_y>0\), this is precisely transverse linear attraction.

**3. Exact fixed-point threshold.** An interior fixed point must have \(0<x<r\) and satisfy
\[
e^{r-x}=\frac{\beta x}{(1-s)(1+\gamma x)},\qquad
y=\frac{e^{r-x}-1}{c}>0.
\]
The left member is strictly decreasing and the right member strictly increasing on \((0,r)\), so a unique solution exists exactly when the right member exceeds \(1\) at \(x=r\). This is the condition \(\beta>\beta_{\mathrm{eq}}\). This independently verifies the source's interior-equilibrium premise.

**4. Strict invasion gap.** The function
\[
\log q(x)=\log(s+(s\gamma+\beta)x)-\log(1+\gamma x)
\]
is strictly concave on \((0,\infty)\) because \((\log q)''=\gamma^2/(1+\gamma x)^2-(s\gamma+\beta)^2/(s+(s\gamma+\beta)x)^2<0\). The strict inequality follows from \(s\gamma+\beta>s\gamma\). Since \(r=(u+v)/2\), we have \(q(u)q(v)<q(r)^2\). At \(\beta=\beta_{\mathrm{eq}}\), \(q(r)=1\), hence \(\lambda_y<1\) there. Its strict monotonicity in \(\beta\) proves \(\beta_{\mathrm{eq}}<\beta_{\mathrm{cyc}}\).

An exact algebraic form of this Jensen defect, valid for \(0<t<r\), is
\[
q(r)^2-q(r-t)q(r+t)=
\frac{\beta t^2[2s\gamma+\beta+2\gamma(s\gamma+\beta)r]}
{(1+\gamma r)^2[(1+\gamma r)^2-\gamma^2t^2]}>0.
\]

**5. Full-map attraction and sharp opening.** When \(|\lambda_x|<1\), both eigenvalues of \(DF^2\) at the cycle have modulus below one for every \(\beta\) in the strict gap. Differentiability and the contraction of a suitable equivalent norm imply local asymptotic stability. The attraction neighborhood intersects the strictly positive quadrant, giving an open set of predator-present initial conditions whose predator population tends to zero. As \(t\downarrow0\), \(r=2+t^2/6+O(t^4)\) and \(\lambda_x=1-2t^2/3+O(t^4)\), ensuring \(|\lambda_x|<1\) for all sufficiently small \(r-2>0\). Expanding the Jensen defect at \(\beta_{\mathrm{eq}}\) and dividing by \(\partial_\beta\lambda_y=s(h_u+h_v)+2\beta h_uh_v\) at \(t=0\) gives
\[
\beta_{\mathrm{cyc}}-\beta_{\mathrm{eq}}
=\frac{3(1-s)(4\gamma+1-s)}{8(1+2\gamma)}(r-2)+O((r-2)^2).
\]
All the displayed coefficients are strictly positive for the stated parameters.

**6. Exact rational Floquet witness.** Let \(L=\log2\) and choose
\[
r=3L,\quad s=c=\tfrac12,\quad \gamma=\frac{1}{2L},\quad b_0=\frac{6}{7L}.
\]
The predator-free cycle is \(u=2L\), \(v=4L\) (verified by multiplication by \(2\) and \(1/2\) respectively). The rare-predator factors are \(q(r)=71/70>1\), \(q(u)=13/14\), and \(q(v)=15/14\), so
\[
\lambda_y=\frac{195}{196}<1,\qquad
\lambda_x=(1-2L)(1-4L)\in(0,1).
\]
The last inclusion follows, for example, from the elementary bounds \(2/3<L<7/10\). The interior equilibrium exists by Step 3, although the unique predator-free cycle is locally attracting from strictly positive states.

## Verification

The self-contained Python standard-library checker `check.py` verifies the exact rational witness, 300 rational instances of the Jensen-defect identity, and several independent parameter checks of the strict threshold gap and its small-amplitude coefficient. It reports `RICKER_BOUNDARY_TWO_CYCLE_CHECK_OK`. These checks test the algebra but are not substitutes for the preceding analytical proof. The hyperbolicity and local-basin statements are proved, not inferred from finite numerical trajectories.

## Relationship to prior work

Niu and Wang introduced and analyzed precisely this map, including the fixed-point existence theorem and flip bifurcations at an **interior** fixed point. Their analysis gives the predator-free **fixed-point** linearization but not a sharp predator-invasion threshold of a predator-free **primitive two-cycle**. Hamada, El-Azab and El-Metwally considered a different Ricker predator-prey update with bilinear predation and without the present rational saturating predator response. Related invasion results for stage-structured predators and other population maps concern different return multipliers and do not imply these parameter thresholds. General strict Jensen concavity motivates the comparison, but neither determines the exact Ricker orbit nor the explicit sharp interval or rational witness without the calculations above.

## Limitations

This theorem is local in state space. It establishes no global basin structure, persistence criterion, interior equilibrium stability, higher-cycle classification, or nonlinear dynamics at either neutral boundary. Near the flip threshold, the overlap is a genuine open parameter region, but its ecological prevalence outside that region is not asserted. Some unindexed or inaccessible literature could contain an equivalent statement; novelty is assessed against the listed inspected material, not certified globally.

## References

1. L. Niu and S. Wang, *Global stability and period-doubling bifurcations of a discrete Kolmogorov predator-prey model with Ricker-type prey growth*, arXiv:2405.11806v1, first publicly posted 2024-05-20. Full-text sections 2–4: https://arxiv.org/html/2405.11806v1 .
2. M. Y. Hamada, T. El-Azab and H. El-Metwally, *Bifurcations and dynamics of a discrete predator–prey model of ricker type*, Journal of Applied Mathematics and Computing 69 (2023), 113–135, DOI:10.1007/s12190-022-01737-8, first journal web publication 2022-04-27. Open-access text: https://link.springer.com/article/10.1007/s12190-022-01737-8 .
