# Frobenius arithmetic of the Chilean twelve-conic divisor

## Finding

Let \(k=\mathbb F_q\) have characteristic at least five, and let \(E\subset\mathbf P^2_k\) be a smooth plane cubic with \(j(E)\ne0\). Let \(V\) be the geometric set of nine inflection points of \(E\), identified as an affine plane over \(\mathbb F_3\); let \(\mathcal P\subset(\mathbf P^2_k)^\vee\) be the nine points representing their tangent lines. For each of the twelve affine lines \(\ell\subset V\), there is a unique smooth conic \(C_\ell\) through the six points of \(\mathcal P\) indexed by \(V\setminus\ell\). The reduced Galois-stable divisor \(D=\bigcup_{\ell}C_\ell\) is the Chilean twelve-conic divisor associated with \(E\).

Write \(\mathcal L\) for the Galois set of twelve affine lines; \(\mathcal U\) for the twelve unordered pairs of distinct parallel affine lines; \(\mathcal I=\{(\ell,v):v\notin\ell\}\) (72 elements); and \(\mathcal J=\{(\ell,m):\ell\ne m,\;\ell\parallel m\}\) (24 elements). The action of arithmetic Frobenius on these finite sets is induced by its affine action \(g\in\operatorname{AGL}_2(\mathbb F_3)\) on \(V\). Each symbol also denotes the corresponding finite étale scheme over \(k\).

