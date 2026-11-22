# Monotone delay coordinates preserve relay dynamics beyond contraction

## Finding

**Theorem (implicit invisibility by an order condition).** Let \(\rho>0\) and \(t_0\in\mathbb R\). Let \(F:[t_0,\infty)\to\mathbb R\) be bounded and measurable, let \(A:\mathbb R\to\mathbb R\) depend only on \(\operatorname{sign}(u)\), and let \(\Psi:\mathbb R\to\mathbb R\) be continuous with
\[
\operatorname{sign}\Psi(u)=\operatorname{sign}u\qquad(u\in\mathbb R).
\]
Suppose a continuous function \(g:[t_0-2\rho,\infty)\to\mathbb R\), locally absolutely continuous on \([t_0,\infty)\), solves the constant-delay relay equation
\[
 g'(t)=F(t)-A(g(t-\rho))\quad\text{for almost every }t\ge t_0.
\]
Assume that for some \(B<\rho\), \(|\Psi(g(u))|\le B\) for every \(u\ge t_0-2\rho\), and that the *delay-coordinate map*
\[
 H(u)=u+\Psi(g(u))
\]
is strictly increasing on \([t_0-2\rho,\infty)\). Then the implicit-delay equation
\[
 h'(t)=F(t)-A(h(t-\tau(t))),\qquad
 \tau(t)=\rho+\Psi(h(t-\tau(t)))
\]
with the prescribed history \(h=g\) on \([t_0-2\rho,t_0]\) has exactly one solution among pairs consisting of a locally absolutely continuous state and a continuous delay with values in \((0,2\rho)\). It is \(h=g\), with
\[
 d(t)=t-\tau(t)=H^{-1}(t-\rho),\qquad
 \rho-B\le\tau(t)\le\rho+B.
\]
Moreover, for every \(t\ge t_0\),
\[
 \operatorname{sign} g(d(t))=\operatorname{sign}g(t-\rho),
\]
and \(d(t)\) is strictly increasing. The result does **not** assert agreement with finite nested-delay equations.

A simple checkable sufficient condition for the order hypothesis, for linear response \(\Psi(u)=\eta u\) with \(\eta>0\), is the *one-sided slope* bound
\[
 g(v)-g(u)\ge -\frac{q}{\eta}(v-u)
 \quad(t_0-2\rho\le u<v),\qquad 0\le q<1.
\]
There is no upper bound on positive slopes. Thus the theorem applies when \(\eta\operatorname{Lip}(g)\ge1\), outside the two-sided contraction hypothesis of the motivating source.

