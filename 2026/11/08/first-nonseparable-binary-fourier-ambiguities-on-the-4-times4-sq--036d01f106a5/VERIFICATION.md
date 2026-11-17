---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: For a full-support sign array a on n-by-n square, |P_a(z,w)|² on the complete torus is a finite Laurent polynomial with coefficients the aperiodic autocorrelations C_a(r,s); equality of intensities is equivalent to coefficient equality. Global sign fixes upper-left entry +1; simultaneous central reversal produces the other trivial equivalence, with no other signs/translations permitted. Independently enumerated all 2^(n²-1) normalized codes at each n=1,2,3,4, computed all nonredundant shifts as exact integer inner products, grouped complete correlation fibers modulo reversal, and tested each rank-one/tensor status. Fiber size histograms are n1 (1 single), n2 (6 singles), n3 (134 singles,1 double), n4 (16488 singles,12 doubles); exactly eight of the 12 n4 doubles are entirely nonseparable; n3 none. The explicit codes 12442 and 3238 are an inequivalent nonseparable equal-correlation witness. This is a complete finite exhaustive certificate for n<=4, not an inference about larger squares.

## originality

PASS

PASS (qualified): Novikov–Xu 2026 full primary Theorems 1–2 prove broad multidimensional Pauli/phase-retrieval nonuniqueness through difference-operator constructions, including non-tensor instances, but neither specifies full-support all-sign 4-by-4 masks, the *first* nonseparable side, nor complete finite autocorrelation fiber multiplicities. October 11 2026 published Resultary full theorem instead classifies fourth-moment MINIMIZERS at 4x4 (32 masks in two orbits, scalar minimum 304). This does not imply full vector-intensity fiber counts; the submitted nonseparable witness has scalar moment 400 and is not a minimizer. No complete binary 4x4 homometry table was found; older specialist tables are a material remaining risk.

## value

PASS

PASS: Nonuniqueness in discrete binary Fourier phase retrieval is a natural inverse-imaging obstruction; distinguishing separable/tensor artifacts from genuinely two-dimensional ambiguities at the first possible full-square size and cataloguing every fiber is a motivated complete finite classification. The 4x4 count and witness make an exact benchmark; no inflated claim about arbitrary arrays or complex phases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
