# Scientific review

## Correctness

**PASS.** The proof handles all nonnegative \(k,r\), defines the scattered-subsequence complement precisely, and proves necessity from the three-valued prefix-balance bound and sufficiency by inserting one deleted \(01\) pair around each maximal \(10\)-run. Counting \(2j\) run boundaries among \(r+1\) positions gives the exact binomial sum. Edge cases \(k=0\), \(r=0\), and equality at \(r=2k\) are included. Exhaustive deletion-set and independent shuffle-DP checks agree on the cited finite ranges. The proof does not rely on extrapolating those computations.

## Originality

**PASS with explicit residual risk.** The relevant full HTML of Adamson–Fleischmann–Huch, arXiv:2603.20790v1 (2026-03-21), was inspected in its definitions, algorithmic section, combinatorial results and conclusion. It supplies a general algorithm and special singleton/self-shuffle results but not the present sharp run-budget characterization or closed cardinality formula; the conclusion explicitly identifies case-specific closed formulas as open. Distinct-remainder enumeration, rather than the much easier embedding count, is the substance of the claim. Related alternating-riffle/Gilbreath theorems concern different input hypotheses and do not yield the required minimum number of deleted alternating pairs. Published mathematical-record and primary-literature searches of the stated formula, aliases and possible stronger coverage found no identified prior implication, but this is not proof of historical uniqueness.

## Value

**PASS.** The precise problem of giving a closed formula for complement-scattered-factor counts in natural cases is explicitly motivated in the March 2026 paper. The alternating binary family is an elementary canonical test case with two independent length parameters. The result provides a complete description of all outputs, exact counts and a sharp phase transition between partially and fully attainable paired outputs, rather than merely evaluating a fixed small case. It also exposes the minimum deletion budget for each output through its \(10\)-run statistic.

## Boundaries and risks

Only aligned alternating binary host/pattern pairs are addressed. No claims are made for arbitrary words, embedding multiplicities, or larger alphabets. The old shuffle/Gilbreath literature could contain an equivalent formulation that was not indexed in the accessible search; independent mathematical and historical review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
