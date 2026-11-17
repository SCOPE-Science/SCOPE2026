---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The contractive no-jump semigroup has a reducing dark eigenspace: Walsh frequency weight w vectors vanishing at every monitored r-shell vertex. For a corner initial state, its projection in each band is the S_d-invariant constant-frequency vector. The full-sphere restriction sends that line to a scalar times the shell constant, namely K_{d,w}(r) or equivalently K_r(w;d) with binomial rescaling. It is dark exactly at a polynomial zero, yielding p=2^-d sum_w C(d,w)1_zero. K_2(w;d)=((d-2w)^2-d)/2, so r=2 survival iff d is an integer square; two roots give the displayed weight and local Gaussian constant. Independent exact K2 root enumeration for d=2..100 verified the square criterion; the all-dimension proof is algebraic. Numeric long-time logs are not infinite-time proof.

## originality

FAIL

FAIL for stronger exact prior coverage: The full published November 2 Hamming-sphere coherent-absorption RESULT.md already establishes the identical Hamiltonian/no-jump model, arbitrary positive per-site loss rates, complete energy-resolved restriction formula, harmonic incidence decomposition and scalar (-2)^i K_{d-2i,w-i}(r-i). Taking its i=0 invariant component and the corner initial state yields the candidate survival law immediately, since the i=0 component is all the corner overlaps in each energy sector. Substituting r=2 gives the perfect-square criterion by an elementary quadratic identity. This is a genuinely covering theorem, not just shared notation or failed novelty search.

## value

FAIL

FAIL independent contribution: the physically interesting perfect-square corner-survival fact and rate invariance are a direct special-case consequence of the previously published all-shell, all-energy dark-space theorem and its proof, followed by an elementary Krawtchouk zero test and binomial asymptotic. As submitted, the final claim does not add a mathematically motivated structural lemma or unknown invariant beyond that stronger publication; nontrivial physics framing alone cannot restore originality or standalone value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
