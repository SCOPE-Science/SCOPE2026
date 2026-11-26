# Independent mathematical audit

## correctness

PASS

Verified the formal word theorem by a separate five-statistic elimination. For a suffix (a,b,c,d), write P=[b=bar(d)], Q=P[a=c], R=[b=d], S=P[c=bar(a)]. Over accepted words of length n≥4 count these four predicates and all words (total Y). Appending one letter sends (Y,P,Q,R,S) to (qY-P,Y-Q,R,Y-S,P-Q) using the same symbols for totals. Indeed only a P-suffix excludes any letter, then precisely bar(a). A new P requires x=bar(c), blocked exactly on Q. A new Q additionally requires b=d, which excludes old P. A new R requires x=c, blocked exactly on S. A new S requires x=bar(c) and d=bar(b), so counts P-Q. The length-four initial vector is (q^4,q^3,q^2,q^3,q^2), including q=2. For the length-four-onward generating functions, these updates imply (1-qz+z²)Y=q^4-q³z+z²Q and (1-z³)Q=q²+q³z-q²z²+z²Y-z³P with zP=q^4-(1-qz)Y. Eliminating gives exactly the displayed D_q and N_q. This checks the infinite recurrence, the initial coefficients and the empty-word convention without assuming the symbolic checker. A separate exact symbolic replay of the original state annihilator also passed. For the abstract four-symbol alphabet, any four-letter suffix can reach some constant suffix by appending four copies of a symbol t: each of the first three appends excludes at most one candidate t, and the fourth excludes none by the absence of complement-fixed letters. Reversal preserves admissibility and gives paths in the opposite direction. Constant suffixes t and s connect by runs whenever s≠bar(t), and if s=bar(t) one uses an intervening symbol from the other pair. There is a constant-suffix self-loop, so the graph is primitive. The Perron growth is at least sqrt(11): each state has ≥3 successors, at most one of which excludes a letter on the next step, hence ≥11 two-step walks. The recurrence makes the growth a positive root of the displayed polynomial. That polynomial is strictly increasing for λ≥16/5 (its derivative there is λ³(5λ−16)+3λ²−2λ+2). Bisection gives 3.75146484123868 and log₂ of it gives 1.90745403735, as claimed for formal word counts.

## originality

PASS

Best-of-knowledge pass for the explicit uniform fifth-order count in the fixed one-gap language over paired abstract alphabets. Rationality by finite pattern avoidance is routine and not credited. The closest checked exact formula is for a different local prohibition; the closest global constraint uses different hypotheses. The broader literature risk remains named below.

## value

PASS

The gap of one symbol is the first local case after adjacency for this paired-letter avoidance problem. The exact result determines every length and all paired alphabet sizes, revealing the same low-order recurrence even as the ordinary suffix space grows as q^4. This answers an exact counting question for a natural family and permits comparison with the adjacent rule; it is more than the generic existence of a rational series or a numerical count at one alphabet size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
