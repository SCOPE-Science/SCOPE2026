# Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums

## Finding

For every real \(\omega>0\) and complex coefficients \(a,b,c\), not all zero, put
\[
g(t)=a+b e^{i\omega t}+c e^{-i\omega t},\qquad
\|g\|_{\mathrm{av}}^2=\frac12\int_{-1}^{1}|g(t)|^2\,dt.
\]
Then
\[
|g(1)|^2<9\|g\|_{\mathrm{av}}^2.
\]
The strict inequality is sharp in the uniform sense: the supremum over all positive \(\omega\) and all nonzero coefficient triples is \(9\), approached but not attained. For any fixed \(\omega>0\), let
\[
s=\frac{\sin\omega}{\omega},\quad
A=\frac{1+s\cos\omega}{2}-s^2,\quad
B=\frac{1-s\cos\omega}{2}.
\]
The **exact** squared norm of endpoint evaluation on the three-dimensional space is
\[
K(\omega)=1+\frac{(\cos\omega-s)^2}{A}+\frac{\sin^2\omega}{B}.
\]
Both denominators are positive. All fixed-frequency extremizers are nonzero complex scalar multiples of the explicit real reproducing kernel
\[
h_{\omega}(t)=1+\frac{\cos\omega-s}{A}(\cos(\omega t)-s)
+\frac{\sin\omega}{B}\sin(\omega t).
\]
For every \(\omega>0\), \(K(\omega)<9\), and \(\lim_{\omega\downarrow0}K(\omega)=9\).

## Assumptions and scope

The frequencies are exactly the symmetric triple \(\{-\omega,0,\omega\}\) with arbitrary positive real gap, and the coefficients can be arbitrary complex numbers. No frequency separation bound is assumed. The interval is \([-1,1]\), with **averaged**, not unnormalized, squared \(L^2\) energy. The endpoint is \(t=1\). A common modulation of the whole signal and an affine rescaling transfer the statement to any centered triple and any compact real interval. The result does **not** assert a sharp constant for nonsymmetric triples or for evaluation strictly outside the interval.

## Proof

**Exact fixed-gap norm.** The real functions \(1\), \(C(t)=\cos(\omega t)-s\), and \(S(t)=\sin(\omega t)\) form an orthogonal basis of the complex span of the three exponentials for the inner product \(\langle u,v\rangle=\frac12\int_{-1}^1u(t)\overline{v(t)}dt\). Their squared norms are \(1,A,B\), respectively. They are linearly independent for every \(\omega>0\); hence \(A,B>0\). Endpoint evaluation has squared norm equal to the sum of the squared endpoint values divided by the squared basis norms, which gives \(K(\omega)\). The Riesz representer is exactly \(h_\omega\), and \(h_\omega(1)=\|h_\omega\|_{\mathrm{av}}^2=K(\omega)\). Equality in the fixed-gap estimate occurs if and only if \(g\) is a scalar multiple of \(h_\omega\).

**Odd component is strictly less than three.** Put \(t=2\omega\) and \(H(t)=t(2+\cos t)-3\sin t\). Elementary trigonometric identities show
\[
\frac{\sin^2\omega}{B}<3\quad\Longleftrightarrow\quad H(t)>0.
\]
For \(0<t<3<\pi\),
\[
H'(t)=2\sin(t/2)\bigl(2\sin(t/2)-t\cos(t/2)\bigr)>0,
\]
because \(\tan u>u\) for \(0<u<\pi/2\). Since \(H(0)=0\), this proves positivity on \((0,3)\). For \(t\ge3\), use \(2+\cos t\ge1\) and \(\sin t\le1\) to obtain \(H(t)\ge t-3\ge0\), with strictness at \(t=3\) because \(2+\cos 3>1\). Thus the odd contribution is everywhere strictly less than \(3\).

