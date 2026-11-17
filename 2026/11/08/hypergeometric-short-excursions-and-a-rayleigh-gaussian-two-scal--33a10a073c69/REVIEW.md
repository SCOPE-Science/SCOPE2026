# Independent mathematical audit

## correctness

PASS

For a uniform fair bridge of length 2n, Catalan primitive-excursion generating function E(z)=2zC(z) yields factorial moments E[(J)_r|K=k]=(n)_r(k−1)_r/(2n−k−1)_r (1≤k<n), uniquely determining Hypergeom(N=2n−k−1,M=k−1,sample=n); k=n is correctly treated as J=n. The exact return-count mass has Rayleigh scaling K/√n⇒X with density x/2 exp(−x²/4) and suitable Gaussian tails. The hypergeometric variance is k/4+O(1) for k~√n and a uniform conditional CLT gives (J−K/2)/n^(1/4)⇒√X Z/2; conditional variance decomposition yields √n(1−Corr(K,J))→√π/[2(4−π)]. Independently enumerated every balanced bridge n=2..7 and compared each conditional probability exactly. The proof of the limit is analytic and not established by these finite checks.

## originality

PASS

PASS qualified: Serlet (2014) equation (6) gives a general product-Catalan exact ordered-length distribution, so the raw excursion decomposition and finite conditional law are partly implicit prior combinatorics. Lindell–Holst (2007) Proposition 3.1 counts macroscopic excursion bins and studies longest lengths, not the shrinking two-step bin with K~√n. The new jointly assessed Rayleigh Gaussian variance-mixture, n^(1/4) scale and explicit Pearson correlation correction are not stated or immediately implied by the inspected prior limit theorems; require a specific hypergeometric conditioning and uniform conditional CLT.

## value

PASS

PASS: short return segments are a canonical microscopic excursion statistic and K is tied-down discrete local time. The exact conditioned finite population law identifies their dependence and the distinct √n versus n^(1/4) scale with random variance, plus the sharp approach-to-one correlation constant. These are meaningful multiscale probabilistic invariants, not an arbitrary cutoff or an already-tabulated number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
