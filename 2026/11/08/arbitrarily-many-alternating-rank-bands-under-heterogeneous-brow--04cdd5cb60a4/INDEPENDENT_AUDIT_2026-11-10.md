# Independent mathematical audit

## correctness

PASS

The first-reset renewal equation differentiates at r=0 to H_d(t)=(Q_d*Q_d)(t)-tQ_d(t). Its Laplace transform is [exp(-2a sqrt s)+(a sqrt s/2-1)exp(-a sqrt s)]/s^2; inversion gives the stated universal erfc kernel scaled by d^2/D. Direct high-precision independent evaluation gives h(1/4)>0 and h(2)<0. For newly separated d_j, its contribution vanishes at all fixed older sample times (small-u exponential tail), while at its two new times it is O(d_j^2), dominating previous classes O(d_j), preserving 2K alternating strictly signed samples. The intermediate-value theorem gives >=2K-1 sign-changing zeros. No-reset first-passage density f0(t)>0 converts these to ordered rank-quantile response signs via t_r prime=H/f0. Independently checked six alternating signs for K=3 and sample patterns K=1..4 with 65-digit arithmetic. The proof supplies arbitrary K; finite tests alone would not.

## originality

PASS

The 2026 Vatash et al multiparticle Brownian-search preprint studies rank-dependent optimal resetting including a homogeneous-start critical rank and heterogeneous examples. Its accessible abstract does not establish an arbitrary 2K-1 count of zero-rate quantile sensitivity changes for independent fixed initial-distance mixtures. Evans–Ray 2024 studies expected search time against random target distributions, a different functional; renewal transforms are classical. Resultary semantic searches found related resetting thresholds but no equivalent unlimited rank-band theorem. Best-knowledge originality passes, with material unresolved priority risk: the closely relevant full Vatash preprint was not accessible through arXiv/OA and authorized institutional retrieval reported disconnected VPN; no whole-document noncoverage is claimed.

## value

PASS

The theorem gives a mathematically motivated structural counterexample: even independent one-dimensional Brownian searches can exhibit arbitrarily many alternations between beneficial and harmful *infinitesimal* resetting across completion ranks, where homogeneous starts have a single known critical-rank narrative. The all-K scale-separation construction and strong sign-count conclusion are substantive, not a tiny finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
