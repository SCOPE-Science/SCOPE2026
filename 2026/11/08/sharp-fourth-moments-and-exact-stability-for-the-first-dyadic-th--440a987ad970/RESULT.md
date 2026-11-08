# Sharp fourth moments and exact stability for the first dyadic three-harmonic space

## Finding
On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with normalized Haar measure \(dm(t)=dt/(2\pi)\), consider the six-dimensional **real** function space
\[
V=\left\{f(t)=\operatorname{Re}\bigl(u_1e^{it}+u_2e^{2it}+u_4e^{4it}\bigr):u_1,u_2,u_4\in\mathbb C\right\}.
\]
For every nonzero \(f\in V\), the following two sharp inequalities hold:
\[
\boxed{\frac32\le\frac{\int_{\mathbb T}f^4\,dm}{\left(\int_{\mathbb T}f^2\,dm\right)^2}\le\frac{45}{14}.}
\]
The **lower equality cases** are precisely the nonzero pure harmonics \(\operatorname{Re}(ue^{ijt})\), with \(j\in\{1,2,4\}\) and \(u\ne0\). The **upper equality cases** are precisely those with
\[
|u_1|^2:|u_2|^2:|u_4|^2=3:2:2,
\qquad
2\arg u_1+\arg u_2-\arg u_4\equiv0\pmod{2\pi}.
\]
The phase condition is invariant under translation of the circle. The upper constant yields the exact embedding norm \(\|\operatorname{id}:V_{L^2}\to V_{L^4}\|=(45/14)^{1/4}\).

In addition to the extremal values, both inequalities have explicit **nonnegative deficit identities**. Put
\[
P=|u_1|^2,\quad Q=|u_2|^2,\quad R=|u_4|^2,\quad S=P+Q+R>0,\quad
T=\operatorname{Re}(u_1^2u_2\overline{u_4}),\quad M=4\int_{\mathbb T} f^4\,dm.
\]
Then \(\int f^2\,dm=S/2\) and
\[
\boxed{M=\frac32(P^2+Q^2+R^2)+6(PQ+PR+QR)+6T.}\tag{1}
\]
The exact lower deficit is
\[
\boxed{M-\frac32S^2
=3P(\sqrt Q-\sqrt R)^2+3QR+6(P\sqrt{QR}+T).}\tag{2}
\]
The exact upper deficit is
\[
\boxed{\frac{45}{14}S^2-M
=\frac{21}{4}\left(P-\frac{3S}{7}\right)^2
+\frac34(Q-R)^2+3P(\sqrt Q-\sqrt R)^2
+6(P\sqrt{QR}-T).}\tag{3}
\]
Every summand on the right of (2) and (3) is nonnegative.

The same calculation locates a sharp **arithmetic resonance threshold** for the geometric three-frequency spaces
\[
V_b=\operatorname{span}_{\mathbb R}\{\cos t,\sin t,\cos(bt),\sin(bt),\cos(b^2t),\sin(b^2t)\},\quad b\in\mathbb Z,\ b\ge2.
\]
For every \(b\ge4\), the exact sharp normalized fourth-moment interval is \([3/2,5/2]\). Lower equality consists of a single nonzero frequency; upper equality consists of equal energy in the three harmonics, with completely free relative phases. At \(b=3\), both independent fourth-order additive resonances occur and the two endpoints of the generic interval fail: \(\cos t-\frac14\cos3t\) has normalized fourth moment \(707/578<3/2\), while \(\cos t+\cos3t+\cos9t\) has normalized fourth moment \(53/18>5/2\). No sharp extremal classification for \(b=3\) is claimed.

## Assumptions and scope
Coefficients are arbitrary complex numbers, while the resulting functions are real-valued. All integrals use normalized Haar measure. The real subspace includes the six positive/negative frequencies \(\{\pm1,\pm2,\pm4\}\), unlike a three-character analytic polynomial with only positive frequencies. The coefficient normalization \(f=\operatorname{Re}\sum u_j e^{ijt}\) implies \(\|f\|_2^2=S/2\); changing the convention changes intermediate constants but not the displayed normalized moment ratio. Equality is understood for nonzero functions.

