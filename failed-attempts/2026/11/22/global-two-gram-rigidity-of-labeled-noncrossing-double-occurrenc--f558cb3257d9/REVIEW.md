# Independent mathematical audit

## correctness

PASS

Choose a shortest matched interval in the noncrossing source. An interior letter would have its other occurrence inside the interval, contradicting minimality, so there is an adjacent doublet aa. Its loop forces the same doublet in any doubled-label competitor. The possible unique exterior predecessor p and successor q, including their absence at a boundary, are read from the spectrum. Removing aa deletes its loop and exterior edges and adds pq when both neighbors exist; the reduced spectra still match, and the reduced source is noncrossing. Induction on the number of labels gives identical reduced words. A noncrossing doubled word has no repeated directed bigram: an equal-letter loop cannot repeat with two copies, and a repeated distinct-letter bigram would force interlacing. Thus the edge pq determines a unique reinsertion, even when p=q; missing neighbors determine the appropriate boundary, with the one-label word as base case. This proves the decoder and uniqueness also against unrestricted competitors. Dyck matchings with labeled pairs give n!C_n; because all are distinguishable the whole source is optimal. The six words at n=2 are distinct in spectrum, and 311232 and 323112 have identical spectra and equal last letter, so appended fresh doublets preserve a collision. One-letter counts are fixed and fail already for n=2. Independent bounded replay `python /workspace/review_replay.py 5` enumerated full fibers through four labels by position-pair assignments and checked the displayed collision; the induction is the all-order evidence.

## originality

FAIL

The central rigidity claim, including uniqueness against arbitrary doubled-label competitors, is a direct special case of a distinct stronger catalogue result and is also in the scope of the classical repeat criterion after encoding the endpoints. The exact subclass count is the labeled Catalan count applied to that rigidity. Distinct same-day records show coverage without settling publication order.

## value

FAIL

The main phenomenon is a worthwhile reconstruction property but already covered. Its labeled capacity is then an immediate Catalan count. The doublet decoder is a short alternative to the broader construction, without a demonstrated material algorithmic or structural improvement; the small unrestricted collision and its padding are a routine boundary check rather than a separate surviving finding. No new and independently valuable claim was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
