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
# Verification and reproducibility

Execute `python3 verification/check_blowup.py` after extracting this package. The program uses only the Python standard library and constructs all seven expanded graphs directly from their base adjacencies and multiplicities. It checks that each base adjacency has full rank over the rationals; evaluates the predicted degree condition for each graph; verifies real diagonal isomorphism identities for each of the four positive cases; and, for six graphs of order at most six, exhaustively checks the left-multiplication rank formula on every nonzero \(\mathbb F_5\)-vector. This is \(38{,}244\) rank checks. The recorded output is in `verification/OUTPUT.txt`.

These finite computations do not prove the unrestricted statement or rule out arbitrary algebra isomorphisms in obstructed finite examples. The proof of that obstruction rests on the intrinsic rank-one-space argument and edge constraints in `RESULT.md`. The output reports the exact tests performed and makes no independent-certification claim.
