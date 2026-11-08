# Scientific review: gamma maturation and Poisson-reset harmonic resonance

## Correctness — PASS

The object is the stationary periodic ensemble mean of an explicitly defined phase-selected two-state observable under Poisson resets. At every reset an independent gamma maturation clock is drawn, and the output remains zero until maturation. Independence of the mark and exponential backward age gives a rigorous renewal integral; the first Fourier coefficient of the selected square wave and a gamma Laplace transform yield the exact amplitude. A displayed quartic has the correct sign relation to the derivative, one positive root by Descartes' sign rule, and two vanishing endpoints, so the root is the unique global maximum. An explicit positive derivative in the gamma shape yields strict fixed-mean ordering. The polynomial scaling and its root structure imply both frequency limits; the amplitude coefficient follows by substitution. The deterministic comparison is a distinct limiting model with its own exact stationary equation. Independent symbolic algebra, gamma-CDF quadrature, and finite parameter tests passed. These tests are not a substitute for proof.

## Originality — PASS, qualified

The closest source is Wang et al., arXiv:2611.01991v1, particularly the general renewal response and equations (A1)–(A5) with its deterministic phase-dependent relaxation approximation. Their general response principle is prior coverage of the renewal-transform step and explains the already known low-frequency two-thirds exponent. The claim here is deliberately narrower and different: independently sampled gamma maturation with a fixed mean, global uniqueness for all positive shapes and frequencies, strict ordering under shape changes, and the shape-dependent high-frequency optimal-rate and amplitude exponents. The cited source's relevant main-text and supplementary passages do not state this classification. Radice, arXiv:2201.01829, treats gamma-distributed *time between resets* and noninstantaneous Brownian return, not post-reset maturation under Poisson phase selection. Earlier phase-based neuron resonance work concerns different state dynamics and does not provide a known implication of these gamma optimization statements.

Searches of indexed mathematical findings using the exact source, gamma/Erlang maturation, optimal reset-rate scaling, and equivalent renewal-response terminology did not locate a matching or dominating statement; an earlier indexed shifted-Erlang phase-response normalization result concerns a different feedback model and does not imply this optimization. The search result alone does not prove priority. A general unindexed Laplace-transform optimization theorem, or a more complete account of random activation in the cited literature, remains a material risk.

## Value — PASS

Uncertain relaxation time is a natural feature of coarse-grained reset-triggered phase selection. Keeping its mean fixed while varying the number or effective shape of activation stages isolates a physically meaningful variability parameter. The theorem does not just recalculate an amplitude: it supplies a global unique optimizer and strict variability ordering, and reveals a singular high-frequency distinction between any finite gamma shape (optimal rate grows linearly with frequency; optimal gain follows a shape-dependent power) and the deterministic-latency limit (bounded optimum). These are precise comparative predictions for the phase-selection response class, useful when optimizing reset frequency under uncertain activation kinetics. No statement is made about universal response in microscopic double-well dynamics.

## Residual limitations

The transfer identity follows from the general renewal method and is not independently original. The model assumes independent maturation and complete reset of unfinished activation. Its physical application requires checking those assumptions. Unindexed generalized optimality theorems may reduce the originality of the classification. No independent scientific validation has occurred.

Self-review: passed. Independent audit: not yet performed.
