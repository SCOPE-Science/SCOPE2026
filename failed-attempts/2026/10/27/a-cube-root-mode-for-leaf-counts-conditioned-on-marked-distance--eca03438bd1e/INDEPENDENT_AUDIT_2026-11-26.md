# Independent mathematical audit

## correctness

PASS

With r=k+1 fixed path vertices, the forest-completion count is r n^(n−r−1), since the relevant complete-graph minor is nI−J with a single eigenvalue r; the empty minor at r=n gives 1. For a specified off-path leaf, deletion preserves the root set and gives n−1 attachments; for a marked leaf, deletion removes an isolated root. The resulting probabilities are q^(n−r−1) and (r−1)q^(n−r−1)/r (q=(n−1)/n), respectively, and the internal vertices are excluded. At r=n the formula evaluates to 2, as required for a spanning path. The fixed-path mean depends only on its length. Subtracting consecutive expressions gives the stated increment with sign of 2(n−1)−k(k+1)². This cubic is strictly increasing; the first transition is positive and the last difference is (3−n)/(n−1) when n≥4, with just a two-point tie at n=3. The integer equality gives exactly the claimed two-point plateaus; the index crossing of a monic cubic at 2(n−1) gives the cube-root asymptotic for either maximizing distance. An individual endpoint's probability strictly increases because both k/(k+1) and q^(n−k−2) increase. The uploaded finite Prüfer check was inspected, not executed, and is not required for the proof.

## originality

FAIL

Two distinct records already in the Resultary corpus state this exact global mean, increment/sign criterion, complete tie rule and cube-root mode in the same uniform unrooted labeled-tree model with two fixed marked vertices. The 10/13 record also uses the same path-conditioned matrix-tree/deletion proof, and the 10/18 record gives the increment in exactly the claimed range and normalization. The marked-endpoint contrast uses the prior endpoint law. This is demonstrable equivalent coverage, not an inference of immutable posting priority from catalog dates or a failure based on searches unavailable.

## value

FAIL

The distinction between typical distance and the conditional-mean maximizer is mathematically meaningful, but this submission adds no new useful boundary, explanation or theorem to the existing exact calculations. The same proof and all claimed effects are already present; merely recasting the coefficient or recomputing finite checks contributes no surviving result of independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
