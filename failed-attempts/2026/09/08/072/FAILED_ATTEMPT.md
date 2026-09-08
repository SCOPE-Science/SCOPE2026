# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Solomon-Stiffler/Belov typing of optimal binary linear codes with k<=5: Griesmer-defect spectrum and certified sporadic witnesses
- **Round:** 2026-09-07-first-light-01
- **Lane:** 215
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Coding Theory
- **Method:** residual-chain family typing with MacWilliams enumerator-incompatibility certificates and shortening-chain replay

## Problem

For each optimal binary linear [n,k] with k<=5 and n<=15, determine the Griesmer defect delta(n,k) = n - sum_{i=0}^{k-1} ceil(d(n,k)/2^i) and prove its Solomon-Stiffler / Belov / sporadic type: exhibit a shortening chain from a simplex/Hamming parent with matching family enumerator, or certify sporadic status by a residual-chain plus MacWilliams enumerator-incompatibility argument excluding both families.

## Attempted claim

Exact Griesmer-defect spectrum delta(n,k) over optimal binary linear [n,k] with k<=5, n<=15, with every cell typed as Solomon-Stiffler, Belov, or sporadic; each sporadic cell carries an explicit generator, MacWilliams-verified weight enumerator, and residual-plus-enumerator certificate of exclusion from both families, including one fully replayable headline sporadic witness.

## Research outcome

Exact defect spectrum + sporadic typing over optimal binary [n,k], k<=5, n<=15 (65 cells, VERIFY_OK replay): 21 sporadic cells, max defect 3 at [12,5,4] with MacWilliams-verified witness; 4 proper optima below Griesmer-max proved by Hamming/puncture/DFS kills.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Replay passes for the stored table (65 rows, ranks, 2^k recounts, enumerators, delta arithmetic, Hamming/puncture kills, both DFS kills at 625654 nodes, headline enumerator 1+15z^4+15z^8+z^12 with MacWilliams dual check). However two headline-level statements are false as written. (1) Abstract says 'Sixty-one cells are Griesmer-tight (delta=0)'; independent recount shows 44 cells have delta=0 and 21 have delta>0 (65 total). 61 is the count of cells with d==gmax(k,n) (max d with g(k,d)<=n), not delta=0. The abstract conflates attaining the Griesmer upper bound on d with meeting the Griesmer bound with equality (n==g(k,d)). Body section 3 correctly lists 21 delta>0 cells, so the abstract contradicts the body. (2) Section 4 claims 'any weight-4 word has support size 4; puncturing it leaves a [8,4,4] residual (computed minimum 4)'. Independent check of the frozen [12,5,4] columns [1,2,4,8,16,1,1,1,14,22,26,28] finds 15 weight-4 words; e.g. u=2 has support {1,8,9,10} whose punctured residual has minimum weight 2, not 4 (only e.g. u=1 gives min 4). replay.py itself only asserts best>=2, not [8,4,4]. The residual sentence is therefore false as a universal claim and the logged check does not certify what the text claims. Lower-bound generators, defect arithmetic, Hamming A(8,3)<=28<32 kill of [8,5,3], puncture A(9,4)<=A(8,3) kill of [9,5,4] (valid since d=4>=2 keeps punctured words distinct), and systematic-DFS infeasibility logic (information-set identity block plus nondecreasing-multiset enumeration with w[u]+r<D pruning) are sound, but the two errors above are essential headline inferences. originality: The delivered typing collapses to mechanical arithmetic from prior bare distances plus a textbook implication, not the promised exclusion certificates. Grassl BKLC stores bare d(n,k); delta(n,k)=n-sum ceil(d/2^i) is then a deterministic ceil-sum. The DRAFT's sole sporadic rule (Sec.1) is 'SS/Belov meet Griesmer (delta=0), hence optimal delta>0 certifies sporadic with no further isomorphism test' — exactly the implication already stated in Wang-Chen-Wu 2605.11431 ('positive-defect optima are certainly not SS/Belov'). No per-cell Solomon-Stiffler/Belov shortening-chain attribution and no enumerator-incompatibility argument is actually given for any cell; the topic's required 'residual-plus-MacWilliams enumerator-incompatibility certificate' is replaced by delta>0 alone (Sec.4 residual is only a best>=2 consistency check). Chen 2406.10825 reconstructs many Grassl optimals as (affine) SS codes but the candidate adds no SS-vs-Belov subdivision (explicitly disclaimed: 'no SS-vs-Belov subdivision'). The explicit generators/enumerators (e.g. headline 1+15z^4+15z^8+z^12) are frozen stochastic-search outputs for small (n,k) whose distances are classical; no substantive comparison shows the enumerator or the 'sporadic' label to be a new structural fact beyond Grassl values plus textbook Griesmer/MacWilliams. A failed live search does not establish p…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['k<=4 achievers via seeded search (frozen, re-verified); equivalent optima give same (d,delta).', '[12,5,5]/[13,5,6] UB is replayed enumeration (625654 nodes), not closed form.', 'Typing is sporadic-vs-Griesmer only; no SS-vs-Belov subdivision of the 44 delta=0 cells.', 'Distances overlap Grassl values; novelty is the certified defect/typing/witness layer.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
