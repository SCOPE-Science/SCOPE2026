# Sharp superquadratic two-mode circle sampling with an overestimation transition

## Finding
Let \(2<p<4\), let \(m\ge2\) be an integer, and let \(z_j=e^{i(\tau+2\pi j/m)}\), \(0\le j<m\), for any fixed real \(\tau\). On the complex two-dimensional subspace \(\operatorname{span}_{\mathbb C}\{1,z\}\subset L^p(\mathbb T)\), define the normalized continuous and sampled \(p\)-moments
\[
I_p(a,b)=\frac{1}{2\pi}\int_0^{2\pi}|a+be^{i\theta}|^p\,d\theta,
\qquad Q_{m,p,\tau}(a,b)=\frac1m\sum_{j=0}^{m-1}|a+bz_j|^p.
\]
Set \(s=p/2\in(1,2)\). The **exact worst relative moment error** for every integer \(m\ge2\) is
\[
\boxed{\sup_{(a,b)\ne(0,0)}\left|\frac{Q_{m,p,\tau}(a,b)}{I_p(a,b)}-1\right|
=E_{m,p}:=-\frac{2\Gamma(1+s)^2\sin(\pi s)}{\pi}
\sum_{\ell=1}^{\infty}\frac{\Gamma(\ell m-s)}{\Gamma(\ell m+s+1)}.}
\]
The series is positive and absolutely convergent. **Every and only** extremizing nonzero pair satisfies \(|a|=|b|>0\) and \(a+bz_j=0\) for at least one sampling node. At every extremizer, the sampled moment **overestimates** the integral: \(Q/I-1=E_{m,p}>0\). An underestimate never reaches the same absolute error.

For fixed \(2<p<4\), the sharp large-grid asymptotic is
\[
\boxed{E_{m,p}\sim -\frac{2\Gamma(1+s)^2\sin(\pi s)}{\pi}\,\zeta(p+1)m^{-(p+1)}\quad(m\to\infty).}
\]
At the cubic-moment exponent \(p=3\) the infinite Gamma series has the exact finite trigonometric evaluation, for every \(m\ge2\),
\[
\boxed{E_{m,3}=\frac{3\pi}{16m}\left(3\cot\frac{\pi}{2m}-\cot\frac{3\pi}{2m}\right)-1.}
\]
In particular \(E_{2,3}=3\pi/8-1\) and \(E_{3,3}=3\sqrt3\pi/16-1\). At the upper exponent boundary there is an exact sampling resonance:
\[
\lim_{p\uparrow4}E_{2,p}=\frac13,
\qquad\lim_{p\uparrow4}E_{m,p}=0\quad(m\ge3).
\]
At the lower boundary \(p\downarrow2\), \(E_{m,p}\to0\) for every \(m\ge2\). This gives the opposite signed error from the known subquadratic exponent regime, together with a distinct two-node fourth-moment transition.

## Assumptions and scope
All integrals use normalized Haar probability measure on the unit circle. The coefficients are complex and need not be real or normalized, provided they are not both zero. Sampling nodes are the complete regular \(m\)-gon with equal weights, and the error concerns \(p\)-th moments (not their \(p\)-th roots). The sharp theorem holds strictly for \(2<p<4\), all integers \(m\ge2\), and arbitrary sampling rotation. The boundary limits are given separately; the theorem does not assert the same equality classification at the endpoint exponents.

## Proof
**1. Normalize the coefficient geometry.** Write \(M=|a|^2+|b|^2>0\) and \(r=2|ab|/M\in[0,1]\). Choosing a phase \(\varphi\) gives
\[
|a+be^{i\theta}|^p=M^s(1+r\cos(\theta+\varphi))^s.
\]
For vanishing individual coefficients take \(r=0\). By arithmetic–geometric mean, \(r=1\) exactly when \(|a|=|b|>0\). Put \(F_r(\theta)=(1+r\cos\theta)^s\) and
\[
c_k(r)=\frac1{2\pi}\int_0^{2\pi}F_r(\theta)e^{-ik\theta}\,d\theta,
\qquad k\in\mathbb Z.
\]
These coefficients are real with \(c_{-k}=c_k\), and \(c_0(r)>0\).

**2. Establish the superquadratic Fourier sign and strict normalized-coefficient growth.** The Chebyshev–Rodrigues identity and \(k\) integrations by parts, valid initially for \(0<r<1\), give for every integer \(k\ge1\)
\[
c_k(r)=\frac{s(s-1)\cdots(s-k+1)}{\pi(2k-1)!!}
\int_{-1}^1r^k(1-u^2)^{k-1/2}(1+ru)^{s-k}\,du.
\tag{1}
\]
All boundary terms vanish: every derivative of order below \(k\) of \((1-u^2)^{k-1/2}\) vanishes at \(u=\pm1\). For \(1<s<2\), the falling factorial has sign \((-1)^k\) for **every \(k\ge2\)**. Thus \(c_k(r)\ne0\) and
\[
\operatorname{sgn}c_k(r)=(-1)^k\quad(k\ge2,\ 0<r\le1).
\tag{2}
\]
The endpoint \(r=1\) follows by dominated convergence in (1), since near \(u=-1\) the integrand is proportional to \((1+u)^{s-1/2}\), which is integrable.

