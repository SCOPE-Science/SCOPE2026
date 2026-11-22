# Sharp real fourth-power contraction of neighboring averages on the five-cycle

## Finding

Let \(G=\mathbb Z/5\mathbb Z\) have normalized counting measure and let \(M:\mathbb R^G\to\mathbb R^G\) be the symmetric neighboring-average convolution
\[
(Mh)(j)=\frac{h(j-1)+h(j+1)}2.
\]
On the mean-zero subspace \(X=\{h:\sum_{j\in G}h(j)=0\}\), the sharp real \(\ell^4\) contraction is
\[
\boxed{\|Mh\|_4\le C_5\|h\|_4,\quad C_5=0.8634764599843693\ldots.}
\]
Here \(\|h\|_4=(\frac15\sum_{j=0}^4|h(j)|^4)^{1/4}\). Precisely, put
\[
a=\frac{\sqrt5-1}{4},\qquad b=-\frac{\sqrt5+1}{4},
\]
\[
N(r)=6(a^4+b^4r^4)+24a^2b^2r^2-8a^3br-8ab^3r^3,
\]
\[
D(r)=6(1+r^4)+24r^2-8r-8r^3.
\]
Then \(C_5=(N(r_*)/D(r_*))^{1/4}\), where \(r_*\) is the **unique positive real root** of the following explicit sextic:
\[
\begin{aligned}
P(r)={}&(-15-6\sqrt5)r^6+(45+27\sqrt5)r^5\\
&+(-15-3\sqrt5)r^4+19\sqrt5\,r^3\\
&+(15-3\sqrt5)r^2+(-45+27\sqrt5)r\\
&+15-6\sqrt5.
\end{aligned}
\]
Numerically \(r_*=3.62064679016704\ldots\). All nonzero extremizers, and only those, are nonzero real scalar multiples and cyclic translates of
\[
h_*(j)=\cos(2\pi j/5)-r_*\cos(4\pi j/5).
\]
In particular \(C_5>\cos(\pi/5)=0.809016994374947\ldots\), the corresponding mean-zero \(\ell^2\) contraction. Thus its sharp fourth-power behavior is not determined by the spectral radius.

Equivalently, set \(\Delta f(j)=f(j+1)-f(j-1)\). For every real \(f:G\to\mathbb R\),
\[
\left\|\frac{f(\cdot+2)-f(\cdot-2)}2\right\|_4
\le C_5\|f(\cdot+1)-f(\cdot-1)\|_4,
\]
and the same constant is sharp. This is the exact one-coordinate, five-state, fourth-power instance of the neighboring-average convolution bound, not a claim about its optimal dimension-independent constant.

## Assumptions and scope

The theorem is for real-valued functions on the five-element cyclic group, normalized counting measure, and exactly one neighboring-average step. Zero-mean is necessary for the stated contraction; constant functions are fixed by \(M\). The equivalent difference inequality allows arbitrary real inputs because differences have zero mean. No assertion is made for complex-valued functions, arbitrary cycle length, other exponents, or multiple-step optimizers.

## Proof

**Fourier reduction.** Let \(\omega=e^{2\pi i/5}\). Every real mean-zero \(h\) has a unique representation
\[
h(j)=u\omega^j+\overline u\omega^{-j}+v\omega^{2j}+\overline v\omega^{-2j}
\qquad(u,v\in\mathbb C).
\]
The operator \(M\) multiplies \(u\) by \(a=\cos(2\pi/5)\) and \(v\) by \(b=\cos(4\pi/5)\). Orthogonality of the fifth roots of unity, enumerating the seven types of zero-sum quadruples in \(\{1,-1,2,-2\}\), gives exactly
\[
\frac15\sum_{j=0}^4h(j)^4=
6(|u|^4+|v|^4)+24|u|^2|v|^2
+8\operatorname{Re}(u^3v+v^3\overline u).
\]

**Sharp phase reduction.** If neither Fourier coefficient is zero, set \(r=|v|/|u|\), \(E=\cos(3\arg u+\arg v)\), and \(F=\cos(3\arg v-\arg u)\). The fourth-power norm quotient is
\[
\frac{6(a^4+b^4r^4)+24a^2b^2r^2+8a^3brE+8ab^3r^3F}
{6(1+r^4)+24r^2+8rE+8r^3F}.
\]
Its denominator is strictly positive. Its numerator is also strictly positive because \(M\) has no zero multiplier on \(X\). For each fixed \(r>0\), the quotient is strictly decreasing in each of \(E,F\): the numerator slopes are negative while the denominator slopes are positive. The map from the two coefficient phases to the two phases in \(E,F\) is surjective on the two-torus (its integer matrix has nonzero determinant \(10\)). The maximum therefore requires \(E=F=-1\), and equals \(N(r)/D(r)\). The single-mode boundaries are \(a^4\) and \(b^4\).

