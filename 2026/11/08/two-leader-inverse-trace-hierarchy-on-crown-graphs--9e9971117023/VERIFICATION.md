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

The mathematical identity is established by the singular-value decompositions and positive rational comparison gaps given in `RESULT.md`.

To reproduce a separate finite check, run `python -S verify.py` with Python 3. The script requires only standard-library modules and constructs crown graph adjacency and grounded matrices from scratch, using exact rational Gauss–Jordan inversion. Its checks comprise all \(\binom{2m}{2}\) distinct two-leader subsets for \(m=3,\ldots,8\) (365 pairs), one representative of each class for \(m=9,10,12\) (9 pairs), and exact identities for the two pairwise objective gaps for \(m=3,\ldots,150\) (148 parameter values).

Expected output:
`PASS exhaustive_2sets 365 representative_larger 9 exact_gap_identities 148 m_range 3..8`

Successful execution of the finite verifier does not certify the general theorem independently; the general proof is symbolic and covers every \(m\ge4\). No unperformed external audit or verification is claimed to have occurred.
