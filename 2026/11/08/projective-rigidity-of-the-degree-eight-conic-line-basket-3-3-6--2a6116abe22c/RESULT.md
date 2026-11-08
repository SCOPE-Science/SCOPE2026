# Projective rigidity of the degree-eight conic–line basket \((3,3,6)\)

## Finding
Over \(\mathbb C\), let \(D\subset\mathbb P^2\) be the reduced union of **one smooth conic and six distinct lines**. Suppose that the singularities of \(D\) are precisely three ordinary nodes, three ordinary tacnodes, and six ordinary transverse triple points, with no other singularities. Then **all such arrangements are projectively equivalent**. In particular, the realization space of this weak-combinatorial basket has exactly one \(\operatorname{PGL}_3(\mathbb C)\)-orbit.

An explicit representative is the union of the conic
\[
Q:\quad xy+xz+yz=0
\]
and the six lines
\[
x=0,\qquad y=0,\qquad z=0,\qquad
L_s=0,\quad L_{s-2}=0,\quad L_{-s}=0,
\]
where \(s^2-s-1=0\) and
\[
L_u:\quad x+(u+1)^2y+u^2z=0.
\]
The two roots \(s=(1\pm\sqrt5)/2\) give projectively equivalent *unlabelled* arrangements. Every arrangement with this basket is nearly free with exponents \((4,4)\): existence and near-freeness of a member of this basket were previously established; the new claim is **uniqueness up to projectivity among all realizations with the specified basket**.

## Assumptions and scope
All curves, incidences, and equivalences are over \(\mathbb C\). “Ordinary triple point” means three smooth branches with distinct tangent directions. An “ordinary tacnode” is two smooth branches with simple tangency (intersection multiplicity two). The six lines are geometrically distinct; the conic is geometrically smooth; the union is reduced. No ordered or component-marked classification is asserted. No classification of other singularity baskets or all degree-eight nearly free curves is asserted.

## Proof
**1. Counting the line-only triple points.** Write \(h\) for the number of ordinary triple points supported by three line branches, and \(c\) for those supported by the conic and two lines. Then \(h+c=6\). Among the six lines exactly three are tangent to the conic, since an ordinary tacnode must be a line–conic tangency. Their total conic–line intersection multiplicity is \(12\). The three tangencies contribute six; the \(c\) conic-containing triples contribute \(2c\), and any other transverse conic–line intersection is a node. Consequently the number of conic–line nodes is
\[
12-6-2c=2(h-3).
\]
Thus \(h\ge3\). For six lines there are \(15\) line pairs, and each line-only ordinary triple consumes three distinct pairs, so \(h\le5\). Equality \(h=5\) is impossible: every one of the five other lines would meet a fixed line at triple points, hence in groups of two, contradicting oddness. Therefore \(h\in\{3,4\}\).

**2. Excluding four line-only triples.** If \(h=4\), four triples consume \(12\) of the \(15\) unordered line pairs. Each line meets the other five and can be incident to at most two triple points. Across four triples there are twelve line incidences; hence each of the six lines belongs to exactly two triples. Combinatorially these are precisely the six edges joining four vertices, and the three remaining pairs are disjoint pairs of opposite edges (the complete-quadrangle pattern).

Now \(c=2\), and the two conic-containing triple points must occupy two of these three residual line-pair intersections. The four lines through those two intersections are distinct. None can be tangent to the conic: at a conic–two-line *ordinary* triple, each incident line is transverse to the conic. Only two of the six lines remain, contradicting the required three distinct tangent lines. Hence \(h=4\) is impossible.

**3. The forced incidence pattern.** Necessarily \(h=3\), \(c=3\), and there are **no** transverse conic–line nodes. Exactly three lines, say \(S_1,S_2,S_3\), are secants of the conic; the other three, \(T_1,T_2,T_3\), are tangents. Every secant meets the conic at two of the three conic-containing triple points; each such point lies on two secants. The three secants therefore form a triangle, and its three vertices lie on the conic.

No two secants meet away from those vertices, and no three distinct tangents to a smooth conic can concur (from any point there are at most two tangents to a smooth conic). Each of the three line-only triple points consequently consists of **two tangents and one secant**. Each of the three tangent-pairs meets on one of the three different secants: two distinct vertices of the tangent triangle cannot lie on the same secant, since their joining line would be a tangent component. Up to relabelling, \(T_1\cap T_2\in S_1\), \(T_1\cap T_3\in S_2\), \(T_2\cap T_3\in S_3\).

