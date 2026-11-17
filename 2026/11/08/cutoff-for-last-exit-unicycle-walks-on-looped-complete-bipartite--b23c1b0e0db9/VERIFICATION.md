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

For balanced a,b with M=max(a,b), position transitions are independent of arrow memory. Coupling position walks gives meeting tail <=exp(-2h/(M+1)); after meeting common departures from every vertex erase differing arrows. Uniform two-step target hitting >=m/((m+1)(M+1))=(1+o(1))/M, so union coupon bound finishes by (1+eps)2Mlog M. For lower bound initialize arrows of all M-side vertices at one opposing vertex z; before (1-eps)2Mlog M at most t/2 uniform crossings into the M side, leaving M^{eps+o(1)} untouched arrows, while stationary expected z-incoming arrows <=M/m=O(1) by part symmetry. Total variation separates. Uniform rooted-unicycle stationarity follows direct transition-column counting; no full-memory independence assumed. Finite checks are corroborative, not infinite proof.

## originality

PASS

Best-of-knowledge after actual Resultary searches and material full published-source reading: The foundational 2024/2026 Kaiser-Levine-Sava-Huss work proves complete-graph cutoff and poses noncomplete-graph cutoff questions; graph-dependent bipartite bounded-aspect result does not follow by matching walk name, since position coupon rates differ. ['Historical literature on total chains beyond the foundational preprint may contain noncomplete-graph cutoff; exact leading window/profile not claimed. Asymptotics assume m/M bounded away from 0.']

## value

PASS

A new explicit noncomplete family with provable total-variation cutoff answers a concrete open direction in locally Markov walks. The full-memory chain, coupon collector bottleneck and balanced-aspect-ratio sharp leading mixing scale are nonroutine, structurally meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
