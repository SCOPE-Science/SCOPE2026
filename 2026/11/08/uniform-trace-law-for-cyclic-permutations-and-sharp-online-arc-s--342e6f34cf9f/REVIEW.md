# Scientific review of the cyclic-permutation arc-trace theorem

## Correctness: PASS
The proof first reduces any shattered support to an arc subset of one directed Hamiltonian cycle, excludes all supports of size at least \(n-1\), then constructs every binary labeling on the remaining directed path forests by reversing the cyclic order of contracted positive blocks. Its only delicate boundary is two blocks: this occurs only when no negative arc remains. Inclusion-exclusion gives the exact number of realizations of each trace, and permutation-cut enumeration gives every coefficient. A depth-\((n-1)\) mistake tree is impossible because the all-positive branch has a unique compatible hypothesis after \(n-2\) decisions. A standalone full finite test over \(3\le n\le6\) passed. The tests are not substituted for the general proof.

## Originality: PASS, with residual priority risk
Literature comparisons examined the permutation-as-bijection framework of Albert–Bouvel–Féray (arXiv:1808.05459), the zero-set VC/Littlestone theorem of Guingona–Kolesnikov–Nierwinski–Soucy (arXiv:2109.04805), the Hamming/Johnson neighborhood VC bounds of Adler–Benediktsson–Macpherson (arXiv:2007.16042), and the general VC set-system operations of Cambie–Girão–Kang (DOI 10.37236/8288). The inspected results apply to other concept families or address expressibility and general bounds. Their statements do not imply the directed single-cycle support criterion or its uniform exact-label multiplicities. An undirected Hamiltonian-tour incidence result is a close conceptual relative, but its support condition and reversal-quotiented hypothesis family do not imply the directed all-label counts or the online dimension.

Keyword searches for cyclic permutations, directed Hamiltonian arc incidence, the factorial coefficient, path-forest supports, and online shattering yielded no exact published match. This is evidence of limited search coverage, not proof of historical uniqueness. A previously unlocated theorem phrased through directed Hamiltonian extensions or cyclic rook polynomials could overlap.

## Mathematical value: PASS
The result gives a complete infinite-family classification, an explicit coefficientwise shattering polynomial, uniform exact trace counts, and an optimal adaptive dimension. The uniform trace property is stronger than merely determining VC dimension, and it contrasts with the more restrictive undirected endpoint geometry. It identifies an exact learning complexity for the natural single-cycle conjugacy class of permutations and exposes the two-block obstruction at the dimension threshold.

## Limitations and closest literature
The result is not a theorem for arbitrary digraphs or arbitrary permutation conjugacy classes. The finite verifier checks only \(n\le6\). The main historical-priority risk concerns a possible earlier equivalent directed-cycle extension/avoidance theorem. The named published sources above were compared by mathematical hypotheses and consequences rather than solely by title.

Self-review: passed. Independent audit: not yet performed.