The object is the first three-level geometric lacunary family. Its positive/negative frequencies create additive relations absent from the corresponding analytic three-character problem. The requested invariant is the sharp \(L^2\)-to-\(L^4\) distortion, including all norming configurations and an exact measure of the deviation from extremality. This is a complete norm-geometry question for a natural six-dimensional real subspace, rather than an individual fourth-moment evaluation.

## Proof
**Step 1: exact Haar moments.** Expand
\[
f(t)=\tfrac12\sum_{j\in\{1,2,4\}}(u_je^{ijt}+\overline{u_j}e^{-ijt}).
\]
The normalized Haar integral of a Fourier monomial vanishes unless its frequency sum is zero. Consequently \(\int f^2\,dm=S/2\). In the fourth moment, the pairwise-balanced contributions have coefficients \(6/16\) on \(|u_j|^4\) and \(24/16\) on \(|u_i|^2|u_j|^2\) for \(i<j\). The only unbalanced four-term frequency relation is \(1+1+2=4\) and its negative, giving coefficient \(12/16\) for each conjugate monomial. Multiplying by four gives formula (1).

**Step 2: exact positive deficits.** The bound
\[
-P\sqrt{QR}\le T\le P\sqrt{QR}
\]
follows from \(|\operatorname{Re}z|\le|z|\). Expanding (2) gives \(3(PQ+PR+QR)+6T\), equal to (1) minus \(3S^2/2\). Similarly expand the right side of (3), substitute \(S=P+Q+R\), and cancel terms to obtain \(45S^2/14-M\). Both expressions are nonnegative. As \(\|f\|_2^4=S^2/4\), they prove the two sharp moment inequalities.

**Step 3: equality.** In (2), if \(P=0\) then \(QR=0\); if \(P>0\), the first term forces \(Q=R\) and the second forces \(QR=0\). Thus at most one of \(P,Q,R\) is nonzero, and every such function is a pure harmonic attaining equality. In (3), equality implies \(P=3S/7\), \(Q=R\), and \(T=P\sqrt{QR}\). Since \(Q+R=4S/7\), both equal \(2S/7\) and are positive. Equality in the complex modulus bound is precisely the stated phase congruence. Conversely these data make every term in (3) zero, proving the claimed upper equality classification.

**Step 4: larger geometric gaps.** For \(b\ge4\), the only zero-sum quadruples from \(\{\pm1,\pm b,\pm b^2\}\) are opposite-paired. Indeed, write a four-term relation as \(A+bB+b^2C=0\), where \(|A|+|B|+|C|\le4\) are the signed multiplicities of the three frequencies. For \(b\ge5\), reduction modulo \(b\) gives \(A=0\), then division and reduction modulo \(b\) gives \(B=0\), hence \(C=0\). For \(b=4\), a nonzero \(A\) divisible by four would require four copies of \(\pm1\) and leave no other frequency to cancel their sum; hence \(A=0\). The same argument then gives \(B=C=0\). Thus formula (1) holds without the last resonance term for \(b\ge4\). In that case
\[
M-\frac32S^2=3(PQ+PR+QR),\qquad
\frac52S^2-M=\frac12\bigl((P-Q)^2+(P-R)^2+(Q-R)^2\bigr).
\]
Both are exact nonnegative deficits, proving the stated sharp interval and complete equality conditions.

For \(b=3\), direct counting shows that the additional unbalanced zero-sum relations are \(1+1+1=3\) and \(3+3+3=9\). Their combined contribution to \(M\) is
\[
2\operatorname{Re}(u_1^3\overline{u_3}+u_3^3\overline{u_9}).
\]
Substitution of the explicit displayed test functions gives the two exact ratios stated in the finding. This establishes the arithmetic boundary without asserting a complete \(b=3\) extremal theorem.

