# Scientific review

## Correctness

PASS. The greedy-arch equivalence gives precisely the length-\(2k\) universal words \(\{01,10\}^k\). The four-state pair transfer checks every newly created length-four window; the six orbit representatives and their rational generating functions follow by finite, explicit matrix algebra. The simple/double pole analysis yields the five growth rates. An exact integer-polynomial checker validates all sixteen rational identities; exhaustive enumeration and separately implemented subsequence tests provide finite cross-checks, not substitutes for the infinite derivation.

## Originality

PASS with residual bibliographic risk. The nearest foundation is Barker et al. (arXiv:2003.04629), which already supplies the shortest-arch characterization. Adamson (arXiv:2304.04583) treats unrestricted counts, while Adamson et al. (arXiv:2311.10658) provide a general regular-language counting algorithm. None of the relevant material inspected states the complete six-rational-function classification or identifies the five growth regimes for a single forbidden four-symbol contiguous factor. The general algorithm is not confused with an explicit evaluated classification. The `0000` case, classic Fibonacci/Padovan numerical sequences, and the transfer technique are not claimed as individually new. Equivalent treatments outside the inspected sources remain possible.

## Mathematical value

PASS. The shortest words provide the minimal-length edge of subsequence-universal coding; a single local forbidden window models a strictly local constraint. The exhaustive natural length-four pattern classification is the first short case displaying more than the trivial unrestricted, linear, and Fibonacci-type behaviors, including distinct non-Fibonacci algebraic growth constants. Every positive universality level is covered. This is an exact structural characterization of a meaningful constrained-code family, not an arbitrary finite table.

## Limits and sources

The theorem is confined to one four-symbol contiguous forbidden factor and words of minimum possible length. The printed proofs and the standalone checker make these boundaries explicit. Primary sources: Barker et al. (2020), Adamson (2023), and Adamson et al. (2023). The relation to classical OEIS values is a numerical coincidence, not a prior identification of these constrained combinatorial objects. No independent external scientific audit has been undertaken.

Self-review: passed. Independent audit: not yet performed.
