# Scientific review

## Correctness (C): PASS
The four-state generator is written explicitly in the physical occupation basis, and its exact characteristic polynomial factorizes into the constant, mean, and pair blocks. The only eigenvalue collision is the equation \(h(a+b)=ab\). A fast mean eigenvector \((a,-b)\) couples to the pair block with matrix element \(ab(q-p)\); this proves the iff Jordan criterion and defect size. Integrating the exact moment equation yields the general polynomial-exponential amplitude and the concrete empty-initial-state pair probability. The standalone `verify.py` passed symbolic, rational-rank, and independent matrix-exponential checks. Finite tests are corroboration, not the general proof.

## Originality (O): PASS, qualified
Schulman–Sinclair (2026, arXiv:2607.22991, Section 5 and Remark 10) prove spectrum independence and describe a three-site Jordan example, but not the complete two-site resonance, density criterion, minimality, and observable-blindness classification. Frassek (2019, arXiv:1910.13163, Sections 2.1–2.2 and 4) obtains generic open-SSEP eigenvectors while explicitly assuming nondegeneracy in the relevant construction, and stationary correlation formulas rather than the resonant transient. Floreani–González Casanova (2023) treat the nonequilibrium stationary law. Comparisons also covered accessible earlier same-topic findings and targeted indexed searches; no covering statement was found. The strongest residual risk is an elementary two-site exceptional parameter calculation or an integrability extension unavailable in the inspected literature.

## Value (V): PASS
The theorem provides the smallest explicitly classified nonequilibrium singularity in boundary-driven exclusion: it pinpoints the exact matching of exchange and reservoir contact rates, distinguishes genuine physical nonequilibrium from spectral degeneracy, and gives a joint observable with a provably nonzero polynomial-exponential relaxation despite complete blindness of one-point means. It supplies a concrete benchmark for interpreting the general recent spectral-invariance result, not merely a recomputation of the stationary law. The scope is two sites; no larger-system phase claim is implied.

Self-review: passed. Independent audit: not yet performed.
