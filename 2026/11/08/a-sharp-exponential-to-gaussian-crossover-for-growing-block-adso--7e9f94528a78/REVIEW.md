# Independent mathematical audit

## correctness

PASS

At state j remaining blocks, proposal success probability p_(n,j)=C(kj,k)/C(kn,k) depends only on j. Hence hitting time is a sum of independent geometric waits G_j, exactly. Ratios a_l=p_r/p_(r+l)=∏_(i=0)^(k−1)(kr−i)/(k(r+l)−i) satisfy a_l≤(r/(r+l))^k and π→0. For bounded u/k, each fixed scaled geometric wait tends to an independent exponential with ratio e^(−l/θ), and integrable tails are uniformly bounded by a monotone integral. Thus weak and first-two-moment convergence hold. If r/k→∞, local logarithms and global power bounds yield Σa_l^m∼r/(mk) for m=1,2,3; the geometric-centered third moment bound and Berry–Esseen yield O(√(k/u)). An independent exact rational check verified the combinatorial variance identity Σ a_l²(1−p_j)=Σa_l²−πΣa_l for n=18,k=4,u=3. These checks complement the all-array proof.

## originality

PASS

Turban (2019) determines exact finite k-mer cover-time distributions, fixed-k near-full coverage extreme-value families and a qualitative fixed-k trend to Gaussian as u grows, but the detailed §4.4.6 treats fixed k and does not give a simultaneous k→∞, u/k critical family or absolute Berry–Esseen rate uniform in the triangular array. Vajna et al. (2012) already have the abstract exponential sum in a task-priority setting; the distribution in isolation is expressly not claimed as new. Published Resultary searches revealed no dominating joint-growth theorem for this deposition model.

## value

PASS

The joint k,u growth regime supplies a motivated phase transition for a standard adsorption model, resolves the critical scale u≈k between a single dominant last wait and many comparable geometric waits, and proves explicit variance scaling with a quantitative normal bound. It is neither a restatement of the fixed-k law nor an arbitrary isolated numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
