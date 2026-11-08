# Scientific review: all identifying codes of two-corona graphs

## Correctness — PASS

For a connected core with at least two vertices, the private support–leaf closed-neighborhood symmetric difference forces every core vertex into every identifying code; the leaf's nonempty trace forces at least one of the two private path vertices. These conditions yield exact trace formulas. Base traces each contain at least two core vertices, support traces exactly one, and leaf traces none. The sole possible collision is between two base vertices with identical core closed neighborhoods and with both private support vertices omitted. This proves the necessity and sufficiency of the stated *at most one leaf-only choice per closed-twin class* rule. Summation of the disjoint local cases gives the product polynomial, roots, minimum multiplicity, and size support. The boundary \(H=K_2\) is included; \(H=K_1\) is explicitly excluded. A separate direct subset verifier checks 49 connected labeled cores/representatives and 583744 subsets.

Risk and limit: finite checks cannot independently prove the assertion for arbitrarily large cores; the unrestricted argument is the exact trace classification, not the enumeration output. The claim counts labeled subsets rather than automorphism types.

## Originality — PASS (publication priority provisional)

The most relevant primary source is Foucaud–Lehtilä, *Revisiting and improving upper bounds for identifying codes* (2022, arXiv:2204.05250), Proposition 9 and Theorem 10. Its Proposition 9 already proves the optimal size \(2h\), forces every base vertex, and gives particular optimal constructions; those facts are not asserted here as new. Neither its statement nor its proof classifies all legal private-path choices when core vertices are closed twins, gives the complete labeled identifying-code polynomial, counts all minimum codes, or recovers the closed-twin profile from polynomial roots. The 2015 Canoy–Malacas study uses a one-step corona operation and is not a two-corona count. The open/total identifying-code variant studies a distinct feasibility condition. Searches for exact two-corona code counting, equivalents under differentiating-domination terminology, and stronger general corona graph enumeration uncovered no dominating theorem.

Residual risks: some unpublished/unindexed study or uninspected article may already contain an equivalent enumeration; bibliographic absence does not establish absolute priority. The visible 2022 proof makes the forced-vertex part known, so originality is assigned to the complete twin-class-sensitive characterization and polynomial, not the scalar bound.

## Mathematical value — PASS

The two-corona family is the recognized extremal family for identification-number density \(2/3\) in the cited graph-code research. A complete code distribution resolves the natural enumeration that remains after its scalar extremum is established, including the precise number of optimal sensor placements. Dependence on the entire closed-twin size profile is a structural refinement: graphs with the same order but different twin profiles have different code polynomials, and the polynomial factors recover that profile. The real-rootedness and sharp independent sensor-success probability are additional concrete consequences. This is not an arbitrary small numerical improvement or a relabeling of the original bound.

Self-review: passed. Independent audit: not yet performed.
