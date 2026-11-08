# Scientific review

## Correctness — PASS
The claim is conditional on an explicit parameter domain. The global convergence follows from bounded Ricker-map comparisons and an eventual predator carrying-cap bound; the critical equality is retained throughout, rather than replaced by an unjustified strict inequality. At the resulting nonhyperbolic boundary equilibrium, the fast multiplier is \(1-h\in(0,1)\); the center-graph coefficient, third-order prey recurrence, and reciprocal-summation logarithm are derived explicitly. Exact arithmetic in `verify.py` confirms both contrasting rational examples and the unique sign-change threshold. Numerical traces are only illustrations. An initial-condition-dependent finite constant is proved to exist but is not computed in closed form.

## Originality — PASS on available evidence
Lin et al. (2022), DOI 10.3390/axioms11100520, cover the model and ordinary local/transcritical and global-attractor analysis; their accessible abstract, introductory model description, discussion, results overview and indexed article passages do not supply the global equality-case reciprocal asymptotic with a logarithmic remainder. The related Chen–He–Chen (2021) paper uses a different predator update and provides attraction criteria rather than this coefficient. Related research records on Du–Han–Lei discrete fear maps, Hong–Zhang discrete fear–Allee systems and continuous critical Leslie–Gower models have materially different hypotheses or claims. An accessible publisher article page was indexed, but full article retrieval was rate-limited, leaving a real risk of a covered calculation hidden in uninspected detailed sections or other publications. This is a best-knowledge assessment, not certification of priority.

## Value — PASS
The natural ecological question is what *rate* of prey extinction occurs exactly where the local prey-invasion multiplier equals one. The result supplies a global quantified answer and a first finite-generation correction which changes direction with prey crowding, all within a fixed ecological model. The two exact examples show that the correction is not an artifact of notation or merely a generic unmotivated higher-order expansion: it differentiates parameter regimes whose leading \(1/n\) mechanism is the same.

## Closest work and residual limits
The strongest overlap is the initiating 2022 article's boundary equilibrium and transcritical analysis. The claimed logarithmic refinement is not implied merely by its stated stability conclusions; a complete inspection of the article's technical body and appendices remains desirable. The theorem applies to a deliberately explicit subcritical-growth subset and not to all feasible model parameters, and does not address stochastic dynamics.

Self-review: passed. Independent audit: not yet performed.
