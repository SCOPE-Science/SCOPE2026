---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A truncated vertex uses either one or three external matching edges; given the external choices the internal matching is forced. The two parity equations at each prism column imply b_i=a_i XOR d with one global bit d and c_i=1 XOR a_(i-1) XOR a_i. Conversely every a and d reconstructs a covering, so there are 2^(n+1). Along a truncated face, the original external edges occupy every other polygon edge and must have equal selection to alternate; odd parity then forces the local internal pattern. On a side octagon this reduces to d=0 and both neighbors of a_i equal to 1; the flip toggles just a_i. The end faces are available precisely for constant a and form a four-cycle whose intersection with the Lucas cube is the all-one d=0 word (the empty independent set). In d=0 the non-isolated zero set is invariant under square flips. At a fixed core B, its closed-neighborhood boundary must be ones, and the remaining zeros form exactly an independent subset outside that neighborhood. The allowed toggles connect every such choice by way of the empty subset. The nonconstant d=1 words have no moves. This proves exhaustion, giving K_n=1+(b_n-2)+(2^n-2). The closed-walk matrix for forbidding 010 has characteristic polynomial x(x^3-2x^2+x-1); its traces yield 5,10,17 and the stated recurrence. No-square-flip words in d=0 are independent sets in the graph of cyclic index offsets +/-2: one n-cycle for odd n, two cycles for even n, with two single edges for n=4. This includes n=3 (offsets modulo three), and excludes the all-zero end-flippable word from the frozen count. At n=4 the Lucas cube is two squares wedged at the empty set; the cap square gives a third, with 10 states in that component, 22 isolated states, and 23 components total. The Hamiltonian is t times the flip-graph Laplacian plus (v-t) times the degree diagonal: component constants give its RK kernel, positive diagonal shifts leave just the frozen states at v>t, and a constant test vector on any nontrivial component gives negative energy for v<t. Counting disjoint forbidden triples bounds b_n/2^n by (7/8)^floor(n/3), and the Lucas corrections are o(2^n), giving both limiting fractions. These are finite face-only statements for precisely the given Hamiltonian. Both checker files and their reported finite verifications were inspected, not executed.

## originality

PASS

The distinct contribution is the all-n component classification and exact frozen and sector counts for the truncated prism with side and end face flips. The odd-degree encoding at the cube, Lucas-cube combinatorics, and Laplacian principle are credited inputs, not fresh claims. Similar reconfiguration work does not furnish the needed move rules and sector decomposition for this graph.

## value

PASS

The family has a natural planar geometry and a fixed physical move set. Resolving its entire configuration-space connectivity identifies exactly which locally mobile matchings can reach one another, all zero-mode multiplicities at and above the RK point, and the nonvanishing frozen fraction in growing prisms. The n=4 specialization is an informative exact check on an ordinary truncated polyhedron, not an arbitrary isolated count or a claim about thermodynamic phases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
