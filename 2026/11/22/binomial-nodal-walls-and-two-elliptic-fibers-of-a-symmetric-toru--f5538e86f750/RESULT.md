# Binomial nodal walls and two elliptic fibers of a symmetric torus sextic pencil

## Finding

For each integer \(n\ge3\), put
\[
G=\sum_{i=1}^{n} X_i^2,\qquad H=\sum_{i=1}^{n}X_i^3,
\qquad X_{n,t}=V(G^3+tH^2)\subset\mathbb P^{n-1}_{\mathbb C},\quad t\in\mathbb C^\times.
\]
Every \(X_{n,t}\) is geometrically integral. The complete **reduced singular support** is the smooth complete intersection \(B=V(G,H)\), plus a finite collection of ordinary quadratic nodes precisely at the parameter walls \(t=-k\), \(1\le k\le n\). At the wall \(t=-k\), the nodes are exactly
\[
P_S=[\mathbf 1_{i\in S}]_{i=1}^{n},\qquad
S\subseteq\{1,\ldots,n\},\quad |S|=k,
\]
so their exact number is \(\binom nk\). Along \(B\), the analytic singularity is transversely an ordinary cusp \(u^3+tv^2=0\). No further singular points occur.

For \(n=3\), \(B\) consists of six distinct cusps. The complete plane-sextic singularity and normalization-genus census is:

| Parameter | Additional nodes | Total singularity basket | Normalization genus |
|---|---:|---|---:|
| \(t\notin\{0,-1,-2,-3\}\) | 0 | \(6A_2\) | 4 |
| \(t=-1\) | 3 | \(6A_2+3A_1\) | 1 |
| \(t=-2\) | 3 | \(6A_2+3A_1\) | 1 |
| \(t=-3\) | 1 | \(6A_2+A_1\) | 3 |

The nodes at the first two walls are respectively the three coordinate vertices and the three projective points with two coordinates equal to one and the third zero. The single node at \(t=-3\) is \([1:1:1]\). The two genus-one specializations are integral, and their normalizations are elliptic curves over \(\mathbb C\).

## Assumptions and scope

Everything is over \(\mathbb C\), and all hypersurfaces are the ordinary projective hypersurfaces in the stated dimension. Only finite, nonzero \(t\) are covered. The limits \(t=0\) and \(t=\infty\), which give a triple conic and double cubic in the plane, are deliberately excluded. An ordinary quadratic node in dimension \(n-2\) means a hypersurface singularity with nondegenerate quadratic term on an affine chart. The statement concerns the reduced support of the Jacobian singular scheme, not its nonreduced infinitesimal structure along the cusp locus.

## Proof

**(1) Base locus.** The forms \(G,H\) meet transversally. Indeed, a projective point where their gradients are dependent has all its nonzero coordinates equal: the equality \(3X_i^2=\lambda\,2X_i\) forces every nonzero coordinate to have one common value \(a\ne0\). If there are \(k\ge1\) such coordinates, then \(G=ka^2\ne0\), excluding a point of \(B\). Therefore \(B\) is a smooth complete intersection of degrees two and three; for \(n=3\), Bézout gives exactly six reduced points. Near any point of \(B\), \(u=G,v=H\) extend to analytic coordinates, and the defining equation is precisely \(u^3+tv^2=0\). Since \(t\ne0\), this is \(A_2\) times a smooth factor of dimension \(n-3\).

**(2) Exhaustion of singularities away from \(B\).** If \(F_t=G^3+tH^2=0\) and a point lies outside \(B\), neither \(G\) nor \(H\) can vanish, and necessarily \(t=-G^3/H^2\). The singular gradient equations then become
\[
3H\,\partial_iG-2G\,\partial_iH
=6X_i(H-GX_i)=0\quad\text{for every }i.
\]
Thus every nonzero coordinate is \(H/G\); upon projective scaling, the point is some indicator point \(P_S\). Writing \(k=|S|\), one has \(G(P_S)=H(P_S)=k\), so
\[
F_t(P_S)=k^2(k+t).
\]
Consequently these points lie on the hypersurface, and are singular, if and only if \(t=-k\), with exactly \(\binom nk\) of them. This describes every possible singular point outside \(B\), including points on coordinate hyperplanes.

**(3) Exact local quadratic form.** At \(P_S\) with \(t=-k\), put \(s_i=\mathbf 1_{i\in S}\). The full homogeneous Hessian is
\[
\operatorname{Hess}F_{-k}(P_S)
=6k\,ss^{\mathsf T}-6k^2 I_S+6k^2 I_{S^c},
\]
where \(I_S\) and \(I_{S^c}\) are coordinate-projector matrices. The radial vector \(s\) spans its kernel. On the \((k-1)\)-dimensional subspace of vectors supported in \(S\) with coordinate sum zero, its eigenvalue is \(-6k^2\); on the \((n-k)\)-dimensional complementary-coordinate subspace, the eigenvalue is \(+6k^2\). Both are nonzero over \(\mathbb C\), so the Hessian induced on projective tangent directions has rank \(n-1\). The analytic Morse lemma gives an ordinary quadratic node, not a worse singularity, for each such \(P_S\).

