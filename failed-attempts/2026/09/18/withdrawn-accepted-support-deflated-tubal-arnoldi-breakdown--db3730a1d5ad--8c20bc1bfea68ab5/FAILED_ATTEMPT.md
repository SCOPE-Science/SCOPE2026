# FAILED ATTEMPT — NOT A VALIDATED FINDING

**Record:** `2026/09/18/support-deflated-tubal-arnoldi-breakdown--db3730a1d5ad`  
**Independent audit date:** 2026-09-29 (UTC)  
**Task:** `04ce824cc366c919805f0d39532afdea`

This package is preserved for provenance, but the independent audit does **not** validate it as a distinct publishable research finding.

## Correctness retained

PASS. Fourier diagonalization identifies the tubal-scalar algebra with C^p and the t-Krylov module with the product of the ordinary slice Krylov spaces, giving component dimensions min(j,ν_k) and the stated free-module criterion. A usual unit-tubal normalization first becomes noninvertible when a slice reaches the minimum grade, and global invariance occurs there exactly when all grades coincide. Componentwise Moore–Penrose inversion of the residual norm correctly zeroes exhausted frequencies and normalizes active ones, producing idempotent support norms, frequencywise Arnoldi continuation to ν_max, the projective direct-sum decomposition, and the slice-wise tensor-function error formula. The explicit two-frequency and finite-tolerance examples are consistent with this analysis.

## Decisive originality finding

FAIL. Gleich–Greif–Varah’s 2012/2013 paper on the same circulant/t-product algebra already states that when a circulant scalar is singular their approach is to use the matrix pseudoinverse and that this suffices for Arnoldi; it also explicitly proves/observes that the Fourier-space Arnoldi process decouples into individual Arnoldi processes on each Fourier block. Those two prior facts are exactly the mechanism of the submitted “support-deflated” continuation: pseudoinvert the singular tubal norm, normalize only nonzero Fourier components, and continue the independent active Arnoldi processes. The min/max grade and projective-support descriptions are useful algebraic restatements, but they follow directly from this established decoupling-plus-pseudoinverse framework. The 2026 global-stop tolerance example may expose an implementation issue, but it does not rescue the package’s central novelty claim.

## Scientific-value finding

FAIL AS A STANDALONE NEW RESEARCH CONTRIBUTION. The package is mathematically coherent and the finite-tolerance counterexample is a useful warning, but its headline continuation mechanism is already present in the older circulant-algebra Arnoldi literature, and the exact grade/free-module consequences are routine once one combines that prior pseudoinverse rule with frequencywise decoupling. The remaining implementation observation is better suited to a correction/note than to validating the present package as a distinct research finding.

## Preservation note

The complete original package should be relocated atomically to the assigned failed-attempt destination. No original evidence file should be selectively deleted. A future submission must contain substantively distinct research content and be audited as a new record.
