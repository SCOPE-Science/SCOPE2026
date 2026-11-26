# Independent mathematical audit

## correctness

PASS

With row probabilities on states 1 and 2, common additive suppression gives Q_s=Q_0−sI+sN, where the only nonzero entry of N is N₂₁=1. The discriminant (λ+m−d)²+4λ(d+s) is strictly positive on the entire stated domain, including ℓ=0, so the divided-difference coefficient b_s(t) of Q_s in exp(tQ_s) is positive for t>0. The exponential swap is b_h(u)b_ℓ(v) times (h−ℓ)[N,Q_0]; the latter commutator applied to the column of ones is (−λ,d−m)ᵀ. Subtracting survival from one gives the stated positive factor times αλ+(1−α)(m−d). For d>m there is one interior tie and the sign changes across it; for d=m only α=0 ties; for d<m both endpoints of the affine expression are strictly positive. The proof's last nonpositive-term remark at RESULT.md line 66 applies to the survival bracket in line 60, not the negated extinction bracket; the formulas and Finding have the correct signs. One transient state gives a scalar cumulative-hazard factor, independent of order. Independently evaluating both exponential products by 70-term matrix Taylor series at λ=m=1,d=2,h=3,ℓ=0,u=v=1 gave extinction differences +0.007741914776 and −0.007741914776, and −0.00309676591033 at α=0.3. The frozen verifier was inspected, not executed; its recorded 7,208 checks are not the universal proof.

## originality

PASS

The supported distinction is the same-exposure, all-positive-duration extinction ranking and exact initial-mixture threshold for the common-additive, two-active-state birth–death chain. Neither the additive-hazard model nor the matrix-exponential technique is claimed as new. The examined sources do not cover the stated comparison; this does not establish historical priority.

## value

PASS

Equal total exposure does not determine finite-deadline extinction, and even the preferred direction of front-loading can reverse with the initial population. The exact demarcation, uniform in episode lengths, and the minimal-capacity example identify when order-independent intuition first breaks. This is a structural conclusion for a deliberately small model, not advice to delay actual fire suppression or a result about burn footprint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