For \(k\ge2\) (hence \(k>s\)), logarithmic differentiation of the strictly positive integrand in the absolute value of (1) gives
\[
\frac{\partial}{\partial r}\log\bigl[r^k(1+ru)^{s-k}\bigr]
=\frac{k+sru}{r(1+ru)}\ge\frac{k+sr}{r(1+r)}.
\tag{3}
\]
The inequality holds because the expression in \(u\) is strictly decreasing when \(k>s\), so its minimum on \([-1,1]\) occurs at \(u=1\). Integrating the positive weighted average yields
\[
\frac{d}{dr}\log|c_k(r)|\ge\frac{k+sr}{r(1+r)}.
\tag{4}
\]
Although \(c_0(r)\) is *increasing* (unlike in the subquadratic regime), its logarithmic growth is controlled:
\[
\frac{d}{dr}\log c_0(r)=
\frac{\int_{-1}^{1}(1+ru)^s\,\frac{su}{1+ru}\,(1-u^2)^{-1/2}\,du}
{\int_{-1}^{1}(1+ru)^s(1-u^2)^{-1/2}\,du}
\le\frac{s}{1+r},
\tag{5}
\]
using the pointwise bound \(u/(1+ru)\le1/(1+r)\). Combining (4)–(5),
\[
\frac{d}{dr}\log\frac{|c_k(r)|}{c_0(r)}\ge\frac{k}{r(1+r)}>0
\quad(0<r<1,\ k\ge2).
\tag{6}
\]
In particular every relevant relative alias coefficient increases strictly to its value at \(r=1\). This additional normalized-growth estimate is essential when \(s>1\); the subquadratic proof based on decreasing \(c_0\) does not apply.

**3. Alias and optimize every coefficient and phase simultaneously.** For \(r<1\), \(F_r\) is analytic in a strip and has absolutely summable Fourier coefficients. At \(r=1\), the beta-integral formula below yields \(|c_k(1)|=O(k^{-2s-1})\), so Fourier series and discrete aliasing are valid there as well. Therefore
\[
\frac{Q_{m,p,\tau}(a,b)}{I_p(a,b)}-1
=\frac{2}{c_0(r)}\sum_{\ell\ge1}c_{\ell m}(r)
\cos\bigl(\ell m(\tau+\varphi)\bigr).
\tag{7}
\]
Since \(m\ge2\), every \(\ell m>s\), and (6) gives
\[
\left|\frac{Q}{I}-1\right|
\le\frac{2}{c_0(r)}\sum_{\ell\ge1}|c_{\ell m}(r)|
\le\frac{2}{c_0(1)}\sum_{\ell\ge1}|c_{\ell m}(1)|.
\tag{8}
\]
The last bound is strict for \(0\le r<1\). At \(r=1\), (2) gives \(\operatorname{sgn}c_{\ell m}(1)=(-1)^{\ell m}\). If the pair has a zero at a sample, then \(\tau+\varphi\equiv\pi-2\pi j/m\pmod{2\pi}\), hence
\[
\cos(\ell m(\tau+\varphi))=(-1)^{\ell m}\quad\text{for all }\ell\ge1.
\]
Every term in (7) is then strictly positive, and (8) is attained as an **overestimate**. Conversely equality in (8) requires \(r=1\), and equality in the first triangle inequality forces each cosine to have absolute value one with a common signed orientation. Positive orientation of the \(\ell=1\) term forces precisely the sample-zero phase. Negative orientation is impossible: the second alias \(c_{2m}(1)\) is positive, while imposing the opposite orientation on the first alias forces \(\cos(2m(\tau+\varphi))=1\). This proves both sharpness and the complete equality classification, including \(m=2\).

**4. Evaluate the constant.** The beta integral yields, for every integer \(k\ge0\),
\[
c_k(1)=2^{-s}\frac{\Gamma(2s+1)}{\Gamma(s-k+1)\Gamma(s+k+1)}.
\]
The reflection formula gives for all \(k\ge2\)
\[
\frac{|c_k(1)|}{c_0(1)}=
-\frac{\Gamma(s+1)^2\sin(\pi s)}{\pi}\,
\frac{\Gamma(k-s)}{\Gamma(k+s+1)}.
\]
Substitute this into (8), yielding the exact Gamma series in the finding. The gamma-ratio asymptotic \(\Gamma(x-s)/\Gamma(x+s+1)\sim x^{-(2s+1)}\), with a summable uniform power majorant for \(x\ge2\), proves the large-\(m\) law by dominated convergence.

