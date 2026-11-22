# The unique seven-point diameter obstruction for order and chain polytopes

## Finding

For a finite poset \(P\), write \(\mathcal O(P)\) and \(\mathcal C(P)\) for its standard order and chain polytopes, and \(d_{\mathcal O}(P)\) and \(d_{\mathcal C}(P)\) for their **one-skeleton graph diameters** (not Euclidean diameters). The following is a sharp size classification:

**Theorem.** Every poset with at most six elements satisfies \(d_{\mathcal O}(P)=d_{\mathcal C}(P)\). For seven elements, inequality occurs, up to poset isomorphism and order duality, only for the poset \(P_1\) of [Lee, Proposition 4.41(i)]:
\[
a,b\prec c\prec g,h,\qquad a\prec p\prec g,\qquad a\prec q\prec h.
\]
All displayed relations are covers after the obvious duplicate implications are removed; there are no further relations beyond transitivity. For \(P_1\) and its dual,
\[
d_{\mathcal O}=2,\qquad d_{\mathcal C}=3.
\]

Thus the first possible disparity between these Ehrhart-equivalent and edge-count-equivalent polytopes occurs in dimension seven and has precisely one duality orbit of extremal posets.

## Assumptions and scope

The poset is finite and may be disconnected. An ideal is a downward-closed subset; an antichain consists of pairwise incomparable elements. The vertices of the order polytope are ideal incidence vectors, while those of the chain polytope are antichain incidence vectors. The order dual reverses all comparisons. The theorem concerns **number of poset elements**, equivalently the dimension of either full-dimensional polytope, and graph distance along polytope edges.

## Proof

1. **Reduction to the five-element obstruction.** Let \(X\) be the poset with two incomparable elements strictly below a middle element and two incomparable elements strictly above it. By the Hibi–Li unimodular-equivalence criterion, recalled as Theorem 2 in [Lee], if \(X\) does not occur in \(P\), the two polytopes are unimodularly equivalent, hence their one-skeleton graph diameters agree. Therefore only posets containing \(X\) need to be tested.

2. **Exact edge predicates.** For distinct ideals \(I,J\), the segment between their incidence vectors is an edge of \(\mathcal O(P)\) if and only if \(I\subset J\) or \(J\subset I\), and the induced comparability graph on \(I\triangle J\) is connected. For distinct antichains \(A,B\), the analogous segment is an edge of \(\mathcal C(P)\) if and only if the comparability graph on \(A\triangle B\) is connected. These established criteria are [Lee, Theorem 1.5], quoting Ito–Tsuchiya and Chvátal. All operations in the supplied checker are finite bit operations; breadth-first search gives graph diameter exactly.

3. **Exhaustive representation.** Every finite poset admits a linear extension. Relabel the elements according to such an extension. Each strict comparison is then among pairs \(i<j\). There are exactly \(2^{\binom n2}\) upward-only relation choices. The transitive closure of each is a partial order, and every poset on \(n\) elements appears among them. Removing duplicate closures yields precisely \(40,357,4824,96428\) distinct upward-labelled poset orders for \(n=4,5,6,7\), respectively. The obstruction \(X\) occurs in precisely \(0,1,66,3705\) of these, respectively. For every obstruction-containing poset of size at most six, the exact graph search finds equal diameters.

4. **The seven-element classification.** Of the \(3705\) obstruction-containing seven-element relations, exactly \(46\) have unequal diameters, invariably \((d_{\mathcal O},d_{\mathcal C})=(2,3)\). The checker computes an isomorphism-invariant canonical adjacency code by minimizing the integer encoding of the directed strict-comparison matrix over all \(7!\) permutations. The \(46\) relations fall into exactly two classes, of \(23\) upward-labelled relations each, with respective canonical codes \(8658630260\) and \(8725738108\). Reversing every comparison interchanges the codes. The relation displayed in the theorem is checked to belong to one class. This proves the claimed uniqueness up to duality.

5. **Sharpness.** Independently of enumeration, the source [Lee, Proposition 4.41(i)] proves the diameter pair \((2,3)\) for \(P_1\). Reversing the order preserves the ideal and antichain graph diameters, through complementing ideal coordinates and leaving antichains unchanged. Thus both dual representatives realize the sharp gap.

The exhaustive certificate covers all relation choices, not a sample or a finite truncation of an infinite assertion; the theorem itself is a classification for the finite cardinality range \(|P|\le7\).

## Verification

Run `python3 CHECK.py` with Python 3.9 or newer. No external packages or input files are required. Its output ends in `PASS`. The certificate independently constructs all upward-labelled transitive closures; enumerates ideals and antichains; uses the stated exact edge predicates; computes all graph diameters by breadth-first search; and checks the two dual canonical classes and Lee's explicit representative. Key independently auditable enumerations are:

| Poset size | Distinct upward-labelled orders | Containing \(X\) | Unequal diameters |
|---|---:|---:|---:|
| 4 | 40 | 0 | 0 |
| 5 | 357 | 1 | 0 |
| 6 | 4824 | 66 | 0 |
| 7 | 96428 | 3705 | 46 |

The checker also tests that both seven-point types are mutual duals and that the witness has graph diameters \((2,3)\). The proof of representational completeness and correctness of each bit predicate is given above and in the program's docstrings. No numerical approximations or probabilistic sampling enter the certificate.

## Relationship to prior work

Stanley's poset polytopes are Ehrhart-equivalent, and Hibi, Li, Sahara and Shikama established equality of their edge counts. Jon Lee's 2026 paper proves a refined edge theorem and, crucially, gives the seven-element poset \(P_1\) as an **example** with graph diameters \((2,3)\), as well as a larger example with the opposite inequality. Its Theorem 1.5 supplies the edge tests used here; Proposition 4.41 supplies the seven-element witness. The new statement is the **minimum-cardinality necessity and complete classification of all minimum-size witnesses up to duality**, which are not assertions of Lee's paper. No claim is made to the seven-element witness or to the standard edge criteria themselves.

## Limitations

This finding does not classify diameter disparities for more than seven elements, give a bound for differences at arbitrary size, or address higher face numbers. The classification relies on a complete finite computer-assisted enumeration, with exact integer operations and a self-contained executable certificate; it is not a hand enumeration. Historical priority beyond the inspected sources and targeted mathematical database searches has not been independently established.

## References

- Jon Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413, first submitted 2026-10-05; Theorem 1.5 and Proposition 4.41. https://arxiv.org/abs/2610.07413
- Takayuki Hibi, Nan Li, Yoshimi Sahara and Akihiro Shikama, *The numbers of edges of the order polytope and the chain poyltope of a finite partially ordered set*, arXiv:1508.00187 (2015). https://arxiv.org/abs/1508.00187
- Dave Goel, *The Hibi–Li (2016) conjecture is fully resolved*, arXiv:2610.40703 (2026), for later face-number context. https://arxiv.org/abs/2610.40703
