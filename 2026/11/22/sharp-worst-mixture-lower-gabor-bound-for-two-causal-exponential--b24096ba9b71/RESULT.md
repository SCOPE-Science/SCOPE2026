# Sharp worst-mixture lower Gabor bound for two causal exponentials at every integer redundancy

## Finding

Fix \(a,b>0\) with \(a\ne b\), an integer \(q\ge2\), and a complex coefficient \(c\). For the causal two-rate window
\[
g_c(t)=(e^{-at}-c e^{-bt})\mathbf1_{[0,\infty)}(t)
\]
consider the Gabor family
\[
\mathcal G_q(c)=\{e^{2\pi i mt}g_c(t-n/q):m,n\in\mathbb Z\}.
\]
Let \(A_q(c)\) denote its *optimal lower squared-analysis frame bound*: the greatest number \(A\) such that
\[
A\|f\|_2^2\le \sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i mt}g_c(t-n/q)\rangle|^2
\quad(f\in L^2(\mathbb R)).
\]
Define
\[
\rho=e^{-a/q},\quad\sigma=e^{-b/q},\quad
U=\sum_{j=0}^{q-1}\rho^{2j},\quad
V=\sum_{j=0}^{q-1}\sigma^{2j},\quad
W=\sum_{j=0}^{q-1}(\rho\sigma)^j.
\]
Then the **sharp worst-mixture lower bound**, over *all complex* secondary amplitudes, is
\[
\boxed{\inf_{c\in\mathbb C} A_q(c)
=\frac{\rho^2}{(1+e^{-a})^2}\left(U-\frac{W^2}{V}\right)>0.}
\]
Its *only* minimizing amplitude is the positive real number
\[
\boxed{c_* =\frac{\rho}{\sigma}
\frac{1+e^{-b}}{1+e^{-a}}\frac{W}{V}.}
\]
This gives a universal quantitative guarantee against arbitrarily destructive complex interference between the two decay channels. In contrast, at critical density \(q=1\), a suitable coefficient produces a Zak zero and the optimal worst-mixture bound is zero.

The deterioration at coalescing rates is also sharp. For fixed \(b>0\) and \(q\ge2\), set
\[
S_k=\sum_{j=0}^{q-1}j^k e^{-2bj/q},\qquad k=0,1,2.
\]
As \(a\to b\),
\[
\boxed{\inf_c A_q(c)=\frac{e^{-2b/q}}{q^2(1+e^{-b})^2}
\left(S_2-\frac{S_1^2}{S_0}\right)(a-b)^2
+O_{b,q}(|a-b|^3).}
\]
The coefficient is strictly positive. At fixed distinct \(a,b\), the large-redundancy law is
\[
\boxed{\lim_{q\to\infty}\frac1q\inf_c A_q(c)
=\frac{1}{(1+e^{-a})^2}
\left[\frac{1-e^{-2a}}{2a}
-\frac{\left(\frac{1-e^{-(a+b)}}{a+b}\right)^2}{\frac{1-e^{-2b}}{2b}}\right]>0.}
\]
The stated constants are optimal, not merely sufficient.

## Assumptions and scope

Use the Lebesgue \(L^2(\mathbb R)\) norm, modulation \(M_mf(t)=e^{2\pi i mt}f(t)\), and translation \(T_{n/q}f(t)=f(t-n/q)\). The first exponential has fixed complex amplitude \(1\); only the relative amplitude \(c\) is varied. Window values at the discontinuity \(t=0\) are irrelevant. No assumption is made on the phase or magnitude of \(c\). The rates are positive and distinct, so the two sampled exponential vectors are linearly independent for each integer \(q\ge2\). The word *sharp* refers to the infimum over coefficients of the **optimal** Gabor lower bound, not to a determination of the optimal bound at every individual coefficient.

## Proof

**1. Exact integer-redundancy Zak multiplier.** Adopt the unitary (for Lebesgue fundamental-domain measure) Zak transform
\[
Zg(x,\omega)=\sum_{k\in\mathbb Z}g(x+k)e^{-2\pi i k\omega},
\qquad 0\le x,\omega<1.
\]
For every integer \(q\ge1\), Fourier orthogonality of integer modulations and the \(q\) translation residue classes gives the frame multiplier
\[
F_{q,c}(x,\omega)
=\sum_{j=0}^{q-1}|Zg_c(x+j/q,\omega)|^2,
\qquad 0<x<1/q,\quad0\le\omega<1.
\]
The optimal lower frame bound is its essential infimum. Indeed, translations of size \(n/q\) split into \(n=q\ell+j\); the integer shifts yield Zak Fourier characters in \(\omega\), while the integer modulations give characters in \(x\). Parseval on the Zak torus gives this multiplier with **no extra factor of \(q\)**. This normalization is independently checked by the window \(\mathbf1_{[0,1)}\), for which the multiplier is exactly \(q\).

