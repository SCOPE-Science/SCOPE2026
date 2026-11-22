# Higher generalized weights of the degree-six toric del Pezzo anticanonical code

## Finding
For every prime power \(q\ge5\), let
\[
P=\{(a,b)\in\mathbb R^2:|a|\le1,\ |b|\le1,\ |a+b|\le1\},\quad E=P\cap\mathbb Z^2,
\]
and let \(C_P(\mathbb F_q)\) be the seven-dimensional code obtained by evaluating the seven Laurent characters \(x^a y^b\), \((a,b)\in E\), at every point of \(T=(\mathbb F_q^*)^2\). This is the dense-torus anticanonical code of the split smooth degree-six toric del Pezzo surface. Put \(t=q-1\). The **higher generalized Hamming weights**, from the third through the seventh, are exactly
\[
\boxed{(d_3,d_4,d_5,d_6,d_7)
=(t^2-t-1,\ t^2-t,\ t^2-2,\ t^2-1,\ t^2).}
\]
Equivalently, the maximum numbers of common torus zeros of \(r\) linearly independent anticanonical sections, for \(r=3,4,5,6,7\), are respectively
\[
\boxed{(q,\ q-1,\ 2,\ 1,\ 0).}
\]
For \(r=3\) the maximum is attained by a full rational ruling fiber and exactly one off-fiber point. For \(r=4\), the maximum is a full ruling fiber and no further point. Earlier first- and second-weight results are not asserted as new.

## Assumptions and scope
The field is an arbitrary finite field of cardinality \(q\ge5\), including nonprime fields. All zeros are taken in the **dense split torus** \(T\), not among all points of the projective del Pezzo surface. The integer lattice points of the polygon are
\[
E=\{(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0)\}.
\]
Character orthogonality on \(T\) gives an injective evaluation map because these exponent vectors are distinct modulo \(q-1\) in both coordinates, so the dimension is seven and the length is \(t^2\). For any \(r\), the generalized weight \(d_r\) is the least cardinality of the union of supports of an \(r\)-dimensional subcode, equivalently \(t^2\) minus the maximum number of common zeros of \(r\) independent elements of the section space. The polygon has normalized area \(2\operatorname{Area}(P)=6\).

## Proof
**1. A finite Newton-polygon lemma.** Let \(V\) be an \(r\)-dimensional space of Laurent sections supported on \(E\) with \(r\ge3\), and suppose its elements have a greatest common nonunit Laurent factor \(h\). Write \(Q=\operatorname{Newt}(h)\) and \(R(Q)=\{u\in\mathbb Z^2:Q+u\subseteq P\}\). Every residual quotient of a section of \(V\) is supported on \(R(Q)\). Consequently \(|R(Q)|\ge r\ge3\). By translating \(Q\) by an integer vector, its vertices occur among the seven points of \(E\): choose one exponent of a nonzero quotient, use the Minkowski identity \(\operatorname{Newt}(hf)=\operatorname{Newt}(h)+\operatorname{Newt}(f)\), and observe that all vertices of the translated \(Q\) lie in \(P\). Thus every possible translated \(Q\) is the convex hull of a subset of \(E\). Taking convex hulls of all \(127\) nonempty subsets, identifying integer translates, and testing every possible integer translate into \(P\) gives the **complete** table below (up to translations):

| Shape of \(Q\) | Classes | Residual exponent set | Residual dimension |
| --- | ---: | --- | ---: |
| Primitive segment | 3 | Unit parallelogram, unimodularly equivalent to \(\{(0,0),(1,0),(0,1),(1,1)\}\) | 4 |
| Unimodular triangle | 2 | Unimodular triangle | 3 |
| All other nonunit shapes | 0 | At most two exponents | At most 2 |

This is an exact finite lemma, not a sample of field sizes. The companion `verify_hexagon_higher.py` contains the full integer-hull and integer-translation enumerator; its output lists all five qualifying classes and checks the residual areas. The polygon has coordinate widths two, so a translate fitting inside \(P\) lies within the script's searched integer box \([-3,3]^2\), which is exhaustive. The unit factor, having a point Newton polygon, belongs to the next case.

**2. A general bound for three or four sections.** If the sections in \(V\) have no nonunit common factor, two generic \(\overline{\mathbb F}_q\)-linear combinations have no common curve component. Their intersection on the degree-six anticanonically embedded del Pezzo surface has length six, by intersection theory (equivalently the Bernstein mixed-area bound \(2\operatorname{Area}(P)=6\)); hence all sections of \(V\) share at most six geometric torus points.

If a nonunit gcd \(h\) has segment Newton polygon, it is, after an invertible monomial change, a scalar times \(X-\lambda\), with exactly \(q-1=t\) torus zeros. Its residual four-character space maps the torus into a projective Segre quadric by
\[
(U,V)\longmapsto [1:U:V:UV].
\]
A three-dimensional subspace of its sections vanishes at *at most one* torus point, because its three independent hyperplanes intersect in a single point of \(\mathbb P^3\) and the Segre map is injective. A four-dimensional residual subspace is the whole residual space and has no common torus zero. Therefore the total common zero counts are at most \(t+1\) for \(r=3\) and \(t\) for \(r=4\).

