# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A rank-7 Fano-rooted splitter cell for 3-connected binary matroids with no M(K5) minor
- **Round:** 2026-09-07-first-light-01
- **Lane:** 433
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Matroid Theory
- **Method:** Seymour splitter-theorem induction with connectivity bridging and excluded-minor decomposition

## Problem

Decide one explicit splitter cell inside 3-connected binary matroids: the rank-7 F7-rooted M(K5)-free cell. Since binary matroids already exclude U(2,4), the direction's 'no U(2,5)' condition is automatic, so the operative content is the Fano/M(K5) seed pair named in the brief. Either (A) prove every rank-7 3-connected binary matroid with an F7 minor and no M(K5) minor reduces by a logged single-element deletion/contraction chain staying 3-connected and F7-retaining to an explicit finite seed list, or (B) exhibit a new rank-7 splitter-minimal obstruction with full connectivity certificate and minor-model logs.

## Attempted claim

Let C be the class of 3-connected binary rank-7 matroids M with an F7 minor and no M(K5) minor (hence no U(2,5) minor). Then either (i) every M in C admits an element e such that M\e or M/e (simplified) is 3-connected, binary, F7-retaining and M(K5)-free, with the full finite bridging table logged down to an explicit seed list containing F7, or (ii) the complete finite list of splitter-minimal obstructions in C at rank 7 is exactly the logged set O produced, each with connectivity table and F7/M(K5) minor logs. Success is the closed bridging table or the certified obstruction list.

## Research outcome

Closed target clause (i) as a splitter bridge: every rank-7 3-connected binary F7-rooted M(K5)-free matroid admits a 3-connected F7-retaining M(K5)-free single-element reduction, iterating to seed {F7}; certified by 4 logged rank-7 witness chains with full connectivity/minor-model/per-element logs replayed by a stdlib-only verifier (VERIFY_OK).

## Why this attempt failed

Failed axes: originality, value.

originality: Nearest prior Seymour splitter theorem (1980, doi:10.1112/jlms/s2-22-2-236) substantively covers headline (a). Instantiating N=F7 (non-wheel/whirl) immediately yields every 3-connected M with F7 minor reduces by one 3-connected F7-retaining step; adding binary and M(K5)-free heredity and |E|-termination adds no new content -- textbook minor-closed heredity and size induction. Hence O=empty at rank 7 has been known since 1980, not a new obstruction list. Strong Splitter (arXiv:1201.4427), Kingan EX[E4] (arXiv:1408.2377), Kingan-Lemos prism-free (arXiv:1203.3741) indeed list no rank-7 F7-rooted M(K5)-free matrix, but absence there does not make a Seymour corollary new; general existence does mechanically imply the M(K5)-free reduction because M(K5)-freeness is minor-closed. Part (b) four towers (seeds 1001,1002,1003 + one extension, n=11,11,11,12, bases 201,208,201,386) are new strings but arbitrary random coextensions by construction (search.py random.Random(seed), 500 tries), explicitly NOT splitter-minimal (10-11 good moves each; report admits fallback M0 not found). They are illustrations of the guaranteed abundant reductions, not canonical extremals, seeds, or blockers. A failed arXiv search or timestamp does not establish priority. value: Headline (a) is textbook restatement / parameter substitution (Seymour with N=F7 plus hereditary flags) with no reusable new lemma: since O=empty there is no terminal case to cite, and witnesses all reduce so provide no decomposition blocker. Headline (b) is unexplained enumeration of arbitrary objects: random tower matrices and their computed invariants (base counts, 10/11 good-move counts, lambda tables) had no pre-computation identity, motivation, or downstream use; certification alone does not rescue an arbitrary object. This is not the eligible narrow-invariant case (natural motivated object + unknown non-implied exact value future work needs). Full C census honestly disclaimed, but the remaining universal existence + 4 building-block chains is exactly the mechanically implied fragment plus illustrations, with no new extremal, obstruction, criterion, or cited reduction lemma.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: C is not enumerated; the universal one-step rung invokes Seymour's splitter theorem and classical wheel-regularity/whirl-non-binarity facts (cited, not re-proved). Logged full chains cover 4 witnesses, not every member; iteration for arbitrary M is existential via the theorem. M(K5)-freeness of chain children uses heredity, not per-child exhaustive search (tops additionally exhaustively searched). One mid-pass connectivity-enumeration bug found and fixed; final logs use the partition-complete s…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
