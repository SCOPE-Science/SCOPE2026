# Exponential edge-layer amplification in Krawtchouk sign interpolation

## Finding

For each integer \(m\ge1\), let \(F_{2m}\) be the complete Krawtchouk Fourier expansion, equivalently the unique polynomial of degree at most \(2m\), interpolating \(\operatorname{sgn}(j)\) at all integer nodes \(-m\le j\le m\), where \(\operatorname{sgn}(0)=0\). It is odd and in fact has degree at most \(2m-1\).

**Theorem (fixed-gap and logarithmic edge layers).** For every fixed \(u\in(0,1)\),
\[
(-1)^m F_{2m}(m-u)
\sim \frac{4^m}{m^{u+5/2}}
\frac{-1}{2^{u+1}\sqrt\pi\,\Gamma(-u)}.
\]
The convergence of the ratio is uniform for \(u\) in any compact subinterval of \((0,1)\). In particular the displayed coefficient is strictly positive. More sharply, for every \(0<a<b<\infty\), uniformly over \(t\in[a,b]\),
\[
\lim_{m\to\infty}
\frac{m^{5/2}\log m}{4^m}
(-1)^m F_{2m}\left(m-\frac{t}{\log m}\right)
=\frac{t e^{-t}}{2\sqrt\pi}.
\]
Consequently the sharp maximum **of this limiting logarithmic boundary-layer profile** occurs at \(t=1\), with value \(1/(2e\sqrt\pi)\). In particular, the global norm on the interpolation interval has the rigorous lower bound
\[
\liminf_{m\to\infty}
\frac{m^{5/2}\log m}{4^m}
\max_{|x|\le m}|F_{2m}(x)|
\ge \frac{1}{2e\sqrt\pi}.
\]
No matching global upper bound or global maximizer classification is asserted.

## Assumptions and scope

The scalar Krawtchouk basis uses \(N=2m\) equally spaced nodes and arbitrary admissible binomial weight parameter; using the complete basis yields the same unique interpolating polynomial. The domain of the maximum is the growing real interval \([-m,m]\), and the edge coordinate is the **unscaled lattice distance** \(u=m-x\). All limits are along positive integer \(m\to\infty\). The second limit is uniform only for \(t\) bounded away from zero and infinity. The scale in the last inequality is a lower bound, not an assertion of equality.

## Proof

