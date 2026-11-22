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

# Reproduction and boundaries

Run `python3 check_hex_bouquets.py` with a standard Python 3 interpreter. The checker exhaustively derives the 15 qualifying local subsets of the five-path, verifies the three local critical patterns, and checks each full-face matching and the absence of directed Hasse cycles in 16 finite cases: m=1..3 and k=2..6, plus m=4,k=4. It is independent computational corroboration; RESULT.md supplies the uniform proof for every m>=2,k>=4. The maximum checked poset contains 34,474 faces. No computer calculation claims to verify the infinite parameter range, an integral Smith form, or an independent mathematical audit.
