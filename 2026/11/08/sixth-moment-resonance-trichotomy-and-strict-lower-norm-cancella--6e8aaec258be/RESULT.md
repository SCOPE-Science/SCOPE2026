# Sixth-moment resonance trichotomy and strict lower-norm cancellation for real two-tone Fourier planes

## Finding

Let \(1\le m<n\) be integers and let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) carry normalized Haar measure. For every nonzero real-valued two-tone polynomial
\[
f(\theta)=\operatorname{Re}(u e^{im\theta}+v e^{in\theta}),\qquad u,v\in\mathbb C,
\]
put \(K(f)=\|f\|_6^6/\|f\|_2^6\). Every possible value of \(K\) lies in the sharp attained interval \([L_{n/m},U_{n/m}]\) described below; its endpoints and **all** equality cases are classified.

Write \(t=|v|/|u|\) when \(u\ne0\), and define
\[
B(t)=\frac52+\frac{15t^2}{(1+t^2)^2},\qquad
R_2(t)=\frac{15t^2}{4(1+t^2)^3},\quad
R_3(t)=\frac{15t/2+15t^3}{(1+t^2)^3},\quad
R_5(t)=\frac{3t}{2(1+t^2)^3},
\]
and \(F_q^\pm(t)=B(t)\pm R_q(t)\).

* If \(n/m\notin\{2,3,5\}\), then \([L,U]=[5/2,25/4]\). Lower equality requires exactly one nonzero frequency coefficient; upper equality requires \(|u|=|v|\), with arbitrary phases.
* If \(n=2m\), then \(L=5/2\) with the same lower equality classification, while \(U=F_2^+(r_2)=6.7316915539090667\ldots\), where \(r_2=\sqrt{(\sqrt{21}-1)/4}\). Upper equality requires \(|v|/|u|=r_2\) and \(2(\arg v-2\arg u)\equiv0\pmod{2\pi}\).
* If \(n=3m\), let \(r_{3,-}\in(26/100,27/100)\) be the unique root there of \(4t^5-6t^4+t^2-4t+1=0\), and let \(r_{3,+}\in(86/100,87/100)\) be the unique root there of \(4t^5+6t^4-t^2-4t-1=0\). Then
\[
[L,U]=[F_3^-(r_{3,-}),F_3^+(r_{3,+})]=[1.5704313738148209\ldots,\ 9.2035263827847247\ldots].
\]
Lower equality requires \(|v|/|u|=r_{3,-}\) and \(\arg v-3\arg u\equiv\pi\pmod{2\pi}\); upper equality requires \(|v|/|u|=r_{3,+}\) and \(\arg v-3\arg u\equiv0\pmod{2\pi}\).
* If \(n=5m\), let \(r_{5,-}\in(49/1000,50/1000)\) be the unique root there of \(20t^5-5t^2-20t+1=0\), and let \(r_{5,+}\in(95/100,96/100)\) be the unique root there of \(20t^5+5t^2-20t-1=0\). Then
\[
[L,U]=[F_5^-(r_{5,-}),F_5^+(r_{5,+})]=[2.4628672447803226\ldots,\ 6.4470894315286700\ldots].
\]
Lower equality requires \(|v|/|u|=r_{5,-}\) and \(\arg v-5\arg u\equiv\pi\pmod{2\pi}\); upper equality requires \(|v|/|u|=r_{5,+}\) and \(\arg v-5\arg u\equiv0\pmod{2\pi}\).

All the phase conditions above assume both coefficients are nonzero. Every intermediate value in each interval occurs. The \(n=3m\) **upper** constant and its extremizers already follow from a published theorem for four consecutive complex Fourier coefficients and are included only to make the two-sided classification complete; they are **not** claimed as new. The new distinctions include the strict lower cancellations at ratios \(3\) and \(5\), the first sixth-order fifth-harmonic resonance, and the complete classification across all pairs of positive frequencies.

## Assumptions and scope

