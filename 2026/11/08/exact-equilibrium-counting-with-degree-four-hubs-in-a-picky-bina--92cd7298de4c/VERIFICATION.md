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

For simple graphs of maximum degree 4, the homogeneous deterministic rule s_v=1 iff neighbor count q_v equals 0 or 2 agrees with (I+A)s=1 over F2 for degrees at most 3, but differs precisely when degree4 and q_v=4, which demands s_v=0. Partition D into exact exceptional vertices B and IE exclusions J for q_v=4 at D\B: for fixed B,J the pinned affine equation (I+A)s=1+1_B and neighbor pins has 0 or 2^(n-rank) solutions. Thus E(G)=sum_B sum_{J⊂D\B}(-1)^|J|L(B,J) with 3^|D| Gaussian eliminations. If D empty, symmetry z^TMz=sum z mod2 proves 1 in im M. The 8-edge 6-vertex example is an obstruction; no smaller graph can be one because maxdeg<=3 parity existence or a universal vertex. Independent direct-payoff comparison with the inclusion-exclusion formula matched 420 random degree<=4 graphs on 3..8 vertices plus the specific six-vertex zero-equilibrium example.

## originality

PASS

The six-vertex eight-edge obstruction and minimality are not new: October25 Resultary complete six-vertex census explicitly lists the identical 8 edges and proves all graphs on <=5 vertices have equilibria. The original 3-sun also predates this. The current main claim, however, is the general exact all-size 3^|D| pinned linear-system census for every maxdeg4 graph, not the known finite witness. Prior Resultary finite-six census, other fixed-family strip/crown results and the 2023 NP-hardness statement do not imply the general all-size degree-four parameterized count in the material inspected. Accept the substantive main census on best-of-knowledge grounds, explicitly excluding the auxiliary eight-edge witness from priority.

## value

PASS

Degree four is the first local degree where the odd-neighborhood parity identity fails under the specific 0-or-2 best response. An exact 3^k parameterized correction for k degree-four vertices is a natural structural/algorithmic invariant on arbitrary graphs, useful independently of the already known six-vertex obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
