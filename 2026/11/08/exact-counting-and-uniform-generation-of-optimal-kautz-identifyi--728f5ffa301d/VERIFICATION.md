---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For K(2,n) arc-vertices of D=K(2,n-1), the two outgoing arcs at each D vertex have equal incoming predecessor sets, so any identifying code contains at least one of the two, giving >=3*2^{n-2}. Equality forces exactly one selected outgoing and (by nonempty signatures) exactly one selected incoming at each lower-order vertex, a cycle cover. Signatures of omitted arcs are distinct singletons; signatures of selected arcs are pairs, with collisions exactly at selected digons. In D=L(H), independent two-way local switches at H vertices enumerate all cycle covers. Exactly three alternating digons forbid one local two-switch pattern each, disjoint for n>=4 (giving 3^3*2^{3*2^{n-3}-6}), while n=3 admits only <=1 backtracking switch and n=2 the two Hamiltonian triangles. Uniform independent local sampling follows from this bijection. Independent literal-code enumeration confirmed 2,4,27 optimum codes at n=2,3,4. Finite tests are not proof for all n.

## originality

PASS

The relevant primary 2020 line-digraph identifying-code article Theorem 3.12 proves minimum cardinality 3*2^{n-2}; its Theorem 3.4 and 1-factor construction provide structural background, but the inspected primary text does not enumerate all minimum labeled codes or provide the digon-exclusion closed formula and uniform sampler. Same-family other Resultary records concern radius-two identification, not this radius-one optimum enumeration. Counting all sharp codes is distinct from having a construction or minimum size.

## value

PASS

Identifying codes are a canonical network location/sensor invariant. Exact number and uniform generation of all optimal labeled Kautz codes supplies a nontrivial combinatorial classification of degeneracy and unbiased sampling at every length, using a natural degree-two line-digraph structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
