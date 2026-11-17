# Positive expansiveness collapses to uniform growth for nonnegative weighted right translations

## Finding

Let \(1\le p<\infty\) and let \(a\in L^\infty(0,\infty;\mathbb R)\) satisfy \(a\ge0\) almost everywhere. On complex \(L^p(0,\infty)\), define the strongly continuous weighted right-translation semigroup
\[
 (T_a(t)f)(x)=
 \begin{cases}
 0,&0<x<t,\\
 \exp\!\left(\int_{x-t}^{x}a(u)\,du\right)f(x-t),&x\ge t.
 \end{cases}
\]
Put
\[
 m_a(t)=\inf_{s\ge0}\int_s^{s+t}a(u)\,du,
 \qquad
 \alpha_a=\sup_{t>0}\frac{m_a(t)}t.
\]
The following classifications hold, independently of \(p\):

1. **Kinematic:** \(T_a\) is positively kinematic expansive in the sense of equal-time orbit comparison if and only if \(\int_0^\infty a(u)\,du=\infty\).
2. **Bowen--Walters:** \(T_a\) is positively expansive with continuous time reparametrizations if and only if \(m_a(L)>0\) for some \(L>0\). This is equivalent to **uniform exponential expansion**, namely the existence of \(C,\beta>0\) such that \(\|T_a(t)f\|_p\ge Ce^{\beta t}\|f\|_p\) for all \(f\) and all \(t\ge0\).
3. **Generator coercivity:** \(0\notin\sigma_{\mathrm{ap}}(A_a)\) holds exactly under the condition in item 2. If \(M=\|a\|_\infty>0\) and \(c=m_a(L)>0\), then every \(f\in D(A_a)\) satisfies \(\|A_af\|_p\ge M(e^c-1)(e^{ML}-1)^{-1}\|f\|_p\).
4. **Sharp rate:** \(\alpha_a\) is the supremum of admissible uniform exponential expansion rates. Every \(0<\beta<\alpha_a\) is admissible when \(\alpha_a>0\), but the endpoint \(\beta=\alpha_a\) need not be admissible.

In particular, within this complete family, positivity with time reparametrization never lies strictly between kinematic expansiveness and uniform exponential expansion. This contrasts with diagonal semigroups, for which these three notions may be distinct.

Two boundary examples are exact. For \(a(x)=1/(1+x)\), every nonzero orbit is unbounded, but \(m_a(t)=0\) for all \(t>0\), so the semigroup is kinematically expansive and not positively expansive. For \(a(x)=x/(1+x)\), one has \(m_a(t)=t-\log(1+t)\), giving \(\alpha_a=1\); the semigroup is positively expansive and uniformly expanding at every rate below \(1\), but at no rate equal to \(1\).

## Assumptions and scope

The field is \(\mathbb C\), \(1\le p<\infty\), and \(a\) is essentially bounded, real, nonnegative, and measurable on the half-line. All integrals are Lebesgue integrals; an infinite integral is interpreted in the extended nonnegative sense. A strongly continuous semigroup is *positively expansive* and *positively kinematic expansive* in the precise senses of Definitions 2.2 and 2.3 of Huynh (2026). In particular, these notions have different quantifiers: the former allows arbitrary continuous nonnegative time changes fixing time zero; the latter uses identical times.

The generator is the closed operator
\[
 A_a f=-f'+af,\qquad D(A_a)=W^{1,p}_0(0,\infty),
\]
where \(W^{1,p}_0(0,\infty)\) here means the first-order Sobolev functions with zero trace at the left endpoint. This follows from the ordinary right-shift generator and bounded perturbation by multiplication by \(a\). The weighted-translation formula can also be verified directly using characteristics and strong continuity. The result does not assert the same classifications for signed, unbounded, time-dependent, or matrix-valued potentials, or for \(L^\infty\).

## Proof

