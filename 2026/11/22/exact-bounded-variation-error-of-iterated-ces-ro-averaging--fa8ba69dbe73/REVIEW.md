# Independent mathematical audit

## correctness

PASS

Interior finite variation gives a bounded representative, up to a constant, by integrating the single-jump kernels against Df. Conditioning on the product of m independent uniforms gives the iterated Hardy operator; the negative logarithm has the integer-shape gamma law. For a jump at s, the signed defect is nonnegative, zero for x<=s, and integrates to exp(-r) times the sum of r^k/k! for 1<=k<=m, where r=log(1/s). Its derivative in r is exp(-r)(1-r^m/m!), giving a unique interior maximum. Integration against total variation bounds the defect of every real BV function. Equality requires total variation supported on the unique maximizing s and that atom suffices, regardless of sign. The single-jump response strictly increases with m at fixed s and tends to 1-s; evaluating at the maximizing jump and then considering arbitrarily small s proves the strict bounds and C_m->1. At r_m, the Poisson upper-tail terms beyond m, divided by exp(-r_m), tend geometrically to the stated sum because r_m/m->1/e and all ratios are eventually uniformly below 1. The next Stirling term fixes the power and prefactor. Replay: python3 /workspace/independent_checks.py 5 uses a gamma-kernel quadrature and numerical maximization for six orders and stable incomplete-gamma deficit calculations at m=80,240,640; deficit/leading-term ratios were approximately 0.9885,0.9947,0.9973. This is finite corroboration only. The frozen verification and checker were inspected, not executed.

## originality

PASS

Best of current knowledge: the supported contribution is the exact all-order sharp unweighted interior-BV to L1 identity-defect norm, all equality cases, and the exact asymptotic scale with prefactor. Step decomposition, gamma iterates and Poisson series are classical tools. The strongest inspected same-day exact analogues change the norm or the operator and do not supply this sharp constant. Not a claim of publication priority.

## value

PASS

The sharp BV-to-L1 defect is a natural endpoint quantity for prefix averaging; total variation supplies the normalization that is not provided by an L1-to-L1 Hardy norm. The formula determines for every order both the worst possible error and the unique scale and shape attaining it, and gives the exact rate and coefficient with which loss approaches the unit variation bound. This is a usable sharp benchmark for comparing discrete, weighted, or mixed averaging operators, without claiming any such generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
