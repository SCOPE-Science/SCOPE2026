# A sharp three-offspring boundary for horizon-dependent lineage extinction rankings

## Finding

Let two independently reproducing, discrete-generation Galton–Watson populations each begin with one ancestor. Let their offspring probability-generating functions be \(f(z)=\sum_{j=0}^3 p_j z^j\) and \(g(z)=\sum_{j=0}^3 q_j z^j\), with nonnegative coefficients summing to one, \(p_0,q_0>0\), and the **same supercritical mean** \(f'(1)=g'(1)=\mu>1\). The probability of extinction by generation \(t\ge0\) is \(F_t=f^{\circ t}(0)\) or \(G_t=g^{\circ t}(0)\), where the superscript denotes composition and \(F_0=G_0=0\).

**Theorem.** (i) If both offspring laws are supported on \(\{0,1,2\}\), the sign of \(F_t-G_t\) never reverses as \(t\) increases. (ii) With support on \(\{0,1,2,3\}\), the sign can reverse at most once, allowing a single equality at the transition. If \(p_0<q_0\), write \(a=p_0-q_0<0\), \(b=p_3-q_3\). A strict reversal from \(F_1<G_1\) to \(F_t>G_t\) at all sufficiently large generations occurs **if and only if**

\[
 b>0,\qquad c=-a/b\in(0,1),\qquad g(c)>c.
\]

If any of these conditions fails, \(F_t<G_t\) for every positive integer \(t\), except that exact equality of the generating functions gives equality throughout. The symmetric criterion applies when \(p_0>q_0\), after exchanging labels. If \(p_0=q_0\), there is no strict ranking reversal.

The maximum possible offspring count \(3\) is sharp. Specifically,
\[
 f(z)=\frac{4+6z+5z^3}{15},\qquad
 g(z)=\frac{5+9z^2+z^3}{15}
\]
have identical offspring mean \(7/5\), and satisfy
\[
 F_1-G_1=-\frac1{15},\qquad
 F_2-G_2=-\frac{77}{3375},\qquad
 F_3-G_3=\frac{5919069959}{3113912109375}>0.
\]
Their extinction ranking changes exactly between generations two and three, and never changes back. Their expected population sizes are identical at every generation, namely \((7/5)^t\).

## Assumptions and scope

The theorem concerns time-homogeneous single-type Galton–Watson processes, one initial ancestor, independent and identically distributed reproductive outcomes for all individuals and generations, and bounded offspring counts. Reproduction replaces the previous generation. The common mean is strictly greater than one, both zero-offspring probabilities are positive, and every coefficient not explicitly listed is zero. Extinction by generation \(t\) means the population size at generation \(t\) is zero; no conditioning on eventual extinction is used. At most one *strict ordering reversal* does not imply that there is necessarily a real-valued time at which the two extinction probabilities agree.

## Proof

**1. Polynomial difference and the sharp support boundary.** Normalization gives \(f(1)-g(1)=0\), and equality of means gives \(f'(1)-g'(1)=0\). Therefore the difference has a double root at one. Writing \(a=p_0-q_0\) and \(b=p_3-q_3\), coefficient comparison yields the exact identity
\[
 f(z)-g(z)=(1-z)^2(a+bz). \tag{1}
\]
If both supports are bounded by two, \(b=0\), and the generating functions are pointwise ordered on \([0,1]\). Their nondecreasing compositions from zero retain that order. If \(a=0\) and \(b\ne0\), the sign is constant for \(z\in(0,1)\), so there is again no reversal. If \(a=b=0\), the functions are identical.

**2. A crossing can happen only once.** After interchanging labels if necessary, assume \(a<0\). If \(b\le0\), or if \(b>0\) and \(-a/b\ge1\), equation (1) gives \(f(z)<g(z)\) for \(0\le z<1\); monotonicity of generating functions proves \(F_t<G_t\) for every \(t\ge1\). The remaining case is \(b>0\) and \(c=-a/b\in(0,1)\). Then \(f<g\) on \([0,c)\) and \(f>g\) on \((c,1)\). Starting at \(F_1<G_1\), whenever \(F_t<G_t\) and \(G_t\le c\),
\[
 F_{t+1}=f(F_t)<f(G_t)\le g(G_t)=G_{t+1},
\]
where strict monotonicity of \(f\) on \((0,1)\) follows from the supercritical positive-offspring hypothesis. Thus the first time \(F_t\ge G_t\), if it exists, must occur with \(G_t>c\). From then on \(F_t\ge G_t>c\) implies
\[
 F_{t+1}=f(F_t)\ge f(G_t)>g(G_t)=G_{t+1}>c,
\]
so every later inequality is strict and has the same direction. At most one strict ranking reversal is possible.

