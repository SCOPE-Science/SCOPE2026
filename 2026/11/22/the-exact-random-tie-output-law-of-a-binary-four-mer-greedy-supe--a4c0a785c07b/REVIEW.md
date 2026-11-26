# Independent mathematical audit

## correctness

PASS

A literal multiset of component strings is a sufficient state. For each ordered pair of distinct component positions the proper overlap is tested; all maximizers, including zero if necessary, receive equal conditional mass and are counted separately even when leading to the same next state. Each transition reduces component count by one, so exact rational recursion over the resulting states is exhaustive. Fresh literal replay, not the frozen endpoint reduction, evaluated 418 states and exactly reproduced every listed mass, normalized to one. Weighting by length gives 3209609/249480. No output above 17 occurs; one legal path to 17 uses overlaps 3,3,3,3,2,1,0 and ends at 00001000100110101. A word of length m has m−3 four-mer positions, so eight distinct four-mers require m≥11, attained by 00101000011. Thus length 17 alone exceeds (3/2)·11. Reversal reverses every ordered pair and its merged word, while complementation preserves pair order; each maps maximal-overlap choices bijectively at every state and preserves probabilities.

## originality

PASS

Best-of-knowledge support is for the full exact stochastic output-length law of the specified instance, not the previously indexed existence, minimal input size, orbit, optimum 11, maximum 17, or generic tie recurrence. The strongest distinct same-day records cover those deterministic endpoints on exactly this input. A same-day random-tie study computes a law for all binary three-mers, not this subset of four-mers. No compared statement supplies the exact probability distribution for this input without new state evaluation. The common catalogue date does not establish relative priority.

## value

PASS

The instance is motivated by the smallest strict 3/2 binary four-mer obstruction and the sharp extremal ratio, not by selecting a random small parameter slice. The exact stochastic invariant determines the robustness of that genuine worst-case obstruction to a natural tie rule: the failure probability is about 0.698%, and the full law quantifies the other outputs. This is additional usable benchmark data for randomized tie behavior, not a recomputation of the deterministic maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