**5. Cubic benchmark and exponent boundaries.** At \(p=3\) and a balanced zero-on-grid polynomial, the sample values are (up to a common rotation) \(8\sin^3(\pi j/m)\) and the circle mean equals \(32/(3\pi)\). The identities
\[
\sin^3x=\tfrac14(3\sin x-\sin 3x),\qquad
\sum_{j=1}^{m-1}\sin\frac{k\pi j}{m}=\cot\frac{k\pi}{2m}\quad(k=1,3)
\]
prove the finite cotangent formula. For \(m=2\) at arbitrary \(2<p<4\), one zero sample and one nonzero sample give the alternative closed form
\[
E_{2,p}=\frac{\sqrt\pi\,\Gamma((p+2)/2)}{2\Gamma((p+1)/2)}-1.
\]
It converges to \(1/3\) as \(p\uparrow4\). For any fixed \(m\ge3\), the Gamma-series terms remain finite as \(s\uparrow2\) and the prefactor \(-\sin(\pi s)\) vanishes, so \(E_{m,p}\to0\). The same prefactor gives \(E_{m,p}\to0\) as \(s\downarrow1\) for every \(m\ge2\), because then all \(\ell m-s>0\). The endpoint behavior is thus fully established.

## Verification
`CHECKER.py` is a standalone Python standard-library diagnostic. It evaluates the Gamma series against direct balanced-grid moments for 42 choices of exponent and node count, tests 3,150 additional nonbalanced, randomly phased coefficient geometries, checks the cubic cotangent identity on 39 node counts, and checks fourth-moment boundary quadrature for 33 counts; it reports `SUPERQUADRATIC_CIRCLE_SAMPLING_DIAGNOSTIC_OK 3307`. These finite computations corroborate specific formulas, but **do not establish the universal quantifiers or the infinite-series identity**. Those follow from the preceding analytic argument. Gamma-series truncation in the checker is used only for these supplementary numerical comparisons.

## Relationship to prior work
Dai and Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)* (first public 4 November 2026), and Dai, Kosov and Murasko, *Empirical approximation of \(L_p\) norms for \(p\in(2,\infty)\)* (first public 6 November 2026), establish probabilistic discretization and sample-complexity estimates for general finite-dimensional \(L^p\) spaces in the respective exponent ranges. The latter paper includes sharpness examples for discrete coordinate spaces. Neither theorem evaluates exact relative errors for a fixed deterministic regular grid on complex two-mode circle polynomials, nor their equality cases. A publicly available 2026 result titled *Sharp two-mode \(L^p\) circle sampling distortion and zero-on-grid extremizers* establishes the subquadratic \(1<p<2\) analogue, with the **opposite underestimate orientation**. The present theorem is the new complementary nonconcave range and requires the normalized-growth inequality (6) because the constant Fourier mode now increases rather than decreases. The two-node resonance at exponent four and the finite cubic cotangent expression are additional new features of this branch. General Marcinkiewicz–Zygmund polynomial sampling inequalities and classical periodic Fourier aliasing provide context but do not by themselves determine this precise constant and all its extremizers.

## Limitations
No conclusion is claimed for arbitrary sampling nodes or weights, higher-degree polynomial subspaces, the one-node case, or general exponents \(p>4\). At integer exponent four, the relative-error structure changes for the two-node grid; only its limit from below is asserted. The comparison with available primary papers, public research records, and indexed sampling literature leaves a residual risk of an unindexed equivalent sharp two-mode quadrature theorem.

## References
1. F. Dai and E. Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)*, arXiv:2611.05930v1, 4 November 2026, https://arxiv.org/abs/2611.05930.
2. F. Dai, E. Kosov and N. Murasko, *Empirical approximation of \(L_p\) norms for \(p\in(2,\infty)\)*, arXiv:2611.08896v1, 6 November 2026, https://arxiv.org/abs/2611.08896.
3. *Sharp two-mode \(L^p\) circle sampling distortion and zero-on-grid extremizers*, public 2026 mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-two-mode-l-p-circle-sampling-distortion-and-zero-on-grid-e--62ae1c7fdc6a.
4. L. N. Trefethen and J. A. C. Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), 385–458, https://doi.org/10.1137/130932132.
5. J. Marzo and K. Seip, *The Kadets \(1/4\) theorem for polynomials*, arXiv:0712.3478, 2007, https://arxiv.org/abs/0712.3478. Background on Marcinkiewicz–Zygmund polynomial sampling, not a claim of the sharp constant here.
