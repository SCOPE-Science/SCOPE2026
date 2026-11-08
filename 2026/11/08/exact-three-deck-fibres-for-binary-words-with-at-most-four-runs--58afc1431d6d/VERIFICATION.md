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

# Reproducibility

Execute `python3 verify.py` from this directory (Python 3, standard library only).

The verifier enumerates all binary words of length \(1\le n\le28\) with at most four constant runs and groups their exact scattered subsequence multiplicity vectors through length three. It checks the complete fibre classification, every repeated class, the divisor census, and the resulting code sizes. It separately verifies injectivity of the length-at-most-four deck for \(1\le n\le24\), the explicit first collision witness, and the arithmetic count constraints for \(1\le n\le300\).

The proof in `RESULT.md` establishes the unrestricted-in-length theorem. Enumeration is independent numerical corroboration, not an inference from finite evidence to all \(n\). No independent scientific audit has been conducted.
