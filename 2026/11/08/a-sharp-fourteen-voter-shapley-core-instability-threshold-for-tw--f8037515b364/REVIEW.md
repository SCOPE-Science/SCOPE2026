# Independent mathematical audit

## correctness

PASS

Derived exact coalition worth from q=floor(2(s+t)/n): 0 for q=0, max(s,t) for q=1, and only grand coalition q=2 with max(3a/2,a+b,3b/2). Marginal contributions in uniformly random player order give two exact binomial-weighted Shapley sums; efficiency follows. Independent Fraction implementation exhaustively tested every 49 unordered nonempty party-size profiles n=2..14 and all 1512 coalition types (s,t), reproducing exactly one negative slack: (a,b,s,t)=(6,8,6,1) with gap 83/858, phi_A=7127/9009 and phi_B=6947/6006. Code directly derives rather than trusting claimed logs; this exhaustive finite proof covers the entire finite threshold, not n>14.

## originality

PASS

Chen–Hatschka already show TU-core failure of PAV Shapley for unrestricted overlapping four-voter ballots, but this gives no lower bound on the first failure within disjoint homogeneous two-party lists. Party-list PAV=D’Hondt concerns committee allocation, not Shapley values of coalitions with floor entitlement; standard NTU committee core is a different notion. The exact restricted threshold 14 and unique split are not among the inspected prior propositions.

## value

PASS

The two-bloc disjoint restriction is a natural tractable robustness test for the TU-core failure phenomenon. A sharp first 14-voter witness, uniqueness of blocking composition and exact rational coalition gap are meaningful finite structural information, not an arbitrary truncation or re-expression of the known four-voter unrestricted example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
