---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Frozen proof Step 2 incorrectly says two extractions after the first injection require an additional injection. At L=3, 100→010→110→101→011→010→001→000→100 is a valid cycle with two extractions and no intervening injection. Both extractions happen with site 1 empty. The repaired proof bounds every nonreset transition from a vacant first site with downstream particles, not merely injections to three particles. A fixed bounded jump path (reset if needed, then remove rightmost particles without vacating site 1) supplies a uniform probability of hitting e1 within a fixed number of jumps, giving geometric jump-count tails and uniform holding-time moment controls. After an injection at e2, no exceptional transition forces exactly one extraction; after an e3 hop, no exceptional transition forces zero. Conditioning on the index and outcome of the first exception gives O(1/r) jump-count-weighted probability from either state. Multiplication by the O(1/r) probability of reaching them bounds the extra-reward moments at O(r^(-2)). A direct two-site exit gives exactly one reward. The rare-mark probability and the first two reward moments are c_L/r+O(r^(-2)); E C_r=1+O(r^(-1)), and E(M_r C_r)=O(r^(-1)) by conditioning on the first nonreset departure. Independent cycle-index marks converge to a Poisson point process. A uniform centered-duration maximal bound places physical exit times near lattice markers without assuming mark-duration independence. The union bound excludes bursts and the Poisson limit has no endpoint atoms, making the ordered time matching valid in J1. The regenerative site-1-only occupation fraction is 1/E C_r, so the stationary initial law follows by coupling. At each fixed r the regenerative variance rate uses E[(M_r-J_r C_r)^2]/E C_r, not an interchange of the time limits. Its mixed and duration terms are O(r^(-2)), proving the repaired sequential Fano limit.

## originality

PASS

The repaired finding credits the exact fixed-size mean-current overlap separately and corrects the frozen attribution. The distinct content is the rate-c_L full extraction process and sequential scaled variance/Fano limits. No inspected statement covers these observables in the specified fixed-size, strong-reset regime. Neither the mean-current result nor stationary occupation covariances imply them.

## value

PASS

Rare extractions in a driven recycling system could remain clustered, even with the known mean current. The process result shows that the clusters do not persist on the natural time scale, and the separate variance calculation shows the same Poisson signature in sequential stationary noise. The two-site anomaly persists in both, not just in the current.

The dated certificate retains the supplied scientific assessment, sources and limitations.
