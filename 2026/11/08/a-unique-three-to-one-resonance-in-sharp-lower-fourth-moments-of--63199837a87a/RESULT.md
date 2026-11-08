# A unique three-to-one resonance in sharp lower fourth moments of real two-tone Fourier spaces

## Finding
Write \(dm(t)=dt/(2\pi)\) on \([0,2\pi]\). For any integers \(1\le m<n\), consider the real four-dimensional subspace
\[
E_{m,n}=\{f(t)=\operatorname{Re}(u e^{imt}+v e^{int}):u,v\in\mathbb C\}\subset L^4(dm).
\]
For \(f\ne0\) set \(K(f)=\|f\|_4^4/\|f\|_2^4\). Let \(r\) be the unique root in \((1/4,3/10)\) of
\[
3r^3-3r^2-3r+1=0,
\]
and put
\[
\kappa=\frac32+\frac{3r^2-2r}{(1+r^2)^2}=1.220691895037155\ldots.
\]
**Sharp lower-moment classification.** For every nonzero \(f\in E_{m,n}\):

* If \(n\ne3m\), then \(K(f)\ge3/2\), with equality precisely for single-frequency harmonics (\(u=0\) or \(v=0\)).
* If \(n=3m\), then \(K(f)\ge\kappa\). Equality holds precisely when \(u,v\ne0\), \(|v|/|u|=r\), and \(\operatorname{Re}(u^3\overline v)=-|u|^3|v|\), equivalently \(\arg v-3\arg u=\pi\) modulo \(2\pi\).

The exceptional lower constant is the unique root in \((1,3/2)\) of \(208z^3-1224z^2+2268z-1323=0\). All these sharp infima are attained. Thus a ratio of frequencies exactly \(3:1\), and no other pair of distinct positive integer frequencies, permits a normalized fourth moment strictly below that of a single real harmonic.

**Exact resonance stability.** If \(n=3m\) and \(u\ne0\), write \(x=|v|/|u|\). If \(v\ne0\) write \(\eta=\operatorname{Re}(u^3\overline v)/(|u|^3|v|)\in[-1,1]\), and take \(\eta=0\) when \(v=0\). Then
\[
K(f)-\kappa=\frac{(x-r)^2P_r(x)}{(1+x^2)^2(1+r^2)^2}+\frac{2x(1+\eta)}{(1+x^2)^2},
\]
where
\[
P_r(x)=r(2-3r)x^2+(2-6r-2r^2)x+3+6r-6r^2.
\]
All three coefficients of \(P_r\) are strictly positive. Consequently the remainder vanishes precisely at the listed amplitude and phase configuration. At \(u=0\) the value is \(3/2>\kappa\).

## Assumptions and scope
The measure is normalized uniform Haar measure on the circle. The two frequencies are **distinct positive integers**, without any coprimality assumption, and both real sine and cosine phases are permitted independently. The claims concern the **lower** \(L^4/L^2\) norm-equivalence constant; no new upper norm assertion is made. In a pair \((m,n)\) with \(n=3m\), multiplication of \(u,v\) by corresponding translation phases preserves the equality condition. Zero coefficients, arbitrary nonzero real overall scalings, and complex coefficient phases are included.

## Proof
Put \(a=|u|\), \(b=|v|\). Fourier orthogonality gives
\[
\|f\|_2^2=\frac{a^2+b^2}{2}.
\]
A fourth-order zero-sum among the four frequencies \(\{-n,-m,m,n\}\) is either a paired cancellation, or (up to reversing all signs) three occurrences of \(m\) against one occurrence of \(n\). The latter is possible if and only if \(n=3m\). Hence the exact identity is
\[
\|f\|_4^4=\frac38(a^4+b^4)+\frac32a^2b^2+
\mathbf1_{\{n=3m\}}\frac12\operatorname{Re}(u^3\overline v).
\tag{1}
\]
For \(n\ne3m\), division by the squared second moment yields
\[
K(f)=\frac32+\frac{3a^2b^2}{(a^2+b^2)^2}\ge\frac32,
\]
with equality exactly when \(ab=0\). This proves the generic case without assumptions on relative phases.

For \(n=3m\), take \(a>0\), set \(x=b/a\ge0\), and define \(\eta\) as above. From (1),
\[
K(f)=\frac32+\frac{3x^2+2x\eta}{(1+x^2)^2}
\ge F(x):=\frac32+\frac{3x^2-2x}{(1+x^2)^2}.
\tag{2}
\]
If \(x>0\), equality in (2) means \(\eta=-1\). Differentiation yields
\[
F'(x)=-\frac{2(3x^3-3x^2-3x+1)}{(1+x^2)^3}.
\tag{3}
\]
The cubic \(G(x)=3x^3-3x^2-3x+1\) is positive at \(1/4\), negative at \(3/10\), and positive at \(2\). Descartes' rule of signs shows that it has at most two positive zeros, so those sign changes give exactly two: \(r\in(1/4,3/10)\) and a second zero greater than \(3/10\). Thus \(F\) decreases to \(r\), increases to the second zero, and then decreases towards \(\lim_{x\to\infty}F(x)=3/2\). Since \(F(r)<3/2\), its unique global minimum on \([0,\infty)\) is \(\kappa=F(r)\). The boundary \(a=0\) has \(K=3/2\), so it is not extremal.

