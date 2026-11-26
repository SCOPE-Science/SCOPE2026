# Independent mathematical audit

## correctness

PASS

A face has induced maximum degree at most one, equivalently contains no connected triple. Separating the four core vertices leaves the eleven listed cores and exactly the F/S/D restrictions on a path word avoiding 111. Under fixed-order toggling of the augmented poset the matching is acyclic: arrows in a cycle would alternate matched up and unmatched down (there cannot be consecutive up arrows and the net dimension change is zero). The earliest matched toggle in that cycle must be undone at a down arrow of the same coordinate; both incident faces would still be available at that stage and would have been matched to each other, a contradiction. On the left, F survivors start 0110: insertion at the first bit fails only after prefix 011, and 111 avoidance forces the fourth bit to zero. For S, omission of the first bit forces an F step at the second, leaving prefix 0011 with a suffix starting in a forced zero. For D, insertion at the first bit fails exactly when the next bit is one; removing the resulting prefix 01 leaves another D suffix (its first two bits cannot both be one), so two such steps give 0101. The right restriction is unchanged for m>=7. All three prefixes are distinct, so before the core toggles, different left types are disjoint at both m and m-4 for m>=11, and within one left type prefixing preserves whether path words are equal. Thus all core toggle matches are preserved and each critical face gains two vertices. A fresh finite enumeration using induced maximum degree reproduces all base critical cores and dimensions for m=2 through 10, with (dimension,count) respectively (1,1),(2,1),(3,3),(3,5),(3,1),(4,1),(5,3),(5,5),(5,1). Undoing the empty-face pairing gives exactly one ordinary critical vertex; the other cells all have the same positive dimension, so they attach to a point and give actual wedges, not just a homology calculation. With m=ell-1 this proves all four assertions including ell=3 and ell=4.

## originality

PASS

The threshold-two definition, cyclic four-residue patterns for different graphs, and sequential acyclic matching all have precedent. The identifiable contribution is the all-length theta classification: the overlapping cycles require a new three-state endpoint analysis with distinct prefixes and core toggle compatibility. The exact theta graph also has prior results for different complexes, none of which gives this homotopy type under the checked hypotheses.

## value

PASS

The family joins two small cycles along common structure in the simplest one-variable theta setting and tests whether the path/cycle periodicity survives a branching core. The classification determines actual integral homotopy types at every length, distinguishing the single-sphere phases from three and five spheres. The endpoint recurrence makes the finite calculation useful beyond the bases and is a transferable way to analyse constrained paths attached to a fixed core without claiming a general suspension theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
