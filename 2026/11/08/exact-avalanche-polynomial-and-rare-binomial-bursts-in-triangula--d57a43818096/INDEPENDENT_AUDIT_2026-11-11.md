# Independent mathematical audit

## correctness

PASS

For undirected K_{1,1,n} with one spine endpoint sink and n>=2, a stable recurrent state has spine height h in 0..n, tip heights eta_i in {0,1}. Dhar forbidden-subconfiguration criterion is equivalent to h>=z=#{i:eta_i=0}. Counting sums binom(n,z)(n-z+1)=(n+2)2^{n-1}. Addition at spine h=n topples spine once plus exactly height-one tips; h<n gives zero. At a tip: eta_j=0 gives zero, eta_j=1,h<n gives tip only, eta_j=1,h=n gives tip then spine then all other height-one tips. Every nonsink topples at most once. This exhausts source cases and yields the stated multivariate polynomial. Specializing yields the given binomial tails, E T=1 at either specified source, exact variances and rare conditional Bin(n,1/2)-scale large events. Independent enumeration of all recurrent states and individual legal topplings for n=2..6 exactly matched the coefficientwise multivariate formula. Not evidence of infinite proof, which is the burning-plus-case analysis.

## originality

PASS

No checked pre-existing result yields the complete n-parameter all-source, toppling-vector polynomial for triangular books. Cori–Micheli–Rossin derive tree avalanche polynomials, Austin et al. explicitly classify trees, cycles, complete graphs and wheels, distinct from K_{1,1,n}. Related fan/friendship/book-named findings concern different graphs or different chip-firing dynamics. The burning lemma and general avalanche generating polynomial are prior; novelty is the all-size exact thagomizer profile.

## value

PASS

The triangular book is a natural edge-sharing triangle family. Exact multivariate firings reveal a pronounced distributional effect hidden by first moments: E T=1 identically, but rare order-n binomial bursts produce variance growing linearly in n, with exact weights and which-tip firing sets. This complete natural classification is more useful than a single known moment or arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
