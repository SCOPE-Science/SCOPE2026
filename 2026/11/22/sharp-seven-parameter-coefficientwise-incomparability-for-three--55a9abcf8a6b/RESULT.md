# Sharp seven-parameter coefficientwise incomparability for three-triangle Henson type spectra

## Finding

Let \(H_4\) be the countable homogeneous universal \(K_4\)-free graph. For each finite individually named induced graph \(G\subset H_4\) with \(n\) vertices, let \(c_j(G)\) count complete nonalgebraic singleton types whose new point has exactly \(j\) neighbours in \(G\), and put \(P_G(z)=\sum_{j=0}^n c_j(G)z^j\). This is the already-known triangle-free induced-subset polynomial of \(G\).

**Sharp coefficientwise-order boundary.** At every fixed \(n\), the polynomials of graphs having at most two triangles are totally ordered coefficientwise. For exactly three triangles, all polynomials are totally ordered coefficientwise when \(n\le6\), but are not totally ordered for any \(n\ge7\). On seven vertices there are exactly seven distinct polynomials and exactly two unordered incomparable pairs among them.

**Complete all-size three-triangle classification.** At \(n=9\), exactly nine distinct polynomials arise, and for each \(n\ge9\) the possible polynomials are exactly those nine multiplied by \((1+z)^{n-9}\). Accordingly, for every \(n\ge9\) there are exactly nine possible polynomials and two unordered incomparable pairs. The possible numbers of polynomials for \(n=5,6,7,8,9\) are respectively \(2,4,7,8,9\); no graph of order at most four has exactly three triangles without containing a \(K_4\).

One explicit incomparable seven-point pair has triangle sets
\[
\mathcal T_A=\{\{0,1,2\},\{0,3,4\},\{0,5,6\}\},\qquad
\mathcal T_B=\{\{0,1,2\},\{0,1,3\},\{4,5,6\}\}.
\]
Take each graph to have precisely the edges belonging to these triangles. They are \(K_4\)-free and have exactly the displayed triangles. Their polynomials are
\[
P_A(z)=1+7z+21z^2+32z^3+23z^4+6z^5+z^6,
\]
\[
P_B(z)=1+7z+21z^2+32z^3+24z^4+6z^5,
\qquad P_A(z)-P_B(z)=z^6-z^4.
\]
In particular, \(P_A(1)=P_B(1)=91\): the two structures have the **same total number** of singleton types despite opposite inequalities in their graded counts. Thus neither coefficient vector dominates the other; adding isolated vertices preserves the incomparability for all larger \(n\).

## Assumptions and scope

All graphs are finite, undirected, simple and induced finite parameter subgraphs of \(H_4\). A triangle means a three-vertex clique; a base is admissible only if \(K_4\)-free. The integer \(n\) is fixed when comparing coefficientwise orders; the total number of triangles is counted as a set, not with multiplicity. Isolated-vertex addition is an operation on labelled parameters. There is no claim about arbitrary forbidden-clique sizes or multivariate type polynomials.

## Proof

**One-point correspondence (known).** A complete nonalgebraic one-point type over the individually named \(G\) is specified by its neighborhood \(S\subseteq V(G)\). It can be realized in the universal \(K_4\)-free graph exactly when \(G[S]\) has no triangle, because a new \(K_4\) would consist of the new vertex and a triangle of old neighbors. The finite extension property realizes every admissible \(S\). Hence \(P_G\) is the generating polynomial of subsets avoiding all old triangles.

**Exact inclusion–exclusion.** If \(G\) has exactly the distinct triangles \(T_1,T_2,T_3\), then
\[
P_G(z)=(1+z)^n-3z^3(1+z)^{n-3}
+\sum_{1\le i<j\le3}z^{|T_i\cup T_j|}(1+z)^{n-|T_i\cup T_j|}
-z^{|T_1\cup T_2\cup T_3|}(1+z)^{n-|T_1\cup T_2\cup T_3|}.
\]
Every term counts subsets containing a specified union of forbidden triangles, with its inclusion–exclusion sign. For two triangles, the same identity has one positive correction \(z^{6-s}(1+z)^{n-6+s}\), where \(s\in\{0,1,2\}\) is their intersection size. At fixed \(n\), the correction is coefficientwise larger as \(s\) grows: the successive differences are \(z^5(1+z)^{n-6}\) and \(z^4(1+z)^{n-5}\) when the configurations exist. A one-triangle graph has coefficientwise more admissible sets than every two-triangle graph (forget any second prohibition); a triangle-free graph has the most. This proves total order with at most two triangles.

