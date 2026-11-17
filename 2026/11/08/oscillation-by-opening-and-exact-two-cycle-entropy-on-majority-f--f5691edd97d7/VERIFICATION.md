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

Read the frozen fan-graph RESULT.md, its majority rule with tie retention, and verification program. For a constant hub the endpoint-reflexive AND/OR path map has only monochromatic recurrent states; a flipping hub gives x=DEx and strict inequalities 2|x|>n>2|Ex|. The neighborhoods form an auxiliary n-cycle; DE x=x means no isolated cyclic 1s, with e=k-r internal 11 edges and r runs. Cyclic composition counting yields n/r*binom(k-r-1,r-1)*binom(n-k-1,r-1) and excludes n=4. Independently enumerated the actual majority update for n=3..11 and matched fixed states, primitive cycles and run formula, including count sequence 3,0,5,3,21,16,66,65,220. The weighted four-state transfer has characteristic z*(z^3-(1+uv)z^2+uv*z-u^2*v); Perron eigenvalue lambda solves lambda^3-2lambda^2+lambda-1=0. Its weighted mean inequalities mu_k>1/2>mu_e yield exponentially small inadmissible words by tilting and hence C_n=lambda^n+O(eta^n) with eta<lambda. The proof is all n>=3; finite enumeration is corroboration.

## originality

PASS

The exact fan orbit morphology, hub-flipping classification, two fixed states, threshold n=4, and exact counts are ALREADY COVERED by the October 26 fan-graph 16-state transfer theorem. The defensible new remainder is the compact closed run-binomial expression AND, more importantly, the nontrivial exact Perron growth constant and exponentially small error for primitive fan oscillations. The earlier source expressly leaves a simple closed asymptotic law open, so the entropy result is not established by its stated conclusions; acknowledge the prior formula determines each finite count.

## value

PASS

The asymptotic exponent log(lambda) and exponential error are a meaningful new invariant for the family of synchronous fan networks. The entropy is not a one-line specialization of the prior exact 16-state transfer: the strict global hub-density inequalities require a quantified large-deviation/Perron argument. Classification and n=4 cutoff by themselves would NOT have independent value after the October theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
