# Sharp binary step-reinforcement mixing via an inverse beta integral

## Finding

Let \(0<\alpha<1\). On the two-element additive group \(\mathbb Z/2\mathbb Z\), start at zero and generate steps \(X_1,X_2,\ldots\) as follows: \(X_1\) is fair Bernoulli, and for each \(n\ge2\), independently of earlier random choices, with probability \(\alpha\) set \(X_n=X_J\) for uniformly sampled \(J\in\{1,\ldots,n-1\}\), while with probability \(1-\alpha\) sample a fresh fair Bernoulli step. Let \(S_n=\sum_{j=1}^n X_j\pmod2\), and let \(d_n\) denote total-variation distance between its distribution and the uniform law on the group.

Put
\[
 h=\frac{1+\alpha}{2\alpha},\qquad
 R_\alpha=\frac{1}{\alpha}\int_0^1(1-u^2)^{h-1}\,du
 =\frac{\sqrt\pi\,\Gamma(h)}{2\alpha\,\Gamma(h+1/2)},\qquad
 \delta_\alpha=\frac1h=\frac{2\alpha}{1+\alpha}.
\]
Then \(R_\alpha>1\). For every odd \(n\ge1\), \(d_n=0\) **exactly**; for even \(n\to\infty\),
\[
 \boxed{\displaystyle d_n=\frac{R_\alpha^{-n}}{1+\alpha}
 \left(1+O_\alpha(n^{-\delta_\alpha})\right).}
\]
In particular \(\lim_{m\to\infty}d_{2m}^{1/(2m)}=R_\alpha^{-1}\). At the critical elephant-walk memory parameter corresponding to \(\alpha=1/2\), \(R_{1/2}=\pi/2\) and \(d_{2m}\sim\frac23(2/\pi)^{2m}\).

There is also an **exact finite-time generating function**. Set \(f_n=2\Pr(S_n=0)-1\). Then
\[
 \sum_{n\ge1}f_n z^{n-1}
 =\frac{v(z)}{(1-v(z)^2)^h},\qquad
 z=\frac1\alpha\int_0^{v(z)}(1-u^2)^{h-1}\,du,
\]
where \(v(0)=0\) selects the unique analytic local inverse. In particular \(f_2=\alpha\) and \(f_4=\alpha^2(\alpha+2)/3\), while every odd-indexed \(f_n\) vanishes. Thus the return excess at every even time is strictly positive.

## Assumptions and scope

The reinforcement probability is a fixed real number \(\alpha\in(0,1)\), not a size-dependent sequence. New steps are independent and exactly fair on \(\{0,1\}\); reinforcement selects uniformly from all earlier steps. The initial position is the identity. Limits take even integers \(n\) to infinity at fixed \(\alpha\). No claim concerns mixing trajectories conditioned on the entire step history, other finite groups, or the joint limit \(\alpha\to1\).

## Proof

**1. A Markov-count and branching representation.** The number \(K_n=\sum_{j=1}^nX_j\) of one-steps has transition probability
\[
 \Pr(K_{n+1}=K_n+1\mid K_n=k)
 =\frac{1-\alpha}{2}+\frac{\alpha k}{n}.
\]
Embed these draws in a continuous-time pure-birth population initialized with one fair type, where every existing individual gives birth at rate one and its child copies the parent's type with probability \(\alpha\), otherwise obtaining a fresh fair type. At each birth, the parent is uniform among existing individuals, so the successive types reproduce the discrete step sequence. The population count \(N(t)\) is a standard Yule process with \(\Pr(N(t)=n)=e^{-t}(1-e^{-t})^{n-1}\), independent of the discrete sequence of types.

