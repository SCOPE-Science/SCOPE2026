# A unique resonant gap for sharp midpoint evaluation of symmetric three-frequency Fourier sums

## Finding
For real \(\mu\), real \(\omega>0\) and nonzero complex coefficients \(a,b,c\), define the symmetric three-frequency Fourier sum
\[
f(t)=e^{i\mu t}\bigl(a+b e^{i\omega t}+c e^{-i\omega t}\bigr),\qquad \|f\|_{\mathrm{av}}^2=\frac12\int_{-1}^1|f(t)|^2\,dt.
\]
There is exactly one positive gap \(\omega_*\) which globally maximizes the squared midpoint evaluation factor. Its value and the optimal inequality are
\[
\omega_*=4.9049244571380714153237888366\ldots,\qquad
|f(0)|^2\le K_*\|f\|_{\mathrm{av}}^2,\qquad K_*=4.2673035613955620568264339469\ldots .
\]
The constant is attained, and equality holds exactly when \(\omega=\omega_*\) and \(f\) is a nonzero complex scalar multiple of the explicitly given midpoint reproducing kernel times \(e^{i\mu t}\). In particular, no colliding-frequency or infinite-separation limit is extremizing: the limiting factors are \(9/4\) and \(3\), respectively.

## Assumptions and scope
The spectral support consists of the three distinct, symmetric real frequencies \(\mu-\omega,\mu,\mu+\omega\); amplitudes are arbitrary complex numbers and the common carrier \(\mu\) is arbitrary. The observation interval is exactly \([-1,1]\) with averaged squared energy. Midpoint evaluation is at \(0\), not endpoint or exterior evaluation. An affine rescaling gives the corresponding result for any centered interval, changing the optimal frequency gap inversely with interval half-length. No assertion is made for nonsymmetric frequency triples or other evaluation sites.

For \(w>0\), introduce \(s=\sin w/w\), \(c_w=\cos w\), and the strictly positive quantity
\[
V(w)=1+s c_w-2s^2.
\]
Then the exact fixed-gap squared evaluation norm is
\[
K(w)=1+\frac{2(1-s)^2}{V(w)}.
\]
The extremal centered kernel is
\[
h_w(t)=1+\frac{2(1-s)}{V(w)}\bigl(\cos(wt)-s\bigr),
\]
so that \(h_w(0)=\|h_w\|_{\mathrm{av}}^2=K(w)\). The unique maximizing gap is the unique solution in \((3\pi/2,2\pi)\) to
\[
N(w)=1-2\cos^2w-2\cos w+(5\cos w+1)\frac{\sin w}{w}
+(\cos w-4)\left(\frac{\sin w}{w}\right)^2=0.
\]

## Proof
**Exact Hilbert-space reduction.** Common modulation does not affect either the midpoint magnitude or energy, so take \(\mu=0\). The three functions \(1\), \(C_w(t)=\cos(wt)-s\), and \(S_w(t)=\sin(wt)\) are mutually orthogonal in averaged \(L^2([-1,1])\), with squared norms
\[
1,\quad V(w)/2,\quad (1-s\cos w)/2.
\]
They are linearly independent for every \(w>0\), hence the last two norms are positive. Because \(S_w(0)=0\), evaluation at the midpoint has the squared norm \(K(w)=1+2(1-s)^2/V(w)\). The reproducing kernel is \(h_w\), and Hilbert-space equality in Cauchy–Schwarz implies that exactly its nonzero multiples are fixed-gap norming functions. In particular their positive- and negative-frequency amplitudes are equal.

