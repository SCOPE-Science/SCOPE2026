# Boundary-induced rank four and two spectral scales for exponential convolution commutators

## Finding
For every length \(L>0\) and two distinct positive rates \(a<b\), let \(E_c:L^2(0,L)\to L^2(0,L)\) be the bounded self-adjoint integral operator
\[
(E_cf)(x)=\int_0^L e^{-c|x-y|}f(y)\,dy \qquad(c>0).
\]
Then the commutator \(K_{a,b,L}=E_aE_b-E_bE_a\) has rank exactly four. Its nonzero eigenvalues, all simple, are \(\pm i d_+\) and \(\pm i d_-\), where \(d_+>d_->0\). Its only other spectral point is zero, and its four nonzero singular values, in decreasing order, are \(d_+,d_+,d_-,d_-\).

Define the reflected exponential functions
\[
U_c^\pm(x)=e^{-cx}\pm e^{-c(L-x)}
\]
and their Gram determinants
\[
G_\pm=\left(\int_0^L(U_a^\pm)^2\,dx\right)\left(\int_0^L(U_b^\pm)^2\,dx\right)
-\left(\int_0^L U_a^\pm U_b^\pm\,dx\right)^2.
\]
The two strictly positive spectral moduli are explicitly
\[
\boxed{d_\pm=\frac{\sqrt{G_\pm}}{2(a+b)}}.
\]
The Gram integrals themselves have closed elementary forms:
\[
\int_0^L(U_c^\pm)^2\,dx=\frac{1-e^{-2cL}}c\pm 2Le^{-cL},
\]
\[
\int_0^L U_a^\pm U_b^\pm\,dx=
\frac{2(1-e^{-(a+b)L})}{a+b}
\pm\frac{2(e^{-aL}-e^{-bL})}{b-a}.
\]
For fixed distinct rates, the interval-length asymptotics are
\[
\boxed{\lim_{L\downarrow0}\frac{d_+}{L^3}=\frac{b-a}{6\sqrt5},\qquad
\lim_{L\downarrow0}\frac{d_-}{L^5}=\frac{ab(b-a)}{120\sqrt{21}}},
\]
while the two modes coalesce at infinite length:
\[
\boxed{\lim_{L\to\infty}d_+=\lim_{L\to\infty}d_-
=\frac{b-a}{2(a+b)^2\sqrt{ab}}}.
\]
Consequently the two full-line convolution operators commute, yet their compressions to every nondegenerate finite interval fail to commute and exhibit a four-dimensional, parity-split boundary defect.

## Assumptions and scope
The Hilbert space is complex \(L^2(0,L)\) with Lebesgue measure; the exponential kernel has **no** probability or covariance normalization factor. Parameters satisfy \(0<a<b<\infty\) and \(L>0\). Interchanging \(a,b\) changes the commutator sign but not its singular values. At \(a=b\), the commutator is zero. The rank statement concerns the infinite-dimensional operator, not a finite-section approximation.

## Proof
**1. Boundary identity.** Extend each exponential kernel to the line as \(k_c(t)=e^{-c|t|}\). Full-line convolutions commute: \(k_a*k_b=k_b*k_a\). For \(0<x,y<L\), the commutator's kernel is therefore the negative of the difference between the two full-line composition integrals over \(( -\infty,0)\) and \((L,\infty)\). These are absolutely convergent. Integrating the four exponential tails gives the exact identity
\[
\begin{aligned}
K_{a,b,L}(x,y)=\frac1{a+b}\bigl[&e^{-bx-ay}-e^{-ax-by}\\
&+e^{-b(L-x)-a(L-y)}-e^{-a(L-x)-b(L-y)}\bigr].
\end{aligned}
\]
This is a continuous antisymmetric real kernel. Writing \(u\otimes v\) for the rank-one operator with kernel \(u(x)\overline{v(y)}\), one gets, exactly,
\[
K_{a,b,L}=\frac1{2(a+b)}\sum_{\varepsilon\in\{+,-\}}
\bigl(U_b^\varepsilon\otimes U_a^\varepsilon
-U_a^\varepsilon\otimes U_b^\varepsilon\bigr).
\]

**2. Rank and singular spectrum.** Reflection \((Rf)(x)=f(L-x)\) is a unitary involution. The two summands above act on its orthogonal even and odd eigenspaces, respectively. In centered coordinates \(t=x-L/2\),
\[
U_c^+(L/2+t)=2e^{-cL/2}\cosh(ct),\qquad
U_c^-(L/2+t)=-2e^{-cL/2}\sinh(ct).
\]
For distinct positive rates, the two hyperbolic cosines are linearly independent, as are the two hyperbolic sines (compare their constant/quadratic and linear/cubic Taylor coefficients). Each parity block is therefore a nonzero skew-adjoint operator of rank two. The elementary identity for two real linearly independent Hilbert-space vectors \(u,v\) states that \(v\otimes u-u\otimes v\) has nonzero eigenvalues \(\pm i\sqrt{\|u\|^2\|v\|^2-|\langle u,v\rangle|^2}\). Applying it separately to the two blocks gives rank four, the asserted spectrum, and the formula for \(d_\pm\).

