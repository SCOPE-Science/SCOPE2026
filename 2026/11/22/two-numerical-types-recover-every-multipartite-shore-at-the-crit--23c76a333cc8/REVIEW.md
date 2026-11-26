# Independent mathematical audit

## correctness

PASS

Universality realizes each induced K_m-free finite extension of the named graph (move its embedded base onto the named one by homogeneity). Any two ordered extensions with the same labelled diagram are conjugate by homogeneity over the named base, and any unequal diagrams differ by an atomic formula. Because the base has clique number ℓ≤m−2, every one-point diagram and every nonadjacent pair diagram is legal, giving 2^n and 4^n respectively. For an adjacent pair only a clique using both new vertices can be forbidden; it needs a common named clique of size m−2. For ℓ=m−2 this means a common neighbor in every shore. The four labels per named vertex have three options other than ‘both’, so the lost adjacent diagrams are precisely the product of 4^a−3^a over the shores. Below this rank none are lost. For the inverse, after comparing products and cancelling shared factors, take the largest unmatched size d≥2. Bang–Zsigmondy applies at d≥2 to (4,3): 4+3 is not a power of two and the sixth-exponent exception is (2,1), not (4,3). The primitive prime at d cannot divide any smaller factor, a contradiction. The total named size then detects the 1-parts (also determined by k after reconstruction of the non-singletons). Even t_2 alone distinguishes critical bases: 4^n<t_2<2·4^n gives disjoint n-ranges, and then the same inverse applies. At n=k,k+1 the partition is unique; at n≥k+2, (n−k+1,1^(k−1)) and (n−k,2,1^(k−2)) are distinct at fixed n, and at the first collision 7²−37=12. The claim of subcritical information loss means no information beyond n, not failure in instances already unique from n and a supplied rank. Section 3 of python /workspace/review_reproduction.py independently enumerates small finite clique-free diagrams, including totals 2011 and 1999 at the first collision; it is not a bound or a proof of number-theoretic rigidity. The package's stored 64-case and partition-census outputs are historical checks, not required for the theorem.

## originality

PASS

The unary formula and legality criterion are covered, and the factors 4^d−3^d have appeared in a closely related maximal-rank pair census. The distinct claim is all-shore recovery from the two numerical low-arity counts at rank m−2 for m≥5. The strongest inspected inverse results use two shores or a different rank and richer counting data. The classical primitive-divisor theorem is an input, not a novelty claim.

## value

PASS

There is a natural information-loss question: can mere totals of logical types over named vertices determine the unnamed multipartite structure? At exactly the first allowed clique rank where pairs see a forbidden configuration, one scalar correction is rigid enough to recover arbitrarily many shore sizes. The all-size inverse, rank boundary and sharp first unary collision answer that question, beyond producing another list of counts. No efficient inverse algorithm, arbitrary-base result or general higher-arity classification follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
