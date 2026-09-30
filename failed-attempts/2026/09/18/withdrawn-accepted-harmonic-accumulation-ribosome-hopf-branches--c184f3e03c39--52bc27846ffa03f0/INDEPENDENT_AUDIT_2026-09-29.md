# Independent Audit — Harmonic accumulation of Hopf envelopes in the ribosome-delay model

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `da82b07f8ec3dbbeaf2287fd4c06cba960713d22`  
**Audited current source tree:** `da82b07f8ec3dbbeaf2287fd4c06cba960713d22`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this audit file is staged by the ledger change-set and is not claimed to be already published.

## Correctness — PASSED

PASS AS A CONDITIONAL MATHEMATICAL STATEMENT. From the source parametrization tau_{k,n}=(2πn-theta_k)/omega_k and M=e^{-mu tau}, the submitted formula mu_{k,n}=(-log M)omega_k/(2πn-theta_k) is exact. Pointwise strict decrease in n is immediate, and taking an attained maximum on a compact branch set gives strict envelope ordering whenever the next maximum is positive. Bounded continuous phases yield the uniform 1/n+O(1/n^2) expansion. Under the additional assumption that the relevant positive-frequency branches persist continuously to M=1 with positive frequencies and valid positive-delay labeling, the fixed-small-mu proliferation statement follows by the intermediate value theorem. The record correctly stops short of the source's exact 2k-count conjecture and of a nonlinear Hopf-bifurcation theorem.

## Originality — FAILED

FAIL. The central ordering and harmonic asymptotic are elementary consequences of formulas already displayed in the 2026 source paper: increasing the integer phase index n simply adds 2π to the denominator of its own tau_k^n formula, while mu_k^n=-log(M)/tau_k^n is also written there. Passing from the pointwise inequality to maxima and expanding 1/(2πn-theta) are routine. The fixed-small-mu theorem is an intermediate-value argument under an extra persistence-to-M=1 assumption that the record does not prove for the ribosome model. No sufficiently independent new mathematical mechanism remains after the source formulas and the conditional hypothesis are recognized.

## Scientific value — FAILED

FAIL AS A VALIDATED NEW RESEARCH CONTRIBUTION. The note is a useful clarification of why the numerically observed branch envelopes should be nested, but it does not prove the source paper's stronger exact-count Conjecture 1, does not certify the model-specific branch persistence needed for its proliferation theorem, and does not establish nonlinear Hopf bifurcations. Its main theorem is therefore best regarded as an expository corollary of the published parametrization rather than a research advance meeting the audit bar.

## Independent checks

- Read the open full text of the 2026 ribosome-delay paper around its fixed-M frequency equation, phase-delay formula, mu_k^n formula, numerical envelope curves, and exact-count conjecture.
- Re-derived the pointwise n-ordering, maximum ordering, and uniform 1/n expansion directly from the published formulas.
- Checked the fixed-small-mu IVT argument and isolated its additional persistence-to-M=1 hypothesis.
- Verified that the record does not establish simplicity/transversality/nonlinear Hopf conditions or the source's exact 2k count.
- Searched for a later source-specific proof; no covering result was found, but the failure verdict does not rely on absence of search hits—it follows from the derivation being routine from the cited source.
- Verified no file under this assigned record changed between the dispatcher source-check commit and current audited main.

## Limitations

- The failure is an originality/scientific-value determination; the conditional formulas themselves are not being declared false.
- The source reports relevant positive-frequency branches numerically near M=1, but the record does not rigorously certify continuous persistence all the way to M=1.
- The result concerns spectral imaginary-root events and does not by itself prove nonlinear Hopf bifurcation.

## Evidence and references

- https://doi.org/10.1007/s00285-026-02420-3
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13263304/
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/harmonic-accumulation-ribosome-hopf-branches--c184f3e03c39

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