**Arithmetic class and all-extension count.** In the Grothendieck ring \(K_0(\mathrm{Var}_k)\), with \(\mathbb L=[\mathbf A^1_k]\),
\[
[D]=(\mathbb L+1)[\mathcal L]+[V]+[\mathcal U]-[\mathcal I]-[\mathcal J].
\]
For every integer \(n\ge1\), setting \(F_n(S)=\#\operatorname{Fix}(g^n\mid S)\),
\[
\boxed{\#D(\mathbb F_{q^n})=(q^n+1)F_n(\mathcal L)+F_n(V)+F_n(\mathcal U)-F_n(\mathcal I)-F_n(\mathcal J).}
\]
If \(Z(S,T)=\prod_{c\in\mathrm{Cycles}(g\mid S)}(1-T^{|c|})^{-1}\), then
\[
\boxed{Z(D,T)=\frac{Z(\mathcal L,qT)Z(\mathcal L,T)Z(V,T)Z(\mathcal U,T)}{Z(\mathcal I,T)Z(\mathcal J,T)}.}
\]
Thus the complete zeta function is obtained from a finite permutation of nine elements, without requiring a splitting field for the conics.

**Complete ground-field classification.** The ten distinct arithmetic fixed-point types have the following formulas. The affine group has eleven conjugacy classes, but its two order-eight classes have the same cycle signatures on the five incidence sets, hence the same arithmetic formula. The determinant column is the determinant of the linear part of Frobenius in \(\mathbb F_3^\times\), hence is congruent to \(q\) modulo three. The cycle-length notation describes the action on the nine flex points, and the order and that cycle information distinguish the two order-three and the two order-six cases.

| Affine type | Linear determinant | Order | Cycles on \(V\) | \(\#D(\mathbb F_q)\) |
| --- | --- | ---: | --- | --- |
| Identity | \(+1\) | 1 | \(1^9\) | \(12q-63\) |
| Reflection | \(-1\) | 2 | \(1^3 2^3\) | \(4q-1\) |
| Central inversion | \(+1\) | 2 | \(1^1 2^4\) | \(4q+9\) |
| Linear nontrivial unipotent | \(+1\) | 3 | \(1^3 3^2\) | \(3q-3\) |
| Affine unipotent without a fixed point | \(+1\) | 3 | \(3^3\) | \(0\) |
| Nonzero translation | \(+1\) | 3 | \(3^3\) | \(3q\) |
| Order-four linear type | \(+1\) | 4 | \(1^1 4^2\) | \(1\) |
| Order-six type with one fixed point | \(+1\) | 6 | \(1^1 2^1 6^1\) | \(q+3\) |
| Order-six type without a fixed point | \(-1\) | 6 | \(3^1 6^1\) | \(q+2\) |
| Irreducible order-eight type | \(-1\) | 8 | \(1^1 8^1\) | \(1\) |

These ten types are the ten distinct affine-cycle signatures in the 432-element affine group (eleven group conjugacy classes, with the two order-eight classes merged). The table is conditional on the Frobenius type; it does not assert that every type occurs over every prescribed field.

**Two realized extremes.** Over \(\mathbb F_5\), take the standard plane cubic \(E_5:y^2z=x^3+3xz^2+2z^3\). It has five rational points and \(j(E_5)=4\). Its Frobenius on three-torsion has characteristic polynomial \(X^2-X+2\) modulo three, hence order eight. Its associated conic divisor has **no individually rational geometric conic** and exactly **one rational point**, the unique rational cusp-dual point:
\[
\#D_5(\mathbb F_{5^n})=
\begin{cases}
1,&4\nmid n,\\
4\cdot5^n+9,&4\mid n,\ 8\nmid n,\\
12\cdot5^n-63,&8\mid n.
\end{cases}
\]
In particular,
\[
Z(D_5,T)=\frac{(1-T^8)^9}{(1-T)(1-T^4)^2(1-5^4T^4)(1-5^8T^8)}.
\]

Over \(\mathbb F_7\), let \(E_7:y^2=x^3+x+3\) with identity \(O\) at infinity, and let \(P=(4,1)\in E_7(\mathbb F_7)\). Embed this elliptic curve as a plane cubic by the complete linear system \(|2[O]+[P]|\). The group \(E_7(\mathbb F_7)\) has six elements, \(j(E_7)=5\), and \(P\notin3E_7(\mathbb F_7)\). The flex torsor therefore has no rational point; Frobenius is an affine nontrivial-unipotent transformation with no fixed point. **None of the twelve conics, nine octuple points, or twelve nodes is rational, and the entire divisor has no \(\mathbb F_7\)-point.** For every \(n\ge1\),
\[
\#D_7(\mathbb F_{7^n})=
\begin{cases}
0,&3\nmid n,\\
12\cdot7^n-63,&3\mid n,
\end{cases}
\qquad
Z(D_7,T)=\frac{(1-T^3)^{21}}{(1-7^3T^3)^4}.
\]
Every closed point on \(D_7\) has degree divisible by three.

## Assumptions and scope

The characteristic is at least five. The plane cubic is smooth and its \(j\)-invariant is nonzero. The conics are constructed in the **dual** projective plane from the tangent lines at flexes, not directly through the flexes themselves. The Frobenius action on flexes is an affine rather than necessarily linear action: for an arbitrary degree-three plane embedding it is the torsor \(\{Q\in E(\bar k):3Q=P\}\) for the corresponding Picard class \(P\). Geometric incidence is used only for parameters where the twelve conics and twenty-one designated singular points form the nondegenerate Chilean configuration. The displayed nonzero-\(j\) assumption ensures this nondegeneracy in characteristic at least five, by the Hesse determinant test described below and the cited geometric construction.

## Proof

**1. Geometric incidence and nondegeneracy.** The 2020 geometric constructions of Kohel--Roulleau--Sarti and Dolgachev--Laface--Persson--Urzúa identify twelve smooth conics through the nine dual flex-tangent points. Their supports are the complements of the twelve affine lines in \(V\cong\mathbb F_3^2\). They show that the only singular points of their reduced union are the nine points lying on eight conics each and twelve additional pairwise transverse intersections, each lying on two conics. The latter points are indexed by unordered pairs of parallel affine lines: two nonparallel affine lines intersect once, hence their two complementary six-point sets share four points, exhausting the degree-four Bézout intersection; parallel lines have disjoint triples, hence their complements share three points and yield one extra intersection. There are \(4\binom32=12\) such parallel pairs.

For the nonzero-\(j\) boundary, an algebraically closed-field Hesse form of the smooth cubic is \(x^3+y^3+z^3-3\lambda xyz=0\). The nine dual flex-tangent points are cyclic permutations of \((1:\eta^2:\lambda\eta)\), where \(\eta^3=1\). Exact norms of all 84 triple determinants, reduced modulo \(\eta^2+\eta+1\), have no factors beyond powers of three and the factors of \(\lambda\), \(\lambda^3-1\), and \(\lambda^3+8\). For characteristic at least five, smoothness excludes \(\lambda^3=1\), while \(j(E)\ne0\) excludes \(\lambda=0\) and \(\lambda^3=-8\). Thus no three dual flex-tangent points become collinear; this recovers the required nondegenerate parameter range without relying on characteristic-zero specialization alone. The finite determinant calculation and its factor restrictions are replayed by `verify.py`. The cited geometric incidence theorem then applies to the nonspecial family over characteristic other than two and three.

**2. Descended normalization.** The normalization of \(D\) is the disjoint union of its twelve smooth conics. The singular-point scheme is the disjoint union of the nine eight-branch points \(V\) and the twelve two-branch points \(\mathcal U\). The inverse image of the singular-point scheme on the normalization consists of the incidence schemes \(\mathcal I\) and \(\mathcal J\). Consequently, the scissors relation gives
\[
[D]=[\widetilde D]-[\mathcal I]-[\mathcal J]+[V]+[\mathcal U].
\]
Every smooth conic over a finite field has a rational point and is isomorphic over that field to \(\mathbf P^1\). Since \(\mathcal L\) is finite étale over \(k\), the normalized conic family is isomorphic (noncanonically) to \(\mathbf P^1\times\mathcal L\); hence \([\widetilde D]=(\mathbb L+1)[\mathcal L]\). This proves the stated identity in \(K_0(\mathrm{Var}_k)\), including nonrational branches above rational singular points.

**3. Frobenius and zeta.** For each finite étale Galois set \(S\), \(\#S(\mathbb F_{q^n})=F_n(S)\). Evaluating the class identity over every extension gives the asserted point-count formula. Exponentiating \(\sum_{n\ge1}\#D(\mathbb F_{q^n})T^n/n\) and using the finite-cycle product for each of the five sets gives the zeta-factorization exactly.

**4. Complete affine-type classification.** Label \(V\) as \(\mathbb F_3^2\), enumerate the twelve sets \(\{(x,y):ax+by=c\}\), and enumerate \(\mathcal U,\mathcal I,\mathcal J\) as defined above. Enumerating the 48 invertible two-by-two matrices and nine translations gives precisely 432 affine permutations and ten cycle signatures (the eleven conjugacy classes have two classes sharing the order-eight signature). Substituting the five fixed-point counts for \(n=1\) gives the ten displayed linear polynomials in \(q\). The exact program `verify.py` implements this entire finite classification, checks all affine maps (not a sample), and checks the two extremal Frobenius types. The proof of the general count formula itself is symbolic and does not depend on enumeration.

**5. Realization of both extremes.** For \(E_5\), direct finite-field enumeration gives \(\#E_5(\mathbb F_5)=5\), whence the Frobenius trace is \(1\). Its mod-three characteristic polynomial is irreducible and has fourth power \(-1\), so Frobenius has order eight on the nine flexes and exactly one fixed point. On the twelve complementary conics it has cycles of lengths four and eight; on \(\mathcal U\) the same; on \(\mathcal I\) nine eight-cycles and on \(\mathcal J\) three eight-cycles. The first count is one, and substitution at each extension yields the displayed zeta function.

For \(E_7\), direct enumeration gives \(\#E_7(\mathbb F_7)=6\), with trace \(2\). Since nine rational three-torsion points would contradict the group order six, Frobenius on \(E_7[3]\) is a nonidentity unipotent matrix. Its flexes in the embedding \(|2[O]+[P]|\) satisfy \(3Q=P\); the point \(P\) has nonzero \(y\)-coordinate and is not in the order-two subgroup \(3E_7(\mathbb F_7)\). Hence the flex torsor has no rational point. Its affine Frobenius type is the unique fixed-point-free nontrivial-unipotent type; all nine flexes form three three-cycles, all twelve conics form four three-cycles, and the other incidence sets have three-cycles only. Thus the divisor has no rational point over extensions whose degrees are not divisible by three. Substitution into the general formula produces the remaining formulas.

## Verification

Run `python3 verify.py` with Python 3. The standalone checker uses only the standard library. It verifies 84 nontrivial dual Hesse triple determinants over the integer Eisenstein ring (permitting exactly the excluded discriminant factors), enumerates all 432 affine transformations on the nine-point affine plane, verifies the ten cycle-signature types, counts the rational points of the two explicit Weierstrass curves, and checks the extension counts and zeta-cycle data. Successful output ends in `CHILEAN_ARITHMETIC_CERTIFICATE_OK`. None of these finite checks is treated as a substitute for the geometric normalization and descent proof.

## Relationship to prior work

Pokora and Szemberg (first public preprint 2020-02-05) describe the Chilean twelve-conic arrangement and its freeness over the complex numbers. Kohel, Roulleau and Sarti (2020-04-23) give the dual-cubic nine-cusp realization and its conic incidences; Dolgachev, Laface, Persson and Urzúa (2020-08-21) establish the Halphen-pencil construction over algebraically closed fields of characteristic other than two and three. Their results supply the **geometric configuration** used here; neither the configuration, the Hesse/affine labels nor its singularity counts are claimed as new. The present result concerns arithmetic descent: a finite-étale class identity, complete extension-field point counts, an exhaustive affine Frobenius classification, and explicit zero-point/one-point finite-field twists. No equivalent complete finite-field formula was located in the inspected works or targeted published-record searches. The possibility of an older equivalent arithmetic deduction is a residual literature-priority risk.

## Limitations

This theorem does not cover characteristics two or three, singular cubics, or the special \(j=0\) case in which the flex-tangent dual configuration can degenerate. The ten-row group table gives conditional formulas and makes no assertion of the realizability of every affine type over every finite field. The \(\mathbb F_7\) example depends on the specified **degree-three embedding**; replacing it with the standard \(|3[O]|\) embedding changes the flex torsor. The finding does not determine Newton polygons, global moduli geometry, or the zeta functions of the underlying elliptic curves beyond the explicit point checks used here. The originality comparison is best-knowledge, not an independent publication-priority certification.

## References

1. P. Pokora and T. Szemberg, *Conic-line arrangements in the complex projective plane*, arXiv:2002.01760, publicly posted 2020-02-05, Section 2. https://arxiv.org/abs/2002.01760
2. D. Kohel, X. Roulleau and A. Sarti, *A special configuration of 12 conics and generalized Kummer surfaces*, arXiv:2004.11421, publicly posted 2020-04-23, Theorem 11 and Section 3.1. https://arxiv.org/abs/2004.11421
3. I. Dolgachev, A. Laface, U. Persson and G. Urzúa, *Chilean configuration of conics, lines and points*, arXiv:2008.09627, publicly posted 2020-08-21, Sections 4--6. https://arxiv.org/abs/2008.09627
