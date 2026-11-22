---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For the ordinary complete six-vertex directed-forest matching complex with one outgoing arrow per source, simultaneously swapping three vertex pairs yields 15 two-arrow orbits, 12 admissible orbit vertices, and 36 two-orbit compatible edges, with no three-orbit face because every 3-source functional quotient contains a cycle. The resulting connected graph has rank 36-12+1=25. The residual centralizer action (S3 permuting pairs and binary flips modulo diagonal) is AGL(2,2)=S4 and acts simplicially. For each conjugacy class, the signed edge trace identity tr(H1)=1-tr(C0)+tr(C1) gives (25,-1,-3,1,1); pairing with the rational S4 character table yields (1,1,3,4,1), dimension25, with one invariant rational line. Independently enumerated all 30 directed arcs and 15 orbits, all 66 candidate pairs, all 24 group elements and their signed cellular traces, reproducing all five class sizes/values. Inspected complete 5852-byte verify_s4.py, which additionally checks connected spanning tree and direct integral cycle-basis traces. The finite enumeration exhausts this one finite graph and does not assert a general formula.

## originality

PASS

The known 25-circle bouquet and orbit enumeration are excluded from the new contribution. The mathematically extra invariant is the full signed centralizer S4 character and its quotient-invariant line; a nonequivariant homotopy equivalence does not determine this representation. Two highly relevant published full RESULTs explicitly classify only geometric fixed-space topology, leaving centralizer action uncomputed. Best-of-knowledge, no covering S4 module has been found, subject to an equivariant matrix–forest priority risk.

## value

PASS

The residual centralizer action is an intrinsic invariant of a natural fixed-point complex: two graph actions with the same 25-circle topology can have different characters. Its full five-class decomposition, sign-sensitive double-transposition trace −3 and one invariant quotient class give precise equivariant information not mechanically determined by the known nonequivariant wedge count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
