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

With s>0, consecutive clockwise gaps sum to n. A gap at most k violates independence, and any offending arc contains such a gap; for a singleton the only gap is n>k. Displacements up to 2k are available in at most two arcs, using one or two permitted positive increments. If a gap is at least 2k+2, the vertex 2k+1 after its start has no selected vertex in its preceding radius-2k interval. In this failure case 2k<n, so no modular representative of a walk can evade that test. Thus every gap must be in [k+1,2k+1], also when 2k>=n, where the upper condition is automatic. Marking one of the s selected vertices gives s times the number sought and is in bijection with a starting label and an ordered admissible gap vector; this works even for rotation-periodic subsets. Bounded composition inclusion-exclusion gives the stated count and can realize every sum from s(k+1) through s(2k+1). The allowed size interval is nonempty: putting f=floor(n/(k+1))>=1 gives n<=f(k+1)+k<=f(2k+1). For (9,2) the two admissible ordered gaps of length two are (4,5) and (5,4), giving nine sets; the only length-three vector is (3,3,3), giving three.

## originality

FAIL

The exact enumerator and support are mechanically implied by the published fixed-weight binary run-length enumeration together with the direct characteristic-word encoding and rotation incidence. This is verified coverage of the counting problem via a reduction, not a claim that the older paper uses quasi-kernel terminology or explicitly names D_{n,k}.

## value

FAIL

The digraph family and its spectrum are natural, and the graph representation is useful exposition. But here the exact result reexpresses fixed-weight run-length enumeration via the nearest clockwise predecessor and an incidence normalization. The gap observation alone is the immediate translation of the two local conditions, with no separate nonroutine remainder or invariant established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
