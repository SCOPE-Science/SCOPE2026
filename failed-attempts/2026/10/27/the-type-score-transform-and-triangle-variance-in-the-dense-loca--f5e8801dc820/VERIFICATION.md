---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The theorem is correct for the named finite nonempty parameter set. The frozen argument's inference from some circle representation of each extension to gaps in one fixed drawing needs justification. Fix p in P. Move the original in-neighbors of p to their antipodes. This reverses exactly edges across the switched subset, leaving a forward semicircle whose transitive order is uniquely determined by the named tournament after switching, with p first. In any extension draw the enlarged tournament, repeat this operation and switch the new vertex iff it beats p. The result puts it in one of the n positions after p in the same fixed transitive order. Conversely insert into the chosen position in the normalized fixed drawing and undo the switches. The position and switch bit are recovered from the extended orientation, giving exactly 2n extensions and showing no missing diagrams. Homogeneity and the finite relational language turn the realized diagrams into complete types over P; each such diagram has arbitrarily many realizations by adding distinct nearby points in its gap and embedding over P. Clockwise degree drops at v from s(v)+1 to s(v), and rises at its antipode from n-s(v)-1 to n-s(v); balance of level crossings gives reciprocity. Reading post-crossing scores gives E=S+z^n S(1/z)=(1+z)S. The uniform type score is thus a uniform vertex score plus an independent fair Bernoulli. Each transitive triple has one source, giving the raw second moment from sum_v binom(s(v),2)=binom(n,3)-c_3; subtracting the squared mean and adding 1/4 yields the stated variance. Its maximum occurs exactly at zero cyclic triples (transitive). Integrality gives the stated minima and equality profiles. Take a regular odd carousel (including n=1), or delete one vertex from the regular carousel on n+1 for even n; exactly n/2 other vertices lose one of their n/2 wins and the remaining n/2 keep all their wins. The frozen finite checks were inspected as recorded, not independently replayed; the proof above is all-order. The case n=0 is excluded.

## originality

FAIL

The central transform and gap classification are explicitly covered in the closest indexed result. The variance and its equality profiles, though not printed there, follow mechanically from that polynomial equality, the elementary source count for triples, and the integer score bounds. There is no independently new theorem left at the stated scope.

## value

FAIL

The degree distribution is a meaningful invariant, but the earlier transform already computes it exactly. Its second moment is just the standard count of noncyclic triples plus the Bernoulli term, and the optimizing profiles follow from mean/integrality or absence of a directed triangle. No new cutoff, example, or optimization phenomenon beyond those deductions is established here. There is no substantive surviving repair in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
