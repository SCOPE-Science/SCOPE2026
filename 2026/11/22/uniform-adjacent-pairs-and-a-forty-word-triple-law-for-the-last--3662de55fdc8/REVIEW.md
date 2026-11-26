# Independent mathematical audit

## correctness

PASS

Verified the recurrence independently: (5q+r)! is 5^q q! times the product of the factors not divisible by five. After removal of trailing zeros, the latter contributes (-1)^q r! modulo five with a compensating 2^(−q), giving 2^q r! modulo five; stripping zeros leaves an even integer for all indices at least two, so this also gives the stated mod-10 formula. The auxiliary e_1=0 is legitimate for the five children of index one. Applying the recurrence twice gives the two-coordinate carry for residue 4 and all five triple rows. Independently recomputed the exhaustive finite certificate: for each of the 64 starting states (a,b,t), for j=0,…,624 evaluate e_(625q+j) by applying e↦e+t+γ_digit, t↦5t+digit modulo four to the four padded base-five digits of j. Evaluate the next exponent with j+1 and the same prefix unless j=624, when the prefix is (b,t+1) and the suffix is 0000. Tally each target pair and (625t+j) mod 4. Over all 4096 entries the minimum and maximum are 4 and 16; every row totals 625. A separate single-digit carry tally verified each column sum 5, pair counts 20 of 320 in every cell, and every triple entry equal to the indicator formula with counts 0,4,8,16 on 24,24,4,12 cells respectively. Uniform stationarity and subtracting the common minorant 4/625 from each entry of P^4 yield contraction by 369/625 every four levels. A base-five greedy cutoff gives at most four complete descendant blocks of each size; the geometric sum of their errors is O(N^(1−δ)), and sorting child indices by n mod 5 applies the same bound to triples. The table proves the exact tail exclusions, with positive density for each allowed word. The finite prefix also does not add forbidden words: the three triples starting at 2,3,4 can be checked directly, and the auxiliary index one handles starts 5–9. Read VERIFICATION.md and verify.py without executing the frozen script; its comparisons beyond full factorials through 500 use the digit recurrence, not independent large full-integer factorials.

## originality

PASS

The evidence supports the explicit consecutive factorial joint law, not the already known decimal digit recursion or single-symbol uniformity. The closest exact analogue shares every headline multiplicity but has a different cellwise distribution and a different underlying indexed sequence. This is a best-of-knowledge comparison of inspected sources, not historical certification.

## value

PASS

The three-symbol law is the first place the adjacent pair uniformity fails to extend to a joint independence law; the exact forbidden words, per-cell frequencies, and effective natural-density estimate quantify that failure. This is structural information about a familiar deterministic number-theoretic sequence, not just another prefix count or a restatement of automaticity. The rate is a valid sufficient rate, not claimed optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
