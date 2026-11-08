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

# Verification performed

Executed `python3 verify_bruteforce.py` using a fresh bounded-state enumeration, independently of the firing-phase proof. All nonnegative chip vectors in the confinement box were tested for \(b=3,4\): respectively 46,656 and 663,552 vectors. The exact least-period-three chip-mass histograms matched the predicted coefficients; the results appear in `verification_bruteforce.txt`.

Executed `python3 verify_polynomial.py` for every integer \(3\le b\le30\). It compares the positive-composition polynomial against the fully signed expanded numerator of the rational formula after multiplying by \((1-z)^3\), and checks all coefficient supports, palindromicity, endpoint coefficients and total counts. The output is in `verification_polynomial.txt`.

The proof itself is the necessary-and-sufficient phase-interval classification, connected-graph firing-count rigidity, and chip-complement involution. Computation is corroborating finite evidence, not an infinite proof, and no independent audit has been performed. Re-run both standalone Python programs with the Python 3 standard library.
