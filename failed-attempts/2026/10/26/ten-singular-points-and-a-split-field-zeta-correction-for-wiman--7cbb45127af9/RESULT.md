# Ten singular points and a split-field zeta correction for Wiman's sextic in characteristic five

## Finding

Consider the classical integral plane sextic
\[
W_{\mathbb Z}:\quad F=x^6+y^6+z^6+(x^2+y^2+z^2)(x^4+y^4+z^4)-12x^2y^2z^2=0.
\]
Let \(W\) denote its coefficientwise fibre over \(\mathbb F_5\). Then \(W\) is geometrically integral. Its complete **geometric singular support** consists of four ordinary double points
\[
[1:\epsilon:\eta],\qquad \epsilon,\eta\in\{1,-1\},
\]
and six ordinary cusps, namely the two points on each coordinate axis satisfying that the squares of their other two coordinates sum to zero. All ten points are \(\mathbb F_5\)-rational. The four nodes have **nonsplit** pairs of tangent directions over \(\mathbb F_5\); the six cusps are geometrically unibranch. The local Tjurina lengths are respectively \(1\) and \(2\), so the zero-dimensional projective singular scheme has length \(16\).

The normalization is \(\mathbb P^1_{\mathbb F_5}\). For every integer \(r\ge1\), writing \(q=5^r\), its arithmetic is
\[
\boxed{\#W(\mathbb F_q)=q+1-4(-1)^r,\qquad
Z(W/\mathbb F_5,T)=\frac{(1+T)^4}{(1-T)(1-5T)}.}
\]
The assertion is about the stated plane model and its singular-point arithmetic, not a stable model of the generic fibre.

## Assumptions and scope

All geometric assertions are made after base change from \(\mathbb F_5\) to its algebraic closure \(k\). The displayed homogeneous polynomial defines the exact integral model being reduced; no other birational model is substituted. A node means a plane ordinary double point with two distinct geometric tangent directions. A cusp means a plane singularity with completed local equation \(U^2+2V^3=0\). By the singular scheme we mean the projective Jacobian/Fitting scheme, or equivalently its affine-chart local Jacobian algebras; for this degree-six equation Euler's relation in characteristic five identifies these constructions. The zeta function uses the closed-point definition \(Z(W,T)=\exp(\sum_{r\ge1}\#W(\mathbb F_{5^r})T^r/r)\).

## Proof

**1. A nodal cubic quotient.** Set \(a=x^2\), \(b=y^2\), \(c=z^2\), and \(s=a+b+c\). Newton's symmetric-polynomial identities yield the exact coefficientwise congruence
\[
F\equiv 2s^3+abc\pmod5.
\]
Let \(H\subset\mathbb P^2_{\mathbb F_5}\) be the cubic \(abc+2s^3=0\). The projective coordinate-squaring morphism \([x:y:z]\mapsto[x^2:y^2:z^2]\) maps \(W\) onto \(H\). Its degree is four on the dense coordinate torus. The partial derivatives of the cubic are \(bc+s^2\), \(ac+s^2\), and \(ab+s^2\). Their simultaneous vanishing has no point with a zero coordinate; with all three coordinates nonzero it forces \(a=b=c\). Thus \([1:1:1]\) is the only geometric singular point of \(H\). In the affine chart \(c=1\), with \(a=1+u\), \(b=1+v\), its quadratic tangent term is
\[
3u^2+2uv+3v^2.
\]
Its discriminant is \(3\in\mathbb F_5\), which is nonsquare. It is geometrically a nondegenerate node and has two branches conjugate over \(\mathbb F_{25}\). In particular \(H\) is geometrically integral: a reducible plane cubic cannot have exactly this single ordinary node without other singularities.

**2. Geometric integrality of the sextic.** The intersection of \(H\) with \(a=0\) is the single smooth point \(P_a=[0:1:-1]\) with intersection multiplicity three, since on that axis its equation is \(2(b+c)^3=0\). Analogously, \(P_b=[1:0:-1]\) and \(P_c=[1:-1:0]\) occur on the other axes. On the normalization \(\widetilde H\), these points are smooth and distinct. Hence
\[
\operatorname{div}_{\widetilde H}(a/c)=3(P_a-P_c),\qquad
\operatorname{div}_{\widetilde H}(b/c)=3(P_b-P_c).
\]
In the function field \(k(H)\), their square classes are independent: parity of valuations at \(P_a\) and \(P_b\) distinguishes all four products. Adjoining \(\sqrt{a/c}\) and \(\sqrt{b/c}\) therefore gives a separable field extension of degree four. This is the generic inverse image of \(H\) under coordinate squaring. The homogeneous pullback has no coordinate-line component, so \(W\) is geometrically integral and reduced.

**3. Complete singular support and local types.** The derivatives of \(F=abc+2s^3\), viewed in the \(x,y,z\) coordinates, are
\[
F_x=2x(bc+s^2),\quad F_y=2y(ac+s^2),\quad F_z=2z(ab+s^2).
\]
There is no point of \(W\) with two coordinates zero. If all \(x,y,z\) are nonzero, the three derivative equations force \(a=b=c\); up to common scaling this gives exactly the four points \([1:\epsilon:\eta]\). Coordinate squaring is etale there, so the nodal tangent form of \(H\) pulls back to a nondegenerate nodal form; its nonsquare discriminant stays nonsquare under any \(\mathbb F_5\)-rational invertible linear change. Thus the four nodes are nonsplit over \(\mathbb F_5\).

