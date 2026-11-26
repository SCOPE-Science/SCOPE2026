# Independent mathematical audit

## correctness

PASS

The proper part is the incidence graph between p-sets and partitions into three p-sets. Two p-sets have a common disjoint p-set, giving connectivity via the corresponding partitions; its edge surplus is M. Rank preservation excludes inversions in both fixed spaces and quotients. For h=p, three rotation orbits are the only possible invariant p-sets; the order-p action fixes each of three blocks separately, so the fixed graph is a 3-star. The induced reflection on residues modulo 3 fixes one leaf. For h=3p, the transitive point action forces a transitive action on the three blocks and its kernel's three orbits force the unique residue partition. For h=3, use CRT coordinates (x,t) in Z/p × Z/3 with rotation adding 1 to t, and conjugate any reflection to negation. Each fixed lower vertex has a block described by one phase at each x; simultaneous phase translation does not change the partition. After normalizing phase at x=0 to 0, reflection invariance is exactly phase(-x)=-phase(x). This gives 3^((p-1)/2) simultaneous fixed lower vertices, and without reflection 3^(p-1), with no fixed upper vertex. A lone reflection fixes one ground label, so exactly one odd block can be fixed in a fixed lower partition; choosing it gives u centers, and the other two p-blocks are exchanged, giving 2^(p-1) leaves per center. Burnside applied to edges minus vertices gives contributions M at identity, -3^(p-1) at the two rotations of order three, -1 at other nonidentity rotations and -u at reflections, exactly the displayed beta formula. Every reflection coset type at given h is conjugate since 3p is odd. Independent exhaustive prime-five reconstruction in /workspace/evidence/partitions.py (output partitions.txt) agrees with all fixed cell counts and all eight quotient ranks, including 16606 and 8293. The finite check corroborates, rather than proves, the all-prime argument.

## originality

PASS

Best-of-knowledge pass for the explicit simultaneous fixed-graph classification together with the quotient computation, not for fixed partitions, ordinary homology or the Burnside method alone. In particular the fixed-star incidence description and simultaneous order-three/reflection count do not follow just by averaging the ambient symmetric-group character. The identical catalogue entry is the subject, not separate coverage.

## value

PASS

The first one-dimensional proper part gives a natural case to classify actual fixed strata, not only traces. Rotation three and a lone reflection yield very different disconnected geometric fixed sets, and their subgroup intersection has a uniform phase law. The classification gives a reusable example distinguishing fixed spaces from connected orbit graphs over an infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
