# A sharp singular-value boundary layer at the Gaussian Fock dilation threshold

## Finding
On the normalized one-dimensional Bargmann–Fock Hilbert space, fix real \(0<a<1\). For real \(t\geq0\), define on entire functions the maximal weighted-composition expression
\[
(T_{a,t}f)(z)=e^{tz^2/2}f(az), \qquad t_*=1-a^2.
\]
For \(0\leq t<t_*\), set
\[
X=(1-a^2)^2-t^2,\quad Y=(1+a^2)^2-t^2,\quad
L=\frac{2}{\sqrt X+\sqrt Y},\quad
q=\frac{\sqrt Y-\sqrt X}{\sqrt Y+\sqrt X}.
\]
Then \(0<q<1\), \(T_{a,t}\) is compact and belongs to every Schatten class, and its **entire** singular-value sequence, indexed from zero and in descending order, is
\[
s_n(T_{a,t})=\sqrt L\,q^{n/2}\quad(n=0,1,2,\ldots).
\]
In particular, for every \(p>0\),
\[
\|T_{a,t}\|_{\mathcal S_p}=\sqrt L\,(1-q^{p/2})^{-1/p},\qquad
\|T_{a,t}\|=\sqrt L,\qquad
\|T_{a,t}\|_{\mathcal S_2}^2=X^{-1/2}.
\]
At the exact threshold, \(T_{a,t_*}\) is bounded, noncompact, and
\[
\|T_{a,t_*}\|=\|T_{a,t_*}\|_{\mathrm{ess}}=a^{-1/2}.
\]
For \(t>t_*\), the maximal expression is not a bounded operator on this space.

A quantitative boundary law accompanies this sharp dichotomy. Write \(\delta=t_*-t\). For every fixed \(U>0\), as \(\delta\downarrow0\),
\[
\sup_{0\leq u\leq U}\left|
 s_{\lfloor u/\sqrt\delta\rfloor}(T_{a,t})
 -a^{-1/2}\exp\!\left(-\frac{\sqrt{2(1-a^2)}}{2a}\,u\right)
\right|\longrightarrow0.
\]
Consequently, for every fixed \(0<\varepsilon<a^{-1/2}\), with \(N_t(\varepsilon)=\#\{n\geq0:s_n(T_{a,t})>\varepsilon\}\),
\[
\lim_{t\uparrow t_*}\sqrt{t_*-t}\,N_t(\varepsilon)
=\frac{a}{\sqrt{2(1-a^2)}}\log\frac{1}{a\varepsilon^2}.
\]
These results concern one **joint** phenomenon: exactly how a compact Gaussian-weighted Fock dilation acquires a noncompact edge while a growing singular-value layer survives.

## Assumptions and scope
The Hilbert-space norm is
\[
\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z),
\]
with orthonormal basis \(e_n(z)=z^n/\sqrt{n!}\), \(n\geq0\). All parameters are real as specified; no claim is made for arbitrary complex quadratic and affine parameters. For \(t>t_*\), “unbounded” means the weighted-composition expression has no bounded everywhere-defined extension.

## Proof
**1. Hilbert–Schmidt regime.** For \(0\leq t<t_*\), Parseval and Tonelli applied to the orthonormal monomials yield
\[
\sum_{n\geq0}\|T_{a,t}e_n\|^2
=\frac1\pi\int_{\mathbb C}
 e^{-(1-a^2)|z|^2+t\operatorname{Re}(z^2)}\,dA(z)
=\frac1{\sqrt{(1-a^2)^2-t^2}}=X^{-1/2}.
\]
Thus the expression on polynomials extends uniquely to a Hilbert–Schmidt operator, and evaluation continuity shows that this extension agrees with the stated weighted composition on all Fock functions.

