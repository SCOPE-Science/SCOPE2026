# Independent mathematical audit

## correctness

PASS

For a fixed length n, a binary palindrome's complete observation is determined by (a,D010,D101), with a its zero count and b=n−a its one count. By reversal, D01=D10=ab/2; D001=D100=(b·binom(a,2)−D010)/2, and D011=D110=(a·binom(b,2)−D101)/2. Constant-letter patterns have binomial counts. Conversely the three coordinates are given observations. To compute them I scanned each literal palindrome from all n-bit strings (retaining leading zeroes). A 1 with x earlier zeroes contributes x(a−x) occurrences of 010, and a 0 with y earlier ones contributes y(b−y) occurrences of 101. This exact reduced signature and reversal filter are independent of the supplied direct-embedding and prefix-DP implementations, which I inspected but did not run. For n=1..13 each fiber is a singleton; at n=14 there are 116 singletons and six doubletons, with exactly the six listed pairs. In table order their reduced signatures are (10,50,30),(8,62,46),(8,60,48),(6,48,60),(6,46,62),(4,30,50). Thus there are 128 palindromes and 122 distinct profiles at n=14, not counting complement as an equivalence. Replay: python3 /workspace/review_evidence/palindromes.py; see palindromes.log. The exhaustive proof establishes no statement above length 14.

## originality

PASS

Best-knowledge pass for the exact lower bound across all palindrome weights and the complete first-layer census as a joint claim. The existence of a length-14 palindrome collision is already known: Angal et al., Remark 3.2, give the identical first pair with the stronger 4-deck equality, which also gives the last listed pair by complement. The same-day four-one classification additionally determines the weight-4 and, by complement, weight-10 layers through length 14. Neither source supplies global injectivity below length 14 or the remaining four doubletons of weights 6 and 8. No originality credit is given to the overlapping witnesses or those restricted layers.

## value

PASS

The useful gap is the exact reconstruction boundary under natural reversal symmetry across all weights, not existence of a collision, which is already known. Verifying no earlier collisions and classifying the entire first ambiguous layer shows four additional pairs at weights six and eight beyond the known pair and its complement, with all remaining profiles singleton. That supplies a precise finite benchmark for palindrome-constrained deck reconstruction, rather than another example or an arbitrarily truncated unrestricted table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
