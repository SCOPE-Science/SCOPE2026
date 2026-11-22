# Unavoidable one-step memory and a zeta-law coupling asymptotic in a polynomial modular map

## Finding

Consider the three-dimensional polynomial modular map of Zhang, Dong, Zhang and Ding, with quadratic coupling and fixed translation:
\[
T(x,y,z)=\bigl(\{a x+b y^2\},\{c y+d z^2\},\{e z+r\}\bigr),\qquad (x,y,z)\in[0,1)^3.
\]
Here \(a,c,e\) are integers at least \(2\), and \(b,d,r\) are arbitrary real numbers. The braces mean the half-open fractional part \(\{u\}=u-\lfloor u\rfloor\in[0,1)\). Normalized three-dimensional Lebesgue measure \(m\) is invariant. Consequently, each coordinate is uniform on \([0,1)\) at every time under stationary initialization.

Put \(B_2(t)=t^2-t+1/6\) for \(0\le t\le1\), extended periodically, and define the coupling-memory function
\[
J(B)=\int_0^1 B_2(\{B t^2\})\,dt,\qquad B\ge0.
\]
For stationary orbits, the exact lag-one *real-coordinate* covariances are
\[
\operatorname{Cov}_m(x_0,x_1)=\frac{J(|b|)}{2a},\qquad
\operatorname{Cov}_m(y_0,y_1)=\frac{J(|d|)}{2c}.
\]
Both are strictly positive for **every finite** real coupling, including zero. More explicitly,
\[
J(B)=\frac{B^2}{5}-\frac B3+\frac16\ge\frac1{36}\qquad(0\le B\le1),
\]
with equality at \(B=5/6\). At large coupling,
\[
\boxed{\quad J(B)=\frac{\zeta(5/2)}{4\pi^2\sqrt B}+O(B^{-1})\quad(B\to\infty).\quad}
\]
Thus the quadratic coupling weakens one-step memory only at the algebraic rate \(B^{-1/2}\), not by eliminating it at a finite coupling. In particular, the leading constant for the first-coordinate covariance is \(\zeta(5/2)/(8\pi^2 a)\). Here \(\zeta\) is the Riemann zeta function.

## Assumptions and scope

The map is the fixed-translation, modulus-one, degree-two specialization of equation (1) of the source article (first public date 2023-06-29). Its last-coordinate translation \(r\) is fixed across iterations, not independently resampled. For the exact product-Lebesgue invariant measure and the displayed formulas, the three diagonal gains \(a,c,e\) must be positive integers at least \(2\). The couplings \(b,d\) can have either sign. All statements concern the canonical real representatives in the half-open cube; no continuity of quadratic coupling across torus seams is asserted. Covariance is defined using the stationary probability space \(([0,1)^3,m)\): e.g. \(x_0(x,y,z)=x\) and \(x_1(x,y,z)=\pi_x(T(x,y,z))\). It is not a claim about the output ciphertext of an encryption algorithm or about every invariant probability measure.

## Proof

**1. Volume invariance.** For every positive integer \(q\), every real \(s\), and every integrable test function \(h\) on \([0,1)\),
\[
\int_0^1h(\{q u+s\})\,du=\int_0^1h(u)\,du.
\]
The identity follows by splitting \([0,1)\) into \(q\) equal branches. For any bounded measurable \(g\) on the cube, successively integrate \(g(T(x,y,z))\) over \(x\), then \(y\), then \(z\). Each integration removes the corresponding translated integer-multiplication map without changing the remaining integral. Hence \(T_*m=m\). In particular the stationary \(x\), \(y\), and \(z\) are jointly independent and uniform at each single time.

**2. Exact phase covariance.** For every integer \(q\ge1\) and real \(s\), direct subdivision into the \(q\) full branches gives
\[
\int_0^1\left(u-\frac12\right)
\left(\{qu+s\}-\frac12\right)du
=\frac{B_2(\{s\})}{2q}.
\]
Indeed, for \(s\in[0,1)\) substitute \(u=(j+v)/q\), sum \(j=0,\ldots,q-1\), and reduce the left side to \(q^{-1}\int_0^1(v-1/2)(\{v+s\}-1/2)dv\); its two elementary polynomial pieces give \(B_2(s)/(2q)\). Periodicity handles arbitrary \(s\). Integrate the first-coordinate identity conditionally over independent uniform \(y\) with phase \(s=b y^2\); similarly integrate the second-coordinate identity with phase \(s=d z^2\). Since \(B_2(\{-t\})=B_2(\{t\})\), the expressions depend on \(|b|\) and \(|d|\), proving the two exact covariance formulas.

**3. Positivity for all quadratic couplings.** For \(0\le B\le1\), \(\{B t^2\}=B t^2\) except possibly a null endpoint, so termwise integration gives the displayed quadratic polynomial. Its exact minimum is \(1/36\) at \(B=5/6\).

