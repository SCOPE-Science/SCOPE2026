# Independent mathematical audit

## correctness

PASS

For real planar SPD A, the bilinear form is the quadratic form of the symmetric Jordan product with SᵀS. It has positive diagonal almost surely in the eigenbasis and has a negative direction exactly when the squared column cosine exceeds 4κ/(κ+1)². Gaussian decomposition into parallel and perpendicular parts gives independent χ²_1 and χ²_(k−1) and the asserted beta tail. For a fixed v the normalized outputs are g and c(v)g+√(1−c(v)²)h with g,h independent standard Gaussian columns. Conditioning on g gives a one-sided normal tail mixed by ||g||²∼χ²_k and yields the asserted half-beta law, including k=1 and zero risk for c(v)=1. Differentiation gives the attainable minimum cosine at high-mode squared weight 1/(κ+1). The row shift is exact. The ratio limit follows from kR² converging to χ²_1 as k grows, the small-threshold argument when k is bounded and κ grows, and E R²=1/k for the strongly oversampled case. The iff follows by subsequence extraction. Independent low-row angular and Gaussian-conditioning checks passed (/workspace/independent_checks.py). In the scope note, zero probability of equality applies to a prescribed v or to the singular determinant threshold, not to existence of a sketch-adaptive null vector: an indefinite form has such null directions. The proof uses the determinant boundary and the main strict-negativity formulas are unaffected. No claim about Ritz eigenvalues of an entire two-dimensional pencil was verified.

## originality

FAIL

Indexed record 82e6f28b1c80 states the same uniform law in complement form on an arbitrary fixed invariant two-eigenvector plane, the same critical normal profile, and the sharper fixed-tolerance row-budget statement. Scaling Gaussian entries by √k does not affect signs. For the precommitted direction, Kabán–Durrant's exact fixed-pair sign-flip formula applies directly to (v,Av). It is monotone in their cosine, so evaluating it at the minimum of the one-variable angle expression yields the frozen worst-fixed law, including k=1. Once these two covered formulas are written in beta form, the one-row bridge is a substitution, and its fixed-vector limits follow from the uniform law. This is substantial direct coverage plus immediate consequences, not a negative-search verdict.

## value

FAIL

The adaptive versus precommitted distinction is relevant for positivity of one-dimensional sketched projections. But the adaptive risk and sharp scale were already given, the precommitted maximum is obtained by the standard fixed-pair probability and an elementary attained angle minimum, and the row shift is direct beta-parameter matching. The frozen result is a useful juxtaposition, not a distinct scientific finding at the stated bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
