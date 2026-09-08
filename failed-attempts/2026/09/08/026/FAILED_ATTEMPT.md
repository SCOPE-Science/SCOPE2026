# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified Hamiltonicity-girth-expansion census of connected cubic bipartite graphs at orders 14-26
- **Round:** 2026-09-07-first-light-01
- **Lane:** 63
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Structural Graph Theory
- **Method:** isomorph-free generation with canonical labeling plus backtracking Hamiltonian-cycle decision with girth and spectral-expansion certification

## Problem

Enumerate isomorph-free connected cubic bipartite simple graphs for each even order n in {14,16,18,20,22,24,26} via canonical labeling, decide Hamiltonicity of every representative by backtracking search with pruning and unsatisfiability logging, and compute girth and algebraic connectivity lambda2 plus adjacency spectral gap for each graph.

## Attempted claim

Exact per-order table for n=14,16,18,20,22,24,26 of total connected cubic bipartite graphs, counts Hamiltonian vs non-Hamiltonian, distributions of girth and lambda2/spectral gap, with (i) minimal-order non-Hamiltonian extremal example: adjacency list, bipartition, girth certificate, lambda2 and gap, cut/bridge obstruction, and failed-search UNSAT log, and (ii) one high-girth Hamiltonian extremal witness with explicit Hamiltonian cycle verifiable independently.

## Research outcome

Exact certified census of connected cubic bipartite graphs for n<=16 (1,1,2,5,13,38 classes), all 60 proved Hamiltonian with explicit cycles, girth witnesses, spectra/expansion, and bridgelessness; completeness doubly certified by an independent transversal plus Held-Karp replay. Range 18-26 explicitly not claimed.

## Why this attempt failed

Failed axes: originality, value.

originality: The core enumeration counts 1,1,2,5,13,38 for connected cubic bipartite graphs on 6,8,10,12,14,16 vertices were already published (OEIS A006823, offset 2n; Faradzev 1978 constructive enumeration; Brinkmann 1996 fast generation; McKay/Sloane; Howroyd extensions; cf. A008325 Euler transform and A004066 bicolored). DRAFT itself concedes 'New does not mean the counts were unknown' but then mis-cites A060851. The remaining joint layer is routine augmentation of that known list: BFS girth, numpy spectra/lambda2, DFS/Held-Karp Hamiltonian cycles, per-edge bridgelessness. The highlighted extremal witnesses are famous objects: the n=14 girth-6 class with lambda2=2-sqrt(2) is the Heawood (3,6)-cage (edges, girth witness and Hamiltonian cycle as filed are standard properties); the n=16 girth-6 class is the standard 16-vertex girth-6 cubic bipartite type (Mobius-Kantor family), long known Hamiltonian with known spectrum. No prior-Isolation argument was needed: cited priors (Georges-Kelmans minimality at 50 vertices for 3-connected case arXiv:2101.00943; planar Barnette sufficiency arXiv:2309.09578; asymptotic minimum spectral gap arXiv:2209.13758) are correctly distinguished, but the decisive nearest prior is the A006823/House-of-Graphs/Meringer explicit-graph database, which the topic file does not substantively compare against. A timestamp or failed literature search does not establish priority; substantive comparison shows the joint table adds no new mathematical object, gap, or non-Hamiltonian witness (the target-plan witness does not exist <=16). This is repackaging of known enumeration with standard invariants. value: Even taking correctness as given and granting narrow novelty as a joint replayable dataset, the result is not independently worth finding later. It is a downscoped fragment (n<=16 complete, explicitly not 14-26; n=18 with 152 expected classes and n=20 with 449 not attempted) whose headline corollary is negative: no non-Hamiltonian connected cubic bipartite graph exists <=16, so the target minimal-non-Hamiltonian witness is absent and the bridge/2-cut obstruction analysis is vacuous (all graphs verified bridgeless). The positive witnesses are textbook cages already known Hamiltonian. Per-graph girth/6-cycle counts/spectra/lambda2 are standard-computation columns that resolve no Barnette-type weakening and no expansion-vs-Hamiltonicity conjecture, give no theorem beyond 'all 60 small cases are Hamiltonian and bridgeless', and supply no extremal record. This falls squarely under the reject categories: textbook restatement of A006823 counts, routine-parameter augmentation, tiny unmotivated gain, and unexplained enumeration (60 rows with no conjecture or downstream use). A seconds-replayable verifier does not by itself confer citable value.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Claimed range is n<=16 only, not the topic's 14-26: n=18 enumeration (expected 152 classes) was started but did not finish in available time and is not claimed; orders 18-26 remain open. Counts coincide with known sequence A060851 so the numbers are not new; novelty is the joint certified dataset (cycle+girth+spectrum per representative with replayable verifier). No minimal-order non-Hamiltonian witness is produced because none exists at n<=16 (proved by the census itself).

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
