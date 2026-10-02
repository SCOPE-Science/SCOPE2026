# Independent scientific audit — 2026-10-01

**Disposition: FAILED — not a validated finding.**

## Final claim assessed

For the specified inhibitory LIF/Fokker-Planck operating point, gamma-distributed delay dispersion moves the approximately 65 Hz linear Hopf crossing from unstable to stable near sigma_D=1.1 ms and matched finite spiking simulations show quenching of the collective gamma peak.

## Correctness — PASS

The critical linear-stability calculation was independently reconstructed from the filed Scharfetter-Gummel discretization rather than trusting its table: at N=600 the stationary rate is 10.532641 Hz and self-consistency gives mu0=15.360830 mV. Evaluating the filed susceptibility at the reported crossing frequencies gives imaginary loop gain approximately zero and J_c=-541.994, -568.586, -590.900, -602.124, -605.114, -621.665, -663.010 mV for sigma_D=0,0.75,1.0,1.1,1.125,1.25,1.5 ms, matching the claim and bracketing -600 mV between 1.10 and 1.125 ms. The archived finite-network sweep is consistent with the claimed peak collapse, although that long simulation was not rerun in full during this audit.

## Originality — PASS

The general phenomenon of delay-driven oscillations in inhibitory integrate-and-fire networks is classical, but the exact gamma-distributed-delay dispersion threshold for this stated Scharfetter-Gummel operating point was not found in Resultary or the inspected primary literature. This is therefore best-of-knowledge exact-instance originality, with the usual residual risk from an incomplete literature search.

## Scientific value — FAIL

The precise threshold is for one hand-picked parameter vector and discretization, with no prior mathematical or neuroscientific motivation for why this exact parameter cell is a natural boundary or an invariant a future researcher would need. It is a reproducible numerical slice of a known delay-oscillation mechanism, not a classification, sharp general cutoff, or structurally motivated counterexample. Correctness and exact-instance novelty do not by themselves supply value.

## Originality checks

### equivalent_formulations

The record is a numerical frequency-domain stability calculation for a distributed-delay kernel; no equivalent published exact threshold was found.

Evidence: Resultary returned this record as the exact threshold match.; Brunel-Hakim 1999 studies fast global oscillations in inhibitory integrate-and-fire networks.

### broader_coverage

The broad mechanism is prior, while the exact parameter-specific threshold appears new as a computation.

Evidence: Classical literature covers asynchronous/oscillatory states and delay-driven oscillation mechanisms, but not the exact stated gamma-delay dispersion table.

### exact_database_or_table

Best-of-knowledge exact-instance originality passes, but this does not establish scientific value.

Evidence: Only the audited record matched the exact parameter table in Resultary.

### claim_vs_prior_implication

The exact threshold requires a fresh numerical solve and is not a direct closed-form corollary of the inspected sources.

Evidence: Those primary papers establish the general oscillatory setting but do not mechanically imply the gamma-kernel threshold without solving the record's susceptibility equation.

## Sources inspected

- Fast global oscillations in networks of integrate-and-fire neurons with low firing rates — https://pubmed.ncbi.nlm.nih.gov/10490941/: broad prior mechanism, not exact distributed-delay threshold
- Dynamics of sparsely connected networks of excitatory and inhibitory spiking neurons — https://pubmed.ncbi.nlm.nih.gov/10809012/: broad state taxonomy only
- Assigned package 2026/09/12/052 — https://github.com/SCOPE-Science/SCOPE2026/tree/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/12/052: linear threshold reproduced; finite-spiking archive consistent but not fully rerun

## Residual risks

- A more exhaustive distributed-delay neural-field/LIF search could reveal a prior identical numerical setup, but no such exact coverage appeared in the searches performed.
- The full finite-size simulation sweep was inspected but not independently rerun; the decisive rejection is instead on scientific value, which does not depend on that replay.
