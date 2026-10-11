---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The channel calculation is correct. The primary weak-measurement definition has \(\zeta=\operatorname{sech}\epsilon\) and stabilizer measurements commute. On a stabilizer-character sector, one elementary nonselective measurement acts as identity when the character is even and multiplies by \(\zeta\) when it is odd; composing a schedule therefore multiplies these factors to \(\zeta^{\operatorname{wt}(u^{\mathsf T}G)}\). Full row rank makes \(u\mapsto u^{\mathsf T}G\) injective, so the largest residual eigenvalue on nontrivial orthogonal sectors is \(\zeta^{d(C_G)}\); deficient rank leaves a nonzero left-kernel sector fixed. The finite checker independently confirms both endpoint spectra and the stated \(r=3\) schedules.

## originality

FAIL

The final claim is a routine implication of the published weak-measurement channel plus standard binary-code terminology. Dominy et al. explicitly define the same commuting products for the full stabilizer group and for a generating set, and their single-observable channel already separates commuting from anticommuting character sectors by the factor \(\zeta\). For an arbitrary list, multiplying those diagonal factors yields Hamming weight immediately; calling the image of \(u\mapsto u^{\mathsf T}G\) a linear code makes the minimum-distance optimization definitional. Under the required implication-based originality bar, absence of the exact code-distance wording does not make this independent work.

## value

FAIL

The coding interpretation is potentially useful engineering language, but as a mathematical finding it is a routine multiplication of published diagonal channel factors followed by the definition of binary minimum distance. The endpoint interpolation and \([4,3,2]\) example do not add a motivated non-implied structural fact under the stated value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
