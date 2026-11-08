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

# Verification of the sharp bispectral spectral-erasure theorem

The argument is self-contained. Its nonstandard ingredient is the dense partial-character extension lemma: for a Fourier support missing \(r<N/4\) frequencies, the translated overlap contains at least \(N-2r>2r\) points, and the threefold translated intersection is nonempty because \(N-3r>0\). Connectivity of the associated difference graph makes each increment quotient independent of the chosen starting point. Telescoping over a threefold intersection produces an exact group character, not an approximate one. Conjugate symmetry and Fourier inversion then give an actual translation.

The dependency-free `CHECK.py` was run from the same packaged source and returned `SHARP_BISPECTRAL_CHECKS_PASSED 28604`. It checks the six exact zero-sum triple types of the \(\mathbb Z_8\) Fourier counterexample, full correlations through order three, numerical positivity, nontranslation, a product-group construction, finite-root small-case extension searches, and translated-overlap graph connectedness for all eligible erasures of cyclic groups of orders two through sixteen. The checked phase exponent identities are exact integer arithmetic; floating point is used only for finite representative function values and correlations with explicit tolerances.

The universal theorem follows from the published proof in `RESULT.md` and not from the finite checks. No Lean, formal proof certification, independent audit, or external reproducibility validation is claimed. The cited literature comparisons support bounded originality confidence, not absolute proof of priority.
