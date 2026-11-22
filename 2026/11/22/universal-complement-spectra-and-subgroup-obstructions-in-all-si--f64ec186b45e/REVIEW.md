# Scientific review

## Correctness — PASS

The finite scope is explicit: five groups of cardinality sixteen, all nonempty subsets of cardinality dividing sixteen, all complements modulo translation, and all possible spectra modulo translation. Two standalone integer checkers agree on the complete size-resolved table. One enumerates complements by exact-cover recursion and spectra by a clique search; the other directly tests every row subset and all normalized complement subsets and candidate frequency sets. The cyclotomic vanishing test is necessary and sufficient because the groups have exponent a power of two. The frequency subgroup scan is exhaustive; this supports negative obstruction counts rather than relying on failure to find witnesses. The normalization factor used only by the recursive checker follows from double counting. No extrapolation from finite experiments to arbitrary group order is claimed.

## Originality — PASS under bounded comparison

The literature already supplies the definition and Fourier-zero criterion for common spectra, plus cyclic prime-power existence, and the group \(\mathbb Z_4^2\) subgroup-obstruction count is covered by an earlier exact result. The accepted contribution is the **full comparative five-group census** and the additional obstruction counts \(764,1056,896,0\), not the preexisting special case or generic existence criterion. Full-text portions of the original universal-spectrum papers were compared with these statements, alongside published finite-group and Fourier-minor tables. None of the inspected sources supplies or implies the entire exact comparative subgroup-coset incidence table without new enumeration. Unindexed parallel calculations remain a possible priority risk; the source search cannot certify global uniqueness.

## Value — PASS

The universal-spectrum question originated as a significant harmonic-analysis interface between tilings and character bases. The new table measures a distinct and mathematically necessary strengthening: whether a **single subgroup-based frequency design** works uniformly across all complements of each tile. At fixed group size, this property distinguishes the elementary abelian group (no obstructions) from all four non-elementary types and quantifies each obstruction by tiling-set cardinality. This is a natural complete classification, not a selected arbitrary test instance, while its scope remains purely finite.

## Closest literature and limitations

Lagarias–Wang (1997), Theorems 1.1–1.3, are especially close: in particular the cyclic existence case is not new. Lagarias–Szabó (2000) treats universal cyclic spectra and related factorization criteria; Kolountzakis–Matolcsi (2004) supplies a counterexample beyond this small size; Farkas–Matolcsi–Móra (2006) explains the common-zero criterion. Existing public counts for \(\mathbb Z_4^2\) and \(\mathbb Z_4\times\mathbb Z_2^2\) are not repackaged as new results. The theorem does not extend to order thirty-two or any infinite family and has not had independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
