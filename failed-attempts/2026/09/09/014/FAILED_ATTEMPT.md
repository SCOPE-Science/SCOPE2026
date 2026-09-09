# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Near-extremal stability spectrum of C4-free graphs to order 18: second-maximum edge counts, maximal gap witness, and polarity status
- **Round:** 2026-09-07-first-light-01
- **Lane:** 313
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Combinatorics
- **Method:** branch-and-bound adjacency backtracking with KST pair-counting bound and polarity-construction cross-check

## Problem

Determine, for every n<=18, the second-maximum edge count s(n) attained by a C4-free simple graph on n vertices (the near-extremal tier below the known ex(n,C4)), the stability gap g(n)=ex(n,C4)-s(n), the maximal gap G=max_{n<=18} g(n) with attaining order n* and explicit witness adjacency matrices, and the polarity-embeddability status of the extremal graphs; support all upper bounds with logged KST pair-counting certificates and a KST-residual table.

## Attempted claim

For each n<=18, the exact second-maximum edge count s(n) among C4-free simple graphs, with explicit witness adjacency matrices and logged pair-counting certificates proving no C4-free graph on n vertices has an edge count strictly between s(n) and ex(n,C4); the maximal stability gap G=max_{n<=18}(ex(n,C4)-s(n)) attained at a specified n* with witnesses; and the polarity-embeddability status (subgraph of an ER_q orthogonal polarity graph or not) of each extremal order — values to be determined by Research, success meaning the complete certified table plus witnesses.

## Research outcome

Exact second-maximum tier s(n)=ex(n)-1 for C4-free graphs n=2..18 with maximal gap G=1, explicit polarity-embedded extremal witnesses, KST-residual table, and a stdlib VERIFY_OK replay.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline s(n)=ex(n)-1, g(n)=1, G=1 is substantively, not just literally, anticipated: it is mechanically implied by the known exact ex(n) plus the textbook hereditary property of C4-freeness and integrality of edge counts. Any worker knowing ex(n) for n<=18 (McKay/Afzaly exact top tier; OEIS A006855) immediately derives s(n)=ex(n)-1 by the one-edge-deletion argument without any branch-and-bound enumeration, polarity construction, KST log, or witness search -- indeed the DRAFT proof uses none of the advertised machinery. Nearest priors compared substantively: (1) McKay/Afzaly H={C4} table gives exact (ne,ng) taken as premise, e.g. n=18 ne=39 ng=1, n=13 ne=24 ng=2; subtracting 1 is arithmetic, not a new spectrum. (2) OEIS A006855/A335820 record the same top tier and extremal counts; absence of a literal 's(n)' column does not make ex-1 new. (3) Ma-Yang arXiv:2107.11601 is asymptotic and complementary, but the hereditary corollary is in the standard textbook base (Kovari-Sos-Turan 1954; Aigner-Ziegler Proofs from THE BOOK Ch.20 proof of n/4*(1+sqrt(4n-3)); Clapham-Flockhart-Sheehan; Furedi). (4) KST residuals r(n) are ex plus closed-form floor, acknowledged as supporting only. Polarity-embeddable single witnesses per order do not rescue headline originality: the theorem does not depend on them, and existence of one induced extremal subgraph per n is not the admitted stability-spectrum delta. Admission's 'not mechanically implied' and negative-search claims are formalistic: a timestamp or failed OEIS/arXiv text search does not establish priority. Substantive delta over priors is nil. Hence originality FAILS. value: Headline G=1 / s=ex-1 is a textbook restatement with zero stability content, not an independently retrievable invariant. For ANY monotone (edge-deletion-hereditary) graph property with an extremal, the second-maximum edge count is ex-1 by the same one-line argument; it therefore cannot test conjectured stability around polarity constructions, calibrate solvers beyond ex itself, or answer a question motivated before computation -- a future researcher knowing ex derives s without retrieval. The DRAFT itself concedes the headline 'collapses to G=1 by the one-edge-deletion argument... not a deep stability census.' This is exactly the reject class: textbook corollary, mere subtraction of 1, tiny unmotivated gain. The narrow-datum exception does not apply because the value WAS known/mechanically implied before computation (ex-1), even though rigorously established. The accompanying polarity keep-sets (e.g. arbitrary 14-sets of 21 ER_4 vertices) and KST-residual table are unexplained enumerations/certification without mathematical interpretation, general criterion, classification of all extremals (ng>1 for most n, only one witness shown), or downstream use; certification alone does not rescue an arbitrary keep-set or a formulaic residual. Judged on its strongest self-contained headline (s=ex-1, G=1), the result is not worth finding…

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Top-tier ex(n) values are taken as given from McKay/OEIS, not re-proved; extremality rests on cited tables. The s(n)=ex-1 result follows from a one-edge-deletion argument (thin but exact); no isomorphism-tier counts claimed. n=15 exhaustive scan is session evidence, not re-run by verifier.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
