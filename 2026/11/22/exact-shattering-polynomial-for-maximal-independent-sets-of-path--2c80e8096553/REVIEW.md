# Scientific review

## Correctness — PASS

The legal maximal-independent-set words have a five-state prefix automaton, equivalently a source-to-sink jump graph on selected vertices with increments two or three. The support-shattering test follows both ways by concatenating positive selected vertices through avoidant directed paths. The finite-state construction for universally realizable support traces is inductive in the word length, and all 28 reachable subset families and the stable six-state quotient are reconstructed by `checker.py` and explicitly recorded in `automaton_certificate.json`. The resulting rational generating function gives the coefficient formula by formal binomial expansion, including every normalization and boundary case. A separate direct enumeration verifies all support traces through length thirteen; transfer and coefficients match through length 100. Those finite tests corroborate the finite-state proof and are not treated as an infinite proof on their own.

## Originality — PASS, qualified to inspected evidence

The earlier published path finding *Linear static–online shattering separation for maximal independent sets of paths* already proves the same VC dimension and an adaptive separation. It does not state the full face polynomial, individual-support reachability criterion or exact maximum-rank counts in the accessible summary; no novelty is claimed for the known VC formula. The published cycle shattering polynomial is for cyclic rather than open boundary conditions and does not mathematically imply the path coefficients without new arguments. Johnson's binary-string paper treats a single sequence's translates and is not the family of all maximal independent sets; Beaton–Brown–Cameron enumerate all independent sets rather than shattered supports. Indexed published-finding corpus searches for polynomial forms, aliases and stronger coverage did not return the exact path-face enumerator. Full documents behind the closest indexed path/cycle entries were not accessible, so equivalent statements in their body/appendices are a genuine priority risk; an unsuccessful search does not establish uniqueness.

## Value — PASS

The complete integer-coefficient formula classifies an infinite graph-indexed family of shattered-support complexes; the pairwise reachability criterion determines individual faces and avoids enumerating all labelings; the sharp top layer contains exactly \(2^k\) faces at order \(3k-1\), and the complex is demonstrably nonpure. The rational enumeration and its efficient finite-state certificate give substantially more information than the previously known scalar VC dimension and provide a reproducible benchmark for shattering under graph-theoretic maximality constraints.

## Closest literature and limitations

The relevant prior records are Johnson (arXiv:2101.06490), Beaton–Brown–Cameron (arXiv:1810.05317), Liu–Shangguan–Skokan–Xu (SoCG 2024, Lemma 27, a general VC/induced-matching upper bound), the published path online/static separation, and the published cycle shattering polynomial, as identified and distinguished in `RESULT.md`. No formula for the exact Littlestone dimension is asserted. Equivalence to an uninspected prior manuscript cannot be ruled out. The proof is reviewed only at the same-model level.

Self-review: passed. Independent audit: not yet performed.
