# Independent mathematical audit

## correctness

PASS

The frozen proof fails at RESULT.md line 80: the extra common-edge count is not bounded in expectation by the extra count in one tree. At n=2 the finite pair is always an edge, and it is common in the infinite parent graphs with probability (1/2)^2; the excess 3/4 exceeds H_2−1=1/2. In the full replacement /workspace/repairs/1/RESULT.md the excess is instead bounded by the sum of the two sample excesses, so its expectation is at most 2(H_n^{harmonic}−1), still o(n). Re-audit of the unchanged kernel: for i<j with priorities u<v, the nearest lower priority on the left must be i (all d−1 interior priorities exceed v), and any first lower priority to the right must be below u so that i wins the parent comparison. Its priority, if present, is uniform below v, giving the factor u/v+(1−u/v)(1−v)^{n−j}. The beta integral and reflected orientation give the exact kernel; direct binary-insertion enumeration independently checked every oriented frequency for n=2 through 7. For the square expansion, a cross term uses sum_{d≤s}1/[d(d+1)]=s/(s+1), and the two boundary indices obey s+t≥n. Partial fractions give sum a_d²=2ζ(2)−3 and sum d a_d²=2−ζ(2); tails give the stated error, since one index in the double boundary sum is at least n/2. On the integers the nearest lower priority on each side exists almost surely; taking finite intervals growing to the integers makes the tested parent relation eventually constant and gives the interior edge probability a_d. The shared right-edge count per vertex is a bounded shift-equivariant function of two independent i.i.d. arrays, so the ergodic theorem gives L¹ convergence of its spatial mean. Retaining both endpoints of an infinite edge retains the winning parent in the nearest-lower rule; omission of outside candidates cannot displace it. The repaired two-sample bound controls internal extras, and at most d starting positions can give right-crossing edges of length d, whose expected count summed over d is bounded by sum d a_d². After division by n both errors vanish. This proves the same scientific result in the repaired file, without calling L¹ convergence a strong law.

## originality

PASS

The repair leaves the statistical claim unchanged. The known ancestor calculation, local fringe-function limit theory, common leaf-interval edges in uniform Catalan trees, and common labelled edges in uniform or recursive tree ensembles do not supply this random-permutation direct-edge kernel and the resulting two-term mean and limiting density. The strongest adjacent indexed claim uses the same BST model but a maximum shared fringe interval, not direct adjacency. The pass is bounded to the distinct calculation and law, not the priority representation or ergodic method.

## value

PASS

The canonical random-permutation tree law is label-inhomogeneous near boundaries. The exact two-sided direct-edge kernel makes finite overlap calculable, resolves how independence can still leave a positive macroscopic fraction of identical labelled adjacencies, and quantifies the finite-size correction. A researcher comparing random tree models or checking random-BST overlap simulations has a precise benchmark, distinguishable from shape, fringe and ancestor overlap. The repaired bound preserves both exact formulas and the density law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
