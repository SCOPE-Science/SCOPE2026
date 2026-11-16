# Sharp first-band covering on every product torus and a rigidity transition

## Finding

For every integer \(d\ge 3\), let \(\mu\) be a positive Borel probability measure on \(\mathbb T^d=(\mathbb R/\mathbb Z)^d\) whose Fourier coefficients vanish at every nonzero rectangular first-band frequency:
\[
\widehat\mu(k)=\int_{\mathbb T^d} e^{-2\pi i k\cdot x}\,d\mu(x)=0,\qquad k\in\{-1,0,1\}^d\setminus\{0\}.
\]
For torus sup distance \(\operatorname{dist}_\infty(x,y)=\max_j\min_{m\in\mathbb Z}|x_j-y_j-m|\), define the covering radius \(\delta(\mu)=\max_{a\in\mathbb T^d}\inf_{x\in\operatorname{supp}\mu}\operatorname{dist}_\infty(a,x)\). Then the **sharp all-dimensional bound** is
\[
\boxed{\delta(\mu)\le r_d:=\frac{\arccos\bigl(-(d-1)/(d+1)\bigr)}{2\pi}},
\]
and equality is attained by an explicit positive atomic measure. In particular, \(r_3=1/3\), and \(r_d=1/2-1/(\pi\sqrt{d+1})+O(d^{-3/2})\).

There is a universal **contact rigidity** phenomenon: if equality holds and \(a\) is any center attaining the covering radius, then for each coordinate \(j\) the two points \(a\pm r_de_j\) must be atoms of \(\mu\), each with mass exactly
\[
\boxed{\frac{d+1}{d\,2^{d+1}}}.
\]
All remaining mass is supported on the **codimension-at-least-two antipodal skeleton**
\[
\Sigma_a=\bigl\{x\in\mathbb T^d:\text{at least two distinct coordinates satisfy }x_j=a_j+1/2\pmod1\bigr\}.
\]
Conversely, any positive measure satisfying the Fourier conditions and this support/contact condition attains the sharp radius at \(a\). Despite the forced contact masses, unlike the two-dimensional case the extremizer is **not unique** for any \(d\ge3\): a positive one-parameter family of distinct exact measures attains equality. Thus rigidity of the full positive rule fails first in dimension three.

## Assumptions and scope

Throughout, \(d\) is an arbitrary finite integer at least three, the coordinate torus has period one, and all probability measures are positive Borel measures; no finite-atomicity assumption is imposed on the upper bound or the contact classification. The Fourier band is the complete rectangular set \(\{-1,0,1\}^d\), not the axial frequency cross. The metric is the quotient \(\ell_\infty\) torus metric; the assertion is not about Euclidean covering, signed measures, or higher Fourier bands. Supremum over centers is attained because torus distance to the nonempty closed support is continuous on the compact torus.

## Proof

**1. Exact multilinear moments.** Fix any prospective hole center \(a\). Define
\[
p_j(x)=\frac{1+\cos(2\pi(x_j-a_j))}{2}=\cos^2\!\bigl(\pi(x_j-a_j)\bigr)\in[0,1].
\]
For each subset \(S\subseteq\{1,\ldots,d\}\), the product \(\prod_{j\in S}p_j\) belongs to the rectangular first Fourier band and has Haar mean \(2^{-|S|}\). Exactness therefore gives
\[
\int\prod_{j\in S}p_j\,d\mu=2^{-|S|}.
\]
Write \(e_m(p)\) for the elementary symmetric polynomial in the \(d\) numbers \(p_1,\ldots,p_d\). Consequently,
\[
\int e_d(p)\,d\mu=2^{-d},\qquad
\int e_{d-1}(p)\,d\mu=d\,2^{-(d-1)}.
\]

