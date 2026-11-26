# Independent mathematical audit

## correctness

PASS

With two regions, the exchange semigroup gives the affine segment x=(m+delta*z,m-delta*z), z=exp(-2*kappa*T). The denominators are positive even for initially dry regions. The uptake sum in z has strictly negative second derivative when delta is nonzero and is constant otherwise. Thus it has at most one interior maximum; the monotone change of variable preserves its type. One region is constant. On the three-region path the eigenvectors (1,1,1), (1,0,-1), and (1,-2,1) give the stated normalized solution with modes 1,q,q^3 and nonnegative water fractions. For the stated positive capacities and half-saturations, independent exact differentiation recovers 108P over the product of the three squared nonvanishing denominators. Independent exact arithmetic reproduces gcd(P,P')=1, Sturm variations 9 and 6 at the nonroot endpoints, and signs +,-,+,- at 1/10,7/10,9/10,19/20. These bracket all three roots; the sign switches are max/min/max, and the smooth bijection q=exp(-kappa*T) reverses order without changing their types. The rates in increasing kappa*T are about 0.0661994572, 0.1881674312 and 0.7494616363. Replay: /workspace/branches/2c7df399-3f8f-41b6-9348-3b1831c18c0b/independent_exact_check.py. The uploaded checker was inspected, not executed. The count applies to finite positive rates for fixed T>0, not endpoint optima or realized daytime transpiration.

## originality

PASS

The standard diffusion modes, concavity and Sturm method are not original. The distinct supported result is the sharp two-region obstruction and three-region example with exactly two interior maxima of saturating dawn uptake in the specified lossless transient model. Related path models inspected do not establish that result. This is a bounded best-of-knowledge comparison, not a priority determination.

## value

PASS

The instantaneous saturation observable and varying exchange rate have a natural interpretation independently of the numerical example. The result separates one-mode averaging, which makes this response concave in the modal amplitude, from a minimal two-mode system with two strict competing optima despite conservative symmetric exchange and positive response parameters. An exact global count on positive rates is stronger than finding two apparent numerical peaks. No field efficacy or plant-specific calibration is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
