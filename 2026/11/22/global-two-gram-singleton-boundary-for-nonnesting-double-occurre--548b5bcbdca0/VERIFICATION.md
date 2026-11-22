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

# Reproducible checks

Run `python3 check.py` from this directory. It enumerates all nonnesting labeled double-occurrence words for \(1\le n\le6\), independently computes every global two-gram inverse-fiber size using directed spanning-arborescence counts and the BEST trail formula, and confirms the mountain criterion and exact singleton counts. It also compares the formula directly against exhaustive unrestricted source-word enumeration for \(1\le n\le5\).

Run `python3 check_switch.py` from this directory. It enumerates every canonical Dyck-matching word for \(1\le n\le9\), searches for an explicit spectrum-preserving switch in each nonmountain case, and checks both its letter counts and ordered adjacent-pair counts. Both scripts passed locally.

The scripts are finite consistency checks, not an infinite proof or independent audit. The proof of all \(n\) is in `RESULT.md`. The reconstruction notion is restricted to indexed linear words and oriented, multiplicity-preserving factors of lengths one and two.