For complex \(w\) near zero, let \(u_0(t;w)\) and \(u_1(t;w)\) be the expected product of all current type-weights, given respectively one initial zero or one initial one, with weights \(w\) for zero and \(-w\) for one. Branching independence gives
\[
 \dot u_0=u_0\left(\frac{1+\alpha}{2}u_0+\frac{1-\alpha}{2}u_1-1\right),\quad
 \dot u_1=u_1\left(\frac{1+\alpha}{2}u_1+\frac{1-\alpha}{2}u_0-1\right).
\]
Put \(s=(u_0+u_1)/2\) and \(d=(u_0-u_1)/2\). The initial data are \(s(0)=0\), \(d(0)=w\), and the equations simplify to
\[
 \dot s=s^2+\alpha d^2-s,\qquad
 \dot d=(1+\alpha)sd-d.
\]
Writing \(r=1-e^{-t}\), \(s=e^{-t}w A(wr)\), \(d=e^{-t}w B(wr)\) yields
\[
 A'=A^2+\alpha B^2,\qquad B'=(1+\alpha)AB,\qquad A(0)=0,\ B(0)=1.
\]
On the other hand, conditioning on \(N(t)\) gives
\[
 s(t;w)=e^{-t}\sum_{n\ge1}(1-e^{-t})^{n-1}w^n f_n.
\]
Comparing powers proves \(A(z)=\sum_{n\ge1}f_nz^{n-1}\) without any asymptotic approximation.

