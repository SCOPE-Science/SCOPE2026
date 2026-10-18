# Independent mathematical audit

## correctness

PASS

Set p=e/(e−1), z=1+log(1−u/p)∈(0,1). Inverting the already defined FEx-G CDF gives (1−w)^w=z. Writing t=log(1−w)<0 transforms it to t e^t−t=−log z. H(t)=t(e^t−1) strictly decreases from +∞ at −∞ to 0 at 0− because H′=e^t(1+t)−1<0. Thus t is the unique negative r-Lambert W_{−1} branch and w=1−e^t; substituting G(x)=1−(1−x^a)^b gives Q=[1−exp(t/b)]^(1/a). This is mathematically correct for 0<u<1 and continuous strictly increasing baseline G.

## originality

FAIL

The original Eldemery et al FEx-G work supplies the full CDF and explicitly its already-inverted scalar relation w log(1−w)=log z; Mező–Baricz (2015/2017) define W_r as precisely the inverse of t e^t+r t and analyze real branches. The alleged exact FEx-G quantile is obtained immediately from that published relation by the one-step substitution t=log(1−w), setting the existing r parameter to −1 and composing with baseline G^{−1}. The branch restriction t<0 follows immediately from 0<w<1 and monotonicity of a known scalar function. The Kumaraswamy formula is algebraic substitution. The complete submitted claim is mathematically implied by these two prior statements, even without an identical named quantile formula. This is a covered corollary, not a distinct original theorem.

## value

FAIL

Although a callable special-function wrapper may help implement distribution quantiles, the record adds no new nontrivial bound, asymptotic, algorithmic complexity, structural classification, or unknown invariant: it merely labels the original article’s already explicit scalar inverse via the established generalized Lambert inverse and restates its branch. Numeric root finding remains necessary and no speed or stability gain is proven. Under the common value bar, this is routine reparameterization/notation of already published mathematics, not a substantive mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
