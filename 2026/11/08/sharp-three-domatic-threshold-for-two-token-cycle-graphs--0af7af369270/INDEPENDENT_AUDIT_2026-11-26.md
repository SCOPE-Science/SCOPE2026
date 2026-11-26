# Independent mathematical audit

## correctness

PASS

An adjacent pair has degree two, yielding the upper bound of three. The unpatched sum-modulo-three colouring works for all pairs except possibly the two cut-adjacent pairs when n is not divisible by three: a nonadjacent pair has an interior token that can move in both directions, and adjacent pairs normally have opposite nonwrap moves. A changed colour affects only the closed neighbourhoods listed around its pair. Checking these moves shows that the affected pairs and all their neighbours use only indices 0,…,4 and n−4,…,n−1 in residue 1 from n=10, or 0,…,4 and n−5,…,n−1 in residue 2 from n=11. These blocks are separated; translating the right block by three preserves the wrap move, collisions, changed-pair membership and all residues in the affected closed neighbourhoods. An independent symmetric-difference construction verified all neighbourhoods at n=7,8,10,11 and recovered boundary counts 11,14,11,14, so the lifts cover the infinite tails. K_{2,4} rules out three colours at n=4 by forcing all four degree-two vertices to have the same colour. At n=5 the B_i colours must form a properly coloured five-cycle; up to cyclic relabelling and colour permutation its sequence is (0,1,0,1,2), forcing (1,2,2,2,0) on the A_i. The closed neighbourhood of B_1 then misses zero. Independent exhaustion of all 729 and 59,049 assignments agrees. A maximal independent set and its complement furnish two classes in both cases, and F₂(C₃)=K₃ has three classes.

## originality

PASS

The bounded search did not establish coverage of the all-n ordinary domatic formula together with the uniform four-entry repair. The n=3 case is an ordinary cycle, n=4 is a standard complete bipartite case, and n=5 can also be identified with the central graph of C₅; do not credit novelty to these isolated cases. No inspected adjacent theorem supplies the family or the repair.

## value

PASS

This is a natural exact invariant of the standard two-particle configuration graph of a cycle. The degree bound supplies a sharp target but not attainability. The result resolves every length, identifies the two obstructions, and supplies explicit partitions via a rule whose repair size is bounded independently of n. The uniform construction is useful when a partition is needed, not merely a numerical threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