The cubic equation for \(\kappa\) follows by eliminating \(r\) between \(G(r)=0\) and its displayed rational definition, or by polynomial division; its only root in \((1,3/2)\) is \(\kappa\), since the derivative of the cubic in that interval is positive and the cubic changes sign. This is an exact algebraic description, not a numerical extrapolation.

For stability, clear denominators in the following polynomial identity:
\[
F(x)-F(r)-\frac{(x-r)^2P_r(x)}{(1+x^2)^2(1+r^2)^2}
=-\frac{2(x-r)G(r)}{(1+x^2)(1+r^2)^2}=0.
\]
Adding the exact nonnegative phase excess \(2x(1+\eta)/(1+x^2)^2\) proves the stated remainder. Positivity of \(P_r\) follows from \(1/4<r<3/10\): \(r(2-3r)>0\), \(2-6r-2r^2>0\), and \(3+6r-6r^2>0\). Therefore both the amplitude and phase requirements are necessary and sufficient for equality, completing the classification for all allowed frequencies.

## Verification
The self-contained Python 3 standard-library program `checker.py` verifies the bivariate polynomial stability identity **coefficient by coefficient over rational integers**, enumerates exact fourth-order Fourier zero-sums for many distinct frequency pairs and rational coefficients, isolates \(r\) using rational bisection, checks the exact positivity assertions and algebraic endpoint, and separately compares six examples with direct normalized quadrature. Run `python3 checker.py` beside this file. Its final line must read `ALL_TWO_TONE_REVERSE_FOURTH_MOMENT_CHECKS_OK`. The enumerations and quadrature are consistency checks; the universal quantifiers are proved by the zero-sum classification and the exact algebraic argument above.

## Relationship to prior work
Fourth moments of Fourier polynomials can be expressed as autocorrelation energies, as in Schmidt's 2013 study of **unimodular, increasing-length analytic** Littlewood polynomials (Section 2). Neuwirth's 2007 work classifies the **supremum norm** geometry of complex trigonometric trinomials, including phase extremality, and Defant–Mastyło study **upper** \(L^p\)-norm comparisons and Mahler measure for polynomials on tori. None of these inspected claims gives the sharp *lower* fourth-moment classification for real two-harmonic spaces with freely varying amplitudes.

A published four-consecutive-character result determines a sharp **upper** fourth moment of \(2.808840165\ldots\). A real \(m:3m\) two-tone function can be modulated into a four-consecutive-character analytic polynomial, so that upper theorem is genuinely applicable and is **not** presented here as new. It does not imply the lower constant \(\kappa\) or its unique exceptional-frequency and equality classification. Another published three-frequency resonance theorem fixes *unimodular* coefficients and analyzes when phases first affect even moments; it does not optimize lower fourth moments over the freely weighted symmetric four-mode coefficients arising here. Earlier results in these areas remain a bibliographic risk, especially under waveform-flattening or correlation-energy terminology.

## Limitations
The theorem is limited to real two-tone functions (two independently phased sine-cosine frequency pairs) and the fourth moment with normalized uniform measure. It does not extend the constants to three or more positive frequencies, general compact abelian groups with finite-order aliasing, other exponents, or nonuniform measures. The stability identity is exact, but no optimal universal metric error constant beyond that identity is claimed. Primary literature searches and accessible published-result comparisons cannot exclude all unindexed equivalent historical statements. Independent mathematical audit has not been performed.

## References
1. S. Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first publicly posted 2007-03-08; https://arxiv.org/abs/math/0703236. Full author-hosted text: https://neuwirth.perso.math.cnrs.fr/the-maximum-modulus-of-a-trigonometric-trinomial/maximum-modulus-of-a-trigonometric-trinomial.pdf.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first publicly posted 2013-02-12; https://arxiv.org/abs/1302.2766. Full author-hosted text: https://math.uni-paderborn.de/fileadmin/mathematik/AG-Diskrete_Mathematik/Publications-schmidt/littlewood.pdf.
3. A. Defant and M. Mastyło, *\(L^p\)-Norms and Mahler's Measure of Polynomials on the n-Dimensional Torus*, *Constructive Approximation* 44 (2016), 87–101, first available online 2015-12-14; https://doi.org/10.1007/s00365-015-9319-x (full open-access HTML).
4. *A universal four-mode fourth-moment constant and the sharp seven-point sampling threshold*, publicly accessible mathematical research result (2026); https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-universal-four-mode-fourth-moment-constant-and-the-sharp-seven--92de3bb230cd.
5. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, publicly accessible mathematical research result (2026); https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79.
