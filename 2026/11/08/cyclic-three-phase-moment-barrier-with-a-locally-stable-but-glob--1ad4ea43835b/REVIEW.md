# Self-review

## Correctness — PASS
The absorption-time moment generating function is obtained from geometric feedback through three independent exponential holding phases. Coefficient extraction gives the four-moment ratio. The factorization \(10AC-9B^2=P_0+qP_1+q^2P_2+q^3P_3+q^4\), together with Schur's three-variable inequality, yields the strict \(6/5\) floor and its only equality case. The equal-rate perturbation has a strictly positive quadratic coefficient for every return probability below one. An exact rational comparison of the equal design with the vanishing-third-time profile gives a unique crossing and a strictly positive finite-rate competitor beyond it. The bundled SymPy checker reproduces essential algebraic identities and the rational finite witness.

## Originality — PASS (qualified)
Weng, Yu, and Zhu's 2026 phase-type Runge--Kutta treatment gives the numerical-analysis motivation, proves related bounds for acyclic representations, and identifies general cyclic higher-order questions as open. The 2019 He--Horváth--Horváth--Telek study supplies eigenvalue-controlled moment bounds rather than this cross-moment quotient and heterogeneous rate-design separation. The 1987 Aldous--Shepp result concerns least variance (second moment). A prior equal-stage feedback calculation determines only the symmetric benchmark, not the fact that equal rates can be locally minimizing and globally dominated. Searches did not identify direct coverage of the joint statement. Residual risk: historical extremal phase-type moment inequalities or symmetric-function inequalities may imply parts of the floor; priority is not independently established.

## Mathematical value — PASS
This establishes a sharp three-phase Erlang moment floor for an explicit cyclic feedback class motivated by positivity-preserving integration and exposes an analytically exact local-versus-global failure in rate selection, with finite rational parameters. The result discriminates one-sided local optimization guarantees from global designs without claiming a global phase diagram; it does not itself yield improved SSP coefficients.

## Scope and verification limits
The polynomial crossover applies only to the two specified comparator profiles. The zero-stage-time comparator is limiting only; strictly positive near-boundary designs and a rational finite witness are established. The computer program tests algebraic identities and rational samples but the infinite-dimensional quantifiers over parameters rest on the written proof. Independent external validation was not performed.

Self-review: passed. Independent audit: not yet performed.
