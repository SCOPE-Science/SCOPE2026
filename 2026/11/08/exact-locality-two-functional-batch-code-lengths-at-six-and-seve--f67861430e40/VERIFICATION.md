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

# Verifying the exact finite constructions

Use Python 3.10 or later, from the directory containing `verify.py` and `certificates/recovery_witnesses.json`:

```bash
python3 verify.py
```

The verifier reads the bundled certificate and checks the two literal rank-three generator-column multisets. It enumerates each multiset of size six (924 instances) and each multiset of size seven (1716 instances) over the seven nonzero binary length-three request types. For each encoded list of subset masks it checks: exactly one subset per requested type; masks nonempty and within column range; popcount one or two; pairwise disjointness; and bitwise XOR of selected columns equal to the requested vector. The lists are tied to a deterministic lexicographic combination-with-replacement enumeration, not to data obtained from an external source.

It also exhaustively enumerates all weak seven-part integer compositions of 11 (12,376 cases) and 12 (18,564 cases) to cross-check their minimum multiplicity discrepancy, and confirms the exact strict bounds on aggregate equal-request capacity. The proof in `RESULT.md` separately establishes the discrepancy minimization for all seven-component integer multiplicities and the validity of the capacity identity, so the lower-bound argument does not depend solely on an observed finite sample.

Expected last line: `ALL_CERTIFICATES_OK`. The run requires only the standard Python library and no network. The output verifies mathematical conditions for the exact two instances; it is neither an independent third-party audit nor evidence about uninspected publications.
