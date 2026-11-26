# Independent mathematical audit

## correctness

PASS

Pure adjacency and equality encode distances capped at two. For ordered triples the five coordinate patterns capture exactly the possible next-symbol choices, and the corresponding capped distance vectors combine by associative capped addition. Pair orbits are indexed by Hamming distance, and vertex transitivity reduces the last recursion to the set of pair types from a fixed vertex. An independent implementation (`cd /workspace && python3 audit-evidence/hamming.py`) checked all 378 singleton-state transition identities and exhaustively compared the types in dimensions 1 through 14 for alphabets 2, 3, and 4. It recovered the sixteen classes, including all cross-alphabet inequalities. The infinite reduction is exact: truncating bin counts at positive caps preserves all profiles beyond the sum of the caps, since excess coordinates can be absorbed by a saturated bin. Pair profiles are thus clipped at (6,8) or (5,9), whose caps sum to 14, so all dimensions at least 14 realize the same set of clipped profiles. At most four distinct symbols per coordinate can be used in four rounds, giving the alphabet tail. These facts also establish sharpness of the 1024-vertex bound within the family; the independent check does not rely on the record's reported runs.

## originality

FAIL

A distinct catalogued finding dated 2026-10-26 states exactly the whole rank-four theorem, including the supposedly new nonbinary regimes, cross-regime distinctions, and sharp representative. This is demonstrable existing coverage, regardless of whether the records are related revisions or have common authorship. It is not a claim about authorship or external priority.

## value

FAIL

The finite-rank cutoff and sharp representative are mathematically useful, but this frozen record adds neither a new class, scope nor independent structural consequence to the exact October finding. The validated replay is corroboration, not a separate scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
