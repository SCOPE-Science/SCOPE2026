# Complete face and gamma polynomials of pellytopes, with simple negative h-roots

## Finding
For every integer \(n\ge1\), consider the \(n\)-dimensional pellytope \(P_n\) defined in the next section. Let \(f_k(P_n)\) denote its number of \(k\)-dimensional faces, with \(f_n(P_n)=1\), and put \(F_n(z)=\sum_{r=0}^n f_{n-r}(P_n)z^r\). Then
\[
F_0(z)=1,\qquad F_1(z)=1+2z,\qquad
F_n(z)=(1+2z)F_{n-1}(z)+z(1+z)F_{n-2}(z)\quad(n\ge2).
\]
In particular, the **complete face polynomial** has the closed form
\[
\boxed{F_n(z)=\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n-j}{j}
 z^j(1+z)^j(1+2z)^{n-2j}}
\]
and its dimension generating function is
\[
\sum_{n\ge0}F_n(z)u^n=\frac{1}{1-(1+2z)u-z(1+z)u^2}.
\]
The (simple-polytope) \(h\)-polynomial and \(\gamma\)-polynomial are exactly
\[
\boxed{h_n(t)=(1-t)^n F_n\!\left(\frac{t}{1-t}\right)
=\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n-j}{j}
 t^j(1+t)^{n-2j}},\qquad
\boxed{\gamma_n(y)=\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n-j}{j}y^j}.
\]
Thus \(\gamma_n(y)\) is the matching-generating polynomial of the path on \(n\) vertices. Moreover, **all \(n\) zeros of \(h_n\) are real, strictly negative and pairwise distinct**, with explicit factorization
\[
\boxed{h_n(t)=(1+t)^{n-2m}\prod_{j=1}^m
\left((1+t)^2+4t\cos^2\frac{j\pi}{n+1}\right)},\qquad
m=\lfloor n/2\rfloor.
\]

## Assumptions and scope
Let \(e_1,\ldots,e_n\) be the standard basis of \(\mathbb R^n\), and define the standard pellytope (equivalently the \(d=2\) member of the Catalan-pellytope interpolation) by
\[
P_n=\sum_{i=1}^n\operatorname{conv}\{0,e_i\}+
\sum_{i=1}^{n-1}\operatorname{conv}\{0,e_i,e_i+e_{i+1}\}.
\]
All sums are Minkowski sums. The combinatorial statements hold for all \(n\ge1\). The convention \(P_0=\{0\}\) is used only for recurrences. The face polynomial includes the full polytope, but excludes the empty face. The \(h\)-polynomial convention is \(h_n(t)=(1-t)^nF_n(t/(1-t))\), standard for an \(n\)-dimensional simple polytope.

## Proof
**Step 1: the established normal-fan construction.** Proposition 3.1 of Bossinger–Telek–Tillmann-Morris proves that the inner normal fan \(\Sigma_n\) is simplicial. In passing from \(n-1\) to \(n\), start with \(\Sigma_{n-1}\times\Sigma_1\), where \(\Sigma_1\) is the two-ray fan of an interval. The sole new ray \(e_{n-1}-e_n\) subdivides the two-dimensional cone spanned by \(e_{n-1}\) and \(-e_n\). This is the stellar subdivision at that cone. Its link is the link of the endpoint ray \(e_{n-1}\) in \(\Sigma_{n-1}\), combinatorially \(\Sigma_{n-2}\) by Lemma 3.3 of the same paper (and for \(n=2\) it is the fan of a point). The papers are cited for this existing geometric input; the next enumerations are not presented there as the formula in this result.

**Step 2: enumerate every fan cone.** For a simplicial fan \(\Sigma\), set \(C_\Sigma(z)=\sum_{\sigma\in\Sigma}z^{\dim\sigma}\), including the zero cone. Taking the product with the interval fan multiplies \(C\) by \(1+2z\). A stellar subdivision of a two-cone \(\tau=\langle v,w\rangle\) removes the cones containing both \(v,w\), contributing \(z^2 C_{\operatorname{link}(\tau)}(z)\), and replaces them with cones based on the new ray and either no old ray or exactly one of \(v,w\), contributing \(z(1+2z)C_{\operatorname{link}(\tau)}(z)\). Thus the exact change is \(z(1+z)C_{\operatorname{link}(\tau)}(z)\). In \(\Sigma_{n-1}\times\Sigma_1\) the link is \(\Sigma_{n-2}\), so
\[
C_{\Sigma_n}(z)=(1+2z)C_{\Sigma_{n-1}}(z)+z(1+z)C_{\Sigma_{n-2}}(z).
\]
Normal cones to \(k\)-faces of a simple \(n\)-polytope have dimension \(n-k\); therefore \(F_n=C_{\Sigma_n}\). The initial fans yield \(F_0=1\), \(F_1=1+2z\).

