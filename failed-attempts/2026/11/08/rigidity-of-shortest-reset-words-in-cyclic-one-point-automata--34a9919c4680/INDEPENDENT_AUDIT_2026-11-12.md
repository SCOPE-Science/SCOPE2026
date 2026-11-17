# Independent mathematical audit

## correctness

PASS

For word with A rotations and h_i effective 0→r jumps, final state from i equals i+A+r h_i (mod n); if gcd>1, distinct residue classes never merge. For coprime r all n jump-count residues must be distinct, forcing a trajectory with at least n−1 effective jumps. At least n−r rotations separate consecutive jumps, giving |w|≥(n−1)+(n−2)(n−r). The explicit alternating word reaches this bound and induction on absent subset states shows reset to r. Equality consumes all rotation and defect letters in forced gaps, yielding the unique string even at n=2. Independently checked shortest-word multiplicity via subset BFS at bounded n≤9; infinite result follows from argument, not BFS.

## originality

FAIL

The prior November 2 published theorem proves the same exact coprime criterion, threshold and *unique* word for all n and d after swapping the roles of input labels a and b. The novelty claim is completely covered.

## value

FAIL

Counting optimum words in this natural automaton is a worthwhile invariant when unknown, but the exact one-element optimizer set was already established uniformly. Generator renaming, another proof and finite BFS provide no new mathematical result over that earlier theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