For \(0<y<1\) and \(z=e^{-2\pi i\omega}\), a geometric series yields
\[
Zg_c(y,\omega)=\frac{e^{-ay}}{1-e^{-a}z}
-c\frac{e^{-by}}{1-e^{-b}z}.
\]
Put \(u=e^{-ax}/(1-e^{-a}z)\) and \(v=c e^{-bx}/(1-e^{-b}z)\). Thus
\[
F_{q,c}=\sum_{j=0}^{q-1}|\rho^j u-\sigma^j v|^2
=U|u|^2+V|v|^2-2W\operatorname{Re}(u\overline v)
=V\left|v-\frac{W}{V}u\right|^2
+\left(U-\frac{W^2}{V}\right)|u|^2.
\]

**2. Strict positivity and universal sharp lower bound.** The sampled vectors \((\rho^j)_{j=0}^{q-1}\) and \((\sigma^j)_{j=0}^{q-1}\) are linearly independent because \(q\ge2\) and \(\rho\ne\sigma\). Strict Cauchy–Schwarz yields \(\Delta=U-W^2/V>0\). In the Zak fundamental strip, \(0<x<1/q\),
\[
|u|^2=\frac{e^{-2ax}}{|1-e^{-a}z|^2}
\ge\frac{e^{-2a/q}}{(1+e^{-a})^2}
=\frac{\rho^2}{(1+e^{-a})^2}.
\]
Hence \(F_{q,c}(x,\omega)\) is uniformly bounded below by the boxed positive constant, **for all** \(c\in\mathbb C\). It is uniformly bounded above for each fixed \(c\), since both geometric denominators are bounded away from zero. Thus the Gabor family is a frame and its optimal lower bound obeys the claimed inequality.

The two inequalities can be equalities simultaneously only in the *one-sided closed* Zak strip at \(x=1/q\) and \(z=-1\): the first because \(e^{-2ax}\) is strictly decreasing, the second because \(|1-e^{-a}z|\) is maximized only at \(z=-1\). Requiring the projection residual to vanish then determines exactly
\[
c=\frac{e^{-a/q}}{e^{-b/q}}
\frac{1+e^{-b}}{1+e^{-a}}\frac{W}{V}=c_*.
\]
The values of \(F_{q,c_*}\) along \(x\uparrow1/q\), \(z=-1\), approach the boxed bound, so its essential infimum equals that bound. To prove uniqueness, if any other \(c\) attained it, a minimizing sequence in the compact closure of the Zak strip would force equality in both nonnegative terms of the displayed decomposition and in the bound on \(|u|\). The only possible limiting point is the same \(x,z\) and it forces \(c=c_*\). This proves both sharpness and unique extremality.

At \(q=1\), the sampled vectors are one-dimensional and \(\Delta=0\). Choosing \(c=(1+e^{-b})/(1+e^{-a})\) creates a Zak zero at the \(x\downarrow0\), \(z=-1\) fiber, so the universal lower guarantee is zero. This is a boundary comparison, not an additional novelty claim.

**3. Sharp coalescence expansion.** Fix \(b,q\) and write \(a=b+\delta\). With \(t_j=e^{-bj/q}\), the vector \((\rho^j)_j\) equals \((t_je^{-\delta j/q})_j\). The exact residual \(\Delta\) is the squared distance of this vector to the span of \((t_j)_j\). Taylor expansion in the finite-dimensional Euclidean space gives
\[
\Delta=\frac{\delta^2}{q^2}
\left(S_2-\frac{S_1^2}{S_0}\right)+O_{b,q}(|\delta|^3).
\]
Here the positive coefficient is \(S_0\) times the variance of \(j\in\{0,\ldots,q-1\}\) under the strictly positive weights \(t_j^2/S_0\); it is strictly positive for \(q\ge2\). Multiplying by \(\rho^2/(1+e^{-a})^2=e^{-2b/q}/(1+e^{-b})^2+O_{b,q}(|\delta|)\) proves the stated quadratic law.

