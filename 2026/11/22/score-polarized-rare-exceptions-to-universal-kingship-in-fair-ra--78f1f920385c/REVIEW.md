# Independent mathematical audit

## correctness

PASS

The event that y has no outgoing path of length at most two to x is exactly that x covers y. A fixed x covering y requires x→y and independently forbids (0,1) at every remaining label; conditioning therefore leaves iid uniform (1,1),(1,0),(0,0) marks and fair independent edges among the remaining labels. In the second Bonferroni sum, shared-coverer and shared-covered pairs have 5/8 allowed patterns per outside label; chains have 4/8; opposed directions are incompatible; disjoint endpoints have 9/16. Independently enumerated both the outside patterns and the internal orientations (2/8 for either same-role overlap, 1/8 for a chain, 0/2 for opposition, 6/64 for disjoint endpoints). Replay: python3 /workspace/frozen_review_arithmetic.py (requires SymPy; no frozen code executed). Summing O(n^3) or O(n^4) pairs and dividing by mu=E W=n(n-1)(3/4)^(n-2)/2 gives the stated bound, including the negligible chain term. Multiple covers have unconditional probability at most the Bonferroni sum. For the full marked tournament the total-variation identity is exact: on a tournament T with W>0 the chosen mark has mass P(T)/P(F), whereas sampling a uniformly chosen specified cover first gives mass P(T)/mu for each valid mark at T. Their total overlap is P(F)/mu, and projection to the pair and array can only decrease TV. Scores under the reference are (1+A+B,A), giving the stated iid bivariate CLT with covariance (2,1;1,2)/9 and O(1) centering shifts. Other vertices have Bin(n-3,1/2) scores on the outside subgraph plus at most two, so a union of Hoeffding bounds separates all of them from the two marked scores with probability 1-o(1); it does not require independent scores across outside vertices. TV transfers the separation and conditional uniqueness identifies the sole covered vertex. The claim is rank recovery given the rare event, not a test for its existence from the scores of an unconditional tournament. Read the frozen verification note and enumerator; its tests are finite and do not prove these limiting assertions.

## originality

PASS

Credit the earlier obstruction theorem for prevalence, multiplicities and, by division, conditional uniqueness and its scale. The marked TV rate is also a direct change-of-measure consequence of the known prevalence deficit plus the specified-cover product law; it does not independently establish priority. The supported distinction is the conditional score profile, especially the joint recovery of both exceptional labels as the global strict degree extremes (and the Gaussian fluctuations of their scores). The earlier verified theorem is about path obstructions and their endpoint coincidences, not order-statistic recovery over all vertices. No checked statement supplies the conditional score recovery result.

## value

PASS

The useful output is structural identification, not another small improvement in the probability of universal kingship. Given a failure, one can typically locate both labels of the exceptional covering relation from the strict global score extremes without checking all pairwise length-two paths. The theorem also distinguishes its strongly polarized bivariate conditional score law from the fair, near-half scores of the rest of the tournament. These claims have precise scope and do not assert that an unconditional tournament's extreme scores certify failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
