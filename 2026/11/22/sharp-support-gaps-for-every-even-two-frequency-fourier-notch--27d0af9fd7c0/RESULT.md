# Sharp support gaps for every even two-frequency Fourier notch

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(k\ge4\) be an even integer, and let \(\mu\ne0\) be a finite positive Borel measure with \(\widehat\mu(1)=\widehat\mu(k)=0\), where \(\widehat\mu(j)=\int_{\mathbb T}e^{-ij\theta}\,d\mu(\theta)\). The maximum possible length of an open circular arc disjoint from the closed support of \(\mu\) is exactly
\[
G_k=\pi-2\arcsin(r_k).
\]
Here \(t_k\) is the unique root in \((\pi/2,\pi)\) of
\[
k\sin t\sin(t/k)+\cos t\cos(t/k)=0,
\]
and, setting \(x_k=\sin(t_k/k)\) and \(\lambda_k=-\cos t_k/x_k>0\), the number \(r_k\) is the unique root in \((0,\sin(\pi/(2k)))\) of
\[
\cos(k\arcsin r)=\lambda_k r.
\]
Every equality measure is, up to a rotation and positive scaling, exactly the **one four-atom probability measure**
\[
\mu_k=\frac{w_k}{2}(\delta_{\alpha_k}+\delta_{-\alpha_k})
     +\frac{1-w_k}{2}(\delta_{\beta_k}+\delta_{-\beta_k}),
\]
where
\[
\alpha_k=\frac\pi2+\arcsin r_k,\qquad
\beta_k=\frac\pi2-\frac{t_k}{k},\qquad
w_k=\frac{x_k}{x_k+r_k}.
\]
In particular, the two moment zeros do not merely admit a four-atom optimizer: they rigidly determine it at the sharp gap. As \(k\to\infty\) through even integers,
\[
G_k=\pi-\frac{2a_*}{k}+O(k^{-3}),
\]
where \(t_*\in(\pi/2,\pi)\) is the unique root of \(t\sin t+\cos t=0\), \(L=-\cos t_*/t_*>0\), and \(a_*\in(0,\pi/2)\) is the unique root of \(\cos a_*=La_*\). Numerically \(a_*=1.167164677153\ldots\). The formulas include the previously known fourth-notch case \(G_4=2.569356100632\ldots\); the family and its asymptotic law are the new assertion.

## Assumptions and scope
A gap is an **open connected arc disjoint from the closed support**, not merely a measurable set of zero mass. The Fourier zeros are complex constraints; no a priori symmetry, discreteness, support cardinality or nonvanishing condition on other coefficients is imposed. Arc length is measured in radians. The theorem is about every even integer \(k\ge4\), not an arbitrary two-frequency mask. Classification is primary MSC2020 42A05 (Fourier series and coefficients). All formulae for \(t_k\), \(x_k\), \(r_k\) and \(w_k\) are intrinsic one-variable root definitions, so do not depend on numerical root selection.

