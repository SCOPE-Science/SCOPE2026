# Independent mathematical audit

## correctness

PASS

In a jammed matching vacancies cannot occur at distance one or two: at distance two the middle site has no available partner, contradicting maximality. Vacancies at distance three force the middle dimer, which must have the earliest of its three neighboring clocks (otherwise a required vacancy would be occupied). Each three-clock test is independent of the other tests and the clocks outside the chain. After those tests, the two outer subpaths have independent endpoint conditions. For k=0 the edge sets of the two subpaths are independent and share only the designated site; it stays vacant in the joined process iff it stays vacant in both isolated processes, by chronological coupling. Conditioning on the first edge (i,i+1) gives residual left path size i-1, hence the displayed endpoint recurrence and alternating sum. Extending the chain one step to the left and subtracting gives the canonical probability; the factorial endpoint errors are summable, giving the claimed mean up to O(3^{-k}). For Poisson convergence, window disagreement at either end requires a decreasing-clock path through the fixed boundary buffer, with probability O(1/w!) for w=ceil(log^2 n). For start differences at most 3k+3, differences divisible by three force the later predecessor to be an earlier vacancy, and other differences force a pair of vacancies at distance one or two. More distant starts require independent disjoint sets of k three-clock tests. Thus b1+b2=O(n(k+w)(3^{-2k}+1/w!))=o(1) on the asserted subsequences; replacing the windowed by the exact count costs O(n/w!) in coupling. Starts omitted at sites 1, 2, 3 have total probability at most 3*3^{-k}. For the logarithmic lower bound, one can use the central edges at left indices s+1,s+4,...,s+3k-2 and the two protecting edges at s-2 and s+3k+1; their three-clock tests use disjoint clocks and fit inside a block of 3k+8 sites. Independent such blocks give the required lower tail, and the chain law plus a union bound gives the upper tail. The infinite line is justified by the same finite-radius stabilization and a_m tending to e^{-1}. The subsequence qualification rules out interpreting (4) as convergence for all n with a continuously centered threshold. The bundled small-n checker was inspected read-only, not used to establish any asymptotic.

## originality

PASS

Gerin's exact infinite-line distance-three pair law, the endpoint framework and the local-minimum mechanism are prior, and the chain factorization extends that mechanism. The distinct material result is the finite all-order factorization together with the terminal canonical-start Poisson extreme, including the specific factor 2/3 and the lattice threshold. Closely related published and corpus results have different observables or are at pair order. The oldest directly relevant full text, Page (1959), was unavailable on the attempted lawful routes; this is a priority risk, not evidence of noncoverage.

## value

PASS

The exact spacing-three chain encodes clustered local augmenting paths for a natural jammed matching. The chain law and exact canonical-start intensity explain why counting raw chain occurrences would give the wrong extreme-value constant. The result gives both the logarithmic scale and a sharp lattice-window limit for the largest cluster.

The dated certificate retains the supplied scientific assessment, sources and limitations.
