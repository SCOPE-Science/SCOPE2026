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

# Reproducibility and verification

Execute `python -m pip install -r requirements.txt` and `python verify_greedy_matching_roots.py` in Python 3. The program reconstructs the matching-size distribution recursively from the input tree's edge set, using exact rational arithmetic, and checks all unlabeled trees of orders one through thirteen.

The actual verification returned `PASS: 2288 unlabeled trees, six exceptional 13-vertex types; witness exact; 12! edge orders verified independently.` It checks the unlabeled-tree counts, full exceptional graph6 list, every support width and discriminant, the explicitly generated symmetric thirteen-vertex witness, its polynomial, and the negative integer discriminant. For the witness, a second integer dynamic program processes all edge orderings and separately yields the four exact multiplicities \(7484400\), \(77006160\), \(214095420\), \(180415620\), which sum to \(479001600=12!\).

These checks are a finite exact certificate only; no claim about larger orders follows from a finite calculation. Exhaustiveness relies on the standard nonisomorphic-tree generation algorithm and verified order counts. Floating-point approximations were not used for the mathematical assertions. Independent external audit remains unperformed.
