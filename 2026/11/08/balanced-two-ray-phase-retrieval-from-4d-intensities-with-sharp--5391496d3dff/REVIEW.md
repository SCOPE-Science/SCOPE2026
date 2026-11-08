# Scientific review

## Correctness — PASS

For a degree-at-most-\(d\) polynomial, each radial squared magnitude is a real polynomial of degree at most \(2d\). The degree-\(2d\) and constant coefficients are independent of the ray. Ordinary degree-\(2d-1\) interpolation at each of the two groups leaves one shared leading-coefficient unknown; the unequal node-product hypothesis uniquely resolves it using the shared constant term. This is an exact algebraic identity, including deficient-degree polynomials and zero.

When two entire radial profiles agree, their polynomial quotient near the common ray origin has modulus one on both rays. Its first nonconstant local term has order at most \(d\); comparing its real parts at angles zero and \(\theta\) produces the prohibited resonance \(\sin(k\theta)=0\). An explicit \(1\pm iz^m\) pair proves necessity for resonant angles. The real span dimension \(4d\) follows by polarization of rank-one Hermitian matrices and independent control of intermediate coefficients using phase differences one or two. The last assertion is explicitly limited to *linear* recovery of full profile pairs.

The checker finished 5,355 numerical/exact arithmetic checks for degrees 1–6 and resonance orders through eight. The first naive double-precision run demonstrated severe interpolation cancellation at degree six, so the final checker uses 90-digit arithmetic; this conditioning is disclosed. Neither test proves the infinite statement, which is justified analytically.

## Originality — PASS (provisional priority)

Perez (2020) and Chalendar–Partington (2024) establish uniqueness from continuous intersecting lines at irrational angle; they do not state the finite balanced positive-radius measurement design, shared-leading-and-constant profile inversion, or bounded-degree rational angular threshold. Bodmann–Hammen (2013), Theorem 2.3, obtains the same overall \(4d\) measurement count for polynomials of degree at most \(d\), but on two *intersecting circles* with a different node distribution (and uses a conformal line argument). Pohl–Li–Boche (2017) give a two-concentric-circle design. The general existence of \(4d\) phaseless measurements is prior art and is not presented as a novelty. The new content is the exact balanced two-ray topology, any strictly positive unequal-product radial nodes, linear whole-profile reconstruction, and sharp degree-sensitive angle criterion.

Semantic searches for aliases of balanced radial samples, Vandermonde phaseless recovery, intersection-line resonance and two-circle reductions found no theorem implying this complete statement. Residual risk: an unlocated generalized polynomial sampling theorem may encompass it. Independent historical-priority examination remains outstanding.

## Mathematical value — PASS

Two rays with a fixed nonnegative radial sampling geometry are a natural deterministic optical or analytic sampling design. The result gives an easily checked algebraic criterion, a reproducible linear reconstruction of both intensity *functions* using exactly the real dimension of their linear span, and an exact boundary between possible and impossible two-ray phase retrieval at each polynomial degree. It improves on a bare existence statement by specifying a robustly describable entire family of sample positions and explaining why the radial product, rather than only distinctness, matters. No general nonlinear minimal-measurement or uniform noise-stability claim is made.

## Literature and residual risks

The exact finite-sampling formulas should be checked independently against broader phase-retrieval-frame constructions; in particular, the conformal reduction in Bodmann–Hammen is not dismissed by title alone. The two-circle geometry does not imply arbitrary balanced positive *ray* locations. Continuity-only results do not yield the stated finite interpolation identity. Near-equal products may make practical reconstruction unstable.

Self-review: passed. Independent audit: not yet performed.
