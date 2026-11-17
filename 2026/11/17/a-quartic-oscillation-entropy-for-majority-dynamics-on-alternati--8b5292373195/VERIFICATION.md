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

# Reproducibility of the mathematical claims

All calculations use the deterministic, labelled graph and recurrence defined in `RESULT.md`.

Run `python3 transfer_check.py` in an environment with SymPy. The program reconstructs the 16-by-16 decorated and undecorated transfer matrices directly from their bit predicates, checks the exact characteristic polynomial, and independently checks the four-state fixed-word transfer polynomial. It then prints the integer fixed populations, two-step-return populations and primitive two-cycle orbit counts through \(m=12\). Compare with `transfer_output.txt`.

Compile and run `g++ -O3 -std=c++17 microscopic_check.cpp -o microscopic_check && ./microscopic_check`. This program uses graph-neighbor bit updates, not transfer matrices. It enumerates exactly \(19,173,952\) assignments for sizes \(m=2,3,4,5,6,7,8\) and directly tests both one-step and two-step return. Its output is `microscopic_output.txt`. These are actual reproduced checks, not claims about all infinite sizes.

The all-size proof is the bijection between returning configurations and closed transfer walks; the determinant identity is exact symbolic linear algebra, and the dominant-root analysis is analytic. The checker can confirm the determinant identity but does not certify historical originality, external audit, or eventual attraction-basin populations.
