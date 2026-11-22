# Cubic Legendre projection: sharp bounded-variation amplification and a unique central jump

## Finding

Let \(\Pi_3:L^2(-1,1)\to\mathcal P_3\) be the real Lebesgue-\(L^2\) orthogonal projection onto algebraic polynomials of degree at most three. For every real \(f\in BV(-1,1)\),

\[
\operatorname{TV}(\Pi_3 f)\le K_3\operatorname{TV}(f),\qquad
K_3=\frac{15}{4}\sqrt{\frac37}-\frac58=1.829951265154914\ldots .
\]

This is the sharp, attained seminorm. Among inputs with positive variation, equality holds **if and only if** \(f\) agrees almost everywhere with \(c+a\mathbf1_{(0,1)}\) for some real \(c\) and nonzero real \(a\). Thus the unique extremizing jump location is the centre of the interval. The result concerns total variation of the projected function, not pointwise overshoot or an \(L^\infty\) norm.

## Assumptions and scope

All functions are real-valued, identified almost everywhere; total variation means distributional variation \(|Df|((-1,1))\). On smooth polynomials it equals the integral of the absolute derivative. \(\mathcal P_3=\operatorname{span}\{P_0,P_1,P_2,P_3\}\), where \(P_j(1)=1\), and the standard Legendre orthogonality is \(\int_{-1}^1P_jP_k=2\delta_{jk}/(2j+1)\). Every \(BV(-1,1)\) input belongs to \(L^2(-1,1)\). Endpoint values play no role.

## Proof

**1. Reduction to one jump.** For \(-1<t<1\) put \(H_t(x)=\mathbf1_{(t,1)}(x)\) and \(J_t=\Pi_3H_t\). The derivative measure \(\mu=Df\) gives, modulo constants and almost everywhere, \(f(x)=c+\int_{(-1,1)}H_t(x)\,d\mu(t)\). Constants are preserved by \(\Pi_3\), so by linearity and the triangle inequality,

\[
\operatorname{TV}(\Pi_3 f)\le\int_{(-1,1)}\operatorname{TV}(J_t)\,d|\mu|(t)
\le \sup_{-1<t<1}\operatorname{TV}(J_t)\,\operatorname{TV}(f).
\]

A unit step has variation one, hence the supremum is attained if a maximizing jump exists. Reflection exchanges \(t\) and \(-t\), preserving projected variation.

**2. Exact step response.** The coefficient of \(P_j\), for \(1\le j\le3\), in \(J_t\) is \(\big(P_{j-1}(t)-P_{j+1}(t)\big)/2\). Using the first five Legendre polynomials and differentiating gives

\[
q(t,x):=J_t'(x)=\frac{15}{32}(1-t^2)
\left[3-7t^2+8tx+7(5t^2-1)x^2\right].
\]

Thus \(\operatorname{TV}(J_t)=\int_{-1}^{1}|q(t,x)|\,dx\). At the centre, \(q(0,x)=15(3-7x^2)/32\). Its roots are \(\pm\sqrt{3/7}\). Direct integration over the three monotonicity intervals gives \(\operatorname{TV}(J_0)=K_3\).

**3. Strict maximum for jumps close to the centre.** Take \(0\le t\le1/10\) and \(u=t^2\). Here the quadratic \(q(t,\cdot)\) has a negative leading coefficient, is positive at \(x=0\), and is negative at \(x=\pm1\). Hence it has exactly two simple zeros inside \((-1,1)\), with positive values between them. Writing the total signed integral as \(D(u)\) and twice the positive middle integral as \(R(u)\), the quadratic discriminant formula gives

\[
\operatorname{TV}(J_t)=R(u)-D(u),\quad
R(u)=\frac5{196}\frac{(1-u)(245u^2-138u+21)^{3/2}}{(1-5u)^2},\quad
D(u)=\frac58(1-u)(1+7u).
\]

The logarithmic derivative of \(R\) is

