# Independent mathematical audit

## correctness

PASS

Angular orthogonality in the normalized harmonic basis gives S=T_z as a bilateral shift whose weights at positive and negative indices are square roots of consecutive radial-moment ratios. The ratios are bounded below by m1>0 and increase to 1: log-convexity gives the increase, and m_j^(1/j) tends to the support endpoint 1. Thus S is invertible and a compact perturbation of the bilateral unitary shift. For lambda off the circle, S-lambda has index zero, and the weight recurrence rules out a square-summable eigenvector (growth at +infinity for 0<|lambda|<1, at -infinity for |lambda|>1). Hence its spectrum and essential spectrum are the circle. Direct projection shows the only defect of T_(z^2)-S^2 is from e_-1 to e_1, with coefficient delta=m2/m1-m1. In the resolvent of S, the only power connecting e_1 back to e_-1 is S^(-2), with entry 1/m1; the geometric series converge in norm by spectral radius on each region. Thus the connecting resolvent entry is s/m1 for |s|<1 and 0 for |s|>1. Its divided difference at the roots of z^2+tz-lambda yields determinant rho for both inside and 1 for both outside, including repeated roots by continuity. For a mixed pair u inside, v outside, the determinant vanishes precisely at v=rho u, giving the stated strict window and spectral point. Unit-modulus roots are already on the essential curve by Calkin spectral mapping, including meeting or crossing points. The simple determinant zero gives a nonzero rank-one resolvent residue, hence algebraic multiplicity one. The examples replay by beta integration: rho=4/3 at alpha=0, rho=5/3 at alpha=3, t=5/2 lies only in the latter window, and lambda=-375/256 there. The unit-circle/origin mixture has all positive moments 3/4 and rho=4/3, matching area despite unequal moments. RESULT.md lines 25–73 suffice to replay the proof. The frozen verification notes and finite checker were inspected, not run; the checker alone does not address spectral completeness.

## originality

PASS

The rho=4/3 window, location, uniqueness and completeness on ordinary area are already matched exactly by indexed records. The supported distinct claim is the complete spectrum for arbitrary rotational measures with nonconstant radial law reaching the unit circle, including singular ones, with all spectral dependence on the measure collapsing to m2/m1^2. Neither the fixed-area classification nor the inspected weighted operator results provide this across-measure equivalence and phase change.

## value

PASS

This gives a complete, sharp spectral classification for a natural class of operators, not just a sufficient outlier test. Higher moments change the operator weights but have no effect on the spectrum for any quadratic, even across singular and absolutely continuous laws. Conversely two beta weights can create or remove an isolated simple spectral point without changing the symbol or essential curve. This separates measure-sensitive spectral information from the fixed-area antecedents and supplies an exact invariant applicable to other radial laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
