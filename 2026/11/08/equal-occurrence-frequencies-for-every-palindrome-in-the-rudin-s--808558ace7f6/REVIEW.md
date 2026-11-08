# Scientific assessment: exact Rudin–Shapiro palindrome frequencies

## Correctness — PASS

The argument proves a length-two state substitution from the adjacent-pair parity recursion, with four-step primitivity and exactly two incoming transitions per state. It then derives exact symbols of every factor of length at most \(16\) from one of \(128\) state/residue cases. The self-contained standard-Python checker exhaustively verifies all \(2048\) finite cases, the claimed factor/multiplicity lists, and exact long-factor occurrence sets. State frequencies of \(1/8\) imply each case occurs with density \(1/128\); absence at lengths \(15\) and \(16\) excludes all longer palindromes. The larger prefix tests are diagnostic, not the proof of infinitude.

## Originality — PASS, with bibliographic limits

The inspected generalized Rudin–Shapiro palindrome-length cutoff in Allouche–Baake–Cassaigne–Damanik (arXiv:math/0106121) and maximal-palindrome descriptions in Schaeffer–Shallit (arXiv:1508.02074) supply background but not the stated starting-position densities or equal-frequency law. Frid–Laborde–Peltomäki (arXiv:2009.02934) studies prefix palindromic decompositions, not factor frequencies. Searches for aliases and density/frequency formulations did not locate a covering result. This is not a claim that failure of search proves novelty: an unindexed equivalent may exist, and one historically relevant 1997 full text was not accessible in the consulted format.

## Mathematical value — PASS

Factor occurrence frequencies are fundamental dynamical data beyond palindromic complexity or length spectra. The result computes them exactly for every palindrome of a natural automatic word and proves the unanticipated equal-frequency property using uniform eight-state dynamics. It gives exact, reusable position descriptions for all \(36\) palindromes and distinguishes this property from arbitrary factors, whose frequencies need not match within a fixed length. The classification is complete, infinite-position, and structurally motivated; the already known palindrome cutoff is not presented as the contribution.

## Sources and limitations

The primary full-text comparisons were arXiv:math/0106121, arXiv:1508.02074 and arXiv:2009.02934. The result is restricted to the indicated binary coding. The checker is executable without external dependencies; independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
