# Scientific review: exact Kneser fourth coefficients

## Correctness — PASS

Four distinct queried triples are completely specified up to ground-point relabeling by fifteen nonempty four-bit Venn-cell multiplicities whose four row sums equal three. Exhaustion of the 666 distinct-query profiles is finite and complete for all orders. The actual center traces depend only on whether the center uses up to three points outside the query union, which yields a minimal-external-point classification. Exact factorial multiplicities, divided by 24 to remove query order, give both coefficient tables. The packaged Python verifier reproduced the entire table, while a separate C++ direct support enumeration independently confirmed the complete order-nine degree-zero-through-four prefixes. The larger-order claims rely on the exhaustive-profile proof, not finite experimental extrapolation.

## Originality — PASS, qualified

Full-text comparisons were made with the Johnson/Hamming neighborhood work of Adler–Benediktsson–Macpherson, the graph VC algorithm paper of Coudert–Csikós–Ducoffe–Viennot, and related disjointness literature. The closest indexed published Kneser result gives the exact *dimension* and witnesses, and another gives the **six-support** classification at order thirteen. Neither implies the full **four-support coefficient sequences**, especially the closed-neighborhood correction. Search covered equivalent formulations, statement-level implication, stronger-coverage work, and exact tables. Inaccessible or unindexed equivalent literature remains a priority risk, not mathematical evidence of uniqueness.

## Value — PASS

The fourth layer is the first nontrivial higher-rank layer of three-set Kneser disjointness neighborhoods. Counting all supports for every ambient order is a natural refinement of the already-known VC-dimension threshold, and the comparison of closed and open neighborhoods exhibits a structural difference that appears one order after the common rank-four onset. The formulas supply all integer coefficients, their sharp activation conditions, and matching leading asymptotic terms. This is not an arbitrary small slice or a recomputation of a known VC dimension.

## Limits

The 666-profile census is proof-critical and supplied as readable standalone source. It does not classify higher support sizes; no general VC-dimension theorem is claimed. All originality conclusions are best-knowledge and subject to priority risks. Independent scientific validation is not available.

Self-review: passed. Independent audit: not yet performed.
