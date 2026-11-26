# Independent mathematical audit

## correctness

PASS

There is at most one zero-product cell, and (0,0) always extends a nonzero-product matching. With t nonzero cells the two positive coordinate lists have combined sum at least t(t+1); the sum of the t distinct product exponents is at most tn−t(t+1)/2. For t>0 this gives 3(t+1)≤2n, and the stated floor bound is also valid when t=0. The odd rotation on 2k+1 entries gives the two offset parity progressions whose union is [k+2,3k+2]. For even t=2k multiplication by k modulo 2k+1 is invertible; substituting odd and even rows gives the two disjoint intervals [k+1,2k] and [2k+2,3k+1]. Their largest exponents are at most n−1 by the same bound on t. Thus the construction has all distinct rows, columns and products; n=2 is handled by (0,0) alone. This is a proof for all n, not an inference from the finite checker.

## originality

FAIL

The exact nonzero-cell problem is the published 2009 IMO shortlist problem C2 by a bijection, not just a similar two-thirds estimate. Put m=n−3. Map a nonzero cell (a^i,a^j) to (i−1,j−1,n−1−i−j). These are nonnegative triples summing to m; conversely all such triples come from one nonzero cell. Coordinatewise distinctness of triples is precisely distinct row, column and product. Official C2 states and proves the exact optimum floor(2m/3)+1 for m≥2 by the same sum obstruction and explicit constructions. For m=0,1 the optimum is trivially one, and n=2 has no nonzero entries. Appending (0,0) to any nonzero optimum gives τ(N_n)=floor(2(n−3)/3)+2=floor(2n/3) for n≥3. OEIS A004396 independently records the same triangular-grid independence optimum after shifting side size to n−2. A different permutation for the even construction does not make the already-determined exact invariant new.

## value

FAIL

Maximum partial transversals are a natural invariant, and the proof is sound. For this family the frozen contribution is an elementary re-expression of a solved extremal problem plus the freely addable zero cell. No new structural fact about semigroups, classification of attaining patterns, or useful stronger property of the different even witness is established. The exact coefficient is therefore not a distinct research contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
