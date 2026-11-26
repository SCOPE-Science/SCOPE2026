---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Stationarity and the two-state transition give E[X_{i+k}−π|X_i]=λ^k(X_i−π). Independent Bernoulli detection then gives m_i=πd_i and C_ij=d_id_jπ(1−π)λ^(j−i). The displayed inverse cancels both detection rates, works for negative as well as positive memory, and is well-defined under the stated strict ranges and λ≠0. For sufficiency, the recovered transition probabilities have sum 1−λ and stationary prevalence π; building the detection coins reproduces the six moments exactly. This is not a feasibility test for the full eight-cell distribution. The two-season example has means 1/5 and 3/10 and joint success 9/100 under both distinct models, which fixes all four cells. At λ=0, each observation is independent with its mean πd_t; even for an infinite sequence, sup m_t≤π<1 and one can choose a different π above sup m_t. The false-positive example has common means and covariances since its gain is 25d_t/24 and its latent variance is 144/625. Its two triple probabilities differ by 7/3456, so it is correctly used only to disprove pairwise recovery. The derivatives of the inverse prevalence check out with the other normalized moment held fixed. The inspected exact-fraction certificate is finite corroboration; verify.py was inspected, not run.

## originality

FAIL

The decisive prior overlap is the actual proof of Resultary a0eacad9db44, not a literal inclusion in its theorem's strict unknown-f parameter domain. Its exact unnormalized and normalized moment identities and inverse already apply once a common false-positive rate f is fixed. In the equal-outer-sensitivity section it explicitly reconstructs the same quantities for each chosen f using those same formulas. Thus specifying f=0 gives the frozen inverse and feasibility calculation for all interior sensitivities, including equal outer seasons: no division by c_01−c_12 is required once f is given. The same proof supplies the boundary reasoning for two seasons and zero memory after fixing f. The six-moment contrast with unrestricted false positives is already implied by a published full-law ambiguity, although the frozen numerical example is valid. This conclusion is based on verified prior implication, not on missing external literature.

## value

FAIL

The design question is well motivated and using low-order moments rather than full histories is useful. As a separate contribution, however, the reconstruction is the earlier fixed-f calculation at a specified rate, with the same structural boundaries. The alternate finite witnesses and derivatives illustrate, but do not supply a separate new design boundary or justified precision result that survives this coverage. No finite-sample utility is established by the conditioning derivatives alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
