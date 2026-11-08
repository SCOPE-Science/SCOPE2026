# Scientific review: reentrant fixed-budget restart control

## Correctness — PASS

The claimed domain is the localized three-state Grover walk with \(\ell>0\), an independent whole-state renewal clock supported on \(\{1,2,3,4\}\) with mean three, and observation in the stationary renewal phase. The coin recurrence generates the four origin-return probabilities explicitly. The finite-support equilibrium renewal identity gives a linear objective on a triangle with exactly three vertices. All pairwise score differences factor into three explicit polynomials; exact sign brackets and Descartes' root bound exhaust the positive crossings. The strict classical comparator follows from positive quadratic factors. The proof does not confuse a periodic clock with a convergent time-origin marginal or substitute a finite numerical sample for a universal proof.

Separately implemented amplitude propagation, exact rational checks of the polynomial differences, classical-convolution enumeration, root brackets and constrained-protocol tests are implemented in `verify.py`. They passed 8,307 bounded diagnostics. Analytical conclusions depend on the documented exact equations and sign arguments, not on the diagnostics.

## Originality — PASS, with residual priority risk

The initiating article by Das (arXiv:2609.08973v1, Sections II–III) already contains the quantum-walk model and general renewal occupation formula. Those are acknowledged foundations, not new claims. Its Sections IV–V specialize to geometric and power-law restart; Section VI optimizes monitored first detection, which uses a different objective. Yin–Wang–Barkai (2024) and Chełminiak–Wójcik–Wójcik (2025) likewise study detection/absorption rather than fixed-budget stationary occupation. A published first-detection renewal optimization on a fully connected quantum model is not a dominating theorem for this return-occupation phase diagram. Accessible earlier research ledgers did not contain the claimed self-loop-dependent three-switch policy. The specific polynomial switching thresholds, exact optimal policies and the classical strict dominance statement were not located in inspected sources.

Caution: generic renewal theory implies the optimization's linear structure, and the later finite algebra is an application of that structure. This does not establish exhaustive novelty. The full text of a plausible 2025 absorption paper was not obtained; its abstract concerns a different objective. A more general unpublished or unlocated policy-optimality theorem could diminish novelty.

## Mathematical value — PASS

The bounded four-step latency is physically meaningful for a clock with a short maximum waiting time; fixing its mean at three separates the *shape* of the clock from its average frequency. The theorem completely classifies every admissible randomized clock, rather than reporting a few examples. It exhibits the nonmonotone order of four distinct optimization regimes: a deterministic law, two different extreme randomized laws, and reentrant deterministic optimality. Under the same one-step position probabilities and restart budget, the classical independent-step walk has no randomized-optimal regime at all. This isolates an experimentally interpretable role of coherent three-step return interference that an average reset-rate comparison misses. At the standard \(\ell=1\) coin the optimal return probability gains exactly \(256/2187\) over sharp three-step restarting.

The stated theorem is finite-latency, not an assertion about unrestricted waiting distributions or monitored hitting times. Independent scientific and publication-priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
