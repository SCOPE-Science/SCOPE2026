# Independent mathematical audit

## correctness

PASS

Orthogonality gives r_k=z−ae_k, g_k=−λe_k and α_k^R=(1+q/e_k²)/λ. The warm step gives −q/e₀; every delayed step multiplies a nonzero e_k by −q/e_{k−1}², so every denominator is nonzero and signs alternate. For the normalized log amplitude u_k this is u₁=−u₀, u_{k+1}=u_k−2u_{k−1}; the displayed oscillatory solution has the correct initial data. The characteristic-root angle is irrational modulo π because 2cosθ=1/√2 is not an algebraic integer (its rational norm is −1/2). Both signs of the nonzero wave are attained bounded away from zero on recurrent open arcs; its amplitude grows as (√2)^k, proving both subsequential limits and the corresponding residual-norm claim. At balance the absolute error stays √q and signs alternate. The nontrivial first residual difference lies in span(a), so RD takes the exact scalar normal-equation step. At consistency the warm step alone suffices if terminated there; this does not assert that the literal quotient is subsequently defined. Read VERIFICATION.md and verify.py as text; the analytic argument proves the infinite claim, not the recorded finite rational tests.

## originality

FAIL

The stated inconsistent example is correct and is not a special case of Xu's positive-mode convergence theorem. Nonetheless the entire delayed dynamical dichotomy is already mechanically implied by the prior component identities and exact, spectrum-independent ratio theorem, by a regular zero-mode specialization; RD termination is already a scalar consequence of the published RD formula. No distinct scientific remainder was established. This is a finding of mathematical implication, not a claim that Xu literally stated the inconsistent theorem or proved convergence there.

## value

FAIL

The example is a useful caution about naively applying a consistent-system algorithm to inconsistent data. As a stand-alone new finding, however, the proposed scalar classification is a routine endpoint substitution in the existing exact ratio law, combined with a one-dimensional secant quotient; no distinct mathematical boundary beyond what those formulas already determine is established. The failure does not suggest the frozen formulas or the warning are false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
