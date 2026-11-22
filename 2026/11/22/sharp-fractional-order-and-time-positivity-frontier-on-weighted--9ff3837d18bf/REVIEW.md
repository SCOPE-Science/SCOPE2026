# Scientific assessment: weighted-triangle fractional heat positivity

## Correctness — PASS

For any positive triangle weights the exact spectral projectors reduce all off-diagonal entries of \(e^{-tL^\alpha}\) to two exponentials and a constant. The identity \(D^2-(S-3w)^2=-3(w-w')(w-w'')\) proves that only a uniquely weakest edge can have a positive high-frequency projector coefficient. Strict convexity of \(y^r\) then proves one and only one negative-time interval above the displayed unique critical order. Stochastic row sums give the exact induced maximum-norm formula, a single derivative zero gives the peak, and explicit spectral expansions give the two singular limits. The standalone checker gave 20,272 supplementary assertions; numerical tests are not substituted for proof.

## Originality — PASS, qualified

The closest background is Benzi–Bertaccini–Durastante–Simunec (2020), https://doi.org/10.1093/comnet/cnaa017, and Benzi–Simunec (2020), https://arxiv.org/abs/2012.08389. These establish the fractional graph Laplacian framework and preserve the Markov property for \(0<\alpha\le1\). Estrada (2021), https://doi.org/10.1088/1367-2630/ac14ac, discusses an unweighted triangle and other network comparisons, not the complete weighted superunit-order phase diagram. A published result on fractional heat over *unweighted noncomplete complete multipartite graphs* has different weight and graph hypotheses and does not imply the weighted complete triangle theorem. Mathematical-record searches for weighted triangles, a unique weakest edge, critical powers, order-time positivity, and M-matrix equivalences yielded no direct implication match. These observations support qualified best-knowledge originality; a specialist earlier classification of powers of three-by-three M-matrices remains an unresolved priority risk. A failed search is not a proof of novelty.

## Mathematical value — PASS

Weighted complete triangles are the smallest complete networks in which an order above one can destroy the positive semigroup property, while two-vertex complete graphs cannot exhibit that phenomenon. The result is a complete natural classification for *all* positive edge weights and *all* fractional powers, extending to an exact transient time window, sharp maximum-norm amplification and peak, and different logarithmic versus reciprocal critical-order divergences near symmetry. The precise positivity frontier matters for interpreting higher-order graph spectral filters as mass-preserving but potentially sign-indefinite diffusion maps.

## Limitations and residual risks

The theorem does not cover directed networks, zero conductances, or more than three vertices. The recovery time is an implicit unique root. Relevant historical graph-functional-calculus or M-matrix literature could contain equivalent unindexed results; the numerical script is supplementary and no external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
