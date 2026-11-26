# Independent mathematical audit

## correctness

PASS

In a finite local ring, unit status is precisely nonzero residue; hence distinct vertices are adjacent iff their two residues do not sum to zero. This yields the balanced complete multipartite graph in residue characteristic two and a complement consisting of K_s plus (q−1)/2 copies of K_(s,s) in odd characteristic. Each residue fiber consists of twins. Three white fibers leave every blue vertex with at least two white neighbors; two distinct white fibers allow a blue vertex in a fiber that misses one residue to force the other white. When the required source is in one of the white fibers a blue vertex is available since s>=2. The graph has no isolates, so one remaining white can always be forced. This gives the polynomial, all minimizers, and the exact inversion from N and c. The rank-two witnesses fit the odd regime and K_(s,s). In the remaining regime nilpotence gives m/m² nonzero, thus s>=q>=4. Rank two cannot accommodate three or more parts of size at least three: each part must use a distinct isotropic line in a nondegenerate real bilinear plane. The squared-difference matrix of distinct real labels, repeated within each part, has rank at most three and the exact pattern. Thus M=N−mr gives the claimed transition. Independent replay python /workspace/audit_checks.py 2 exhausts every initial subset for Z/4, Z/8, Z/9 and the F4 dual numbers and tests each coloring against the profile rule; the 16-vertex case gives {14:96,15:16,16:1}. Finite corroboration is separate from the rank and forcing proofs. The recognition statement is relative to the stated graph class, not ring reconstruction.

## originality

FAIL

The entire finding is covered by direct specialization and elementary inversion. Boyer et al. Proposition 4 directly gives the even polynomial and profiles. For the odd branch, Barrett–van der Holst–Loewy equation (4.1) and Corollary 2 give mr<=2 on exactly this complement shape (and mr>=2 since it is connected and noncomplete). Thus M=N−2 and no forcing set is smaller. Boyer et al. Theorem 1(1)–(3), not merely its multipartite proposition, gives the complete polynomial on that branch: its n−2 pairs are precisely nontwin pairs of nonisolates, here all pairs from different fibers. Distinct residues have distinct missing-neighbor fibers and s>=2 gives a witness outside the two vertices. The remaining real rank values follow from K_(s,s) and the induced K_(3,3,3) obstruction (Barrett et al. Observation 6(b)) plus the classical rank <=3 univariate squared-distance matrix, using one coordinate per part. This is exactly the frozen upper witness, expressed in distance notation. M=N−mr then gives the transition. Solving the resulting known coefficient identity for q and s, which already specify the graph, is mechanical rather than a distinct theorem at the claimed level. The decision rests on these verified implications, not on unavailable literature or on an exact-title match.

## value

FAIL

The statement is a clear worked example connecting ring residue structure, a forcing polynomial and rank, but the entire exact outcome is mechanically implied by the cited graph theorems and elementary coefficient inversion. It does not provide an independently useful unknown exact fact or a surviving substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
