# Scientific review

## Correctness
PASS. Exact reduction from unanchored trigram profiles to directed Euler trails, the published fixed-start proper-transposition criterion, and an explicit closed-trail correction yield a finite-state recognizer. The generated 166-state exact transfer matrix satisfies a full vector identity at lengths 9, 21, 33 and 45, which proves the twelve-period recurrence for all lengths. Independent profile enumeration for lengths 3 through 16 agrees.

## Originality
PASS, qualified. Li and Xie (2005) provide the underlying unique Euler-trail test; Kontorovich (2004) establishes general regularity; Kiah, Puleo and Milenkovic (2014/2015) count profile equivalence classes. Related work on *binary bigram* and *cyclic trigram* observations does not establish the claimed *linear trigram* singleton enumerator. No inspected primary text supplies the explicit quadratic twelve-period law, but the unavailable complete 2004 article creates historical-priority risk. The method is attributed and not claimed new.

## Value
PASS. It determines exactly, for every length, the number and asymptotic density of sources that admit unambiguous reconstruction from full, unordered three-symbol reads. A 166-state integer certificate gives a reproducible all-length argument rather than an isolated finite census.

## Closest literature and limitations
Kontorovich, *Uniquely decodable n-gram embeddings* (2004); Li and Xie, *Finite automata for testing uniqueness of Eulerian trails* (2005); Kontorovich and Trachtenberg, *Unique decodability of bigram counts by finite automata* (2011); Kiah, Puleo and Milenkovic, *Codes for DNA sequence profiles* (2014). The result covers binary linear words and perfect read multiplicities, not cyclic strings or noisy readouts. Full priority comparison with Kontorovich (2004) remains outstanding.

Self-review: passed. Independent audit: not yet performed.
