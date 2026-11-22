# A negatively skewed limiting law for the power-scale Abelian complexity of a binary automatic word

## Finding
Let \(s(n)\) be the number of base-four digits equal to three in \(n\), reduced modulo three, and let \(b(n)=\mathbf 1_{\{s(n)=0\}}\). Define \(A_m=\rho_b^{\mathrm{ab}}(4^m)\), the number of distinct Parikh vectors among the length-\(4^m\) contiguous factors of the infinite binary word \(b\). Write
\[
\rho=\sqrt7,\qquad \theta=\arctan(\sqrt3/5),\qquad
\Phi(t)=\max_{a=0,1,2}\cos(t-2\pi a/3)-\min_{a=0,1,2}\cos(t-2\pi a/3).
\]
Define the continuous periodic function
\[
H(t)=2\sum_{j=1}^\infty\rho^{-j}\Phi(t-j\theta).
\]
Then the empirical measures of the *normalized* Abelian-complexity values \(X_m=A_m/\rho^m\) converge weakly:
\[
\frac1M\sum_{m=0}^{M-1}\delta_{X_m}\ \Longrightarrow\ \nu=H_*\operatorname{Unif}[0,\pi/3].
\]
The law is nondegenerate, supported on the exact compact interval \([\min H,\max H]\), and has the absolutely and uniformly convergent Fourier representation
\[
H(t)=\frac{6\sqrt3}{\pi}\sum_{\ell\in\mathbb Z}
\frac{e^{6i\ell t}}{(1-36\ell^2)(\rho e^{6i\ell\theta}-1)}.
\]
Its first two moments are explicit:
\[
\boxed{\mathbb E_\nu X=\frac{6\sqrt3}{\pi(\sqrt7-1)}=2.01000804331\ldots,}
\]
\[
\boxed{\operatorname{Var}_\nu(X)=\frac{216}{\pi^2}\sum_{\ell=1}^\infty
\frac{1}{(36\ell^2-1)^2(8-2\sqrt7\cos(6\ell\theta))}
=0.00193216222\ldots.}
\]
Moreover the *third centered moment is strictly negative*, with the fully reproducible interval
\[
\boxed{-0.00005710<\mathbb E_\nu[(X-\mathbb EX)^3]<-0.00003609.}
\]
In particular the limiting fluctuation law is not symmetric about its mean. The exact phase representation and its accumulation interval are already accessible from prior recurrences; the finding is the explicit distributional/moment refinement and certified negative asymmetry.

## Assumptions and scope
The word \(b\) is infinite and one-sided with indices starting at zero. Its binary coding is \(b(n)=1\) precisely when the count of digit three in the base-four representation of \(n\) is divisible by three. A length-\(n\) factor is contiguous, and its Abelian class is determined by its one-count. The empirical limit samples *exponents* \(m\) uniformly, not all factor lengths \(n\) uniformly. The scaling is \(7^{m/2}\), not \(4^m\). All series and numerical bounds refer to this exact word.

## Proof
**1. Exact phase recurrence.** The substitution on \(\mathbb Z/3\mathbb Z\), \(\sigma(a)=aaa(a+1)\), generates the ternary digit-three counter, and the binary coding picks its zero symbol. Allouche--Rampersad--Rigo--Shallit--Stipulanti prove, with \(A_0=2\), that
\[
A_{m+1}-A_m=3g_m,\quad g_m=\max_aN_m(a)-\min_aN_m(a),
\quad N_m(a)=\frac{4^m+2\rho^m\cos(m\theta-2\pi a/3)}3.
\]
Consequently \(A_{m+1}-A_m=2\rho^m\Phi(m\theta)\). The series defining \(H\) converges uniformly since \(\rho>1\), and satisfies
\[
\rho H(t+\theta)-H(t)=2\Phi(t).
\]
Induction, including the initial condition at \(m=0\), gives the exact identity
\[
A_m=\rho^mH(m\theta)+2-H(0).\tag{1}
\]
The paper also proves \(\theta/\pi\) irrational. Thus \(m\theta\pmod{\pi/3}\) is uniformly distributed, while the error \((2-H(0))/\rho^m\) in \(X_m\) tends to zero. The continuous mapping theorem for equidistributed rotations (or elementary Cesàro averaging of continuous test functions) proves the stated weak limit. Since \(H\) is continuous, its image is an interval. Since \(\Phi\) is nonconstant, the functional equation makes \(H\) nonconstant. Hence the interval is nondegenerate, and its full image is the support of \(\nu\).

