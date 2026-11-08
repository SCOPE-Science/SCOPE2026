# Frobenius zeta formula and fifteen incidence profiles for the sixteen-line complement of a quartic del Pezzo surface

## Finding
Let \(X\) be a smooth del Pezzo surface of degree \(4\) over a finite field \(\mathbb F_q\) of odd characteristic. Let \(D\) be the reduced union of all sixteen geometric exceptional \((-1)\)-curves, considered as a Galois-invariant divisor, and set \(U=X\setminus D\). Write \(g\in W(D_5)\) for the Frobenius action on their configuration.

The group \(W(D_5)\) acts on the sixteen vertices \(V\) and forty edges \(E\) of the exceptional-curve intersection graph. Define \(m(g)\) as the number of fixed vertices, \(a(g)\) as the number of edges fixed pointwise on their two endpoints, \(b(g)\) as the number of edges whose endpoints are interchanged, and \(\tau(g)=\operatorname{tr}(g\mid\operatorname{Pic}(\overline X)\otimes\mathbb Q)\). Then

\[
\boxed{\#U(\mathbb F_{q^n})=q^{2n}+\tau(g^n)q^n+1-m(g^n)(q^n+1)+a(g^n)-b(g^n)}
\]
for every integer \(n\geq 1\). In particular, across the \(1920\) elements of \(W(D_5)\), exactly fifteen tuples \((\tau,m,a,b)\) occur, giving fourteen distinct quadratic expressions for \(\#U(\mathbb F_q)\). These are formal Weyl-group possibilities; a particular tuple need not be realized by a surface over every small field.

Let \(P\) be the six-dimensional rational Picard representation, \(\mathbb Q[V]\) the vertex-permutation representation, and \(\mathbb Q[E]^-\) the forty-dimensional *signed-edge representation* with basis an orientation of each edge and sign reversal when its endpoints are swapped. The entire Hasse–Weil zeta function is

\[
\boxed{Z(U,T)=\frac{\det(1-Tg\mid\mathbb Q[V])\det(1-qTg\mid\mathbb Q[V])}{(1-T)(1-q^2T)\det(1-qTg\mid P)\det(1-Tg\mid\mathbb Q[E]^-)}.}
\]

Here \(Z(U,T)=\exp(\sum_{n\ge 1}\#U(\mathbb F_{q^n})T^n/n)\), and determinants are polynomials in \(T\). The formula determines all extension-field counts from one finite permutation-with-sign action.

The exhaustive profile census is:

| \(\tau\) | \(m\) | \(a\) | \(b\) | Elements of \(W(D_5)\) | \(\#U(\mathbb F_q)\) |
|---:|---:|---:|---:|---:|---|
| -2 | 0 | 0 | 0 | 20 | \(q^2-2q+1\) |
| -2 | 0 | 0 | 8 | 5 | \(q^2-2q-7\) |
| -1 | 0 | 0 | 0 | 80 | \(q^2-q+1\) |
| 0 | 0 | 0 | 0 | 360 | \(q^2+1\) |
| 0 | 0 | 0 | 4 | 60 | \(q^2-3\) |
| 1 | 0 | 0 | 0 | 160 | \(q^2+q+1\) |
| 1 | 0 | 0 | 2 | 160 | \(q^2+q-1\) |
| 1 | 1 | 0 | 0 | 384 | \(q^2\) |
| 1 | 2 | 0 | 0 | 160 | \(q^2-q-1\) |
| 2 | 0 | 0 | 0 | 130 | \(q^2+2q+1\) |
| 2 | 2 | 1 | 1 | 240 | \(q^2-1\) |
| 2 | 4 | 2 | 2 | 60 | \(q^2-2q-3\) |
| 3 | 4 | 4 | 0 | 80 | \(q^2-q+1\) |
| 4 | 8 | 12 | 0 | 20 | \(q^2-4q+5\) |
| 6 | 16 | 40 | 0 | 1 | \((q-5)^2\) |

The tabulated element counts sum to \(1920\). The last row is the completely split case and is *already implied by* the point-count calculation of Banwait–Fité–Loughran; the contribution here is the full non-split incidence spectrum and the uniform zeta identity.

## Assumptions and scope
A *degree-four del Pezzo surface* means a smooth projective geometrically integral surface with ample anticanonical divisor and \(K_X^2=4\). Every geometric exceptional curve is a smooth rational \((-1)\)-curve, and in odd characteristic these are precisely the sixteen lines of the anticanonical embedding as the intersection of two quadrics in \(\mathbb P^4\). The Galois-invariant union \(D\) is defined even when none of its individual components descends to \(\mathbb F_q\). All counts concern geometric curves removed from the surface, not merely the curves individually rational over the ground field.

The intersection graph has sixteen vertices, forty edges, degree five at each vertex, and no triangles. Adjacent exceptional curves intersect transversally at one geometric point. The vertex set is modeled by the even-weight bit vectors \(v\in\mathbb F_2^5\), with adjacency iff the Hamming distance is four. The Weyl group is \(2^4\rtimes S_5\); its elements are \((\pi,s)\) with \(\pi\in S_5\) and even-weight \(s\), acting by \(v\mapsto\pi(v)+s\). This action is faithful and equals the full automorphism group of the intersection configuration.

## Proof
**1. Rational points of the surface.** The geometric Picard group has rank six; its canonical class is fixed and its orthogonal complement is the rank-five root lattice of type \(D_5\). The Weyl-group element \((\pi,s)\) acts as the signed permutation \(e_i\mapsto (-1)^{s_{\pi(i)}}e_{\pi(i)}\) on the standard five-dimensional module. Hence

\[
\tau(\pi,s)=1+\sum_{\pi(i)=i}(-1)^{s_i}.
\]

The cohomological point-count formula for smooth rational surfaces gives \(\#X(\mathbb F_{q^n})=q^{2n}+\tau(g^n)q^n+1\).

**2. Rational points of the sixteen-curve divisor.** Fix \(n\ge 1\) and write \(Q=q^n\). Each Frobenius-fixed component is a smooth \(\mathbb P^1\) over \(\mathbb F_Q\), contributing \(Q+1\) points. If two such components intersect, their common rational point has been counted twice and is subtracted once; there are \(a(g^n)\) such edges. If a rational point belongs to a nonfixed geometric component, Frobenius sends that component to another one through the same point. Because the graph is triangle-free, at most two components pass through any geometric point, so the two must be interchanged, and their intersection contributes precisely one rational point. These are exactly the \(b(g^n)\) swapped edges. There are no other rational points of \(D\). Consequently

\[
\#D(\mathbb F_Q)=m(g^n)(Q+1)-a(g^n)+b(g^n).
\]

Subtracting this from the surface count proves the boxed formula for all \(n\).

**3. Zeta factorization.** The character of \(\mathbb Q[V]\) at \(g^n\) is \(m(g^n)\). Orient each edge arbitrarily; the signed-edge representation acts by permuting oriented edges, negating a basis vector if the orientation is reversed. Its character at \(g^n\) is \(a(g^n)-b(g^n)\). For a finite-dimensional representation \(R\), the formal identity

\[
-\log\det(1-Tg\mid R)=\sum_{n\ge1}\operatorname{tr}(g^n\mid R)T^n/n
\]

turns the extension-field point-count formula into the displayed rational zeta function, with \(P\) the Picard representation. No conjectural cohomology computation is used.

**4. Exhaustive Weyl-group census.** Enumerate all \(120\) permutations \(\pi\) of five coordinates and all \(16\) even-weight translations \(s\). In the explicit sixteen-vertex model count fixed vertices, edges with fixed endpoints, and edges with exchanged endpoints; compute \(\tau\) using the signed-coordinate trace. The accompanying exact finite verification program enumerates all \(1920\) group elements and reproduces each row, verifying that the fifteen row frequencies total \(1920\), that they aggregate into eighteen conjugacy classes, and that exactly fourteen distinct count polynomials result. This enumeration is genuinely exhaustive because \(W(D_5)=2^4\rtimes S_5\), not a sample of Galois actions.

## Verification
Run the two standalone standard-library Python files with `python3 verify_frobenius.py` and `python3 verify_geometry.py`. The first reproduces the complete \(1920\)-element profile census, the eighteen conjugacy classes (by conjugation closure), the fourteen polynomials, and the signed-edge trace identities for powers through ten. The second independently enumerates \(\mathbb P^2(\mathbb F_p)\) minus a conic and ten chords through five geometric base points, using two families. For five rational points it tests \(p\in\{5,7,11,13,17,19\}\), obtaining the previously known split value \((p-5)^2\). For three rational points and one conjugate pair over \(\mathbb F_{p^2}\), it uses exact quadratic-extension arithmetic for \(p\in\{5,7,11,13\}\) and obtains \(p^2-4p+5\), the row \((\tau,m,a,b)=(4,8,12,0)\). The blow-up is an isomorphism away from the base points; all exceptional divisors are removed, so these plane complements coincide with \(U(\mathbb F_p)\).

The group census proves a finite combinatorial fact; the geometric and cohomological arguments, not finite-field tests, prove the general theorem for every eligible \(q\) and every extension degree.

## Relationship to prior work
Kunyavskii–Skorobogatov–Tsfasman established the sixteen-line configuration, its \(W(D_5)\) action, and the related arithmetic of quartic del Pezzo surfaces. Banwait–Fité–Loughran computed Frobenius traces of complete del Pezzo surfaces over finite fields; their Lemma 3.2 and Corollary 3.3 imply the *split* \((q-5)^2\) formula, which is not claimed as new. Darwin studied quadratically enriched counts of the sixteen lines over perfect fields, with a different enumerative objective. The present statement refines the complete-surface trace by giving the non-split complement's rational-point profiles and the signed-edge zeta factorization for every extension degree. It is an exact derived arithmetic invariant of the established incidence configuration, not a new classification of the surfaces themselves.

## Limitations
The fifteen rows classify abstract Weyl-group incidence profiles, not which profiles are realizable over each particular small \(\mathbb F_q\). Distinct Frobenius conjugacy classes can share a row or a ground-field count polynomial while having different higher-degree zeta data; the determinant formula retains that information. The sixteen geometric curves need not be defined individually over the base field. No claim is made for singular del Pezzo surfaces, other degrees, or arithmetic stability/moduli interpretations requiring further hypotheses. The construction uses classical intersection-graph and Picard representations; priority over older equivalent group-theoretic incidence tables is a residual literature risk.

## References
1. C. Darwin, *A quadratically enriched count of lines on a degree 4 del Pezzo surface*, arXiv:2205.04456, first public version 2022-05-09. https://arxiv.org/abs/2205.04456
2. B. Banwait, F. Fité, D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300, especially Lemma 3.2, Corollary 3.3, and Section 3.2. https://arxiv.org/abs/1606.00300
3. B. È. Kunyavskii, A. N. Skorobogatov, M. A. Tsfasman, *Del Pezzo surfaces of degree four*, Mémoires de la Société Mathématique de France 37 (1989), Sections 0 and 3. https://www.numdam.org/item/MSMF_1989_2_37__1_0/
