# Independent mathematical audit

## correctness

PASS

With A high opponents earlier in the tie order and B later, the two ranks are 1+A and i+B. Their quadratic payoff difference has degree at most two; its Walsh constant is (N²+2Ni−N−4i+2)/8, singleton coefficients are −i/4 on earlier indices and (N+i−1)/4 on later ones, and pair coefficients are ±1/4 for pairs on the same side and zero otherwise. For each coordinate set U the gradients give the equal-coordinate line in the edge coefficient block, so subtracting its mean gives the residual. The only nonsingleton residuals are (N+i+j−1)²/32 per pair and 1/8 per triple. The pair sum before division by 32 is C(N,2)(N−1)²+2(N−1)² sum(i)+(N−2) sum(i²)+(sum(i))². In the total norm, writing k=i−1 and m=N−1, the numerator of the sum of singleton-coefficient squares is mN²+m²k−mk²; the quadratic terms sum to 2 C(N,3)/16. These sums and the constant coefficients yield exactly the stated T and H. For affine increments 1 the edge mean is (N−1)/2 and each singleton has magnitude 1/2, with opposing signs in each pair, giving H/T=1/N. The quadratic witness differs by the stated factorized excess; it ties at seven and is strict for all N>=8. My independent exact vertex-Laplacian replay /workspace/branches/audit_priority.py solved the normal equations directly from rank-sorted profiles (no edge Walsh coefficient computation), matched both energies for N=2 through 9 including 1919/2192 at N=8, and reproduced the seven-agent witness 53454277/62354880>6/7. For 2<=N<=6 it formed Q=H−T/N by polarization, verified its all-ones kernel vector and positive Schur pivots of the complementary principal minor (zero form at N=2), hence PSD on the whole space of increments. These checks and the analytic proof establish the exact threshold only for the stated uniform two-level complete-conflict model; there is no nonlinear optimum claim.

## originality

PASS

Credit the affine benchmark, small-N comparison, and exact seven-agent example to prior work. The supported addition is the single explicit quadratic-payoff witness, with a closed-form positive excess for every N>=8, completing the population threshold. No distinct retrieved statement covers that unrestricted tail; finite signs are not an implication. The unresolved primary supplement access is recorded, not treated as negative evidence.

## value

PASS

The sign of the improvement, rather than its small numerical size at eight, answers when an affine rank rule ceases to maximize the potential component in this basic design model. A single strict monotone witness for every larger population replaces a finite pattern of isolated examples and gives a quantitative gap, so the sharp threshold is both motivated and useful without claiming the optimal nonlinear payoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
