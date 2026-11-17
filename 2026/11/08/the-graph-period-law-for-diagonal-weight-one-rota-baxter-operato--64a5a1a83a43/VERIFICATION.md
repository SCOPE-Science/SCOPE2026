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

Substitution into the bilinear Rota–Baxter identity yields r_i²=(2r_i+1)r_j on each nonzero edge; strong connectivity propagates zero support. On full support u_i=1+1/r_i conjugates the edge map to u_j=u_i². Closed-walk cycle-length gcd d yields u^(2^d-1)=1, and path-length congruence constructs all well-defined operators without dividing by two, even in characteristic two. Constant u=0 gives -id; the finite-field count uses cyclic F_q^×. Independent direct F7 edge-equation sweeps match 3-cycle, reverse-edge and period-two branching cases.

## originality

PASS

The published Nov2 all-field scheme theorem covers directed single cycles and is properly credited; it does not force a common parameter in a nonmonomial branching strongly connected digraph with multiple different cycle lengths, and hence cannot by itself establish the all-graphs gcd-period law. Qaralleh et al. study nilpotent maximal-nilindex chains, not strongly connected graphs. Historical coverage remains provisional.

## value

PASS

The arithmetic graph-period invariant gives exact operator counts under arbitrary branching and nonzero structure coefficients; a single added reverse edge can collapse the whole family, and perfect nonmonomial examples show this is not merely a cyclic renaming. This is a motivated structural extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