**Uniqueness of the maximizing amplitude ratio.** Direct expansion gives the exact identity
\[
N'(r)D(r)-N(r)D'(r)=P(r).
\]
Write \(s=\sqrt5\). The coefficients of \((1+t)^6P(4t/(1+t))\), in ascending powers of \(t\), are
\[
15-6s,\quad -90+72s,\quad -435+402s,\quad -540+1984s,\quad -3975+3582s,\quad 38550+30072s,\quad -19125+3574s.
\]
The first six are strictly positive, while the last is strictly negative. Descartes' rule of signs and the endpoint signs show exactly one root in \(0<r<4\). On the other hand, the ascending coefficients of \(P(4+t)\) are
\[
-19125+3574s,\ -38325-2157s,\ -30225-5823s,\ -12240-3389s,\ -2715-903s,\ -315-117s,\ -15-6s,
\]
all strictly negative. Thus \(P(r)<0\) for \(r\ge4\), and \(r_*\) is the unique positive root. The quotient increases up to \(r_*\) and decreases thereafter, so its global maximum is \(N(r_*)/D(r_*)\). Direct substitution shows it exceeds both single-mode boundary values.

**Equality.** The strict phase monotonicity forces \(3\arg u+\arg v\equiv\pi\) and \(3\arg v-\arg u\equiv\pi\) modulo \(2\pi\), while the amplitude ratio is \(r_*\). Consequently \(\arg u=k\pi/5\), \(\arg v=\pi-3k\pi/5\), with \(k\) taken modulo ten. Translation changes \(k\) by two, and multiplication by negative one changes \(k\) by five. These operations act transitively on the ten solutions. Hence precisely the stated scaling-and-translation orbit attains equality.

**Difference formulation.** The operator \(\Delta\) has nonzero multipliers \(2i\sin(2\pi k/5)\) for all nonzero characters. It therefore maps real functions onto \(X\), with constants as its kernel, and \(M\Delta f(j)=[f(j+2)-f(j-2)]/2\). The previous sharp bound is exactly the displayed difference inequality.

## Verification

The bundled `check.py` symbolically verifies the sextic derivative identity, all 14 coefficient signs used in the global root argument, the exact fifth-root frequencies, the quartic resonance count, the numerical root bracket, and a maximizer witness. It also checks 1,200 independently sampled real Fourier coefficient pairs and verifies the difference map's range. The symbolic and finite tests complement the explicit proof; sampling is not used to prove global optimality. Run with `python check.py` using SymPy and NumPy.

## Relationship to prior work

Jiao, Luo, Zanin, and Zhou, *The Strong Naor–Schechtman Convolution Inequality on the Product of Cyclic Groups*, first posted 14 September 2026, prove a dimension-independent bound for every finite product of cycles and \(1\le p<\infty\), with an explicit available constant \(p-1\) for \(p\ge2\). Their Section 2 (including Theorem 2.5 and its proof) uses martingale transforms. The present result instead determines the **optimal modulus-specific real constant** at the first odd cyclic modulus with two distinct nonconstant Fourier multiplier magnitudes, together with all equality cases. A general upper bound does not imply an exact lower constant or its optimizer classification.

Previously published exact fourth-power results for **four-state** cyclic convolutions concern another group order; a published five-state result for the **cyclic Hilbert transform** concerns a different multiplier. Both full published RESULT texts were inspected. The four-state formula is a radical determined by its two-dimensional rotation-dilation block on \(\mathbb Z/4\mathbb Z\); it does not cover the five-point group. The five-state Hilbert result uses a sign Fourier multiplier, the same fifth-root quartic resonance mechanism, and a different exact optimizing quartic \(3t^4-12t^2+8t-9=0\), yielding norm \(1.202320949\ldots\). This shared Fourier reduction is prior technique; neither full theorem determines the present positive neighboring-average multiplier, sextic ratio or equality scale. The discovery searches did not yield an exact five-state neighboring-average formula; this negative search is not a proof of global priority.

## Limitations

The result is a finite five-state, real, one-step theorem. Its exact algebraic specification requires selecting the unique positive sextic root; the decimal values are illustrative. No general sharp \(\ell^4\) contraction formula across all cyclic moduli or claim of optimality in the full multidimensional Naor–Schechtman inequality follows. Possible older treatments in finite-state nonlinear Markov contraction or circulant norm theory remain a bibliographic risk. Independent review has not been performed.

## References

1. Y. Jiao, S. Luo, D. Zanin, D. Zhou, *The Strong Naor–Schechtman Convolution Inequality on the Product of Cyclic Groups*, arXiv:2609.15768, first public version 14 September 2026, https://arxiv.org/abs/2609.15768.
2. A. Naor, G. Schechtman, *Metric \(X_p\) inequalities*, Forum of Mathematics, Pi 4 (2016), e3, as cited and discussed in reference 1.
3. *Exact real \(\ell_4\) contraction factors for every four-state cyclic convolution*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-ell-4-contraction-factors-for-every-four-state-cyclic--4bb94785b883.
4. *Exact fourth-power norm of the order-five cyclic Hilbert transform*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fourth-power-norm-of-the-order-five-cyclic-hilbert-transfo--b6627f6ff641.
