# Independent mathematical audit

## correctness

PASS

For phi(0)=001, phi(1)=011, W_k=phi^k(0), m=3^(k-1), the AAB decomposition with A/B differing at their exact central position creates four repeated-factor intervals. Their increasing endpoints cover all positions, and the bridge lemma forces any unique factor to contain one of three bridges. The substitutions have disjoint start-modulo-three factor patterns, so trimmed-image occurrence bijections preserve uniqueness inductively; each bridge has repeated proper prefix/suffix. Independent direct occurrence counting on W_k for k=2,3,4 produced exactly the predicted three (start,length) pairs: k2 (2,3),(5,3),(7,2); k3 (8,6),(16,7),(22,4); k4 (26,15),(49,19),(67,10). This finite check corroborates, not replaces, universal bridge induction.

## originality

PASS

Kishi–Guo–Urbina–Bannai characterize occurrence-preserving morphisms and derive MUS results for Fibonacci and Thue–Morse, not the canonical Stewart choral iterates. Fici–Shallit identify this morphism and study complexity, repetitions, palindromes, etc., not the explicit three MUS bridges. Other Resultary records on Mephisto–Waltz concern a different morphism (0->001,1->110). A priority risk remains for unindexed Stewart-specific MUS tables.

## value

PASS

The complete exact three-MUS classification across an unbounded sequence of morphic words provides natural unique-factor anchors relevant to string algorithms. Despite growing length 3^k, the count stays exactly three and their positions/sizes scale in a precise way; this is a structural infinite-family result not mechanically implied by general factor complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