**Sharp witness.** Pairwise triangle unions in \(A\) all have size five and the triple union has size seven. In \(B\), the pairwise union sizes are four, six, six, and the triple union has size seven. Substitution in the preceding identity yields \(P_A-P_B=z^6-z^4\), as claimed. Adding \(h\) named isolated vertices sends every polynomial to \((1+z)^hP\). In the difference \((1+z)^h(z^6-z^4)\), the least nonzero coefficient is negative and the greatest is positive, so no extension of this pair becomes coefficientwise comparable.

**Exhaustive classification and infinite reduction.** For an arbitrary three-triangle graph, all of its triangles occupy at most nine vertices. Extra vertices belong to no triangle and hence contribute freely, multiplying \(P_G\) by \((1+z)\) per vertex. Conversely, any triple of triangles realized on at most nine vertices can be realized on exactly nine by adding isolated points, and this retains the \(K_4\)-free condition. Therefore the complete classification for every \(n\ge9\) reduces rigorously to nine points. The separate finite checker enumerates every triple of three-element vertex subsets through nine points after relabelling the first triangle to \(\{0,1,2\}\), and retains a triple exactly if taking the union of its triangle edges produces no additional triangle. Every graph with exactly three triangles is represented by such an edge-union graph: any other edges cannot change the set of forbidden triples or the type polynomial. For each retained triple, independent direct enumeration of all \(2^n\) subsets agrees with the displayed inclusion–exclusion formula. The checker establishes the reported spectrum counts, incomparability counts and lower boundary through six points. This finite exhaustivity, combined with the nine-vertex reduction, proves the all-size claim.

For reproducibility, the nine polynomials at order nine share first four coefficients \((1,9,36,81)\), followed by these six-coefficient tails, in ascending lexicographic order:

| Tail coefficients for degrees \(4,5,6,7,8,9\) |
|---|
| 108, 81, 27, 0, 0, 0 |
| 108, 82, 30, 3, 0, 0 |
| 108, 83, 33, 5, 0, 0 |
| 108, 84, 36, 8, 1, 0 |
| 109, 86, 36, 6, 0, 0 |
| 109, 87, 38, 7, 0, 0 |
| 109, 88, 41, 10, 1, 0 |
| 110, 91, 44, 11, 1, 0 |
| 111, 95, 50, 15, 2, 0 |

Among the nine displayed spectra, the only two incomparable unordered pairs involve the tail \((108,84,36,8,1,0)\) against respectively \((109,86,36,6,0,0)\) and \((109,87,38,7,0,0)\). Their difference polynomials have lowest nonzero coefficients negative at degree four and highest nonzero coefficients positive at degree eight. Multiplication by \((1+z)^h\) preserves these opposite extreme signs. Every other pair is coefficientwise comparable and remains so after multiplication by a polynomial with nonnegative coefficients. This establishes exactly two incomparable unordered pairs for every \(n\ge9\), not merely at nine vertices.

## Verification

Run `python3 verify.py` with Python 3.8 or newer. No third-party packages are needed. The checker constructs all possible triples after normalizing a designated triangle, rejects those whose edge-union graph contains additional triangles, and for each valid triple compares independent direct-subset and inclusion–exclusion counts. It checks all seven base sizes from three through nine, the seven-vertex displayed witnesses and the complete nine-polynomial table, ending with `VERIFY_OK`. These are finite exhaustive calculations; the all-size extension follows separately from the proof above.

## Relationship to prior work

Herwig's 1995 preprint establishes extension properties for generic \(K_m\)-free graphs and provides the homogeneous setting. The previously published result *Exact finite-parameter 1-type counting in Henson graphs is #P-complete* identifies the general triangle-free-subset polynomial representation; this general identification is **not** new here. The present result specifically classifies all coefficientwise three-triangle profiles, proves the first incomparability boundary and reduces every larger size to nine canonical spectra. No inspected source supplies those further enumerative statements, though unindexed overlap cannot be excluded.

## Limitations

The complete nine-polynomial classification assumes exactly three old triangles. The classification does not enumerate isomorphism types or claim that the grade polynomial identifies a graph. The exact finite checker is not independent mathematical validation. Relevant older combinatorial work not located by indexed searches may contain equivalent statements.

## References

1. B. Herwig, *Many omega-categorical Structures Have the Small Index Property*, arXiv:math/9502206v1 (submitted 1995-02-14), https://arxiv.org/html/math/9502206v1.
2. *Exact finite-parameter 1-type counting in Henson graphs is #P-complete*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-parameter-1-type-counting-in-henson-graphs-is-p-com--7c84dde7c650.