**Derivative identity.** Direct differentiation, using \(s'=(\cos w-s)/w\), gives
\[
K'(w)=\frac{2(1-s)}{wV(w)^2}N(w).
\]
As \(w>0\), the prefactor is strictly positive, so the signs of \(K'\) and \(N\) agree. The Taylor limit of \(K\) at zero is \(9/4\); this is also the centered degree-two Legendre evaluation kernel limit. At infinity \(s\to0\), giving \(K(w)\to3\).

**Excluding low and distant frequencies.** For positive \(s\), algebra gives
\[
K(w)-3=\frac{2s(3s-2-\cos w)}{V(w)}.
\]
On \(0<w<\pi\), the elementary Cusa–Huygens inequality \(3\sin w/w<2+\cos w\) shows \(K(w)<3\). For completeness, this follows by setting \(H(w)=w(2+\cos w)-3\sin w\), with \(H(0)=0\) and \(H'(w)=2\sin(w/2)[2\sin(w/2)-w\cos(w/2)]>0\) since \(\tan(w/2)>w/2\). On \(2\pi<w<3\pi\), \(0<s\le1/(2\pi)<1/6\), while \(2+\cos w\ge1\), again yielding \(K(w)<3\). On \(w\ge3\pi\), put \(u=|s|\le1/(3\pi)<1/9\); then
\[
K(w)\le1+\frac{2(1+u)^2}{1-u-2u^2}<\frac{27}{7}<4.
\]
But at \(w=3\pi/2\), \(K(w)>4\) (substituting \(s=-2/(3\pi)\), \(\cos w=0\) suffices). Therefore any global maximizer lies between \(\pi\) and \(2\pi\).

**Strict increase until the final quadrant.** On \(\pi<w<3\pi/2\), let \(c=\cos w\in(-1,0)\) and \(s<0\), with \(|s|<1/\pi\). The base \(1-2c^2-2c\) is at least \(1\). If \(c\le-1/5\), the term \((5c+1)s\) is nonnegative, whence \(N(w)>1-5/\pi^2>0\). If \(-1/5<c<0\), then \(N(w)>1-1/\pi-21/(5\pi^2)>0\). Thus \(K\) increases strictly throughout this quadrant.

**Exactly one turning point in the last quadrant.** Now \(3\pi/2<w<2\pi\), so \(c=\cos w\in(0,1)\), \(s<0\), and \(|s|<2/9\). Define \(c_0=(\sqrt3-1)/2<2/5\), the sole zero of \(1-2c^2-2c\) on \([0,1]\). At \(w=3\pi/2\), \(N(w)>1-2/9-16/81=47/81>0\). Whenever \(c\ge c_0\), all three summands in \(N=(1-2c^2-2c)+(5c+1)s+(c-4)s^2\) are nonpositive, with the last two strictly negative, hence \(N<0\).

For \(0\le c<c_0\), write \(N=N(c,s)\). The partial derivatives satisfy
\[
\partial_cN=-4c-2+5s+s^2<-158/81,\qquad
0<\partial_sN=5c+1+2(c-4)s<43/9.
\]
Along the interval, \(c'=\sqrt{1-c^2}>9/10\) and \(0<s'=(c-s)/w<7/50\). Consequently
\[
\frac{dN}{dw}=(\partial_cN)c'+(\partial_sN)s'
<-\frac{158}{81}\frac9{10}+\frac{43}{9}\frac7{50}<0.
\]
There is therefore exactly one zero of \(N\) in this quadrant, with \(N>0\) before it and \(N<0\) afterward. Together with the preceding bounds, this zero is the unique global maximizer of \(K\) over every \(w>0\). Inserting its value into the reproducing kernel gives the stated equality classification. \(\square\)

## Verification
`CHECK.py` is a Python standard-library consistency checker. It verifies the derivative formula against centered differences, the Gram-matrix energy identities against numerical integration for complex coefficients, the reproducing-kernel equality, and numerical bracketing of the unique root. A replay of the package checker passed 1,000 finite assertions. Its finite checks do not prove uniqueness; that conclusion follows from the sign inequalities in the proof.

## Relationship to prior work
Ruizhe Zhang's 2026 *Optimal Extrapolation Bounds for Sparse Fourier Sums* studies arbitrary sparse-frequency sums and establishes universal endpoint/exterior growth and leverage estimates. Those bounds do not resolve the sharp *midpoint* in-domain evaluation factor or optimize it over all symmetric three-frequency gaps. The published *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums* proves the endpoint factor is strictly below \(9\) at positive gaps, approaching \(9\) as the gap collapses; its exact endpoint representer is different from the midpoint representer here, and that endpoint theorem does not imply this finite-gap resonance or its uniqueness. The collision-limit comparison uses classical degree-two Legendre polynomials only as the limiting model and does not give a global inequality in the frequency parameter.

## Limitations
Only symmetric three-frequency supports are treated. The bound pertains to evaluation at the center of an observation interval. The root and constant are specified exactly by the unique transcendental root and analytically proved inequalities; their decimal values are approximations. Unrestricted asymmetric supports and evaluations away from the midpoint are not addressed. An equivalent optimization might appear in older nonharmonic Fourier or reproducing-kernel literature not fully indexed; publication priority is not independently established. No independent mathematical audit has been performed.

## References
1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, version 1 first posted July 11, 2026, https://arxiv.org/abs/2607.10501.
2. *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-endpoint-nikolskii-constant-for-symmetric-three-tone-fouri--e11889d28f9d/RESULT.md.
3. T. Erdélyi, *Inequalities for exponential sums* (2016), arXiv:1602.02315, https://arxiv.org/abs/1602.02315.
