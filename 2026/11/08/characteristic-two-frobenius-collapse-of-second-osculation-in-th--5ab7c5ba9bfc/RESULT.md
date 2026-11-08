# Characteristic-two Frobenius collapse of second osculation in the truncated-simplex cubic toric family

## Finding
For every integer \(n\ge2\) and every field \(k\), let \(X_n\subset\mathbb P_k^{n(n+1)-1}\) be the closure of the torus image of the cubic monomials \(x_i^2x_j\) for all ordered pairs \(0\le i\ne j\le n\). At **every point of the dense torus**, the Hasse-jet ranks in orders zero and one are \(1\) and \(n+1\), and the rank in order three is \(n(n+1)\). The second Hasse-jet rank is
\[
\operatorname{rank}J_2(X_n)=
\begin{cases}
2n+1,&\operatorname{char}k=2,\\
2n+\binom n2,&\operatorname{char}k\ne2.
\end{cases}
\]
In characteristic two the second-osculating projective dimension is exactly \(2n\), giving \(\binom n2\) independent second-order Laplace defects, instead of the characteristic-not-two defect of one. In characteristic two the quadratic second fundamental map on the projectivized tangent space is, up to linear coordinates on its image, the Frobenius map
\[
[v_1:\cdots:v_n]\longmapsto[v_1^2:\cdots:v_n^2].
\]
Its image is a linear \(\mathbb P^{n-1}\) in the projectivized normal space, and the map is purely inseparable of degree \(2^{n-1}\). This latter assertion uses the quadratic Hasse-jet construction, not the ordinary characteristic-two Hessian.

## Assumptions and scope
The field \(k\) is arbitrary; perfection and algebraic closure are unnecessary. The integer \(n\) is at least two. The statements concern the dense torus of the toric image, not every possible boundary point. The rational cubic map has base points on the ambient source \(\mathbb P^n\); the image is defined as the closure of its restriction to the torus, where it is a morphism.

The \(r\)-jet space at a torus point is the image of the linear evaluation map from the span of the displayed monomials to the truncated completed local ring \(k[u_1,\ldots,u_n]/(u_1,\ldots,u_n)^{r+1}\); it is defined by polynomial Taylor coefficients (Hasse derivatives), with **no division by factorials**. The projective \(r\)-osculating dimension is the rank minus one. The nontrivial second-order defect is relative to the expected projective dimension \(\binom{n+2}{2}-1\), which is no larger than the ambient dimension for every \(n\ge2\).

## Proof
**1. Local coordinates and smooth torus.** Work in the source chart \(x_0=1\), write \(t_i=x_i/x_0\) for \(1\le i\le n\), and order the sections in three groups:
\[
 f_i=t_i,\qquad g_i=t_i^2,\qquad h_{ij}=t_i^2t_j\quad(i\ne j).
\]
There are \(2n+n(n-1)=n(n+1)\) distinct sections. On the torus all \(g_j\) are invertible, and for every \(i\) there is some \(j\ne i\), giving \(t_i=h_{ji}/g_j\). Thus the projective morphism restricts to an isomorphism onto the image torus (with its natural open subvariety structure); in particular its image is smooth of dimension \(n\) there. Torus translation and invertible diagonal rescaling of all monomial coordinates identify the jets at any torus point with those at \(t_1=\cdots=t_n=1\).

**2. Exhaustive second-jet expansions.** Put \(t_i=1+u_i\). Modulo terms of total degree at least three,
\[
\begin{aligned}
 f_i&=1+u_i,\\
 g_i&=1+2u_i+u_i^2,\\
 h_{ij}&=1+2u_i+u_j+u_i^2+2u_iu_j.
\end{aligned}
\]
The \(2n\) jets \(f_i,g_i\) are linearly independent in every characteristic: their independent linear coefficients \(u_i\) and quadratic coefficients \(u_i^2\) force all coefficients of a purported linear relation to vanish. For each ordered pair \(i\ne j\),
\[
 h_{ij}-g_i-f_j=-1+2u_iu_j\pmod{(u_1,\ldots,u_n)^3}.
\]
This expression depends only on the unordered pair \(\{i,j\}\). When the characteristic is not two, the \(\binom n2\) expressions are independent modulo the span of the \(f_i,g_i\), because the distinct mixed monomials \(u_iu_j\) occur in no \(f_i\) or \(g_i\) jet and each appears with coefficient two. Consequently the second-jet rank is \(2n+\binom n2\).

