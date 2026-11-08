---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 verify_sink.py` with a standard Python 3 interpreter; it has no external dependencies. It prints a distribution-comparison table and ends in `VERIFY_OK 182 exact-enumerative and numerical cross-checks` when successful. The executable independently enumerates every orientation of \(K_{a,b}\) for \(1\le a,b\le4\), testing acyclicity via forbidden alternating binary minors, comparing whole distributions to the Stirling poly-Bernoulli formula, and checking all derived factorial-moment identities. It also computes finite numerical total-variation distances for balanced sizes up to \(n=50\) as a diagnostic.

The infinite theorem is *not* inferred from these finite diagnostics. The proof uses the marked generating-function identity, the established strict-minimality lemma, and the published analytic smooth-point transfer theorem applied with an entire parameterized numerator. The limit of total variation and the local probability error depend on those analytic steps. The independent audit is not performed; historical priority under related enumerative language remains a risk.