Functions are real, with arbitrary complex Fourier amplitudes \(u,v\), on the continuous circle with normalized Haar probability \(d\theta/(2\pi)\). Exactly two distinct positive frequencies are allowed, although either coefficient may vanish. The normalized functional uses sixth and second moments, not the \(L^6\) to \(L^2\) ratio itself (that ratio is \(K^{1/6}\)). The frequency ratio cases mean exact integer equalities, not approximations. All the boundary claims include zero coefficients by continuity. This theorem does not address finite cyclic aliases or complex-valued Fourier sums.

## Proof

**1. Exact sixth-order resonance classification.** With \(a=|u|\) and \(b=|v|\), the second moment is \((a^2+b^2)/2\). Expand \(f^6\) as products of six signed characters of frequencies \(\pm m,\pm n\). Only zero-sum tuples survive normalized integration. If the net signed counts of the two frequencies are \(r\) and \(s\), then \(rm+sn=0\), \(|r|+|s|\le6\), and \(|r|+|s|\) is even. For \(m<n\), the only nontrivial reduced solutions have \(n/m\in\{2,3,5\}\). Direct multinomial enumeration yields the exact identity
\[
K(f)=B(b/a)+\begin{cases}
R_2(b/a)\cos(2(\arg v-2\arg u)),&n=2m,\\
R_3(b/a)\cos(\arg v-3\arg u),&n=3m,\\
R_5(b/a)\cos(\arg v-5\arg u),&n=5m,\\
0,&\text{otherwise},
\end{cases}
\]
when \(a,b>0\); the endpoint formulas for zero coefficients follow from the original expansion. For clarity, the unnormalized universal term is \(5(a^6+b^6)/16+45(a^4b^2+a^2b^4)/16\); the extra unnormalized terms are respectively \(15a^4b^2\cos(2\psi)/32\), \((15a^5b/16+15a^3b^3/8)\cos\psi\), and \(3a^5b\cos\psi/16\). These expressions also give a direct independent check of the normalization.

**2. Phase optimization.** The three \(R_q(t)\) are strictly positive for \(t>0\). Consequently the least and greatest values at each fixed positive \(t\) are respectively \(F_q^-(t)\) and \(F_q^+(t)\); equality forces the displayed cosine to be \(-1\) or \(+1\). In nonresonant pairs \(B(t)\) has unique interior maximum at \(t=1\) and limiting minimum \(5/2\) at \(t=0,\infty\).

**3. The twice-frequency case.** For \(q=2\), \(F_2^-(t)-5/2=15t^2(3/4+t^2)/(1+t^2)^3>0\) when \(t>0\). Moreover
\[
(F_2^+)'(t)=-\frac{15t(4t^4+2t^2-5)}{2(1+t^2)^4}.
\]
The unique positive critical point is \(r_2\) above and is the strict global maximum.

**4. Triple and quintuple cases: global critical-point counting.** Exact differentiation gives
\[
(F_3^\pm)'(t)=-\frac{15P_{3,\pm}(t)}{2(1+t^2)^4},\qquad
(F_5^\pm)'(t)=-\frac{3P_{5,\pm}(t)}{2(1+t^2)^4},
\]
where
\[
\begin{aligned}
P_{3,-}(t)&=4t^5-6t^4+t^2-4t+1, &P_{3,+}(t)&=4t^5+6t^4-t^2-4t-1,\\
P_{5,-}(t)&=20t^5-5t^2-20t+1,&P_{5,+}(t)&=20t^5+5t^2-20t-1.
\end{aligned}
\]
The two plus-polynomials each have exactly one positive root by Descartes' sign rule, since their coefficients have one sign change and their values at zero and positive infinity have opposite signs. Each gives the unique strict global maximum of \(F_q^+\) because \((F_q^+)'(0)>0\) and \(F_q^+(t)\to5/2\) at infinity.

