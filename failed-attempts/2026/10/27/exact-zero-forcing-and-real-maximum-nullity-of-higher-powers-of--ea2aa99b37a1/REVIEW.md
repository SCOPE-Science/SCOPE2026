# Independent mathematical audit

## correctness

PASS

For each of the first m−1 arms the outermost r black vertices force inward: the forcer at t+r is not adjacent off its arm and sees only depth t white. The hub can then be forced from depth r, depths 1 through r−1 of the last arm follow from the depth-sum rule, the hub forces depth r, and propagation continues outward. In the witness the length-(r+1) windows cover exactly the same-arm pairs at separation at most r (including the case of just one window); the threshold block and hub vector give exactly the other edges. P has rank ℓ−r by its triangular minor. Independent choices of m−1 vectors in ker(Pᵀ), followed by their negative sum on the last arm, give (m−1)r independent null vectors: the window terms vanish armwise and all threshold and hub terms vanish by zero sum. For any exact-support matrix, restriction of the kernel to the initially black set is injective, because each forcing row propagates a zero. These bounds yield equality, and subtracting nullity from 1+mℓ gives the stated rank. Independent replay with python3 /workspace/spider_power_check.py used BFS graph powers, exact rational elimination and forcing closure on (m,ℓ,r)=(3,5,4),(4,7,5),(3,10,9); all size-seven initial sets were excluded for the first case. Uploaded scripts were read, not run.

## originality

FAIL

The exact uniform result and its Gram-block and arm-difference witness already appear in indexed record 8e9d1cb373f9. The independently indexed theorem 5580508bfee7 also covers the entire range, even allowing unequal arms. Proposition 9 and Conjecture 10 correctly locate the motivating question, but do not establish that the frozen proof fills an otherwise uncovered gap.

## value

FAIL

The uniform higher-power equality answers a worthwhile conjecture question, but the frozen narrower result adds no independent instance, invariant, or witness to the indexed proof. A restatement of the exact covered range with the same matrix certificate is not a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
