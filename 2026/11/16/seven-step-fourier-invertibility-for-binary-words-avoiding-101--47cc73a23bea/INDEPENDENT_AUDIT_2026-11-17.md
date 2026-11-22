# Independent mathematical audit

## correctness

PASS

For length-n binary strings avoiding the ordinary contiguous factor 101, the three-state prefix automaton tracks suffix empty/1/10 with weighted transition matrix M(s)=[[1,s,0],[0,s,1],[1,0,0]], initial e=(1,0,0) and terminal all-ones. Its signed matrix product equals each genuine Walsh character sum. The unsigned count satisfies a_n=2a_(n-1)-a_(n-2)+a_(n-3), with A^7 congruent identity mod2 and residue parities odd exactly n mod7 in {0,3,5,6}; every coefficient is therefore nonzero in those classes. Explicit exact integer matrices C=BA^6, D=A^6B and identities L C=L, C R=R, D R'=R' prove the table of zero witnesses in residues {1,2,4} and multiplier-one witnesses in all others, for all k and short n including 1,2. The counting-convolution inverse norm on zero-free classes is exactly 1. Read frozen RESULT.md and actual CHECK.py, independently checked matrix products and entire spectra for n<=17. This is an all-length matrix identity proof; finite tests alone are not used as inference.

## originality

PASS

Earlier Bilotta–Grazzini–Pergola enumerations for avoiding alternating patterns constrain balance/#zeros and count by weight; they do not assert the Walsh spectrum for unrestricted 101-avoiding strings. The nearest published pattern-avoidance theorem for unbordered patterns cannot specialize to 101, whose length-one prefix/suffix coincide. The different '001' three-phase result is also a distinct nonoverlapping pattern and its residue period is three, not seven. New exact seven-step cancellation witnesses and full invertibility classification survive these statement-level comparisons.

## value

PASS

The unrestricted 101-avoiding language is a classical automaton-constrained binary code. A complete infinite periodic criterion for its all-character Fourier invertibility and an exact inverse norm supplies a meaningful spectral property not contained in its generating-tree enumerator, with constructive witness signs explaining the seven-phase obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
