# Scientific review: complement-block minimax sampling

## Correctness

PASS. The rank-one residual identity follows by exact block minimization in the \(H\)-orthogonal complement of the updated subspace. The induced conditional expected energy matrix has a Gram representation. A fixed normalized Rayleigh witness gives a universal \(1/R\) lower bound on the largest eigenvalue; a positive Perron vector attains it, and invertibility proves uniqueness even against boundary probability vectors. The three-variable star Gram, determinant probabilities, eigenvalue branch, derivative signs and \(4/3\) limit are derived without relying on finite experiments. The packaged checker independently reconstructs exact residuals and spectral identities. Risk: results assume exact SPD arithmetic and fixed iid block draws.

## Originality

PASS, qualified. Rodomanov–Kropotov's full preprint develops volume sampling and broad convergence rates but does not state that volume sampling is inferior to uniform omission for the displayed star family or the optimal leave-one-out law. Qu et al. develop general randomized Newton block methods without the sharp fixed-law classification. The closest published inverse-positive coordinate result optimizes single-coordinate updates via a smallest eigenvalue and cannot be substituted directly into the all-but-one-coordinate largest-eigenvalue problem. Existing three-variable pair-sampling work already provides the special star minimax weights; that covered component is used as a comparator, not counted as novel. The all-parameter strict volume-versus-uniform reversal and the sharp limiting decrement ratio are separate comparisons not supplied by the inspected statements. Residual precedence risk: an equivalent saturated E-optimal-design or diagonal-scaling theorem could yield the general signed-Gram lemma; the elementary star-volume reversal was not identified in the inspected primary texts. No claim of exhaustive precedence is made.

## Value

PASS. Determinant-proportional volume sampling is a mathematically motivated fixed-size block design with known theory; finding a uniform family where it loses to uniform sampling in the sharp energy metric is a substantive benchmark. The exact optimal distribution and its factor-\(4/3\) asymptotic expected-decrement advantage quantify the distinction at equal block solve dimension. This is not a guarantee of better wall-clock speed or longer-horizon optimality.

## Scope and independence

The reviewed claim is only the joint explicit minimax law plus the three-variable star comparison, with all hypotheses in RESULT.md. Proof and finite checks are internal to this package; no independent scientific validation has been performed.

Self-review: passed. Independent audit: not yet performed.
