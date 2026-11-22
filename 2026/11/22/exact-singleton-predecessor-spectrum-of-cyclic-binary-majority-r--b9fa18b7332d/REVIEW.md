# Scientific review

## Correctness — PASS

The claimed series follows from an explicit bijection between periodic preimages and length-matched closed paths in a four-pair de Bruijn graph, including ring sizes one and two. A saturated-at-two product correctly preserves whether a closed-path count is zero, one, or greater than one. The certificate checks all coordinates of an exact integer vector identity at exponent 21, establishing the recurrence at every subsequent exponent, and separately checks the initial polynomial numerator. Exhaustive direct enumeration for rings of lengths 1–16 independently agrees. Critical assumptions (labelled sites, the cyclic majority convention, one-step update) are explicit. Computation is used as a finite exact certificate and not as an unsupported extrapolation.

## Originality — PASS, with residual uncertainty

Jen (1989), especially pp. 441–442 and the appendix, establishes general predecessor-count methods for finite blocks with free boundaries. That is substantive prior foundation but does not give the all-target, periodic-ring singleton-count series. Powley–Stepney (2010) focuses on homogeneous target preimages. Turau (2023) addresses fixed points and two-cycles. The closest published cyclic Rule-232 enumeration counts all attainable targets, not the subset having exactly one predecessor; a published singleton enumeration concerns a different rule, Rule 54. The separate majority temporal-entry enumeration addresses a different invariant. Source and equivalence searches did not identify a dominating all-length singleton formula, but negative searches cannot prove universal priority. An unindexed equivalent theorem or a non-obvious consequence of earlier predecessor formulas remains possible.

## Value — PASS

The number of output configurations having a unique possible source is a natural finite-size exact reconstruction invariant for a classical nonlinear cellular automaton. Counting reachable outputs alone does not measure which ones can be inverted without extra information. The complete rational series gives every ring size in one theorem; the recurrence and its exact certificate also provide a reproducible benchmark for periodic preimage enumeration. It is more specific than a general classification theorem, but the precise all-length singleton output count is intrinsically meaningful rather than an arbitrary finite slice.

## Limitations

The work does not enumerate all preimage-fiber multiplicities, prove a general theorem for other elementary rules, or claim independent validation. The strongest primary comparison is the classical Rule-232 predecessor formula, whose boundary convention differs. Related published results were examined at the relevant sections; one historical homogeneous-preimage comparison was available chiefly through its detailed abstract and public excerpt. Priority remains subject to further literature examination.

Self-review: passed. Independent audit: not yet performed.
