# Independent mathematical audit

## correctness

PASS

The claim fixes two undirected vertex-transitive graphs on Z_4^2 and defines X_G=0 when the root is vacant. For each occupied root component U, connectivity and the exact vacant external boundary force H_G(k,s)=sum_{U connected rooted, |U|=s} binom(16-s-|partial U|,k-s), with H_G(k,0)=binom(15,k). All 65536 labeled vertex-subsets of each graph were exhaustively enumerated independently by two new methods: repeated fixed-point neighborhood growth and a separately written rooted-connected-subset boundary census. The 17x17 integer matrices agree entry for entry within each graph (578 entries total), and the new signed difference agrees with the package: k=4: (s3:-12,s4:12); k=5: (s3:-36,s4:-24,s5:60); k=6: (s3:-36,s4:-48,s5:-30,s6:114); k=7: (s3:-12,s4:-24,s6:-6,s7:42); k=8: (s4:-6,s8:6); all other entries exactly zero. Independent tail sums for t=4,...,8 give respectively [12,36,36,12,0], [0,60,84,36,6], [0,0,114,36,6], [0,0,0,42,6], [0,0,0,0,6] for k=4,...,8, with every other entry zero. Thus every fixed-population conditional tail difference D_{k,t}/C(16,k) is nonnegative; the independent-site mixture has polynomial sum D_{k,t}p^k(1-p)^(16-k). For all 0<p<1 this is strictly positive exactly t=4..8 and zero for every other integer threshold; p=0,1 are equality. Weighting the delta by component size yields exact mean coefficients 12,96,234,126,24, sum 492. Both explicit neighbor sets are symmetric and six-regular with two common neighbors for every distinct vertex pair, implying A^2=4I+2J and eigenvalues 6^1,2^6,(-2)^9. Translation symmetry covers any root. Finite exhaustive enumeration is a complete proof for these fixed 16-vertex graphs, not an extrapolation beyond them. The actual 10-blob frozen Git tree was independently reconstructed and equals the assignment SHA.

## originality

PASS

Best-of-knowledge originality PASS for the exact comparison of the full rooted site-percolation distributions on the canonical nonisomorphic strongly regular pair, not for the known graphs, their spectra, or the general binomial-mixing technique. Newman–Ziff supply the canonical/microcanonical transformation without evaluating these rooted cluster tails; Diskin–Krivelevich prove asymptotic results for growing regular graph families, not exact finite coefficient signs for this pair; Huang et al. distinguish the pair by four-cliques, which does not imply rooted stochastic order. Inspected published same-graph findings on irreversible hard-core adsorption, paired domination, and neighborhood shattering count different objects and do not determine site-component distributions. Exact database searches identify generic graph invariant functions, not this rooted boundary-weighted coefficient matrix. No stronger covering result was identified in the cited primary texts and searches. Historical tabulation of rooted connected-set boundaries and a 2026 monograph with inaccessible full book chapters remain explicit priority risks; absence in a search is not proof of novelty.

## value

PASS

Rooted occupied-cluster size is a fundamental site-percolation susceptibility and network robustness variable, and the Shrikhande/4x4 rook pair is the canonical nonisomorphic, cospectral strongly regular (16,6,2,2) test pair. The complete signed fixed-population histograms yield a genuinely more informative simultaneous first-order stochastic order over all 16 thresholds, every 0<=k<=16 and all p in [0,1], with a precisely located strictness window and exact positive mean polynomial. This is a motivated exact finite-system benchmark showing what common spectra and two-point parameters fail to fix. It is not merely a few small graph statistics or an arbitrary numerical slice: the finite space is exhausted and the full natural rooted distribution classified. The result is independent of a large-N theorem or paper-sized downstream use; it could be reused to test reliability enumerators and compare graph models. The narrow scope is explicit and does not assert a universal percolation inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
