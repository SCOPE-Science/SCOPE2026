# Optimal timing and a sharp reversal for fixed-budget Friedman–Pólya reinforcement

## Finding

A two-colour urn initially contains \(u,v\) balls, both positive integers. At each step a uniformly drawn ball is returned, followed by one of two balanced reinforcement rules:

- **P** (Pólya): add \(c=a+b\) balls of the drawn colour.
- **F** (Friedman): add \(a\) balls of the drawn colour and \(b\) of the other colour.

Here \(a>b\ge1\) are fixed integers. Fix any horizon \(n\ge2\) and intervention budget \(1\le k\le n-1\): exactly \(k\) of the \(n\) rules must be F, the rest P. The entire rule order is selected in advance independently of the urn draws. Let \(X_n=U_n-V_n\) and \(T_n=U_n+V_n=u+v+nc\).

**Fixed-budget rearrangement theorem.** For every admissible rule string \(\sigma\) containing \(k\) F steps,

\[
\mathbb E_{\mathrm{F}^{k}\mathrm{P}^{n-k}}X_n^2
\le \mathbb E_{\sigma}X_n^2
\le \mathbb E_{\mathrm{P}^{n-k}\mathrm{F}^{k}}X_n^2.
\]

Both inequalities are *strict* unless \(\sigma\) is the corresponding endpoint string. Thus administering all F steps early is the unique minimum-squared-imbalance design, and postponing them to the end is the unique maximum, among all \(\binom nk\) open-loop designs, at every finite horizon and all positive starting compositions. The same endpoints uniquely minimize and maximize \(\mathbb E[(Z_n-1/2)^2]\), with \(Z_n=U_n/T_n\).

The theorem has a **persistent-risk extension**: after completing any of these \(n\)-step schedules, use only P steps forever, and let \(Z_\infty\) denote the almost-sure terminal red fraction. The same two endpoint schedules uniquely minimize/maximize its unconditional squared imbalance, exactly

\[
\mathbb E_\sigma[(Z_\infty-\tfrac12)^2]
=\frac{\mathbb E_\sigma[X_n^2]+cT_n}{4T_n(T_n+c)}.
\]

The positive eigenvalue condition \(a>b\) has a **sharp boundary**. When \(a<b\), the sign of the effect of swapping adjacent P,F depends on the preceding second moment: there is no universal early/late ordering. For example, at \((a,b)=(1,3)\) and two steps, P then F gives a strictly *smaller* final second moment than F then P from starting counts \((5,5)\), but a strictly *larger* one from starting counts \((9,1)\).

## Assumptions and scope

Replacements are additive, balanced and deterministic conditional on the drawn colour. The drawn ball is returned; every draw is uniform among currently present balls. All initial and replacement counts are positive integers. The total reinforcement \(c=a+b\) is identical under both rules. The schedule is fixed before sampling (or may be independently randomized, in which case each risk is a convex combination of deterministic-schedule risks); no feedback-adaptive policy is claimed to be optimized. The unique fixed-budget ordering assertion requires \(a>b\); at \(a=b\) strictness can fail and at \(a<b\) the reversal example applies. Variance of the count difference itself is **not** being optimized; the target is its *uncentered second moment*, equivalent here to squared deviation of the colour proportion from one half.

## Proof

