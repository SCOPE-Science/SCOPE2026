# Independent mathematical audit

## correctness

PASS

C PASS. N=binom(n,r), M=binom(n−1,r), u=2r−t and K_t= N binom(r,t)binom(n−r,r−t)/2. Conditional on a vertex being isolated, the m edges are a uniform subset of M avoiding edges; the proportion of t-overlap pairs also avoiding it is (n−u)/n. Hence Cov/(EI ET)=(n−u)N(N−1)/[nM(M−1)]−1. Expanding with M=(n−r)N/n yields the claimed expression. For nt≥r² numerator positive; for nt<r² write d=r²−nt≥1 and use binom(n,r)≥n(r−t) with the only equality n=5,r=3,t=1 occurring at d=4, so numerator strictly negative. Domain exclusions ensure both expectations positive; degeneracies m<2,n<u,m>M have zero covariance. Independent full finite fixed-edge enumeration checks negative n=5,7,8 and positive n=9 for r=3,t=1, including ratios −1/34 at n=8 and +1/165 at n=9.

## originality

PASS

O PASS best-of-knowledge. Published Behrisch–Coja-Oghlan–Kang gives H_r(n,m) model and component-size/local limit laws, not a joint finite covariance of isolated vertices with two-edge exact overlaps. López uses independent Bernoulli edge appearance and local neighbor distributions, not this fixed-m mixed motif statistic. Resultary search finds other motif/isolated covariance findings on nonidentical graphs or ensembles but no dominating exact nt=r² theorem. The initial finite factorial-moment identity is standard; the complete arithmetic sharp sign boundary and m-independent strictness remain independently useful. An unlocated general subhypergraph moment table might yield this by routine specialization, so bibliographic priority is not certified.

## value

PASS

V PASS. Isolation and prescribed edge-overlap counts are natural structural diagnostics in the canonical fixed-edge hypergraph model. Exact dependence can reverse despite unchanged edge budget; the integer threshold, absence of zero state, full parameter coverage and contrast with replacement sampling are motivated, rather than an arbitrary small-n census. The sign diagram is an exact nontrivial finite-size invariant useful for interpreting the joint behavior of coverage and clustering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
