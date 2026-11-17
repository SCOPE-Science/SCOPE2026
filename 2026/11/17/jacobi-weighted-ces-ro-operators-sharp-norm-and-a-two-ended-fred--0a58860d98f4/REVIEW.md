# Scientific review

## Correctness — PASS

The exact logistic isometry converts the weighted Cesàro kernel to one-sided integration on an exponentially two-ended weighted line. Its right-translation semigroup has sharp norm \(e^{-t\min(A,B)}\), giving the nonattained operator norm. The inverse derivative problem is solved explicitly by one-sided convolutions; the relative order of the endpoint rates yields the kernel, cokernel, and Fredholm index. Localized approximate plane waves prove non-Fredholmness on both limiting lines, including the single-circle case. A separate high-frequency test proves that zero has nonclosed range. The documented proof treats complex parameters and strict boundary inequalities, not just numerical examples. All 181 packaged finite diagnostics passed; these are auxiliary to the proof.

## Originality — PASS (with stated priority risk)

The June 2026 Belli–Gül–Ross–Siskakis theorem studies the same singular-kernel operator, but only on unweighted \(L^p(0,1)\). That paper's unrestricted norm and crescent formula are specializations here, not new contributions. The weighted ambient spaces introduce two freely varying endpoint rates; their inversion gives a new phase boundary, a sharp nonattained norm, and an explicit weighted annihilating functional. Abadías–Mahillo–Miana study a different Hardy kernel. Existing qualitative first-order exponential-dichotomy theory could imply the reduction at a more general level, and a directly covering weighted model may exist under different terminology. Literature priority is therefore not independently certified.

## Mathematical value — PASS

Jacobi powers are the natural endpoint weights on a finite interval. They separate the left and right exponential tails that coincide in the unweighted Hilbert case. In particular, nonzero endpoint powers generate a genuine open eigenvalue or residual crescent even when \(p=2\), and the exact norm and range formulas make the change quantitatively testable. The classification supplies the full sharp Fredholm picture for a meaningful two-parameter family, rather than a parameter substitution in the unweighted theorem.

## Scope and limitations

Only \(1<p<\infty\), \(-1<\gamma<p-1\), and \(\delta>-1\) are claimed. Boundary weights and other Cesàro–Hardy kernels are unexamined. Norm, spectrum and Fredholm claims are analytically proved; numerical checks are finite diagnostics. There is no independent external validation of correctness or originality.

Self-review: passed. Independent audit: not yet performed.
