# Sharp Schatten-sixth numerical radius for four-site nilpotent weighted shifts

## Finding

Let \(T:\mathbb C^4\to\mathbb C^4\) be any nonzero one-step nilpotent weighted shift, so \(Te_j=a_je_{j+1}\) for \(j=0,1,2\), \(Te_3=0\), with arbitrary complex weights. Define its Schatten-sixth numerical radius by
\[
w_6(T)=\sup_{\theta\in\mathbb R}\left\|
\frac{e^{i\theta}T+e^{-i\theta}T^*}{2}
\right\|_6,\qquad
\|A\|_6^6=\operatorname{tr}((A^*A)^3).
\]
There is a **sharp, attained** four-dimensional constant
\[
\boxed{w_6(T)^6\le
\frac{(r_*+2)(r_*^2+4r_*+1)}
{32(r_*^3+2)}\,\|T\|_6^6,}
\tag{1}
\]
where \(r_*\) is the **unique positive root** of
\[
\boxed{r^4+3r^3-4r-3=0,\qquad 1<r_*<2.}
\tag{2}
\]
Numerically \(r_*=1.23283538459334\), and the sharp quotient \(w_6(T)/\|T\|_6\) is approximately \(0.761064247904\).

**Complete equality classification.** Equality in (1) for \(T\ne0\) holds if and only if
\[
\boxed{|a_0|=|a_2|>0,\qquad |a_1|=\sqrt{r_*}\,|a_0|.}
\tag{3}
\]
The three complex phases are unrestricted. In particular, neither equal-modulus weights nor a boundary shift with a zero weight can be optimal.

An exact formula for **every** shift in this class, with \(x=|a_0|^2\), \(y=|a_1|^2\), \(z=|a_2|^2\) and \(S=x+y+z\), is
\[
\boxed{32\,w_6(T)^6=S^3-3xzS,\qquad
\|T\|_6^6=x^3+y^3+z^3.}
\tag{4}
\]

## Assumptions and scope

All matrices are over the complex field; no positivity or nonvanishing of the individual weights is assumed until equality is discussed. Schatten norms use the **unnormalized** matrix trace. Formula (1) applies to exactly the four-site one-step nilpotent shift class, not arbitrary nilpotent matrices, not ordinary operator-norm numerical radius, and not the unrestricted family of all matrix sizes. The exact numerical value is for orientation; equations (1)–(3) are the precise algebraic statement.

## Proof

**1. Remove phases and compute the sixth moment.**
The diagonal unitary \(U_\theta e_j=e^{ij\theta}e_j\) conjugates \(T\) to \(e^{i\theta}T\). Hence the norm in the definition of \(w_6\) is independent of \(\theta\). Another diagonal unitary removes all nonzero complex edge phases, so we may compute using the real symmetric matrix \(H=(T+T^*)/2\) with nonnegative off-diagonal moduli.

The bipartite path matrix \(2H\) has spectrum
\(\{\sqrt{\lambda_+},-\sqrt{\lambda_+},\sqrt{\lambda_-},-\sqrt{\lambda_-}\}\), with
\[
\lambda_++\lambda_-=x+y+z=S,\qquad
\lambda_+\lambda_-=xz.
\]
This follows directly from the characteristic polynomial
\(\mu^4-S\mu^2+xz\) of \(2H\).
Therefore
\[
\operatorname{tr}(H^6)
=\frac{2}{64}(\lambda_+^3+\lambda_-^3)
=\frac{S^3-3xzS}{32}.
\]
Also \(T^*T\) has eigenvalues \(x,y,z,0\), establishing both identities in (4).

**2. Optimize over the two outer squared weights.**
By homogeneity normalize \(x^3+y^3+z^3=1\), and write
\[
F(x,y,z)=(x+y+z)^3-3xz(x+y+z).
\]
Put \(m=x^3+z^3=1-y^3\), \(u=(x+z)/2\), \(v=(x-z)/2\). If \(m>0\), then
\[
m=2u^3+6uv^2,\qquad
\frac{m^{1/3}}{2}\le u\le\left(\frac m2\right)^{1/3}.
\]
The smaller endpoint corresponds to \(xz=0\), and the larger to \(x=z\). Eliminating \(v^2\) gives the **exact identity**
\[
F=m+y^3+6uy^2+8u^2y+\frac{my}{2u}.
\tag{5}
\]
For fixed \(m>0\) and \(y>0\), this expression is **strictly convex** in \(u\), since
\[
\frac{\partial^2F}{\partial u^2}=16y+\frac{my}{u^3}>0.
\]
Consequently its maximum on the admissible interval occurs at an endpoint, with no interior equality.

