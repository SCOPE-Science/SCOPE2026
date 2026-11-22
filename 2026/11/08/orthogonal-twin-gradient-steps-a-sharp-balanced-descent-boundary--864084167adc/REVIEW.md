# Independent mathematical audit

## correctness

PASS

Independently reconstructed the full planar SPD quadratic proof. In the orthonormal basis of the two nonzero orthogonal positive gradients let B=A^{-1}=[[a,c],[c,d]], Ax=Ue1, Az=Ve2 (a,d,U,V>0; ad>c^2). The constrained two-ray minimizer equals alpha=aU-cV and beta=dV-cU if both positive, and the rays then intersect uniquely. Balanced energies aU^2=dV^2 imply alpha=aU(1+r), beta=dV(1+r)>0, where r=-c/sqrt(ad) in (-1,1). Direct quadratic expansion gives identical energy ratios R=1-2 eta(1+r)+eta^2(1+r)/(1-r), hence R-1=eta(1+r)(eta/(1-r)-2). For eigenvalue condition kappa(A)=kappa(B), determinant/trace and (a+d)^2>=4ad give |r|<=(kappa-1)/(kappa+1), sharp at a=d, c<0. Therefore R<=1 for every balanced admissible pair of condition <=kappa iff kappa<=4/eta-1, including equality and kappa=1. Beyond the boundary the equal-diagonal construction strictly increases both energies. For any fixed kappa>1, r=(kappa-1)/(kappa+1), B=[[1,-r],[-r,1]], Ax=e1, Az=M e2 yield alpha=1+rM, beta=M+r>0, exact meeting, separation factor 1-eta and energy factor 1-2eta(1+rM)+eta^2(1+rM)^2/(1-r^2), diverging as M^2 with positive coefficient. At kappa=1 all orthogonal meeting updates shrink both objectives by (1-eta)^2. Independent SymPy identities plus 372 exact rational evaluations (252 balanced, 72 unbalanced, 27 isotropic, 21 sharp spectral) passed without executing source VERIFY.py. These checks corroborate the universal analytic proof, not substitute for it. All seven actual Git blob identities reconstructed the frozen assigned tree.

## originality

PASS

Best-of-knowledge originality survives as the sharp orthogonal equal-energy condition-number/damping frontier and an unbounded-ascent construction constrained to EXACTLY orthogonal descent directions. The original Twin-gradient preprint contains the exact least-distance step, equal-energy positivity (Section 4), possible objective spikes and damped safeguards, but the inspected mathematical sections do not state a two-endpoint objective-ratio frontier or the fixed-angle unbounded one-sided amplification. A closely related separately published November 8 result proves unbounded amplification at every kappa>1 and fixed damping for NEAR-PARALLEL gradients; its existential near-parallel family does not imply an orthogonal family, and its sharp c* threshold concerns eta scaling with an angular gap rather than balanced energies. Conversely it limits broad claims that the general fixed-damping obstruction is entirely new. A pre-existing objective-minimizing 2D acceleration method selects a different subspace line search. A bounded search is not proof of historical uniqueness; a classical inverse-SPD correlation bound underlies one ingredient and is credited as standard.

## value

PASS

This is a motivated sharp reliability boundary for a recently proposed nonstandard paired optimization step. It answers a specific mathematically natural question a method designer needs: when do exact orthogonal normalized-gradient, equal-energy twin endpoints BOTH guarantee objective nonincrease uniformly over every SPD quadratic of condition at most kappa? The answer kappa<=4/eta-1 is exact with equality extremizers and a strict example beyond. It further shows that removing energy balance allows arbitrarily large one-sided objective amplification at any fixed mild anisotropy even while the twin distance contracts, with the angle held exactly 90 degrees. These facts isolate genuine objective-versus-distance mismatch, distinguish balanced and unbalanced regimes, and motivate independent objective safeguards. It is a narrow one-step planar fact and not a theorem about full algorithm convergence, but a sharp analytic classification with a nontrivial unbounded counterfamily rather than an unmotivated numerical test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
