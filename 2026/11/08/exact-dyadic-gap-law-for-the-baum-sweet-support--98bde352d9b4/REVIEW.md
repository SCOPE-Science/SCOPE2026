# Scientific review: exact dyadic gap law for the Baum–Sweet support

## Correctness — PASS

For each positive integer, the no-odd-zero-run property is equivalent to the unique prefix-free tile expansion \(1(1\mid00)^*\). In every fixed binary-length layer, immediate successors are obtained by replacing the final `00` tile with `1` and minimizing the tail; the two parity cases yield the displayed gaps. Fibonacci counts of valid prefixes give the exact multiplicities. The layer boundary is checked separately, including the initial zero. Summing the multiplicities and taking the standard Fibonacci ratio yields the limiting law. The `verify.py` program independently checks finite cases, but all infinite statements follow from a complete argument.

## Originality — PASS, qualified

Direct external comparisons included OEIS A060142, OEIS A086747, the original article's accessible bibliographic record, and Kimberling's related full-text 2000 self-generating-set paper. A060142 fully specifies the same set via closure, and A086747 specifies the same binary sequence via the zero-run condition, but neither inspected entry gives the numerical spectrum and Fibonacci per-layer counts of *adjacent* gaps or the limiting dyadic frequencies. Kimberling's article treats the genuinely different maps \(2x\) and \(4x-1\). Semantic database searches using the alternative `A060142`, `Baum–Sweet`, `odd-part compositions`, `first differences`, and `return-gap` terminology found no matching published claim. Priority remains qualified because sequence database entries, the original 1976 full text, and unindexed equivalent formulas may contain undiscovered coverage.

## Value — PASS

The finding is a complete all-length classification of a natural return-time statistic of a classical sparse automatic sequence, not an arbitrary finite cutoff or a re-tabulation of sample terms. It describes exactly which zero-block lengths can occur between consecutive ones, the multiplicity of each within each dyadic layer, and a nondegenerate limiting gap distribution. The elementary tile-succession mechanism explains a surprising mixture of exponentially separated allowed large gaps with Fibonacci-weighted short gaps. It can be used to study recurrence and gap sampling in automatic sets without enumerating their elements.

## Closest prior work and limits

The exact underlying set is already OEIS A060142; its equivalence with Baum–Sweet indices is explicitly recorded and must not be counted as new. The closest source's recurrence is necessary but does not directly state the complete gap law. The review does not establish absolute historical priority, arbitrary-cutoff convergence, or results for general gaps between non-adjacent support elements.

Self-review: passed. Independent audit: not yet performed.
