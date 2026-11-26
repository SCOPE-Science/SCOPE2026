# Independent mathematical audit

## correctness

PASS

For n>=2 let b count adjacent unequal pairs. The b incidences on zeros cover b−t distinct zeros, since exactly the centers of 101 are counted twice. Thus n−(b−t) replacements are allowed. Among the b potential swaps precisely two per such center are forbidden, without repeat swap positions even for overlapping occurrences. All allowed operations give distinct outputs by their changed-position sets. This gives degree n−t (also directly for n=1) and ball size one more. With k ones, choose c of the k−1 interior zero gaps to have length one, give all others two zeros, and allocate the residual n−3k+2+c across k+1−c variable gaps. Stars and bars yields the stated multiplicities and a geometric series in the number of gaps gives H(z,u). Spacing of starts and the words (10)^c followed by 1 and trailing zeros give exact support; at maximum c one must have k=c+1 for n>=3, with at most one extra zero in an exterior gap, giving the stated extremizers. Setting u=0 counts maximum-degree words. The small Fibonacci root stays simple and separated from other poles near u=1 for complex u; the nonzero amplitude and strict radius gap permit differentiating the simple-pole coefficient asymptotic via analyticity. Differentiating D(r(t),exp(t))=0 twice gives the two displayed cumulant slopes for d=n−t.

## originality

PASS

The graph and its edge total are prior; by the handshaking identity the leading mean 2/sqrt(5) is already implied and is not independent novelty. The supported distinct contribution is the local 101 identity for the combined degree, the exact degree spectrum refined by number of ones, sharp endpoints, and the variance coefficient, which are not supplied by the inspected edge totals or replacement-only degree polynomials.

## value

PASS

For a standard constrained edit graph, the histogram measures how one-error exposure varies by source and weight. The local characterization gives extremal neighborhoods and the variance gives a fluctuation scale neither determined by the prior mean nor by graph diameter. The distribution is for all lengths and usable for constrained-channel analysis without claiming a new packing bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
