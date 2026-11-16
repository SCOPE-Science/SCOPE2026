# Scientific review

## Correctness — PASS
The exact path-word language consists of words avoiding adjacent ones, triples of zeros, and two-zero endpoint prefixes/suffixes. A three-state transfer reproduces it, with initial and terminal boundary vectors. Direct multiplication of the alternating sign block gives \(Bw=-w\), yielding an exact identity for every sign prefix. The path maximal-independent-set counts satisfy the Padovan recurrence; their seven-period parity is checked from three initial residues and recurrence uniqueness. All remaining residue classes have explicit seeds and their arbitrary seven-step extensions. Fourier diagonalization then makes zero-free equivalent to convolution invertibility. The computations in `check_path_mis.py` separately corroborate the formula.

## Originality — PASS under bounded comparison
Published graph-enumeration results establish maximal-independent-set counting and Padovan-type recurrences, not the simultaneous Walsh nonvanishing criterion. The closest inspected full texts [1]–[5] address extremal numbers, weak kernels, general domination polynomials, higher domination conditions, and caterpillar enumeration. Result comparisons are of implication: counting results alone do not determine which signed sums at individual frequencies cancel, and the present seven-letter transfer identity provides the missing witnesses. No equivalent theorem was found in the queries recorded in `AUDIT.json`. Published search coverage is incomplete, so an unindexed equivalence remains a priority risk.

## Mathematical value — PASS
The path's maximal independent sets are a canonical, nontrivial family of Boolean-cube subsets, also central to independent domination. Whether their group convolution is invertible is a naturally defined harmonic invariant not answered by knowing the number of such sets. The theorem gives a complete, exact criterion in every dimension, identifies the non-obvious modulus seven, and provides constructive witnesses in all singular cases. The universal sign-block law is structural rather than a finite table or a restatement of Padovan parity.

## Boundaries
The Padovan numbers and enumeration methods are prior work. No claim is made about the number of zero coefficients, arbitrary graph families, independent validation, or complete literature priority.

Self-review: passed. Independent audit: not yet performed.
