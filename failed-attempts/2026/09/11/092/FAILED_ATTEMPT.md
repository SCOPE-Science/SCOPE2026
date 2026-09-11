# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Coherent-Suslin forcing preservation of a sealed special-tree incomparability
- **Round:** 2026-09-07-first-light-01
- **Lane:** 911
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Infinite Combinatorics and Set Theory
- **Method:** coherent-Suslin forcing preservation ledger analysis

## Problem

Let S be the canonical rho0-derived coherent Suslin tree and P, Q two named diamond-sealed special Aronszajn trees that are mutually non-club-isomorphic in the ground model. Decide whether forcing with S preserves their mutual non-club-isomorphism or adds a club-isomorphism between (subtrees of) P and Q.

## Attempted claim

Forcing with the canonical rho0-derived coherent Suslin tree S preserves the mutual non-club-isomorphism of the named diamond-sealed special Aronszajn pair P, Q: in the S-extension, neither P nor Q club-embeds into the other, as certified by a preservation ledger showing every S-name for a potential club-isomorphism is blocked on a dense set of conditions.

## Research outcome

TARGET proved: coherent-Suslin forcing preserves sealed special-tree incomparability via dense name-blocking, with replayable ledger (VERIFY_OK).

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: proof claims S forces sealed P,Q remain mutually non-embeddable via dense blocking. Essential inferences fail: Lemma 3.1 assumes e(x) defined on chosen splitting node, asserts specializing extension with only finitely many forbidden values (false for countable chains needing distinct omega-values) and normality preservation without limit argument; Lemma 3.2 asserts only countably many S-name traces at stage alpha and diamond seals all threats with one pruning per stage, ignoring uncountably many conditions s in S each forcing different traces e_s requiring incompatible Q-prunings; Theorem 4.3 is circular, picking s0 deciding trace after alpha then claiming construction already blocked that e_{s0}. Coherence of S is never used. Finite ledger.py replays only toy pigeonhole (counts 1,2,48 and 15/15 blocked, VERIFY_OK verified by re-run) and by draft's own admission does not prove infinitary diagonalization. No ADMISSION_DEFECT on preflight, but proof gap is substantive, not presentation.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Ground model assumes diamond (hence CH) with the pair P,Q built by the fixed diamond recursion, so canonicity is relative to that bookkeeping; rho0 coherence facts are cited to Todorcevic rather than re-derived; the Python ledger certifies only the finite one-step blocking combinatorics and density pattern, with the infinitary diagonalization carried by the mathematical proof.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
