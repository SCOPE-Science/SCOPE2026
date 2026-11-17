# Independent mathematical audit

## correctness

PASS

The stable heavy-ball interval follows Jury criteria for z²−βz+β: −1/2<β<1; q∈(−1,1). For augmented state (x_k,x_(k−1),xi_(k−1)), solved stationary 3×3 Lyapunov covariance Σ=MΣMᵀ+σ²BBᵀ exactly, reproducing the rational variance ratio. Factored R−1 gives strict wrong-sign exclusion, while derivative at β=0, 2q(1−q), gives an improving opposite-sign candidate. Pole divergence guarantees interior minimizers. For q<0 the exact decomposition R=(1+2β)^(−2)+strict positive term proves R>1/9. Setting q=−1+t², β=1−ct expands R=1/9+t(4c/27+4/(9c))+O(t²); compactness from two positive terms forces all optimizing c→√3, coefficient 8√3/27. Independent symbolic Lyapunov solve and both factorizations/expansion verified using SymPy, after inspecting verify.py. The claim excludes q=±1 and unstable β boundaries.

## originality

PASS

The inspected primary work on epoch-correlated stochastic gradient noise explicitly limits heavy-ball momentum to β≥0 and uses a finite-epoch, non-AR(1) covariance model. It therefore does not imply the global negative-β sign theorem or the sharp 1/9 AR(1) optimization layer. Additional stochastic-heavy-ball papers use independent noise or different algorithms. Classical ARMA/H2-control colored-noise filters could implicitly contain the same scalar optimization; priority qualified accordingly.

## value

PASS

Temporally correlated gradients affect long-run optimization risk, and allowing negative momentum is a motivated often-excluded design choice. The complete global wrong-sign exclusion and ninefold extreme-antipersistence variance floor with optimal square-root approach give informative sharp benchmarking that local derivatives or variance computation alone would not provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
