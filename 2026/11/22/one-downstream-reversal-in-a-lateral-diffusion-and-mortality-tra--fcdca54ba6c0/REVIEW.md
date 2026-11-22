# Scientific review

## Correctness — PASS

The single claim is the terminal lateral-side-and-survival probability comparison for two homogeneous Gaussian drift scenarios. It has a complete proof: the normal-tail integral gives the exact delivery probability, a strict Gaussian Mills bound makes the logarithmic probability ratio strictly decreasing when lateral access favors one design but travel mortality favors the other, and endpoint limits imply exactly one transversal crossing. Implicit differentiation proves the comparative statics; normal-tail expansions prove both sharp asymptotic exponents. The full domain, normalization, ties, and omitted physical processes are stated in RESULT.md. The standalone executable `check_crossing.py` reproduced 38,011 supporting numerical checks; the proof does not depend on the finite tests.

## Originality — PASS on inspected evidence

The cited 2024 larval-drift study uses two-dimensional particle tracking to evaluate spawning-to-nursery connectivity, not a two-design theorem in downstream reach length. The 2021 mortality/diffusion study compares complex spatially varying mortality fields and long-duration settlement and does not identify this exact all-parameter crossing. A publicly available mathematical work on advection–dispersion first-arrival distributions treats **first-passage CDFs at common times**, rather than normal terminal side probabilities multiplied by independent survival to design-specific arrival times. Classical error-function formulas and Gaussian-tail inequalities are expressly credited as prior tools, not novelty. Relevant mathematical searches did not identify the combined parameter classification and sharp two-exponent limit; search absence is not an absolute priority guarantee. Older or nonindexed results might cover this elementary-kernel comparison.

## Value — PASS

Lateral access and survival are opposing bottlenecks in larval transport. A model containing both permits two river configurations to reverse their relative success with nursery distance despite each design's hydraulic/mortality parameters remaining fixed. The complete **one-and-only-one** reversal classification rules out multiple design switches in this benchmark and distinguishes weak- from strong-mortality-penalty scales (exponents \(2/3\) and \(1/2\)). This is a motivated structural benchmark for interpreting and testing richer connectivity simulations, not a relabeled one-variable maximum or a claim about actual river management efficacy.

## Scope and residual scientific risks

The idealized lateral coordinate is unbounded, there is no directed lateral swimming, mortality is uniform within each design, travel time is deterministic, and the nursery occupies the side of a transect past a fixed lateral threshold. The probability describes being alive on the nursery side **at the downstream transect**, not literal larval settlement or long-term population persistence. Historical mathematical priority remains unverified beyond the inspected works; extensions to bounded/heterogeneous channels are unproved.

Self-review: passed. Independent audit: not yet performed.
