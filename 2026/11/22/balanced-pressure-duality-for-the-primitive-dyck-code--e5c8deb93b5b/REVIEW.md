# Independent mathematical audit

## correctness

PASS

In a finite core all complete excursions contribute zero signed sum and the two end fragments are uniformly bounded; that interval bound survives closure and integration gives exact balance. For entropy density, mixing the target with a small amount of fair Bernoulli makes all block probabilities positive without changing balance or significantly lowering entropy. Its stationary k-step approximation matches the required cylinder probabilities for large k, is mixing because the full de Bruijn graph is positive on its allowed edges, and has entropy no smaller than the approximated process. The typical-word step gives exponentially many words of the desired empirical frequencies and |signed sum|<=δm. Selecting one signed-sum class loses only a factor O(m); balancing by appending at most δm symbols, rotating at a height minimum, and wrapping with + and − gives primitive equal-length generators with at most L preimages each. The distortion of fixed block frequencies is O(δ+1/m), since rotation changes cyclic frequencies by zero and changes at the padding/wrapper and concatenation boundaries are bounded by the block length. On concatenations the global lowest height identifies generator boundaries (every proper prefix is strictly above it); the randomized fixed length phase and iid generators therefore yield entropy log|E|/ℓ. Choose δ smaller than the positive Markov entropy and then large m to obtain the lower-entropy approximation. The pressure limit follows for all continuous potentials; concavity and upper semicontinuity of constrained free energy give a supporting slope at the interior frequency 1/2, so the multiplier minimum is attained. For pair potentials, stationarity and balance reduce the joint law to one flip probability; conditional entropy is optimized by the symmetric Markov chain. The Perron root for the full shift is at least sqrt(e^a e^d)+e^((b+c)/2) with equality iff a=d. The finite renewal root follows from the cyclic transition counts and Narayana numbers (including the sole semilength-one generator). At the root it is weighted free energy, not bare name entropy, that the Bernoulli weights optimize. Inspected the finite code and verification notes; no frozen script executed.

## originality

PASS

The code, its full-shift closure and unique decoding, qualitative exhaustion of sequential pressure, and the unweighted entropy limit are established antecedents. The distinction supported by the inspected sources is identifying the entire entropy-lower accessible family of invariant measures and thus the sequential-pressure functional for every continuous potential. The nearest-neighbor formula is a consequence of that identification, not a new transfer-matrix or Narayana formula.

## value

PASS

Topological density of the cores in the binary full shift does not say what free energies they approximate. The theorem identifies a natural, exact surviving measure constraint, proves entropy approximation even for nonergodic targets, and resolves when a continuous potential can recover full pressure. The full nearest-neighbor equality locus supplies a concrete strict-gap application beyond the previously understood zero potential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
