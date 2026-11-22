# Independent mathematical audit

## correctness

PASS

Gale evenness makes every even-dimensional cyclic-polytope facet exactly a k-matching of the label cycle C_n. A minimum transversal is complement Y with induced matching number <=k-1. For proper cycle-induced path unions, alpha(Y)=|Y|-nu(Y) <=floor(n/2), so |Y|<=floor(n/2)+k-1 and equality forces a maximum independent set with k-1 additional vertices. Odd-n cyclic run encoding splits into t=u or t=u+1 and gives n[binom(h-1,r)+binom(h-1,r-1)] = n binom(h,r); even n has two alternating independence sets, each with binom(h,r) choices. Independent enumeration generated facets from literal Gale parity, enumerated all transversals and checked minimum families for n=3..11 and all admissible k. All-parameter proof is structural, not inferred from tests.

## originality

FAIL

FAIL: Published stronger Resultary theorem "The complete facet-transversal polynomial and a Poisson deletion window for even cyclic polytopes" establishes H_n,k(s)=n/s sum_{a=0}^{k-1} binom(s+a-1,a)binom(s,n-s-2a) for EVERY s and n,k, and its full proof gives the circular gap matching-number characterization. The present minimum-transversal count equals the known polynomial coefficient at s=ceil(n/2)-k+1, while its equality-family description follows by specializing the same gap constraints/known matching versus independence equality. The published stronger statement explicitly disclaims originality of classification/count of minimum transversals. Existing Briggs–Dobbins–Lee min SIZE alone would not cover this, but complete published enumerator decisively does.

## value

FAIL

FAIL as a new contribution: The full optimizer count and parity jump are an already published special coefficient of the complete size polynomial, and the claimed classifier follows directly from the already published induced-cycle matching/gap analysis. No independent mathematically motivated unknown invariant or nonmechanical remaining result survives this coverage. Its elementary correct proof still has pedagogical value, but cannot be treated as a valuable novel finding under the required standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