**Step 3: solve the recurrence and transform.** Tile a row of length \(n\) with singleton blocks of weight \(1+2z\) and adjacent domino blocks of weight \(z(1+z)\). Choosing exactly \(j\) dominoes leaves \(n-2j\) singletons and has \(\binom{n-j}{j}\) placements. This gives the boxed face polynomial. Summing its recurrence gives the rational bivariate generating function. Under \(z=t/(1-t)\), the singleton and domino factors transform respectively into \((1+t)/(1-t)\) and \(t/(1-t)^2\). Multiplication by \((1-t)^n\) yields the stated \(h\)-expansion and its coefficient \(\binom{n-j}{j}\). A size-\(j\) matching in a path of \(n\) vertices is a choice of \(j\) nonconsecutive edges among \(n-1\), counted by the same binomial coefficient.

**Step 4: prove exact root structure.** The path-matching polynomial \(\gamma_n(y)\) obeys \(\gamma_0=\gamma_1=1\) and \(\gamma_n=\gamma_{n-1}+y\gamma_{n-2}\). The adjacency matrix of a path with \(n\) vertices has eigenvalues \(2\cos(j\pi/(n+1))\), \(1\le j\le n\). Its characteristic polynomial, or the same two-term determinant recurrence, gives
\[
\gamma_n(y)=\prod_{j=1}^{m}\left(1+4y\cos^2\frac{j\pi}{n+1}\right),\quad m=\lfloor n/2\rfloor.
\]
Inserting \(y=t/(1+t)^2\) proves the boxed factorization. For \(1\le j\le m\), each angle is strictly between zero and \(\pi/2\). Each quadratic factor is \(t^2+(2+4c_j^2)t+1\) with \(c_j=\cos(j\pi/(n+1))>0\): its discriminant is strictly positive and its two roots are distinct, reciprocal and negative. Distinct \(j\) yield distinct positive \(c_j^2\), hence no root shared across factors (subtract two factor equations to get \(4t(c_j^2-c_k^2)=0\), while \(t=0\) is not a root). If \(n\) is odd, the extra \(1+t\) contributes a single root \(-1\); no quadratic vanishes there. This establishes \(n\) distinct strictly negative roots for all \(n\ge1\).

## Verification
A standalone Python 3 checker, `verify_pellytope_faces.py`, is included. It constructs chord-labelled rays and tests every subset for compatibility in dimensions \(1\) through \(7\), independently reproducing the complete face counts from the chord model, not using the recurrence. It additionally verifies the \(h\)/face transforms, matches the \(\gamma\)-coefficients to enumerated path matchings, and tests the recurrence and \(h\)-identities through dimension \(50\), with **201 exact assertions passed**. Example coefficient lists \((f_n,f_{n-1},\ldots,f_0)\) are \((1,11,40,58,29)\) in dimension four and \((1,14,71,164,175,70)\) in dimension five. Finite computations corroborate, but do not replace, Steps 1–4 of the unrestricted proof.

## Relationship to prior work
The 2026 Bossinger–Gürdoğan work studies Catalan pellytopes and their normal fans and vertex enumerations; the polytope above is the pellytope endpoint. The 2024 Bossinger–Telek–Tillmann-Morris paper provides the essential stellar-subdivision and link identities, as well as the known number of facets and Pell-number vertex enumeration. He–Li–Raman–Zhang introduced the same family of geometric examples and gave facet and vertex counts in 2020. Volodin's work establishes broad \(\gamma\)-positivity and flag-complex realizations for 2-truncated cubes, which covers general qualitative positivity considerations but does not specify the exact path-matching \(\gamma\)-polynomial or all-rank face counts of this particular family. The new assertion is the closed all-face enumeration and exact root spectrum; the fan construction, Pell vertex recurrence, and generic \(\gamma\)-positivity are not asserted as new.

## Limitations
The theorem concerns the standard pellytope endpoint, not the entire two-parameter Catalan-pellytope family. The root conclusion is about the combinatorial \(h\)-polynomial, not the Ehrhart \(h^*\)-polynomial. The statement does not address Euclidean volume, metric geometry, or a closed form for other interpolation depths. Historical novelty is provisionally assessed rather than independently certified; equivalent enumerations might exist in unindexed literature.

## References
1. L. Bossinger and Ö. Gürdoğan, *A combinatorial interpolation between the hypercube and the associahedron*, arXiv:2609.38456v1, first public 2026-09-29. https://arxiv.org/abs/2609.38456
2. L. Bossinger, M. L. Telek, H. Tillmann-Morris, *Binary geometries from pellytopes*, arXiv:2410.08002v1, Proposition 3.1 and Lemma 3.3. https://arxiv.org/abs/2410.08002
3. S. He, Z. Li, P. Raman, C. Zhang, *Stringy canonical forms and binary geometries from associahedra, cyclohedra and generalized permutohedra*, arXiv:2005.07395. https://arxiv.org/abs/2005.07395
4. V. D. Volodin, *Geometric realization of the gamma-vectors of 2-truncated cubes*, arXiv:1210.0398. https://arxiv.org/abs/1210.0398
