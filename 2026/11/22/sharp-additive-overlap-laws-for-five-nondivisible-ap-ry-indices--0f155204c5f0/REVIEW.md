# Independent mathematical audit

## correctness

PASS

The frozen theorem is correct. The digitwise Apéry congruence selects {0,2,4}; independently one obtains the digit factorization from binomial Lucas by noting that the first carry in n+j makes (n+j)'s digit smaller than j's digit there, killing that summand. The nonzero summands factor over the carry-free choices. For the frozen counting argument, each even output digit forces the outgoing carry to equal the parity of shift digit plus incoming carry. Enumerating input 0,2,4 gives the displayed weights, including both neutral transitions. Odd shifts cannot match by parity. Even shifts return to carry 0, so all r-L later digits are free. In the repaired RESULT the independent balanced-digit proof gives the same count: no even-shift witness can overflow at r>=L because its leading digit would be 1. The distinct r-place words over {-2,-1,0,1,2} fill [-(5^r-1)/2,(5^r-1)/2] by reducing modulo 5 and counting. At fixed h/2, each digit difference delta has exactly 3-|delta| realizations as a difference of two digits in {0,1,2}. The normalized factor is therefore 1, 2/3 or 1/3. One absolute-one digit gives the maximum; two give the runner-up, whose leading sign is positive and whose lower sign is free, giving exactly the stated sum and difference families; an absolute-two digit or three absolute-one digits is strictly worse. This also checks the ordinary-digit rewrite and the zero-density distinction. Independently ran /workspace/branches/independent_checks.py: direct binomial sums for n=0..249 and every shift 0..124 at depth three agree. The frozen checker was read, not run; the bounded replay is not the all-shift proof.

## originality

PASS

This is a fresh PASS for the narrowed extremizing-displacement claim in repairs/2/RESULT.md, not a PASS for originality of the frozen all-shift count as advertised. The normalized finite count specializes the earlier sparse deleted-digit intersection recurrence and terminating-translation results. The repair credits that fact, uses a self-contained balanced-digit derivation as background, and claims only the explicit two highest nonzero shift levels and their exact inverse classifications. Neither a one-point automaton nor the inspected general recurrence states those order statistics or which positive displacements attain them. The repair determines them by analyzing the factor levels, the possible support sizes and signs of all balanced words, and their integer translations; it is not a recomputation for selected shifts.

## value

PASS

The repaired result answers which positive displacements retain the most eligible indices and which form the next level once the first family is excluded. Ordinary density loses all this separation. Both the precise equality sets and their separation from every other displacement are useful features of the sparse-scale invariant; no value is claimed for rebranding the already-covered general intersection count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
