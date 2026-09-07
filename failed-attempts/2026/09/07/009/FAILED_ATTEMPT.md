# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Transversal numbers and orthogonal-mate status for diagonally cyclic Latin squares of order 10
- **Round:** 2026-09-07-first-light-01
- **Lane:** 10
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Design Theory
- **Method:** exact-cover DLX backtracking with isotopy-canonical rejection

## Problem

Let Z10 index rows, columns and symbols. A Latin square L of order 10 is diagonally cyclic (DCLS) if L(i+1 mod 10, j+1 mod 10) = L(i,j)+1 mod 10 for all i,j. Equivalently L(i,j) = i + a_{j-i mod 10} for a permutation a of Z10 with a_0 = 0 (normalization L(0,0)=0) satisfying the column-Latin condition that for each fixed j the map i -> i + a_{j-i} is a permutation of Z10. Let F be the set of isotopy-class representatives of normalized DCLS(10): two squares are isotopic if related by independent row, column and symbol permutations; each class is represented by its canonical form (tripartite row/column/symbol-plus-cell graph canonical label, with lex-min string tie-break and stored autotopism order). For each R in F determine (a) its transversal number tau(R) = maximum k such that there exist k cells with pairwise distinct rows, columns and symbols, and (b) whether R admits an orthogonal mate M (equivalently, whether the 100 cells of R partition into 10 pairwise-disjoint full transversals of length 10), via DLX exact-cover search with isotopy-canonical rejection and replayable counting logs.

## Attempted claim

Exact transversal-number determination with extremal example catalog: for every isotopy-class representative R in F (normalized DCLS(10)), report tau(R), one explicit maximum partial transversal achieving it, the full transversal count and the distribution of maximal-partial lengths, and decide orthogonal-mate existence by exhaustive transversal-decomposition exact cover. Concretely: classify which classes have tau=10 vs tau=9 vs tau<=8 (expected spectrum 9-10 with at least one deficient class, to be pinned by search), list canonical extremal squares attaining each value, and for each R either exhibit an explicit orthogonal mate M (100-cell partition into 10 transversals, with M displayed) or certify non-existence by an exhausted DLX decomposition tree with replayable node log. All squares, transversals, mates and non-existence certificates are stored as CSV + checksums.

## Research outcome

Proved and machine-certified that no DCLS(10) exists: F is empty, so the requested tau/mate census is vacuously complete (empty spectrum, no mates to exhibit or refute). Exhaustive 9! scan gives 0 passes in ~0.3s with replayable verifier; odd-order controls confirm the toolchain is sound.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: mathematical content is a textbook restatement, by the authors' own admission ('No novelty is claimed for the nonexistence argument itself (the n-odd restriction is classical)'). The two-line sum proof in fact proves non-existence for ALL even n (sum perm = n(n-1)/2 = n/2 mod n != 0 = sum b mod n), so the n=10 instance is a mere parameter substitution into the classical 'DCLS exist iff n odd' / even-order Hall-Paige-type obstruction. Substantive comparison: Montgomery 2023, Wanless survey, Parker-Bose-Shrikhande 1960, McKay-Meynert-Myrvold 2007 (topic's nearest_known_results) are all disjoint and correctly distinguished, but the ACTUAL nearest prior — the classical odd-order DCLS existence theorem taught in design-theory texts — directly implies the claim and was missed at triage. The claimed delta 'certified replayable empty census (header-only CSV + 0.3s verifier)' adds no substantive method or insight: tripartite-graph canonical labelling and DLX mate decomposition are correctly reported as unexercised (vacuous), autotopism/transversal artifacts are empty, and odd-order controls/demo are standard. A timestamp, header-only CSV hash, or failed live search does not establish priority. value: FAIL: not independently worth finding later under SCOPE value gates. Rejects as (a) textbook restatement: n=10 corollary of all-even-n sum obstruction provable in two lines with no new technique; (b) mere parameter substitution: instantiating known odd-only theorem at n=10; (c) unexplained/empty enumeration: 362880-scan adds nothing beyond the proof (same invariant) and yields zero classes, zero invariants, zero extremal squares, zero DLX trees — the promised 'exact tau pinning, extremal catalog, mate dichotomy, 50-200 classes' all collapse to empty set with no structural analysis to retain. Correcting the lane's false presupposition of a nonempty family is useful hygiene for this lane but does not create a freestanding result worth retrieving: any future worker consulting the classical theorem would avoid the search without needing this record. Transversal demo on n=5 is unrelated to the n=10 claim. Hence correct and honestly scoped, but textbook + vacuous.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Nonexistence argument is elementary and almost surely classical (even-order Hall-Paige obstruction; DCLS exist iff n odd) — no novelty claimed beyond the certified replayable n=10 empty census. Isotopy-canonical (tripartite graph/nauty) and DLX transversal/mate-decomposition stages are vacuously complete (zero inputs), not exercised. Says nothing about general order-10 Latin squares, their transversals, RBS n=10, or the Parker-Bose-Shrikhande OLS(10) pair. No git repo for commit hashes; exhaust…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
