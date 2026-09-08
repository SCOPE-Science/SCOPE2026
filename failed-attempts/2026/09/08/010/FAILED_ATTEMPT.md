# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact S4-orbit census of monotone Boolean functions on B4 with width and self-dual witnesses and certified replay toward D5=7581
- **Round:** 2026-09-07-first-light-01
- **Lane:** 72
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Order Theory
- **Method:** antichain backtracking with Sperner pruning and Dedekind recursion plus symmetric-group canonical reduction and evaluation replay

## Problem

Produce an exact symmetric-group orbit census of monotone Boolean functions on B4 (identified with antichains of the 4-cube): enumerate all 168 antichains by Sperner-pruned backtracking, partition them into S4-orbits under variable permutation with lexicographically minimal 16-bit canonical representative per orbit, verify sum of orbit sizes equals 168 with each size dividing 24, tabulate orbit-size and width (|antichain| bounded by C(4,2)=6) plus rank-profile distributions, enumerate self-dual fixed points under f^d(x)=not f(not x) with one explicit fixed witness and one non-self-dual separating pair in distinct orbits, and attempt certified replay enumeration of B5 targeting D5=7581 via Dedekind recursion with evaluation-replay log and timeout certificate.

## Attempted claim

Machine-checkable census: |MBF4|=168 antichains enumerated and partitioned into S4-orbits with canonical representatives, orbit-size histogram summing to 168, width distribution bounded by 6 with explicit 6-set extremal witness, rank-profile table, self-dual fixed-point count with explicit fixed antichain and explicit non-self-dual separating pair, plus replay log that either certifies |MBF5|=7581 or issues a timeout certificate with partial counts; all artifacts re-validated by an independent replay script.

## Research outcome

Exact S4-orbit census of monotone Boolean functions on B4 (168 antichains, 30 orbits, canonical reps, width/rank profiles, Burnside, self-dual witnesses) with full certified replay to B5=7581 (210 S5-orbits, Burnside, width extrema, 81 self-dual); independent replay script passes.

## Why this attempt failed

Failed axes: originality, value.

originality: All quantitative claims are classically known and the DRAFT concedes this (D4=168, D5=7581 and orbit counts 30/210 are classical, not claimed as new). OEIS A003182 lists inequivalent MBFs 2,3,5,10,30,210,... (n=4 ->30, n=5 ->210); OEIS A001206 lists self-dual MBFs 0,1,2,4,12,81,... (n=4 ->12, n=5 ->81) with pre-2000 references (Mills, Brouwer-Verbeek, Riviere, Knuth). Stephen-Yusun arXiv:1209.4623 counts inequivalent MBFs (490013148 for n=7) by profile-splitting/Burnside; Pawelski arXiv:2305.06346 gives n=9 inequivalent count; Szepietowski arXiv:2205.03868 gives methods to count fixes of permutations acting on MBFs (directly anticipating Burnside fix tables); Jakel arXiv:2304.00895 (D9) and a Campo arXiv:2206.10293 (b5=7581 via poset evaluation) anticipate D5=7581. Remaining delta - lexicographically-minimal sorted-tuple CSV layout, rank-profile/width histograms, and stdlib replay script - is an arbitrary re-encoding of the same known finite sets, not a substantively new theorem, object, or method. A different canonical-hash choice or CSV formatting does not establish priority, and a failed/absent search for that exact formatting does not establish novelty. value: Even taking correctness for granted, the result is a textbook restatement plus unexplained enumeration with no motivated gain. n=4 brute force over 2^16 subsets and n=5 independent-set enumeration over 32 vertices run in seconds; S_n lex-min canonicalization, Sperner bound C(4,2)=6/C(5,2)=10 with middle-layer extremal witnesses, duality f^d(x)=NOT f(NOT x), Burnside orbit-count check, and Dedekind recursion counting f0<=f1 pairs are all standard exercises/identities. The frontier (D8 1991, D9 2023) is untouched; recomputing D4/D5 and their long-known orbit/self-dual counts (30/210, 12/81) provides no new method, no downstream theorem consumes the 30-row table, and width/rank-profile histograms are trivial statistics of a tiny explicitly enumerable set. This is precisely mere recomputation with standard tooling and an enumeration without theoretical use, not independently worth finding later.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: D4=168, D5=7581 and orbit counts are classical values, not new; novelty is explicit canonical tables plus replayable witness/Burnside certificates. Scope n=4/5 only; trust rests on short stdlib-only auditable code.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
