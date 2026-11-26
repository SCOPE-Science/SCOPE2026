# Independent mathematical audit

## correctness

PASS

The 16 distinct selected starts occur in a cyclic order. Each positive gap is at least the least compatible shift (2 for a nonconstant reversed ordered pair, 3 for equal outer letter, 4 otherwise). Conversely a cyclic target tour can be laid out at its least shifts: adjacent windows match on each overlap, and nonadjacent starts are separated by at least four positions in either cyclic direction when they are nonadjacent on both sides. Thus all windows are compatible, including closing the cycle. At minimum cost every selected gap attains its bound, so every optimum is recovered by a minimizing tour. The exact subset recurrence anchors at 0000, goes to an unvisited target, and charges the final return to 0000. An independently written exact checker at /workspace/branches/0c226ade-1e89-49d6-b73e-b5ca8fee2efc/independent_census.py (result_q4.txt in the same directory) found minimum 44 and visited every optimal successor, giving 5472 tours. It scanned all cyclic windows, verified each required factor occurs once in each expansion, and recovered the generating order from each circle, yielding 5472 distinct rotation classes without dividing by reversal. Applying the 24 global permutations and reversal, with renormalization by the unique 0000, gave 124 orbits (105 of size 48, 17 of size 24, 2 of size 12) and exactly matched all representative/orbit-size pairs in the frozen CSV. This is exhaustive at q=4 only.

## originality

PASS

The supported distinct contribution is the exact census of all shortest labeled circles, uniqueness of each required occurrence in every optimum, and the full symmetry quotient. The minimum 44 is demonstrably covered by a distinct same-day general formula, and receives no separate originality credit. No intra-day order is established. The closely related general record and its verifier do not enumerate the optimizers; the present frozen finding is a census rather than a minimum-only claim.

## value

PASS

The quaternary case is the first even alphabet beyond the binary case and exhibits a nontrivial parity obstruction and nonuniform symmetry stabilizers. An equality census for this natural cyclic cover problem answers more than a rerun of its known minimum: it proves unique target occurrences in every shortest host, distinguishes true labeled multiplicity from symmetries, and makes all symmetry representatives available for further structural comparisons. Neither the minimum nor one optimal construction resolves those questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
