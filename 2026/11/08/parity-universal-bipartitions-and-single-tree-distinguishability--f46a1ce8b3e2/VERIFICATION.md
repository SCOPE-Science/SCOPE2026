---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Tree bipartiteness and parity of every genuine edge traversal imply: a new vertex has the start color for an odd walk, and opposite color for an even walk. With uniform start, A-size increments with a/n or (n-a)/n irrespective of adaptive walk transitions. Initial a_2=1 yields discrete uniform via Pólya induction for odd, Eulerian insertion recursion for even. For even, D_n=2a_n-n has E[D_n²]=n/3 for n>=3. Event |D_n|<=n^(3/4), invariant under unlabelled unrooted isomorphisms, has even failure <=1/(3sqrt n) and odd acceptance <= (n^(3/4)+1)/(n-1), proving the stated TV lower bound tending 1.

## originality

PASS

The urn marginals themselves are classical and are credited. Neither the inspected full Random Friend Trees paper nor Anomalous scaling in redirection networks states the walk-rule-independent graph bipartition projection or uniform unlabelled-law separation. Resultary searches returned no earlier published exact parity-universality theorem beyond the assigned work. The unrestricted adaptive edge-following model is essential.

## value

PASS

Bipartition size is a natural isomorphism invariant of a random growing tree. An exact all-n distribution and a one-observation parity test applicable uniformly to arbitrary history-adaptive odd/even walk rules provide a structurally motivated classification despite the urn algebra itself being elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
