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

The two explicit Cayley/rook neighbor constructions each have 16 degree-6 vertices and exactly 2 common neighbors for each pair, yielding A²=4I+2J and the same spectrum 6,2^6,(-2)^9. Rook row/column K4 gives eight four-one fixed majority configurations; Shrikhande neighborhood C6 precludes any K4. Independently built all six neighbor masks and enumerated all 2^16 bit states for each graph, traced complete functional graphs until cycle repetition, and classified exact first-entry time tau and least period. Rook p=1 tau=0:302,1:10104,2:29984,3:18720; p=2 tau=0:2394,1:4032. Shrikhande p=1 tau=0:142,1:7576,2:26240,3:18496,4:9024,5:960; p=2 tau=0:1370,1:1728. Each graph totals 65536; primitive two-cycle orbits 2394/2=1197 and 1370/2=685. The enumeration is exhaustive finite proof exactly over each declared 16-vertex graph; it asserts nothing for arbitrary strongly regular graphs or other tie conventions.

## originality

PASS

The fundamental eventual-period-at-most-two theorem is classical, but it supplies no exact two-graph census, transient depth or 8-versus-0 fixed-point witness. Related published exhaustive censuses on the same Shrikhande/rook graph pair use a three-state excitation automaton, whereas the same-rule census on Q4 uses a different graph. Both potential ambiguities were checked at the actual rule level.

## value

PASS

Rook and Shrikhande are the classical cospectral nonisomorphic SRG(16,6,2,2) mates. A complete natural nonlinear majority dynamical invariant distinguishing them—fixed counts, oscillatory cycles and sharp relaxation—and the independent K4 witness has clear graph-dynamics motivation and is nontrivial despite finite state space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
