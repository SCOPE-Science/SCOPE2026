# Scientific review: exact palindrome-pair complexity at Thue–Morse tetradic lengths

## Correctness — PASS
The claim and scope are explicit for every nonnegative integer \(k\). The upper bound is an actual all-length proof: cyclic reversal symmetry implies six-factor histogram symmetry; the finite local table excludes a mismatched partial block; unique decoding of the palindromic four-letter blocks descends any permissible palindrome-pair factor from length \(4m\) to a rotation of a permissible factor of length \(m\). The two length-three classes close the induction. Squares found at explicit positions give every rotation, and unique block decoding establishes primitiveness and class separation. Both included checkers independently passed. Finite tests are corroboration of the symbolic lemmas, not substitutes for induction.

## Originality — PASS, with stated residual risk
Borchert and Rampersad (2015, Proposition 11) prove the same lower bound but not equality and explicitly request exact complexity formulas. Bell and Shallit (2021) study full conjugacy classes; their Lie-complexity count does not exclude partial palindrome-pair classes, whereas the new local six-factor obstruction does. Searches by factor, parameter, palindromic-pair synonyms, conjugacy, morphic descent and known lower bound found no covering theorem in the accessible literature or indexed research findings. The possibility of an unindexed equivalent result remains.

## Value — PASS
The result closes a published lower bound exactly on the infinite, natural family of lengths \(3\cdot 4^k\), supplies complete extremizer classes rather than a numerical count alone, and introduces a reusable local morphic-descent obstruction. It is neither a finite table nor a substitution of known parameters into a stronger published theorem.

## Limitations and closest literature
The theorem does not give the palindrome-pair complexity for all positive lengths. Historical priority is provisional and independent mathematical validation remains unperformed. Closest primary reference: Borchert–Rampersad, *Words with many palindrome pair factors*, arXiv:1509.05396v1, Section 3 Proposition 11 and conclusion. Related but nondominating: Bell–Shallit, *Lie complexity of words*, arXiv:2102.03821.

Self-review: passed. Independent audit: not yet performed.
