# Self-review

## Correctness — PASS

The claimed minimax problem is over two homogeneous laziness gains in \([0,1]\) on a fixed irreducible reversible bipartite kernel, with the centered norm taken in \(L^2(\pi)\). The proof first uses the sign-conjugation spectral symmetry to identify all nontrivial eigenvalues in \([-s,s]\cup\{-1\}\); it then derives an endpoint lower bound, excludes gains below \(1/2\), and proves that equality uniquely requires \(\{\alpha,\beta\}=\{1,1/(2-s)\}\). The candidate multiplier \(\lambda(\lambda+1-s)/(2-s)\) has modulus at most \(s/(2-s)\) throughout the remaining spectrum. The strict interval comparison is an exact rational identity valid on the specified open parameter range. A fresh execution of the embedded checker passed 39,756 exact finite assertions; the analytic argument, not the enumeration, establishes the general theorem.

## Originality — PASS on inspected evidence, with priority risk

The inspected 2004 Boyd–Diaconis–Xiao treatment optimizes a single stationary transition kernel. Apers–Sarlette (2015) optimize unrestricted quadratic spectral filters and mention finite two-step convergence for complete bipartite graphs, which corresponds to \(s=0\) and is excluded. The published stagewise-safe Richardson interval theorem has a high-condition-number branch already implying the same gains for \(s\ge3-2\sqrt2\); this **covered** range is excluded from the contribution. In the actual new range \(0<s<3-2\sqrt2\), that interval theorem instead yields a strictly worse Chebyshev bound; the exact spectral gap \([-s,s]\) permits the improvement. An inspected odd-cycle theorem does not cover bipartite spectra, and crown-graph fastest-mixing rigidity concerns one step. No equivalent statement was located in the actual published-finding corpus and bibliographic searches. Unindexed classical or recent work remains a genuine publication-priority risk.

## Value — PASS

The strict divergence between the best stagewise-safe interval design and the best **actually Markov-positive** two-round design gives a structural reason to use spectral cluster information instead of the enclosing interval. The infinite crown family makes the performance difference nonvanishing: optimal alternating two-round error factor tends to zero while best repeated-step error factor tends to \(1/9\). This is more than a new parameter value or a renaming of a known optimum, and both gains correspond to implementable nonnegative stochastic kernels. It does not claim a general optimum over independently rewired or nonhomogeneous edge weights.

## Closest literature and limitations

See `RESULT.md` references and `AUDIT.json` source inspections for the 2004 stationary optimum, the 2015 unrestricted polynomial treatment, the published interval-safe frontier, the odd-cycle two-round result, and the exact crown one-step theorem. The publication-priority conclusion is evidence-limited. The new proof does not establish robustness to edge failure, rounding error or arbitrary distributed per-edge gain schedules.

Self-review: passed. Independent audit: not yet performed.