**Step 1: Exact minimum modulus and lower-growth exponent.** Changing variables in the norm gives, for every \(t\ge0\),
\[
 \|T_a(t)f\|_p^p
 =\int_0^\infty |f(s)|^p
 \exp\!\left(p\int_s^{s+t}a(u)\,du\right)ds.
\]
By testing with functions supported where the weight is arbitrarily close to its essential infimum,
\[
 \inf_{\|f\|_p=1}\|T_a(t)f\|_p=e^{m_a(t)}.
\]
Since the interval integral is continuous in its starting point, its usual infimum equals its essential infimum. Nonnegativity yields \(m_a(t)\ge0\). Splitting the interval at time \(s\) shows
\[
 m_a(s+t)\ge m_a(s)+m_a(t).
\]
Also \(0\le m_a(t)\le\|a\|_\infty t\). Superadditivity and local boundedness give the continuous-time Fekete relation
\[
 \lim_{t\to\infty}\frac{m_a(t)}t
 =\sup_{t>0}\frac{m_a(t)}t=\alpha_a.
\]
Indeed, dividing \(t\) into integer multiples of any fixed \(L\) and a nonnegative remainder proves the lower limit, while the supremum gives the upper limit.

**Step 2: Kinematic criterion.** If \(\int_0^\infty a<\infty\), the displayed norm identity gives \(\|T_a(t)\|\le \exp(\int_0^\infty a)\) for all \(t\); hence no nonzero orbit is unbounded. Conversely, if \(\int_0^\infty a=\infty\), then for each fixed \(s\ge0\), \(\int_s^{s+t}a\to\infty\) as \(t\to\infty\). Monotone convergence applied to the displayed norm identity shows \(\|T_a(t)f\|_p\to\infty\) for every nonzero \(f\). Huynh's Theorem 3.3 equates unboundedness of every nonzero orbit with positive kinematic expansiveness.

**Step 3: Sufficient and sharp condition for positive expansiveness.** Suppose that \(m_a(L)=c>0\) for some \(L>0\). Given \(t=kL+r\) with \(k\) a nonnegative integer and \(0\le r<L\), superadditivity and nonnegativity give
\[
 m_a(t)\ge kc\ge(c/L)t-c.
\]
Thus \(\|T_a(t)f\|_p\ge e^{-c}e^{(c/L)t}\|f\|_p\). By Huynh's uniform-exponential-expansion implication (Theorem 4.2), this semigroup is positively expansive. Moreover, for \(f\in D(A_a)\), the generator identity and the triangle inequality give
\[
(e^c-1)\|f\|_p\le\|T_a(L)f-f\|_p
\le\int_0^L\|T_a(s)\|\,ds\,\|A_af\|_p
\le\frac{e^{ML}-1}{M}\|A_af\|_p,
\]
where \(M=\|a\|_\infty>0\). This gives the stated explicit coercivity constant. The same estimate with any fixed \(L\) satisfying \(m_a(L)/L>\beta\) establishes all rates \(0<\beta<\alpha_a\).

