# Scientific review: fixed-composition complement-deletion moment laws

## Correctness

**PASS.** For a word with \(m\) copies of a specified symbol and \(b\) other positions, the residual words obtained by deleting \(k\) copies are in exact bijection with bounded gap-deletion vectors; equal non-target letters do not change that bijection. This proves the polynomial coefficient formula, and uniform fixed-composition sampling corresponds to uniform weak compositions. Two rational generating-function identities prove all first and second moments, including the complete covariance matrix. Coefficientwise smoothing proves the sharp simultaneous bound, and Stirling's formula proves the \(27/32\) rate and its constant. Exhaustive mask-based tests and independently organized composition/series evaluations agreed on all documented finite cases. No finite test is used to infer the all-length statements.

## Originality

**PASS against inspected evidence; not independent historical certification.** The March 2026 primary paper defines complement scattered-factor sets and studies general algorithms and qualitative properties, without a fixed-composition mean, full second-moment kernel, or exponential extremal gap for repeatedly deleting the same symbol. The published two-distinct-letter deletion formula concerns \(ab\), not \(a^k\), and its independent-letter expectation does not determine the present fixed-content moments. The general deletion-pattern collision theorem already uses the balancing polynomial; Li–Wang–Fu likewise study balanced extremal **unrestricted** deletion spheres. Thus **the smoothing identity and balanced maximum alone are not claimed to be novel**. The novelty assessment concerns the exact conditional moment laws and their exponential comparison with the optimum. An equivalent result under composition or random product-of-chains terminology remains an explicit priority risk.

## Value

**PASS.** This is a complete all-length moment characterization for a natural subcase of a recently introduced combinatorial object. In the symmetric fixed-content ensemble, the exact base \(27/32\) proves that mean ambiguity is exponentially smaller than the largest possible ambiguity, while only a \((m+1)/\binom{2m}{m}\) fraction of words reach the maximum. This distinguishes worst-case and average-case behavior rather than reporting an isolated small numerical improvement. The scope is deliberately restricted to a monochromatic prescribed deletion; no conclusion about general deletion patterns or channel capacity is inferred.

## Related literature and limitations

Relevant primary work includes Adamson–Fleischmann–Huch (arXiv:2603.20790v1) and Li–Wang–Fu (arXiv:2601.06493v2). Relevant published comparison results are *A run-pair formula for two-letter complement scattered factors* and *Exact run-pattern collision thresholds and short-deletion extremal counts*. The main unresolved historical risk is that older product-of-chain or conditional-composition moment theory might imply the displayed identities in another formulation. The random source is uniform conditional on the number of distinguished letters, and the asymptotic comparison is for equal distinguished/nondistinguished counts. Finite checks are corroborative only.

Self-review: passed. Independent audit: not yet performed.
