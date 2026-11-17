---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

On μ(C_n), n>=4, each shadow spin minimizes a sum of three signs uniquely. Fix apex η, encode original spins in binary x_i; minimized energy is -2(B+T)J where B=#binary adjacent changes and T=Σx_i x_{i+2}. With k=#ones, C1=Σx_ix_{i+1}, D2=k-T, F=B+T=3k-2C1-D2. For even n, maximum F=3n/2 attained only by 2 alternating words; for odd n>=5, D2>=1 for nonconstant words and C1>=2k-n give max 3(n-1)/2 with precisely n unique single-11-defect words. Each apex choice doubles counts, giving g=4 or 2n and energies -3nJ or -3(n-1)J. Independently enumerated all physical graphs for n=4..8 and checked full degeneracy/magnetization; finite corroboration only.

## originality

PASS

The same graph family q=3 Potts result and single n=5 case are credited, but q=2 all-length energy and extremizer multiplicities require a separate cyclic binary maximization; no dominating q=2 theorem was identified.

## value

PASS

An exact, all-size maximum-cut/Ising frustration classification on the natural Mycielskian graph family, showing sharp even/odd defect mobility, constant versus linear ground degeneracy and magnetization ±1. This is a structural infinite-family result, not merely chromatic-number restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
