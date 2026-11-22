# Independent mathematical audit

## correctness

PASS

For 1/2<p<1, θ=2p−1 in (0,1), integer d>=3, set k=2(d−1), a=k^{p−1}, b=sqrt(1−a²), x_{i,±}=a e0±b ei, source -e0, and all unit outgoing sinks. Unit vectors satisfy sum x_i=k^p e0, so weighted equilibrium and star degree k+1=2d−1 hold. Every sink subset I of size j has squared vector-sum j²k^{θ−1}+s(I)(1−k^{θ−1}), where s(I) counts singly-selected orthogonal pairs and is bounded by min(j,k−j). For j<=k/2, concavity of j^θ and the threshold k^θ(2^{-θ}−1/2)>=1 establish maximal subset norm²<=j^{1+θ}; for j>=k/2 the convexity inequality t^{θ−1}−1>=(1−θ)(1−t) and k^θ> =4/(1−θ) establish the same. For any finite single-source admissible network with strictly concave p-power cost, a cycle-free oriented tree competitor may be chosen, and pairing each edge with its downstream sink subset yields calibration j_e^p||z_e||>=sum_{i∈S_e}<x_i,z_e>; telescoping sums along paths yield cost>=k+k^p. The constructed star has exactly k+k^p cost, proving GLOBAL optimality (not merely stationary). Independent recomputation of maximal subset inequality for admissible p=.7,.75,.85,.9 and even k=116,64,42,44 respectively corroborates. The stated high-d threshold is sufficient, not claimed sharp; finite subsets cannot certify the universal parameters without this analytic bound.

## originality

PASS

PASS best-of-knowledge for the explicit asymptotic 2d−1 star-degree lower bound at every fixed p in (1/2,1). Cherkashin’s general degree d+1 construction is strictly weaker; Volz et al supply a universal star optimality criterion but no such paired orthogonal feasible configuration; Teplitskaya lists high-dimensional degree improvement as a current problem. Unindexed previously known orthogonal-pair constructions remain a priority risk, heightened by lack of institutional full text.

## value

PASS

An explicit family of globally optimal branched transport networks nearly doubling the previously exhibited linear-in-d degree is a natural response to a stated open high-dimensional Gilbert–Steiner question. The proof is not a local angle/stationarity condition: it supplies all-subset inequalities and a global calibration. Even as a lower bound without optimality of coefficient two or endpoint cases, it provides a consequential geometric construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
