# Independent mathematical audit

## correctness

PASS

For a complex Haar vector the four squared amplitudes are independent exponential variables normalized by their sum, hence Dirichlet(1,1,1,1). Distinct eigenvalues force a commuting target to be diagonal. Under the Walsh coordinates of the finding put a=p_(++)+p_(--), V=(X+Y)/2 and W=(X−Y)/2. Dirichlet aggregation gives a~Beta(2,2); conditionally on a, V and W are independent uniforms on [−a,a] and [−(1−a),1−a]. Their conditional density times 6a(1−a) is the constant 3/2 on |V|≤a≤1−|W|, so Q=2a−1 is uniform between the stated endpoints. Its midpoint gives the unique a.e. optimal predictor, with a continuous point-mass version at interval collapse. The density of (|V|,|W|) is 6(1−v−w) on v,w≥0, v+w≤1. The conditional variance of Q is (1−v−w)^2/3, whose expectation is 2∫∫(1−v−w)^3 dv dw=1/10. Sign symmetry of V,W conditional on a makes Q orthogonal to the observed linear coordinates, and E Q²=1/5 from a's beta law. The real-affine projection removes precisely the constant and the X,Y components, since the real-linear parallelogram map is invertible. Multiplication by |c_3|² gives the two risks, and only c_3=0 gives loss zero. A fresh exact test checked the triangle/beta integrals and 560 simplex grid points; replay: python /workspace/replay_frozen.py 3. The grid is an algebraic check, not a proof of the conditional distribution.

## originality

PASS

Pass is for the geometry-specific explicit optimal predictor and quantitative residual risk, yielding a universal one-half ratio for the nonzero hidden direction. The uniform simplex law, marginal fiber-volume formula, inherited conditional uniformity, and optimal affine benchmark are not counted as new. Neither the inspected general marginal theorems nor the earlier quantitative regression criterion supplies the conditional-mean/error evaluation for this four-level geometry. The available earlier explicit three-level calculation has a genuinely different loss ratio.

## value

PASS

The four-level parallelogram is a natural first planar spectrum with one unobserved commuting coordinate. The explicit predictor and nonzero optimum determine the attainable recovery accuracy and quantify what is lost by insisting on an affine predictor for any target in that geometry. The factor compares two precisely motivated risks independently of the parallelogram embedding; it captures a different phenomenon than the known qualitative strict-improvement criterion or the marginal shadow density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
