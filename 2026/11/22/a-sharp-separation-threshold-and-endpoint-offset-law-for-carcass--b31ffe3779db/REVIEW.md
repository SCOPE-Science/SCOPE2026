# Independent mathematical audit

## correctness

PASS

With normalized stock r_i the recurrence is r_i=1−exp(−d_i)+(1−p)exp(−d_i)r_(i−1). The last visit strictly gains on postponement before H because 0≤r_(n−1)<1; a pass at zero can be moved to H with strictly positive gain, since positive stock survives and can escape finitely many trials. On the simplex the negative Hessian is a positive sum of outer products of interval indicator vectors; singleton vectors already make it positive definite. Thus strict concavity gives one optimizer, including boundary schedules. With U_i=1−r_i and Q_i the backward propagation factor for stock, adjacent equality of gradients pU_iQ_i gives U_i=p exp(−d_(i+1))Q_(i+1). Combining successive equalities and the forward recurrence gives U_1=…=U_(n−1) (not generally U_n). Writing A=1−(1−p)q, the candidate has U_1=…=U_(n−1)=pq/A, Q_i=1/A for i<n, and U_n=pq/A², so all gradients agree. At n=2 the direct condition is exp(−d_1)=p exp(−d_2), with feasibility exactly h≥−log p; it gives the same q parametrization. The horizon function strictly decreases from infinity to h_c at q=1/(2−p); there d_n=0 and all earlier gaps are positive. The candidate is optimal at equality because its equal-gradient condition still implies the concave supporting-plane bound. Below h_c an all-positive maximizer is impossible and d_1 cannot vanish. The invariant follows from the endpoint log ratio. Independently reproducing the n=4 example with a cohort sum gave 1.30167008997 versus 1.27510268262 for equal gaps. VERIFICATION.md and checker.py were read, not executed.

## originality

PASS

Repeated-discovery expectation modeling is established, and there is a material two-visit overlap with the closely related persistence-mixture result. The supported distinct claim is the arbitrary-n unique-calendar separation threshold and invariant, including identical interior gaps. The strongest inspected sources do not imply this multi-visit result.

## value

PASS

Identical repeat searches might suggest equal spacing. The unique endpoint offset and exact change from a collision to full separation show why that intuition fails in a natural discovery-count model, and distinguish a true scheduling constraint from numerical near ties. This benchmark is useful for model and search-design comparisons, not a recommendation about field coverage or estimator precision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
