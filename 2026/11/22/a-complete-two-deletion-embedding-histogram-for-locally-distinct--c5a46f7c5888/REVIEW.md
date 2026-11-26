# Independent mathematical audit

## correctness

PASS

An indexed embedding maps position i to the window [i,i+2]. Candidate sets for distinct i are disjoint: intersecting windows have source distance at most two and the matching symbol would have to be equal. A host with an embedding has all m sets nonempty and at most two surplus positions. Consequently a host with at least three embeddings has one size-three set or two size-two sets; every host position is then in a candidate set. A size-three set occupies the whole three-site window; any other singleton must occur on the correct side of the window (some embedding exists and no singleton is inside it). This is exactly tripling one occurrence of a source letter, even if that letter recurs elsewhere. Two size-two windows at distance at least two cannot invert their picks because their ranges meet at most in a single position and the sets are disjoint. Compatibility with fixed singleton neighbors therefore factors, yielding four embeddings exactly when both duplicated positions have both choices available, forcing adjacent copies by exhaustion of host positions. At distance one the four positions fill one block starting with a and ending with b; aabb has four indexed choices and abab has three. The locations in each constructed host are uniquely retrievable from its surplus-candidate indices, so none of these host families overcounts. This includes m=1, where only tripling occurs, and m=2, where distance two is vacuous. Greedy scanning counts the ordinary insertion sphere S; double-counting pairs (host, embedding) gives Z=q^2*binom(m+2,2). Thus Z-S=N2+2N3+3N4 proves the remaining histogram, including zeros, by algebra. Uniform input and uniformly chosen masks give posterior weight e/Z. The entropy correction numerator is 2q*m^2+O_q(m) and denominator (q^2/2)*m^2+O_q(m), so the limit correction is 4/q with the stated uniformity. Sequentially choosing distinct next letters gives q(q-1)(q-2)^(m-2) targets for m>=2 and forces period-three continuation for q=3. No global entropy extremum follows or is claimed.

## originality

PASS

Best-of-knowledge pass for the complete nonbinary locally distinct histogram and its exact high-multiplicity structural classification. The one-embedding row has an earlier exact derivation, and insertion-sphere size, history normalization, and the general posterior-entropy identity are prior. These are not separate novelty claims.

## value

PASS

The fixed received-word embedding spectrum is the actual posterior uncertainty in the exact-two-deletion channel. A locally distinct target is a natural nonbinary way to suppress short repeats while still allowing repeated symbols later. The exact support and high-multiplicity classes quantify what ambiguity remains, including the adjacent alternating insertion and a posterior entropy deficit of 4/q bits in the long-target limit. This is more than recalculating the prior sphere size or the prior single-embedding count and does not assert entropy maximization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