**2. Fourier coefficients.** The range of three equally spaced cosines is \(\pi/3\)-periodic. For the representative satisfying \(|t-\pi/6|\le\pi/6\), one has \(\Phi(t)=\sqrt3\cos(t-\pi/6)\). Integration against the \(\pi/3\)-periodic characters gives
\[
\widehat\Phi(\ell)=\frac3\pi\int_0^{\pi/3}\Phi(t)e^{-6i\ell t}\,dt
=\frac{3\sqrt3}{\pi(1-36\ell^2)}\qquad(\ell\in\mathbb Z).
\]
In particular \(\widehat\Phi(0)=3\sqrt3/\pi\). The coefficients decay quadratically, so the Fourier series is absolutely and uniformly convergent. Summing the geometric series in the defining expression for \(H\) yields
\[
\widehat H(\ell)=\frac{2\widehat\Phi(\ell)}{\rho e^{6i\ell\theta}-1}
=\frac{6\sqrt3}{\pi(1-36\ell^2)(\rho e^{6i\ell\theta}-1)}.
\]
This proves the claimed Fourier representation. Integrating gives the stated expectation. Parseval applied to \(H-\widehat H(0)\) gives
\[
\operatorname{Var}_\nu(X)=2\sum_{\ell=1}^\infty|\widehat H(\ell)|^2,
\]
which simplifies to the displayed positive, absolutely convergent variance series because \(|\rho e^{6i\ell\theta}-1|^2=8-2\rho\cos(6\ell\theta)>0\). Consequently the law is not a point mass.

**3. Certified asymmetric third moment.** Let \(\mu=\widehat H(0)\), \(P=\pi/3\), and \(H_K(t)=2\sum_{j=1}^{K}\rho^{-j}\Phi(t-j\theta)\). The bounds \(3/2\le\Phi\le\sqrt3\) imply \(3/(\rho-1)\le H\le2\sqrt3/(\rho-1)\), and hence \(|H-\mu|<0.3\). Since the maximum and minimum of 1-Lipschitz functions are each 1-Lipschitz, \(\Phi\) is 2-Lipschitz and \(H\) is \(4/(\rho-1)\)-Lipschitz. Therefore \(t\mapsto(H(t)-\mu)^3\) is \(0.657\)-Lipschitz.

For \(K=24\), the uniform tail bound is
\[
|H-H_K|\le\frac{2\sqrt3\rho^{-24}}{\rho-1}<1.521\cdot10^{-10}.
\]
For \(N=16384\), take midpoints \(t_j=(j+1/2)P/N\). The average of the exact centered cube differs from the midpoint average of \((H_K(t_j)-\mu)^3\) by at most
\[
\frac{0.657P}{4N}+3(0.301)^2\frac{2\sqrt3\rho^{-24}}{\rho-1}
<1.0499\cdot 10^{-5}.\tag{2}
\]
The executable `verify_waveform.py` evaluates that finite sum with 60-decimal precision, independently obtained \(\pi=16\arctan(1/5)-4\arctan(1/239)\), \(\theta=\arctan(\sqrt3/5)\), and a 20-term cosine series after reducing its argument to \([-\pi/6,\pi/6]\). The arctangent alternating-series error is less than \(2\cdot10^{-90}\), the cosine error less than \(8\cdot10^{-60}\), and the accumulated decimal-rounding error is conservatively below \(10^{-15}\). It obtains midpoint value \(-0.0000465936779147\ldots\). Bound (2), including a \(10^{-15}\) numerical allowance, places the exact moment between \(-0.000057092\) and \(-0.000036095\), which implies the displayed wider strict bounds and proves the sign. The finite quadrature is an *error-controlled evaluation of a proved integral*, not an extrapolation from finite random experiments.

