# Independent mathematical audit

## correctness

PASS

The sign word and c₀ are a bijective encoding exactly when 3 divides W=2p−n. A move exchanges the two signs incident to the recoloured site and is available exactly when they differ. This gives the sector sizes and the edge count by dividing the count of legal site choices by two. All-equal sign sectors consist of three frozen states (including the n=3 cases). The twisted height representation h_(i+n)=h_i+W is parity-consistent because W≡n mod 2. Its projective ambiguity is translation by 6, not 3, and a move lifts uniquely to a peak lowering or valley raising by 2 on one residue class. For H≤T, a coordinate with positive gap can be followed down until a valley; the gap does not decrease because both profiles have unit slopes, and both signs prevent a descending circuit across a full period. Raising the valley retains the bound, and the total integer gap drops by two. The pointwise minimum of two lifts retains parity, twist and Lipschitz bound, proving mixed-sector connectivity. In a closed projected walk the lift displaces all heights by 6t; its length is at least 3n|t| and congruent to 3nt mod 2. For existence through an edge, orient it as a raise H→H' and complete monotonically to H+6 in the lifted graph. There are 3n total raises, and any repeated projected colour before completion would require a uniform shift of at least 6, already costing the entire length. Thus the cycle is simple. The colour-sum mod 3 gives a graph 3-colouring; the odd cycle gives equality when n is odd, and a connected nonempty bipartite sector has chromatic number two. One minority sign gives a connected 2-regular sector of size 3n. Otherwise the two boundaries in a two-block sign word are nonadjacent recolouring sites and commute to give a four-cycle; triangles are ruled out by the closed-walk bound. A backtrack gives length two, so the stated nonlazy periods follow. The analytic replay is RESULT.md Steps 1–5. Both uploaded verifiers were read, not executed; their rooted odd-walk tests and unprescribed monotone lifts are finite corroboration, not a certificate for every edge.

## originality

FAIL

The conclusion is covered as a specialization of the absolute-height path lemmas of Johnson et al., even though their headline shortest-path theorem does not give a nontrivial distance from a colouring to itself. The relevant prior construction handles an arbitrary admissible terminal height k before minimizing over k. It yields the sharp length and the prescribed-edge completion by taking k=6 at a suitable focal vertex. The remaining counts and small girth cases are immediate sign-encoding consequences; no separate valuable new assertion is established.

## value

FAIL

Odd girth through each edge is a natural and useful quantitative invariant, and the specialized proof is clear. But the sharp numerical answer and the prescribed-edge construction already follow directly from an existing constructive metric lemma; the remaining ordinary-girth and count observations are routine. The frozen finding adds a readable specialization rather than a separate useful new mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
