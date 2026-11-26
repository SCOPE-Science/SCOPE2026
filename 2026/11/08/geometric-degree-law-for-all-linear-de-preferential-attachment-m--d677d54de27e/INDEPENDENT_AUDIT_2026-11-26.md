# Independent mathematical audit

## correctness

PASS

Conditionally on the full joint past, a fresh uniform proposal is rejected with probability sum_i(d_i/D)/n=1/n. Repeating without updating degrees until acceptance gives exactly Q_i, and the first proposals themselves are independent choices for the uniform comparison. Deterministic conditional rejection probabilities imply independence by iterated conditioning. The log moment generating function is m(e^t-1) log N+O_m,t(1); choosing small signed t gives summable tail bounds on dyadic N, and monotonicity interpolates because consecutive dyadic logarithms have ratio tending to one. Changing H targets alters at most two final vertex degrees per edit, so histogram TV is at most 2H/N. For uniform attachment a nonseed birth rank i has independent Bernoulli increments, m per old count n from i to N-1. On ranks i/N bounded away from zero the Poisson approximation is uniform (the summed squared probabilities are O(1/N)), and its mean is uniformly m log(N/i)+o(1). A Riemann sum and removal of the lower-rank cutoff yield the exponential–Poisson mixture m^r/(m+1)^{r+1}. Each coordinate is 2/N-Lipschitz in each of m(N-2) independent choices; concentration, Borel–Cantelli and truncation of a probability limit give almost-sure TV convergence, then transfer by the coupling. The fixed seed contributes only 2/N and m=1 also obeys every estimate.

## originality

PASS

The uniform law and the de-preferential m=1 geometric limit are prior. In the exact sequential repeated-target model the all-fixed-m law, especially m>1, and the quantitative pathwise transfer are distinct from the available primary statements.

## value

PASS

Answers an explicit empirical-law question for multiple sequential attachments and gives a pathwise error guarantee that explains why the limiting histogram is the uniform one, despite nonuniform conditional transitions. The classical mixture on its own is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
