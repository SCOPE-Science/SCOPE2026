# Scientific review

## Correctness — PASS

The conditional covariance map is computed directly and has exact \(\det(I-T)=h(2-h-ph^2)\). The map is positive on \(2\times2\) covariance matrices; its nonnegative Perron root starts below one for positive small steps and can cross the unit circle only at the unique positive zero of that determinant. The initial-pair quantifier is justified by rank-one spanning. For the witness, the strong-law weighted-operator-norm bound is negative while the exact moment generating function has a unique positive dominant pole and nonzero positive residue. The separately packaged exact symbolic and rational checks passed. This does not rely on finite enumeration to certify a continuous theorem.

## Originality — PASS, with precedence risk

Arjevani–Shamir–Srebro (2018) fix the gradient delay; Mulayoff–Michaeli (2024) randomize minibatch gradient selections without staleness. Lale and colleagues (2021) provide the general positive-map moment-stability framework, which is credited as prior theory; their analytic formulae cover no-delay random updates and their genuinely delayed random case is analyzed numerically. The exact Bernoulli stale-gradient stability curve and the explicit almost-sure/mean-square split were not found in those statements or the compared public records. General stochastic recurrence or Markov-switching results could give an equivalent formulation and remain a source of precedence uncertainty.

## Value — PASS

For a natural asynchronous scalar quadratic solver, the result supplies a sharp entire probability/stepsize frontier and proves why pathwise convergence alone can badly misrepresent expected numerical error. The witness is elementary enough to be a reusable numerical stress test but its failure is exponential, not a negligible numerical artifact. The argument is restricted to constant-step iid one-step delays on scalar quadratics; no general speedup or multivariate stability claim is made.

## Reproducibility and limitations

The standalone `verify.py` checks all critical exact algebraic expressions and reproduces finite histories. Independent mathematical validation is pending. Other random-delay distributions, history-dependent delays, and nonlinear targets are not covered. An earlier equivalent random-coefficient recurrence result has not been excluded exhaustively.

Self-review: passed. Independent audit: not yet performed.
