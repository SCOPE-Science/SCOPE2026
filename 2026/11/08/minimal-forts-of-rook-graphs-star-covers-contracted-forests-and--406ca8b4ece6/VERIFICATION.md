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

# Verification

Run the standalone standard-library-only verifier with `python3 verify.py`.

The verifier uses exact integer neighborhood bitmasks for each labeled rook graph, enumerates every nonempty vertex subset, and decides the fort condition directly. It independently uses an upward subset dynamic program to determine whether any proper subset is a fort, rather than assuming single-deletion minimality. The second algorithm expands rational labeled exponential generating functions using Cayley's tree count and alternating-cycle components.

The compared boards are \((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4)\). Actual successful output:

```
VERIFY_OK boards=13 examined_subsets=129155 forts=90253 minimal_forts=2165 coefficientwise=PASS thin_family_n5..20=PASS
```

The two-row formula is additionally checked against exact component enumeration for each integer \(5\le n\le20\). These finite checks do not establish the unrestricted theorem; the proof in `RESULT.md` supplies that step. No independent audit has been performed.