## Verification
Run `python3 verify_waveform.py` in a standard Python 3 environment. It independently generates all length-\(4^m\) windows of every ordered pair of \(m\)-level substitution blocks for \(0\le m\le5\), checks the published complexity values through exponent nine, evaluates the exact Fourier variance series, and carries out the explicit high-precision certified-sign quadrature. Its corresponding captured output is `verification_output.txt`. Every ordered pair of ternary letters occurs in the infinite substitution word; hence the nine-pair enumeration truly covers all infinite-word factors at the checked lengths. The infinite statements follow from the algebraic and harmonic-analysis proof, not from those finite tests.

## Relationship to prior work
Allouche, Rampersad, Rigo, Shallit and Stipulanti, arXiv:2610.03837 (publicly posted 2026-10-02), establish the nonregular binary example, the exact recurrence for \(A_m\), and irrationality of \(\theta/\pi\). Those are credited as inputs, not claimed as new. Their entire 12-page HTML text, including Sections 3--4, was read and compared: it proves nonperiodicity of parity, but states no empirical limiting distribution, explicit variance or third-moment sign.

The related published published-finding corpus finding *An infinite nonregular abelian-complexity family with interval-valued power-scale limits* (2026-10-26, identifier `7b09e62adf22`) treats the same morphism *for exponents at least four* and provides a continuous phase function and its full accumulation interval; its `RESULT.md` was read. Its method helps explain formula (1) for the exponent-three word but it does not give the normalized empirical law, Fourier coefficients, any exact distributional moments, or a certified asymmetry. The novelty here is only the latter statistical refinement, not existence of a phase function or interval.

The related published-finding corpus finding *An infinite ternary-morphism family with nonregular binary abelian complexity* (2026-11-02, identifier `f292807a24e1`) establishes nonregularity for exponents at least four, not this moment law. Broader general abelian-complexity results, including Couvreur et al. (arXiv:2504.13584), do not report the present distribution for this specific non-Pisot example. The literature and indexed-record searches found no explicit equivalent of the mean/variance/skewness triple. Such absence is not proof of absolute priority; undiscovered results and unindexed notes remain risks.

## Limitations
This theorem describes only length scales \(4^m\) and uniform sampling in \(m\); it does not describe the distribution for every integer factor length. The support endpoints are characterized as exact extrema of \(H\), not computed in closed elementary form. The limiting probability measure is a pushforward of uniform phase; no claim of absolute continuity of this measure is made. The numerical interval certifies only the third moment's negative sign, not high-accuracy identification of its decimal expansion beyond the stated wide interval.

## References
1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837, first public 2026-10-02, especially Sections 2--4. https://arxiv.org/html/2610.03837v1
2. *An infinite nonregular abelian-complexity family with interval-valued power-scale limits*, published published-finding corpus mathematical record (2026-10-26), identifier `7b09e62adf22`, `RESULT.md`. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-an-infinite-nonregular-abelian-complexity-family-with-interval-v--7b09e62adf22
3. *An infinite ternary-morphism family with nonregular binary abelian complexity*, published published-finding corpus mathematical record (2026-11-02), identifier `f292807a24e1`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-infinite-ternary-morphism-family-with-nonregular-binary-abeli--f292807a24e1
4. J. Couvreur, M. Delacourt, N. Ollinger, P. Popoli, J. Shallit, M. Stipulanti, *Effective computation of generalized abelian complexity for Pisot type substitutive sequences*, arXiv:2504.13584, first public 2025-04-22. https://arxiv.org/abs/2504.13584
