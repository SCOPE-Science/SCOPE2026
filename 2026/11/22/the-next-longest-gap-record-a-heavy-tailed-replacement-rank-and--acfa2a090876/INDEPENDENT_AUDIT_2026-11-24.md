# Independent mathematical audit

## correctness

PASS

Rooting the circle at one sampled point gives Dirichlet gaps, so the ordered lengths are ordered independent exponentials divided by their sum. A binomial exceedance count at (1−δ)log n and a union bound at (1+δ)log n show that each fixed leading length is asymptotic to log n/n. Exponential memorylessness yields independent descending differences of rates j, giving the fixed-rank normalized gap-drop vector. Conditional Poisson thinning gives first-hit clocks E_i/G_(i) with the E_i independent of the initial gaps. The first strict decrease is exactly the first hit of rank one. The number of other marks before its clock is conditional Poisson with mean (1−G_(1))τ_1; the conditional centering difference from τ_1 is 1−G_(1)τ_1=1−E_1 and the conditional variance is O_P(n/log n). Both errors vanish under scaling by log n/n. If a rank in 2,…,m survives intact, it is at least as long as G_(m). Every damaged rank >m is shorter; for each hit leading rank the uniform first-cut position bounds its chance to leave any fragment ≥G_(m) by min(1,2(G_(i)−G_(m))/G_(i)), which has expectation tending to zero for fixed m. Thus the earliest rank that survives is the exact winner except on a vanishing event and the all-hit event. Finite clock/difference vectors converge jointly by independence and Slutsky; no limiting clocks tie. The all-hit event tends to 1/m both by exchangeability of m exponential clocks and by the integral in the record. Truncating bounded continuous test functions and then letting m grow proves the joint limit without requiring finite rank means. Given T=t, K−1 is geometric with parameter e^(−t), and integrating gives mass 1/[k(k−1)]. Given K=k the drop is a sum of independent rate-j exponentials and hence the maximum of k−1 rate-one exponentials. Mixing the CDF q^(k−1), q=1−e^(−y), against the rank weights yields survival y/(e^y−1), and termwise nonnegative integration yields π²/6. The difference variables, not the drop itself, are independent of (T,K); T and K are dependent.

## originality

PASS

The supported distinct claim is the marked joint next-decrease law for sequential insertion after a specified initial size, including the original-parent rank and the drop. Old static spacing representations and larger-scale record-time/count asymptotics are credited. None of the closest inspected statements supplies the two marks or their coupling with waiting time.

## value

PASS

The first subsequent decrease is the natural event at which the extremal gap changes length. The marked law distinguishes the original-parent survival mechanism from the possibility that a cut fragment wins. It shows coexistence of an exponential waiting limit, a dependent rank with infinite mean, and a light-tailed non-Gumbel drop with finite mean. The two new marks and their coupling are useful precision missing from aggregate record counts and static extremes, not just another statement of the elementary waiting law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