Conversely, suppose \(m_a(L)=0\) for every \(L>0\). Fix \(0\ne\varphi\in C_c^\infty(0,1)\) with \(|\varphi|\le1\), and let \(M=\|a\|_\infty\). For every integer \(N\ge1\), choose \(s_N\ge0\) so that
\[
 \int_{s_N}^{s_N+N}a(u)\,du<N^{-1},
\]
and define \(f_N(x)=\varphi((x-s_N)/N)\). Then \(f_N\in D(A_a)\),
\[
 \|f_N\|_p=N^{1/p}\|\varphi\|_p,
 \qquad
 \|f_N'\|_p=N^{1/p-1}\|\varphi'\|_p,
\]
and, using \(a^p\le M^{p-1}a\) (with the evident interpretation for \(p=1\)),
\[
 \|a f_N\|_p^p\le\frac{M^{p-1}}N.
\]
Consequently
\[
 \frac{\|A_af_N\|_p}{\|f_N\|_p}
 \le\frac{\|\varphi'\|_p}{N\|\varphi\|_p}
 +\frac{M^{1-1/p}}{N^{2/p}\|\varphi\|_p}
 \longrightarrow0.
\]
Thus \(0\) belongs to the approximate point spectrum of the generator. Huynh's Theorem 3.6 shows that a positively expansive semigroup cannot have this property. Therefore \(T_a\) is **not** positively expansive. This proves the necessity of a positive interval lower mass and the collapse of the two stronger notions.

**Step 4: Exact limiting rate and its potential failure of attainment.** If \(\|T_a(t)f\|\ge C e^{\beta t}\|f\|\) for all \(f,t\), the exact minimum-modulus formula gives \(m_a(t)\ge\log C+\beta t\). Dividing by \(t\) and letting \(t\to\infty\) yields \(\beta\le\alpha_a\). Together with Step 3 this proves the claimed supremal rate. For \(a(x)=x/(1+x)\), which is increasing, the infimum over starting points occurs at \(s=0\), so
\[
 m_a(t)=\int_0^t\frac{x}{1+x}\,dx=t-\log(1+t).
\]
Here \(\alpha_a=1\), whereas \(e^{m_a(t)-t}=(1+t)^{-1}\to0\), excluding any positive global constant at the limiting rate. For \(a(x)=1/(1+x)\), divergence of its total integral yields kinematic expansiveness, whereas \(\inf_{s\ge0}\log(1+t/(1+s))=0\) for every \(t>0\), excluding positive expansiveness. Both examples have bounded nonnegative potentials.

## Verification

The proof uses no finite enumeration or computational certificate. Its nonstandard core is the explicit approximate-null construction in Step 3; each displayed norm bound follows by substitution, scaling, and \(a^p\le M^{p-1}a\). Independently reproduce the critical checks by (i) computing the norm identity by changing variables, (ii) integrating the two example potentials, and (iii) checking that the right-hand side of the normalized generator estimate tends to zero for every finite \(p\ge1\). These are analytic checks valid over the entire declared domain; no finite test is substituted for a limit proof.

## Relationship to prior work

Huynh (2026), arXiv:2611.01005, proves the abstract orbit-growth characterization (Theorem 3.3), the generator approximate-spectrum obstruction (Theorem 3.6), and the sufficiency of uniform exponential expansion (Theorem 4.2). That paper's right-translation example has a *constant* exponential weight; its diagonal examples separate three expansiveness notions. The contribution here is a complete, explicit potential-level classification for the entire nonnegative bounded weighted right-translation family, including the converse that positive expansiveness forces uniform exponential expansion and the sharp endpoint/nonattainment analysis. It does not claim the general abstract implications as new.

Lods, Mokhtar-Kharroubi and Sbihi (2008/2009), arXiv:0805.3654, study spectral mapping and spectral shapes for general weighted advection semigroups. Those spectral results are not used as novelty claims and do not state the bounded-nonnegative-potential Bowen--Walters classification above. Lee and Morales (2022/2023) introduce the relevant expansiveness notion; Phatak and Sholapurkar (2019/2020) study a distinct, higher-order isometric notion of *hyperexpansive* weighted translations.

## Limitations

The conclusion concerns positive time-reparametrization expansiveness on complex \(L^p\) for finite \(p\) and real nonnegative **bounded** potentials. It makes no assertion for sign-changing weights, unbounded potentials, nontransport semigroups, or other expansiveness conventions. The sharp rate is a supremum and is not always attained. A more general older equivalent classification for weighted-shift cocycles may exist; the available comparisons did not establish such coverage. Independent mathematical validation has not been performed.

## References

1. H. M. Huynh, *Positive expansiveness of operator semigroups: orbit growth and spectral criteria*, arXiv:2611.01005 (initial public submission 2026-10-31), especially Theorems 3.3, 3.6, 4.2, 4.4 and Example 4.6. https://arxiv.org/abs/2611.01005
2. B. Lods, M. Mokhtar-Kharroubi, M. Sbihi, *Spectral properties of general advection operators and weighted translation semigroups*, arXiv:0805.3654 (2008); *Communications on Pure and Applied Analysis* **8** (2009), 1469--1492. https://arxiv.org/abs/0805.3654
3. J. Lee, C. A. Morales, *Bowen--Walters expansiveness for semigroups of linear operators*, *Ergodic Theory and Dynamical Systems* **43** (2023), 1942--1951, DOI:10.1017/etds.2022.20.
4. G. M. Phatak, V. M. Sholapurkar, *Hyperexpansive weighted translation semigroups*, *Colloquium Mathematicum* **159** (2020), 157--169, DOI:10.4064/cm7583-12-2018.
