# Scientific review

## Correctness — PASS
The domain is every prime \(p\ge5\) and every positive block depth \(L\); the \(z=0\) case is separate. The proof verifies the critical nonstandard fact that single-digit zeros are interior and isolated using the exact recurrence, the formal prime-power generating-function identity, and \(T_0=T_1=1\). It then derives every zero-run multiplicity from uniquely located forbidden blocks and every nonzero-run multiplicity from the exact count \(E_h\) of consecutive admissible prefixes. These are infinite, all-primes arguments, not inferences from finite testing. The standalone checker passed 125,867 exact recurrence-based index comparisons across all tested primes to 101 and block sizes to 15,000. Remaining correctness risk is independent verification of the combinatorial run-bijection; no independent audit is claimed.

## Originality — PASS within inspected evidence
Noe (2006) Theorem 8.5 and equation (13) already establish the base-prime digit criterion. Kohen (arXiv:2411.03681v1, 2024) Proposition 7 and Section 3 discuss the digit product, symmetry, and densities. Rampersad–Shallit (2022) treat congruences of related combinatorial sequences by finite automata. These facts are expressly credited: neither a digit product nor a mere density is novel here. The inspected material does not give the **complete maximal run-length spectra at every depth**, the exact high-prefix adjacency count, or the sharp global nondivisibility run bound for all primes. The closest related mathematical-record results concern different sequences, prime powers, or two-point residue correlations; none inspected implies the full claimed classification. Searches are not proof of priority, and an implicit preexisting formulation in word-combinatorics remains possible.

## Value — PASS
A primary research question for prime-divisible combinatorial sequences is how the zero positions are arranged, not just what their asymptotic density is. The exact classification reveals a strong dichotomy: either no terms are divisible, or zero runs of unbounded prime-power lengths coexist with a **uniform prime-dependent finite bound** on nonzero runs. Giving exact multiplicities of both kinds at each finite block depth is a natural complete invariant, with substantive structural content beyond pointwise Lucas factorization. This scope is not a generic arbitrary slice or an unexplained experimental count.

## Limitations and verification status
No classification of primes having nonempty single-digit zero sets is claimed; it is a separate question. Higher powers and arbitrary-index endpoints are outside scope. Priority against unindexed sources and formal independent verification remain open.

Self-review: passed. Independent audit: not yet performed.
