# The nonpure shattering complex of five-point linear-order betweenness

## Finding

Fix five labeled points \(X=\{0,1,2,3,4\}\). Let \(\mathcal{C}_5\) be the binary concept class whose concepts are all strict linear orders of \(X\), observed only through ternary betweenness queries. A query \(B(m;a,b)\) asks whether \(m\) lies strictly between the distinct endpoints \(a\) and \(b\); the endpoints are unordered, and the middle point is distinguished. There are \(3\binom{5}{3}=30\) distinct queries.

For a subset \(S\) of queries, call \(S\) *shattered* when for each binary assignment to all queries in \(S\), some linear order realizes that assignment. Define \(\Phi_5(z)=\sum_{S\text{ shattered}}z^{|S|}\). Then

\[
\boxed{\Phi_5(z)=1+30z+405z^2+2700z^3+510z^4.}
\]

Thus \(\operatorname{VCdim}(\mathcal{C}_5)=4\). Exactly \(1530\) inclusion-maximal shattered supports have three queries, and exactly \(510\) have four. Under the natural permutation action of \(S_5\), the two types of maximal supports have respectively \(18\) and \(7\) orbits, giving \(25\) facet orbits in all. In particular, the shattering complex is **not pure**: some maximal supports have three queries even though four-query supports are shattered.

For context and as separately verified smaller cases, \(\Phi_3(z)=1+3z\), whereas \(\Phi_4(z)=1+12z+54z^2\). No extrapolation to arbitrary numbers of labels is asserted.

## Assumptions and scope

A strict linear order is a permutation \(\pi\) of \(X\). Define \(\operatorname{pos}_{\pi}(x)\) as the zero-based location of point \(x\) in that order. For all pairwise distinct \(m,a,b\), the binary answer is \(1\) precisely when

\[
\min(\operatorname{pos}_{\pi}(a),\operatorname{pos}_{\pi}(b))
<\operatorname{pos}_{\pi}(m)<
\max(\operatorname{pos}_{\pi}(a),\operatorname{pos}_{\pi}(b)).
\]

There are exactly \(30\) query coordinates and \(5!=120\) permutations. An order and its reversal give the same answers. The finite checker confirms that these reversals are the only coincidences, leaving \(60\) distinct concept rows.

The query indexing used in the supporting certificates is explicit: enumerate each three-element subset \(\{a,b,c\}\) in lexicographic order, and for each such subset take its possible distinguished middle element in increasing label order; the remaining two elements are the unordered endpoints in increasing label order. Indices start at zero. The TSV files encode query supports in this order.

## Proof

**Exhaustiveness of the concept representation.** The accompanying independent script `check_betweenness5.py` constructs every permutation of \(X\) by two algorithms: library permutation generation and recursive insertion of successive labels. Their outputs are compared as sets. It then implements the answer predicate twice, once using positions and once using pairwise relative comparisons. The resulting complete sets of \(30\)-bit concept rows agree, have cardinality \(60\), and contain precisely every permissible betweenness response pattern.

**Exact shattering test.** For each nonnegative integer \(k\le5\), the script enumerates **every** \(k\)-subset of the \(30\) query coordinates. On each support it projects all \(60\) concept rows, constructing the set of realized \(k\)-bit traces. The support is shattered if and only if this set has cardinality \(2^k\). This is an exhaustive decision procedure, not random sampling or a heuristic. Its run yields the face counts \(1,30,405,2700,510,0\) for sizes \(0\) through \(5\). In particular, the size-five computation explicitly excludes all \(\binom{30}{5}=142506\) possible five-query supports. Every support of size greater than five contains a five-query subset, so none of those is shattered either. Consequently, the displayed polynomial has no further terms and the VC dimension is four.

The quadratic coefficient provides a direct cross-check: every two distinct betweenness queries are jointly shattered except when their triples of underlying points coincide but the designated middle elements differ. On each of the \(\binom{5}{3}=10\) underlying triples, the three distinct middle predicates are mutually exclusive, excluding \(\binom{3}{2}=3\) pairs. Thus \(\binom{30}{2}-10\binom{3}{2}=405\), as enumerated.

