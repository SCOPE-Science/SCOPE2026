# Independent mathematical audit

## correctness

PASS

For any chosen active second-difference rows S, all H_S are linearly independent and the KKT construction chooses z with H_S z=R, other curvature entries zero, and input u=z+H_S^T lambda (lambda>0). Strict complementarity ensures local derivative Q_S=I-H_S^T(H_SH_S^T)^(-1)H_S. Taking four inactive rows at indices 1,4,n-5,n-2 yields six affine truncated-power basis functions; the midpoint step has BV seminorm one. A separately implemented SymPy orthogonal projection at n=30 produces exactly increments [11/196,(-33/392)x3,(13/196)x21,(-33/392)x3,11/196], sum of absolute values 197/98>2. It independently verifies the actual finite input pair u and v=u+0.001h: active KKT multipliers stay strictly positive; all four inactive output curvatures stay strictly inside R=1; active curvatures equal one. Scaling yields every positive R. For n→∞ the central affine L2 fit to a half-interval step is -1/4+(3/2)s, giving central variation 3/2; boundary layer least squares gives each edge variation 11/28, total 16/7. The same coercive Riemann-sum and fixed-width boundary argument applies to odd lengths. This proves a lower limit only, not an exact limit or global upper bound; finite tests support rather than replace the asymptotic reasoning.

## originality

PASS

The closest published second-difference trend-filtering result gives an all-active-set formula and small BV constants for an L1-PENALIZED denoiser, not the two-sided hard-curvature-cap projection. It implies a general shared local projector mechanism, and thus is genuinely close, but does not evaluate the concrete four-knot hard-cap finite witness or prove its 16/7 boundary-layer lower envelope. Earlier Kim et al. and Tibshirani/Taylor establish trend-filter and generalized-lasso active-set methods, which are credited, without this hard-cap two-input BV instability result. Related TV-ball projection uses first differences and a sharp factor two on a different feasible set. Historical possibility that a broader unstated active-face computation yields the same formula remains explicit.

## value

PASS

An explicit finite pair with strict gain >2 invalidates a plausible uniform twofold stability bound for physically motivated curvature-capped least-squares smoothing. The all-size four-knot boundary layer forces a nontrivial asymptotic 16/7 lower envelope, a structurally motivated mechanism rather than an arbitrary dimension slice. The claim carefully avoids asserting optimality or full n-classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
