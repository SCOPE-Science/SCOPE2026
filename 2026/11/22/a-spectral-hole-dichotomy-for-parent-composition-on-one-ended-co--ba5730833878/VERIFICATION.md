---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Summing prescribed increments along finite root paths gives the inverse of the isometric increment map on the full Lipschitz space. The scalar root summand always has Fredholm index zero, including at λ=1. Bounded tooth lengths make the tooth block uniformly nilpotent, so bounded block elimination reduces the nonzero pencil to the spine pencil. The latter is injective and bounded below for 0<|λ|<1, and its range is precisely the kernel of the nonzero absolutely summable telescoping functional; the bounded backwards-tail solution gives the converse, hence index −1. At |λ|=1 its phase-corrected ramps have defect 1/m and it is injective, so the range is not closed. For unbounded teeth the corresponding supported unit vectors have defect |λ|^m inside and 1/m on the circle; injectivity of the nonzero increment pencil follows successively on the spine and each finite tooth. At zero the infinitely many terminal coordinates give an infinite kernel. The exterior Neumann argument and the spine obstruction give the full ordinary disk. RESULT.md line 38 should say that the tooth block has norm at most one: it is zero if all lengths equal one. No step uses the asserted equality; the stated theorem and estimates hold in that case too. The packaged rational checker was inspected, not executed, and is not needed for the infinite-dimensional proof.

## originality

PASS

The ordinary disk and the zero-parameter obstruction are not new. The strongest previous Fredholm-pencil theorem concerns leafless trees; the terminal-tooth length transition, isolated essential zero, and nonclosed-range regime here are distinct. The ordinary and essential spectral conventions have been separated.

## value

PASS

Identical ordinary spectra, one end, and a uniform degree bound do not determine Fredholm essential geometry. The exact length criterion separates a disconnected essential set and finite-defect punctured disk from a filled essential disk due to nonclosed range. This is a useful structural witness on a canonical family, not a claim of new shift or nilpotent-block lemmas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
