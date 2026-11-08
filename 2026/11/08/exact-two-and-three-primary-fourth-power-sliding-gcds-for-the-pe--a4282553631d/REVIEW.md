# Scientific review: two- and three-primary fourth-power sliding Pell GCDs

## Correctness — PASS

The claim concerns the exact prime valuations of an infinite gcd, not the complete gcd. The proof gives an explicit integer quartic block \(F\) divisible coefficientwise by \(6\), the four-step matrix \(M\), and a precise integer-polynomial finite-difference expansion. The congruences for sums of \(4m\) terms hold for every starting index and every \(m\ge1\). The exhibited Pell and associated-Pell starting indices make the lower bounds sharp. Residual lengths are handled separately by exhaustive periodic residue patterns modulo \(2\) and \(3\). The finite replay in `verify.py` checks representative parameters and exact algebra; it is not offered as an infinite proof.

## Originality — PASS within checked evidence

The closest primary work is Mbirika–Schrader–Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, arXiv:2301.05758 (first public 2023-01-13). It defines all-power sliding GCD notation but proves first-power formulas and reports second-power values; sections 1 and 6 were checked directly in the complete publisher PDF. The new theorem gives exact \(2\)- and \(3\)-parts for the fourth power for both Pell sequences. Mbirika–Spilker, arXiv:2204.12626, treats squares for a different recurrence. Anand et al., arXiv:2407.12868, concerns consecutive unsquared terms and uses a different companion-sequence normalization. Search comparisons with related indexed research, distinct prime-adic Lucas periodicity results, and available historical claim statements did not identify a covering assertion. Novelty cannot be established by search absence; unindexed broader Lucas-power congruences remain a residual risk.

## Mathematical value — PASS

The result characterizes *all lengths* and all powers of \(2\) and \(3\) dividing two fourth-power sliding GCDs, rather than sampling a few exponents or lengths. It shows a sharp contrast between the companion pair at prime \(2\), while the \(3\)-adic valuations agree and arise precisely for window lengths divisible by four. The exponential-in-valuation divisibility is unbounded as the window length varies. It supplies a structurally explained, exact local part of the higher-power sliding-GCD problem motivated by the 2023 work, without claiming the full gcd at other primes.

## Limits and risks

No formula for primes \(p\ge5\) is established, and no complete fourth-power GCD is claimed. No universal statement for arbitrary second-order recurrences is claimed. Possible coverage by a general unpublished or unindexed theorem remains an originality risk. This is a self-review only, not independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
