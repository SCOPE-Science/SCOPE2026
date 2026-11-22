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

Every positive weight w_j<=1 tends to zero, so W_k=Π_{j<k} w_j decays faster than any fixed exponential. The exact n-step backward preimage coefficient ratio W_max(k-n,1)/W_k for k>0 (and 1 for k<=0), and its weighted ell_p norm, give both directions of the analytic-core characterization: the predecessor coordinate 1 forces |x_k/W_k|≤CR^k, while the weighted tail series Σ_m R^{pm}W_m^p is finite. Forward iterates on the positive half-line decay in nth-root norm, while the n-th output at index 0 equals x_-n, giving the exact H0 negative-tail condition. One test vector x_k=W_k forces necessity of the exponential comparison for core inclusion; the reverse implication uses the coordinate envelope. W/V and V/W exponential comparison yields log-difference O(k). The specific 2^{-j²} vs 2^{-j} witness separates cores. Finitely supported vectors establish density, the sqrt(W_k) and polynomial negative-tail vectors establish properness, and nonclosed range plus dense analytic core excludes generalized Kato splitting. Independent finite exact-rational predecessor identity checks passed for 96 (k,n) pairs with nonmonotone weights.

## originality

PASS

The Nov 8 published geometric-tail analytic-core theorem covers only w_j=q^j on ell², not arbitrary nonmonotone null tails in all ell^p or necessary-and-sufficient inclusions between different cores. General local spectral backward-orbit lemmas are credited. The cross-weight order is a mathematically additional condition, not simply the older Gaussian membership test rewritten.

## value

PASS

Analytic cores and quasinilpotent parts are natural local-spectral invariants and pseudo-Fredholm obstructions. The exact all-weight membership tests, tail-independent H0 and strict cross-operator partial order give a useful classification across nonmonotone asymptotic tails rather than a single example. This is not just a reparameterized known geometric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