If \(x=0\), then \(y,z\ne0\) and the derivative equations imply \(b+c=0\); conversely both such points lie on \(W\) and are singular. Since \(-1=4\) is a square in \(\mathbb F_5\), they are \([0:2:1]\) and \([0:-2:1]\), and cyclic permutations produce six distinct rational points. In the chart \(z=1\), set \(U=xy\) and \(V=x^2+y^2+1\). At either point, the Jacobian determinant of this change of variables is \(2(y^2-x^2)=3\ne0\), and the equation becomes **exactly** \(U^2+2V^3=0\). Hence each is an ordinary unibranch cusp, with delta invariant one and local Tjurina length two. Each node has delta invariant one and Tjurina length one. The preceding derivative stratification proves there are no additional geometric singularities. The local lengths sum to \(4+2\cdot6=16\).

**4. Normalization and finite-field arithmetic.** A geometrically integral plane sextic has arithmetic genus \((6-1)(6-2)/2=10\). The ten identified singularities contribute total delta \(4+6=10\), so the normalization has geometric genus zero. The cusp \([0:2:1]\) is rational and geometrically unibranch; its unique geometric preimage under normalization is Frobenius-fixed and hence \(\mathbb F_5\)-rational. Therefore the normalization is \(\mathbb P^1_{\mathbb F_5}\), which has exactly \(5^r+1\) points over every \(\mathbb F_{5^r}\).

Normalization induces a bijection on geometric points away from the singularities. At each cusp it replaces one rational point with one rational point over every extension, so its contribution to the point-count difference is zero. At each rational nonsplit node, the two points of the normalization above it are defined over \(\mathbb F_{25}\) and interchanged by the \(5\)-power Frobenius. For odd \(r\) neither is \(\mathbb F_{5^r}\)-rational, whereas the node is rational, contributing \(+1\) relative to the normalization. For even \(r\) both are rational, contributing \(-1\). The four nodes therefore contribute \(-4(-1)^r\), giving the asserted count. Exponentiating the point-count series yields the stated zeta function.

## Verification

The reproducible standalone Python program `check_wiman.py` uses only the standard library. It verifies the polynomial congruence coefficientwise, enumerates the entire \(\mathbb F_5\)- and \(\mathbb F_{25}\)-projective planes, checks ten \(\mathbb F_5\)-singular points by gradients, and checks the node discriminant and cusp coordinate Jacobian. Its complete results are \(\#W(\mathbb F_5)=10\), \(\#W(\mathbb F_{25})=22\), and `CHECK_OK`. Exhaustive enumeration over these two finite fields is a corroborating calculation; the global geometric completeness, integrality, and formula for all \(r\) come from the preceding proofs.

## Relationship to prior work

The classical Wiman sextic and its four ordinary nodes over characteristic zero are described by Edge and by Inoue--Kato. Inoue--Kato explicitly work in characteristics other than two, three, and five, so their geometry does not settle this exceptional fibre. Giulietti--Kawakita--Lia--Montanucci explicitly state that the characteristic-five curve is rational and that its abstract automorphism group is \(\operatorname{PGL}_2\); these are **prior results, not new claims here**. Their treatment does not give the six cusps, complete local singular scheme, nonsplit tangent fields, or singular-model zeta correction established here. Rationality of the normalization alone does not imply these arithmetic corrections. Historical treatments not yet located could still overlap with parts of the stated refinement.

## Limitations

The result concerns the displayed coefficientwise plane model. It does not determine semistable reduction, any minimal regular arithmetic surface model, a conductor of the Jacobian of the characteristic-zero generic curve, or the reduction of the full classical group action. No independent scientific audit has been performed. Novelty is assessed against inspected sources and database searches, not asserted as an exhaustive literature theorem. A 2005 Kyoto preprint is known from a year-only archive listing, while a day-resolved publication record for its journal version is dated July 14, 2006.

## References

- W. L. Edge, *A pencil of four-nodal plane sextics*, Mathematical Proceedings of the Cambridge Philosophical Society **89** (1981), 413–421. Full text: https://webhomes.maths.ed.ac.uk/cheltsov/edge2021/pdf/1982b.pdf.
- N. Inoue and F. Kato, *On the geometry of Wiman's sextic*, Journal of Mathematics of Kyoto University **45** (2005/2006), 743–757, DOI: 10.1215/KJM/1250281655. Full preprint: https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf.
- M. Giulietti, M. Kawakita, S. Lia, and M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317 (May 15, 2018), https://arxiv.org/pdf/1805.06317. Remark 3.1 treats characteristic five.
- Kyoto University, *Preprint 2005*, entry 2 (year-only evidence): https://www.math.kyoto-u.ac.jp/preprint/preprint2005.html.
- MaRDI mathematical bibliography, Inoue--Kato publication entry, journal publication date 2006-07-14: https://portal.mardi4nfdi.de/wiki/Publication%3A2494637.
