# Independent mathematical audit

## correctness

PASS

For no-repeat survival a_n, conditioning on k observations at distinct atoms yields a_n=Σ_{k≤n} n!/(n−k)! e_k(p)q^{n−k}. Since Σp_i<∞, the product ∏(1+p_i z) converges normally on compact sets; multiplying by e^{qz} gives the entire EGF. Zeros recover masses with multiplicity, and normalization recovers q. The local logarithm gives C_r=Σp_i^r. For ≤m atoms, C_2,...,C_{2m+1} are the first 2m moments of ρ=Σp_i²δ_{p_i}; the signed difference of two such measures has ≤2m support points, so a Vandermonde argument proves uniqueness. The proof covers purely nonatomic and finite/infinite atom boundaries.

## originality

FAIL

Camarri–Pitman's complete 2000 primary paper already gives the exact first-repeat survival law for arbitrary finite/countable discrete p as k!e_k(p), formula (2). Its introduction credits Stein 1990 with Newton-polynomial treatment of the same generalized birthday law. Taking the exponential generating function of the published formula gives ∏(1+p_i z), whose zeros recover the masses; the mixed-law e^{qz} factor is the standard independent nonatomic/no-collision term obtained by conditioning or infinitesimal-atom limit. The finite-horizon statement is the standard finite moment/Vandermonde inversion of the same collision power sums. These are direct implications of the prior exact law plus elementary generating-function algebra, not a new independent theorem merely because an inverse phrasing and dust parameter are absent.

## value

FAIL

The proposed invariant is natural, but this package supplies no unknown exact answer or nontrivial boundary beyond reformulating Camarri–Pitman's complete coefficient law and standard Newton/Vandermonde inversion. The dust component is invisible to repeats except through normalization, which follows immediately from the same factorization. Under the standard, a correct renamed or immediate corollary of stronger prior work is not a new survey-worthy gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
