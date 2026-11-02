# A universal four-mode fourth-moment constant and the sharp seven-point sampling threshold

## Finding
Let \(G\) be a compact abelian group with normalized Haar probability measure \(\mu\). Let \(\gamma,\chi\) be continuous characters, with \(\chi\) of finite order at least \(7\), or of infinite order. For arbitrary complex \(c_0,c_1,c_2,c_3\), define
\[
F(g)=\gamma(g)\sum_{j=0}^3 c_j\chi(g)^j.
\]
Let \(\rho\) be the unique positive root of
\[
3\rho^3+3\rho^2-3\rho-1=0
\]
(\(\rho\approx0.7925172139743403\)), and put
\[
\mathcal K=\frac{3\rho^4+12\rho^2+4\rho+3}{2(1+\rho^2)^2}
\approx2.8088401654743969.
\]
Then the sharp inequality is
\[
\int_G |F(g)|^4\,d\mu(g)\ \leq\ \mathcal K\left(\sum_{j=0}^3|c_j|^2\right)^2.
\]
Every nonzero equality case, and no others, is
\[
(c_0,c_1,c_2,c_3)
=\lambda(\rho,e^{i\varphi},e^{2i\varphi},\rho e^{3i\varphi}),
\qquad\lambda\in\mathbb C\setminus\{0\},\ \varphi\in\mathbb R.
\]
For four distinct consecutive characters, the finite-order restriction is sharp: if \(\chi\) has order \(4\), \(5\), or \(6\), the displayed inequality with constant \(\mathcal K\) fails. Thus order \(7\) is precisely the start of the stable fourth-moment regime.

## Assumptions and scope
The group is compact and abelian, with normalized Haar measure. The characters have modulus one. The only order assumption concerns \(\chi\), not \(\gamma\); no connectedness or cyclicity of \(G\) is required. The support \(\{\gamma,\gamma\chi,\gamma\chi^2,\gamma\chi^3\}\) consists of four distinct characters. No sign, phase, or equal-magnitude restriction is imposed on the coefficients. The formula also applies to the usual circle norm by taking \(G=\mathbb T\) and \(\chi(z)=z\).

## Proof
Write \(s=\sum_{j=0}^3|c_j|^2\) and define the three aperiodic coefficient correlations
\[
R_h=\sum_{j=0}^{3-h}c_{j+h}\overline{c_j},\qquad h=1,2,3.
\]
The character frequencies \(\chi^h\) for \(-3\leq h\leq3\) are distinct because the order of \(\chi\) is at least \(7\), or infinite. Expanding \(|F|^2\) and applying character orthogonality therefore gives the **exact** identity
\[
\int_G|F|^4\,d\mu=s^2+2\bigl(|R_1|^2+|R_2|^2+|R_3|^2\bigr). \tag{1}
\]
Let \(a_j=|c_j|\), and put
\[
A=\sqrt{(a_0^2+a_3^2)/2},\qquad
B=\sqrt{(a_1^2+a_2^2)/2}.
\]
Then \(s=2(A^2+B^2)\). Cauchy--Schwarz and the arithmetic--geometric mean inequality give
\[
\begin{aligned}
|R_1|&\leq a_0a_1+a_1a_2+a_2a_3\leq 2AB+B^2,\\
|R_2|&\leq a_0a_2+a_1a_3\leq 2AB,\\
|R_3|&=a_0a_3\leq A^2.
\end{aligned}\tag{2}
\]
Thus averaging each outer magnitude pair and each inner magnitude pair cannot decrease the fourth moment. Substituting (2) into (1) yields
\[
\int_G|F|^4\,d\mu\leq4(A^2+B^2)^2+
2\bigl((2AB+B^2)^2+4A^2B^2+A^4\bigr).
\]
If \(B>0\), set \(t=A/B\geq0\) and divide by \(s^2\). The right-hand ratio is
\[
H(t)=\frac{3t^4+12t^2+4t+3}{2(1+t^2)^2}.
\]
Direct differentiation gives
\[
H'(t)=-\frac{2(3t^3+3t^2-3t-1)}{(1+t^2)^3}. \tag{3}
\]
The numerator polynomial \(P(t)=3t^3+3t^2-3t-1\) is decreasing on \((0,1/3)\), increasing on \((1/3,\infty)\), and satisfies \(P(0)=-1\), \(P(1)=2\). Hence it has exactly one positive zero \(\rho\in(1/3,1)\); equation (3) shows that \(H\) increases up to \(\rho\) and decreases thereafter. The cases \(B=0\) and \(A=0\) have fourth-moment ratio at most \(3/2\), whereas \(H(\rho)>H(1)=11/4\). Consequently \(\mathcal K=H(\rho)\) is the unrestricted optimum.

