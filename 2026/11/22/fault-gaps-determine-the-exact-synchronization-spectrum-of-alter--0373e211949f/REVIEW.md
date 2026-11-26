# Independent mathematical audit

## correctness

PASS

Composing the two complement swaps gives a_j'=a_{j-1} except at j in J and b_j'=b_{j+1} except at j+1 in J, where the output is one. With no faults, reverse the indexing of the b stream to obtain rotation of an m-letter word on four symbols; the fixed point count of its d-th power is 4^gcd(m,d), yielding the primitive census. With faults, each stream is a disjoint union of directed copy chains of lengths g_i with forced-one heads. At round t each chain retains max(g_i-t,0) distinct original bits. All ones is reached iff every surviving bit is one, giving the stated cumulative and first-entry counts. This proves sharpness, the maximum-depth fraction and the phase-resolved cycle, including one fault (g=m), every edge faulty (g=1), and m=2. The longest intact Bernoulli run is L-1 on the conditioning event. The cyclic union bound and disjoint blocks at (1±epsilon) log_{1/(1-p)} m prove the claimed convergence for fixed p. As a check separate from the general proof, /workspace/nor_review_check.py (output /workspace/nor_review_check.txt) rebuilt the NOR tables for every fault pattern and every even-phase initial state at m=2 through 7: 246 nonempty fault patterns, 2374896 faulted initial states, and the complete fault-free orbit censuses. None of the frozen checkers was executed.

## originality

PASS

The supported distinct contribution is the exact fault-layout-dependent first-entry spectrum of alternating matching NOR and its sharp depth. The intact orbit count after rotation reduction is the standard primitive necklace count; the random-fault limit after the gap reduction is the classical longest-run scale, not an independent novelty claim. Neither the closest earlier alternating lower-approximation finding nor the same-day NOR synchronization result supplies the deterministic matching-fault spectrum. This is a statement-level comparison, not a priority guarantee.

## value

PASS

An exact robustness invariant for a natural switched cycle: a single deletion destroys a full recurrent permutation, and the complete synchronization-time population depends on the fault gap profile, not simply the number of deletions. The whole first-entry distribution, including the exact fraction at the sharp depth, adds information needed to distinguish layouts. The standard necklace and longest-run consequences are useful baselines rather than the main contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
