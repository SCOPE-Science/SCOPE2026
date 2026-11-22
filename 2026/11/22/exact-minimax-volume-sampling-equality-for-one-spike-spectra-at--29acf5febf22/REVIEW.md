# Scientific review

## Correctness — PASS

The exact Schur-complement formula holds for every positive \(a,b\), every unit real \(v\), and every \(k\)-subset, because the chosen principal block remains invertible. The rational residual (1) is strictly decreasing in selected spike mass. The largest \(k\) squared coordinates carry at least \(k/n\) of total mass, with strict inequality unless all are equal, for every interior \(k\). Flat vectors exist and are realized by real orthogonal eigenbases. The elementary symmetric-polynomial calculation independently matches the precise expected-error formula. The finite checker uses actual rational matrix inversions but is not substituted for these universal arguments. The asserted domain, equality cases, and excluded scalar boundary are consistent.

## Originality — PASS, subject to independent priority review

Amsel et al., arXiv:2602.05394v1, Problem 4.7, defines the exact min/max and determinantal expectation and proves a general-spectrum equality only at the endpoint \(k=n-1\); it explicitly asks about other sizes. The present all-interior one-spike equality is not implied by that endpoint argument. Fornace–Lindsey, arXiv:2407.01698, supplies general expectation and selection bounds, not sharp worst-orientation attainment. Chen–Epperly–Tropp–Webber analyze randomized pivoting rather than this deterministic minimax. Related published results on the three-dimensional one-spike *random* two-pivot expected error and three-point correlation-kernel sampling address different quantifiers and lie at the already-known endpoint in dimension three. The proof and comparison support a distinct claim; an unlocated exact special-case statement remains a residual historical-priority risk.

## Value — PASS

A published and explicit low-rank-approximation question asks whether the volume-sampling spectral upper bound can be tight outside the single-unselected-column endpoint. A rank-one spike above isotropic background is a canonical covariance and kernel-matrix test spectrum. The theorem resolves all genuinely interior subset sizes for this class, exactly identifies when determinant sampling's expected error is as good as the best possible subset for the worst eigenbasis, and supplies a full characterization of maximizing orientations. The result is not extrapolated to arbitrary eigenvalue patterns.

## Limitations and references

Only strictly positive background and spike are covered, with \(n\ge4\) and \(2\le k\le n-2\). The two-level spectrum has a repeated lower eigenvalue, not a general multicluster spectrum. Finite experiments do not prove the statement. References: Amsel et al. (2026), arXiv:2602.05394v1, sec. 4.2; Fornace and Lindsey (2024), arXiv:2407.01698, secs. 2/5 and App. C; Chen et al. (2024/2025), doi:10.1002/cpa.22234, App. C.

Self-review: passed. Independent audit: not yet performed.