**1. Exact polynomial and boundary normalization.** Put
\[
W_m(x)=\prod_{j=-m}^{m}(x-j),\qquad
r_{m,k}=\frac{\Gamma(m+1)^2}{\Gamma(m+k+1)\Gamma(m-k+1)}.
\]
The derivative \(W_m'(k)=(-1)^{m-k}(m+k)!(m-k)!\), so pairing the elementary Lagrange basis functions at \(k\) and \(-k\) gives the identity
\[
F_{2m}(x)=\frac{(-1)^m W_m(x)}{(m!)^2}
\sum_{k=1}^m\frac{2(-1)^k k r_{m,k}}{x^2-k^2}.
\tag{1}
\]
The poles are removable by interpolation. For \(x=m-u\) with \(0<u<1\), the product has the exact Gamma representation
\[
W_m(m-u)=\frac{\Gamma(2m+1-u)}{\Gamma(-u)}.
\]
Write
\[
T_m(u)=\sum_{k=1}^m(-1)^k k r_{m,k}
\frac{(m-u)^2}{(m-u)^2-k^2}.
\]
Equation (1) becomes
\[
F_{2m}(m-u)=
(-1)^m\frac{2\Gamma(2m+1-u)}{
\Gamma(-u)\Gamma(m+1)^2(m-u)^2}T_m(u).
\tag{2}
\]

**2. Alternating central-binomial lemma.** We prove
\[
T_m(u)=-\frac14+O(m^{-1/2}),
\tag{3}
\]
uniformly either for \(u\) in any fixed compact subset of \((0,1)\), or for \(u=t/\log m\) with \(t\in[a,b]\subset(0,\infty)\). All constants may depend on these ranges.

For \(0\le s\le m/2\), extend \(r_{m,k}\) smoothly by
\[
r_m(s)=\frac{\Gamma(m+1)^2}{\Gamma(m+s+1)\Gamma(m-s+1)}.
\]
The logarithmic derivative identities
\[
(\log r_m)'(s)=\psi(m+1-s)-\psi(m+1+s),
\quad
(\log r_m)''(s)=-\psi'(m+1-s)-\psi'(m+1+s)
\]
and standard series bounds for the positive trigamma function give, uniformly on this interval,
\[
0<r_m(s)\le e^{-c s^2/m},\quad
| (\log r_m)'(s)|\le Cs/m,\quad
|(\log r_m)''(s)|\le C/m,\quad
|(\log r_m)'''(s)|\le C/m^2
\]
for absolute \(c,C>0\) and all sufficiently large \(m\). Let \(\chi\) be a fixed smooth cutoff equal to one on \([0,1/3]\) and zero on \([1/2,\infty)\). Define
\[
a_m(s)=\chi(s/m)\,s\,r_m(s)
\frac{(m-u)^2}{(m-u)^2-s^2}\quad(s\ge0),
\]
with zero extension beyond the cutoff. The rational denominator is uniformly separated from zero on its support for \(m\ge2\). Differentiating three times and putting \(v=s/\sqrt m\), the preceding bounds give
\[
|a_m'''(s)|\le C m^{-1}(1+v^6)e^{-cv^2}
+Cm^3 e^{-cm}\mathbf1_{[m/3,m/2]}(s).
\]
Thus \(\int_0^\infty|a_m'''(s)|\,ds=O(m^{-1/2})\). Also \(a_m(0)=0\), \(a_m(1)=1+O(m^{-1})\), and \(\Delta^2 a_m(0)=O(m^{-1})\), where \(\Delta a(k)=a(k+1)-a(k)\).

For a finitely supported sequence \(a(k)\), exact index shifts give
\[
\sum_{k\ge0}(-1)^k a(k)
=\frac{a(0)}2-\frac{\Delta a(0)}4
+\frac14\sum_{k\ge0}(-1)^k\Delta^2 a(k).
\tag{4}
\]
Elementary summation by parts bounds the last alternating sum by \(|\Delta^2a(0)|+\sum_k|\Delta^3 a(k)|\), and the integral formula for finite differences bounds the latter sum by \(3\int_0^\infty|a'''(s)|ds\). Therefore the cutoff sum equals \(-1/4+O(m^{-1/2})\).

Finally, since \(r_{m,k}\le e^{-c k^2/m}\) for \(k\le m\), the omitted tail \(k\ge m/3\) is \(O(m^3\log m\,e^{-cm})\) in the logarithmic regime (and exponentially small for fixed \(u\) away from \(0,1\)). Here the possible near-endpoint denominator at \(k=m\) is explicitly bounded using \(u\ge a/\log m\). This establishes (3), including its uniformity.

**3. Gamma asymptotics and the scale transition.** Uniformly for \(u\in[0,1/2]\), Stirling's ratio formula gives
\[
\frac{\Gamma(2m+1-u)}{\Gamma(m+1)^2}
=\frac{4^m(2m)^{-u}}{\sqrt{\pi m}}
\bigl(1+O(m^{-1})\bigr).
\]
Substitution of (3) into (2) proves the fixed-gap assertion (the same uniform Gamma estimate holds on compact subsets of \((0,1)\)). For \(u=t/\log m\), use
\[
-\Gamma(-u)^{-1}=u\bigl(1+O(u)\bigr),\qquad
m^{-u}=e^{-t},\qquad 2^{-u}=1+O(u).
\]
This gives the locally uniform boundary-layer law. The function \(t e^{-t}\) has its unique maximum at \(t=1\). Evaluating the polynomial at that point proves the lower bound on the full-interval supremum, without requiring any estimate elsewhere in the expanding interval.

## Verification

`checker.py` uses exact rational arithmetic and two independent interpolation formulas: barycentric Lagrange weights and the paired nodal-product formula (1). It verifies 96 interpolation identities, 100 exact alternating-binomial first-moment identities and six fixed-edge asymptotic comparisons. The checker runs with Python's standard library. These finite calculations are supplementary; the infinite limits follow from the uniform alternating-difference estimate and Stirling's formula above. In particular the code does not certify a global maximum on the expanding interval.

## Relationship to prior work

Cullinan and Young (2026) establish that the full Krawtchouk projection of the sign function is its unique equispaced interpolating polynomial, and prove the fixed-origin derivative limit \(\log4\). The separately published *The exact limiting Gibbs overshoot for Krawtchouk interpolation of the sign function* determines local-uniform convergence on **fixed complex compact sets** and the limiting first-lobe maximum about \(1.06578\), explicitly without controlling the finite-degree maxima on expanding intervals. Neither of those results implies the present exponential lower bound or the exact moving-edge scaling: convergence on compact sets has no bearing on \(x=m-t/\log m\). Classical Runge instability and equispaced Lagrange weights are acknowledged as established general background; the quantitative specific-sign edge-layer constant is the contribution here.

## Limitations

No global matching upper bound, asymptotic global location, or uniqueness of the finite-polynomial maximizer is established. The profile maximum at \(t=1\) is only within the displayed logarithmic boundary layer, not necessarily the global maximum. In particular, pointwise fixed-origin convergence is fully compatible with exponentially growing norms on the expanding interpolation intervals. The assertion covers the complete Krawtchouk Fourier expansion, not its degree-truncated projections.

## References

- J. Cullinan and E. Young, *The Gibbs phenomenon for the Krawtchouk polynomials*, arXiv:2603.05408v1, publicly posted March 5, 2026. https://arxiv.org/abs/2603.05408
- *The exact limiting Gibbs overshoot for Krawtchouk interpolation of the sign function*, published mathematical result, November 2, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-exact-limiting-gibbs-overshoot-for-krawtchouk-interpolation--95d6218c0f0c
- NIST Digital Library of Mathematical Functions, §3.3, Lagrange interpolation and equally spaced cardinal weights. https://dlmf.nist.gov/3.3