At equality both \(A\) and \(B\) are positive and (2) is sharp. Equality in \(a_0a_3\leq A^2\) gives \(a_0=a_3=A\), while equality in \(a_1a_2\leq B^2\) gives \(a_1=a_2=B\). Equality in the triangle inequality for \(R_1\) forces the three consecutive phase increments to agree modulo \(2\pi\). Thus \(c_j\) has a common scalar phase and a linear phase progression, and \(A/B=\rho\). This gives precisely the coefficient family in the finding; substitution into (1) attains equality.

For the sharp order threshold, choose these same coefficients with \(\lambda=1\) and \(\varphi=0\), all strictly positive. When the order of \(\chi\) is \(4\), \(5\), or \(6\), at least two among the exponents \(-3,-2,-1,0,1,2,3\) coincide modulo the order. Since the corresponding autocorrelation coefficients are positive, collecting their terms strictly increases the sum of squared Fourier coefficients over the unaliased value \(\mathcal K s^2\). Thus no one of these three orders obeys the inequality with \(\mathcal K\). For an elementary witness, choosing all four coefficients equal gives fourth-moment ratios \(4\), \(13/4\), and \(23/8\) at orders \(4\), \(5\), and \(6\), respectively.

## Verification
The standalone standard-library Python program `checker.py` computes \(\rho\) by bisection, checks its defining cubic, and evaluates the fourth moment two ways: direct finite character sums and identity (1). It checks the three small-order witnesses, \(3500\) randomized complex coefficient vectors, and \(560\) phase-parametrized extremizers on seven cyclic orders \(7,8,9,11,16,32,47\). Execute `python3 checker.py` from the directory containing this result. Every assertion must pass. The checks are finite and numerical; the proof for all compact groups is the preceding orthogonality and inequality argument.

## Relationship to prior work
The aperiodic-correlation identity underlying (1) is standard. Schmidt's *On a problem due to Littlewood concerning polynomials with unimodular coefficients* (arXiv:1302.2766, Section 2, equation (5)) uses it to analyze asymptotic **small** fourth moments of **unimodular** long polynomials. Katz and van der Linden's *Peak Sidelobe Level and Peak Crosscorrelation of Golay--Rudin--Shapiro Sequences* (arXiv:2108.07318, Sections 1--2) studies fixed binary recursive sequences and low peak correlations. Neither proves a sharp **maximum** over all freely weighted four-mode coefficients or its equality classification.

The published *Four-point support geometry quantizes the phase-only fourth Fourier moment* (published-finding corpus, identifier in References) addresses a four-point frequency support but takes a **minimum** over **equal-magnitude** coefficients, and varies the support geometry in prime groups. Its four-term-progression value \(19\) is a phase-only minimum, not the present weighted maximum \(\mathcal K\) (equivalently \(16\mathcal K\) at energy \(4\)). Hence its stated theorem does not imply this claim. The present result unifies circle and finite cyclic cases, with a sharp finite sampling threshold and full unrestricted optimizer characterization.

## Limitations
No sharp constants are asserted for orders \(4\), \(5\), or \(6\); only failure of the stable constant is proved there. The result does not address arbitrary non-progression four-point spectra or higher moments. A bibliographic risk remains that an earlier source may state this particular four-tap maximum under correlation-energy or polynomial-embedding terminology. The numerical checker cannot exclude such prior coverage or replace the algebraic proof.

## References
1. D. J. Katz and C. M. van der Linden, *Peak Sidelobe Level and Peak Crosscorrelation of Golay--Rudin--Shapiro Sequences*, arXiv:2108.07318v1, first posted 2021-08-16; https://arxiv.org/abs/2108.07318.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first posted 2013-02-12; https://arxiv.org/abs/1302.2766.
3. *Four-point support geometry quantizes the phase-only fourth Fourier moment*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-point-support-geometry-quantizes-the-phase-only-fourth-four--2b7f859e0b5c.
