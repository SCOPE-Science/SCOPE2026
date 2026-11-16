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

# Reproducible verification

From the directory containing the supplied scripts, run `python3 check_exact.py` and `python3 check_symbolic.py` using the Python standard library. Both commands were executed successfully against the delivered source text.

The direct checker enumerates all balanced bitstrings of lengths \(6,10,14,18\), independently tests least cyclic period, calculates the complete integer Walsh transform, verifies Parseval, checks that the only zero frequencies have odd weight, and verifies prime specializations. Its observed ranks are \(32,512,8192,131072\), respectively, and its successful run ends in `CHECK_EXACT_PASS`.

The independent combinatorial checker enumerates all signed multiplier multiplicities for prime half-lengths \(3,5,7,11,13\), and checks their totals, sharp positive extrema and minimum multiplicities. It also evaluates small exceptional inequalities and positive spectral gaps for odd half-lengths at most \(401\). Its successful run ends in `CHECK_SYMBOLIC_PASS`.

The infinite statement is proved algebraically using periodic-word repetitions, the Krawtchouk transform, a strict finite-to-exponential comparison, and Fourier diagonalization. Verification programs alone would not prove the all-length conclusions. No independent audit has been carried out, and no formal proof-assistant certificate is claimed.
