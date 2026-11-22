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

# Verification and proof boundaries

The full theorem follows from the unrestricted endomorphism normal form, the composition-idempotence equation, splitting an idempotent additive operator into image and kernel, and a double count of prescribed images. Both endpoint cases \(r=0\) (constants) and \(r=f\) (identity) are included. Finite enumeration is a check, not the proof of an infinite family.

Run `python3 verify.py` from the directory containing the distributed files. This standard-library-only program directly computes the operation table, independently evaluates the preservation identity for each candidate, tests \(F^2=F\), and compares distinct embedded-image sets against the image polynomial. It exhaustively checks all 256 set maps for the four-element quandle and independently enumerates 16, 243 and 16,384 parameterized homomorphisms at \((p,f)=(2,1),(3,1),(2,2)\). The final output line is `UNIPOTENT_RETRACTION_CENSUS_VERIFIED`.

This review does not independently validate published-source priority; the same-Q all-subquandle census and semisimple retraction theorem are credited. No independently performed audit is reported.
