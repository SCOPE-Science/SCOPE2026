---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

The directed-arc four-slot face predicate excludes repeated leaf port conflicts, directed 2-cycles and the lone possible directed 4-cycle. Independent enumeration of all size<=4 arc subsets for n=6,7 gives exactly (1,4n,6n²-4n,4n(n-1)²,n(n-1)²(n-2)), and the alternating count yields the stated quartic. The assigned source specifies an acyclic sequential-toggle matching, a bounded fresh-tail/pivot induction for n>=20, and a finite exhaustive certificate for widths 6..19 (verify_k2n.py inspected from the pinned Git blob); these distinguish finite verification from the infinite induction. Furthermore, complete published pre-existing independent mathematical proofs establish the identical all-n wedge homotopy theorem by two different Morse/finite-locality arguments, corroborating the final correctness independently of any finite extrapolation. The universal theorem is mathematically correct.

## originality

FAIL

Decisive prior coverage: an October 18, 2026 publication proves the same bidirected K_{2,n} multipath wedge polynomial for all n>=7; two November 1, 2026 publications already prove exactly the same theorem for every n>=6, one additionally supplying the sharp n=2..5 homological cutoff and the other the n=5 Moore-space transition. All three full primary RESULT.md files were read, and their graph definition, directed-cycle exclusions, quantifiers, homotopy category, coefficient ring and polynomial agree with the assigned final claim. A fresh matching proof, numbers 169/491/1105, and acknowledgment of only n=6 do not create an original theorem. O FAIL because the result is a direct subset of previously published assertions.

## value

FAIL

The entire named mathematical output—sharp stable starting width n=6, exact homotopy type, quartic rank and integral homology—is already available in the complete prior K_{2,n} classifications. The alternate four-type matching can be a valid proof technique, but no distinct motivated lemma/generalization or new invariant is asserted as the final claim. As submitted this is a known-table/theorem recomputation, not an independent valuable scientific gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
