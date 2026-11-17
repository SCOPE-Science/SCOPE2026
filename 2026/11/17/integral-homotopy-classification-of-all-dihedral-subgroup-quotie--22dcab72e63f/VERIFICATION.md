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

# Verification scope

Run `python3 verify.py` in the same directory as `verification_output.json` and compare the exact JSON bytes written to standard output with the recorded output file. The script uses only the Python standard library. It enumerates the full closed-cell configuration complex for the pentagonal wheel, all chains in its face poset, the ordinary quotient flag orbits under each representative subgroup, and every simplex boundary. Its Burnside fixed-chain count is independent of the canonical representative count. All free-face deletions are recorded, and the remaining connected one-dimensional complex has the asserted first Betti number.

The output includes the ordered lists of elementary collapse pairs, not only final counts. No probabilistic checks, finite-range extrapolations or infinite classification are involved. This checks the packaged finite claim; it is not a formal proof assistant or an independent external validation.
