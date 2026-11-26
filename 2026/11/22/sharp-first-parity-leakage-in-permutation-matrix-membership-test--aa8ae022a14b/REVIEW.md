# Independent mathematical audit

## correctness

PASS

On the full assignment board, let T and F be the positive and negative cells of a trace. Inclusion–exclusion on F sums the signed completion count for each T union U with coefficient (-1)^|U|. Nonmatchings contribute zero, and for a matching leaving two or more rows free, swapping their images cancels the signed count. At n-1 cells only the full-support term can survive, with the stated sign and magnitude one exactly for a matching. For short traces with T a matching, the residual board of order m has at most m-2 forbidden cells; a one-factorization leaves at least two surviving completions, and cancellation supplies both parities. If the support is a matching, ordinary inclusion–exclusion produces the stated factorial count before dividing by two. A match of n-1 cells has only one all-positive completion, and its sign class lacks the trace obtained by making just one cell negative: the residual two-row switch has the other sign. Heredity and the all-positive requirement give the exact shattered supports and their matching-number polynomial. Littlestone dimension is bounded by the positive child at every root, a single sign class on the board of order n-1; induction from the n=2 singletons gives n-2, matching the VC lower bound. For a deterministic tree, an inconsistent leaf has no mass, a consistent short-support leaf has zero signed difference, and a boundary leaf has absolute difference at most one. Because each parity class has n!/2 members, TV is the sum of these absolute differences divided by n!; at most 2^(n-1) leaves are possible, and the nonadaptive matching has that many unit terms. Convexity handles independent randomization, and equal priors give the stated Bayes success. The unrestricted dimensions n-1 follow by the same positive-child induction and shattering a near-perfect matching (at most m-1 forbidden residual cells). The n=2 boundary has TV one and both dimensions zero. Source verifiers and stored outputs were inspected, not executed. Independent bitset checks (python3 /workspace/review_checks.py 1) exhaust all supports and responses through size n-1 at n=2..5, including nonmatching boundary supports, and check both online dimensions. Finite checks supplement the proof.

## originality

PASS

The credited transitivity, matching counts and edge-restriction comparisons are not stand-alone contributions. The supported distinct claim is the exact first signed Boolean trace and optimal bounded-query distinguishing law, together with the sign-class structural classification, on row-to-image queries. None of the matching statements inspected in the catalogue or compared in the frozen package supplies that combination or its first-depth TV formula. This is bounded evidence, not a claim of historical uniqueness.

## value

PASS

For a canonical permutation query model this identifies the first query budget with any statistical signal, computes the exact optimal signal and parity rule even against adaptivity, and describes what parity restriction does to the VC complex and online learnability. The leafwise signed boundary makes the result substantially more informative than a transitivity observation or a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
