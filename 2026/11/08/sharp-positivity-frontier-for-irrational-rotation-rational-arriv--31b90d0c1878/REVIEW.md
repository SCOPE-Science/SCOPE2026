# Scientific review: sharp positivity frontier for irrational-rotation rational arrival processes

## Correctness — PASS

For the precise three-coordinate matrices and all integer orders, the proof starts from the exact density formula in Peralta's Lemma 2. Its partial sums have two distinguishable forms: \(W_m=\operatorname{Re}(A(1-z^m))\) for nonterminal indices and \(W_k=\operatorname{Re}A-\operatorname{Re}(Bz^k)\) at the terminal index. The key strict inequality \(|A|>|B|\) makes the critical parameter itself admissible even though the infimum of the normalized densities is zero. Summation by parts proves the lower bound for arbitrary nonnegative delays, and dense irrational rotations together with an isolated long final delay prove sharpness over all orders. Normalization and the finite-dimensional non-Markovian obstruction are explicitly identified as results already established in the motivating paper. The standalone finite diagnostic passed 50,694 assertions; those checks are not being mistaken for a proof of the all-orders statement.

## Originality — PASS, subject to historical-priority risk

The closest directly relevant full primary source is Peralta, arXiv:2603.28047v1 (2026-03-30). Proposition 4 uses the explicit sufficient cutoff \(\varepsilon<1/(1+M)\); neither a necessary cutoff nor strict admissibility of the sharp endpoint is stated. The new conclusion is the exact infimum \(1-\varepsilon/\varepsilon_\star\), the necessary-and-sufficient amplitude range, and critical endpoint. This is a proper strengthening of that paper's positivity lemma, not a reassertion of its non-Markovian counterexample. Searches for exact positivity amplitudes, irrational-rotation RAPs, and related terminology did not establish a previously published result with the same conclusion. Classical general RAP theory might contain a more general cone-positivity result that could indirectly imply the extremum; the older 1999 and 2022 sources were accessible only through their bibliographic descriptions and are not certified as excluding every implicit specialization.

## Value — PASS

The allowed perturbation amplitude is the natural exact admissibility parameter of a recently introduced and explicitly specified non-Markovian point-process construction. A purely sufficient small-perturbation bound leaves unclear how much signed rotational structure can be supported before a negative joint density appears. The theorem resolves that structural boundary for every irrational rotation angle, including the nontrivial fact that all finite-order densities remain strictly positive at the critical endpoint. At \(\varphi=\pi/\sqrt 2\), it expands the rigorous admissible interval from a previously supplied sufficient cutoff of approximately \(0.184953749154\) to the sharp cutoff \(0.526915669239\). This exact classification may be useful when choosing non-Markovian synthetic arrival models without an arbitrary safety margin; no additional applied performance claim is made.

## Scope and residual risks

This is a narrow exact classification for the published three-state family, not a general characterization of rational arrival processes. The essential irrationality hypothesis cannot simply be dropped. Non-Markovian nonrealizability and probability consistency are inherited from the original source, with their hypotheses checked for the enlarged admissible interval. It remains possible that general earlier positive-realization theory contains a stronger theorem whose specialization implies the formula; no such implication was identified from inspected evidence. An independent mathematical audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
