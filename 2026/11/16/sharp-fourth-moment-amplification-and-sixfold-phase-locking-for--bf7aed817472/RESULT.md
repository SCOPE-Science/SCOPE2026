# Sharp fourth-moment amplification and sixfold phase locking for four cyclic Fourier characters

## Finding

Let \(G=\mathbb Z/6\mathbb Z\) have normalized counting measure, let \(\omega=e^{2\pi i/6}\), and let
\[
 f(n)=c_0+c_1\omega^n+c_2\omega^{2n}+c_3\omega^{3n},\qquad (c_0,c_1,c_2,c_3)\in\mathbb C^4.
\]
There is a unique positive root \(\rho\) of
\[
 \rho^3+3\rho^2-3\rho-2=0,\qquad \rho=1.145102691200422\ldots.
\]
For every coefficient vector the **sharp fourth-moment inequality** is
\[
 \boxed{\frac16\sum_{n=0}^5|f(n)|^4\le C_6\left(\sum_{j=0}^3|c_j|^2\right)^2,\quad C_6=\frac{3\rho^4+4\rho^3+12\rho^2+4}{2(1+\rho^2)^2}=2.892164358578031\ldots.}
\]
All nonzero equality cases are precisely
\[
 \boxed{(c_0,c_1,c_2,c_3)=\lambda(1,\rho\eta,\rho\eta^2,\eta^3),\qquad \lambda\in\mathbb C\setminus\{0\},\quad\eta^6=1.}
\]
Thus precisely six complex-projective directions attain equality. The coefficient phase circle that is available without modular quadratic aliasing collapses to six allowed translations on the six-cycle.

## Assumptions and scope

The input spectrum is exactly the four *allowed* characters with frequency indices \(\{0,1,2,3\}\) modulo six; coefficients may vanish. The group has six points, Haar probability is uniform, and the input norm is \(\sum_j|c_j|^2\) by Parseval. The fourth moment is the fourth power of the output \(L^4\) norm. The theorem is not about the operator's \(\ell^\infty\) projection norm, other cyclic orders, phase-only coefficients, or higher moments. No unproved extrapolation to those cases is made.

## Proof

**1. The exact cyclic correlation formula.** Extend the coefficient sequence by zero to six slots. Write \(E=\sum_{j=0}^3|c_j|^2\) and its cyclic autocorrelations
\[
 R_1=c_1\overline{c_0}+c_2\overline{c_1}+c_3\overline{c_2},\qquad
 R_2=c_2\overline{c_0}+c_3\overline{c_1},\qquad
 R_3=c_3\overline{c_0}+c_0\overline{c_3}.
\]
Orthogonality of the six characters and \(R_{6-k}=\overline{R_k}\) give the **identity**
\[
 \frac16\sum_{n=0}^5|f(n)|^4
 =E^2+2|R_1|^2+2|R_2|^2+|R_3|^2.\tag{1}
\]
The third correlation is a real sum of two conjugate terms, specifically because \(3\equiv-3\pmod6\). This extra torsion collision is the source of the equality-phase rigidity.

**2. Sharp magnitude symmetrization.** Define
\[
 A=|c_0|^2+|c_3|^2,\qquad B=|c_1|^2+|c_2|^2,\qquad E=A+B.
\]
Cauchy–Schwarz, the arithmetic–geometric mean inequality, and the triangle inequality yield
\[
 |R_1|\le\sqrt{AB}+B/2,\qquad |R_2|\le\sqrt{AB},\qquad |R_3|\le A.\tag{2}
\]
For example \(|c_0c_1|+|c_2c_3|\le\sqrt{AB}\), \(|c_1c_2|\le B/2\), and \(|c_0c_3|\le A/2\). These inequalities are **simultaneously attained** for every fixed \(A,B\ge0\) by choosing the real nonnegative symmetric vector
\[
 (c_0,c_1,c_2,c_3)=(\sqrt{A/2},\sqrt{B/2},\sqrt{B/2},\sqrt{A/2}).
\]
Consequently the supremum for fixed \(E\) is exactly the one-variable maximum obtained by substituting the bounds (2) into (1), not merely an upper estimate.

**3. Exact one-variable optimization.** For \(A>0\) set \(t=\sqrt{B/A}\ge0\). Dividing the resulting bound by \(E^2\) yields
\[
 F(t)=\frac{3t^4+4t^3+12t^2+4}{2(1+t^2)^2},\qquad
 F'(t)=-\frac{2t(t^3+3t^2-3t-2)}{(1+t^2)^3}.\tag{3}
\]
The cubic \(p(t)=t^3+3t^2-3t-2\) has exactly one positive zero: its coefficient signs have one variation, \(p(0)=-2\), and \(p(t)\to+\infty\). Thus \(F\) strictly increases up to \(\rho\), then strictly decreases. The endpoint values \(F(0)=2\) and \(\lim_{t\to\infty}F(t)=3/2\) are smaller. This proves the asserted global sharp constant and guarantees that every extremizer has \(A,B>0\).

