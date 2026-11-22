# Self-review

## Correctness (PASS)
The proof differentiates the stabilizing continuous-time algebraic Riccati solution at a strictly Hurwitz diagonal generator. The Sylvester differential is invertible, the mixed trace derivative is explicitly computed, the kernel's two-by-two determinant factors exactly, and a negative direction is realized by two actual input columns. Analyticity controls the remainder on the positive-strength quadrant, making the weak-actuation counterexample rigorous. The checker independently evaluates derivative recurrences and closed-form identities with 2,043 exact rational assertions. This is not independent verification or a replacement for the analytical proof.

## Originality (PASS, qualified)
The closest inspected sources study topological derivatives of actuator support (Azmi--Wachsmuth, arXiv:2611.12553v1, full publicly accessible manuscript, including §§3.3--3.4 and §4) and Riccati-based reduced-order actuator placement (Watanabe et al., Actuators 15 (2026), 234, full HTML). Searches for LQR Riccati submodularity, mixed Hessians, weak actuator gains, and exact two-mode interactions did not yield this sharp all-direction equivalence. General Riccati sensitivity formulae are acknowledged as possible broader antecedents; unindexed prior results and unindexed general Riccati sensitivity theory are residual risks. Novelty here attaches to the combined sharp modal classification and constructive counterexample, not to the existence or differentiability of Riccati solutions.

## Value (PASS)
Greedy actuator addition is naturally evaluated by diminishing returns of optimal LQR savings. The theorem identifies exactly when the leading local interaction respects that sign for *all* possible actuator directions, and shows that two different decay rates already destroy it in a minimal two-state plant. This is a motivated sharp structural boundary, not an arbitrary single numerical counterexample. Its precise scope is weak actuator strength; no approximation guarantees for greedy algorithms are asserted.

## Closest literature and limitations
The motivating support-optimization manuscript and the full actuator-selection study use related Riccati objectives but do not present the compared exact kernel in the relevant material inspected. Broader perturbation theorems could contain the result implicitly. The exact proof covers arbitrary dimension with strictly positive diagonal damping, \(Q=I\), \(R=I\), and isotropic averaging. Numerical experiments serve only as checks. Independent priority and proof review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
