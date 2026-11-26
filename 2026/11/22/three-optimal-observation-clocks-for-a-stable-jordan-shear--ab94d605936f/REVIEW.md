# Independent mathematical audit

## correctness

PASS

With dimensionless shift u and gap d the two-row design is e^(-u) B(d) S(u), where S is a determinant-one shear. Delaying at fixed d lowers the squared determinant, strictly increases the explicit inverse trace, and increases the unscaled Gram trace at fixed determinant (hence lowers its lesser eigenvalue), with another loss from the scalar prefactor. Thus all criteria uniquely start at zero. At zero the determinant scales as d² exp(-2d); the inverse trace in noise-normalized units is 1+(exp(2d)+1)/(rho² d²). Their turning points are 1 and c. The A derivative's sign factor is -1, not zero, at d=1 (proof §2 wording slip); it increases strictly thereafter and its unique zero is unchanged. For E, trace P=1+exp(-2d)(1+rho²d²) and determinant K=exp(-2d)rho²d² imply the smaller eigenvalue is simple and lies in (0,1) since the row Gram has a nonzero off-diagonal and first diagonal 1. The derivative is positive for d<=1. For d>1 put v=rho²d(d-1); the derivative sign is the sign of lambda-v/(1+v). Substituting v/(1+v) in the characteristic polynomial gives the sign of 1+v-(d-1)exp(2d), as the test point is below the larger root. Hence the derivative is positive through c and changes sign exactly once above c: G(d)=exp(2d)/d-1/[d(d-1)] is strictly increasing from G(c)=0 to infinity. This proves uniqueness and horizon clipping. At the root the smaller eigenvalue is v/(1+v); differentiability of G inverse at 0 gives the displayed small-shear coefficient, and log rho=z-(log z)/2+o(1) gives the large-shear expansion. Independent bisection and direct Gram eigenvalue evaluation at rho=4 gave c=1.108857552878545, z=1.669845528726068 and E/A/D lesser eigenvalues 0.947080475, 0.918283293, 0.903161655. The frozen check.py banner says six symbolic identities although there are five explicit symbolic asserts; neither that banner nor the reported random comparisons is required for the result. Read 'dissipative' as stable here, not as Euclidean dissipativity for all shears: the latter would restrict s<=2a, which the actual theorem does not require.

## originality

PASS

The model is an exponentially weighted straight line and the Fisher/criterion machinery is standard. The substantive distinct result is the simultaneous exact fixed-equal-allocation classification, especially the shear-dependent E clock, clipping and asymptotics in the stated physical coordinates. The nearest approximate-design E result has a different admissible set and a different support equation.

## value

PASS

In a canonical nonnormal two-state system with a strict measurement budget, equal event weights are mandatory rather than convenient. The result shows concretely when determinant, average variance and worst-direction variance give different sampling decisions, and how the E clock continues to move as the shear increases while the other two saturate. It is an analytic benchmark, including the short-horizon clipping cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
