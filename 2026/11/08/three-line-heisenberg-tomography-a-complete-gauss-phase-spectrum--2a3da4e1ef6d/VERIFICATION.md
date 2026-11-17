---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Used regular decomposition into p² scalar characters and p−1 degree-p Schrödinger irreps, each p times. For three distinct directions each subgroup average is rank-one projection in a degree-p irrep, pair squared overlap 1/p by group trace orthogonality; triple trace is p^-2 sum_t exp(2πiτ(At²+Bt)/p). Gram cubic (λ−1)^3−3(λ−1)/p−2 Re(qτ)=0 gives every block; p>=5 Gershgorin lower bound 1−2/sqrt(p)>0, and p3 direct Gauss-phase values yield 0,1,2 at B0 versus positive roots for B!=0. Character census 3(p−1) ones, rest zeros; 4 direction choices×27 lift choices gives exactly 36/72. Independently built regular convolution matrices and checked ranks p3 B=0/1 19/25, p5 B=0/1 73. The infinite claim relies on representation argument, not these tests.

## originality

PASS

Passed with explicit restriction: general finite-group Radon Fourier framework and Heisenberg MUB overlaps are classical. Ilmavirta full-geometry Radon transform and Blanchfield dependent MUB vectors do not give the selected three-subgroup regular-operator spectrum and exact central-lift rank census in inspected statements. An older triple-stabilizer Gram theorem could subsume cubic, retained as risk.

## value

PASS

Exact spectral tomography/stability and precise exceptional p=3 rank-jump census for an important finite noncommutative group, an objectively motivated incomplete-view inverse problem. The 36/72 count and cubic phase link are meaningful beyond restating standard pairwise MUB overlaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
