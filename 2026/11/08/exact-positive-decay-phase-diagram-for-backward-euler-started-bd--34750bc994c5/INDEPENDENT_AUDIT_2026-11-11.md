# Independent mathematical audit

## correctness

PASS

The frozen proof uses genuine variable-step BDF2 with r_n=h_n/h_{n-1}, backward-Euler u1=u0/(1+x), and arbitrary positive alternating normalized steps x first, y second. Algebra gives det P=xy/(D_x D_y), trace P=[s²(2-s)+2xy(s+1)]/(D_x D_y), and discriminant s^4[(x-y)²-4(s-1)]/(D_x²D_y²). Independent SymPy expansion verifies this exact identity. For s<2 and Δ≥0, positive distinct eigenvalues and a positive dominant starter component or a positive Jordan correction at Δ=0 establish all-index positivity; complex roots oscillate in sign, and negative-real roots for s>2 force sign changes. The recurrence difference identity makes every positive trajectory strictly decreasing. Exact-rational 120-step trajectories corroborated both short-first (1/8,9/8) and long-first (9/8,1/8) boundary, and excluded equal-step example (3/5,3/5) displayed sign loss. The proof treats all index and parameter quantifiers; finite checks alone would not.

## originality

PASS

The earlier October 26, 2026 full theorem Exact positivity threshold for alternating-grid BDF2 already proves the sharp boundary 0<λh≤2/(√r+1)² for a **long-first** H,h,H,h,... sequence with backward-Euler first step of size H. Algebra with r=H/h shows its boundary equals the submitted symmetric (x+y)² relation when x≥y. That whole long-first portion and its high-contrast limit are decisively prior and are NOT claimed novel. The earlier result does not cover the reverse **short-first** BE starter x<y, because changing time origin alters the initial BDF2 history. The submitted all-index argument covers this additional phase and proves the same sharp boundary/strict decay without inherited-starter equivalence. No checked stronger all-phases result was found; originality PASS best-of-knowledge for phase-completeness ONLY, with unusually large partial prior coverage and a residual possibility of trivial or implicit phase derivation in old Floquet analyses.

## value

PASS

Exact all-index sign preservation of a genuine variable-step multistep method under both starting phases is a natural numerical-analysis robustness criterion; an initial BE value depends on the first step. Establishing phase invariance of the sharp boundary at arbitrarily large step contrast and strict monotone decay gives meaningful additional completeness beyond the published long-first theorem. Importance resides in the nontrivial short-first starter analysis, not a claimed discovery of the already known boundary polynomial or high-contrast limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
