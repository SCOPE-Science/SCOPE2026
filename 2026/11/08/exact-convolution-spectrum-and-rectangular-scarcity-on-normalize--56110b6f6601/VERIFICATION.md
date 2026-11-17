---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Each rank-one matrix with total sum 1 has a unique factorization u v^T with sum u=sum v=1. Splitting those affine hyperplanes reduces each Fourier multiplier to a bilinear sum over d=m-1,e=n-1. Summation over x then y gives nonzero q^(d+e-r) times a pth-root phase precisely when ell in im B and h in im B^T; for rank r, each admissible linear term has q^r choices and scalar constant c has q choices. Thus multiplicity q^(2r+1)N_de(r), with phases equally distributed. The rank-deficit distribution derived from the exact matrix-rank product and dominated convergence gives the sequential rectangular limit, not a joint uniform estimate. Independent full character enumeration at q=2 and dimensions 2x2,2x3,3x2,3x3 agrees including zeros. The proof (not enumeration) covers all finite fields.

## originality

PASS

Delsarte rank-metric association-scheme spectra classify GL-invariant unrestricted rank orbits; the affine hyperplane-normalized Segre patch is not such an orbit, and its bilinear Fourier transform yields separate row and column solvability conditions. Similar affine-Veronese and self-Fourier rank-one cone findings use symmetric matrices or different operators. No direct complete rank-stratified spectrum and rectangular scarcity formula was identified in the compared sources, subject to uninspected general bilinear-exponential-sum literature.

## value

PASS

The convolution operator is a canonical harmonic-analysis object on an affine rank-one slice. Its complete kernel dimension, sharp positive conditioning, and sparse Fourier-support asymptotics characterize exactly what frequencies survive under increasingly rectangular sampling. That is mathematical structure beyond a small finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