**1. Exact conditional second-moment recurrence.** Put \(d=a-b\), so \(0<d<c\) in the optimization theorem. At a step whose eigenvalue is \(\alpha=c\) for P or \(\alpha=d\) for F, let \(\eta\in\{-1,1\}\) encode the sampled colour. Conditional on the preceding urn, \(\mathbb E[\eta\mid X,T]=X/T\), and \(X'=X+\alpha\eta\). Hence

\[
\mathbb E[(X')^2\mid X,T]
=\left(1+\frac{2\alpha}{T}\right)X^2+\alpha^2.
\]

Writing \(V_i=\mathbb E X_i^2\) and \(T_i=u+v+ic\), one gets the *closed* deterministic recurrence

\[
V_i=\left(1+\frac{2\alpha_i}{T_{i-1}}\right)V_{i-1}+\alpha_i^2,
\qquad V_0=(u-v)^2.
\]

In particular every future factor \(1+2\alpha_i/T_{i-1}\) is strictly positive when \(a>b\).

**2. Exact adjacent-interchange identity.** Compare two schedules with the same preceding \(i-1\) steps and otherwise identical suffix, but with P,F versus F,P in positions \(i,i+1\). Write \(T=T_{i-1}\), \(V=V_{i-1}\). Applying the recurrence twice gives the exact difference immediately after those two steps,

\[
\boxed{V_{i+1}(\mathrm{PF})-V_{i+1}(\mathrm{FP})
=\frac{2(c-d)}{T+c}\left(\frac{cV}{T}+cd\right).}
\]

For \(0<d<c\) and \(V\ge0\) this is strictly positive, independent of starting composition. Every later identical action multiplies the difference by a strictly positive factor. Consequently **every adjacent inversion P,F can be removed by moving F one position earlier and strictly decreases final \(V_n\)**. Repeated adjacent swaps reduce any string other than \(\mathrm{F}^k\mathrm{P}^{n-k}\) to that unique string, proving the minimum. Reversing the swaps proves the unique maximum \(\mathrm{P}^{n-k}\mathrm{F}^k\). Since \(Z_n-1/2=X_n/(2T_n)\) and \(T_n\) is deterministic, the squared-proportion ordering is identical.

For an independently randomized open-loop schedule supported on strings with exactly \(k\) F actions, conditioning on the schedule and averaging preserves the risk bounds. Equality at an endpoint requires unit probability on the unique extremizing string.

**3. Persistent Pólya continuation.** Conditional on the urn at time \(n\), running only P thereafter is the classical two-colour Pólya scheme with reinforcement \(c\). Its terminal red fraction is beta distributed with positive shape parameters \(U_n/c\) and \(V_n/c\), and therefore

\[
\mathbb E[(Z_\infty-\tfrac12)^2\mid U_n,V_n]
=\frac{(U_n-V_n)^2+cT_n}{4T_n(T_n+c)}.
\]

Taking expectations gives the formula in the statement. Its coefficient of \(V_n\) is strictly positive and the remaining term is schedule-independent, transferring both unique extrema to the limiting random fraction. This limit is a genuine non-Gaussian Pólya limit in general; nothing assumes asymptotic normality.

**4. Boundary and reversal.** The adjacent-swap identity itself remains valid for arbitrary \(a,b>0\), with \(d=a-b\). When \(d<0\), its sign is the sign of \(V/T+d\), since \(c-d=2b>0\). In the two-step case there is no suffix. At \(a=1,b=3\), \(c=4\) and \(d=-2\), initially \(T=10\). With starting populations \((5,5)\) one has \(V=0\), so P,F minus F,P is negative. With \((9,1)\), \(V=64\), so it is positive. This proves a strict, explicit failure of every initial-state-independent ordering rule on the opposite-reinforcement side. \(\square\)

## Verification

Execute `python3 check.py` using Python 3 standard library. Its independent exact-rational urn-state enumeration compares all two-colour draw histories with the second-moment recurrence across all rule strings through five steps in several positive integer starting states and reinforcement choices. It also checks the two-action identity with prefixes/suffixes, the complete fixed-budget optimum in the positive-eigenvalue range, the Pólya-continuation risk invariant, and both sides of the negative-eigenvalue reversal. It passed **12,517 exact-rational assertions**. These exhaustive *finite examples* test algebra only; the all-size theorem is proved by the recurrence and adjacent exchange, not by enumeration.

## Relationship to prior work

Shi, Yin and Miao (first public version May 26, 2026) study Gaussian fluctuations for the Pólya–Friedman urn when the reinforcement type is independently sampled with a fixed probability at every step. Alves and Rosales (2025) study its convergence under fixed mixing. Neither supplies an extremal theorem over all *deterministic* fixed-budget rule sequences or a persistent-risk comparison after Pólya continuation. The published quenched harmonic-frequency theorem for arbitrary fixed rule sequences establishes **infinite-horizon convergence versus nondegeneracy** under a weighted intervention criterion; its statement does not compare finite-horizon second moments, optimize the allocation of a fixed number of actions, or give the strict exchange sign and opposite-eigenvalue reversal. Classical balanced-urn moment recurrences and Pólya beta limits are used as known tools; no priority is claimed for them. Other general moment papers concern bounds or limiting moments for fixed replacement mechanisms and do not, as inspected, state this fixed-budget schedule extremum.

## Limitations

The theorem addresses nonadaptive open-loop timing of a fixed intervention budget and squared deviation from colour balance, not every convex risk, the variance around the (schedule-dependent) mean, or feedback-optimal control. No distributional stochastic-order theorem is asserted. The exact interchange formula is general for both signs of \(d\), but the strong universal sorting theorem is restricted to \(d>0\); a complete dynamic optimum for \(d\le0\) is not supplied. A broad, unindexed intervention-scheduling theorem might imply this special case; inspected literature cannot prove universal priority. Finite verification does not replace analytical proof. Independent assessment has not occurred.

## References

1. J. Shi, Q. Yin and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model*, arXiv:2605.26669v1, first posted 2026-05-26, https://arxiv.org/html/2605.26669v1.
2. R. Alves and R. A. Rosales, *Friedman vs Pólya*, arXiv:2502.16768v1, first posted 2025-02-24, https://arxiv.org/html/2502.16768v1.
3. S. Janson, *Moments of Balanced Pólya Urns*, *Journal of Theoretical Probability* (2025), https://doi.org/10.1007/s10959-025-01447-4.
4. S. Janson, *Mean and variance of balanced Pólya urns*, *Advances in Applied Probability* **52** (2020), 1224–1248, https://doi.org/10.1017/apr.2020.38.
5. *A quenched harmonic threshold for vanishing Friedman reinforcement*, public mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-quenched-harmonic-threshold-for-vanishing-friedman-reinforceme--a851c23e380a.
