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

# Exact verification

Run `python3 verify_cycle12_quotient.py c12_reduction_certificate.json` beside the supplied JSON certificate. Python's standard library suffices. The executable enumerates the 321 nonempty independent faces and 38,347 strict chains, obtains 3,203 orbit cells and the vector \((30,291,912,1190,660,120)\), independently recomputes the Burnside counts for each cell dimension, checks all integral boundary compositions, and replays 1,242 free-face and 359 integral unit-pivot deletions. The residual chain complex has one degree-zero cell. The recorded successful invocation is supplied as `cycle12_verification_output.txt`.

Each free-face deletion is accepted only if the face has a unique immediate coface *and* that coface is maximal. Each algebraic elimination requires a signed incidence of magnitude one and performs the exact integral Schur-complement update; hence it preserves integral homology rather than merely rational ranks. These checks are complete for the specific combinatorial complex and rotation action. The checker also verifies the two stabilizer-bearing independent faces, but the external standard theorems (cycle homotopy, Armstrong, Hurewicz, Whitehead) are separately required for the homotopy conclusion. Numerical output is not an independent audit or an extension to other cycle sizes.