**3. Exact criterion for whether a reversal occurs.** Write \(r_f,r_g\in(0,1)\) for the unique nontrivial fixed points of the supercritical generating functions. Standard convexity of generating functions with a positive zero-offspring mass gives \(F_t\uparrow r_f\), \(G_t\uparrow r_g\), and \(g(z)>z\) for \(0\le z<r_g\), while \(g(z)<z\) for \(r_g<z<1\). Therefore \(g(c)>c\) is equivalent to \(r_g>c\). If \(r_g\le c\), induction in step 2 keeps \(F_t<G_t\) at all finite \(t\). If \(r_g>c\), equation (1) yields
\[
 f(r_g)-r_g=f(r_g)-g(r_g)>0.
\]
The same convex fixed-point property for \(f\) shows \(r_f>r_g\). As the two finite-generation sequences converge to those distinct limits, \(F_t>G_t\) for all sufficiently large \(t\). Step 2 makes this reversal unique. This proves both necessity and sufficiency.

**4. Exact example.** The two displayed laws have zero-offspring masses \(4/15\) and \(5/15\), both have mean \(7/5\), and equation (1) becomes
\[
 f(z)-g(z)=\frac{(1-z)^2(4z-1)}{15}.
\]
The crossing abscissa is \(c=1/4\), with \(g(c)-c=39/320>0\). Three rational compositions starting at zero give the exact differences stated in the finding. They prove the first strict reversal is between generations two and three; step 2 rules out a later reversal. Together with the support-two obstruction, the example proves the sharpness of maximum offspring count three.

## Verification

Execute `python3 check.py` with Python 3.9 or later. The checker uses only the Python standard library and exact rational arithmetic. It verifies normalization, the shared mean, the factorization coefficients, the explicit three-generation comparison, the algebraic threshold \(g(c)>c\), and a bounded additional collection of rational offspring-law comparisons. Its finite checks are diagnostics; the universal theorem is proved in the preceding argument, not extrapolated from computation.

## Relationship to prior work

Sawaya and Klaere (2014) study offspring distributions with the same reproductive mean and bounds on *eventual* extinction via moment and convex orders; their full-text results do not provide the sharp maximum-offspring threshold and one-switch characterization for *finite-generation* rankings proved here. Garcia-Millan, Font-Clos and Corral (arXiv first posted November 11, 2014) derive asymptotic finite-generation survival scaling, not pairwise rank changes. Bürger (2026), Section 4.4, gives an exact switching classification between a cubic generating function and a specially matched fractional-linear bounding function with the **same eventual extinction probability and convergence slope**; that specific comparison does not have two freely chosen, equal-mean cubic offspring laws and does not imply this sharp same-mean, two-versus-three-offspring boundary by statement. The familiar pointwise probability-generating-function comparison order is the underlying monotonicity tool; the present result concerns pairs whose generating functions cross in the unit interval, outside a global pointwise ordering.

## Limitations

The model excludes population density dependence, stochastic environmental switching, overlapping generations, dependence among reproductive outcomes and multitype offspring. An equality of expected population sizes does not mean equal realized growth or comparable extinction risk at every horizon. No claim is made about more than three offspring per individual: generating-function differences may then have multiple interior zeros, and the one-reversal proof does not apply. The classification is a mathematical theorem for this model, not an empirical prediction. Historical originality remains provisional pending independent scholarly review, particularly for older results in branching-process iteration and single-crossing comparative dynamics.

## References

1. S. Sawaya and S. Klaere, *Extinction in a branching process: why some of the fittest strategies cannot guarantee survival*, Journal of Statistical Distributions and Applications **1**, article 10 (2014), first published June 16, 2014. https://doi.org/10.1186/2195-5832-1-10
2. R. Garcia-Millan, F. Font-Clos and A. Corral, *Finite-size scaling of survival probability in branching processes*, arXiv:1411.2817v1, first posted November 11, 2014; Phys. Rev. E **91**, 042122 (2015). https://arxiv.org/html/1411.2817v1
3. R. Bürger, *Bounds for survival probabilities in supercritical Galton-Watson processes and applications to population genetics*, Journal of Mathematical Biology **92**, article 40 (2026), published February 26, 2026, especially Sections 2.2 and 4.4. https://doi.org/10.1007/s00285-026-02349-7