**Complete facet classification.** A shattered support is inclusion-maximal if it has no shattered one-coordinate extension; this immediate-extension criterion is sufficient by downward closure. The script checks this condition on the complete enumerated face collection, obtaining \(1530\) maximal triples and \(510\) maximal quadruples. For each of the \(120\) permutations of the five labels it computes the induced action on all \(30\) query coordinates. The file `facet_orbits.tsv` contains precisely one representative of each of the \(25\) distinct facet orbits, its size, exact orbit cardinality, and trace count. The verifier independently expands each listed orbit and proves by finite equality of sets that these orbits are disjoint and exhaust *all* facets. It also regenerates the entire face collection by taking subsets of those facets, comparing the result against the direct shattering enumeration. The size-three orbit cardinalities sum to \(1530\); the size-four orbit cardinalities sum to \(510\).

**Explicit four-query lower-bound certificate.** The four coordinates \(\{4,7,10,13\}\) designate the queries \(B(1;0,3)\), \(B(1;0,4)\), \(B(2;0,3)\), and \(B(2;0,4)\). The file `witness_4.tsv` lists one full linear order for each of the sixteen binary assignments to these coordinates. Its content is checked by the independent position-based predicate. Thus even without the full face counts it gives a small certificate that \(\operatorname{VCdim}(\mathcal{C}_5)\ge4\).

For \(3\) and \(4\) labels the same exhaustive two-generator/two-predicate method checks all possible query supports up to the information bound from the number of distinct concept rows. This gives the stated smaller polynomials.

## Verification

Place the three attached files `check_betweenness5.py`, `facet_orbits.tsv`, and `witness_4.tsv` in one directory. Run `python3 check_betweenness5.py` using an ordinary Python 3 installation; no third-party libraries or downloaded data are required. A successful complete replay prints `BETWEENNESS5_PASS` with the face, facet and orbit counts. The certificate contains all \(25\) facet-orbit representatives and \(16\) explicit four-query witnesses, and the checker reconstructs rather than trusting their summary counts.

The proof is a finite, fully enumerated computation on all \(30\) queries and all \(60\) distinct response rows. The executable source is part of the mathematical certificate, not an indication that a nontrivial infinite assertion has been established.

## Relationship to prior work

Ternary betweenness of linear and tree orders is a classical model-theoretic object. Courcelle's work on order-theoretic tree betweenness (arXiv:2004.10127; arXiv:2111.15357) establishes definability and structural axiomatizations. Those investigated results do not enumerate the five-point binary betweenness-query shattering complex. Raz's notion of VC dimension for *sets of permutations* is based on realizing all linear orders on selected positions and is a different, multivalued projection predicate; it does not immediately imply the exact four coefficients or the facet-orbit classification here. Work on betweenness-feasibility constraints addresses satisfiability rather than all binary trace profiles. The distinction from cyclic-orientation queries is material: whether one element is the middle of a linear triple is invariant under reversal and is not the same Boolean function as orientation of a cyclic triple.

A historical priority search did not identify the precise face polynomial or the combined facet census. The possibility of equivalent results in older constraint satisfaction, order theory, or computational databases remains an explicit limitation.

## Limitations

The enumeration is confined to the five-label concept class, with three- and four-label comparisons. It establishes no general formula for all ground-set sizes, no bound on arbitrary-instance computational complexity, and no independent external mathematical validation. Older literature on betweenness feasibility and permutation shattering may contain terminology that hides an equivalent finite census. The submitted source and TSVs are sufficient to rerun the claimed finite proof, but cannot certify originality globally.

## References

- Bruno Courcelle, *Axiomatization of betweenness in order-theoretic trees*, arXiv:2004.10127, initially public 21 April 2020. https://arxiv.org/abs/2004.10127
- Bruno Courcelle, *Induced betweenness in order-theoretic trees*, arXiv:2111.15357, initially public 30 November 2021. https://arxiv.org/abs/2111.15357
- Ran Raz, *VC-dimension of sets of permutations*, Combinatorica 20 (2000), 241–255. DOI: 10.1007/s004930070023.
- Benny Chor and Madhu Sudan, *A geometric approach to betweenness*, SIAM Journal on Discrete Mathematics 11 (1998), 511–523. (bibliographic context; full text not used as proof).
