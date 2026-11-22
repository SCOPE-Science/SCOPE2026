# Self-review

## Correctness — PASS
Every nilpotent map has directed-path orbits, strictly monotone by chain-order preservation and confined to one parity class. A maximum-length orbit exhausts its class and necessarily steps by two. The fence adjacency and parity requirements force any additional source to obey that same translation. Odd dimensions give two disjoint Boolean families; even dimensions give two per direction with one full-translation overlap. This proves the all-size index bound and both domain-rank enumerators. The attached `verify.py` exhaustively enumerates all admissible maps and checks actual zero powers in sizes three through ten. Finite checks are corroboration and do not replace the proof. The low-dimensional boundary \(n<3\) is outside the theorem.

## Originality — PASS relative to sources inspected
Sareeto–Koppitz's papers establish the membership criterion and generating rank, a presentation, and ideal/maximal-subsemigroup structure, respectively, rather than the power-index extremizer locus. The closest whole-monoid cardinality result counts maps without least zero powers. The partial-isometry nilpotence distribution does not rule out maximizers outside the isometries; the partial-contraction fixed-rank extremality result concerns another monoid and parameter. Searches for synonymous formulations and equivalent/stronger results found no decisive covering statement. Historical priority remains uncertain where sources are unindexed or older results imply the same claim indirectly.

## Mathematical value — PASS
The rigidity bridge is structural and produces a complete, natural infinite-family classification, including an exact Boolean-cube intersection phenomenon in even sizes, not just an ad hoc finite count. Both the exact maximum nilpotency index and its rank distribution are motivated natural power-map invariants of the previously studied inverse monoid.

## Closest literature and limitations
The full-text sources [arXiv:2208.03202](https://arxiv.org/abs/2208.03202), [arXiv:2310.15809](https://arxiv.org/html/2310.15809v1), and [arXiv:2403.06957](https://arxiv.org/abs/2403.06957) were inspected, alongside published published-finding corpus statements on cardinality, partial-isometry nilpotency and partial-contraction extremality. The theorem covers \(n\ge3\), maximal index only, and the two-sided fence- and parity-preserving inverse monoid. Finite verification covers sizes through ten only, and search cannot certify global priority.

Self-review: passed. Independent audit: not yet performed.
