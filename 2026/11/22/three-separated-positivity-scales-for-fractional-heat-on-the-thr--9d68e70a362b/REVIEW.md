# Independent mathematical audit

## correctness

PASS

Character degree j has Laplacian eigenvalue 2j; summing the character signs at each distance gives the four exact rows. Diagonal and distance-one entries are positive, and ordinary product heat plus positive subordination yields strict positivity for 0<alpha<=1. Set a=2^alpha, b=4^alpha, c=6^alpha. The derivative of the distance-two numerator, multiplied by exp(ct), is a exp((c−a)t)+b exp((c−b)t)−c, strictly increasing and negative initially for alpha>1. This gives one positive crossing. For distance three an exponential sum with four distinct exponents has at most three real zeros with multiplicity (divide out one term and induct by Rolle). Its initial slope divided by a is 3−3*2^alpha+3^alpha; this three-term sum has its two roots at alpha=1 and 2 and is negative between, positive above. At alpha=2 the time-zero root is double with second derivative −576. For 1<alpha<=2, the negative initial sign and positive limit force one simple positive zero by the count and sign parity. For alpha>2 the initial sign is positive, but the entry is negative at (log 2)/b and tends to a positive limit, giving exactly two simple positive zeros. At (log 2)/b the distance-two numerator is also negative, using b/a>=4 and c/b>=9/4; at (log 2)/a it is positive while the distance-three numerator is negative. Thus the negative intervals overlap and entrywise nonnegativity returns exactly at the later distance-three zero, with the isolated t=0 case. At t=u/b and t=v/a the antipodal numerators tend to −2+3 exp(−u) and 1−3 exp(−v), yielding the two constants by brackets. For the middle zero u=bt_2 and p=b/a, evaluating between (1±epsilon)log p gives u~log p, then (1−exp(−u/p))exp(u)=1−exp(−(c/b−1)u) gives u exp(u)/p→1. The slope of u+log u is >=1, giving the stronger additive o(1) Lambert remainder.

## originality

PASS

The supported distinct claim is the exact Q3 superlinear sign regime and its three quantitative large-exponent scales, including the additive Lambert remainder and the exact later recovery root. There is substantial overlap at alpha=2, near alpha=1, and on another four-level graph; those pieces and the ordinary/noise or subordinated range are not fresh claims in isolation.

## value

PASS

The three-cube is the first cube with the distance-three entry needed for this question. Its antipodal positive–negative–positive pattern disappears when testing positivity of the full matrix because the distance-two obstruction overlaps the antipodal interval. Separating the three characteristic times, including a logarithmically enhanced middle scale, quantifies what an eventual-positivity criterion or a single antipodal test misses on this natural graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
