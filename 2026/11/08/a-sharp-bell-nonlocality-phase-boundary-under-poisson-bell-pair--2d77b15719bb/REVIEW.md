# Scientific review: sharp Bell-nonlocality threshold under decoherence and resetting

## Correctness — PASS

For the exact two-qubit Lindblad generator and Poisson reset-to-Bell state, regenerative averaging yields the X-state with entries \(q=x/[2(x+1)(x+2)]\), \(w=x/[2(x+2)]\), and \(c=x/[2(x+b)]\). The Horodecki correlation singular-value condition gives the stated maximum CHSH value. Each competing inequality has a unique positive crossing: one elementary, one the unique positive root of a polynomial with exactly one Descartes sign change. The monotone longitudinal correlation on the relevant interval proves the crossover \(b_c\); scaling the polynomial gives the strong-dephasing exponent. Wootters spin-flip eigenvalues yield the stated concurrence. The standalone independent Lindbladian/resolvent checker passed 491 assertions, including exact-rational inversions. Residual correctness risk: no formal proof assistant or independent scientific audit; this is a human-checkable analytic proof with computational corroboration.

## Originality — PASS, qualified

Relevant literature inspected at the level of directly applicable equations and models: Kulkarni–Majumdar 2023 (closed interacting two-spin resets and concurrence), Carollo–Lesanovsky–Garrahan 2023 (general open Lindblad reset generator and ordering probabilities), Wald et al. 2024 (discrete-time unitary two-qubit resets and correlations), and Murauer et al. 2026 (discrete-time Ising reset and depolarizing noise). These sources do not state a continuous-time Bell-pair amplitude-damping/dephasing CHSH phase boundary, its unique switch of dominant singular-value pair, or the \(\kappa^{2/3}\) law. Horodecki's general CHSH and Wootters's concurrence formulas are explicitly inherited. Their combination with known reset-resolvent machinery permits implicit derivation; this remains an originality/prior-publication risk, not an independence claim. No exact earlier statement was found in targeted literature searches or in previously documented comparable theorem statements.

## Mathematical value — PASS

There is a motivated experimental-control question: how quickly must a maximally entangled state be replenished to recover unfiltered Bell nonlocality against irreversible decay and dephasing? The theorem answers that question globally rather than at isolated parameter values. It identifies a nontrivial witness-geometry transition at a small but exact ratio, a unique CHSH-onset boundary, and a stronger \(2/3\)-power recovery-rate scale than the \(1/2\)-power entanglement scale. It does not assert a hardware-implementable loophole-free test, arbitrary noise, or an effect beyond the stated model.

## Literature and limitations

The first motivating reset-specific source identified was arXiv:2307.07485 (2023-07-14); the open-reset work arXiv:2310.06981 (2023-10-10) is the closer generator precedent. Additional inspected sources are arXiv:2410.11497 and arXiv:2610.40638. The older Horodecki and Wootters theorems supply standard diagnostic formulas. General channel-composition literature not directly located could cover an equivalent specialization. The result is confined to symmetric zero-temperature independent local Lindblad channels and ideal simultaneous Poisson Bell-state reinitialization. The included checker provides corroboration rather than an infinite-parameter proof.

Self-review: passed. Independent audit: not yet performed.