**3. Strict parity ordering.** For \(0<s<t\le L/2\), define
\[
C=\cosh(at)\cosh(bs)-\cosh(as)\cosh(bt),\quad
S=\sinh(at)\sinh(bs)-\sinh(as)\sinh(bt).
\]
Since \(b>a>0\), both \(\cosh(bt)/\cosh(at)\) and \(\sinh(bt)/\sinh(at)\) increase strictly with \(t>0\); thus \(C<0\) and \(S<0\). In addition,
\[
C-S=\cosh(at-bs)-\cosh(as-bt)<0,
\]
because \((as-bt)^2-(at-bs)^2=(b-a)(a+b)(t^2-s^2)>0\). Hence \(C^2>S^2\) on a set of positive measure. Each Gram determinant equals one-half of the double integral of the squared two-by-two evaluation determinant, and the even/odd symmetry reduces these double integrals to the same positive multiple of the corresponding integrals of \(C^2\) or \(S^2\), with an identical positive exponential prefactor. Thus \(G_+>G_->0\) and \(d_+>d_-\).

**4. Short-interval expansion.** On \(|t|\le L/2\), uniformly as \(L\downarrow0\),
\[
\cosh(ct)=1+\frac{c^2t^2}{2}+O(L^4),\qquad
\sinh(ct)=ct+\frac{c^3t^3}{6}+O(L^5).
\]
The leading exterior-product coefficients of the even and odd function pairs are respectively \(2(b^2-a^2)(1\wedge t^2)\) and \(\tfrac{2ab}{3}(b^2-a^2)(t\wedge t^3)\). Here \(f\wedge g\) denotes the exterior square of two \(L^2[-L/2,L/2]\) vectors. Exact moments yield
\[
\|1\wedge t^2\|^2=\frac{L^6}{180},\qquad
\|t\wedge t^3\|^2=\frac{L^{10}}{33600}.
\]
The common scalar factors \(e^{-(a+b)L/2}\) tend to one. Dividing these wedge norms by \(2(a+b)\) proves the cubic and quintic limits in the Finding. The Taylor remainders are uniform on the shrinking interval and contribute lower-order wedge terms.

**5. Long-interval expansion.** Since left- and right-boundary exponentials become asymptotically orthogonal,
\[
\|U_c^\pm\|_2^2\longrightarrow\frac1c,\qquad
\langle U_a^\pm,U_b^\pm\rangle\longrightarrow\frac{2}{a+b}.
\]
Consequently \(G_\pm\to 1/(ab)-4/(a+b)^2=(b-a)^2/[ab(a+b)^2]\); substitution in the exact Gram formula proves both long-interval limits.

## Verification
The accompanying `verify.py` checks the tail-integration identity using independent piecewise quadrature, both parity Gram formulas and their strict ordering for sampled rates and intervals, the two moment identities exactly as rational fractions, short- and long-window limits numerically, and the four nonzero singular values of a Nyström discretization. It passed 63 assertions or check groups. The analytic proof above, not finite numerical evidence, establishes the statements for all admissible parameters and all interval lengths. Run with `python verify.py` (Python 3, `mpmath`; `numpy` enables the optional finite-matrix comparison).

## Relationship to prior work
Full-line convolution commutativity and general integral-kernel commutation criteria are discussed by Djinja, Silvestrov and Tumwesigye (2023). Castrigiano (2020, subsequently published 2021) studies rational-symbol Wiener–Hopf operators on the half-line and their domain, Fredholm and spectral properties. The truncated finite-interval convolution setting and finite-rank exponential-symbol characterizations appear in Andersson and Carlsson (2015). Their individual finite-rank symbol characterization is not a rank formula for a commutator of two infinite-rank compressions; the present result adds an exact four-eigenvalue spectrum, strict parity ordering, and two different sharp powers as the interval shrinks. Classical compression-product/Hankel identities explain why finite boundary rank can occur but do not, without the present calculations, determine the two moduli and their coefficients. No claim is made that the general finite-rank compression mechanism is novel.

## Limitations
Only real positive distinct decay rates and a single finite interval are covered. The result does not characterize arbitrary exponential mixtures, nonstationary kernels, higher dimensions, or nonuniform windows. The exact parity Gram representation is elementary to evaluate numerically but need not simplify to an elementary closed expression for arbitrary rates. Historical-priority verification against older specialist Wiener–Hopf identities remains incomplete; the mathematical comparison distinguishes the specific spectral and two-scale statements from the inspected general operator results.

## References
1. D. Djinja, S. Silvestrov and A. B. Tumwesigye, *Volterra integral operators and general linear integral operators representing polynomial covariance type commutation relations on \(L_p\) spaces*, arXiv:2305.13603, publicly posted 23 May 2023, https://arxiv.org/abs/2305.13603.
2. D. P. L. Castrigiano, *Unbounded Wiener–Hopf Operators and Isomorphic Singular Integral Operators*, arXiv:2002.08116, publicly posted 19 February 2020, https://arxiv.org/abs/2002.08116.
3. F. Andersson and M. Carlsson, *On General Domain Truncated Correlation and Convolution Operators with Finite Rank*, Integral Equations and Operator Theory 82 (2015), 339–370, https://doi.org/10.1007/s00020-015-2217-6.