**4. All equality phases.** At the strictly positive maximizing values of \(A,B\), equality in \(2|c_0c_3|\le A\) requires \(|c_0|=|c_3|=\sqrt{A/2}\). Equality in \(2|c_1c_2|\le B\) and the Cauchy–Schwarz parts then forces \(|c_1|=|c_2|=\sqrt{B/2}\). Hence the magnitudes are proportional to \((1,\rho,\rho,1)\).

Because all magnitudes are nonzero, triangle equality in \(R_1\) forces the three phase differences \(\arg(c_1/c_0)\), \(\arg(c_2/c_1)\), and \(\arg(c_3/c_2)\) to be equal modulo \(2\pi\). Thus \(c_j=\lambda a_j e^{ij\theta}\), with amplitudes \((a_0,a_1,a_2,a_3)=(1,\rho,\rho,1)\). The inequality \(|R_3|\le A\) is an equality only when \(e^{6i\theta}=1\), i.e. \(\theta\in(\pi/3)\mathbb Z\). These constraints also saturate \(R_2\) and every earlier inequality. Conversely, every listed vector saturates (1)–(3). Thus the six projective possibilities are both necessary and sufficient.

## Verification

`artifacts/verify.py` is standalone standard-library Python. It checks the cyclic correlation formula against exact rational convolution in 1,600 cases; checks the Cauchy–Schwarz/AM–GM input inequalities on 6,000 integer cases; compares the direct discrete Fourier average to the autocorrelation formula and the sharp upper bound on 4,600 complex tests; and checks all six equality-phase witnesses. It also verifies the rational bracketing signs for the cubic's unique positive root. The exact derivation in the proof, not the finite tests, establishes the universal inequality and equality characterization.

## Relationship to prior work

The recent finite \(\Lambda(p)\) selection theorem of Burstein, Iosevich, and Krause (first public September 11, 2026) motivates asking for exact finite Fourier amplification constants, but concerns large-system probabilistic selection rather than this fixed four-character computation. The published four-consecutive-character symmetrization theorem gives an all-even-moment magnitude reduction **on the continuous circle**, and calculates a sharp sixth moment; its premise does not cover the additional opposite-frequency collision modulo six, and its complex equality phases differ here. The published three-character finite-cyclic \(\Lambda(4)\) classification and the co-singleton classification handle, respectively, smaller Fourier supports and the four-out-of-five case, but do not imply the four-out-of-six result. The published four-frequency endpoint projection-norm formula concerns \(\ell^1/\ell^\infty\) operator bounds, not this coefficient-\(\ell^2\)-to-output-\(L^4\) constant. The subgroup-hole fourth-moment identity treats complements of whole Fourier subgroups and does not cover the complementary pair \(\{4,5\}\) in \(\mathbb Z/6\mathbb Z\), which is not a subgroup coset of order two.

## Limitations

Only the sixth-cycle, its indicated four-character frequency set, and the fourth moment are classified. A theorem under an older equivalent finite-dimensional norm or two-hole Fourier-space description might exist, despite the targeted searches and inspected close results; absolute priority is not certified. The motivating 2026 source was available for its full abstract but not its full main text, so no whole-document noncoverage claim is made. The printed decimals are approximations to exact algebraic quantities. No independent audit has been performed.

## References

1. W. Burstein, A. Iosevich and B. Krause, *Bourgain's \(\Lambda(p)\) selection theorem: a greedy proof with polynomial failure bounds*, arXiv:2609.12566v1, first submitted 2026-09-11, https://arxiv.org/abs/2609.12566 .
2. *Sharp sixth-moment Fourier norm via four-term even-moment symmetrization*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moment-fourier-norm-via-four-term-even-moment-symmet--f3e238ebf219 .
3. *Exact \(\Lambda(4)\) constants for every three-character subset of a cyclic group*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lambda-4-constants-for-every-three-character-subset-of-a-c--5562292e7127 .
4. *Sharp \(\Lambda(4)\) constant for the co-singleton spectrum of a finite abelian group*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lambda-4-constant-for-the-co-singleton-spectrum-of-a-finit--dba95505302c .
5. *Exact four-frequency Fourier projection norm on every cyclic group*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-four-frequency-fourier-projection-norm-on-every-cyclic-gro--6fefdbed98ba .
6. *Exact two-scale fourth-moment deficit for subgroup-hole Fourier spectra*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fourth-moment-norm-and-deficit-for-a-subgroup-hole-in-a-fi--7e5381608851 .
