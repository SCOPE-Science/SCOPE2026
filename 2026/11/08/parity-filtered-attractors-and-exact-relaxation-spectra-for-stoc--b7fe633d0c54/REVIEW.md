# Independent mathematical audit

## correctness

PASS

With t agreeing incident edges at degree d, the two closed-neighborhood counts are t+1 and d-t; a flip occurs iff 2t>=d and changes the number of agreeing edges by d-2t. A path of positive-probability updates reaching strictly lower energy rules out recurrence by monotonicity. Leaf particles give an immediate drop; two particles in one arc can be brought together at an unmarked vertex, and occupied distinct adjacent arcs can bring particles together at their shared mark. These exhaust the exclusions. In the remaining configurations all leaves and marks are frozen, and the arc positions move independently except for the single-update clock. In particular the root bit can be taken at a marked vertex, making it invariant. Cycle consistency is precisely parity of the number of occupied arcs; it gives two complementary bit assignments for every allowed tuple. For k=1 a lone particle cannot occupy both edges at its repeated endpoint; for k=2 the two arcs conflict and the independence polynomial is 1+2w. The trace of the cyclic hard-core transfer matrix gives F_k(1)=L_k and F_k(-1)=2 cos(k pi/3) for k>=2, which produces the parity-filtered count. Each allowed coordinate move has probability 1/(n+k), hence the transition matrix is identity minus the tensor sum of reflecting path Laplacians divided by n+k. Cosine modes yield the full spectrum and longest-arc gap; each path's maximum Laplacian eigenvalue is at most its number of sites, so all class eigenvalues are nonnegative. Symmetry gives uniform stationarity, and any finite chain eventually enters a closed class almost surely. Independent direct SCC enumeration of all 65,536 configurations for the n=12 example found sizes [1,1,4,4,15,15], and the n=7 S={0,1,4} instance gave [1,1,3,3,3,3]; replay files: /workspace/branches/83497e97-2ba0-4f4b-89a2-366086af6f79/independent_scc_check.py and independent_scc_check_output.txt. The frozen verification narratives were inspected; the stated original scripts/output were not attached as frozen support. The proof rather than the bounded reproduction establishes all sizes.

## originality

PASS

The same stochastic minority rule, particle energy, tree matching description and bare cycle kink dynamics are prior art. The supported distinct claim is the parity-filtered recurrent-class realization on cycles with attached private leaves, including the arbitrary arc-length weights and the full discrete-time class spectra. No exact duplicate or mechanical implication was found in the inspected relevant sources. The theorem numbering in the inspected Rouquier et al. PDF is 20 and 33 for the cited cycle and tree statements; the frozen citation's 4.2 and 4.6 do not match that version.

## value

PASS

It completely determines which recurrent dynamical phases survive and how each relaxes in a natural unicyclic family. The counts separate the effect of the number of marks from their geometry, and the exact product realization explains why a bipartite graph can support mobile non-ground-state recurrent classes. The same realization supplies all class relaxation modes and shows which intermark distance controls the gap, rather than restating a graph independence-set count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
