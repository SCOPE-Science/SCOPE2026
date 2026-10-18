# Independent mathematical audit

## correctness

PASS

For binary strategies S in {0,1,2,3}, (S/3)^gamma converges uniformly to 1_{S=3}=s_i s_j s_k; the exact maximum discrepancy is (2/3)^gamma. Normalized game payoff discrepancy is at most B=3 alpha r q_*(2/3)^gamma. Payoff-gap perturbations are <=2B; the Fermi response is 1/4-Lipschitz; the one-step imitation-plus-mutation kernel perturbation in total variation is <=B/2, capped by 1. Telescoping gives fixed-time bound tB/2; irreducibility/aperiodicity at 0<mu<1 on finite graph gives unique stationary distributions which converge by finite-dimensional continuity. Assumptions fixed finite hypergraph with nonempty game/model-player sets. Inspected verifier checks 8 triad states and a 3-person kernel; those experiments are not needed for the uniform analytic bound.

## originality

FAIL

The originating 2026 Tang–Rao paper itself writes both the power-law and strict-product formulas for the exact same binary triads. The endpoint identity follows immediately by substituting S=0,1,2,3; its stated kernel/stationary convergence is a routine consequence of the derivative bound for logistic imitation and standard finite Markov-chain continuity. No independently unentailed mathematical theorem is supplied. The article does not explicitly call the product rule a gamma-infinity endpoint, but lack of wording does not make a direct corollary original.

## value

FAIL

The observation clarifies what the original robustness experiment actually tests, but the exact limiting identity is a one-line elementary normalization of formulas already printed side by side, and the total-variation bound/stationary convergence are standard finite-state perturbation exercises. No nonstandard structural, sharp threshold, new model classification or deeper mathematical obstruction is identified. Interpretive utility alone does not meet this audit’s substantive mathematical-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