\[
\frac{R'(u)}{R(u)}=
\frac{2(1225u^3-1275u^2+315u-9)}{(u-1)(5u-1)(245u^2-138u+21)}.
\]

For \(0\le u\le1/100\) the denominator is strictly positive and the numerator is negative, since \(1225u^3+315u-9\le1225/10^6+315/100-9<0\). Thus \(R\) strictly decreases, while \(D'(u)=5(6-14u)/8>0\). Consequently \(\operatorname{TV}(J_t)<K_3\) whenever \(0<t\le1/10\).

**4. Exact continuum bound for all other jumps.** On every interval \([j/50,(j+1)/50]\), \(j=5,\ldots,49\), substitute \(t=j/50+s/50\) in the degree-four polynomial \(q(t,x)\). Convert its powers of \(s\) into the degree-four Bernstein basis:

\[
q(j/50+s/50,x)=\sum_{k=0}^4 {4\choose k}(1-s)^{4-k}s^k\,b_{j,k}(x),\qquad 0\le s\le1,
\]

where each \(b_{j,k}\) is a rational-coefficient quadratic in \(x\). The Bernstein weights are nonnegative and sum to one. Consequently

\[
\int_{-1}^1|q(j/50+s/50,x)|\,dx
\le\max_{0\le k\le4}\int_{-1}^1|b_{j,k}(x)|\,dx.
\]

The standalone script `checks/cubic_legendre_bv.py` computes all \(45\times5=225\) right-hand sides with exact rational arithmetic, using rational root isolation on each quadratic's monotonicity intervals. Its upper bound includes an explicit conservative root-location error: after 40 bisections, every approximated internal zero has error at most \(2^{-40}\); if \(M=|A|+|B|+|C|\) for \(Ax^2+Bx+C\), the code adds \(4M2^{-40}\) per approximated zero to the sum of absolute antiderivative increments. This bounds the integral on the entire interval, not just at sample points. **Every one of the 225 certified upper bounds is strictly below \(9/5\)**. Finally \(9/5<K_3\) because \(3/7>(97/150)^2\). It follows that all \(t\in[1/10,1]\) have strictly smaller projected variation than \(t=0\), including \(t=1\) by continuity. Reflection covers negative jump positions.

**5. Attainment and rigidity.** The step \(H_0\) has variation one and its projection has variation \(K_3\). For any other \(f\), the bound from step 1 is strict if \(|Df|\) charges any \(t\ne0\), since each such step has strictly smaller variation and the gap is positive pointwise. Equality therefore forces \(|Df|\) to be supported at zero; hence \(Df=a\delta_0\) and \(f=c+aH_0\) almost everywhere. Conversely these functions attain equality if \(a\ne0\).

## Verification

Run `python3 checks/cubic_legendre_bv.py` using Python 3 standard library only. It checks the step-derivative polynomial by a second Legendre-moment reconstruction, the rational strict lower comparison for the central constant, and all 225 Bernstein coefficient integrals as exact rational upper bounds for a continuum of jump positions. The executed checker reports `ALL_CUBIC_LEGENDRE_BV_CERTIFICATES_PASS`. A separate direct evaluation of cubic extrema at ten interior jump positions agreed with the formula but is supplementary. The infinite-dimensional reduction is a mathematical proof via signed derivative measures, not an extrapolation from finite tests.

## Relationship to prior work

Low-degree Legendre projection is classical. Cohen and Tan (2011) derive a general polynomial least-squares approximation framework but do not optimize variation on the BV unit ball. Tagade and Choi (2012) discuss spectral Gibbs oscillations and postprocessing for discontinuities, not the degree-three BV operator norm. Braess, Pillwein and Schöberl (2007 manuscript) construct a different polynomial projector with \(H^1\)/\(L^2\) bounds. Davis and Hagelstein (2021/2022) study universal large-degree Gibbs overshoot constants for orthogonal polynomial expansions; those pointwise asymptotics do not directly determine the fixed-degree total-variation norm or its unique maximizing jump. The precise finite cubic constant and its central-jump rigidity are not supplied by the inspected statements. Historical priority is not independently established.

## Limitations

This is restricted to the real unweighted degree-three Legendre \(L^2\) projection on one interval and distributional first variation. It does not determine the sharp BV norm at any other polynomial degree, under nonuniform weights, or for complex-valued data. Some historical works could not be inspected in full. The exact-rational continuum verification is an essential finite algebraic component of the proof, not a separately independently verified formal proof.

## References

- M. A. Cohen and C. O. Tan, *A Polynomial Approximation for Arbitrary Functions*, arXiv:1108.0608 (first public version 2011-08-02), https://arxiv.org/abs/1108.0608.
- P. M. Tagade and H.-L. Choi, *A Dynamic Bi-orthogonality based Approach for Uncertainty Quantification of Stochastic Systems with Discontinuities*, arXiv:1210.6269 (2012-10-23), https://arxiv.org/abs/1210.6269.
- D. Braess, V. Pillwein and J. Schöberl, *Equilibrated Residual Error Estimates are p-Robust* (manuscript dated 2007-11-24), Section 4, https://www3.risc.jku.at/publications/download/risc_3414/ho_equilibrated.pdf.
- J. M. Davis and P. Hagelstein, *Gibbs phenomena for some classical orthogonal polynomials*, J. Math. Anal. Appl. 505 (2022), 125574, DOI:10.1016/j.jmaa.2021.125574.
- NIST Digital Library of Mathematical Functions, Section 18.3, https://dlmf.nist.gov/18.3.
