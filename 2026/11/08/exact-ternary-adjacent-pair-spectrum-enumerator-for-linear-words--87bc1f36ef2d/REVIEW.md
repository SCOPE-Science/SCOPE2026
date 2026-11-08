# Scientific review: ternary linear adjacent-pair spectra

## Correctness — PASS

The statement concerns the *unlabeled endpoints* of linear ternary words and counts nine-entry count matrices, not word realizations. The Euler-trail existence criterion is necessary and sufficient, including the no-edge case. Each unordered off-diagonal vertex pair has a unique signed difference and independent nonnegative slack, yielding the formal factors \(z^{|d|}/(1-z^2)\). All three divergence constraints leave one integer degree of freedom; the balanced term \((1+z^3)/(1-z^3)\) and each of the six endpoint-imbalanced terms \((z+z^2)/(1-z^3)\) follow by exact geometric summation. The complete classification of disconnected cases on three vertices gives the three correction terms without overlap. Rational simplification and the order-seven pole at one yield the asserted enumeration and asymptotic. Two standalone checkers respectively tested matrices with \(0\le m\le9\) and all words with \(1\le n\le12\), without substituting those finite tests for the proof.

## Originality — PASS, with a documented residual risk

The closest foundational source is Jacquet–Knessl–Szpankowski, *Counting Markov Types* (DOI 10.46298/dmtcs.2768). Its full text, in particular its explicit cyclic-only assumption and its exact three-letter balanced generating function, was inspected. The balanced component is prior art and is acknowledged. The new result includes six endpoint-divergence classes and precisely the weak-connectivity exclusions for noncyclic word spectra. Karhumäki–Puzynina–Rao–Whiteland (arXiv:1605.03319) treats the strictly finer \(2\)-abelian observation retaining boundary letters, so its equivalence classes are not these spectrum classes. The closest indexed research result gives the corresponding binary-alphabet count, not the ternary enumeration. Searches for the full sequence, generating function, noncyclic frequency matrices, and ternary window-two spectra did not identify a theorem or table implying the specific nine-entry matrix count. Search failure alone is not proof of historical uniqueness.

The 2012 expanded Jacquet–Knessl–Szpankowski article (DOI 10.1109/TIT.2012.2191476) was located, but its full text could not be accessed through the attempted lawful sources. Its accessible abstract discusses balanced matrices. Historical priority remains subject to inspection of this version and any unindexed work, although the public evidence available did not provide a stronger covering claim.

## Value — PASS

The precise invariant is the maximum number of messages distinguishable using only the multiplicities of length-two windows over three symbols, with no endpoint annotation. The binary case is known, while a three-letter alphabet introduces an independent directed three-cycle flow and six possible endpoint imbalances, so the ternary count is structurally different. The result enumerates the complete population for every length, gives a compact rational function and its growth constant, and makes explicit why the cyclic/2-abelian analogues are different. Such spectrum counts quantify the capacity of complete bigram-count reconstruction, rather than an arbitrary finite slice or a restatement of a known table.

## Scope and limits

No assertion is made for longer windows, four or more symbols, individual signature-fiber sizes, cyclic observations, or independent historical verification. The two replayable programs test bounded cases; the proof establishes the all-length identity. The manuscript date 2009-09-02 does not itself establish first public availability; the publisher record states the earlier verified public release for the cited journal source as 2009-12-31.

Self-review: passed. Independent audit: not yet performed.
