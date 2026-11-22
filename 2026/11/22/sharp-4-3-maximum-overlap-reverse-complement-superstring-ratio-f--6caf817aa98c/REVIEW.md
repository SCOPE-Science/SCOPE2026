# Research assessment

## Correctness

PASS. The ten orbit representatives follow directly from the reverse-complement involution. The optimal-cover checker enumerates every binary candidate of lengths four through thirteen; length thirteen is a proved global cap from the explicit all-class covering word. The greedy checker exhausts all ordered pairs and both reverse-complement orientations, retains every globally maximum-overlap transition, and takes the maximum terminal length. Each transition strictly decreases the number of components. Thus dynamic programming is exhaustive, not a finite sample or inference from a log. Two independently written executable implementations agree on all 1023 input cases, six maximizers, and the 31-cell joint table. The explicit small equality witness is directly inspectable.

## Originality

PASS against available primary text and retrieved records. Yamano–Shibuya (arXiv:2611.16573v1, November 12, 2026) give bounds for MGREEDY-RC and TGREEDY-RC, not the exact finite simple-GREEDY-RC worst-tie census; the March 2026 SCS-RC article is likewise general. The exact binary three-mer greedy result concerns ordinary SCS with no reverse-complement orientation. The ordinary binary four-mer full-set spectrum answers a different instance/algorithm question. Reverse-complement covering constructions give optimal full-coverage words but not all 1023 greedy outcomes. Full-text comparisons were made where accessible; some related records could only be compared from retrieved summaries. Possible unindexed previous exhaustive enumerations remain a risk.

## Value

PASS. Binary four-mers provide a canonical complete first nontrivial fixed-width reverse-complement testbed, with exactly ten irredundant orientation classes. The exact gap \(4/3\), its six and only six worst inputs, and the full optimal-versus-greedy distribution identify where tie-breaking loses compression, and distinguish simple greedy from cycle-cover-based heuristics. This is a complete natural finite classification, not an arbitrary small counterexample or a claim to general asymptotic improvement.

## Limitations

No broader approximation ratio, no treatment of double-stranded four-base DNA, and no external independent review. Other unindexed finite tables might overlap.

Self-review: passed. Independent audit: not yet performed.
