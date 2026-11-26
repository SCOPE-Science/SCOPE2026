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

After k deletions and j retentions, the next host letter has parity k+j, while the next required deleted letter has parity k. Thus a deletion is legal only at even j, and at odd j the next host letter, if any, must be retained. This gives consecutive opposite-letter pairs, with any odd tail last and equal to d mod 2. At an even retention count a full pair does not change phase; a deletion gap flips phase exactly when its length is odd. Boundary phases 0 and d mod 2 prescribe the parities of all ell+1 gaps, including the virtual phase at the end when r is even. Conversely each gap vector of those parities summing to d gives one positional embedding and the stipulated residual. Removing the T compulsory gap increments leaves (d−T)/2 freely allocated pairs of deletions, giving the stated binomial and the zero cases. Choosing transition positions is a bijection from size-t subsets of the ell+1 gaps when t has the endpoint parity. Summing and applying Pascal yields the finite binomial tail through min(d,ell); in particular all types are possible iff ell≤d, and at ell=d+1 the only omitted type switches at every gap. The empty word, no deletions, no retentions, and either tail parity obey the same argument. As an additional check, writing deleted positions with zero-based indices j+2z_j gives weakly increasing z_j between 0 and ell, so the aggregate number of embeddings is binomial(d+ell,d), also as stated.

## originality

PASS

The supported addition is the exact conditional positional fibre and histogram for arbitrary d and both host parities. Credit the known even-even support theorem and an exact same-day fixed-pattern multiplicity overlap; neither supplies the arbitrary-length result. General shuffle formulations and unconditioned embedding spectra also do not give these conditional fibre counts.

## value

PASS

The exact conditional weights determine the law induced on residual words by uniformly chosen positional embeddings, which neither a support census nor an aggregate embedding count determines. The transition statistic gives all weights and frequencies in one uniform law including parity and the first missing-word threshold, not just a finite or short-pattern extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
