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

# Exact arithmetic verification

All packaged files are self-contained and readable as UTF-8. Run both programs in the same directory as `certificates.json`:

```text
python3 verify.py
python3 verify_independent.py
```

The programs use only the Python standard library, not an optimizer, internet access, external libraries, or saved outputs. `verify.py` recursively generates each Dyck language and checks all deletion shadows. `verify_independent.py` enumerates balanced bit masks through combinations of up-step positions and independently deletes bits using integer shifts. Both check every listed codeword, every nonnegative primal/dual certificate entry, every shadow-packing inequality, and exact rational objective equalities for semilengths one through six.

Observed terminal markers: `EXACT_DYCK_CERTIFICATES_OK` and `INDEPENDENT_DYCK_OK`. For lengths two through twelve, both reconstruct input sizes \((1,2,5,14,42,132)\), distinct output counts \((2,4,10,28,84,264)\), code sizes \((1,1,2,4,9,24)\), and rational LP totals \((1,1,2,4,29/3,3269/131)\).

Every feasibility statement concerns a complete finite source layer. No external or infinite proof-checking is claimed; independent expert audit is not performed. Equality of the primal/dual rational objectives gives exact LP optimality and integer floor bounds, while disjoint deletion shadows give the attaining zero-error codebooks. Reconstructing the records from complete words makes this verification independent of how the certificates were originally found.
