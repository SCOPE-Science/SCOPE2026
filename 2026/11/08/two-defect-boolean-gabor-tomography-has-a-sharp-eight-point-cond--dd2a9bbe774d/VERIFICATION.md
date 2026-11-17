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

For a=0,d,otherwise, Walsh character orthogonality produces the stated 11 spectral rows and positive multiplicities summing N^2. Four nonexceptional rows enforce least ambiguity <=2r for r=min(|U|,|V|,|P|,|Q|), with H=N+2U+(U²+V²+P²+Q²)/2. Minimization in two ranges r<=2 and r>=2 yields kappa>=sqrt(2N)-1 for N>=8, equality only r=sqrt(N/2), U=-r, other three signed r. Solving linear equations yields exactly eight optimizers; direct substitution gives rank and finite condition. Independent exact integer-Gaussian ambiguity enumerations at N=8 and 16 matched all 11 rows and multiplicities in six sample parameter cases. General proof rests on Weyl diagonalization, not finite tests.

## originality

PASS

The one-site real-plus-imaginary optimal spike and condition sqrt(2N)-1 already occur in Zhu–Wang 2026 and are explicitly credited. New survival: global two-parameter (two arbitrary complex-site defects) lower bound, all eight equality configurations including four separated-site optima, and complete eleven-row rank/spectrum for all parameters. Earlier two-hole cyclic Z_N rank theorem is different group structure and missing-site case; it does not imply Boolean two-site conditioning. Full Zhu-Wang text inaccessible, materially qualifies priority of exact optimized family.

## value

PASS

Determining whether a second defect can improve a known measurement design is a natural minimax stability question. The exact all-parameter rank discriminant and extra full-rank separated optimizers distinguish complete tomography from isolated real/imag perturbations and are potentially useful as explicit sensing designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