**2. Sharp obstruction to a large empty cube.** Suppose the support avoids the open sup ball of radius \(R\) centered at \(a\), with \(r_d<R<1/2\). Put \(s=\cos^2(\pi R)\), so \(s<1/(d+1)\). At every support point at least one coordinate has \(p_j\le s\). When all \(p_j>0\),
\[
 e_{d-1}(p)=e_d(p)\sum_{j=1}^d\frac1{p_j}
 \ge \left(\frac1s+d-1\right)e_d(p).
\]
If any \(p_j=0\), the same inequality holds because \(e_d=0\) and \(e_{d-1}\ge0\). Integration yields
\[
 d\,2^{-(d-1)}\ge\left(\frac1s+d-1\right)2^{-d},
\quad\text{i.e.}\quad 2d\ge\frac1s+d-1,
\]
contradicting \(s<1/(d+1)\). A radius equal to \(1/2\) is also impossible: the avoiding condition would force \(e_d=0\) almost everywhere, contradicting its positive integral. Hence every covering radius is at most \(r_d\).

**3. Explicit exact rule achieving equality.** Let \(r=r_d\) and \(c=\cos(2\pi r)=-(d-1)/(d+1)\). For each subset \(S\subseteq\{1,\ldots,d\}\) with \(|S|\le d-2\), introduce the vertex \(v_S\in\mathbb T^d\) having coordinate zero on \(S\) and coordinate \(1/2\) on its complement. Set
\[
\mu_d=2^{-d}\sum_{|S|\le d-2}\delta_{v_S}
 +\frac{d+1}{d\,2^{d+1}}\sum_{j=1}^d
 \bigl(\delta_{r e_j}+\delta_{-r e_j}\bigr).
\]
All weights are strictly positive. There are \(2^d-d-1\) retained vertices, and the total mass is one.

To check every first-band Fourier moment exactly, start with the uniform measure on all \(2^d\) vertices of \(\{0,1/2\}^d\), whose nonzero coefficients in the band vanish by tensor-product cancellation. The rule \(\mu_d\) replaces only the \(d+1\) missing vertices: the all-zero vertex and the \(d\) vertices with exactly one coordinate \(1/2\). For a frequency with \(s\) nonzero coordinates, their original total Fourier contribution is \((d+1-2s)/2^d\). The new \(d\) symmetric pairs contribute
\[
\frac{d+1}{d\,2^d}\bigl((d-s)+s c\bigr)
=\frac{d+1-2s}{2^d}.
\]
This identity is exact for all \(s=0,\ldots,d\) and all signs of the nonzero Fourier frequencies. Thus \(\mu_d\) has precisely the prescribed moments. Every retained vertex lies on at least two antipodal faces, while each added node has sup distance \(r\) from the origin. Therefore its support avoids the open sup cube centered at zero of radius \(r\). Together with Step 2 this proves sharpness.

**4. Every equality contact mass is forced.** Translate a maximizing center to zero. Write \(s_*=1/(d+1)\) and \(p_j=\cos^2(\pi x_j)\). On the support, at least one \(p_j\le s_*\). The nonnegative *deficit*
\[
D(p)=\frac{e_{d-1}(p)}{2d}-e_d(p)
\]
has integral zero by Step 1. Hence \(D=0\) almost everywhere. If two or more coordinates of \(p\) vanish, both symmetric polynomials vanish. If precisely one vanishes, then \(D>0\). When all are positive, equality requires
\[
\sum_j p_j^{-1}=2d\quad\text{and}\quad\min_j p_j\le s_*.
\]
Each of the other \(d-1\) reciprocals is at least one, while the smallest-coordinate reciprocal is at least \(d+1\). Equality thus forces exactly one coordinate \(p_j=s_*\) and all others one. Its torus realizations are precisely \(\pm r e_j\). Since \(D\) is continuous, the same support constraint applies to every support point, not only almost everywhere. This proves the asserted contact-and-skeleton support restriction.

Let \(h_j\) be the total mass at the two \(j\)-th contact points and \(H=\sum_jh_j\). The identity \(\int e_d=2^{-d}\) gives \(H/(d+1)=2^{-d}\), so \(H=(d+1)/2^d\). Also, for each \(j\), the moment \(\int\prod_{k\ne j}p_k=2^{-(d-1)}\) receives no contribution from the skeleton and equals \(h_j+s_*(H-h_j)\). Consequently,
\[
 h_j=\frac{d+1}{d\,2^d}.
\]
Finally, the band-limited test \(\sin(2\pi x_j)\prod_{k\ne j}p_k\) has zero integral, vanishes on the skeleton and on all contact nodes of other coordinates, and takes opposite nonzero values at \(\pm r e_j\). Therefore the two \(j\)-th contact masses are equal, each \((d+1)/(d2^{d+1})\). A supported measure satisfying the moment constraints and these mandatory contacts automatically has an empty open ball of radius \(r\) about the center, so sharpness holds in the reverse direction.

