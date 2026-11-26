---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With nonempty A, the quantity t+(1−e)+(1−f) counts T augmented by ∅ and A. It is 2 on the singleton; an empty-parameter factor changes neither the augmented family nor m. For both factors nonempty in parameters, a union can duplicate only ∅ and necessarily misses A; the augmented count is t_1+t_2+2−e_1−e_2, at most the sum of the two child augmented counts. For a join the roles are swapped: only A can be duplicated, ∅ is absent, and the count is t_1+t_2+2−f_1−f_2. The resulting induction proves the bound for all finite cographs. Each leaf twin realizes its singleton; each internal apex realizes its descendant leaf set, all distinct by full binary branching; an isolate realizes ∅. There are exactly 2m external witnesses and m parameters, including the edge-plus-isolate case m=1. No host with fewer than 3m vertices can provide the 2m separate external witnesses. All-vertex adjacency traces are not all complete equality-sensitive quantifier-free types, a distinction correctly made in the stated scope. The uploaded finite checks were read, not run; the proof does not depend on them.

## originality

FAIL

The distinct same-day exact cograph spectra record proves the identical augmented bound and the stronger all-vertex spectrum, including an attaining host of order 2m. Its result also mechanically gives the external extremum and the 3m minimum via cograph false-twin extension. This is demonstrated coverage of the full frozen theorem, not a historical priority decision based on the date.

## value

FAIL

The exact trace spectrum is a useful structural invariant, but the frozen cap and augmented lemma recapitulate the stronger existing statement. The frozen external optimization adds no new extremal obstacle: duplicating the parameter leaves in a smallest all-vertex extremizer attains the unavoidable witness-count lower bound. The alternative laminar construction is a valid example, not a distinct classified trace structure or a new exact invariant beyond the mechanically implied result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
