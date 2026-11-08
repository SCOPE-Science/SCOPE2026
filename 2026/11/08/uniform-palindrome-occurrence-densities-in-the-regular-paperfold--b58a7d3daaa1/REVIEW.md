# Review of uniform palindrome occurrence densities in the regular paperfolding word

## Correctness — PASS

The paperfolding bit at position \(n\) depends only on the odd part of \(n+1\). For each window of length at most \(15\), all entries except at most one are determined by its starting residue modulo \(32\). The exceptional bit is balanced within every residue class, so all \(64\) state pairs have natural weight \(1/64\). The full \(960\)-case finite certificate lists exactly \(28\) palindromic factors and their wordwise state counts, with none at lengths \(14\) or \(15\). Every longer palindrome contains one of those forbidden central lengths. The standalone checker returned `VERIFY_OK 2adic_states=64 lengths=15 state_cases= 960 palindromic_factors=28 direct_windows= 786432`. Finite direct sampling is not substituted for the congruence and density proofs.

## Originality — PASS (qualified)

The paperfolding theorem in Allouche–Baake–Cassaigne–Damanik, *Palindrome complexity*, arXiv:math/0106121, gives the known absence of palindromes longer than \(13\), not individual frequency or full starting-position rules. Frid–Laborde–Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934, examine a different statistic for the same word. Burns, arXiv:2210.14719, studies first appearance, and Fici–Shallit–Simpson, arXiv:2407.10564, study palindromic periodicity. Material from the relevant primary full-text sections was inspected. Exact-paperfolding searches and available prior-claim comparisons did not locate an equivalent density table. These are comparisons of implications, not just of titles; a nonindexed equivalent is still possible.

## Mathematical value — PASS

A complete exact distribution for every palindrome in a canonical automatic word determines more than the known length spectrum or total palindrome-complexity function. Equality of density for every pair of palindromes of the same length is a nontrivial symmetry, and the residue/exceptional-bit rule supplies a uniform position-level characterization with no finite-prefix restriction. The statement is deliberately limited to the regular paperfolding instruction sequence.

## Limitations

The result makes no assertion for general folding instructions or all arbitrary factors. The exhaustive finite state count rests on the stated reduction, and a human independent audit remains to be performed. An unindexed covering theorem may exist.

Self-review: passed. Independent audit: not yet performed.
