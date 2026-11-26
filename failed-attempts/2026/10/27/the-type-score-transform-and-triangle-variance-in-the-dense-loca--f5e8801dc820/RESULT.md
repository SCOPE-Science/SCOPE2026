# The type-score transform and triangle variance in the dense local order

## Finding
Let \(\mathbb L\) be the countable homogeneous dense local-order tournament. Fix any individually named nonempty finite induced subtournament \(P\) with \(n\ge1\) vertices. For \(v\in P\), write \(s(v)\) for its outdegree *within* \(P\). Let \(\mathcal S_1^*(P)\) denote the complete nonalgebraic one-types over these named parameters; for \(p\in\mathcal S_1^*(P)\), let \(d_P(p)\) be the number of parameters beaten by a realization of \(p\). Define the score and type-score polynomials
\[
S_P(z)=\sum_{v\in P}z^{s(v)},\qquad E_P(z)=\sum_{p\in\mathcal S_1^*(P)}z^{d_P(p)}.
\]
Then
\[
S_P(z)=z^{n-1}S_P(z^{-1}),\qquad
\boxed{E_P(z)=(1+z)S_P(z)}.
\]
In particular, there are exactly \(2n\) nonalgebraic one-types, and each occurs with multiplicity one in the geometric gap classification (the displayed polynomial groups them by outdegree). If a type is chosen uniformly among these \(2n\) types, its outdegree \(D\) has mean \(n/2\) and variance
\[
\boxed{\operatorname{Var}(D)=\frac{n^2+2}{12}-\frac{2c_3(P)}n},
\]
where \(c_3(P)\) is the number of three-vertex induced directed cycles of \(P\). These are exact equalities for every \(n\ge1\), not limiting distributions.

The variance is sharp over all parameter tournaments in the age of \(\mathbb L\): for odd \(n\), its minimum is \(1/4\), attained exactly when every parameter has score \((n-1)/2\); for even \(n\), its minimum is \(1/2\), attained exactly when half of the parameters have score \((n-2)/2\) and half have score \(n/2\). In either parity, its maximum is \((n^2+2)/12\), attained precisely for transitive \(P\). All extrema are attained by locally transitive tournaments.

## Assumptions and scope
A tournament has exactly one oriented edge between each two distinct vertices. It is *locally transitive* when the subtournaments induced by each vertex's in-neighbors and out-neighbors are transitive. The age of \(\mathbb L\) consists of these finite locally transitive tournaments; homogeneity identifies complete one-types over named \(P\) with admissible oriented one-point extensions of \(P\). Equalities to parameters are excluded throughout. The empty parameter set is deliberately excluded: it has one nonalgebraic one-type rather than the formula \(2n\).

Use the geometric realization on an oriented circle: the finitely many vertices of \(P\) can be placed at angles \(\theta_v\), with no two antipodal, and \(u\to v\) if and only if the clockwise arc from \(u\) to \(v\) is shorter than a semicircle. This is the classical circular representation of locally transitive tournaments, not a new assertion. Adding any further point away from the \(2n\) parameter and antipodal boundary points yields an admissible one-point extension. This remains valid when \(P\) is transitive and when some score values repeat.

## Proof
**All one-point types are distinct circular gaps.** The \(n\) parameter points and their \(n\) antipodes partition the circle into \(2n\) open gaps. The directions to the named parameters are constant in each gap. Every locally transitive one-point extension belongs to the age, and homogeneity realizes it over the *fixed* named copy of \(P\) inside \(\mathbb L\). Thus the gaps of that single ambient circular realization give all complete nonalgebraic one-types. They are distinct: suppose two gaps have identical orientation vectors. Moving from one to the other, each coordinate of this vector must flip an even number of times. For each parameter, its two flips occur exactly at its position and its antipode. One of the two directed arcs between the chosen gap representatives has length at most a semicircle, and hence cannot contain both boundary points of any pair. Thus identical vectors would force that short arc to cross no boundary at all, contradicting distinctness of the gaps. Therefore there are exactly \(2n\) types.

**Scores of the gaps.** For a parameter vertex \(v\), the gap immediately clockwise after \(v\) has outdegree \(s(v)\): it beats the same other parameters that \(v\) beats, and loses to \(v\). The gap immediately clockwise after the antipode of \(v\) has outdegree \(n-s(v)\): it beats \(v\) and each other parameter that beats \(v\). These are all \(2n\) gaps, so initially
\[
E_P(z)=S_P(z)+z^nS_P(z^{-1}). \tag{1}
\]

