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

For fixed hub, leaves independently wait their first rate-one copy; T is max of n+1 Exp(1) with CDF (1-e^-t)^(n+1), mean H_(n+1), centered Gumbel. For fixed positive leaf, the (hub state h, number k of positive ordinary leaves) generator is exact. From all-negative ordinary state F, the only changing exit has rate 1/(n+1); an excursion from (1,0) has uniformly bounded expected duration O(log n) by geometric spell completion. Degree-weighted M=h/2+(k+1)/(2(n+1)) has generator (1-h)/(2(n+1)), giving (2n+1)q=n+1+EB and q=1/2+O(log n/n). Geometric compounding of Exp(1/(n+1)) holding times gives exact exp(q/(n+1)) wait, and O(log n) excursions vanish at n scale. Reconstructed reduced finite-state rational generator and independently solved small n hitting times (n=1..6) as a bounded cross-check, not an asymptotic proof.

## originality

PASS

Pinned internal star center versus leaf, with first all-positive passage and rate-one node clocks, is not the same as external opinion maker dynamics, unpinned star consensus or competing zealots. The surveyed primary literature and Resultary records address these related but different observables; no exact rate-1/2 leaf-pinned exponential first-passage law was found in material inspected. A finite-graph duality derivation remains a possible alias, openly recorded as residual risk.

## value

PASS

Zealot placement is a natural structural variable of voter dynamics. Switching the pinned positive vertex between the hub and a leaf changes not only expected scaling logarithmic versus linear but the entire limiting law Gumbel versus exponential; the precise 1/2 hazard constant makes it a meaningful boundary result for network consensus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
