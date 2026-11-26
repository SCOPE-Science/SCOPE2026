# Independent mathematical audit

## correctness

PASS

In the linear word P^k# with q,k>=2, distinct letters, and r_i>=2, a factor containing # occurs only once. Every other nonunary factor has a unique phase modulo |P|, since its first ordered letter change fixes that phase. It is right-maximal exactly when it is a suffix of P^(k-1): it then occurs both before the final # and at the previous period boundary before a_0. A unary factor shorter than its run has the self follower and its cyclic successor, and if it belongs to the last run it can also have #. The full unary last run has the two boundary followers a_0 and #, whereas the other full unary runs have only one. These cases, including the empty word, place every extension under a listed candidate in suffix order. The candidates are all extensions and have distinct last two symbols (the two long ones end in a_(q-1)a_0 and a_(q-1)#), so none is a suffix of another. This also supplies the suffix direction intended in the aside about a_0 in proof step 2. Each short candidate has one end offset per period, distinct between the first and last positions of any run by r_i>=2. The long candidates have just the last-period first position and the terminal position as their respective single endings. Every smallest set chooses one from each disjoint end class, giving 2q+1 positions and k^(2q-1) sets. For attractors, the q+1 one-letter factors give the lower bound. Choose each last run position of the first period and #. A nonunary factor without # can be shifted so that its first ordered change aligns with the first-period occurrence of that change: the leading unary segment fits in the chosen first-period run, so the shifted occurrence stays inside the text and meets the selected run end. Unary factors end-align there, and marked factors meet #. The supplied literal-substring verifier and captured output were inspected, not run: 246 parameter instances, 12358 extensions and four direct counts of minimum sets corroborate the proof; these are not infinite certificates.

## originality

PASS

The general correspondence between supermaximal extensions and optimum suffixient sets and the attractor comparison are not the distinct contribution. The supported contribution is the explicit SRE list and exact minimum-set census for the entire marked distinct-run family. The closest retrieved sources give general methods, unrelated symbolic families, or finite binary coverage rather than this parameterized theorem.

## value

PASS

Distinct contiguous letter runs isolate local within-run branching from periodic phase and sentinel branching, making this a natural family in which to understand exact suffixient complexity. The theorem does more than compute the size: it exhibits every optimum, explains why varying run lengths does not affect their number, and distinguishes this suffix-ending condition from the attractor invariant on the same text.

The dated certificate retains the supplied scientific assessment, sources and limitations.