**Score reciprocity by level crossing.** As a point traverses the circle clockwise without hitting a boundary, let \(d\) be how many named parameters it beats. Crossing a parameter point \(v\) makes \(d\) decrease from \(s(v)+1\) to \(s(v)\). Crossing its antipode makes \(d\) increase from \(n-s(v)-1\) to \(n-s(v)\). Along a closed walk, for each integer \(j\), the number of downward crossings of the level pair \(j+1\to j\) equals the number of upward crossings \(j\to j+1\). Consequently
\[
|\{v:s(v)=j\}|=|\{v:s(v)=n-1-j\}|\qquad(0\le j<n).
\]
This proves \(S_P(z)=z^{n-1}S_P(z^{-1})\). Substitution into (1) proves the type-score transform.

**Triangle variance.** The transform says that the uniform type-score distribution is that of \(s(V)+B\), where \(V\) is a uniformly chosen parameter and \(B\) is an independent fair \(\{0,1\}\)-valued variable. Hence \(\mathbb E D=n/2\) and
\[
\operatorname{Var}(D)=\operatorname{Var}(s(V))+\tfrac14.
\]
In any tournament, each transitive triple has a unique vertex beating its other two vertices. Thus
\[
\sum_{v\in P}\binom{s(v)}2=\binom n3-c_3(P).
\]
Using \(\sum_v s(v)=\binom n2\) and expanding the squared scores gives \(\operatorname{Var}(s(V))=(n^2-1)/12-2c_3(P)/n\). The displayed triangle-variance identity follows.

**Sharp bounds.** Scores are integers averaging \((n-1)/2\), so their variance is at least zero for odd \(n\) and at least \(1/4\) for even \(n\), with exactly the indicated equality conditions. Regular cyclic tournaments (odd case) and near-regular circle tournaments (even case) realize these minima. For the even case, place \(n\) points at angles \(2\pi j/n+\epsilon j\), \(0\le j<n\), for sufficiently small positive \(\epsilon\), which resolves each antipodal pair in one direction and gives the required half-and-half scores. For the maximum, the sorted scores of any \(n\)-vertex tournament are majorized by \(0,1,\ldots,n-1\), since every set of \(k\) vertices spans at most \(\binom k2\) internally directed edges. Strict convexity of the square bounds the score variance by \((n^2-1)/12\), with equality precisely when the score multiset is \(\{0,1,\ldots,n-1\}\); such a tournament must be transitive. Adding \(1/4\) proves the asserted sharp type-score bounds.

## Verification
The standalone script `verify.py` uses no external modules. It exhaustively enumerates all labeled tournament orientations through order six, retains precisely the locally transitive bases, and compares the predicted type-score histogram with direct enumeration of all oriented one-point extensions. This covers 4,283 eligible labeled bases and separately checks score reciprocity, type counts, and the integer-scaled variance identity. An independent antipodal binary-word construction checks every word of lengths one through twelve (8,190 words) and directly enumerates the \(2n\) distinct geometric-gap vectors. Execute `python verify.py`; recorded output is in `verification_output.txt`. The computation does not prove the infinite all-order statement; the circular and crossing arguments do.

## Relationship to prior work
Brouwer's 1980 paper establishes the cyclic interleaving of parameter points with opposite boundary points and enumerates isomorphism classes of locally transitive tournaments; this geometric representation is explicitly used rather than claimed as new. Lachlan's 1984 classification supplies the homogeneous-tournament setting. Coregliano's 2015 paper studies the same local-transitivity class and balanced carousel tournament limits, including the structural cyclic-order theorem. The present statement is the exact finite-parameter *degree-refined one-type* transform, the score-reflection lemma and the resulting triangle-variance identity and sharp bounds. These are more specific than counting abstract isomorphism classes or asymptotic tournament densities; the essential additional observation is the closed-walk level-crossing equality at every integer degree. They may be accessible as short consequences of Brouwer's framework, so any claim of originality is restricted to these explicit refinements and should be checked independently.

## Limitations
This theorem concerns one new point and finite locally transitive parameters only; it does not give a corresponding transform for arbitrary tournaments, higher-arity types, or a uniform measure on realized points. Equalities to named parameters add \(n\) algebraic types and are excluded. The score distribution is not a complete isomorphism invariant of locally transitive tournaments. The sharp bounds assert equality profiles, not uniqueness of the tournaments attaining the minimum. Earlier cyclic representations imply portions of the argument; absence of an identical printed formula in inspected literature is not a proof of novelty. No independent external scientific audit has been carried out.

## References
1. A. E. Brouwer, *The enumeration of locally transitive tournaments*, Stichting Mathematisch Centrum, ZW 138/80 (1980), full text: https://ir.cwi.nl/pub/6805/6805D.pdf.
2. A. H. Lachlan, *Countable homogeneous tournaments*, Transactions of the American Mathematical Society **284** (1984), 431–461, DOI: 10.1090/S0002-9947-1984-0743728-1.
3. L. N. Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124, initial public submission 2015-03-13, https://arxiv.org/abs/1503.04124.
