# Review of the dyadic Narayana zero-count theorem

## Correctness — PASS

The complete recurrence is specified, including initial zero terms and the precise least-period convention. Matrix powers at exponents \(7,14,28\) are displayed and are checkable by integer multiplication. They prove \(T_k=7\cdot2^{k-1}\) via matrix-order lifting and cyclicity of the initial state. The even-modulus zeros split into three congruence branches modulo seven. For the two nonsingular branches, the change on adding one period is a unit multiple of \(2^k\), forcing a unique lift. On the singular branch, the binomial expansion of \(M^{28}\) yields a well-defined \(2\)-adic function whose odd linear coefficient and eight-divisible Lipschitz remainder prove an isometry with one odd root. The two separated congruence classes of zero parameters contribute exactly eight indices for every \(k\ge6\). The finite initial counts are covered by the exact checker.

The proof is infinite; finite computations corroborate its explicit identities and base cases rather than replacing the lifting or isometry arguments. Remaining mathematical risk is principally the correctness of the displayed coefficient congruences; both the companion matrix calculations and direct sequence iteration were checked.

## Originality — PASS within inspected sources

Guadalupe (arXiv:2112.06187, 2021) explicitly establishes **3-adic**, not 2-adic, valuations of Narayana numbers. Kirthi (arXiv:1509.05745, 2015), inspected in its source PDF, studies periods **modulo primes** and cryptographic correlation properties; it gives no higher 2-power zero count. OEIS A271953 lists modular periods, not the eleven-zero stabilization. Lin (2021) studies negative indices and convolution formulas. Sobolewski (arXiv:1702.05819, 2017) determines 2-adic valuations for even-order full-support generalized Fibonacci recurrences; the zero-coefficient Narayana recurrence is not covered by that formula. These distinctions concern theorem implications, not just source titles. No earlier equivalent was found in the documented searches; unindexed equivalent results or overlooked applications of general analytic methods remain possible.

## Mathematical value — PASS

The constant zero count after modulus \(64\) is an exact and non-obvious invariant for a canonical third-order recurrence, across an infinite tower of moduli. The proof explains both the stable three ordinary lifts and the exceptional eight-fold branch through a new 2-adic isometry. It supplies precise arithmetic data not derivable from a period table alone, and naturally complements the existing odd-prime valuation studies.

## Scientific limits

No exhaustive historical search is possible. The finding does not give pointwise valuation formulas for all indices or complete residue distributions. Independent mathematical validation has not taken place.

Self-review: passed. Independent audit: not yet performed.
