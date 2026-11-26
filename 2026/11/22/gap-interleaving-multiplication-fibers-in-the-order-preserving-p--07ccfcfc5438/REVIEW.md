# Independent mathematical audit

## correctness

PASS

Each factor is uniquely specified by its ordered domain and image. For the prescribed composite, I=im(f)∩dom(g) is in order-preserving correspondence with both A and D. Extra source/image entries of f and extra domain/output entries of g must have matching counts in their respective gaps. Extra intermediate entries for the two factors must be disjoint; disjointness also suffices, because the only points surviving both maps are then the t points matched through I. The four binomial factors count the choices without duplication. As an independent check, choose instead the full intermediate union of size r+s−t, and mark its sorted elements as survivor, f-only or g-only. With u_j and v_j extras in gap j, there are binom(u_j+v_j,u_j) local words; the survivor separators then determine I. This independently yields binom(n,r+s−t) times the coefficient of the product of gap polynomials with coefficients binom(a_j,u_j) binom(d_j,v_j) binom(u_j+v_j,u_j). It confirms both the empty target and the two impossible-rank bounds. With two rank-(n−1) factors, equal intermediate holes give rank n−1 and n choices; different holes give rank n−2 and four ordered choices of one outer hole on each side. Each pair of choices fixes two insertion slots, u or v−1 on the source side and a or b−1 on the target side; equal slots permit both intermediate orders, otherwise just one. The multiset dot product is therefore 0,1,2,4. Ordered pairs contributing 1 use three distinct indices with one common index, giving N(N−1)(N−2); contributing 2 are identical simple multisets or repeated/simple pairs sharing an index, giving 5N(N−1)/2; contributing 4 are N matched repeated multisets. Subtract from binom(n,2)^2 for class 4. This accounts for the n=2 and n=3 degeneracies and rules out 7. Independent direct compositions for n=1 through 5 agree with the union formula on every target and pair of ranks, including zeros (63,504 products and 9,072 target/rank checks at n=5; replay python3 /workspace/reproductions/2.py, output 2.txt). The universal proof is the bijection, not extrapolation.

## originality

PASS

The supported contribution is the target-specific two-factor structure constants for increasing partial injections and the full corank-one fiber spectrum and multiplicities. The rank criterion and the aggregate law are elementary/antecedent; they are not the basis for this pass. Same-object historical full-text gaps are retained as risks, not negative evidence.

## value

PASS

These counts refine rank-aggregate convolution by distinguishing actual maps in a natural finite inverse monoid. The order-sensitive gap invariant handles every target and rank pair, while the natural first nontrivial rank drop exhibits a complete spectrum and target census rather than a few small examples. This gives usable product statistics that knowing only rank or ideal structure cannot provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
