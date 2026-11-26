# Independent mathematical audit

## correctness

PASS

The parts give complementary within-part contrasts, across-part mean contrasts and global constants, with Laplacian eigenvalues d,N,0; the projectors give off-diagonal entries b across parts and b-1/[(mu+N)(mu+d)] = a within. Independent signs cancel all cross terms among distinct unordered pairs, giving four times the sum of squared same-color entries. Writing s_i=2k_i-m, S=sum s_i and Q=sum s_i^2 produces the displayed objective S^2-(1-r^2)Q with r=a/b strictly between 0 and 1. For even q the bounds Q<=qm^2 and S^2>=0 are attained together only by balanced whole parts. For odd q and |S|<m, strict convexity forces any continuous fixed-sum maximum of Q to be extreme: if two coordinates are interior, a small opposite-coordinate perturbation increases the mean square over its two signs. Hence only one coordinate can be interior; the other q-1 endpoints have sum a multiple of 2m, necessarily zero, leaving Q<=(q-1)m^2+S^2. At |S|=m this bound is automatic; |S|>m costs strictly more by Q<=qm^2. The minimum |S| is epsilon=m mod 2, attainable with the one interior coordinate, and r>0 and 1-r^2>0 force the claimed equality conditions. They obey the nonempty-class constraint. Substitution gives both minimum variances, and the best whole-part S^2=m^2 for odd q gives the stated positive gap. Independent replay: python3 /workspace/review_checks/probing.py computes exact inverse matrices and exhausts admissible vertex-level sign placements on four small graphs at three rational shifts, corroborating all optimizers, the variance, the gap, and the stated K_{2,2,2} example. The frozen exact-rational checker was inspected; neither finite check substitutes for the fixed-sum proof.

## originality

PASS

The fixed-partition variance identity and equivalent weighted-cut representation are prior tools. The supported distinct claim is the sharp parity-dependent global optimizer and equality classification over all two-class designs on the balanced multipartite resolvents, including the positive quantitative whole-part gap. The inspected exact bipartite, three-probe and signed MaxCut theorems do not provide it; historical priority for an equivalent two-coupling optimization remains qualified.

## value

PASS

A fixed two-probe budget on q>=3 original parts makes proper coloring impossible. The theorem resolves the exact variance cost of forbidding splits over the whole balanced multipartite family and shows that the optimizing geometry does not depend on the positive shift even though the gap does. Those are useful benchmarks for stochastic probing and the equivalent weighted cut, not a runtime improvement or a claim that probing is necessary for these explicitly diagonalizable matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
