---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Exact verification

Run `python3 verify.py` in the same directory as this file. It needs only Python's standard library and checks the following exact integer assertions: the value of the proposed quotient polynomial at \(3\); all legal base-three carry transitions for the \(32\) states in the closed set; absorption of its \(12\) dead states; the unique weighted encoding for each of the \(20\) live carries; all \(26\) internal live edges' polynomial-digit identities; and the precise reachability and returnability sets independently reconstructed by graph search. It also tests \(1,022\) bounded returning walks, the positive representation \(80920/280=289\), and a local control at multiplier \(22\).

The program should print `VERIFY_OK live_states=20 dead_states=12 live_edges=26 returning_paths_through_length_38=1022 identity_for_all_lengths=finite_state_proof`. The proof of the theorem's arbitrary-length quantifier depends on the state-closure and transition-induction argument stated in `RESULT.md`. The independent audit remains unperformed.
