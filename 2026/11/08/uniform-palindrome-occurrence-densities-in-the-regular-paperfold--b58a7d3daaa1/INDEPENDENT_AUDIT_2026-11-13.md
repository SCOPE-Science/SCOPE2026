# Independent mathematical audit

## correctness

PASS

The odd-part definition makes every symbol with argument m not divisible by 16 depend only on m modulo 32; any length≤15 window contains at most one multiple of 16. Therefore 32 residue classes times one exceptional bit give an exhaustive 64-state finite representation. Each of the two exceptional values has conditional density 1/2 by odd-part valuation residues, giving state weight 1/64. Independently computed all 64×15 windows and their reverse tests: exactly 28 palindromic words at lengths 1,2,3,4,5,6,7,9,11,13, with multiplicities respectively 32,16,4,8,4,2,2,2,1,1 per word and none at 8,10,12,14,15. Any longer even/odd palindrome contains centered length14/15, so none occur. This is an exact exhaustive finite-state certificate linked by a proof to infinite factors, not a finite-prefix extrapolation.

## originality

PASS

The 2001/2003 Allouche–Baake–Cassaigne–Damanik primary article establishes the absence of paperfolding palindromes of length≥14 (Theorem 4), a bound explicitly credited here. Its Section 4.1 does not give individual finite palindrome occurrence densities or exact residue-state positions. Resultary searches find related generalized-paperfolding run frequencies and exact palindrome statistics for other automatic words, but no independent prior 28-word individual table of this specified regular paperfolding word. The exact 64-state weighted occurrence classification is thus a distinct best-of-knowledge invariant.

## value

PASS

Exact natural densities of all 28 named palindromes and a position-level congruence rule are a natural finer invariant than palindrome complexity. Equal frequencies within each length reveal specific arithmetic symmetry; this complete classification of a standard automatic sequence is a potentially reusable exact dataset, not merely an arbitrary small-slice statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