If \(Q\) is a unimodular triangle, \(h\) becomes \(A+B U+C V\) with all three coefficients nonzero and hence has exactly \(q-2=t-1\) torus zeros. The residual space has dimension exactly three, so for \(r=3\) the three independent residual sections have no simultaneous torus zero; for \(r=4\) this case is impossible. Combining with the coprime bound six gives, for every \(q\ge7\), the upper bounds \(q\) and \(q-1\), respectively. These apply to nonprime prime powers as well.

**3. The exceptional smallest permitted field.** For \(q=5\), the coprime bound six alone does not exclude six common zeros for three sections or five common zeros for four. The complete \(16\)-point evaluation matrix is formed exactly over \(\mathbb F_5\). Its every six-row submatrix has rank at least five, and its every five-row submatrix has rank at least four. These assertions are established by exhaustive modular elimination of, respectively, all \(\binom{16}{6}=8,008\) and \(\binom{16}{5}=4,368\) choices in `verify_hexagon_higher.py`; the minimum ranks are attained. A three-dimensional kernel would require rank at most four, and a four-dimensional kernel rank at most three. Hence the same upper bounds \(5\) and \(4\) apply for \(q=5\). There is no prime power strictly between five and seven.

**4. Sharpness for \(r=3,4\).** Choose distinct \(a,b\in\mathbb F_q^*\) and any \(c\in\mathbb F_q^*\). Set \(h=x-a\). The four-dimensional residual Laurent space is
\[
W=\operatorname{span}\{x^{-1},x^{-1}y,y^{-1},1\}
=x^{-1}\operatorname{span}\{1,y,x/y,x\}.
\]
Multiplication by \(h\) embeds \(W\) in the seven-character space. All four sections in \(hW\) have exactly the \(t\) zeros of the fiber \(x=a\) in common, giving the \(r=4\) bound. The three-dimensional subspace \(h\ker(\operatorname{ev}_{(b,c)}:W\to\mathbb F_q)\) vanishes at that fiber and the off-fiber point \((b,c)\). The Segre embedding from Step 2 proves there are no further common zeros, giving exactly \(t+1=q\) points for \(r=3\).

**5. The final three higher weights.** Write \(v(x,y)\) for the seven-coordinate evaluation row. Any three rows belonging to distinct torus points are linearly independent. If the three \(x\)-coordinates are distinct, their three columns \(1,x,x^{-1}\) have nonzero Vandermonde determinant. If exactly two \(x\)-coordinates agree, the columns \(1,x,y\) give a nonzero determinant because the two points with equal \(x\) have distinct \(y\). If all three \(x\)-coordinates agree, the three distinct \(y\)-coordinates give a nonzero determinant in columns \(1,y,y^{-1}\). Thus any three distinct evaluation rows have rank three, and any two have rank two. A five-dimensional section space can vanish at at most two torus points, and the kernel of evaluation at any two distinct points has dimension five and vanishes at exactly those two. The corresponding statements for six and seven independent sections give maxima one and zero. This proves all five formulas. \(\square\)

## Verification
The standalone exact-integer script `verify_hexagon_higher.py` and its saved output `verify_output.txt` are included with this result. It reconstructs the seven-point hexagon, exhausts every integer convex hull of subsets and all relevant translations, verifies the five nontrivial gcd polygon classes with at least three residual monomials, and exhausts the small-field submatrix ranks that the general intersection bound does not settle. It additionally constructs extremal subcodes over \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_{11}\). This is a finite proof certificate for the field-independent Newton lemma and the \(q=5\) exceptional check; the all-field claims rely additionally on the algebraic argument in Steps 2, 4, and 5.

## Relationship to prior work
Little–Schenck [1] motivates toric surface evaluation codes and Minkowski factor methods, but studies ordinary minimum distance rather than these higher support weights. Soprunov–Soprunova [2] refine first-distance bounds via full Minkowski length, not the five displayed higher weights. The previous calculation [3] proves \(d_2(C_P)=(q-2)^2\) for the **same polygon and torus**, and even classifies common gcds for pairs of sections; it expressly leaves the remaining generalized weights untreated. Its two-section argument does not imply the sharp three- and four-section maxima, particularly at \(q=5\). Published full-surface del Pezzo generalized-weight tables count the projective surface's rational points rather than just the \((q-1)^2\) torus evaluation positions; they do not directly give this punctured code's higher weights. The claimed addition is limited to the five explicit values \(d_3,\ldots,d_7\), including the structural sharpness statement for the third and fourth weights.

## Limitations
The theorem concerns only the split degree-six smooth toric del Pezzo anticanonical character set, evaluated on its dense torus, for prime powers \(q\ge5\). It does not determine weights of the full-surface evaluation code, non-split forms, other polygons, or small fields below five. The exact first and second generalized weights are prior work, not part of this claim. Mathematical correctness is supported by a complete proof and exact finite certificate; historical originality has not received an independent audit and could be affected by a specialized source not found in the inspected searches.

## References
1. J. Little and H. Schenck, *Toric surface codes and Minkowski sums*, arXiv:math/0507598 (first posted July 28, 2005), especially Sections 1–5. https://arxiv.org/abs/math/0507598
2. I. Soprunov and J. Soprunova, *Toric surface codes and Minkowski length of polygons*, arXiv:0802.2088 (first posted February 14, 2008), especially Sections 1–3. https://arxiv.org/abs/0802.2088
3. *The second generalized weight of the anticanonical degree-six toric del Pezzo code*, published mathematical record containing its full proof and exact code certificate, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-second-generalized-weight-of-the-anticanonical-degree-six-to--86be39341a03/RESULT.md
