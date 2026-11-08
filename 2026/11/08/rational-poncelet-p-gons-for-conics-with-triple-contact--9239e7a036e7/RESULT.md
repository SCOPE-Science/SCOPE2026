# Rational Poncelet \(p\)-gons for conics with triple contact

## Finding

Let \(q=p^r\) be a power of an odd prime, and let \((C,D)\) be an **ordered** pair of distinct smooth conics over \(\mathbb F_q\). Assume their geometric intersection divisor on \(C\) is \(3P+Q\), where \(P\ne Q\). A *rational simple Poncelet \(p\)-gon* means a cyclic sequence of \(p\) pairwise distinct \(\mathbb F_q\)-points on \(C\), with each consecutive joining line tangent to \(D\), counted modulo cyclic rotation and reversal. Every tangent point on \(D\) is then automatically rational. The number of such polygons is exactly

\[
\boxed{N_q(C,D)=\frac{q-p}{2p}=\frac{p^{r-1}-1}{2}.}
\]

All ordered conic pairs with the stated intersection type are \(\operatorname{PGL}_3(\mathbb F_q)\)-equivalent. Thus the count is universal; in particular, **there is no rational simple polygon over the prime field**, whereas one exists over every proper finite extension \(\mathbb F_{p^r}\) with \(r\ge2\). The polygon length is \(p\), not an arbitrary positive integer. For example \(N_3=0\), \(N_9=1\), \(N_5=0\), and \(N_{25}=2\).

## Assumptions and scope

The base field is \(k=\mathbb F_q\) with odd characteristic \(p\). The conics \(C,D\subset\mathbb P^2_k\) are smooth and distinct, and the geometric intersection multiplicities are exactly \((3,1)\). The length \(p\) is the field characteristic. The count concerns polygons with *all vertices and sides defined over* \(k\), not merely polygons over its algebraic closure or the existence of a geometric Poncelet orbit. A cyclic polygon is simple here when its vertices are pairwise distinct; the proof also shows its tangent lines are pairwise distinct. A tangent line to a smooth conic defined over \(k\) has a unique geometric tangency point, necessarily \(k\)-rational by Frobenius invariance.

## Proof

