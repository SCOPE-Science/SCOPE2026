# Sharp spectral-gap commutator stability for the two-dimensional Golden–Thompson defect

## Finding
Let \(A,B\) be Hermitian \(2\times2\) matrices. Set \(\mu_A=\operatorname{Tr}(A)/2\), \(\mu_B=\operatorname{Tr}(B)/2\), \(A_0=A-\mu_AI\), and \(B_0=B-\mu_BI\). Suppose \(A_0\) and \(B_0\) have eigenvalues \(\pm r\) and \(\pm s\), respectively, for prescribed \(r,s>0\). Define the scalar-shift-normalized Golden–Thompson defect
\[
\mathcal D(A,B)=e^{-\mu_A-\mu_B}\bigl(\operatorname{Tr}(e^Ae^B)-\operatorname{Tr}(e^{A+B})\bigr).
\]
Put \(a=(r-s)^2\), \(b=(r+s)^2\), \(d=b-a=4rs\), \(f(x)=\cosh\sqrt{x}\), and \(f'(0)=1/2\). Then **the optimal two-sided coefficients for every fixed spectral-gap pair** are
\[
\boxed{C_-(r,s)={f(b)-f(a)-d f'(a)\over d^2},\qquad
C_+(r,s)={d f'(b)-f(b)+f(a)\over d^2}.}
\]
For every such pair,
\[
\boxed{C_-(r,s)\|[A,B]\|_{\mathrm F}^2\le\mathcal D(A,B)
\le C_+(r,s)\|[A,B]\|_{\mathrm F}^2.}
\]
For noncommuting pairs both inequalities are strict and the quotient \(\mathcal D(A,B)/\|[A,B]\|_{\mathrm F}^2\) increases strictly as the cosine of the angle between their traceless Pauli vectors increases from \(-1\) to \(1\). Each coefficient is sharp (approached by noncommuting pairs tending to opposite or aligned commuting directions, respectively). The universal sharp bound \(\mathcal D(A,B)\ge\|[A,B]\|_{\mathrm F}^2/24\) holds in this equal-dimension class for all \(r,s>0\); conversely, no finite coefficient can replace \(C_+(r,s)\) uniformly in unbounded spectral gaps.

## Assumptions and scope
All matrices are over \(\mathbb C\), Hermitian of size \(2\times2\); \(\|\cdot\|_{\mathrm F}\) is the Frobenius/Hilbert–Schmidt norm with unnormalized matrix trace. The two positive parameters \(r,s\) are their **traceless spectral half-gaps**, not their trace norms; independent scalar shifts are removed by the explicit exponential factor. The inequalities include commuting matrices (both sides then vanish). Sharp ratios and strict monotonicity are asserted only when \([A,B]\ne0\). This is not a claim of a uniform upper estimate for arbitrary matrix size or arbitrary spectral gaps.

For a fixed unitary transform, the same result applies separately to each traceless Hermitian \(2\times2\) slice of a transform-based tensor algebra: summing over slices gives the universal lower bound \(\Delta_{\Phi}\ge\mathcal C_{\Phi}/24\), with \(\mathcal C_{\Phi}=\sum_{\omega}\|[A_{\omega},B_{\omega}]\|_{\mathrm F}^2\); if the positive gap pairs are prescribed, an upper bound is \(\sum_{\omega} C_+(r_{\omega},s_{\omega})\|[A_{\omega},B_{\omega}]\|_{\mathrm F}^2\). Zero-gap slices contribute zero. One-slice near-equality proves sharpness of the uniform lower coefficient and of each fixed-gap upper coefficient.

## Proof
**1. Reduction to a divided difference.** Any traceless Hermitian \(2\times2\) matrix is \(v\cdot\sigma\) with \(v\in\mathbb R^3\), where \(\sigma\) denotes the Pauli triple. Put \(A_0=v\cdot\sigma\), \(B_0=w\cdot\sigma\), \(\|v\|=r\), \(\|w\|=s\), and \(u=v\cdot w/(rs)\in[-1,1]\). The Pauli identities give
\[
\operatorname{Tr}(e^{A_0}e^{B_0})=2(\cosh r\cosh s+u\sinh r\sinh s),\qquad
\operatorname{Tr}(e^{A_0+B_0})=2\cosh\sqrt{x},
\]
where \(x=r^2+s^2+2rsu\in[a,b]\). By the hyperbolic addition formulas, the first trace equals twice the affine chord \(L(x)\) through \((a,f(a))\) and \((b,f(b))\). Hence \(\mathcal D=2(L(x)-f(x))\). Also, the Pauli commutator identity yields
\[
\|[A,B]\|_{\mathrm F}^2=8r^2s^2(1-u^2)=2(x-a)(b-x).
\]
Thus for \(-1<u<1\),
\[
{\mathcal D(A,B)\over\|[A,B]\|_{\mathrm F}^2}
={L(x)-f(x)\over(x-a)(b-x)}=f[a,x,b],
\]
where \(f[a,x,b]\) denotes the *second divided difference* at the three displayed nodes. At \(u=\pm1\) both sides of the original inequality vanish; no ratio is asserted there.

**2. Strictly increasing angular quotient.** The entire function \(f(z)=\sum_{k\ge0}z^k/(2k)!\) satisfies \(f''(z)>0\) and \(f'''(z)>0\) for every real \(z\ge0\). The Hermite–Genocchi formula, with \(\mathcal S=\{(t_1,t_2):t_1,t_2\ge0,\ t_1+t_2\le1\}\), gives
\[
f[a,x,b]=\int_{\mathcal S}f''\bigl((1-t_1-t_2)a+t_1x+t_2b\bigr)\,dt_1dt_2.
\]
Differentiating under the integral sign yields the strictly positive derivative
\[
{\partial\over\partial x}f[a,x,b]
=\int_{\mathcal S} t_1 f'''\bigl((1-t_1-t_2)a+t_1x+t_2b\bigr)\,dt_1dt_2>0.
\]
This proves monotonicity and identifies the sharp endpoint constants \(f[a,a,b]\) and \(f[a,b,b]\), equal to the displayed formulas. The endpoints can be approached through any nonzero small Pauli-vector angle from the corresponding commuting configuration.

**3. Scale boundary and sharp universal lower coefficient.** The series of \(f\) gives \(f''(z)\ge f''(0)=1/12\), strictly for \(z>0\). Since \(\mathcal S\) has area \(1/2\), the preceding representation proves \(f[a,x,b]\ge1/24\), strictly for every positive \(r,s\) and noncommuting pair. As \(r,s\to0\), the divided difference tends to \(f''(0)/2=1/24\), so the universal coefficient is optimal.

At matched half-gaps \(s=r\), the optimal constants simplify to
\[
C_-(r,r)={\sinh^2r-r^2\over8r^4},\qquad
C_+(r,r)={r\sinh(2r)-2\sinh^2r\over16r^4}.
\]
As \(r\to\infty\), the first already satisfies \(C_-(r,r)\sim e^{2r}/(32r^4)\), while the second satisfies \(C_+(r,r)\sim (r-1)e^{2r}/(32r^4)\). Therefore every fixed finite universal upper commutator coefficient fails even within this traceless equal-gap \(2\times2\) subclass. This establishes the full stated boundary.

## Verification
The standalone `golden_thompson_check.py` uses rational series coefficients and direct \(2\times2\) matrix multiplication/exponentials to test the chord identity, commutator normalization, strict angular monotonicity, spectral-gap endpoint coefficients, and high-scale growth. Running `python golden_thompson_check.py` produces `PASS 1352 finite assertions`. These finite checks are supplementary: the Hermite–Genocchi identity, Pauli reduction, and positivity of the full power series are the proof for all parameters. In particular, finite tests are not treated as exhaustive coverage of the continuum.

## Relationship to prior work
Chang and Ng (arXiv:2606.21667, first posted 19 June 2026) investigate transform-dependent Golden–Thompson defects and state a dimension-independent, spectral-scale-independent quadratic commutator upper bound in their Theorem 6(i). The present result establishes explicit **sharp spectral-gap-dependent constants** for all Hermitian \(2\times2\) pairs and shows that the scale-free upper comparison cannot hold without additional restrictions. Its tensor-slice consequence uses their block-diagonal reduction only, not their upper estimate.

Forrester and Thompson (arXiv:1408.2008, Section 2.1) derive the Pauli-vector hyperbolic formula underlying the \(2\times2\) Golden–Thompson inequality. Their full formula is acknowledged as prior background; the result claimed here is the **optimized commutator-to-defect quotient for every prescribed two-gap pair**, including strict angular monotonicity, the endpoint divided differences, and the global sharp \(1/24\) boundary. No claim is made to having originated the Pauli representation, the Golden–Thompson inequality, or the Hermite–Genocchi formula.

## Limitations
The theorem concerns Hermitian \(2\times2\) matrices and their two-dimensional tensor slices; no upper statement is made for general matrix size. Sharp coefficients are limiting, not attained at noncommuting endpoint orientations. The bibliographic comparison is not an exhaustive mathematical-priority certification; a previously published equivalent optimization in older matrix-inequality literature could change the originality assessment. An independent audit has not been performed.

## References
1. S.-Y. Chang and M. K. Ng, *Operator Inequalities in \(\Phi\)-Product Tensor Algebras: Invariance and Transform Sensitivity*, arXiv:2606.21667 (first submitted 19 June 2026), https://arxiv.org/abs/2606.21667.
2. P. J. Forrester and C. J. Thompson, *The Golden–Thompson inequality—historical aspects and random matrix applications*, arXiv:1408.2008 (2014), Section 2.1, https://arxiv.org/html/1408.2008v1.
3. W. So, *Equality Cases in Matrix Exponential Inequalities*, SIAM J. Matrix Anal. Appl. 13 (1992), 1154–1158, https://doi.org/10.1137/0613070 (equality criterion).
