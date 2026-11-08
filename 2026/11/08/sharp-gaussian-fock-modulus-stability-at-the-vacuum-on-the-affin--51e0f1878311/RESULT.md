# Sharp Gaussian-Fock modulus stability at the vacuum on the affine Hermite subspace

## Finding
Let \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) be Gaussian probability measure on \(\mathbb C\), and write \(\|H\|_\gamma^2=\int_{\mathbb C}|H|^2d\gamma\) (also for nonholomorphic measurable \(H\)). On the first nontrivial Fock truncation \(E=\operatorname{span}_{\mathbb C}\{1,z\}\), the **optimal global modulus-stability constant at the vacuum** is
\[
\boxed{\sup_{F\in E,\ \||F|-1\|_\gamma>0}\frac{\inf_{|\lambda|=1}\|F-\lambda\|_\gamma}{\||F|-1\|_\gamma}=\sqrt{\frac{2}{2-\sqrt\pi}}=2.964696582853\ldots.}
\]
Equality at a nonzero denominator holds precisely for \(F(z)=e^{i\vartheta}z\) with \(\vartheta\in\mathbb R\). The zero-denominator cases in \(E\) are unimodular constants, for which both sides vanish.

## Assumptions and scope
The reference is the constant function \(1\); competitors are *all* affine entire polynomials \(F(z)=a+bz\), with arbitrary complex \(a,b\), including zero. The numerator minimizes over global phases. The comparison is between unsquared Gaussian \(L^2\)-norms of the complex functions and of their moduli; it is not an intensity-squared estimate. The Gaussian has \(\mathbb E Z=0\), \(\mathbb E|Z|^2=1\), and \(\mathbb E|Z|=\sqrt\pi/2\).

## Proof
**1. Reduction to a one-variable Gaussian modulus mean.** Since \(1,z\) are orthonormal,
\[
\inf_{|\lambda|=1}\|a+bz-\lambda\|_\gamma^2=|a|^2+|b|^2+1-2|a|.
\]
Rotational invariance implies \(\mathbb E|a+bZ|\) depends only on \(|a|\) and \(|b|\). For a nonzero competitor write \(t=(|a|^2+|b|^2)^{1/2}>0\) and \(s=|a|/t\in[0,1]\), and set
\[
m(s)=\mathbb E\left|s+\sqrt{1-s^2}Z\right|.
\]
By \(\mathbb E|s+\sqrt{1-s^2}Z|^2=1\), the squared modulus defect and phase distance are respectively
\[
D^2=t^2+1-2tm(s),\qquad N^2=t^2+1-2ts.
\]
Jensen and strict Cauchy–Schwarz yield \(s\le m(s)<1\) for \(0\le s<1\). Consequently, when \(s<1\),
\[
\frac{N^2}{D^2}=1+\frac{2t[m(s)-s]}{t^2+1-2tm(s)}.
\]
For fixed \(s<1\), the positive function \(t/(t^2+1-2tm(s))\) attains its unique maximum for \(t>0\) at \(t=1\), because its derivative has the sign of \(1-t^2\). Thus the maximum squared ratio at fixed \(s\) is \((1-s)/(1-m(s))\).

**2. The needed strict convexity.** Let \(c_0=\sqrt\pi/2\). For \(0\le s<1\), put \(x=s^2/[2(1-s^2)]\). Evaluation of the Rice mean by angular integration, or by integrating the everywhere convergent power series of \(I_0\), gives
\[
m(s)=c_0\sqrt{1-s^2}\,e^{-x}\big[(1+2x)I_0(x)+2xI_1(x)\big].
\]
Here \(I_0(x)=\sum_{k\ge0}(x/2)^{2k}/(k!)^2\) and \(I_1(x)=\sum_{k\ge0}(x/2)^{2k+1}/[k!(k+1)!]\). The power-series identity is equivalently \(m(s)=c_0\sqrt{1-s^2}\,{}_1F_1(-1/2;1;-s^2/(1-s^2))\). Thus the displayed mean formula is established by absolutely convergent series, not an assumed statistical approximation.

