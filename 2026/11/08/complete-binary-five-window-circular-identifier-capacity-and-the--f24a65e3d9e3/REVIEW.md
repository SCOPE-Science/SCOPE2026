# Scientific review

## Correctness — PASS

The exact domain is binary cyclic identifiers of length \(k\ge5\), with **five** consecutive bits observed at each indexed position, no repeated windows within a codeword and no overlaps across codewords. The universal \(\lfloor32/k\rfloor\) bound follows by counting 32 possible five-windows. For every \(5\le k\le32\), except seven, the complete constructive witness table supplies exactly that many pairwise disjoint valid cyclic words. At \(k=7\), the 20 binary seven-necklaces are exhaustively divided into two constant invalid classes, six nonconstant invalid classes and twelve valid classes. A three-row cover of the twelve valid classes has pairwise intersecting window sets within each row, implying an upper bound of three, and the explicit three-cycle witness attains it. For \(k>32\), the counting bound is zero. Both direct word and independent directed-graph verification scripts passed on the actual included artifacts. No asymptotic or finite-experiment inference is substituted for the exact finite proof.

## Originality — PASS (qualified)

Grubman, Şekercioğlu and Wood, arXiv:1502.02199 (2015), define this precise robot-identifier packing number, give the simple upper bound, and exhibit some parameter families and examples, including binary five-window eight-position identifiers. The inspected statement of the original problem, Theorems 1–6, necklace constructions and concluding open directions do not establish its full binary five-window capacity profile or the seven-position obstruction. Cameron, Gündoğan and Sawada, arXiv:2205.02815, establish efficient construction of *one* prescribed-length repeat-free cyclic sequence, not a maximum mutually disjoint family. Álvarez et al., arXiv:2308.16257, analyze disjoint cycles without fixing every cycle length and factors of an expanded graph, so their results do not imply this fixed-seven obstruction. Research-record searches for de Bruijn fixed-length seven-cycle packing, five-window cyclic labeling and eBug capacities identified related but not dominating results. Historical-priority verification has not been independently performed, and a specialist may locate an unindexed exact table.

## Value — PASS

The capacity of a fixed visibility window is an explicit, application-motivated invariant for circular identifiers whose rotation must be recovered. The five-bit binary case has exactly 32 possible observations and is used in the motivating robot-identification literature; determining the capacity for **every** ring length is a natural complete classification rather than an arbitrary finite slice. The exceptional seven-position deficit is a sharp failure of an otherwise tight volume bound, with a transparent twelve-cycle intersection mechanism and explicit optimal constructions. It directly distinguishes single-cycle existence from simultaneous capacity, a structural distinction important for multi-identifier systems.

## Limits and closest literature

The mathematical camera is noiseless and reads five consecutive ordered bits with orientation retained. It does not model symbol misrecognition, reading reversal, larger alphabets, longer windows, or laboratory reliability. The literature comparisons support best-knowledge originality but do not establish absolute historical priority.

Self-review: passed. Independent audit: not yet performed.