**2. Exact integration.** Set \(v=A/B\). Direct differentiation gives \(v'=\alpha B(1-v^2)\), and division of the differential equation for \(B\) by that for \(v\) gives
\[
 \frac{d\log B}{dv}=\frac{(1+\alpha)v}{\alpha(1-v^2)}.
\]
Using \(B(0)=1\) produces \(B=(1-v^2)^{-h}\), hence \(A=v(1-v^2)^{-h}\) and
\[
 v'=\alpha(1-v^2)^{-(h-1)}.
\]
Integration with \(v(0)=0\) proves the stated inverse-integral generating function. Symmetry under interchange of zeros and ones shows \(f_n=0\) for odd \(n\). The differential equations, or the percolated recursive-forest representation, show \(f_n>0\) for every even \(n\).

**3. Singularities and exact coefficient constant.** Since \(h-1>0\), the power series of \((1-v^2)^{-(h-1)}\) has strictly positive even coefficients. Iterating \(v'=\alpha(1-v^2)^{-(h-1)}\) shows that the analytic inverse \(v(z)\) has positive coefficients for every odd power and no even powers. Along the real interval, \(v\) increases from zero to one at \(z=R_\alpha\). Consequently its Taylor series converges absolutely on \(|z|=R_\alpha\) with total absolute coefficient sum one. At each point of this circle other than \(\pm R_\alpha\), the triangle inequality is strict because both the coefficients of \(z\) and \(z^3\) are positive. Hence \(|v(z)|<1\) there. The analytic differential equation therefore continues \(v\), and consequently \(A\), through every such point; the only dominant singularities are \(\pm R_\alpha\).

As \(v\to1\), writing \(h=(1+\alpha)/(2\alpha)\),
\[
 R_\alpha-z
 =\frac{2^{h-1}}{\alpha h}(1-v)^h\bigl(1+O(1-v)\bigr).
\]
It follows in a dented complex neighborhood of \(R_\alpha\) that
\[
 A(z)=\frac1{(1+\alpha)(R_\alpha-z)}
 \left[1+O\left((1-z/R_\alpha)^{1/h}\right)\right].
\]
The same expansion holds at \(-R_\alpha\) with opposite parity. Cauchy coefficient extraction on a circle deformed around these two isolated algebraic singularities (equivalently the standard algebraic-singularity transfer estimate) gives, for even \(n\),
\[
 f_n=\frac{2}{1+\alpha}R_\alpha^{-n}
 \left[1+O_\alpha(n^{-1/h})\right].
\]
Indeed, the two simple-pole contributions add for the \(z^{n-1}\) coefficient when \(n\) is even, and the remainder of local order \((R_\alpha-z)^{-1+1/h}\) contributes \(O(R_\alpha^{-n}n^{-1/h})\). Since \(\Pr(S_n=0)=(1+f_n)/2\) and there are two group states, \(d_n=|f_n|/2\); this proves the result.

Finally, \(R_\alpha>1\): since \(h>1\), \(1-u^2>1-u\) on \((0,1)\), so
\[
 R_\alpha=\frac1\alpha\int_0^1(1-u^2)^{h-1}\,du
 >\frac1{\alpha h}=\frac2{1+\alpha}>1.
\]

## Verification

A standalone Python script `check.py` reconstructs the exact distribution of \(K_n\) from its one-step transition rule and independently computes the two analytic-series coefficients from the coupled differential equations, using rational arithmetic. It checks multiple positive rational reinforcement parameters up to \(n=34\), checks the first two nonzero coefficients, and compares long-series numerical ratios against the proved asymptotic. Its recorded run produced 683 exact assertions and three monotone-ratio numerical diagnostics. These finite checks validate implementation identities but are not proofs of analytic continuation or infinite-horizon asymptotics.

Run from this directory with `python check.py` using Python 3 standard libraries only.

## Relationship to prior work

Peres and Qin (2026, arXiv:2604.07207, initial submission April 8) established exponential convergence of step-reinforced walks on finite groups and gave the two-state example \(\Pr(S_2=0)=(1+\alpha)/2\). Their paper does not state the sharp all-parameter binary exponential base, leading constant, or inverse-beta ordinary generating function derived here. Guérin, Laulin and Raschel (2024, arXiv:2401.04959) developed the elephant characteristic polynomials and their root properties; in the fair binary model the even-time discrepancy corresponds to evaluating one such polynomial at zero. That recurrence underlies the present calculation but does not by itself give the claimed singularity constant. Murahara and Tokumitsu (2026, arXiv:2610.35019) prove global exponential Fourier bounds for the elephant walk and sharp central/local Gaussian approximations, not the exact single-frequency exponential asymptotic here. Gut and Stadtmüller's *Bernoulli Elephant Random Walks* (2026) uses a different update: it copies a historical zero-one value or introduces zero, not an independent fair value. Peres and Qin’s companion preprint on transition probabilities (arXiv:2604.07227) advertises general upper bounds; only its abstract was accessible, so stronger full-text coverage cannot be excluded. A related independently indexed near-total-reinforcement result concerns \(n(1-\alpha_n)\to\lambda\), which does not subsume the fixed-\(\alpha\) regime.

## Limitations

The generating function is implicit, not a finite elementary expression at arbitrary reinforcement; the asymptotic error is pointwise in fixed \(\alpha\), not uniform up to its endpoints. This result does not establish historical uniqueness: a broader, unlocated theorem on elephant-polynomial coefficient singularities might imply the claim. The full manuscript of the potentially relevant companion transition-probability preprint was inaccessible; possible broader coverage is an originality limitation. The argument is a mathematical proof with finite diagnostics, not an independently audited certificate.

## References

1. Y. Peres and S. Qin, *Mixing times of step-reinforced random walks*, arXiv:2604.07207 (first submitted 2026-04-08), https://arxiv.org/abs/2604.07207.
2. H. Guérin, L. Laulin and K. Raschel, *Elephant polynomials*, arXiv:2401.04959 (first submitted 2024-01-10), https://arxiv.org/abs/2401.04959.
3. H. Murahara and G. Tokumitsu, *Optimal Rates in Local and Central Limit Theorems for the Elephant Random Walk*, arXiv:2610.35019 (first submitted 2026-10-26), https://arxiv.org/abs/2610.35019.
4. A. Gut and U. Stadtmüller, *Bernoulli Elephant Random Walks*, Journal of Theoretical Probability 39, article 60 (2026), https://doi.org/10.1007/s10959-026-01517-1.
5. Y. Peres and S. Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227 (first submitted 2026-04-08), https://arxiv.org/abs/2604.07227 (abstract accessible; full text inaccessible).
