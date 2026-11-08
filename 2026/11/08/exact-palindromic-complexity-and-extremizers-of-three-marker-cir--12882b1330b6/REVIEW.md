# Three-marker circular-palindrome extremizers: scientific review

## Correctness — PASS

The claim counts distinct literal cyclic factors of lengths from \(1\) to \(n\) in binary words of exactly three \(1\)'s, including zero-length gaps. The proof partitions possible palindromes by the number \(0,1,2,3\) of marked symbols. Explicit, nonoverlapping descriptions of the four families give the exact gap formula. It then minimizes the maximum gap under strict ordering, enumerates all equality triples, and uses a strict integer comparison to exclude repeated-gap patterns for every \(n\ge14\). A separate literal-factor enumerator agrees with the formulas for every one of 7,140 ordered triples through length \(36\), and independent extremum computations cover lengths \(14\)–\(24\). The computation supports, but does not replace, the general proof.

## Originality — PASS with historical-priority qualification

The closest primary result is Simpson (2014), Lemma 6 and Theorem 7: a three-marker example yields a lower bound at lengths divisible by three, while a separate theorem bounds the unrestricted maximum by \(5n/3\). The paper's open questions discuss possible optimality of analogous words. A construction plus an unrestricted upper bound does **not** imply exact optimum *within* all three-marker words, nor classify equality cases at each residue class. Proposition 13 treats circular words admitting palindromic conjugates and does not give the three-gap classification. OEIS A247000 records numerical unrestricted optima through length \(30\), without an infinite gap-dependent classification. Blondin Massé et al. (2011) study palindromic equations and periodicity in circular words, not these extrema. Searches of relevant mathematical records identified no statement implying the complete theorem. Unindexed historical calculations and future discoveries remain possible.

## Value — PASS

This resolves a natural and explicitly motivated subproblem of Simpson's circular-palindrome extremal program: among words with exactly the three markers used in the proposed extremal constructions, it proves the exact optimum at every length \(n\ge14\), identifies **all** maximizers up to dihedral equivalence, and determines the palindrome total for **every** three-marker word. A nonobvious special feature is that whenever exactly two gaps agree, the total becomes independent of their numerical values; distinct gaps instead depend only on the largest. The result rules out all alternative three-marker extremizers but deliberately leaves unrestricted optimality unresolved. This is a complete natural subclass classification, not an arbitrary finite slice or an unproved extrapolation.

## Verification and limitations

The source file `verify.py` runs without third-party dependencies and checks a finite domain. The proof covers the full infinite domain. Primary-source inspection includes the published Simpson text's Lemma 6, Proposition 13, Theorem 7, and stated open questions; the Blondin Massé et al. author preprint was inspected for its distinct algebraic/periodicity scope. Lack of a matching indexed result is not logically sufficient to establish historical novelty. The theorem makes no claim for four or more markers or all binary circular words.

Self-review: passed. Independent audit: not yet performed.
