# Independent mathematical audit

## correctness

PASS

Writing S for the squared Frobenius norm, sign averaging gives second moment S/n. In the fourth moment only a repeated cell and products of two disjoint cells survive, with probabilities 1/n and 1/[n(n-1)] and pair multinomial factor 6. For normalized squared masses, T is their squared sum, P the unordered colliding-pair sum and D the unordered disjoint-pair sum. Then T+2P+2D=1, so K=n-2nP+2n(4-n)D/(n-1). For n≥4 this gives the upper bound and isolates partial matchings at four and singletons above four. At n=2,3, repartitioning the total mass of two colliding positive cells gives a strictly convex one-variable objective (their joint term in D is absent), so a maximizer has matching support. On a matching K=3n/(n-1)+n(n-4)T/(n-1), maximized only when T=1/n, i.e. a full equal-mass matching. For the lower bound the variance of the squared linear form is the permutation variance of the selected squared-mass sum plus 4/[n(n-1)] times the unnormalized disjoint-pair sum. Zero of the latter forces a star; zero of the former then forces all n entries in that row/column to have a single positive absolute value. The interval follows by connectedness. For Banach–Mazur distance, averaging the two squared norm inequalities over signed row and column actions preserves them and turns any candidate quadratic form into a scalar Frobenius form, by sign elimination of off-diagonal terms and transitivity on entries. This proves optimal distortion with precisely the fourth root claimed. All steps use n≥2, real matrices, and independent fair signs.

## originality

FAIL

The full claim is already covered as a specialization of a distinct indexed finding on fixed-rank signed rooks, including both equality classifications, the transition at n=4, and real Banach–Mazur distance. Both records show the same publication day; this establishes exact coverage, not which proof or record came first.

## value

FAIL

The rank-four transition and exact Euclidean distortion are natural and useful invariants, but their entire classification, including the method and both endpoint deficits, is mechanically recoverable at k=n from the signed-rook theorem. No distinct useful remainder was identified in this frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
