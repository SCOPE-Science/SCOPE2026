# Independent mathematical audit

## correctness

PASS

With positive runs, all common subsequences are monochromatic. Their maximum length is s=max(min(a,d),min(b,c)), and any pair of embeddings into a shortest output covers all letters, so it shares exactly s equal letters. If the shared letters are zeros and a≤d, every output zero is required by the second input. This forces its c ones before the first zero, and the first input's b ones after the a-th zero. The prefix is therefore 1^c0^a and the suffix a shuffle of d−a zeros and b ones. If a>d use the last d zeros and the symmetric suffix argument; exchange letters and inputs for one-sharing. The classes are disjoint by inventory. With s≥2 the general upper bound has binomial top at most N−4 and is strictly below the proposed maximum. With s=1 the four cases forced by the two minimum constraints reduce to Pascal's identity for the two displayed families, or to N−2 for the two opposite unit pairs when the other two lengths exceed 1. Here N≥6, giving strict inequality in the latter cases; the cases N=4,5 are included in the two main families. This establishes all equality cases, and Stirling gives the asymptotic. The proof's statement that the central binomial coefficient is strictly increasing needs m≥1 (it takes the value 1 at m=0 and m=1); all uses of strict increase are in the valid range. Independently checked the exact count, shortest length and every optimizer on all 35,960 positive quadruples of total length 4 through 32 by a deterministic next-letter dynamic program. The finite check does not prove the unbounded range.

## originality

FAIL

The inspected distinct same-day longest-minimal record gives an exact zero-sharing count H for all four independent runs when the overlap is one letter. The overlap is not confined to s=1: every shortest zero-sharing class at s=min(a,d) contracts bijectively onto exactly that record's one-shared-zero class for (a−s+1,b,c,d−s+1); exchange the symbols and inputs for the other branch. The resulting H evaluations are exactly the asserted formula. The complete fixed-N equality classification then follows from the general bound for s≥2 and the exact longest-minimal result without any contraction for s=1, by Pascal's identity and the four unit-run boundary cases. This is demonstrated coverage by mathematical reduction, not a claim that the same-day record predates this one, nor that its global longest-minimal objective is literally the same as shortest.

## value

FAIL

Distinct shortest-output ambiguity for two opposing runs and its extremizers are meaningful invariants, and the frozen argument is correct. But against the inspected exact longest-minimal result the evaluated counts require only contracting the mandatory consecutive gap, while the optimizer list reduces to the s=1 table by the known general bound and elementary binomial comparisons. No further structural result or useful independent exact remainder is claimed in the frozen record beyond these consequences. A reference correction or a new certificate would not create such a remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
