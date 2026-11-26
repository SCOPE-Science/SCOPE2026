# Independent mathematical audit

## correctness

PASS

Above the normalized sample maximum, the average of Y is 1 and the indicator average is 1, so G_n=C_n=(1−φ̂(u−1))/2 exactly. It is zero for ML and equals (v−u)/(2(v−1)) for MO. The real-analytic numerator on the positive normalized simplex is not identically zero: using coordinates 1±δ and the rest 1 gives v−u=−2δ⁴/[n(1−δ²)]. The fixed-sample conclusions follow by splitting at the maximum. For the joint limit normalize μ=1 and use s=bar(X)t. Subtracting the plateau leaves the four functions 1{x>s}, (x−s)_+, (x−s)_+/x and (x−s)_+/x², with squared unweighted norms x, x³/3, x/3 and 1/(3x). For the IG density f, −f'/f=(φ+3/x−φ/x²)/2; integration by parts against (x−s)_+ proves population cancellation of their specified linear combination. Each empirical mean is root-n tight in unweighted L² by its finite second moment; the fitted coefficients are root-n tight around their population values, so n∫(G_n−C_n)²=O_P(1) after changing variables. Thus multiplying by a_n or √a_n makes the weighted remainder negligible at any rate, with the mixed term controlled by Cauchy–Schwarz. Differentiating v−u as bar(X²)/bar(X)²−bar(X)·bar(X⁻¹) gives the stated influence function H. The density reciprocity f(1/x)/x²=x f(x) and integration by parts give M_j=M_{j−2}+(2j−3)M_{j−1}/φ and the displayed moments. Substitution in E[H²] gives 6/φ³; dividing by 4(v−1)² asymptotically gives 3/(2φ), and the Gaussian weight contributes its mass √π/2 after scaling. Checked both estimators and both weights against the original definitions. Inspected check.py and recorded 50-check report without running the uploaded script; its seeded simulation checks the plateau fluctuation, not triangular-array convergence.

## originality

PASS

The original estimator and statistic formulas directly imply the samplewise plateau and exact ML cancellation; these algebraic observations are not credited as independent novel theorems. The supported distinct contribution is the joint, unrestricted-rate null limit for the original four statistics, with exact constants, obtained by an unweighted remainder bound. The same-statistic preprint and journal version have fixed-weight Gaussian-element theory, not this diagonal limit in the inspected sections.

## value

PASS

The boundary of the positive tuning range matters for interpreting these established goodness-of-fit statistics. It exposes a qualitative estimator dependence that is not described by fixed-positive-weight theory: a root-n moment mismatch controls the scaled MO statistic over the whole vanishing-rate regime, while ML removes the effect exactly. The joint limit with explicit constants resolves a specific stability question about the original statistics, without inferring failure of a separately recalibrated test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
