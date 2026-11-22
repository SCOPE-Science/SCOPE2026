# Self-review

## Correctness

PASS. The normal oscillator gives the exact \(\mathcal R=\prod_iq(h_i)^{-1}\) identity. A strict quadratic convexity identity in the pair product eliminates every schedule with unequal positive lengths, without treating a finite grid as exhaustive. The curvature of \(\log q\) proves uniform optimality at \(b\leq a\), and the unique maximum of \(\log q(t)/t\) together with a single-crossing derivative gives all thresholds and equality cases when \(b>a\). The symbolic checker independently simplifies the three critical algebraic identities and compares many nonuniform schedules. Numerical checks alone do not certify the quantified proof.

## Originality

PASS under the inspected evidence, with historical-priority risk. Gander–Halpern–Ryan–Tran prove the real-decay uniform-partition case, which is strictly covered by the present theorem, but not the oscillatory sparse-support case. Song–Zhang–Eisenträger–Ankit analyze different high-order Padé damping and time-step guidance; Sun–Shu analyze superviscosity stabilization of explicit RK. Closest indexed fixed-budget BDF2 and prior implicit-midpoint statements optimize different stability functions. The older and broader literature has not been exhaustively searched; one relevant variable-step refactorization preprint was available only as an abstract during review, so absence of coverage is not inferred from its full text.

## Value

PASS. The theorem gives a complete all-step-count solution to a natural fixed-horizon damping-allocation question, identifies a dimensionless oscillatory threshold, proves that every optimal schedule is sparse and equal on its support, and locates all adjacent active-count transitions by unique scalar roots. The exact example exhibits approximately 19.64% smaller numerical squared amplification than using all four equal steps. It does not address endpoint solution accuracy or claim speedups.

## Scope and limitations

All step lengths are allowed to be nonnegative; strict positivity can destroy attainment. Results concern normal planar damped rotations, one fixed damping objective and arbitrary finite maximum solve count. They do not extend automatically to nonnormal dynamics or multiple eigenfrequencies. Historical equivalence remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
