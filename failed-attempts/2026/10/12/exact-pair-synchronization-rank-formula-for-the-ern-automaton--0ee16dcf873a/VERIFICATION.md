---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The canonical short-arc start x is unique (choose the larger endpoint at a diametric tie). For rank D=(r-1)n+n-x, rotation drops rank by one off wraparound and raises it at wraparound. When x=n-1, b changes the pair to P(r-1,0) or merges it if r=1, dropping rank by one. If only the other endpoint is n-1, x=n-1-r; b increases the separation by one and the rank by n when 2r+2<=n (including the diametric endpoint), or flips the start to zero and increases the rank by r when 2r+1=n. Otherwise b fixes the pair. The rank therefore lower-bounds length, and a^(n-1-x)b(a^(n-1)b)^(r-1) attains it; this also covers n=2. For i<j and g=j-i, the shorter gap gives the smaller cost since a gap change of at least one contributes at least n, larger than a start-coordinate difference; for g=n-g the second cost is smaller. Each full separation layer gives n consecutive ranks and the final diametric layer when present gives n/2. This proves the proposed hardest pair, spectrum, and mean. certificate.json and verify.py were inspected, not executed; the all-n proof is the rank argument.

## originality

FAIL

Cardoso's accessible 2014 thesis, in the same automaton convention, gives the constructive shortest path from the labeled extremal pair upon specializing its gap procedure to two states. That path already gives the rank of every labeled pair by taking suffix lengths; the submitted formula is an immediate evaluation of those lengths. Several distinct later-dated Resultary records also have actual mathematical coverage; that corroborating overlap is not a claim about their priority. The thesis passage, not the mere extremal length or unavailable literature, decides this failure.

## value

FAIL

Prescribed-pair distances are natural invariants, and the local rank proof is clear. But the closed expression is the count of the unused rotations and blocks of an already known constructive geodesic, and the mean and spectrum require no further result. The proof is a useful presentation of covered mathematics, not a new scientific contribution; no separate claim about larger subsets or costs is made in the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