## Verification
The standalone `checker.py` expands all zero-frequency quartic monomials from six formal Fourier symbols and checks the entire coefficient tensor against the claimed formulas for geometric gaps \(b=2,3,4,5,6,7,10,19\). It verifies the sharp dyadic value and both deficits exactly on \(728\) nonzero integer-amplitude sign patterns, checks both exact ternary-gap witnesses, and compares analytical moments with independent normalized-circle quadrature for eight complex coefficient samples. It returns `ALL_LACUNARY_FOURTH_MOMENT_CHECKS_OK`.

The finite enumeration and testing are not the proof for all gaps or coefficients. The universal statements follow from Fourier orthogonality, the zero-sum relation classification and the exact algebraic nonnegative identities above. The checker uses only Python's standard library and can be run with `python3 checker.py`.

## Relationship to prior work
Neuwirth's *Metric unconditionality and Fourier analysis* (1997) examines even-exponent Fourier moments and arithmetic relations, including geometric sequences. Its Sections 3.3, 4.2 and 9.2 provide relevant additive-relation context but optimize unconditionality properties rather than this sharp real six-dimensional \(L^2\)-to-\(L^4\) ratio. Neuwirth's 2001 Sidon paper treats a three-character supremum-norm extremal problem, not the present real signed-frequency moment interval.

Bonami's 1970 work develops \(\Lambda(p)\) norm inequalities for lacunary trigonometric series, but the accessible introductory and estimate pages provide general bounds, not a sharp coefficient-space classification for \(\{\pm1,\pm2,\pm4\}\). Nursultanov, Ruzhansky and Tikhonov (2014) give Nikolskii-type norm estimates on compact manifolds using spectral counting, not this exact finite spectral support and its equality classes. Bonami, Latała, Nayar and Tkocz (2018) study finite Riesz *products* and coefficient inequalities; their Theorem 1 controls different product-generated functions and explicitly does not give these best constants.

Published results on the \(\Lambda(4)\) constant of *three complex characters* and on the four-character spectrum \(\{0,1,2,4\}\) optimize different coefficient spaces: neither contains all six conjugate-paired frequencies or supplies the two real deficit identities here. These are genuine distinctions in the mathematical hypotheses, not merely differences in title. An older exact real-subspace calculation with equivalent scope remains a bibliographic risk.

## Limitations
The complete sharp constant and extremizer theorem concerns the real subspace of frequencies \(\{\pm1,\pm2,\pm4\}\), normalized Haar measure, and fourth moments. The generic geometric-gap theorem concerns only three harmonics for integer gap \(b\ge4\). The two explicit \(b=3\) examples prove only that the generic interval fails; they do not give the \(b=3\) sharp endpoints. None of the results extends automatically to higher moments, more frequencies, arbitrary non-geometric supports, or non-Haar measures. No independent validation or exhaustive historical-literature claim is made.

## References
1. S. Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211v1, first public 1997-07-28; full text examined in version 2, https://arxiv.org/html/math/9707211v2 .
2. S. Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145v1, first public 2001-02-19, https://arxiv.org/abs/math/0102145 .
3. A. Bonami, *Étude des coefficients de Fourier des fonctions de Lp(G)*, Ann. Inst. Fourier 20 (1970), 335–402, https://www.numdam.org/article/AIF_1970__20_2_335_0.pdf .
4. E. Nursultanov, M. Ruzhansky, S. Tikhonov, *Nikolskii inequality and Besov, Triebel-Lizorkin, Wiener and Beurling spaces on compact homogeneous manifolds*, arXiv:1403.3430v1, first public 2014-03-13, https://arxiv.org/abs/1403.3430 .
5. A. Bonami, R. Latała, P. Nayar, T. Tkocz, *Bounds on moments of weighted sums of finite Riesz products*, arXiv:1805.10918v1, first public 2018-05-28, https://arxiv.org/abs/1805.10918 .
6. *Exact Lambda(4) constants for every three-character subset of a cyclic group*, published mathematical research record 5562292e7127, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lambda-4-constants-for-every-three-character-subset-of-a-c--5562292e7127 .
7. *Sharp fourth moments for linked-midpoint four-character spectra*, published mathematical research record 0b57c5d24021, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-linked-midpoint-four-character-spectra--0b57c5d24021 .