## Proof
**1. Global one-lobe tangent.** Put \(F_k(x)=\cos(k\arcsin x)\), which is even because \(k\) is even, and satisfies \(F_k(\cos\theta)=(-1)^{k/2}\cos(k\theta)\). For positive \(x\le1\), let \(t=k\arcsin x\). The nonnegative ratio needed to touch a linear function is
\[
h_k(t)=\frac{-\cos t}{\sin(t/k)},\qquad 0<t\le k\pi/2,
\]
on intervals where \(\cos t<0\). In the first such lobe, \((\pi/2,3\pi/2)\), its derivative has the sign of
\[
g_k(t)=\sin t\sin(t/k)+k^{-1}\cos t\cos(t/k).
\]
The identity \(g_k'(t)=(1-k^{-2})\cos t\sin(t/k)<0\) on this lobe shows that its unique zero lies in \((\pi/2,\pi)\): the endpoint signs are positive at \(\pi/2\) and negative at \(\pi\). Thus \(h_k\) has exactly one maximizer there, at \(t_k\). For \(k=4\), no later negative-cosine lobe lies in the allowed interval. For \(k\ge6\), every later negative-cosine lobe starts at \(t\ge5\pi/2\), and monotonicity of the denominator implies
\[
h_k(t)\le\frac1{\sin(5\pi/(2k))}
<\frac1{\sin(\pi/k)}=h_k(\pi)<h_k(t_k).
\]
This proves the *global* and *unique* positive contact \(x_k=\sin(t_k/k)\), and the sharp inequality
\[
F_k(x)+\lambda_k x\ge0\qquad(0\le x\le1),
\]
with equality exactly at \(x=x_k\). Notice \(\lambda_k>0\).

**2. The negative boundary contact.** On \(0\le u\le\sin(\pi/(2k))\), the function \(F_k(u)=\cos(k\arcsin u)\) decreases strictly from one to zero. Consequently \(F_k(u)-\lambda_k u\) decreases strictly from one to a negative value, and has exactly one zero \(u=r_k\) in this interval. Since \(F_k(-u)=F_k(u)\), the witness polynomial
\[
P_k(x)=F_k(x)+\lambda_k x
\]
is nonnegative on \([-r_k,1]\), and its zero set there is *exactly* \(\{-r_k,x_k\}\). For \(-r_k\le x<0\), the defining monotonicity proves strict positivity except at the left endpoint; for \(x\ge0\), the previous step applies. No algebraic factorization or asymptotic approximation is used in this sign argument.

**3. Universal bound for arbitrary measures.** Rotate any alleged empty arc to be symmetric about angle \(\pi\), so the closed support is contained in \([-\alpha,\alpha]\). Then \(\cos\theta\in[\cos\alpha,1]\). Vanishing of the two complex Fourier coefficients gives the real equalities \(\int\cos\theta\,d\mu=0\) and \(\int\cos(k\theta)\,d\mu=0\), hence
\[
\int P_k(\cos\theta)\,d\mu(\theta)=0.
\]
If the gap length exceeded \(G_k=2\pi-2\alpha_k\), then \(\alpha<\alpha_k\), so \(\cos\alpha>-r_k\). The nonnegative witness and strict zero-set description force all mass onto \(\cos\theta=x_k>0\). This contradicts the first moment zero. Therefore every support-free arc has length at most \(G_k\), with no assumption of finite support.

**4. Attainment and complete equality rigidity.** At the sharp boundary \(\alpha=\alpha_k\), the same integration forces the cosine pushforward of \(\mu\) to be supported on exactly \(x=-r_k\) and \(x=x_k\). The first cosine moment fixes the total weights uniquely as \(w_k=x_k/(x_k+r_k)\) and \(1-w_k=r_k/(x_k+r_k)\), both positive. Since \(P_k\) vanishes at both contacts, this also gives the \(k\)-th cosine moment zero. Splitting each cosine fiber equally between its two angles defines the stated measure \(\mu_k\); symmetry makes both sine moments zero. It has all four masses positive and an open complement of length exactly \(G_k\).

For uniqueness without assuming symmetry, let \(\Delta_\alpha,\Delta_\beta\) denote the differences of the two opposite masses in the fibers at \(\pm\alpha_k\) and \(\pm\beta_k\). Vanishing of the two sine moments requires
\[
\begin{pmatrix}
\sin\alpha_k&\sin\beta_k\\
\sin(k\alpha_k)&\sin(k\beta_k)
\end{pmatrix}
\begin{pmatrix}\Delta_\alpha\\\Delta_\beta\end{pmatrix}=0.
\]
Write \(k=2m\). Because \(0<k\arcsin r_k<\pi/2\) and \(\pi/2<t_k<\pi\),
\[
\sin(k\alpha_k)=(-1)^m\sin(k\arcsin r_k),\qquad
\sin(k\beta_k)=(-1)^{m+1}\sin t_k.
\]
These values have **opposite nonzero signs**, while both first-row sine values are positive. The determinant is nonzero, so both mass differences vanish. This proves the full rotation-and-scaling equality classification.

**5. High-harmonic limit.** The equation for \(t_k\), multiplied by \(k\), converges uniformly on \([\pi/2,\pi]\) to \(t\sin t+\cos t=0\), which has a unique root because its derivative is \(t\cos t<0\) on that interval. Taylor expansion in \(k^{-2}\), or the implicit function theorem at this simple root, gives \(t_k=t_*+O(k^{-2})\) and \(\lambda_k/k=L+O(k^{-2})\). Let \(a_k=k\arcsin r_k\in(0,\pi/2)\). Its defining equation is \(\cos a_k=(\lambda_k/k)k\sin(a_k/k)\). The right side tends uniformly to \(La_k\), and \(a\mapsto\cos a-La\) has a unique simple root \(a_*\) in the interval. Another Taylor expansion gives \(a_k=a_*+O(k^{-2})\). Since \(G_k=\pi-2a_k/k\), the stated cubic-order error follows.

## Verification
Run the dependency-free `CHECK.py` with Python 3. It solves the defining one-variable equations for fifty even notches \(2\le k\le100\), checks the two vanishing cosine moments for the explicitly constructed measures, tests the witness polynomial on 2,001 deterministic support points per notch, verifies the nonzero sine rigidity determinants, checks agreement with the previously established fourth-notch constant, and checks the large-degree limiting coefficient. The script prints `CHECK_PASSED 104522` on the tested platform. These finite calculations are **diagnostics**, not a substitute for the all-integer and all-measure proof above; numerical nonnegativity on a mesh is not used to infer nonnegativity between mesh points.

For comparison, at \(k=6\), the unique sharp gap is approximately \(2.755760967446\); at \(k=8\) it is \(2.851142074984\). The proof determines these numbers without any finite-degree exhaustive enumeration.

## Relationship to prior work
Peherstorfer (2010), §1–3, characterizes positive circular quadrature exact for all frequencies through a **consecutive degree**, using orthogonal polynomials on the unit circle. The present constraints consist only of nonconsecutive frequencies \(1\) and an even \(k\), so that characterization does not supply the sharp gap or the four-atom equality law. Di Dio and Kummer (2019), §3, study Carathéodory-number bounds for truncated polynomial moment sequences with missing monomials; those bounds are about **minimal atom counts across moment functionals**, not the maximal circular hole of this fixed sparse moment vector.

The published result *A sharp sparse Fourier-notch gap on the circle* (2026) solves the different mask \(\{1,2,6\}\), with a rigid six-atom measure; requiring the second zero as an additional constraint is essential in that theorem and its certificate is not a bound under \(\{1,k\}\) alone. A previously established two-frequency \(\{1,4\}\) circular gap theorem is the \(k=4\) specialization here and is explicitly **not** being claimed anew. The new contribution is the uniform theorem for all even \(k\ge6\), its global one-lobe contact classification, and its sharp high-harmonic limit.

Tan and Zhang (2026), §2, prove a sharp gap and equality law under *all* consecutive Fourier zeros \(1,\dots,r-1\); their hypotheses do not follow from the two sparse zeros here. Their proof also uses a positivity witness, but does not imply the present two-contact even-notch root law. The classical papers of Gilbert–Smyth (2000) and Goldstein–McDonald (1984) are plausibly relevant to nonnegative trigonometric polynomials: only abstract/bibliographic material was accessible, so their potential stronger implications remain an explicit originality risk. Searches and inspected documents cannot certify historical uniqueness.

## Limitations
No claim is made for odd secondary frequencies, for more than two prescribed Fourier zeros, for noisy/approximately vanishing coefficients, or for quantitative near-extremizer stability. The sharp formula is implicit through unique real roots, not a general elementary-radical expression. The proof and diagnostics were checked without an independent expert audit. Older broad extremal trigonometric polynomial results could conceivably subsume the family; the inaccessible papers noted above warrant later historical review.

## References
- Philipp J. di Dio and Mario Kummer, *The multidimensional truncated Moment Problem: Carathéodory Numbers from Hilbert Functions*, arXiv:1903.00598, first publicly posted 2019-03-02, §3, https://arxiv.org/abs/1903.00598 .
- Franz Peherstorfer, *Positive trigonometric Quadrature Formulas and quadrature on the unit circle*, arXiv:1001.2451, first publicly posted 2010-01-14, §§1–3, https://arxiv.org/abs/1001.2451 .
- Hu Tan and Ying Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646, first publicly posted 2026-09-07, §2, https://arxiv.org/abs/2609.07646 .
- *A sharp sparse Fourier-notch gap on the circle*, published research record `2026/11/16/SCOPE-a-sharp-sparse-fourier-notch-gap-on-the-circle--6a5a2c4b54f3`, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-sharp-sparse-fourier-notch-gap-on-the-circle--6a5a2c4b54f3 .
- A. D. Gilbert and C. J. Smyth, *Zero-Mean Cosine Polynomials which are Non-Negative for as Long as Possible*, J. London Math. Soc. 62 (2000), 489–504, https://doi.org/10.1112/S0024610700001216 (abstract inspected; full text not accessible).
- M. Goldstein and J. N. McDonald, *An Extremal Problem for Non-Negative Trigonometric Polynomials*, J. London Math. Soc. 29 (1984), 81–88, https://doi.org/10.1112/jlms/s2-29.1.81 (bibliographic record only).
