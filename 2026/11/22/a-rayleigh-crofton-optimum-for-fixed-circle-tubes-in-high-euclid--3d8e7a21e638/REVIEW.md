# Independent mathematical audit

## correctness

PASS

I checked the topology independently in the normal disk bundle of the circle, which is injectively parametrized for r>1. At angle theta, a hyperplane with signed offset m and normal projection length S cuts a convex disk fiber if |m-rS cos(theta)| is at most sqrt(1-S^2 sin^2(theta)). For generic S<1 each nonempty fiber contracts continuously to the minimum-norm point of its affine slice. With u=cos(theta), the feasible set in [-1,1] is an interval (the defining quadratic has positive leading coefficient S^2(r^2-1) for S>0). Its inverse cosine image is one contractible arc, two disjoint arcs or the entire circle according to whether it includes one, neither or both endpoints. Excluding null transitions, the endpoint tests |m-rS|<1 and |m+rS|<1 on 0<=m<1+rS give the three asserted lengths. Normalization uses the orientation-dependent available offset length, not a uniform orientation conditional on a hit. S squared has the stated beta law. Differentiating the truncated first moment gives the sign I-B, a strict crossing, and substitution gives the optimum probability 2B. Rescaling by sqrt(d) yields a Rayleigh projection and convergence of the truncated first moments by the bounded second moment. In rescaled inverse radius t, the critical sign tends pointwise to E[Y 1(Y<=t)]/E[Y]-Pr(Y>t), which increases strictly from -1 to 1; bracketing its root proves convergence of the optimizers. For Rayleigh Y the zero reduces to the displayed erf equation. Independent quadrature reproduced 0.734903908748044 and 0.792442639799811; in d=4 the exact equation is r^3-r-1=0.

## originality

PASS

Finch gives the exact underlying 3D slice law and 3D optimum; they are not new. Changing the ambient space while keeping the circle plane fixed changes the Crofton projection law. The cited growing spherical-core optimization has a different body and conclusion. The checked passages do not give the fixed-core d>=4 optimizer or its Rayleigh limit, nor a stronger theorem already supplying them.

## value

PASS

Holding the circle fixed is a natural alternative to growing the spine dimension and isolates the effect of adding normal directions. The exact three-type law and maximum identify how much radius is needed to offset the concentrating normal projection. The contrast with the spherical-core optimum is qualitative as well as numerical: the optimal radius diverges and the optimal probability is bounded away from one. This is more informative than the d=4 constant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