**5. Nonuniqueness beginning in dimension three.** For any \(d\ge3\), let \(v_\emptyset=(1/2,\ldots,1/2)\) and \(v_{\{1\}}=(0,1/2,\ldots,1/2)\), both retained vertices in \(\mu_d\). Choose \(0<\eta<2^{-d}\). Subtract mass \(\eta\) from each of these two atoms and add mass \(\eta\) at each of
\[
 w_\pm=(\pm1/4,1/2,\ldots,1/2).
\]
For any first-band frequency, the sum of the two removed characters equals the sum of the two added characters (after division by \(\eta\)): if its first frequency is zero both equal \(2(-1)^s\); if the first frequency is nonzero both equal zero. Thus all Fourier moments and total mass are unchanged. All four affected points lie on the antipodal skeleton for \(d\ge3\), so the sharp hole remains. Varying \(\eta\) gives infinitely many distinct extremizers. In \(d=2\), by contrast, the antipodal skeleton consists only of the fully antipodal vertex, and the forced four contact weights leave its mass fixed; hence the corresponding two-dimensional extremizer is unique up to translation.

The stated asymptotic follows from \(\arccos(-1+2/(d+1))=\pi-2(d+1)^{-1/2}+O(d^{-3/2})\).

## Verification

The standalone standard-library program `CHECK.py` reconstructs the explicit rational cosine contributions and checks every Fourier coefficient in \(\{-1,0,1\}^d\) for dimensions \(2\le d\le7\), together with normalization, dual mean identities, and the nonrigidity perturbation. On the saved standalone file it prints `FIRST_BAND_CUBE_EXACT_CHECKS_PASS 6594`. All assertions use exact rational arithmetic. This is finite consistency testing only; the proof for every integer \(d\ge3\) is Steps 1–5 and does not rely on a bounded computation.

## Relationship to prior work

Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials* (arXiv:2608.11915, publicly posted August 12, 2026), investigates positive multivariate trigonometric quadrature and gives general covering-radius bounds by sign-localized test functions, notably Theorem 3.3 for exactness through rectangular degree \(2n\), \(n\ge1\). It does not give the sharp complete degree-one rectangular result in every dimension, its exact non-tensor positive construction, or the forced contact masses and dimension-three nonuniqueness. The distinction matters: his theorem assumes exactness of a strictly larger frequency space than the first band here, so its estimate cannot be invoked as an implication of these weaker moment hypotheses.

The known two-dimensional special case gives the constant \(\arccos(-1/3)/(2\pi)\) and a uniquely determined five-node measure. The present result is not a restatement of that case: it proves a sharp **all-dimensional** law with explicit replacement of \(d+1\) corners of the \(d\)-cube and identifies a genuine rigidity-to-nonrigidity transition in the higher-dimensional optimizer set. Generic positive cubature existence theorems and the classical product-torus Haar rule do not imply the sharp hole radius or its equality support classification. Searches of related exact first-band cubature and positive quadrature results did not identify an older equivalent all-dimensional sharp statement; this does not certify publication priority.

## Limitations

The theorem concerns only first-band rectangular exactness, positive probability measures, and the wrap-around supremum metric. The equality-support statement gives compulsory atoms and the allowed remainder skeleton, not a parametrization of every possible remainder measure on that skeleton. The continuum of optimal measures is exhibited explicitly, not claimed to enumerate all extreme points of the convex moment polytope. No higher-frequency, weighted-target, or Euclidean-metric claim follows automatically. Earlier equivalent high-dimensional positive quadrature results may exist under different terminology; independent mathematical and historical audit has not been performed.

## References

1. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915v1, first posted August 12, 2026, https://arxiv.org/abs/2608.11915 ; especially Section 3.1, Theorem 3.3 and Remark 3.4.
2. Standard product-torus Fourier orthogonality, as recalled in Kunis, Section 2, and the multivariate elementary-symmetric-polynomial identity \(e_{d-1}/e_d=\sum_j1/p_j\) for positive coordinates.
