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

Run `python3 verify_matching.py` using Python 3's standard library. Verified outcome from the supplied checker:

`VERIFY_OK sizes=1..10 words=23713 quadratic=OK collision=OK extrema=OK`

The checker exhaustively reconstructs the literal matched-pair deletion sets of every Dyck source through semilength ten; parses the plane-tree statistic independently and compares all coefficient polynomials to those derived recursively from the displayed quadratic. The independent analytical proof in `RESULT.md` handles all lengths. Nothing here independently verifies novelty or establishes bounds for arbitrary nonmatching deletions.
