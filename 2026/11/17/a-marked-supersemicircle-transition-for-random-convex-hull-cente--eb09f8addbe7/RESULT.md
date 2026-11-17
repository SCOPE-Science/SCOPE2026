# A marked supersemicircle transition for random convex-hull center clearance

## Finding

Let \(n\ge3\) independent points have angular coordinates uniform on the same oriented unit-circle arc \([0,L]\), \(0<L\le2\pi\). Let \(H_n\) be their Euclidean convex hull, and define the center clearance \(D_n\) to be the distance from the origin to \(\partial H_n\) if the origin belongs to the interior of \(H_n\), and zero otherwise. Write \(U_{(1)}\) and \(U_{(n)}\) for the smallest and largest sampled angles.

**Fixed-sample opening.** Fix \(n\ge3\), and write \(L=\pi+\delta\) with \(\delta\downarrow0\). Conditional on \(0\in\operatorname{int}H_n\), the pair
\[
\left(\frac{U_{(1)}}{\delta},\frac{L-U_{(n)}}{\delta}\right)
\]
converges **in total variation** to the probability density \(2\) on \(\{(x,y):x\ge0,\ y\ge0,\ x+y<1\}\). Moreover the hull edge joining the two angular extremes is the unique closest boundary edge to the origin with conditional probability tending to one, and jointly
\[
\frac{2D_n}{\delta}\ \Longrightarrow\ 1-X-Y\sim\operatorname{Beta}(1,2).
\]
Thus the three normalized proportions \((X,Y,1-X-Y)\) have the \(\operatorname{Dirichlet}(1,1,1)\) law.

**Critical-many-point opening.** Fix \(c>0\), let \(L_n=\pi(1+c/n)\), and write \(A_n=nU_{(1)}/L_n\), \(B_n=n(L_n-U_{(n)})/L_n\). Conditional on \(0\in\operatorname{int}H_n\), \((A_n,B_n)\) converges **in total variation** to two independent unit exponentials \((E_1,E_2)\) conditioned on \(E_1+E_2<c\). On the inclusion event the extreme-pair chord is the unique closest facet with probability tending to one. Unconditionally,
\[
\frac{nD_n}{\pi}\Longrightarrow Z_c:=\frac{(c-E_1-E_2)_+}{2}.
\]
This law has an atom \((1+c)e^{-c}\) at zero and density \(2(c-2z)e^{-(c-2z)}\) for \(0<z<c/2\). The limiting center-inclusion probability is \(1-(1+c)e^{-c}\).

For reference, the exact scalar probability is, with \(a=\pi/L\),
\[
p_n(L)=\begin{cases}0,&0<L\le\pi,\1-na^{n-1}+(n-1)a^n-(n-1)(1-a)^n,&\pi<L\le2\pi.\end{cases}
\]
The scalar formula is background normalization and is **not** claimed as a new general coverage theorem.

## Assumptions and scope

Every sample is independent and uniform by angle, equivalently by arclength, on a **single connected arc of a round circle**. Angles are in radians and the geometric circle has radius one. Endpoints have probability zero. The fixed-\(n\) and growing-\(n\) limits are distinct regimes; \(c\) is fixed and strictly positive in the second limit. A tangent or boundary-contact event has probability zero.

## Proof

**1. Exact gap reduction.** Sort the angular variables and put \(u=U_{(1)}\), \(v=L-U_{(n)}\). The \(n\) circular gaps are the \(n-1\) adjacent internal gaps and the exterior gap of size \(2\pi-L+u+v\). Strict origin inclusion is equivalent to every circular gap being less than \(\pi\). Thus it requires \(u+v<\delta=L-\pi\) and all internal gaps smaller than \(\pi\). If \(\delta\le0\), inclusion is impossible. The \(n+1\) spacings, including \(u,v\), are uniformly Dirichlet after division by \(L\). The event \(u+v<\delta\) is exactly the event that the sample range exceeds \(\pi\), with probability \(1-na^{n-1}+(n-1)a^n\). An internal gap can reach \(\pi\) with probability \((1-a)^n\), and at most one internal gap can do so for \(L\le2\pi\). Such an event has range exceeding \(\pi\). Subtracting the \(n-1\) disjoint internal-gap events proves the scalar formula.

**2. Endpoint density and the first marked limit.** On \(u,v\ge0\) and \(u+v\le L\), the exact joint density of the extreme endpoint slacks is
\[
h_{n,L}(u,v)=\frac{n(n-1)(L-u-v)^{n-2}}{L^n}.
\]
After substituting \(u=\delta x\), \(v=\delta y\), its density on \(x+y<1\), normalized by the inclusion probability, tends pointwise to \(2\). The probability of an internal gap at least \(\pi\) is at most \((n-1)(\delta/L)^n\), whereas the probability \(u+v<\delta\) is asymptotic to \(n(n-1)\delta^2/(2\pi^2)\). The excluded fraction tends to zero for every \(n\ge3\), and Scheffé's lemma yields conditional total-variation convergence to the uniform triangle. The two-point chord joining the extremes has distance \(\sin((\delta-u-v)/2)\) from the origin. Given inclusion, the other edges are internal consecutive-point chords, each at distance \(\cos(g_j/2)\), where \(g_j\) is the associated internal angular gap. Given the limiting uniformly distributed interior points of \((0,\pi)\), their maximum internal gap is strictly below \(\pi\) almost surely. Consequently their distances stay bounded away from zero in probability, while the extreme chord's distance is at most \(\delta/2\). This establishes uniqueness with probability tending to one. The continuous mapping theorem gives \(2D_n/\delta\Rightarrow1-X-Y\), whose density is \(2(1-z)\) on \(0<z<1\). Joint convergence of the first two marks is in total variation; the deterministic distance mark converges jointly weakly (a total-variation claim for the three-vector is **not** made, since the finite-threshold distance is a different deterministic function of the first two marks).

