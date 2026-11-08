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

# Computational verification

Run `python3 artifacts/verify.py` alongside `artifacts/orbit_certificate.tsv` using Python 3 without third-party packages. The script enumerates all 192 undirected maximal antipodal geodesics; the 384 automorphisms; all 4,368 five-vertex and 8,008 six-vertex subsets; and all 50 symmetry orbits with 48 exclusion witnesses. It checks both proposed families constructively and verifies that they coincide exactly with all accepted subsets.

A complete run returned:

```
TWO_CONSTRUCTIVE_FAMILIES_OK sphere8=8 prism32=32
NO_FIVE_VERTEX_TRANSVERSALS_OK tested=4368
ALL_SIX_VERTEX_SETS_EXHAUSTED_OK tested=8008 hits=40
FIFTY_AUTOMORPHISM_ORBIT_CERTIFICATE_OK all=8008 accepted_orbits=8,32 rejected=48
VERIFY_OK
```

The certificate is a complete finite proof only for \(Q_4\). No computational extrapolation, external proof certification or independent mathematical audit is claimed. Review status is confined to the self-review recorded in `REVIEW.md` and `AUDIT.json`.
