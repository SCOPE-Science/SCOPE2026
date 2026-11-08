# Scientific review

## Correctness — PASS
The one-sided differentiable exponential generator integrates to zero and has squared Fourier multiplier \(a^2\omega^2/(a^2+\omega^2)^2=\operatorname{sech}^2(\log|\omega/a|)/4\). Uniform periodization gives sharp Plancherel frame bounds. The strict global maximum/minimum and monotonicity of the periodized kernel follow from an exact DLMF elliptic-series representation, whose derivative has the correct sign on the entire half-period. For any non-half phase, sampling the long-gap midpoint proves its lower bound is strictly smaller, while sampling a bank center proves its upper bound is strictly greater. At half phase both bounds follow from a single finer periodization. Large-spacing tail dominance and small-spacing first Fourier harmonic give the constants and rates. Standalone numerical integration and identities pass 486 finite checks; these are corroboration, not an infinite certificate.

## Originality — PASS relative to inspected sources
The full mathematical text of Pedersen–Lindeberg–Gerstoft, arXiv:2609.17201, §§3–5, treats finite differences of exponential smoothing kernels in finite scale banks with a lowpass residual, and computes their frame constants and channel overlaps, without a two-offset infinite derivative-bank minimax. The companion arXiv:2605.09770 and Lindeberg (2026) concern different finite banks or infinite-cascade kernels. The general equally-spaced circle-polarization theorem of Hardin–Kendall–Saff (2013) requires a convex geodesic potential; the current potential is concave at its peak, and that theorem does not yield simultaneous upper- and lower-bound constants. The DLMF hyperbolic/elliptic sum is an acknowledged classical ingredient. Targeted mathematical-record searches found no statement dominating the complete claim. Search absence alone does not prove novelty. Residual risk: equivalent general two-point rearrangement results, or unindexed causal wavelet frame optimization.

## Mathematical value — PASS
Sharp nonasymptotic frame extrema for causal continuous-translation two-bank designs determine which relative scale phase optimizes reconstruction stability for every geometric ratio. The exact elliptic constants and the sparse \(\sqrt q\) versus single-grid \(q\) conditioning growth, plus exponentially near-tight dense limit, quantify a meaningful reconstruction/spacing tradeoff not available from qualitative frame existence or a generic periodization formula.

## Limits
Fixed wavelet family and equal channel gains; all two-sided integer log-scale indices; no finite-bank or sampled-time implementation bounds. No claim to independent originality certification. Full original mathematical proof is in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
