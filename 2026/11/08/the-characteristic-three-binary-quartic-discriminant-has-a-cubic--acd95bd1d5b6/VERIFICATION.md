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
# Verification record
The proof is symbolic and valid over every field of characteristic \(3\). The local discriminant and ideal-intersection identities were independently replayed using `python verify.py`, requiring SymPy, and the exact output is included in `verify-output.txt`.

The script checks: the integer discriminant followed by modular reduction; the depressed normal form; the full Tjurina ideal (including the defining equation); equality with the computed intersection via two exact ideal containments; parametrized triple-root and square-quadratic loci; and the rank-three Veronese projection center. The generic multiplicity \(6\) and cycle degree \(16\) follow from the algebraic proof. A finite computation of chart ideals is not in itself a verification of global gluing; the \(\mathrm{GL}_2\)-invariant cover and faithfully flat descent are established in the proof.

Independent audit has not been performed. Mathematical priority beyond the inspected references remains open to further specialist review.