**Exact separating example.** Take \(\rho=2\), \(\Psi(u)=u\), \(A(u)=\operatorname{sign}u\), \(t_0=0\), and the continuous eight-periodic function \(g\) obtained by periodically extending the following definition over \([-1,7]\):
\[
 g(t)=\begin{cases}
 -1,&-1\le t\le-\tfrac12,\\
 2t,&-\tfrac12\le t\le\tfrac12,\\
 1,&\tfrac12\le t\le\tfrac32,\\
 1-\tfrac12(t-\tfrac32),&\tfrac32\le t\le\tfrac{11}{2},\\
 -1,&\tfrac{11}{2}\le t\le7.
 \end{cases}
\]
Set \(F(t)=g'(t)+\operatorname{sign}g(t-2)\) at points of differentiability and define it arbitrarily at the finitely many corners per period. It is a bounded measurable eight-periodic forcing with \(|F|\le3\). The reference \(g\) satisfies the relay equation, \(|g|\le1<\rho\), the one-sided slope bound with \(q=1/2\), and \(\operatorname{Lip}(g)=2\). Hence the implicit-delay model has globally the unique state \(g\), even though its nested delay iteration can fail: at \(t=9/4\), the delayed-argument iterates \(d_1=t-2\) and \(d_{j+1}=t-2-g(d_j)\) are exactly
\[
 \frac14,\ -\frac14,\ \frac34,\ -\frac34,\ \frac54,\ -\frac34,\ \frac54,\ldots,
\]
whereas the unique implicit argument is \(d_*(9/4)=1/12\). Even nesting orders sample negative values of \(g\) near this time, while the constant and implicit delays sample positive ones; hence \(g\) is not a solution of the even-order nested equations there. The nested iteration eventually forms an exact two-cycle despite the unique implicit solution and its increasing delayed-time coordinate.

## Assumptions and scope

Solutions are interpreted in the usual Carathéodory sense: the state is continuous, locally absolutely continuous forward from \(t_0\), and satisfies the DDE almost everywhere; the delay is continuous, takes values strictly between zero and \(2\rho\), and satisfies the algebraic delay equation at every time. \(A\) is any fixed relay taking possibly different values on the negative, zero, and positive signs; the result does not require \(A\) to be symmetric. The forcing may be merely measurable and bounded. No periodicity or smoothness of the general reference state is assumed beyond the stated hypotheses. The sufficient one-sided slope bound is not claimed to be necessary for an individual reference state; the structural condition is strict monotonicity of \(H\).

## Proof

**1. Unique algebraic delay from the reference state.** For any fixed \(t\ge t_0\), let \(s=t-\rho\). Because \(|\Psi(g)|\le B<\rho\),
\[
 H(t-2\rho)\le t-2\rho+B<s<t-B\le H(t).
\]
Continuity and strict increase of \(H\) give a unique \(d(t)\in(t-2\rho,t)\) satisfying \(H(d(t))=s\). Put \(\tau(t)=t-d(t)\). Then
\[
 \tau(t)=\rho+\Psi(g(d(t))),
\]
so \(\rho-B\le\tau(t)\le\rho+B\) and \(\tau\) is continuous. Since the inverse of a strictly increasing continuous function is strictly increasing, \(d(t)=H^{-1}(t-\rho)\) is strictly increasing.

**2. Exact sign preservation, including zeros.** The identities
\[
 H(d)=s=d+\Psi(g(d)),\qquad H(s)=s+\Psi(g(s))
\]
and strict monotonicity give the three cases. If \(g(s)>0\), then \(H(s)>H(d)\), hence \(s>d\), so \(\Psi(g(d))=s-d>0\) and \(g(d)>0\). If \(g(s)<0\), all inequalities reverse. If \(g(s)=0\), then \(H(s)=s=H(d)\) forces \(d=s\), and both sampled values vanish. Thus the two sampled states have the same sign for every \(t\). Since \(A\) is constant on each sign class, \(g'\) satisfies the implicit-delay equation almost everywhere. This proves global existence of the stated implicit solution.

**3. Uniqueness of the entire trajectory in the specified solution class.** Let \((h,\widehat\tau)\) be any other solution on \([t_0,T]\) for finite \(T>t_0\) with the same history. By continuity and positivity of both delay functions, their minimum on this compact interval is some \(\varepsilon>0\). Suppose \(h=g\) up to a time \(a\ge t_0\). For \(a\le t\le\min(a+\varepsilon/2,T)\), both delayed arguments are strictly less than \(a\). Hence \(h(t-\widehat\tau(t))=g(t-\widehat\tau(t))\), and the algebraic delay equation for \(\widehat\tau\) becomes \(H(t-\widehat\tau(t))=t-\rho\). Strict monotonicity of \(H\) makes that argument exactly \(d(t)\), so the two differential right-hand sides agree almost everywhere. Equality at time \(a\) and integration imply \(h=g\) over this next interval. A finite partition proves equality up to \(T\), and as \(T\) is arbitrary, on the whole common domain. The delay then agrees pointwise by the same uniqueness of the algebraic root. This does not depend on any regularity of an unknown competing state other than the specified solution class.

**4. One-sided quantitative criterion.** For \(\Psi(u)=\eta u\), the asserted lower slope condition yields
\[
 H(v)-H(u)=(v-u)+\eta(g(v)-g(u))\ge(1-q)(v-u)>0.
\]
In particular \(H^{-1}\) is \((1-q)^{-1}\)-Lipschitz on its image. Positive slopes of \(g\) may be arbitrarily large; a two-sided contraction of the nested-delay map is unnecessary for the implicit result.

**5. Periodic separating example.** All five displayed pieces of \(g\) match continuously at their endpoints and under eight-periodic extension. Their slopes belong to \(\{0,2,-1/2\}\), so \(g(v)-g(u)\ge-(v-u)/2\) for all \(u<v\), while \(\sup|g|=1\) and \(\operatorname{Lip}(g)=2\). The constructed \(F\) makes \(g'=F-\operatorname{sign}g(t-2)\) identically at every nonswitching differentiability point. Hence Steps 1–4 apply globally. At \(s=t-2=1/4\), the values \(g(1/4)=1/2\), \(g(-1/4)=-1/2\), \(g(3/4)=g(5/4)=1\), and \(g(-3/4)=-1\) give the stated iteration exactly. The unique implicit root satisfies \(H(d)=1/4\); on \([-1/2,1/2]\), \(H(d)=3d\), so \(d=1/12\). Every even iterate from index two samples a negative state, while \(g(s)>0\). Since all iterates and sampled states depend continuously on \(t\), the sign mismatch persists on an open time interval about \(9/4\); the right-hand sides of the reference and even-nesting equations disagree there, rather than merely at one exceptional time. This proves the asserted separation.

## Verification

The proof is analytic. Run the included standalone `verify.py` with `python3 verify.py` to reproduce the exact-rational periodic continuity and slope data, the first twelve nested delayed-argument iterates, the implicit root, and the sign mismatch at a rational neighborhood of the witness time. The code tests this explicit witness only; the general theorem follows from the order argument in Steps 1–4, not finite testing.

## Relationship to prior work

Bolduc-St-Aubin, Subramanian, and Krauskopf (2026), Theorem 1.1, establish invisibility for **all finite nested delays and the implicit delay together** under a two-sided Lipschitz contraction condition. Their Section 6 explicitly identifies the noncontracting regime as a further direction. The present theorem weakens the regularity requirement for the **implicit branch only** to the order condition on \(H\), proves global trajectory uniqueness and increasing delayed-time order there, and exhibits an exact noncontracting periodic forcing for which nesting cycles and loses sign consistency. Neither the source's all-nesting theorem nor its hypotheses imply this result outside the contraction range.

The published finding *Sharp history-slope threshold for invisible and oscillating nested delays* (2026) constructs a particular clipped history at the two-sided threshold. Its implicit uniqueness is local and example-specific; it does not establish an order condition that guarantees global implicit invisibility for arbitrary bounded reference solutions or a periodic forcing with strictly subcritical downward but supercritical upward slopes. Its nonconvergent nesting example is related and credited, not claimed in isolation as new.

Keane, Krauskopf and Dijkstra (2019) study a smooth ENSO delay model by bifurcation continuation; Humphries, Krauskopf, Ruschel and Sieber (2021/2022) study smooth delayed-state dependence and its bifurcations. These do not supply the relay-specific global order criterion. Walther (2009, Sections 1 and 8) establishes a smooth algebraic-delay semiflow framework and analyzes increasing versus decreasing delayed-time arguments in a white-blood-cell feedback model. Its monotone inverse-coordinate mechanism is relevant background, but its differentiable model does not state exact sign invariance or the globally unchanged state of this nonsmooth relay under a one-sided noncontractive condition. No priority is claimed for inverse-function monotonicity by itself.

## Limitations

The theorem assumes strict monotonicity of a state-dependent delayed-time coordinate along the **given reference solution**, not a global one-sided condition on every possible history. It proves implicit-branch invisibility and uniqueness, not invisibility or convergence for finite nested delays. It does not classify nonmonotone implicit-delay branches, smooth switching functions, or long-time dynamics of the nested counterexample. The periodic example uses a forcing explicitly constructed from a bounded reference trajectory, allowed by the source's measurable-forcing model; its existence does not assert the same behavior for sinusoidal ENSO forcing. A general specialized earlier equivalence in state-dependent-delay literature cannot be excluded by database search alone.

## References

1. S. Bolduc-St-Aubin, P. Subramanian and B. Krauskopf, *Dynamic invisibility of implicit and nested state-dependent delays in a class of externally forced delay equations*, arXiv:2610.39281v1, first publicly submitted 2026-10-29. https://arxiv.org/html/2610.39281
2. *Sharp history-slope threshold for invisible and oscillating nested delays*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-history-slope-threshold-for-invisible-and-oscillating-nest--ef3fbc3fd082
3. A. Keane, B. Krauskopf and H. A. Dijkstra, *The effect of state dependence in a delay differential equation model for the El Niño Southern Oscillation*, Philosophical Transactions A 377 (2019), 20180121. https://pmc.ncbi.nlm.nih.gov/articles/PMC6661334/
4. A. R. Humphries, B. Krauskopf, S. Ruschel and J. Sieber, *Nonlinear effects of instantaneous and delayed state dependence in a delayed feedback loop*, arXiv:2110.01850v1 (2021). https://arxiv.org/abs/2110.01850
5. H.-O. Walther, *On solution manifolds for algebraic-delay systems*, arXiv:2310.12845v1 (2023). https://arxiv.org/abs/2310.12845

6. H.-O. Walther, *Algebraic-Delay Differential Systems, State-Dependent Delay, and Temporal Order of Reactions*, Journal of Dynamics and Differential Equations 21 (2009), 195–232. https://jlupub.ub.uni-giessen.de/server/api/core/bitstreams/5a45d5e6-29f7-4570-814f-a50be0d3619d/content