**4. Normalize and solve.** Send the three secants to \(x=0\), \(y=0\), \(z=0\) by a projectivity. A smooth conic through all three coordinate vertices has equation \(a xy+b xz+c yz=0\) with \(abc\ne0\); a diagonal change of coordinates normalizes it to \(Q:xy+xz+yz=0\). Its tangent lines not passing through a coordinate vertex admit the unique parameters \(u\in\mathbb C\setminus\{0,-1\}\),
\[
L_u:\ x+(u+1)^2y+u^2z=0,
\]
plus the excluded tangent at the remaining coordinate vertex corresponding to the parameter at infinity. In fact, if the line is normalized as \(x+B y+C z=0\), the parameter is uniquely recovered as \(u=(B-C-1)/2\). The excluded tangents cannot occur here because they would pass through a pre-existing conic–two-secant triple point.

For distinct \(s,t,u\), the conditions
\[
L_s\cap L_t\in\{x=0\},\qquad
L_s\cap L_u\in\{y=0\},\qquad
L_t\cap L_u\in\{z=0\}
\]
reduce, after cancelling the nonzero pairwise parameter differences, to
\[
2st+s+t=0,\qquad s+u=0,\qquad t+u+2=0.
\]
Thus \(u=-s\), \(t=s-2\), and \(s^2-s-1=0\). The equation has exactly two complex roots, both producing six distinct lines and the required basket, as checked directly by projective incidence and tangency.

**5. The two roots define one orbit.** Swapping \(x\) and \(z\) preserves the conic and the set of coordinate lines, and sends tangent parameter \(v\) to \(1/v\). For \(s^2-s-1=0\), the identities
\[
1/s=s-1,\qquad 1/(s-2)=-s-1,\qquad -1/s=1-s
\]
show that the unordered parameter triple \(\{s,s-2,-s\}\) maps to \(\{1-s,-1-s,s-1\}\), precisely the triple for the conjugate root \(1-s\). Therefore both normalized solutions lie in one projective orbit. All possible arrangements have already been exhausted, proving uniqueness.

Near-freeness follows by projective invariance from the previously constructed degree-eight nearly free arrangement with the same basket. Alternatively, for this representative the published minimal-Jacobian-syzygy lower bound and its exact syzygy calculation give \(\operatorname{mdr}=4\), while \(\tau=3+3\cdot3+6\cdot4=36\); the standard numerical criterion yields exponents \((4,4)\).

## Verification
Run `python verify_geometry.py` and `python verify_classification.py` with Python 3 and SymPy (see `requirements.txt`). The first script performs exact arithmetic modulo the irreducible quadratic \(s^2-s-1\), independently constructs the six lines, all pairwise intersections, the conic incidences and tangent-line tests, and checks the basket and Tjurina number. The second checks the complete-quadrangle pair-incidence lemma by exhaustive combinatorics on six abstract lines, eliminates the tangent-normal-form equations symbolically, and verifies projective equivalence of the two conjugate parameter sets. Both scripts have been executed successfully from this package. The scripts support finite and algebraic certificates; the proof's universal quantification is the symbolic classification given above, not extrapolation from test cases.

## Relationship to prior work
Gałecka's 2022 paper introduces the near-freeness classification problem in this singularity class; it constructs degrees three through seven and leaves degree eight open. The later public mathematical result *A degree-eight nearly free conic-line arrangement over a quadratic field* provides an explicit member of this same basket and establishes near-freeness, but explicitly does **not** classify all arrangements. That prior existence result is not claimed here. The present theorem determines the **entire complex projective realization class** of its basket and shows that no other realization exists, including outside the previously exhibited coordinate model. Broader classifications of free (rather than nearly free) conic-line arrangements have different hypotheses and do not imply this result. Searches for equivalent projective-uniqueness formulations found no earlier full classification; this negative search is not a proof of priority.

## Limitations
Uniqueness concerns the single weak-combinatorial vector: one smooth conic, six lines, and the specified \((3,3,6)\) singularity basket. There may be other degree-eight nearly free arrangements with different vectors. The theorem does not settle degree-nine existence, determine the full marked realization scheme, or prove historical novelty independently of literature access. The explicit model is over \(\mathbb Q(\sqrt5)\), but no minimal field-of-definition assertion is made. Independent review has not been conducted.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969v1, first public 2022-04-29; Bol. Soc. Mat. Mex. 28 (2022), Article 67, DOI 10.1007/s40590-022-00461-4. See §§3–5 for the near-freeness criterion, minimal-syzygy bound, and open degree-eight question.
2. *A degree-eight nearly free conic-line arrangement over a quadratic field*, public mathematical research record (2026-10-04); result available at https://github.com/published-finding corpus/2026 (published record identifier: 2edf9ed667f2; locate by exact title). Its `RESULT.md` gives the precise earlier existence claim, exact basket and explicit non-classification limitation.
3. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, J. Algebraic Combin. 56 (2022), 403–424, DOI 10.1007/s10801-022-01116-3 (classification of free arrangements, not this nearly free basket).
