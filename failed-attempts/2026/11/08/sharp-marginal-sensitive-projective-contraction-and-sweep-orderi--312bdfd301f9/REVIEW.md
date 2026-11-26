# Independent mathematical audit

## correctness

PASS

In dimension two, componentwise inversion agrees projectively with the swap J, since (1/x,1/y)=(y,x)/(xy). Write D_r=diag(r,1−r), D_s=diag(s,1−s). The exact full sweep is projectively the action of T=D_s J KᵀD_r J K. Apart from its left diagonal multiplier, T has entries α=rbc+(1−r)ad, β=bd, γ=ac, δ=rad+(1−r)bc. In x=v_1/v_2, the map is a positive constant times (αx+β)/(γx+δ). Its log-coordinate derivative is (αδ−βγ)/[αγx+αδ+βγ+βδ/x], with nonnegative numerator r(1−r)(ad−bc)². Minimizing the denominator by AM–GM gives (√(αδ)+√(βγ))² at x=√(βδ/(αγ)); derivative sharpness is global by the mean-value theorem and arbitrarily close inputs at the peak. Since αδ/(βγ)=1+r(1−r)(R−1)²/R, this is the claimed q. For R=1 the map is constant; otherwise q<1 and Banach's theorem on the whole real log-ratio line gives the stated convergence bound. The factor increases strictly with r(1−r) for R≠1 and at r=1/2 reduces to the stated classical kernel-only bound. Transposition and exchange of the marginals give the reverse-order comparison, not a trajectory-wise or local rate claim. The example rounds to the displayed values. The package numerical check was inspected but not run; it does not certify the all-input claim.

## originality

FAIL

The exact factor is the already-established Birkhoff–Hopf coefficient of the positive matrix representing one binary sweep, not merely the product bound applied to two individual half-steps. In two dimensions the entire reduction is the identity (1/x,1/y)∼(y,x); evaluating the classical coefficient gives the marginal factor and, by transposition and monotonicity, every stated comparison. This is a mechanical prior implication, not proof of historical precedence from an identical indexed formula.

## value

FAIL

Sharper orientation-specific certificates are useful in principle, especially for imbalanced margins. Here the claimed exact coefficient and ordering are direct textbook deductions from the positive-matrix representation of a binary sweep and the exact Birkhoff theorem. The frozen result adds no independently new sharp invariant or distinct improvement beyond evaluating that known coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
