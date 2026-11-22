---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

At r_*=X+log(1−h/X), X(X−h)=h, define b=X−h=h/X and a=1−b. The (N+1)-dimensional linearization has polynomial λ^(N+1)−aλ^N+b. At a root b=|λ|^N|λ−a|, ruling out |λ|≥1 by the reverse triangle inequality, including equality λ=1 which is not a root. For near-unit branches set λ=exp(z/N) and solve exp(z)(exp(z/N)−a)=−b around odd multiples of iπ. The IFT expansion gives log|λ|=−a(2m+1)²π²/(2b²N³)+O(N^-4) and phase π/N−π/(bN²)+O(N^-3). Every maximal-modulus root has bounded z=Nlogλ and must lie on finitely many such branches; |2m+1|=1 gives exactly one dominant conjugate pair and 1−ρ_N=aπ²/(2b²N³)+O(N^-4). Independently solved dominant branch numerically for h=1 at N=30,100,400; scaled gap approaches π²/2; finite tests not universal proof.

## originality

PASS

Published Ricker studies derive stability regimes for the same stocked equation and different finite lags. Kuruklis (1994) treats precisely the generic delay recurrence and its stability criteria, but its entire original article was inaccessible; authorized Oxford institutional retrieval returned VPN disconnected after arXiv/OA attempts. This inability ALONE is not originality failure. No positively verified earlier statement dominates the sharp N^-3 spectral coefficient and unique dominant conjugate branch; best-of-knowledge PASS with material priority risk from Kuruklis and Levin–May.

## value

PASS

At a natural exact stability threshold, strict Schur stability of each finite lag does not quantify practically relevant relaxation times. The explicit cubic damping law and nearly 2N oscillation period resolve a distinct asymptotic spectral bottleneck, motivated directly by delay-population dynamics; it is not a tiny parameter gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
