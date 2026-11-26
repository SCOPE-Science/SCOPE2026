# Independent mathematical audit

## correctness

PASS

For the empty labelled old base, decompose triples into per-new-vertex matchings (no repeated old edge), an internal linear triple system H, and optional witnesses for uncovered new pairs. A witness for ij must be fixed by both matchings, and simultaneous witnesses are legal exactly when no new-old pair is reused. To verify the limit, write a_n=I_n/I_{n-1}. The recurrence a_n=1+(n-1)/a_{n-1} gives the upper bound 1+sqrt(n) from the preceding lower bound; the increasing two-step map evaluated at a_{n-2}=s=sqrt(n-2) is s+2/(1+s)>sqrt(n), with n=1,2 checked directly. Thus the probability of prescribing k distinct consumed labels in one involution is asymptotic to n^(-k/2) for fixed k. In a compatible mixed factorial-moment expansion each old label is prescribed in at least two colours. If two distinct marked motifs use the same old label, it is prescribed in more than two colours: a repeated motif of the same pair of colours is excluded by the falling factorial, and different prescriptions at one label in an overlapping colour are incompatible. Such terms lose at least n^(-1/2). Disjoint motifs give independent Poisson limits of means 1 for common fixed sites and 1/2 for common transpositions (unordered endpoints), with bounded moments of every fixed order. At least three involutions must fix any repeated witness label; the probability of such a label is O_r(n^(-1/2)). Cauchy–Schwarz with the bounded second moment of the witness-choice polynomial makes the error negligible even under weighted counting. Truncation therefore justifies the no-common-edge indicator times the witness polynomial. Each fixed H and fixed subset of uncovered pairs has limiting weight exp(-m/2), giving the asserted law and conditional presence distribution. For r=5 two internal triples meet in one point (5 choices followed by one of 3 splits of the other four); a third is impossible, giving 2544 exp(-5). The nine r=3 patterns follow separately. The finite checkers and their recorded output are consistent supporting examples, not the proof of this asymptotic. No statement is made about witness-label independence, nonempty bases or growing r.

## originality

PASS

Credit the exact one-point matching correspondence and the general random-action machinery. The supported distinct claim is the fixed-arity simultaneous-extension normalization and limiting joint profile over an empty labelled base, obtained by combining a coloured coincidence limit with a separate constrained assignment reduction and packing-polynomial sum.

## value

PASS

Asymptotic factorization of independently chosen one-point diagrams fails already at two new points. The theorem separates the suppression from shared old edges from the gain from new-pair witnesses, and identifies how internal packings bias the limiting law for every fixed number of new vertices. It supplies both a normalization and a probability distribution for a natural counting problem, rather than isolated small coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
