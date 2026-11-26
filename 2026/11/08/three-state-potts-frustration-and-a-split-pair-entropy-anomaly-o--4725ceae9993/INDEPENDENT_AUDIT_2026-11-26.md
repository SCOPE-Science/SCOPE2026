# Independent mathematical audit

## correctness

PASS

For population sizes N_c and split count b, deleting the matching subtracts exactly m-b from the count sum_c binom(N_c,2), denoted F. Transferring a vertex from a class at least two larger than another strictly decreases F, so its minimizers are precisely balanced sizes. When m=3t they are even and can be realized with b=0. In either other residue, balance forces two odd populations, and one split realizes the lower bound F_min+1 on F+b. The other possibility for equality is b=0 and F=F_min+1; this is exactly the balanced distribution of monochromatic pairs among the three colors, since balancing the pair counts minimizes F over even sizes. Thus there are no further minimizers. Evaluating energy on those pair counts gives the displayed minimum. Counting named colors, labeled pairs and both orientations of the split gives B=2(t+1)A for the one-split and no-split counts in the two nonzero residues. Matching symmetry gives a uniform conditional split location. The balanced multinomial is asymptotic to (3 sqrt(3)/(2 pi m))3^m in all residues; the extra factor 3(2t+3) is asymptotic to 2m and gives the other prefactor and the common residual entropy. Independent enumeration over graph edges for m=2–6 gave energy/count pairs (0,18), (0,6), (4,180), (8,450), (12,90); split counts 12,0,144,360,0. An independent pair-counting DP matched the full ground-state split histogram for m=2–18; large-index prefactors were checked in all residues.

## originality

PASS

The distinct supported result is the exact optimizer structure, ground-state multiplicity and residue-dependent prefactor for the total-edge antiferromagnetic objective on this matching-deleted family. Neither the inspected maximum-3-cut theory nor the exact overlapping defective-coloring finding establishes that classification.

## value

PASS

The family isolates frustration induced by using fewer spin colors than parts on a standard dense graph. The optimizer census distinguishes two parity-constrained mechanisms with identical energy rather than just returning the minimum cut complement. The ratio of the two sectors explains why one exceptional matching pair becomes typical in two residue classes, and why the normalized entropy alone misses a factor of order m in the ground-state count. These are concrete data for zero-temperature measures on this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
