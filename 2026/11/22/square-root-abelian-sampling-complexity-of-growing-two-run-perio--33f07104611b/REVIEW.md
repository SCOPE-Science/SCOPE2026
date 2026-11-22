# Scientific review

## Correctness — PASS
Each pattern corresponds exactly to a nonnegative vector of residue counts totaling \(k\). Translated one-counts are cyclic sums of \(h\) consecutive coordinates, with total sum \(hk\), giving the triangular-number upper bound. The explicit staircase has a nonnegative last coordinate and produces all counts \(0,\ldots,\lfloor\sqrt{2hk}\rfloor-h\). The result does not extrapolate finite enumeration into an infinite proof; 4,995 construction checks and 168 exhaustive finite instances are reproducible with the embedded program.

## Originality — PASS relative to inspected evidence
The 2013 foundational article treats Abelian maximal pattern complexity, principally recurrent aperiodic words. The 2026 Zeng–Xue–Zeng paper treats general aperiodicity and periodicity criteria, but does not state a uniform period-sampling phase law for binary consecutive-run periods. Related indexed work on periodic-marker extensions concerns different alphabets and aperiodic components; work on cyclic two-run factors concerns contiguous rather than arbitrary sampling. Literature and semantic database searches found no implication of this precise sharp joint-parameter result. Residual risk: an unindexed sliding-window-sum theorem may imply it.

## Mathematical value — PASS
The result addresses the natural quantitative gap between bounded complexity for each fixed period and varying periods. Its universal energy obstruction and explicit asymptotically sharp construction identify the exact leading scale and run-length-dependent coefficient uniformly across infinitely many periods, not a routine finite-case census.

## Limitations
No claim is made of an exact maximum at every finite parameter triple. Independent validation and general bibliographic exhaustiveness have not been established.

Self-review: passed. Independent audit: not yet performed.
