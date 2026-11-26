# Independent mathematical audit

## correctness

PASS

The extension lemma is valid with overlapping border occurrences allowed. A suffix border of the extended word of length at most b, where b is the old longest-border length, would also occur at the start of the second copy of the old longest border, giving a third occurrence. Any longer new border, with its last letter deleted, would be an old border, so only length b+1 can witness closedness. Matching the context letter extends both old copies without creating a third. Reversal gives the left test. In the proposed word the interior block occupies positions a+2 through a+8. The two long zero blocks flank it; for the indexed row their clipped portions both have length a+2−j≥2 and the interior zeros are singletons, giving exactly two border occurrences. The other proposed borders each occur exactly twice by the displayed run positions; in particular the long 1-zero border selects the first and last long zero runs, whose lengths are at least two even in the exceptional case. In all rows the available context letters differ on each compared side. The endpoints straddle the prescribed cut and are distinct. The indexed row contributes a−2, including zero for (2,1), and seven fixed intervals give a+5=floor(n/2)+1. The parameters cover every n≥13; the proof neither needs nor establishes an upper bound on F₂(n).

## originality

PASS

The separately indexed finite census contains exactly the n=14 word/cut and, by reversal, its intervals. No priority is inferred from the same date and that witness is not separately new. The supported distinct claim is the two-parity all-length extension n≥13, including its explicit construction and proof, not that finite witness, the singleton convention, or the border-extension method.

## value

PASS

The additive improvement matters here because the inequality crosses the exact half benchmark at every n≥13 and even the rounded-up benchmark at every even length from 14. The result explains how the same fixed run pattern maintains the phenomenon as the length grows, rather than merely giving another isolated optimum or extrapolating a census. It provides a reusable explicit test family for cut-query analyses. It does not claim a better asymptotic density coefficient or refute a published conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