**3. Growing-sample endpoint limit.** Write \(u=L_na/n\) and \(v=L_nb/n\). Their joint density becomes
\[
g_n(a,b)=\frac{n-1}{n}\left(1-\frac{a+b}{n}\right)^{n-2},\quad a,b\ge0,\ a+b\le n.
\]
It converges pointwise and in \(L^1\) to \(e^{-a-b}\), the density of independent unit exponentials. The exterior gap is less than \(\pi\) precisely when \(a+b< cn/(n+c)\), and the chance of an internal gap exceeding \(\pi\) is at most \((n-1)(c/(n+c))^n\), which tends to zero. Restricting \(g_n\) to the moving triangle, dividing by its mass and using Scheffé's lemma gives conditional total variation on the endpoint marks. Its normalization converges to
\[
\Pr(E_1+E_2<c)=\int_0^c se^{-s}\,ds=1-(1+c)e^{-c}.
\]
For the internal gaps, \(\Pr(\max_jg_j>\pi/2)\le(n-1)(1-\pi/(2L_n))^n\to0\). Thus internal chord distances approach one uniformly in the sense needed, while the extreme chord distance is at most \(\pi c/(2n)\), proving the closest-facet assertion. On inclusion,
\[
\frac{nD_n}{\pi}=\frac{n}{\pi}\sin\left(\frac{\pi}{2n}\left(c-\frac{n+c}{n}(A_n+B_n)\right)\right),
\]
for all sufficiently large \(n\) outside an event of vanishing probability. This converges in distribution to \((c-E_1-E_2)/2\) on the event \(E_1+E_2<c\), and setting zero on its complement proves the unconditional law. Transforming the gamma density \(se^{-s}\) by \(z=(c-s)/2\) gives the stated density and atom. No Gaussian or independence approximation for the complete vertex configuration is assumed.

## Verification

The standalone `checks/arc_center_clearance.py` checks the exact gap formula against a deterministic numerical integration of the two extreme-order-statistic density (and the subtraction of the internal-gap events); it also checks the special full-circle Wendel value and the fixed-\(c\) critical limit at growing sample sizes. Randomized simulations, using a documented fixed seed, test the inclusion criterion based on **all** circular gaps against exact probabilities within conservative standard-error bounds. These checks are finite numerical corroboration only; the proof above establishes the infinite statements.

## Relationship to prior work

Wendel's 1962 theorem gives \(p_n(2\pi)=1-n/2^{n-1}\) for the full uniform circle under centrally symmetric sampling. Jewell and Romano (1982) provide general planar convex-hull inclusion and circular-coverage formulas under arbitrary placement distributions, so the scalar inclusion probability and likely scalar center-clearance distributions must not be promoted as independent novelty. The present claimed contribution is solely the **joint conditional endpoint geometry at the sharp opening and in the finite-size critical window**, including identification of the nearest hull facet and the beta–Dirichlet versus truncated-exponential regimes. Bárány–Hug–Reitzner–Schneider (2015) analyze a different spherical-halfspace random-polytope regime. Their sampled domain and observables do not yield the conditional endpoint marks above. A general inclusion formula does not by itself specify which extreme vertices witness the rare inclusion or their joint conditional distribution.

## Limitations

The result uses a connected arc, uniform angular sampling and fixed \(c\) (rather than an arbitrary moving-window profile). The critical limit is weak for center clearance and total variation only for the two-dimensional endpoint marks; the joint triple consisting of marks and clearance is weak, not claimed to converge in total variation. The general coverage results of Jewell and Romano have not been fully inspected owing to unavailable full text; their explicit formula may provide alternative derivations of scalar parts, and historical priority of any marked specialization requires further scrutiny. No independent mathematical audit has been performed.

## References

1. J. G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* **11** (1962), 109–112, https://doi.org/10.7146/math.scand.a-10655 (full text examined).
2. N. P. Jewell and J. P. Romano, “Coverage Problems and Random Convex Hulls,” *Journal of Applied Probability* **19** (1982), 546–561, https://doi.org/10.2307/3213513 (abstract and publication details examined; full text unavailable).
3. I. Bárány, D. Hug, M. Reitzner and R. Schneider, “Random Points in Halfspheres,” arXiv:1505.04672, first public version 18 May 2015, https://arxiv.org/abs/1505.04672 (introduction, setup and main theorem examined).