For \(B>0\), substitute \(v=B t^2\):
\[
J(B)=\frac{K(B)}{2\sqrt B},\qquad
K(B)=\int_0^B B_2(\{v\})\,v^{-1/2}\,dv.
\]
The first full period contributes \(K(1)=1/15\). Every subsequent full period contributes a nonnegative amount. To see this, write \(w(u)=(k+u)^{-1/2}\) for integer \(k\ge1\). Twice integrating by parts using
\[
H(u)=\frac{u^2(1-u)^2}{12},\qquad H''(u)=B_2(u),\qquad H(0)=H(1)=H'(0)=H'(1)=0
\]
gives \(\int_0^1B_2(u)w(u)du=\int_0^1H(u)w''(u)du>0\). Any incomplete final period beginning at integer \(k\ge1\) contributes at least \(-\sqrt3/(54\sqrt k)\), since the total absolute negative area of \(B_2\) over one unit period is \(\sqrt3/54\), and the weight there is at most \(1/\sqrt k\). Because \(1/15>\sqrt3/54\), the accumulated first-period mass cannot be cancelled. Thus \(K(B)>0\) for all \(B\ge1\), and hence \(J(B)>0\) for every finite \(B\ge0\).

**4. Sharp large-coupling constant.** The periodic Bernoulli polynomial has the absolutely convergent Fourier expansion
\[
B_2(\{v\})=\frac1{\pi^2}\sum_{k=1}^{\infty}\frac{\cos(2\pi k v)}{k^2}.
\]
Its mean over every unit interval is zero. Integration by parts against a bounded periodic primitive therefore shows that the tail \(\int_B^\infty B_2(\{v\})v^{-1/2}dv\) is \(O(B^{-1/2})\). The standard Fresnel/Gamma integral
\[
\int_0^\infty v^{-1/2}\cos(2\pi k v)dv=\frac1{2\sqrt k}
\]
and termwise integration (justified, for example, by exponential damping followed by uniform Dirichlet tail bounds) give
\[
K(\infty)=\frac{1}{2\pi^2}\sum_{k=1}^{\infty}k^{-5/2}
=\frac{\zeta(5/2)}{2\pi^2}.
\]
Finally \(J(B)=K(B)/(2\sqrt B)\) yields the stated leading term with remainder \(O(B^{-1})\). This completes the proof for both coordinate directions.

## Verification

The included standalone `verify.py` uses only the Python standard library. It checks 182 exact rational instances of the phase-covariance identity, the exact low-coupling minimum and positivity kernel, and 14 numerical coupling integrals up to amplitude \(400\), including the predicted zeta-law constant. The program prints `PASS`. These finite computations are not the proof of positivity on an infinite parameter range or of the asymptotic limit; those conclusions follow from Steps 3 and 4.

## Relationship to prior work

Zhang, Dong, Zhang and Ding (2023), equation (1) and Sections 2–4, introduce the triangular polynomial modular map and analyze its Jacobian-derived Lyapunov exponents, sample entropy, quantized sequence tests, and encrypted-image correlations. Their reported image correlations are not stationary temporal autocovariances of real coordinates. The exact Bernoulli-integral formula, strict positivity over all finite quadratic couplings, and \(\zeta(5/2)\) coupling-decay law are not present in the inspected full article.

The separately published *Periodic-point lifting and a sharp two-cycle phase diagram for a polynomial modular skew map* establishes exact periodic-point counts and a nonintegral-base bifurcation, while *Coupling-independent periodic grids and sharp equidistribution in triangular modular maps* establishes periodic-grid distribution and Lebesgue invariance. Those theorems have different conclusions: periodic-point arithmetic or one-time invariant distribution does not determine the sign or exact size of a coordinate's two-time covariance. The present result uses a different Bernoulli-polynomial integral and an all-coupling positivity argument. Classical expanding-skew-product statistical limit theorems supply general mixing or asymptotic frameworks but do not give this exact all-amplitude sign and leading constant. Unindexed equivalent integral identities and unpublished priority remain possible.

## Limitations

The theorem applies to stationary initialization by normalized Lebesgue measure and fixed last-coordinate translation, integer expanding gains, quadratic couplings, and modulus one. It does not assert stochastic-output security, independence of successive coordinates, higher-lag correlation formulas, uniqueness of the invariant law, or analogous positivity for arbitrary coupling functions or powers. Uniform one-time marginals and positive one-step covariance are compatible. Although both coordinate covariances are nonzero, they tend to zero as the respective coupling magnitudes become large. No independent mathematical audit has been performed.

## References

1. Y. Zhang, W. Dong, J. Zhang and Q. Ding, *An Image Encryption Transmission Scheme Based on a Polynomial Chaotic Map*, **Entropy** 25 (2023), 1005, first public date 2023-06-29, DOI: 10.3390/e25071005; lawful full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10377869/ .
2. *Periodic-point lifting and a sharp two-cycle phase diagram for a polynomial modular skew map*, public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-periodic-point-lifting-and-a-sharp-two-cycle-phase-diagram-for-a--1b4dbfe9d320 .
3. *Coupling-independent periodic grids and sharp equidistribution in triangular modular maps*, public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-coupling-independent-periodic-grids-and-sharp-equidistribution-i--538c265ee323 .
4. Y. Hafouta, *Large deviations, moment estimates and almost sure invariance principles for skew products with mixing base maps and expanding-on-average fibers*, **Ergodic Theory Dynam. Systems** 44 (2024), 118–158, first online 2023-04-11, DOI: 10.1017/etds.2023.23 (general statistical background, not an exact covariance formula).
