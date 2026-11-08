# Scientific review: square-bouquet acyclic sink polynomials

## Correctness — PASS

The graph definition fixes each edge exactly once. Every simple cycle is a single square, so choosing acyclic orientations blockwise is a bijection. The local table gives the peripheral-sink polynomial \(T(z)=z^2+10z+3\) and the hub-sink subpolynomial \(B(z)=z+3\). Correcting the hub weight proves the claimed formula. Factoring through \(R(z)=T(z)/B(z)\) and comparing it with \((1-z)^{1/r}\) on four rigorously specified intervals proves both uniqueness and existence of each real root. The derivative bound for even \(r\), the pole \(-3\), the positive half-line, degree and simple zero at \(0\) have been separately checked. Direct orientation enumeration for \(r=1,2,3,4\) and exact coefficient checks through \(r=100\) are consistent with the proof.

The formula and root count hold for every integer \(r\ge1\); finite enumeration is only corroboration. No claim is made about the positions of the individual nonreal roots.

## Originality — PASS (historical priority provisional)

The 2026 primary paper arXiv:2610.41502v1, particularly Proposition 3.21 and Sections 3.1, 3.4 and 5.1, treats cycles, chordal claw-free graphs, and a different nonreal-rooted example involving a line graph. Its acyclic real-rootedness theorem does not apply to square bouquets: a single square is nonchordal, and bouquets with two or more petals also have induced claws. Its all-orientations real-rootedness statement concerns a different enumerator. Hwang et al. arXiv:1910.10920 give general recurrences, not this family-specific parity classification.

Previously established results for clique bouquets concern distinct graphs with clique blocks; they do not imply the present nonchordal-square result. Searches for cactus, square-bouquet, wedge-of-cycles and exact polynomial/root-count aliases found no result explicitly covering the claimed parity law. Broad database and internet searches are not exhaustive, so unindexed prior work remains possible.

## Mathematical value — PASS

This gives an exact all-parameter root-count classification for a natural cactus family rather than a numerical sample. The sharp change from real-rootedness for one or two squares to nonreal roots for every larger bouquet, plus a persistent two-versus-four count of real zeros while the degree grows without bound, answers a natural real-rootedness question prompted by recent sink-polynomial results. The phenomenon occurs outside both the chordal and claw-free hypotheses of the available positive theorem. The argument isolates an elementary monotone rational mechanism that may help analyze other block constructions, though no unproved generalization is claimed.

## Sources and limits

Primary comparison: Alexandersson–Maia Leite, arXiv:2610.41502v1, first public 2026-10-30; general background: Hwang–Jung–Lee–Oh–Yu, arXiv:1910.10920 (2019). The applicable graph family is one-vertex wedges of identical four-cycles; other cactus families remain open here. Originality is a comparison with inspected and searchable literature, not a global priority certificate. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
