# Independent mathematical audit

## correctness

PASS

Conditional on k observed negative leaves, the OR of the remaining m=n-k has positive probability u_m=1-(1-p)^m and posterior p/u_m per remaining source when positive. A positive-side decision flip improves correctness by [2p-u_m]_+, so the stated general root gain follows by multiplying by the probability (1-p)^k and by m/n. For k=0, u_n/p decreases strictly from n to 2-2^(1-n) as p rises to one half, giving the unique crossing of 2 for n>=3. With q=1-p and n=3, three times the marginal accuracies are D=(3p[-1+3p-p^2]_+,2p^2q,pq^2,0). Leaf pairs without the root have concave coverage and affine accuracy. With the root, coverage is constant; the two accuracy curvatures are (D2-2D1+D0)/3 and (D3-2D2+D1)/3. The first numerator is pq(1-5p) below the posterior crossing at (3-sqrt(5))/2 and p(p+2)(2p-1) above it; the second is 2pq(2p-1). Thus exactly p<1/5 is irreparable. For p>=1/5, the remaining pair conditions give the maximum of zero and (D_(k+1)-D_k)/(3pq^k) for k=0,1,2; the last bound is -1/3. Comparing the other two bounds gives all four stated pieces and the matching endpoint values; the cutoff is always less than one. Two leaves yield D=(2p^2,pq,0), strictly negative root-present leaf curvature, and only the possible positive bound (1-3p)/2. One leaf yields duplicate readings and no obstruction.

## originality

PASS

The underlying Boolean observation model and related placement scores are known; general localization objectives can also lack submodularity. The distinct contribution is the exact prevalence obstruction, sharp weight and minimum size in this precisely specified iid OR model, not the general phenomenon.

## value

PASS

A three-element sensing mechanism yields the smallest example where coverage cannot correct complementarity in the classification objective. The sharp prevalence and coverage-weight boundary distinguishes failure that no tuning can fix from failure that weight tuning can fix; it specifies when a generic submodularity argument is mathematically available for this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
