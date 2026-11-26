# Independent mathematical audit

## correctness

PASS

Rankings of labels in each coordinate are independent uniform permutations. A given triple chain is obtained exactly when its orientation in the first coordinate persists in all others, so p=6^(1-d). For two triples with one common label of ranks i,j, interleave below and above it independently: L_ij=C(i+j-2,i-1)C(6-i-j,3-i); there are four labeled orientations for each i,j. With two shared labels, both must agree on their order; each private label chooses one of three slots, and equal slot choices have two total orders while distinct slots have one, giving six two-extension and twelve one-extension prescriptions. Independently, /workspace/reproduce_chains.py counts restriction pairs of all 120 and 24 permutations: extension-size histograms {1:8,3:16,4:4,6:8} and {1:12,2:6}, reproducing q1 and q2. The intersecting ordered-pair counts N1,N2 follow by choosing shared labels then private labels for the second triple; distinct disjoint pairs are independent and the missing diagonal subtracts M p². At n=3,4 the first overlap cannot occur; d=1 is the deterministic check. The intersecting-triple dependency graph makes the third Arratia–Goldstein–Gordon term zero and yields the claimed ordinary-TV upper bound at the exact finite mean. At critical positive limiting mean, d=3 log n/log 6+O(1) along the specified integer-dimensional sequences/subsequences. 20³>6⁵ gives delta>0, (20/12)³<6 makes the two-overlap term smaller, and n⁵6^(-2d) is also lower order. N1~n⁵/4 times q1~8·20^(-d) gives the positive leading constant 2. This is not a sharp TV lower bound, nor a claim of full-integer-sequence mean convergence on the dimensional lattice. The frozen finite script was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the explicit three-chain second factorial cumulant and its shared-extreme leading term, with the resulting explicit Poisson-approximation bound. The existence threshold and the Poisson approximation method are prior; historic full-text coverage of the refined critical law is unresolved.

## value

PASS

Three-element chains add a higher-order order statistic beyond simple comparability. At a natural critical scale the second factorial cumulant measures the surplus of chain pairs beyond Poisson; its strikingly small decay exponent and exact leading coefficient isolate the common-extreme mechanism. This exact dependence diagnostic is substantive even though it is not a distributional lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
