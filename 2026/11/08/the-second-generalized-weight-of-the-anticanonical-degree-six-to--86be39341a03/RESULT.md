# The second generalized weight of the anticanonical degree-six toric del Pezzo code

## Finding
Let \(q\ge5\) be any prime power. Put
\[
 P=\{(a,b)\in\mathbb R^2:|a|\le1,\ |b|\le1,\ |a+b|\le1\},\qquad
 E=P\cap\mathbb Z^2.
\]
The seven points of \(E\) are \((-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0)\). Let \(C_P(\mathbb F_q)\) be the evaluation code of Laurent polynomials supported on \(E\) at the \((q-1)^2\) points of \((\mathbb F_q^*)^2\). The polygon \(P\) is the anticanonical hexagon of the smooth split degree-six toric del Pezzo surface. The evaluation map is injective, hence \(C_P\) has dimension seven. Its **second generalized Hamming weight** is exactly
\[
 d_2(C_P(\mathbb F_q))=(q-2)^2.
\]
Equivalently, for any two linearly independent such Laurent polynomials, the number of common torus zeros is at most \(2q-3\), and that bound is attained. This is an exact infinite-prime-power statement, not an extrapolation from small fields.

## Assumptions and scope
All polynomials have coefficients in \(\mathbb F_q\), and \(q\) is an arbitrary prime power with \(q\ge5\). Common zero means a simultaneous \(\mathbb F_q\)-point of the **dense torus**, not a rational point of the whole projective del Pezzo surface or a point on its toric boundary. The \(r\)-th generalized Hamming weight of a linear code is the least size of the union of supports of an \(r\)-dimensional subcode. For \(r=2\), this equals the code length minus the greatest number of rational common zeros of two independent sections. Evaluation is injective because after multiplying by a monomial all exponents lie in \([0,2]^2\), strictly below \(q-1\) in both coordinates; characters on the finite torus are linearly independent. The six primitive edges and unique interior lattice point give \(2\operatorname{Area}(P)=6\).

## Proof
**Step 1: a sharp lower bound on common zeros.** Let
\[
 f=\frac{(x-1)(y-1)}x,\qquad g=\frac{(x-1)(y-1)}y.
\]
The four monomial exponents of each lie in \(E\); the two sections are independent. Their common zero locus in \((\mathbb F_q^*)^2\) is \(\{x=1\}\cup\{y=1\}\), with \(2(q-1)-1=2q-3\) rational points. Thus \(d_2\le(q-1)^2-(2q-3)\).

**Step 2: the coprime case.** Let \(f,g\in\mathbb F_q[x^{\pm1},y^{\pm1}]\) be any independent sections of the seven-monomial space. If their greatest common divisor is a Laurent unit, then they have no common one-dimensional torus component. The plane Bernstein–Kushnirenko intersection bound, or the corresponding intersection theory on a toric compactification, bounds the number of geometric torus intersection points (without multiplicity) by the mixed volume of two copies of \(P\), namely \(2\operatorname{Area}(P)=6\). Since \(q\ge5\), this is at most \(2q-3\).

**Step 3: the finite Newton-polytope lemma.** Otherwise factor \(f=ha\), \(g=hb\), where \(h\) is a nonunit greatest common divisor and \(\gcd(a,b)=1\). Laurent units translate Newton polytopes. Write \(H=\operatorname{Newt}(h)\) and
\[
 S(H)=\{u\in\mathbb Z^2:H+u\subseteq P\}.
\]
As \(\operatorname{Newt}(ha)=\operatorname{Newt}(h)+\operatorname{Newt}(a)\) (and similarly for \(g\)), all exponents of \(a,b\) lie in \(S(H)\). Because \(a,b\) are linearly independent, \(|S(H)|\ge2\). Translate \(H\) into \(P\); then each vertex is among the seven points of \(E\). Thus all possible \(H\), up to translation, can be exhaustively classified by convex hulls of the \(2^7-1=127\) nonempty subsets of \(E\). Testing the integer translates \(u\) for which \(H+u\subseteq P\) yields the following **complete** table, verified by the standalone exact-integer enumerator:

