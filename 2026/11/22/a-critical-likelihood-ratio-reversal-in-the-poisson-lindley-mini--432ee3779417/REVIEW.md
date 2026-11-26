# Independent mathematical audit

## correctness

PASS

The PGF of the modified geometric sum is the stated geometric/shape-two negative-binomial mixture (polynomial rational identity independently checked). Its tail divided into the Poisson–Lindley tail gives E(k); the exact identity (1-U)D=t^2F was independently checked. The upward quadratic F has one positive root, above 1/(1+t), so gamma<1; the difference formula for E(k)-E(k+1) is positive for k>=1, with U=1 exactly at the endpoint. This both certifies the innovations and establishes stationarity by independent multiplication of tails. For each k>=1, the shorter geometric sum can equal k-1 while the added summand is positive with nonzero probability, so multiplication by E(k)>0 makes the conditional tail order strict. Expanding the two columns with p=r^(y+1) and consecutive factor rp gives Delta_y=-qp B_a(y) symbolically for arbitrary y. Independent rational reduction of N=U(1+Vq^2)-2qV to the displayed L^2 Q divided by the positive denominator confirms that the positive-coefficient certificate is exact, so B_a(0)<0, not just a sampled sign. At U=1, B_a=V-1-Vr^(y+2)<0. In the interior B_a is strictly increasing to infinity, proving uniqueness and the integer signs and refuting TP2 there. The root escapes all bounded intervals by continuity and the strictly negative boundary function, and r^(z_*+2) then vanishes since r is bounded away from one near fixed a_c(t). The zero equation and differentiation of (1-U)D=t^2F at that simple root give exactly the stated escape constant. The supplied verify.py was inspected but not run; to replay the exact checks, clear denominators in the PGF and certificate and expand the symbolic two-column minor with p and rp. No TP2 assertion for other boundary minors is made.

## originality

PASS

Provisional and limited to the explicit two-column reversal classification and its critical escape rate. The PL-MINAR model, its transitions and stationarity are prior, and the strict stochastic order follows from the established construction. The nontrivial new comparison is the sign of the likelihood-ratio minor uniformly across the admissible region, not another transition formula.

## value

PASS

The two lowest columns are a natural minimum witness for distinguishing stochastic monotonicity from TP2, rather than a randomly selected finite minor. Their complete sign classification over both parameters provides a counterexample for every interior pair; the reciprocal-distance escape law explains why checks confined to small counts can miss that failure near admissibility. The result does not claim a census of higher-column minors or empirical financial significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