From \(I_0'=I_1\) and \(I_1'=I_0-I_1/x\), direct differentiation gives
\[
m'(s)=c_0\sqrt{2x}\,e^{-x}I_1(x),
\quad m''(s)=c_0(1+2x)^{3/2}e^{-x}\big[2xI_0(x)-(2x+1)I_1(x)\big].
\]
For \(x>0\), let \(q(x)=I_1(x)/I_0(x)\) and \(b(x)=2x/(2x+1)\). Positive-series definitions give \(I_0(x)>0\) and \(q(x)\sim x/2<b(x)\sim2x\) near zero. The Riccati identity \(q'=1-q^2-q/x\) holds. Meanwhile
\[
b'(x)-\left(1-b(x)^2-\frac{b(x)}x\right)=\frac3{(2x+1)^2}>0.
\]
A first-crossing argument therefore gives \(q(x)<b(x)\) for every \(x>0\), whence \(m''(s)>0\) for \(0<s<1\). Continuity yields \(m(0)=c_0\) and \(m(1)=1\). The strict chord inequality now reads
\[
m(s)<c_0+(1-c_0)s\qquad(0<s<1),
\]
with equality at the two endpoints.

**3. Sharp optimum and equality.** Thus \(1-m(s)\ge(1-c_0)(1-s)\), so for \(s<1\)
\[
\frac{N^2}{D^2}\le\frac{1-s}{1-m(s)}\le\frac1{1-c_0}=\frac2{2-\sqrt\pi}.
\]
The second inequality is strict when \(0<s<1\), and the first is an equality only for \(t=1\). When \(s=0,t=1\), the polynomials are exactly \(F(z)=e^{i\vartheta}z\), and their ratio attains the claimed constant. At \(s=1\), the competitor is constant and the ratio equals \(1\) whenever the denominator is nonzero. The zero polynomial likewise has ratio \(1\). This exhausts all cases.

## Verification
`CHECK.py` is a standalone standard-library numerical corroboration, not a replacement for the analytic argument. It independently integrates the Gaussian radial-angular formula, evaluates the Bessel-series mean, verifies the Riccati comparison and several ratio bounds, and checks the sharp extremizing case. Run with `python3 CHECK.py`. The strict inequality for all real parameters is proved above, rather than extrapolated from a finite grid.

## Relationship to prior work
Bertolini, de Dios Pont, Pineau, Taylor and Ramos (2026) prove existence of a finite Gaussian-Fock modulus-stability constant at \(1\) for **all** Fock functions. This result determines the *sharp numerical constant* for the natural first-degree subspace only; their existence theorem, with unspecified best constant, does not imply its value or its equality cases. Bortolotto and Ramos (2026) prove a square-restricted coercivity theorem in Fock space, involving squared analytic competitors and squared moduli; that statement does not determine the present unsquared modulus optimal constant for affine competitors. The classical Rice distribution gives the special-function evaluation of a noncentral complex Gaussian mean, but not the Fock-space extremal optimization over scale and coherent displacement.

## Limitations
No claim is made about the optimal constant on the entire Fock space, at nonconstant reference functions, in higher-degree polynomial subspaces, or for other windows. The result does not provide a sharp noisy-recovery constant outside this two-complex-dimensional model. Publication priority has not been independently established; specialized literature might have an equivalent formulation under Gaussian Rice-mean inequalities.

## References
Bertolini, S., de Dios Pont, J., Pineau, B., Taylor, M. A. and Ramos, J. P. G., *L2-Stability for STFT phase retrieval*, arXiv:2605.20527v1 (submitted 2026-05-19), https://arxiv.org/abs/2605.20527.

Bortolotto, C. and Ramos, J. P. G., *A complex-analytic proof of square-restricted stable phase retrieval in Fock space*, arXiv:2608.26365v1 (submitted 2026-08-26), https://arxiv.org/abs/2608.26365.

Wolfram MathWorld, *Rice Distribution*, https://mathworld.wolfram.com/RiceDistribution.html (formula and background only).