For \(P_{3,-}\), its derivative \(20t^4-24t^3+2t-4=4t^3(5t-6)+2t-4\) is strictly negative on \((0,1]\), while its second derivative \(8t^2(10t-9)+2\) is strictly positive for \(t\ge1\). Because \(P_{3,-}(0)=1\), \(P_{3,-}(1)=-4\), and its leading coefficient is positive, it has exactly two positive roots: one in \((0,1)\) and one above \(1\). The first is a strict local minimum of \(F_3^-\), the second a local maximum. The first lies below \(5/2\), since \((F_3^-)'(0)<0\), while both boundary limits are \(5/2\). It is therefore the unique global minimum.

For \(P_{5,-}\), the derivative \(100t^4-10t-20\) decreases once and then increases strictly to infinity because its derivative \(400t^3-10\) has exactly one positive root. Thus \(P_{5,-}\) has one positive local minimum and, using \(P_{5,-}(0)=1\), \(P_{5,-}(1)=-4\), and positive leading coefficient, exactly two positive roots. As in the triple case, the first is the unique global minimum of \(F_5^-\), with value strictly below \(5/2\); the second is a local maximum. The rational root-isolating intervals in the Finding are verified by exact opposite-sign endpoint evaluations; the monotonicity proves uniqueness. This exhausts every interior and boundary candidate.

**5. Equality and interval filling.** Equality in phase reduction and the strict critical-point classification yields all stated extremizers. The set of unit coefficient vectors \(\{(u,v)\in\mathbb C^2:|u|^2+|v|^2=1\}\) is connected, and the continuous sixth-moment ratio maps it to a connected compact subset of \(\mathbb R\). Since both global endpoints are attained, every value between them is attained.

## Verification

The self-contained `artifacts/verify.py` (standard Python library only) independently expands all signed six-character sums for ratios \(2\) through \(50\) and matches every coefficient and phase term with the stated classification. It checks each critical derivative polynomial exactly using rational polynomial arithmetic; it checks rational root-isolating sign brackets and independent exact moment witnesses for zero-phase amplitudes. Execute with `python3 artifacts/verify.py` from the extracted package root. The checker is finite algebraic identity verification; the universal frequency restriction and global extrema follow from the proof above, not from finite enumeration over frequencies or numerical tests.

## Relationship to prior work

The frequency-space \(L^p\) framework goes back at least to Bonami's 1970 paper on Fourier coefficient decay and \(\Lambda(p)\) sets; Mockenhaupt and Schlag's arXiv paper from 2002 discusses even-exponent Fourier coefficient majorization but does not give the two-sided real two-tone sixth-moment classification. The existing exact four-consecutive-character sixth-moment theorem **does** imply the \(n=3m\) upper endpoint after shifting and rescaling the symmetric support \(\{-3,-1,1,3\}\) to \(\{0,1,2,3\}\). Its upper value is the same \(9.20352638\ldots\), and that overlap is acknowledged rather than relabeled as novel. It does not provide the sharp *lower* constant or the quintuple-frequency cancellation. Previously established real two-tone fourth-moment results have a third-harmonic but not a fifth-harmonic resonance, and do not imply the sixth-moment statements. The classical finite-dimensional polynomial Banach-space investigations of Gordon and Reisner are potentially relevant, but only their abstract was accessible; their full text was not compared.

## Limitations

The claim does not assert mathematical priority over unindexed tables, uncatalogued manuscripts or any inaccessible specialist polynomial-space source. It gives no Banach--Mazur claim and no extension to other even exponents. The extrema are algebraic numbers defined by the given isolated roots; decimal values are diagnostic approximations. A full independent audit has not been performed.

## References

- A. Bonami, *Étude des coefficients de Fourier des fonctions de \(L^p(G)\)*, Annales de l'Institut Fourier 20 (1970), 335–402, DOI: 10.5802/aif.357; full text https://numdam.org/item/10.5802/aif.357.pdf .
- G. Mockenhaupt and W. Schlag, *On the Hardy--Littlewood majorant problem for random sets*, arXiv:math/0207226v1, first public arXiv submission 2002-07-25, https://arxiv.org/html/math/0207226v1 .
- *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, public mathematical record https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219 .
- Y. Gordon and S. Reisner, *Some geometrical properties of Banach spaces of polynomials*, Israel J. Math. 42 (1982), 99–116, DOI: 10.1007/BF02765014 (abstract inspected; full text unavailable).