| Shape of \(H\) | Number of translation classes | Residual polygon bound | Consequence |
| --- | ---: | --- | --- |
| A lattice point | 1 | \(2\operatorname{Area}(\operatorname{conv}S)=6\) | Laurent unit, already handled |
| Primitive lattice segment | 6 | \(2\operatorname{Area}(\operatorname{conv}S)\le2\) | \(\#Z(h)\le q-1\), \(\#Z(a,b)\le2\) |
| Unimodular lattice triangle | 8 | \(2\operatorname{Area}(\operatorname{conv}S)\le1\) | \(\#Z(h)=q-2\), \(\#Z(a,b)\le1\) |
| Unit lattice parallelogram | 3 | \(|S|=2\) and \(\dim\operatorname{conv}S=1\) | \(\#Z(h)\le2q-3\), \(Z(a,b)=\varnothing\) |

For reproducibility the classification algorithm takes every nonempty subset of \(E\), computes the integer convex hull and its translation-normalized vertex list, and retains shapes with at least two integer translations into \(P\). Every successful translation vector lies in the finite box \([-2,2]^2\), since both \(H+u\) and its vertices lie in \([-1,1]^2\). Thus the enumerator's larger \([-3,3]^2\) loop is exhaustive. It additionally checks primitive segment direction, the doubled residual area, and residual cardinalities. The table is a rigorous finite classification because the reduction to all subsets is proved above and the exhaustive algorithm and exact outputs accompany this result; no sampling of an infinite family is used.

**Step 4: bound every nonunit common factor.** If \(H\) is a primitive segment, the Laurent polynomial \(h\) has exactly two nonzero terms and, after a unimodular monomial change of variables, is a scalar multiple of \(X-\lambda\), with \(\lambda\in\mathbb F_q^*\); therefore \(\#Z(h)=q-1\). Coprime residual sections with Newton polytopes in \(\operatorname{conv}S(H)\) have at most its doubled area \(\le2\) common torus points by the mixed-volume inequality (zero if \(S(H)\) is collinear). Hence \(\#Z(f,g)\le q+1\le2q-3\).

If \(H\) is a unimodular triangle, \(h\) has exactly three nonzero coefficients and is, after a monomial change, a scalar multiple of \(\alpha+\beta X+\gamma Y\) with \(\alpha\beta\gamma\ne0\). Exactly \(q-2\) torus pairs satisfy it, and the residual intersection has at most one point. Thus \(\#Z(f,g)\le q-1\le2q-3\).

If \(H\) is a unit parallelogram, after a monomial coordinate change \(h=\alpha+\beta X+\gamma Y+\delta XY\), with all four vertex coefficients nonzero. If \(\alpha\delta\ne\beta\gamma\), its closure is a smooth bidegree-\((1,1)\) curve in \(\mathbb P^1\times\mathbb P^1\), isomorphic over \(\mathbb F_q\) to \(\mathbb P^1\), and contains at most \(q+1\le2q-3\) torus points. If \(\alpha\delta=\beta\gamma\), it factors over \(\mathbb F_q\) as two nonparallel torus binomials; their zero sets are subtori-translates of cardinality \(q-1\) intersecting in exactly one rational point, giving \(2q-3\) zeros. In all cases \(S(H)\) has exactly two exponents, so independent residual sections \(a,b\) form a basis of their two-monomial space and have **no simultaneous torus zero**. Therefore \(\#Z(f,g)\le2q-3\).

Combining all cases proves the common-zero upper bound, matching Step 1, hence \(d_2=(q-2)^2\). \(\square\)

## Verification
The complete reproducible package includes `verify_hexagon.py` and `verify_hexagon_output.txt`. The script computes all 127 subset hulls, identifies exactly 18 nonunit-relevant (or 19 including unit) translation classes, checks doubled residual areas and support cardinalities, and evaluates the sharp pair on prime fields of sizes 5, 7, 11, and 13. For \(q=5\) it independently checks all \(\binom{16}{8}=12,870\) eight-point subsets of the 16-point torus: every eight-row evaluation matrix has rank at least six, precluding two independent sections vanishing at eight or more points. These finite checks support but do not replace the argument for all prime powers; the proof's finite shape table is exhaustively certified by explicit integer enumeration.

## Relationship to prior work
Little–Schenck [1], the archival motivating paper, defines these toric-surface evaluation codes and uses Newton-polygon/Minkowski decompositions to study **minimum distance**, that is the first generalized weight. Its Sections 1–5 do not determine the second generalized weight of this seven-monomial hexagon. Soprunov–Soprunova [2] refine first-distance techniques using Minkowski length; their claims also concern one section at a time. Boguslavskii [3] establishes generalized-weight hierarchies for **evaluation on all rational points of complete split del Pezzo surfaces**; for degree six the block length there is \(q^2+4q+1\), whereas the present code is **punctured to the dense torus** with block length \((q-1)^2\). The full-surface formula does not imply this exact punctured second weight without a new common-zero argument. Luo–Yau–Zhang–Zuo [4] classify toric surface codes of dimension at most six, whereas this code has dimension seven. The later works [5,6] treat general evaluation bounds or other polygon/parameterized code families and do not provide the asserted exact hexagonal value. No exhaustive claim of historical uniqueness is made.

## Limitations
The result concerns precisely the dense-torus evaluation code of the seven lattice points of \(P\) for \(q\ge5\), not the full del Pezzo evaluation code, arbitrary larger polygons, or the remaining generalized weights. Its historical originality has not been independently audited and could be affected by equivalent formulations in specialized toric-code literature. The exact finite enumerator provides a short reproducible certificate for a combinatorial sublemma; its validity rests additionally on the proved reduction from arbitrary gcd shapes to 127 candidate subsets. The manuscript does not assert a new general Bernstein intersection theorem or a new general Minkowski-sum inequality.

## References
1. J. Little and H. Schenck, *Toric surface codes and Minkowski sums*, arXiv:math/0507598 (first posted 2005-07-28). Sections 1–5; primary MSC 14G50. https://arxiv.org/abs/math/0507598
2. I. Soprunov and J. Soprunova, *Toric surface codes and Minkowski length of polygons*, arXiv:0802.2088 (2008). Sections 1–3. https://arxiv.org/abs/0802.2088
3. M. I. Boguslavskii, *Sections of del Pezzo surfaces, and generalized weights*, Problems of Information Transmission 34 (1998), 14–24, especially Sections 2, 5, 6 and Table 3. https://www.researchgate.net/publication/242402363_SECTIONS_OF_THE_DEL_PEZZO_SURFACES_AND_GENERALIZED_WEIGHTS1
4. Z. Luo, C. Yau, M. Zhang, and H. Zuo, *On classification of toric surface codes of low dimension*, arXiv:1402.0060 (2014). https://arxiv.org/abs/1402.0060
5. A. Jaramillo-Vélez, H. López, and J. Pitones, *Relative generalized Hamming weights of evaluation codes*, arXiv:2112.07085 (2021). https://arxiv.org/abs/2112.07085
6. M. González-Sarabia et al., *Second generalized Hamming weight of some evaluation codes arising from a projective torus*, arXiv:1611.06405 (2016). https://arxiv.org/abs/1611.06405