**1. Normal form over the ground field.** The unique triple-contact point \(P\) and the unique residual point \(Q\) are fixed by Frobenius and hence are \(k\)-rational. Since \(C\) is a smooth conic containing \(P\), it is \(k\)-isomorphic to \(\mathbb P^1\). A projective change of coordinates over \(k\) carries \(C\) to \(XZ-Y^2=0\), and the ordered points \((P,Q)\) to \(([1:0:0],[0:0:1])\). On the parametrization \([T:U]\mapsto[T^2:TU:U^2]\), a quadratic form defining \(D\), restricted to \(C\), has divisor \(3[1:0]+[0:1]\); it is therefore a nonzero multiple of \(TU^3\), the restriction of \(YZ\). Since the kernel of restriction of plane quadrics to \(C\) is spanned by \(XZ-Y^2\), the equation of \(D\) has the form \(\alpha(XZ-Y^2)+\beta YZ=0\). Here \(\beta\ne0\) by distinctness, and \(\alpha\ne0\), because otherwise \(D\) is the singular conic \(YZ=0\). After division by \(\alpha\), the transformation \((X,Y,Z)=(c^2X',cY',Z')\), with \(c=\beta/\alpha\), gives

\[
C:\ XZ-Y^2=0,\qquad D:\ XZ-Y^2+YZ=0.
\]

Both are smooth in odd characteristic, and their intersection divisor is indeed \(3P+Q\). This proves universal projective equivalence, not merely equivalence over an algebraic closure.

**2. Explicit incidence correspondence.** Away from the common contact point at infinity, write

\[
c(t)=[t^2:t:1]\in C,\qquad d(s)=[s^2-s:s:1]\in D.
\]

The tangent at \(d(s)\) is \(L(s): X+(1-2s)Y+s^2Z=0\). It contains \(c(t)\) precisely when

\[
t^2+(1-2s)t+s^2=(s-t)^2+t=0.
\]

Consequently, every finite rational incidence flag \((c(t),L(s))\) is uniquely parametrized by \(u=s-t\in k\):

\[
t=-u^2,\qquad s=u-u^2.
\]

The only flag outside this affine parametrization is the common contact flag at infinity, which cannot lie on a simple polygon. The other intersection of \(L(s)\) with \(C\) is \(c(t')\), where \(t'=2s-1-t=-(u-1)^2\). The other tangent to \(D\) through \(c(t')\) has parameter \(s'=2t'-s=(u-1)-(u-1)^2\). Thus the Poncelet transition on finite flags is exactly

\[
\boxed{u\longmapsto u-1.}
\]

This identity is valid in every odd characteristic, including at repeated-root flags; those are subsequently excluded by simplicity.

**3. Exact orbit and degeneracy calculation.** Every orbit of the translation is a coset \(u+\mathbb F_p\) of length \(p\); there are \(q/p\) such oriented flag cycles. Its vertices have parameters \(t_i=-(u-i)^2\) for \(i\in\mathbb F_p\). For distinct \(i,j\), the equality \(t_i=t_j\) is equivalent to \(2u=i+j\). Since \(p\) is odd, this occurs for some distinct \(i,j\) exactly when \(u\in\mathbb F_p\). Hence precisely the single coset \(\mathbb F_p\) is degenerate. For every other coset, all \(p\) vertices are distinct; the tangent parameters \(s_i=(u-i)-(u-i)^2\) are also pairwise distinct, because equality for distinct indices would imply \(2u\in\mathbb F_p\).

For the same vertex \(t=-u^2\), its two rational tangent flags have parameters \(u\) and \(-u\). Switching them reverses the polygon, pairing the translation cosets \(u+\mathbb F_p\) and \(-u+\mathbb F_p\). A nondegenerate coset is never fixed by this pairing, as equality would imply \(2u\in\mathbb F_p\), hence \(u\in\mathbb F_p\). Moreover, two simple polygons sharing a vertex and a tangent are the same oriented cycle by determinism of the transition; sharing only the vertex yields either that cycle or its reversal. Thus there is no additional identification. Dividing the \(q/p-1\) good oriented cycles by two proves

\[
N_q(C,D)=\frac12\left(\frac qp-1\right)=\frac{q-p}{2p}.
\]

The prime-field obstruction and all-extension existence follow immediately.

## Verification

Two independent standalone programs are included. Run them from the package directory as follows:

```sh
python3 verify_flags.py
python3 verify_translation.py
```

The first program constructs finite-field operations without third-party libraries and **independently enumerates all rational incidences** between each parametrized vertex and each tangent line. It follows the two geometric involutions, removes non-simple cycles, and identifies reversal pairs. It checks \(\mathbb F_p\) and \(\mathbb F_{p^2}\) for \(p=3,5,7,11\); the geometric enumeration gives respectively \(0,1,0,2,0,3,0,5\) unoriented polygons. The second program checks the coordinate identities over exact integer polynomial rings using a self-contained implementation and independently verifies the coset/reversal counts for \(p=3,5,7,11,13\). All executions completed successfully. These finite checks are corroboration only; the proof above covers every odd prime power.

## Relationship to prior work

Jow and Liang, *Poncelet's theorem for conics in any position and any characteristic*, arXiv:2112.11770 (first public December 22, 2021), Theorem 3.1 and Proposition 2.8, prove geometric \(p\)-periodicity and the cuspidal nature of the incidence correspondence when the intersection type is \((3,1)\). Those geometric facts are acknowledged; their statement is over an algebraically closed field and does not count simple rational polygons or identify the prime-field obstruction.

Hungerbühler and Kusejko, *A Poncelet criterion for special pairs of conics in* \(PG(2,p^m)\), 2020, study a **nested, disjoint** diagonal conic pencil and an associated arithmetic period criterion; their conic pairs cannot have intersection type \((3,1)\). Radnović and Ragas, *Poncelet triangles and tetragons over finite fields*, arXiv:2511.06347 (first public November 9, 2025), count conic pairs satisfying geometric closure conditions for triangles and tetragons; in their Section 2, being a Poncelet pair is defined over the algebraic closure. Their results do not give the number of *fully rational simple polygons* for an individual triple-contact pair, or the all-prime formula established here. Chipalkatti, arXiv:1604.00436, studies the transverse Poncelet triangle condition, a different intersection regime.

## Limitations

The result is restricted to odd characteristic and intersection type \((3,1)\); it does not address type \((4)\), other nontransverse types, or general transverse Poncelet pairs. It counts simple polygons with all vertices and edges defined over the base field, not all geometric closure cycles. The arithmetic count is a derived result beyond the established geometric porism but is not a claim to originality of the latter. The theorem and computations have received no independent mathematical audit. A historically equivalent finite-geometric count in different terminology remains a priority risk.

## References

1. S.-Y. Jow and C.-T. Liang, *Poncelet's theorem for conics in any position and any characteristic*, arXiv:2112.11770, first submitted 2021-12-22; *Communications in Algebra* 51 (2023), 3510–3520. https://arxiv.org/abs/2112.11770
2. N. Hungerbühler and K. Kusejko, *A Poncelet criterion for special pairs of conics in* \(PG(2,p^m)\), *International Electronic Journal of Geometry* 13 (2020), 21–40. https://doi.org/10.36890/iejg.590595
3. M. Radnović and R. Ragas, *Poncelet triangles and tetragons over finite fields*, arXiv:2511.06347, first submitted 2025-11-09; *Finite Fields and Their Applications* 112 (2026), 102815. https://arxiv.org/abs/2511.06347
4. J. Chipalkatti, *On the Poncelet triangle condition over finite fields*, arXiv:1604.00436, first submitted 2016-04-01. https://arxiv.org/abs/1604.00436
