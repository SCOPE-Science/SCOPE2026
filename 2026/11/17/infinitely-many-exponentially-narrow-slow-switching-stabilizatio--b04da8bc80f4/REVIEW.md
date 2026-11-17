# Scientific review of infinite late-dwell stability windows

## Correctness
PASS. The frozen-mode classifications use exact determinants. Exact matrix exponentials yield the trace and determinant, and the quadratic Jury criterion gives the if-and-only-if stability test. The growing oscillatory term has uniformly simple separated zeros; local monotonicity and scaled boundary analysis establish one and only one window per late zero. A geometric series proves the tail-measure constant. The attached `verify.py` checks independently evaluated matrix exponentials and finite boundary roots. Numerical checks are corroborative, not used to prove the count or asymptotic limit.

## Originality
PASS within inspected evidence. The closest source is Jeter et al., arXiv:2611.03355v1, whose exact finite-time Floquet criterion applies to the *same* focal model. That is a very strong antecedent and makes this result an asymptotic refinement, not a new stability criterion: its Section IV gives the trace inequalities and depicts a small number of windows, but it neither proves infinitely many connected components at fixed parameters nor derives their exponential width and exact total tail measure. Other switched-system works study different matrices (the transformed triangular pair in Porfiri et al. 2021, or mechanical Meissner matrices in Xiedeng et al. 2026). A published related mathematical record about directed Stuart–Landau triads establishes arbitrarily many reentrances by changing a reactive-coupling parameter, not this fixed-parameter infinitely many late windows. Broader Floquet or asymptotic-switching literature could imply a similar tail result; exhaustive historical priority is not guaranteed.

## Mathematical value
PASS. This resolves the long-time structure of a natural exact stability criterion, showing an unbounded sequence of exceptional *slow* stabilization schedules although both frozen modes and their average are unstable. The explicit decay exponent and prefactor quantify the precision required to realize each stability window and prove the total measure of viable switching times is finite despite infinitely many components. The difference between existence of arbitrarily slow schedules and poor robustness matters for interpreting numerical stability scans and schedule design.

## Limitations
The result treats only the exact planar linear on-off mode with equal phase duration and fixed parameters. It does not establish convergence of the full nonlinear Rössler network; the focal-plane approximation omits a transverse variable. No independent audit or universal historical-priority certificate has been performed.

Self-review: passed. Independent audit: not yet performed.
