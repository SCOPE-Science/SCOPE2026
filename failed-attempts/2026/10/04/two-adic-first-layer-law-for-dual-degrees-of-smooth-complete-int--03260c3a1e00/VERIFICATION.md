---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The arithmetic is correct. The classical dual-degree formula is \(D h_n(d_1-1,\ldots,d_c-1)\). If exactly \(e>0\) defining degrees are even, reduction modulo two leaves the coefficient of \((1-t)^{-e}\), namely \(\binom{n+e-1}{n}\), whose oddness is exactly the no-carry condition \(n\mathbin{\&}(e-1)=0\). If all defining degrees are odd, each shifted degree contributes a factor two and the same argument after extracting \(2^n\) uses the number of degrees congruent to three modulo four. The advertised mod-four boundary follows. Fresh exact checks reproduced the package examples \(306\) and \(108\); the finite verifier is corroborative only.

## originality

FAIL

Originality fails under the required implication standard. Kleiman's published conormal/Segre theorem already gives the exact dual degree of every smooth nonlinear complete intersection as the defining-degree product times the complete homogeneous symmetric polynomial in the shifted degrees. Reducing that known exact formula modulo two and applying the standard Lucas/Kummer no-carry criterion mechanically yields the stated first 2-adic layer, including the all-odd case after extracting the common factor of two from every shifted degree. The mod-four corollary is then an immediate specialization. The statement is a neat arithmetic repackaging, but the full final claim is logically covered by a published exact formula plus a classical textbook parity theorem.

## value

FAIL

The dyadic boundary is a natural way to summarize the classical degree formula, but its proof is only a routine modulo-two reduction followed by Lucas/Kummer parity. Under the required value standard, this is a textbook-level arithmetic corollary of an already exact invariant formula rather than a distinct structural gap that needs the precise new fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
