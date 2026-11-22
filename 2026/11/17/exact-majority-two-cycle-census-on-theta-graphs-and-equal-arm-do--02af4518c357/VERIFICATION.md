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

PASS. A changing degree-two interior vertex on a genuine temporal two-cycle must have both neighbors flip in antiphase, so any active theta path flips in full alternating pattern and both terminals flip. All other path interiors are frozen binary words with no singleton runs incl both ends (except L=2 singleton frozen iff the terminal phases oppose). If S is the nonempty set of active paths, common length parity is necessary, while terminal strict majority gives disjoint |S|=3 contribution1, |S|=2 contribution 2(E+O) on remaining path, and |S|=1 contribution 2(E_j E_k+O_j O_k); exact run-composition functions E(z)=z²(1-z)/[(1-z)²-z4], O(z)=z4/[(1-z)²-z4]. Check L=2 special, path lengths >=2, tie-retaining degree-two sites, no direct chord, label phases counted once. Equal arm E+O=F_{L-2}, E-O=periodic delta, yielding total 3(F²+delta²)+6F+1 and exponential one-active dominance with golden ratio rate. Independent brute-force F(F(x))=x!=F(x) on several triples reproduces exact numbers; universal claim follows the propagation proof.

## originality

PASS

PASS, qualified. An earlier complete singly-chorded-cycle majority theorem shares run-count method, but it has a direct edge between the two exceptional terminals, whereas these theta graphs have three internally subdivided paths and no direct chord. Its all-parameter formula cannot be substituted without altering local degree-two dynamics and terminal support conditions. General Goles–Olivos and Benjamini et al period-two results give no orbit numbers; three-state excitable theta results use a different update rule. No searched prior exact three-path no-direct-edge majority two-cycle formula dominates this one.

## value

PASS

PASS. The all-length three-parameter labelled orbit classification with active-path refinement and sharp equal-arm dominance is a motivated structural invariant of a natural two-terminal graph family. Endpoint parity and stationary-run interface produce nontrivial exact Fibonacci/period-six terms, beyond textbook period-two existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