**(4) Geometric integrality.** First consider \(n=3\). The six base points are unibranch \(A_2\) cusps, so an irreducible component of the sextic passing through one base point contains the unique local branch. Let \(C\) be any irreducible component of degree \(e\). Since \(G\) cannot divide \(F_t\), Bézout with the conic \(G=0\) shows \(C\) meets it only at base points. A smooth-cusp parametrization gives \(G\) local vanishing order two along the unique branch, so the intersection number is \(2e=2r\), where \(r\) is the number of base cusps carried by \(C\). Hence \(r=e\). Each ordinary cusp contributes delta invariant one, so the plane genus bound gives \((e-1)(e-2)/2\ge e\). For \(1\le e\le 4\) this fails, hence every irreducible component has degree at least five. As the total degree is six, exactly one component is possible; it occurs with multiplicity one because the six base cusps are reduced and unibranch. Thus every plane member is geometrically integral.

For \(n>3\), restrict to the coordinate plane \(X_4=\cdots=X_n=0\). The restriction is the irreducible three-variable polynomial just proved. A nontrivial homogeneous factorization of \(F_t\) in more variables would restrict to a factorization into nonzero, positive-degree homogeneous polynomials on this plane, contradicting irreducibility. Thus all higher-dimensional members are geometrically integral too.

**(5) Plane geometric genus.** An integral sextic has arithmetic genus \((6-1)(6-2)/2=10\). The six fixed cusps each contribute \(\delta=1\); each extra ordinary node contributes \(\delta=1\). Therefore the geometric genus is \(10-6-\binom{3}{k}\) at \(t=-k\) (for \(k=1,2,3\)) and \(10-6=4\) at every other nonzero parameter. These values are respectively \(1,1,3\) and \(4\), proving the table.

## Verification

The self-contained `checker.py` evaluates the defining polynomial, its gradient, and its exact Hessian at each representative indicator point for all \(3\le n\le7\), checks the asserted Hessian matrix, verifies the radial kernel and a nonzero projective Hessian determinant, and checks the subset counts. It uses exact symbolic arithmetic, prints the node-count vector for each dimension, and succeeds. This finite checker corroborates the formulas; Steps (1)–(5), not finite enumeration, prove them for all integers \(n\ge3\). The arithmetic genus and delta computations are explicit in Step (5).

## Relationship to prior work

Cogolludo-Agustín and Elduque (arXiv:2507.15814, first submitted 21 July 2025) study fundamental groups of generic fiber-type curves and explicitly discuss sextic pencils formed by a cube of a conic plus a square of a cubic (their Example 5.5). Their results concern generic fibers and complement fundamental groups, not the exact special-fiber count of the symmetric power-sum pencil above. Oka and Pho (arXiv:math/0201035) already classify possible torus-sextic singularity baskets, including \(6A_2+3A_1\); thus that basket and its genus are emphatically **not** claimed as new. What is claimed here is the explicit complete parameter-wall classification for the displayed symmetric pencil, the two distinct genus-one fibers within it, and the dimension-uniform binomial node formula.

A related earlier classification of modular power-sum complete intersections and a different Fermat–Ceva pencil have quite different equations, fields or singular loci; neither yields the displayed wall count by specialization. Searches of accessible mathematical records and algebraic-geometry literature located no equivalent parameter classification for this particular family, but an unindexed classical symmetric-power-sum calculation could exist.

## Limitations

The base-locus Jacobian scheme structure (beyond the proved local analytic cusp normal form), global monodromy, fundamental groups of special-fiber complements, and the nonreduced limiting fibers \(t=0,\infty\) are not classified. No assertion of publication priority or independent verification is made. The infinite-dimensional-index statement rests on the proof; the finite checker alone would not establish it.

## References

1. J. I. Cogolludo-Agustín and E. Elduque, *The fundamental group of the complement of a generic fiber-type curve*, arXiv:2507.15814 (2025), https://arxiv.org/abs/2507.15814; published in *Journal of the London Mathematical Society* (2026), https://doi.org/10.1112/jlms.70547. See Definition 1.1, Condition 1.4, and Example 5.5.
2. M. Oka and D. T. Pho, *Classification of sextics of torus type*, arXiv:math/0201035 (2002), https://arxiv.org/html/math/0201035v1; see the singularity-configuration table, entry `nt19`.
3. G. Sticlaru, *Plane curves attaining the Dimca–Sernesi bound and Jacobian syzygies of pencil-type curves*, arXiv:2611.25767 (19 November 2026), https://arxiv.org/abs/2611.25767; later supporting context about generic torus-type curves, not a prior source for the specific parameter census.