**Even centered component is strictly less than five.** Define
\[
F(t)=t^2(4-\cos t)+9t\sin t-24(1-\cos t).
\]
A direct expansion of \(A\), \(s\) and \(\cos\omega\) yields the *exact identity*
\[
F(2\omega)=8\omega^2\left(5A-(\cos\omega-s)^2\right).
\]
Thus it suffices to prove \(F(t)>0\) for all \(t>0\). If \(t\ge6\),
\[
F(t)\ge3t^2-9t-48>0,
\]
where the right-hand quadratic is \(6\) at \(t=6\) and strictly increasing thereafter. For \(0<t\le6\), Taylor series cancellation through degree six gives the *exact convergent series*
\[
F(t)=\sum_{n=4}^{\infty}(-1)^n\frac{4(n-2)(n-3)}{(2n)!}t^{2n}.
\]
For \(n\ge5\) the absolute ratios of successive terms are
\[
\frac{t^2(n-1)}{(n-3)(2n+1)(2n+2)}
\le\frac{36\cdot4}{2\cdot11\cdot12}<1.
\]
The alternating tail starting at the positive term \(n=8\) is therefore nonnegative. Retaining terms \(n=4,5,6,7\) gives
\[
F(t)\ge\frac{t^8}{5040}\left(1-\frac{t^2}{30}+\frac{t^4}{1980}-\frac{t^6}{216216}\right)>0.
\]
For the last strict inequality, put \(z=t^2\in[0,36]\). The quadratic \(1-z/30+z^2/1980\) has minimum \(9/20\) at \(z=33\), whereas \(z^3/216216\le36^3/216216<1/4\). Thus the parenthesis is strictly greater than \(1/5\). This proves the even part is strictly smaller than \(5\).

Combining the orthogonal contributions gives \(K(\omega)<1+5+3=9\) for every positive gap, hence the desired strict inequality for every nonzero \(g\).

**Uniform sharpness.** As \(\omega\to0^+\), Taylor expansions give \(s=1-\omega^2/6+O(\omega^4)\), \(A=\omega^4/45+O(\omega^6)\), \(B=\omega^2/3+O(\omega^4)\), \(\cos\omega-s=-\omega^2/3+O(\omega^4)\), and \(\sin\omega=\omega+O(\omega^3)\). The two nonconstant terms in \(K\) approach \(5\) and \(3\). Therefore \(K(\omega)\to9\). The kernels \(h_\omega\) approach \(1+3t+5P_2(t)\) (uniformly on \([-1,1]\)), where \(P_2(t)=(3t^2-1)/2\). This is the degree-two Legendre evaluation kernel at \(t=1\); its endpoint value and averaged squared norm both equal \(9\). Hence the uniform constant cannot be improved. \(\square\)

## Verification

The accompanying `CHECK.py` runs standalone Python standard-library evaluations of the exact trigonometric formula against complex Gram-matrix quadratic forms for many positive gaps, verifies the Taylor-series coefficients as exact fractions, and evaluates near-collision limits using decimal arithmetic for intermediate gaps (small gaps below the normal floating-point conditioning threshold are left to the analytic expansion). It does not replace the proof of global positivity or unrestricted sharpness.

## Relationship to prior work

Zhang (2026), first publicly posted July 11, derives frequency-uniform extrapolation and endpoint estimates for general sparse Fourier sums, including an endpoint \(O(k)\) factor. This does not yield the exact frequency-dependent three-tone evaluation constant, sharp coefficient \(3\) under the stated averaged normalization, or its strict fixed-gap/nonattainment analysis. Erdélyi (2016), Theorem 2.3, proves a general exponential-sum Nikolskii inequality with a larger generic coefficient, and does not settle this exact three-tone case. The classical degree-two Legendre reproducing kernel supplies the sharp collision limit, but does not establish a uniform bound at every positive real gap: the global positivity of the oscillatory analytic quantities \(F\) and \(H\) is required.

## Limitations

Only symmetric equispaced three-frequency supports and endpoint evaluation are treated. This result makes no claim that asymmetric triples have the same sharp bound, and it does not quantify the optimal rate of approach to \(9\) beyond the expansions used in the proof. Originality is based on inspected accessible source text and a comparative search; it is not a proof of publication priority. A separate independent mathematical audit has not been performed.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, version 1 posted July 11, 2026; https://arxiv.org/abs/2607.10501.
2. Tamás Erdélyi, *Inequalities for exponential sums*, arXiv:1602.02315 (2016), especially Theorem 2.3; https://arxiv.org/abs/1602.02315.
3. Classical orthogonality and endpoint reproducing kernels of the Legendre polynomials, for the collision-limit comparison.
