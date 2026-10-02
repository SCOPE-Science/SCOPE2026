# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `SCOPE-20260912-052`

An independent scientific audit on 2026-10-01 rejected the final claim for publication as a validated finding.

- Correctness: **PASS** — The critical linear-stability calculation was independently reconstructed from the filed Scharfetter-Gummel discretization rather than trusting its table: at N=600 the stationary rate is 10.532641 Hz and self-consistency gives mu0=15.360830 mV. Evaluating the filed susceptibility at the reported crossing frequencies gives imaginary loop gain approximately zero and J_c=-541.994, -568.586, -590.900, -602.124, -605.114, -621.665, -663.010 mV for sigma_D=0,0.75,1.0,1.1,1.125,1.25,1.5 ms, matching the claim and bracketing -600 mV between 1.10 and 1.125 ms. The archived finite-network sweep is consistent with the claimed peak collapse, although that long simulation was not rerun in full during this audit.
- Originality: **PASS** — The general phenomenon of delay-driven oscillations in inhibitory integrate-and-fire networks is classical, but the exact gamma-distributed-delay dispersion threshold for this stated Scharfetter-Gummel operating point was not found in Resultary or the inspected primary literature. This is therefore best-of-knowledge exact-instance originality, with the usual residual risk from an incomplete literature search.
- Scientific value: **FAIL** — The precise threshold is for one hand-picked parameter vector and discretization, with no prior mathematical or neuroscientific motivation for why this exact parameter cell is a natural boundary or an invariant a future researcher would need. It is a reproducible numerical slice of a known delay-oscillation mechanism, not a classification, sharp general cutoff, or structurally motivated counterexample. Correctness and exact-instance novelty do not by themselves supply value.

The original research files and computational evidence are retained for reproducibility and historical inspection. Their presence does not constitute validation. See the dated independent-audit files for the full source comparison and residual risks.
