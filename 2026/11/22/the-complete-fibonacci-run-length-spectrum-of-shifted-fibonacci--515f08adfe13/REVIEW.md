# Independent mathematical audit

## correctness

PASS

For m=F_a, the published Apéry representative mβ(r)+r gives the gap test β(r)>q at qm+r. The multiples of m separate the rows, so the runs in each thresholded word really are maximal in the semigroup. The Zeckendorf split B_a=B_(a−1) concatenated with (1+B_(a−2)) follows by using F_(a−1) and then a remainder strictly below F_(a−2). At each q≥1 the first entry of the second piece is a separator; its q=1 tail contributes exactly one block of length F_(a−2)−1 and its higher levels give the noninitial blocks from B_(a−2). The first piece contributes those from B_(a−1). The empty noninitial multisets at a=3,4 and this recurrence give the stated Fibonacci multiplicities, including a=5; q=0 contributes the unique initial block. Summation gives F_(a−2) blocks. An independent coin-change replay for a=10 scanned 1 through 275 and recovered the complete displayed spectrum; it is a finite cross-check only. The frozen verifier was inspected, not executed.

## originality

PASS

The supported distinct result is the full uniform maximal-gap-length histogram, not the Apéry theorem, known genus or isolated-gap count. The closest same-family record gives exactly the length-one component. The inspected prior inputs do not give the run recurrence or an equivalent all-length count; the uniform distribution uses the separating threshold boundary and a run-multiset recurrence, not just a fixed-parameter Apéry enumeration.

## value

PASS

Maximal gap blocks refine the established genus and isolated-gap invariants of a previously studied numerical-semigroup family. A uniform complete distribution tells which lengths occur and their frequencies, including the skipped penultimate Fibonacci length, without enumerating the semigroup. The threshold-word recurrence explains those facts and provides a reproducible structural reason for the Fibonacci frequencies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
