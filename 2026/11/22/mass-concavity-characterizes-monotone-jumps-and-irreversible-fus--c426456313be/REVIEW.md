# Scientific review: mass-concavity and irreversible fusion

## Correctness — PASS
The stated equivalence is established with positive vertex fidelity masses and positive internal edge penalties, with the two exterior penalties fixed to zero. A finite signed-block decomposition yields affine solution pieces. For any active gap, its absolute-value derivative is bounded by the difference between the chord interpolant of the penalty profile and its value at the intervening mass coordinate; concavity makes that bound nonpositive. Necessity uses strictly increasing data to expose a locally expanding jump. A separate finite-parameter construction, with one initially negative gap and large positive neighboring gaps, proves actual positive-interval fusion and subsequent unfusion whenever concavity fails. The rational three-site example satisfies the KKT equations on all five pieces. The standalone finite checker passed 3,864 concave-profile comparisons and nine witness checks; no infinite statement rests on the numerical tests.

## Originality — PASS, with historical priority uncertainty
The 2004/2005 fused-lasso introduction provides the model but not this mass-aware edge-weight design theorem. The 2013 direct 1D TV algorithm treats equal edge/fidelity weights. Bento–Furmaniak–Ray (2018) describe possible unfusion, the worst-case number of fusion events and a sufficient dual-boundary criterion for possible events; their Section IV identifies conditions on weights and signals affecting path complexity as future research. That work does not state the necessary-and-sufficient arbitrary-mass concavity classification or universal monotonicity of each jump magnitude. The accessible summaries of a separate weighted-isotonic-regression result concern two-input projection stability, not the parameter-dependent path of TV regularization. Known primal-dual characterizations are used as methods, not misclaimed as new.

Residual risk: earlier or unindexed sources may contain the same universal classification; the 2004 founding paper was accessible through its abstract and bibliographic description but not verified in full. Priority is not independently certified.

## Value — PASS
A common algorithmic simplification is to merge fused sites permanently as regularization increases. Weighted penalties do not guarantee that behavior. The result gives a checkable, sharp, local and dimension-independent condition—concavity in cumulative fidelity mass—under which this simplification is valid for every datum, and identifies edgewise jump shrinkage as the stronger controlling invariant. When the condition fails it supplies a constructive, genuine unfusion interval, not just a numerical pathology. This is a natural complete weight-design classification, rather than a narrow unmotivated parameter slice.

## Scope and limits
Finite paths with strictly positive diagonal quadratic masses, strictly positive interior TV penalty weights, and a shared nonnegative regularization parameter only. No assertion for cycles, arbitrary graphs, nonquadratic fidelity, or two-input Lipschitz stability. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
