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

The proof is elementary and all-length; the finite checker is a separate corroboration, not a replacement for the proof.

Run `python3 verify.py` from this directory (Python standard library only). It exhaustively enumerates indexed input/output tables for \(3\le n\le18\), confirms the parity-language characterization of every multiple-predecessor output, and checks an independently constructed inverse algorithm against all \(2^n\) outputs for \(3\le n\le11\). It also checks the exact Lucas-weighted population identities through \(n=300\).

Scientific boundaries: there is no claim of arbitrary-noise correction, iterated dynamics, or a formula for outputs with no predecessors. No formal proof assistant or independent mathematical audit has been used.
