# Scientific review of the Mycielskian-cycle Potts result

## Correctness (PASS)

The graph and Hamiltonian are precisely specified for every integer \(n\ge4\). The Mycielski coloring argument proves that the minimum number of equal-spin edges is zero for even \(n\) and one for odd \(n\), with explicit achieving colorings. Summing each clone spin independently gives a nine-state transfer identity for the entire low-temperature counting polynomial. The exact characteristic polynomial of the zero-order transfer matrix and its first-order insertion give both parity formulas; exact matrix identities prove the odd sequence recurrence for every length. All integer certificates were reconstructed using the embedded `verify.py`; a separate spin enumerator `bruteforce.cpp` corroborated the four smallest test sizes. Exhaustive finite examples are not confused with the infinite proof. The large-length growth constant follows from simple, positive, distinct cubic roots and a nonzero leading residue.

## Originality (PASS on checked evidence; residual priority risk)

The exact \(n=5\) three-state Potts computation is acknowledged as existing. The earlier all-length Ising result has a two-spin alphabet, a different Hamiltonian, different ground energies and different multiplicities; it does not imply the present three-spin formula. The classical Mycielski color theorem determines only existence or nonexistence of proper colorings, not their exact counts or one-defect census. Chang–Shrock (arXiv:0907.0777) and Shrock–Xu (arXiv:1009.1182) provide general Potts partition and weighted-coloring frameworks for arbitrary graphs and evaluate other families, but the examined sections and targeted searches do not exhibit an evaluated Mycielskian-cycle three-state parity sequence. Sokal's general Tutte formalism likewise expresses the relevant coefficient but does not by itself evaluate the specific cubic recurrence. A directly equivalent published graph polynomial, an unindexed table, or an inaccessible detailed appendix could cover the claim; this risk remains.

## Mathematical value (PASS)

The ordinary Mycielskian of a cycle is an intrinsic, well-motivated infinite family of sparse graphs with a sharp chromatic parity obstruction. Counting all minimum-energy three-state Potts configurations, not just the unavoidable frustration number, yields a nontrivial cubic recurrence, a length prefactor on odd cycles, and a shared exact residual entropy density. This measures precisely how a single global coloring obstruction coexists with exponentially many lowest-energy microstates. The family-wide parity law is not a relabeling of a standard coloring count and is not justified solely by finite computation. No thermodynamic phase transition or arbitrary-graph result is claimed.

## Closest literature and limits

- Chang and Shrock (2009), arXiv:0907.0777: general external-field Potts/Tutte identity, relevant for coefficient interpretation, not an evaluated cycle-Mycielskian census in inspected text.
- Shrock and Xu (2010), arXiv:1009.1182: generalized-field formulation with explicit other graph families, relevant as potentially stronger coverage; inspected introduction, formulas, selected evaluation and conclusion, with full-document text searches for Mycielski/Grötzsch.
- Chang, Huang and Zhu (1999), DOI 10.1016/S0012-365X(99)00033-3: circular chromatic numbers and graph family; introductory material accessible, full article not obtained.
- Sokal (2005), arXiv:math/0503607: generic graph-polynomial background; not an evaluated result for these multiplicities.

The result is restricted to uniform positive coupling, three classical spin states, zero field, and cycle Mycielskians. The journal article and broad historical tables were not exhaustively surveyed, and the full text of the 2012 Xu dissertation was unavailable; these are residual priority risks.

Self-review: passed. Independent audit: not yet performed.