**4. High-redundancy limit.** For fixed distinct \(a,b>0\), Riemann sums give \(U/q\to\int_0^1e^{-2at}\,dt\), \(V/q\to\int_0^1e^{-2bt}\,dt\), and \(W/q\to\int_0^1e^{-(a+b)t}\,dt\). Moreover \(\rho\to1\). Substituting their elementary integrals gives the boxed expression. Its positivity is strict by the continuous Cauchy–Schwarz inequality: \(e^{-at}\) and \(e^{-bt}\) are not proportional almost everywhere when \(a\ne b\).

## Verification

The standalone script `check_uniform_two_decay.py` uses Python's standard library and deterministic sampling. It verifies the projection lower inequality against direct Zak-fiber evaluations for five distinct parameter triples, checks the analytic minimizing coefficient at the exact limiting fiber, independently sums the original geometric Zak series, tests the coalescence coefficient at several small rate differences, and checks the critical-density zero. The recorded execution printed `TWO_DECAY_GABOR_CHECKS_PASS 950 grid samples; 5 edge and coalescence parameter cases`.

For instance, at \(a=2.3\), \(b=0.7\), \(q=2\), the sharp guarantee is approximately \(0.00833316172112\), attained at \(c_*\approx0.49950773945\). The finite test is a normalization and reproducibility check only; the exact all-parameter result is established by the projection argument above.

## Relationship to prior work

Belov, Kulikov, and Lyubarskii establish **qualitative** Gabor-frame existence for general two-pole rational windows above density two (their Theorem 1.7) and explicitly discuss two kernels (Section 1.7.2) [1]. Under Fourier duality, causal exponentials correspond to Cauchy kernels. Therefore frame existence for the present oversampled mixtures is **not** claimed new. Their theorem does not state the sharp *coefficient-uniform optimal lower constant*, its unique worst complex mixing coefficient, or its quadratic pole-coalescence law.

Faulhuber and Shafkulovska [2] obtain sharp bounds for standard one-sided and symmetric two-sided exponentials and optimize lattice shape. Their windows are not signed two-distinct-rate mixtures with arbitrary complex secondary amplitude. The published exact bound on a protected stable interval of *critical-density* signed two-Cauchy Gabor systems [3] addresses a different density and optimizes over a restricted real residue interval. It neither implies a positive universal two-channel bound at redundancy two nor determines the variance-coalescence law above. Relevant exact higher-redundancy bounds for an *asymmetric two-sided* exponential [4] treat a single piecewise window, not a linear combination of two causal exponentials and optimization over all complex mixture ratios. The standard integer-density Zak criterion is classical [5]. No novelty is claimed for that reduction or elementary vector projection separately; the contribution is their sharp quantitative synthesis for the structurally motivated two-pole family.

## Limitations

The theorem fixes translation spacing \(1/q\) and unit modulation spacing, uses exactly two positive *distinct* exponential decay rates, and fixes the first coefficient to \(1\). The sharp formula concerns the worst possible **optimal lower** frame bound over complex mixing ratios; it is not a closed form for both frame bounds at each given ratio, nor for arbitrary lattice aspects or three or more decay channels. At coinciding rates, a nonzero coefficient cancels the window and the guarantee vanishes. The bibliographic comparison supports best-knowledge priority only; an uninspected equivalent explicit inequality could affect the originality assessment. No independent mathematical validation is claimed.

## References

[1] Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959v1, first posted 16 March 2021; *Inventiones Mathematicae* 231 (2023), 431–466, doi:10.1007/s00222-022-01151-8.

[2] M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917, first posted 6 April 2022; *Applied and Computational Harmonic Analysis* 67 (2023), 101574.

[3] *Exact protected-gap lower frame bound for signed two-Cauchy Gabor windows*, publicly accessible mathematical note, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-protected-gap-lower-frame-bound-for-signed-two-cauchy-gabo--1d27ec3a4907 .

[4] *Sharp asymmetric double-exponential Gabor frame bounds at every higher integer redundancy*, publicly accessible mathematical note, 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-asymmetric-double-exponential-gabor-frame-bounds-at-every--76de6cc216c1 .

[5] K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser, 2001, Chapter 8, for the classical Zak transform representation.
