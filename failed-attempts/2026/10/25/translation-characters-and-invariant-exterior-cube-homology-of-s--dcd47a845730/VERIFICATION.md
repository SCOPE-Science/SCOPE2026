---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every n>=3 the face condition is Hamming diameter at most 2. The cited Adamaszek–Adams wedge theorem supplies H_3 concentration. For a nonzero translation of weight 1 or 2, invariant faces are orbit-unions; their signed Lefschetz sum reduces to the Euler characteristic of a triangle-free n-1 cube graph on 2^(n-1) orbit vertices and (n-1)2^(n-2) edges. For weight >=3 no orbit lies in a simplex. Thus the stated traces, Walsh Fourier multiplicities, and dimension C(n,3) follow; distinguished even-parity tetrahedra support independent three-cube fundamental cycles, giving the exterior-cube S_n action on T-invariants. An independently authored face-enumeration/reduced Lefschetz check (not merely executing the repository verifier) confirmed all translation weights for n=3,4,5 (80,392,1776 simplices respectively), and n=4 traces 9 at identity, 5 for weights 1/2, 1 above. These finite checks are only corroboration of the uniform proof.

## originality

FAIL

DECISIVE PREEXISTING COVERAGE: Galetto–Montaño–Wellner, arXiv:2606.20784v1, posted 2026-06-18, Theorem 5.4 provides the COMPLETE H_3 representation of precisely the same scale-two hypercube Vietoris–Rips complex X^{n,2} for all n>=3 under the full hyperoctahedral group F_2^n ⋊ S_n. Restriction to its normal binary translation group immediately gives all Fourier constituent multiplicities, hence the full translation character. The weight-zero constituent of the previously published decomposition is precisely the stated exterior-cube permutation representation (Specht exterior-square and exterior-cube standard summands). Therefore the submitted conclusions are mathematical consequences of a stronger earlier theorem, not new discoveries. Citation to earlier nonequivariant topology alone omitted this directly stronger 2026 primary paper.

## value

FAIL

Translation characters and the invariant exterior-cube module are natural and interesting symmetry data, but for this precise same complex and every n>=3 they are already determined by the prior complete full-group decomposition. Restating/evaluating this covered specialization without any new mathematical distinction is known-result recomputation; its intrinsic mathematical motivation cannot make it an original valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
