# Independent mathematical audit

## correctness

PASS

For a light pulse beginning at (x₀,y₀), integration of x(1−y) gives (1−y₀)(C−D+Dx₀). Inserting the initially zero state and then (Xe^(−bg),Ye^(−dg)) yields the stated three-exponential gap objective. C>D>0 and X,Y>0, so P,Q,R>0. The derivative divided by e^(−bg) is −bP+dQe^(−(d−b)g)+(b+d)Re^(−dg), with strictly negative derivative for d>b and limit −bP. This proves uniqueness at zero even at Δ=0, or strict increase then decrease around the only positive root. A cap truncates that root, including the one-point case G=0. At the stated dimensionless rates, substitution gives Δ=(1−u)²(4−3u−3u²)/2; u decreases from 1 to 0 and the only relevant zero is (√57−3)/6. The normalized root equation has strictly positive z-derivative and its right side strictly increases with ℓ at fixed z>0, so the branch has decreasing z and increasing g. At threshold z=1 and the implicit derivative is the stated strictly positive value; at u=0 the positive root is 1/3. Independent evaluation of the quadratic at ℓ=1 gave g≈0.649546036 and gains ≈0.373822536 and 0.483248394. VERIFICATION.md and check_sunfleck.py were read, not executed. This is a fixed-light-time, shade-neutral objective, not an optimization of gain per unit elapsed time.

## originality

PASS

Fluctuating-light induction and photosynthetic inhibition are known, as are first-order response models. The supported distinct result is the exact gap optimum with a sharp sign criterion for these two coupled contributions to assimilation, plus its specified duration bifurcation. The closest indexed optimization statements and the accessible historical evidence do not establish the result as a corollary; some historical full-text comparisons remain unresolved.

## value

PASS

Shade can simultaneously dissipate the beneficial induction memory and remove harmful photodamage. An exact solution showing when these opposing effects favor no recovery time versus a unique interior optimum is a useful benchmark for more detailed models; it is stronger than a sign-of-initial-slope calculation without global control. The illustrative rate slice locates the onset and branch shape but is not offered as physiological calibration, and its numerical gain is not the basis of the value judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
