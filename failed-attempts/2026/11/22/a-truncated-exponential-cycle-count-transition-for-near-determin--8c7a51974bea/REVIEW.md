# Independent mathematical audit

## correctness

PASS

The initial zeros are fixed in stable rank; after the first nonzero, every zero at index i maps to i minus the positive number of earlier nonzeros. Thus every other cycle uses at least one nonzero and the deterministic sandwich holds, including the all-zero word. The initial run has tail (1−ε)^j for 0≤j≤n. For ε>0 it couples to the floor of an exponential of rate −log(1−ε), capped at n; capping and rounding cost at most 1/n after rescaling. The pathwise difference from K/n costs at most E[R]/n=ε. On [0,1] the Wasserstein distance between capped exponentials is the integral of the absolute survival-function difference; |exp(−at)−exp(−bt)|≤t|a−b| gives the exact factor 1/2, also at rate zero. For nε bounded, −n log(1−ε)=nε+O(nε²). For nε→∞ and ε→0, the initial run is o_P(n) and E[R]/n→0. In the finer regime its ε-scaled truncated geometric law tends to Exp(1) because nε→∞, and E[εR]=nε²→0. If ε=0 the word gives K=n exactly. The finite checker was inspected, not executed.

## originality

FAIL

The claimed first-defect mechanism and its law are covered by the combination of two directly relevant existing results in Guerder, not merely by the availability of a general exact generating function. Proposition 3.1 identifies the fixed-point count of the least symbol with the exact truncated-geometric law, and Proposition 3.11 identifies all longer cycle labels as primitive, making the deterministic error bound immediate. The explicit near-deterministic theorem is not printed there; the stated error and scales follow by elementary capped-geometric coupling and rescaling of these results.

## value

PASS

As a mathematical description, the singular regime is worth understanding: it gives a macroscopic non-Gaussian fluctuation with an endpoint atom, and gives a uniform estimate independent of the rare alphabet, across more than one scaling. The first-defect interpretation is useful even though it does not supply a scientifically distinct claim from the cited exact structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
