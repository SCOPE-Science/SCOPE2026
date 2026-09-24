# Independent audit — low-order diagonal rational filters for |x|

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/047`  
**Audited source tree:** `5b2d77b5049fa86f67f76d37f31297e76d89d0f9`  
**Review type:** separate AI independent audit.

## Claim audited

The record gives short-decimal type-(2,2) and type-(4,4) even rational approximants to `|x|` on `[-1,1]`, certifies their sup-norm errors in narrow intervals, pads the first to type (3,3), and compares them with degree-3 polynomial approximation and Newman's explicit degree-2 construction.

## Correctness — PASS

I independently reconstructed the two rational error functions. For the printed type-(2,2) coefficients, the only interior stationary points on `[0,1]` are approximately `0.1914897276` and `0.6477891103`; together with the endpoints their error magnitudes are at most `0.0437000`, with interior extrema approximately `0.04367862` and `0.04369353`. For the printed type-(4,4) coefficients, the four interior stationary points are approximately `0.03793685, 0.14842090, 0.39716117, 0.77805616`, and the largest error magnitude is about `0.0085104264`, below the stated `0.00852` cap. The stated lower-node values are therefore consistent with the actual extrema, and denominator positivity is immediate from the nonnegative coefficients. Padding the type-(2,2) rational to type (3,3) is valid. The degree-3 polynomial comparator `x^2+1/8` has the stated five-point alternation and hence exact minimax error `1/8`. I found no mathematical error in the displayed certified bounds.

## Originality — FAIL

The contextual premise that existing Varga–Ruttan–Carpenter work supplies only high-type floating information is materially misleading. Their 1991/1993 paper *Numerical results on best uniform rational approximation of |x| on [-1,1]* explicitly determines the entire sequence `E_{2n,2n}` for `n=1,...,40` to at least 200 significant digits. Thus the exact low orders relevant here — types (2,2) and (4,4) — were already among the published best-approximation data decades earlier, at precision vastly beyond the `0.04367–0.04370` and `0.00847–0.00852` intervals in this record. Later work by Filip, Nakatsukasa, Trefethen and Beckermann gives robust ordinary-precision minimax algorithms for the same `|x|` problem, making these low-order approximants routine to regenerate.

The record's specific rounded decimal coefficients and elementary Sturm-style certification may be a convenient implementation artifact, but they do not constitute a new approximation-theoretic invariant once the actual minimax errors at these exact low orders were already published to 200 digits. The matched-degree polynomial comparison and Newman comparison are likewise direct post-processing of classical objects.

## Scientific value — FAIL

After subtracting the prior low-order minimax results, the residual contribution is certification of two rounded, non-optimal decimal approximants and two elementary comparisons. This does not improve the known minimax constants, provide a new algorithm, establish a new asymptotic or structural theorem, or cover a previously inaccessible degree regime. The certificates are correct and reproducible, but they primarily verify coarse surrogates for quantities already known much more accurately.

A bounded wording repair cannot restore the missing contribution: a scientifically distinct retry would need, for example, genuinely new certified minimax data not covered by the published tables, a new low-cost structural filter result, or a nontrivial theorem about coefficient quantization/certification rather than two rounded examples.

**Final disposition: FAILED — correctness passes, but the headline low-order constants are subsumed by prior exact-order minimax computations and the residual certification is not a sufficiently distinct scientific contribution.**