**2. Gaussian kernel.** Set \(S=T_{a,t}^*T_{a,t}\), and abbreviate
\[
c=(1-t^2)^{-1/2},\qquad b=\frac{a^2}{1-t^2},\qquad d=\frac{a^2t}{1-t^2}.
\]
Here \(b>0\), \(d\geq0\), and \(b+d=a^2/(1-t)<1\). The standard two-variable Gaussian integral, first for real parameters and then by analytic continuation in its linear sources, gives the integral kernel
\[
(Sf)(z)=\frac1\pi\int_{\mathbb C}
 c\exp\!\left(bz\overline w+\tfrac d2(z^2+\overline w^2)\right)
 f(w)e^{-|w|^2}\,dA(w).
\]
Indeed, evaluate \(\int e^{-|w|^2+t(w^2+\overline w^2)/2+pw+q\overline w}\,dA(w)/\pi\) as
\[
(1-t^2)^{-1/2}\exp\!\left(\frac{pq+t(p^2+q^2)/2}{1-t^2}\right)
\]
and use \(p=a\overline w\), \(q=az\) for the reproducing-kernel pairing.

**3. A complete geometric eigenvalue list.** The scalar map
\[
\Phi(v)=d+\frac{v b^2}{1-dv},\qquad 0\leq v\leq1,
\]
is a strict contraction, because \(0<\Phi'(v)=b^2/(1-dv)^2<1\) and \(\Phi(1)<1\). Hence it has a unique fixed point \(v\in[0,1)\). Define
\[
r=\frac b{1-dv}\in(0,1),\qquad A_0=\frac c{\sqrt{1-dv}},\qquad
h=\frac d{(1-dv)(1-r^2)}.
\]
The Fock-valued entire generating family
\[
F_\xi(z)=\exp\!\left(\frac v2z^2+\xi z-\frac h2\xi^2\right)
\]
obeys the exact identity
\[
S F_\xi=A_0 F_{r\xi}.
\]
To check, integrate the kernel against \(F_\xi\); the coefficients of \(z^2\), \(z\xi\), and \(\xi^2\) are respectively \(\Phi(v)/2=v/2\), \(r\), and \(-hr^2/2\). Differentiating in the Fock norm at \(\xi=0\) produces nonzero eigenvectors for the distinct eigenvalues \(A_0r^n\), \(n\geq0\). These vectors are mutually orthogonal because \(S\) is positive and self-adjoint.

A direct substitution into \(v=\Phi(v)\), using \(b=a^2/(1-t^2)\), \(d=tb\), gives
\[
r=\frac{\sqrt Y-\sqrt X}{\sqrt Y+\sqrt X}=q,
\qquad A_0=\frac2{\sqrt Y+\sqrt X}=L.
\]
There is no hidden positive spectral part: the sum of these known eigenvalues is \(L/(1-q)=X^{-1/2}=\operatorname{Tr}S\), already computed in Step 1. Since \(S\) is positive trace class, its residual positive spectrum must vanish. Since \(T_{a,t}\) is injective (both \(a\ne0\) and the exponential weight is nowhere zero), \(S\) has zero kernel; the displayed eigenvectors form a complete orthogonal basis. Taking square roots proves the full singular-value formula and its Schatten consequences.

**4. Critical norm and essential norm.** The formula above gives \(L\uparrow1/a\) as \(t\uparrow t_*\). For each fixed \(f\in\mathcal F^2\), \(T_{a,t}f(z)\to T_{a,t_*}f(z)\) pointwise, and Fatou’s lemma with the uniform norm bound proves \(\|T_{a,t_*}\|\leq a^{-1/2}\). Let \(v_t\) denote the fixed point in Step 3. Then \(v_t\uparrow1\), and
\[
g_t(z)=(1-v_t^2)^{1/4}\exp(v_tz^2/2)
\]
has norm one. Its fixed monomial coefficients vanish as \(t\uparrow t_*\); by density of polynomials, \(g_t\rightharpoonup0\). It is the leading eigenvector of \(S_t\): \(\|T_{a,t}g_t\|^2=L\). All Taylor coefficients of \(g_t\) are nonnegative and so are those of the multipliers \(e^{tz^2/2}\). Comparing coefficients for \(t_*\geq t\) therefore yields
\[
\|T_{a,t_*}g_t\|\geq\|T_{a,t}g_t\|=\sqrt L\longrightarrow a^{-1/2}.
\]
Every compact operator sends the weakly null unit family \(g_t\) to a norm-null family. Thus \(\|T_{a,t_*}\|_{\mathrm{ess}}\geq a^{-1/2}\); the upper norm bound gives equality and noncompactness.

For \(t>t_*\), the adjoint applied to normalized reproducing kernels \(k_x(z)=e^{xz-x^2/2}\), \(x>0\), would have norm
\[
\|T_{a,t}^* k_x\|=
\exp\!\left(\frac{t+a^2-1}{2}x^2\right),
\]
which diverges. Hence no bounded extension exists.

**5. Critical spectral layer.** With \(\delta=t_*-t\downarrow0\),
\[
X=2t_*\delta-\delta^2,\qquad Y\longrightarrow4a^2,\qquad
L\longrightarrow a^{-1},\qquad
-\log q=\frac{\sqrt{2t_*}}a\sqrt\delta+O(\delta).
\]
Insert these expansions into \(s_n=\sqrt L\exp[(n/2)\log q]\). Uniformity for \(n\sqrt\delta\) in a fixed compact interval proves the claimed locally uniform boundary profile. For \(0<\varepsilon<a^{-1/2}\), the threshold inequality \(Lq^n>\varepsilon^2\) counts an initial integer interval of length \(\log(L/\varepsilon^2)/(-\log q)+O(1)\). Multiplication by \(\sqrt\delta\) gives the stated exact limit.

## Verification
An independent finite-section computation uses the explicit monomial matrix
\[
\langle T_{a,t}e_n,e_{n+2k}\rangle
=a^n\frac{(t/2)^k}{k!}\sqrt{\frac{(n+2k)!}{n!}}
\quad(k,n\geq0),
\]
with all other entries zero. The supplied `checker.py` compares its leading singular values with the analytic formula for five interior parameter choices, verifies the geometric root identities and trace/second-moment identities, and checks convergence to the critical counting profile. These are finite diagnostics, not an infinite-dimensional proof. Run with Python 3, NumPy, and SciPy using `python checker.py`.

## Relationship to prior work
Tian (arXiv:2610.29786v1, first posted 21 October 2026, primary MSC 47B38) investigates compactness and invertibility of products involving weighted Fock composition operators; it motivates the present quantitative singular-value question but does not provide this fixed-slope boundary-layer law. Sang and Zhao (arXiv:2608.13832, Section 2.1 and Theorem A) give the exact bounded-versus-compact threshold for the same type of quadratic exponential weight and eigenvector generating functions for the *weighted composition operator itself*. Those are distinct from the orthogonal singular-vector decomposition of its modulus.

Dereziński and Karczmarczyk's general oscillator-semigroup theory supplies broader Gaussian-kernel normal-form, polar-modulus, trace-norm, and operator-norm machinery. It explains the geometric form of the subcritical singular values in principle, and that background is not claimed as new. The present joint claim is the explicit parameter-dependent spectrum together with its *critical noncompact essential norm and sharp locally uniform counting boundary layer* under a fixed-slope deformation; these latter boundary assertions are not stated in the inspected oscillator-semigroup work. General Gaussian-semigroup specialization remains a potential implication/priority risk, so this finding is not an assertion of an entirely new Gaussian diagonalization principle.

## Limitations
The theorem is for one complex dimension, real positive contraction slope, and real nonnegative quadratic amplitude. It does not treat arbitrary affine terms, complex phases, nonlinear weights, or spectra of nonnormal operators themselves. The fixed-slope critical-scale law does not assert a trace-class limit. General oscillator-semigroup theory may furnish an alternate route to the subcritical geometric spectrum, and the extent of any implicit critical-endpoint deductions warrants independent literature review. No independent mathematical audit has been performed.

## References
1. X. Tian, *Weighted composition operators on the Fock space*, arXiv:2610.29786v1 (21 October 2026), https://arxiv.org/html/2610.29786v1.
2. Y. Sang and L. Zhao, *A Characterization of Complex Symmetric Weighted Composition Operators on the Fock Space*, arXiv:2608.13832 (13 August 2026), https://arxiv.org/abs/2608.13832.
3. J. Dereziński and M. Karczmarczyk, *Quantization of Gaussians*, arXiv:1701.07297 (2017), https://arxiv.org/abs/1701.07297; published in *Analysis as a Tool in Mathematical Physics* (2020), pp. 277–304.
4. T. Le, *Normal and isometric weighted composition operators on the Fock space*, *Bull. London Math. Soc.* 46 (2014), 847–856, DOI:10.1112/blms/bdu046.