At \(xz=0\), one outer weight vanishes and
\[
F=(x+y+z)^3\le4(x^3+y^3+z^3)=4,
\]
because only two variables are nonzero and the two-variable power-mean inequality applies. If \(y=0\) or \(m=0\), then \(F=1\). By contrast, for \(x=y=z>0\) the normalized value is \(F=6\). Hence no zero-weight or one-outer-weight configuration is optimal. Strict convexity forces **every** optimizer to satisfy \(x=z>0\) and \(y>0\).

**3. Solve the remaining one-variable problem.**
On \(x=z>0\), write \(r=y/x\ge0\). The normalized objective is
\[
g(r)=\frac{(r+2)(r^2+4r+1)}{r^3+2}.
\]
Direct differentiation yields
\[
g'(r)=-\frac{6(r^4+3r^3-4r-3)}{(r^3+2)^2}.
\tag{6}
\]
The polynomial in (2) has **exactly one positive root** by Descartes' sign rule; its value at \(1\) is \(-3\) and at \(2\) is \(29\). As \(g'\) is positive before that root and negative after it, \(g\) has a unique global maximum at \(r=r_*\). Substitution into (4) proves (1); the strict endpoint and one-variable arguments prove that (3) exhausts the equality cases. Individual phases are free because of the diagonal gauge reduction.

**4. The first nontrivial balancing effect.**
For a two-edge three-site nilpotent shift the corresponding moment is
\((x+y)^3/32\) and the norm-sixth power is \(x^3+y^3\), so its optimizer has equal edge moduli by convexity. Four sites are the first path length in which the distance-two spectral term \(xz\) enters, and the equality ratio of central to outer squared weights becomes the nontrivial algebraic number \(r_*>1\).

## Verification

The accompanying pure-standard-library script `verify_schatten_sixth_four_site.py` computes the sixth trace of the explicit real symmetric matrix with exact rational arithmetic, using all \(343\) integer weight triples in a finite test grid. It also checks the eliminated identity (5) at rational test points and the quotient derivative (6) at fifty rational arguments. Running `python -S verify_schatten_sixth_four_site.py` should print `SCHATTEN_SIXTH_FOUR_SITE_EXACT_CHECK_OK 796`. A separate symbolic calculation factored (6) and recovered the reduced identity (5). These finite or symbolic checks corroborate the proof; the all-weight and equality statements follow from the analytic argument above.

## Relationship to prior work

Pal and Chandok [1] define the same Schatten-\(p\) numerical-radius framework and prove general Aluthge-transform bounds, including their Theorems 2.1–2.12 and numerical examples in dimension three. Their published formulas do not optimize the Schatten-sixth quotient over all four-site weighted shifts or classify its extremizers. Sahoo [2] provides earlier general Schatten-\(p\) inequalities, but not the present fixed-dimensional sharp constant.

The published fourth-moment weighted-shift theorem [3] gives a sharp **Schatten-fourth** constant and sine-law equality weights for every finite shift; it neither implies the sextic objective (4) nor fixes its maximizing parameter. The general circle-covariant even-moment theorem [4] proves a **dimension-free** \(2m\)-moment inequality with coefficient \(C_m(1/2)\); at the sixth moment its coefficient is \(5/16\), strictly above the exact four-site coefficient \(g(r_*)/32\). Its stated nonattainment for compact operators at the dimension-free sharp threshold is entirely compatible with the present finite-dimensional attained optimum. A 2026 resolvent-rearrangement result [5] concerns Schatten norms of \((I-T)^{-1}\), a different functional, and does not imply (1).

The claim here is therefore the **specific sharp four-site sixth-moment constant and complete equality class**, not the existence of generic Aluthge bounds, an identity at exponent four, or a dimension-free inequality.

## Limitations

This theorem does not determine sharp constants in other fixed dimensions, at arbitrary real Schatten exponents, for general directed graphs or for arbitrary nilpotent matrices. It asserts no optimal quantitative stability coefficient for near-equality. An older general theorem on sharp finite-path Schatten moments might imply the result even if published under unrelated terminology; priority is assessed only against the cited, examined sources and searches, and has not been independently established.

## References

1. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1, first publicly posted 2026-10-08, https://arxiv.org/abs/2610.11336 .
2. S. Sahoo, *Further bounds on p-numerical radii of operators via generalized Aluthge transform*, arXiv:2504.04693v1, first publicly posted 2025-04-07, https://arxiv.org/abs/2504.04693 .
3. *Sharp weighted Schatten-fourth radii of nilpotent shifts*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-weighted-schatten-fourth-radii-of-nilpotent-shifts--17db4dbf42a4 .
4. *Sharp even Schatten numerical-radius moments under circle covariance*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-even-schatten-numerical-radius-moments-under-circle-covari--6104c50d4ada .
5. *Strict Schatten rearrangement for four-site weighted-shift resolvents*, published 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-schatten-rearrangement-for-four-site-weighted-shift-resol--a0f6a336e377 .