In characteristic two, every expression above equals the same nonzero constant \(1\). That constant is not in the span of \(f_i,g_i\): elimination of their \(u_i\) and \(u_i^2\) coefficients forces all their coefficients to be zero. Hence the second-jet rank is exactly \(2n+1\). More precisely its image is the entire \(k\)-linear span of \(1,u_i,u_i^2\), for \(1\le i\le n\). The rank-one and rank-zero claims follow by taking lower truncations. The expected second-jet rank is \(\binom{n+2}{2}\); subtracting the established ranks gives respectively one and \(\binom n2\) defective dimensions.

**3. Third jets.** The affine monomials \(f_i,g_i,h_{ij}\) are pairwise distinct, of total degree at most three, so they are linearly independent polynomials. Translation \(t_i\mapsto1+u_i\) is an automorphism of the vector space of all polynomials of degree at most three. Thus the cubic Taylor truncation remains linearly independent, giving third-jet rank \(n(n+1)\) in every characteristic. No argument about infinitesimal higher order terms is needed.

**4. Quadratic fundamental map in characteristic two.** The second fundamental quadratic system is the quadratic term of the local projective parametrization modulo the value and tangent terms. Its image is exactly the quotient of the second-jet space by the order-one jet space. In characteristic two the proof in step 2 identifies this quotient with the span of the \(n\) independent pure squares \(u_i^2\), with no mixed products. Therefore, for tangent direction \([v_1:\cdots:v_n]\), the second fundamental map has homogeneous coordinates \([v_1^2:\cdots:v_n^2]\) after an invertible linear change of target coordinates. This is the relative Frobenius on projective space followed by a linear embedding. The extension of function fields \(k(v_1/v_n,\ldots,v_{n-1}/v_n)\) over \(k((v_1/v_n)^2,\ldots,(v_{n-1}/v_n)^2)\) is purely inseparable of degree \(2^{n-1}\), establishing the stated degree. The derivative of the map vanishes identically.

## Verification
The included `verification/check_osculation.py` independently constructs the full Hasse-jet matrix using integer binomial coefficients and computes exact ranks in orders zero through three for \(2\le n\le8\) in characteristics two, three, five, and seven. It also performs rational exact arithmetic for \(2\le n\le5\) and checks that all characteristic-two mixed quadratic coefficients vanish while the pure-square coefficients form an identity submatrix. Execute `python3 verification/check_osculation.py`; expected exact output is in `verification/output.txt`. The script performs 32 complete characteristic/range rank comparisons. These finite comparisons corroborate but do not substitute for the all-\(n\), all-field proof above.

## Relationship to prior work
The truncated-simplex family of cubic monomials and its characteristic-zero second-order Laplace equation are classical; they are explicitly described in Mezzetti, Miró-Roig, and Ottaviani (2011, Section 4) and studied further by Michałek and Miró-Roig (2013). Those sources work over characteristic-zero fields. They establish the existence of an osculating defect but do not state the sharp characteristic-two rank \(2n+1\), the growing defect \(\binom n2\), or the Frobenius second fundamental map. General jet and toric inflection constructions, including Perkinson's work, provide relevant background but do not replace this characteristic-two calculation. The available bibliographic record of Perkinson's later inflection paper could not be used to exclude all possible earlier coverage; historical priority should therefore be independently verified.

## Limitations
The result does not describe the scheme of inflection points at the toric boundary, global higher osculating varieties, or classifications of arbitrary monomial cubic projections. The finite checks do not prove the general theorem by enumeration. The phrase “second fundamental map” refers to the quadratic Hasse-jet map; polarizing the quadratic forms in characteristic two would lose the pure-square information. No claim of independent audit or absolute historical priority is made.

## References
1. E. Mezzetti, R. Miró-Roig, G. Ottaviani, *Laplace Equations and the Weak Lefschetz Property*, arXiv:1110.5239v1, 24 October 2011; especially Sections 2 and 4. https://arxiv.org/abs/1110.5239
2. M. Michałek, R. Miró-Roig, *Smooth monomial Togliatti systems of cubics*, arXiv:1310.2529v1, 9 October 2013; especially Introduction and Section 3. https://arxiv.org/abs/1310.2529
3. E. Mezzetti, R. Miró-Roig, *The minimal number of generators of a Togliatti system*, arXiv:1506.05914v1, 19 June 2015. https://arxiv.org/abs/1506.05914
4. D. Perkinson, *Principal parts of line bundles on toric varieties*, Compositio Mathematica 104 (1996), 27–39.
5. D. Perkinson, *Inflections of toric varieties*, Michigan Mathematical Journal 48 (2000), DOI:10.1307/mmj/1030132730 (bibliographic record and indirect discussion only).
