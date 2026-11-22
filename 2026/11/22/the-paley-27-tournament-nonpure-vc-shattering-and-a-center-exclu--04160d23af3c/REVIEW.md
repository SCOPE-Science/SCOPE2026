# Review of the Paley-\(27\) neighborhood-shattering classification

## Correctness — PASS

The finite domain is exactly the 27 elements of \(\mathbb F_3[u]/(u^3-u+1)\); the irreducibility check and the nonzero-square convention are explicit. Exhaustive search over every support of cardinality 1–4 finds ordinary coefficients 27, 351, 2925, and 5967, and outside-center coefficients 27, 351, 2925, and zero. All larger supports are excluded because 32 independent label masks would require at least 32 concepts, but only 27 exist. Each of 22 four-support affine-semilinear orbits is fully covered and the orbit sizes sum to 17,550. The 351 unextended triples form one orbit and a 2-(27,3,3) design (checked independently by pair incidence). Exact binary simplex-boundary reductions give ranks 26, 325 and 2249, hence reduced Betti ranks 351 and 3718. The Python and C++17 source files use different irreducible field representations and different arithmetic constructions, and both are replayable. Source code, not the stored logs, is the evidence.

Risk: finite arithmetic or a shared misinterpretation of shattering could still escape self-review. No integral or infinite-field result follows from these finite checks.

## Originality — PASS against inspected records

McDonald–Sahay–Wyman (2022, arXiv:2210.03789) study the same quadratic-residue translation class and prove general bounds, but their numerical experiments restrict to prime fields, so do not give the full GF(27) polynomial, orbits, maximal triples or homology. Their discussion of zero-character and center exclusions motivates the precise convention comparison. Pham–Senger–Tait–Nguyen (2023, arXiv:2303.07878) establish pseudorandom graph VC bounds, not this exact finite count.

The published published-finding corpus classification of four-variable deletion thresholds establishes that every 3-support has an outside-center extension at order 27; that **constituent is prior coverage** and is not claimed separately as original. The published rank-five genericity classification shows that not all 4-support patterns have outside-center witnesses at order 27, but this does not imply the new claim that **none** of the 4-supports are fully outside-center shattered. Published Paley-25 graph shattering is a different undirected field; Paley-23 out-neighborhood topology concerns the downward closure of positive neighborhoods, not the Boolean all-traces shattering complex. Published online learning bounds do not imply this static polynomial. Search by field, synonyms, support counts, orbits, aliases, and alternative complex definitions found no covering equivalent theorem. Actual searches and closest source IDs appear in AUDIT.json.

Risk: unindexed computational tables, an overlooked full-text passage, or an independently derived equivalent classification could establish earlier priority; literature search does not prove uniqueness. Additional relevant unpublished computations may remain undiscovered.

## Value — PASS

The order-27 Paley tournament is the first nonprime field order congruent to three modulo four, a natural test of prime-field-only empirical VC observations. The full coefficientwise polynomial distinguishes ordinary and off-support concepts sharply at the extremal layer; the nonpure facet layer is a balanced 2-design, while the full mod-two homology has two adjacent nonzero degrees. These are mutually reinforcing finite combinatorial and topological invariants of a canonical quadratic-character incidence class, not a detached arbitrary slice or a small numerical tweak. A natural use is to test how arithmetic field extension, center-convention changes and shattering-complex topology interact in larger families.

Risk: the result has no all-field theorem and no independent priority review. It is valuable as an exact finite classification, not as evidence of an unproved universal pattern.

Self-review: passed. Independent audit: not yet performed.
