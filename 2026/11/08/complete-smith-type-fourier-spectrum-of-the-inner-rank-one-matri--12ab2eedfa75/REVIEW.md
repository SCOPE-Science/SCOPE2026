# Independent mathematical audit

## correctness

PASS

The nonzero inner-rank-one matrices partition by common p-adic valuation into primitive outer-product layers of size U_n=p^(3n-3)(p-1)(p+1)^2. Character orthogonality on primitive vectors, followed by Smith reduction B~diag(p^a,p^b), gives the five explicit nonzero local character-sum cases, whose layer sum yields the four-piece lambda_(a,b) formula in RESULT.md. Smith-type multiplicities follow from invertible and primitive rank-one orbit counts and exact determinant valuation differences. All types sum to p^(4k); diagonal a=b<k and off-diagonal a<b<k eigenvalues are negative with magnitudes >=p+1, while b=k types are positive and larger. Equality of abs lambda with p+1 is precisely a=b=0. An independent implementation constructed adjacency sets and full four-dimensional DFT, matching all Fourier multipliers and multiplicities for (p,k)=(2,2),(2,3),(2,4),(3,2) (77,338 cumulative independent assertions). The all-depth result relies on the proved orthogonality and Smith count, not tests.

## originality

PASS

Huang 2017 arXiv:1705.07083 studies the identical inner-rank-one graph at d=2 over residue rings, but its inspected complete 17-page paper proves graph independence, clique, chromatic and core parameters, not adjacency Fourier eigenvalues. Watanabe 2026 arXiv:2607.21913 gives a full Smith-type eigenmatrix on Galois rings of LENGTH TWO only, implying possible k=2 overlap explicitly disclaimed. Neither source covers arbitrary k>=3 or the exact depth-independent least singular value p+1. Originality remains conditional on older inaccessible ring character-table sources.

## value

PASS

An exact all-depth spectral multiset and the surprising uniform inverse norm 1/(p+1) for natural additive rank-one matrix convolution are intrinsic operator invariants despite vertex degree and volume growing exponentially. The unique minimizer Smith type identifies the extremal Fourier frequencies; not just an already known graph valency or arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
