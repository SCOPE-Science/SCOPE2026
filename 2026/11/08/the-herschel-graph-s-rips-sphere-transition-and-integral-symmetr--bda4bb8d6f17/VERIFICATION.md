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

# Verification scope

The included standard-library program `verify_rips.py` computes the exact graph distances from the literal edge list and checks them using two independent shortest-path algorithms. It enumerates all eleven-vertex subsets at each distance threshold, constructs an 88-pair acyclic discrete-Morse matching, topologically sorts all 178 directed cover faces and 526 incidences, and checks 767 explicit unique-coface elementary collapses at distance three. A separate mod-two simplicial boundary-rank computation corroborates the nonzero integral sphere stage but does not alone prove the homotopy statement.

For symmetry, the graph degree pattern proves the automorphism group has at most twelve elements, and the program constructs and checks all twelve permutations. It calculates signed simplex traces and Lefschetz numbers exactly, verifying the product-sign orientation character. All stages, restrictions, critical cells and terminal counts are independently reproducible from the graph's 18 edges; no downloaded data or third-party libraries are needed.

To replay, run `python3 verify_rips.py` alongside the extracted file. The provided `verification_output.txt` contains the complete recorded standard output; the final line is `ALL_CHECKS_PASS`. This check is computational verification of an explicit finite proof, not independent validation and not a statement about all graph families.
