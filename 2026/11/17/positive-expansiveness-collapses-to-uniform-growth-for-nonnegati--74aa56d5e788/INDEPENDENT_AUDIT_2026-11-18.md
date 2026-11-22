# Independent mathematical audit

## correctness

PASS

The exact Lp norm change of variables gives the minimum modulus exp(m_a(t)) for m_a(t)=inf_s int_s^(s+t) a, continuous in s and superadditive in t. For nonnegative a, total mass divergent iff each nonzero orbit diverges by monotone convergence, hence kinematic positive expansiveness via Huynh Theorem 3.3. If m(L)=c>0, splitting t=kL+r gives m(t)>=(c/L)t-c and uniform exponential lower bound; Huynh Theorem 4.2 gives Bowen–Walters positive expansiveness. Conversely if m(N)=0 for every integer N, choose intervals with int a<1/N and f_N=phi((x-s_N)/N): ||f_N||~N^(1/p), ||f_N prime||~N^(1/p-1), ||a f_N||^p<=||a||_infty^(p-1)/N. Therefore ||A f_N||/||f_N||->0, and 0 in approximate generator point spectrum contradicts Huynh Theorem 3.6. Generator coercivity follows comparing T(L)f-f to integral T(s)Af and bounding ||T(s)|| by exp(Ms). Superadditive Fekete limit alpha=sup m(t)/t is sharp; a(x)=x/(1+x) has m(t)=t-log(1+t) and no endpoint constant at beta=1. Separately checked normalization and the two monotone example integrals; M=0 case is trivial shift. Analytic proof covers all finite p, not a numerical search.

## originality

PASS

Huynh proves abstract kinematic criterion, approximate-generator obstruction, sufficient uniform exponential expansion, and Example 4.6 for a constant scalar multiple of the right translation; those are credited. The audited statement handles arbitrary bounded nonnegative *spatially varying* potential and proves necessity of a uniformly positive lower interval mass with an explicit normalized approximate-null construction, so Bowen expansiveness collapses to uniform growth within that family. Huynh abstract hierarchy allows strict separation in general, and his constant-weight example does not imply this full family classification. Older weighted-advection spectral mapping addresses different spectral questions, not a located exact Bowen time-change classification.

## value

PASS

Provides an explicit necessary-and-sufficient criterion for a natural infinite-dimensional semigroup family and resolves an actual distinction between two meaningful dynamical expansiveness notions. The nontrivial lower-interval-mass to generator-coercivity converse, sharp growth-rate supremum, and nonattainment counterexample are useful for operator-semigroup stability; more than merely substituting a constant in Huynh’s example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
