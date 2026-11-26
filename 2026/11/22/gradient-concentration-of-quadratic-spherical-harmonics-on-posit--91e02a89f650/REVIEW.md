# Independent mathematical audit

## correctness

PASS

For trace-free symmetric Q, the tangential gradient is 2(Qx−(xᵀQx)x), so its squared norm is 4(||Qx||²−|xᵀQx|²), also over the complexification. The global norm in the stated coefficients is 2(||u||²+||v||²)/(d+2). Using conditional orthant moments, the scaled edge block has diagonal 1, entries a(d−2)/(2d) on edges sharing one vertex, and −2a²/d on disjoint edges. The trace-free diagonal block is I and its coupling to edges is (a/√2)B. Writing the edge block as αI+βBᵀB+γJ and using BBᵀ=(d−2)I+J gives the reported constant, incidence-kernel and standard sectors and all multiplicities. The characteristic polynomial is negative at α and L: for α, 3a−2<0 and 4a²−6a+2=2(2a−1)(a−1)<0; for L the first bracket is negative and the second is 1+(d−3)(2a−1)>0. L−α>0. Strict positivity and upper bound one for the actual fractions follow because a nonzero pure quadratic cannot have identically zero tangential gradient on either open region. Writing T=α+(d−2)β and k²=a²(d−2)/2 gives μ₊=ad/2+O(1) and μ₋=(T−k²)/μ₊=1−a+O(1/d), hence d/(π−2)+O(1) for the eigenvalue ratio. An exact independent generalized Gram calculation using infinitesimal rotations reproduced the characteristic polynomials for d=3 and d=4 and checked the three explicit d=3 values.

## originality

PASS

The strongest direct overlap is the published scalar-value calculation on exactly the same domain and harmonic space. Its moments and representation decomposition make the gradient computation accessible, but its evaluated operator is not the new one. The distinct contribution is the evaluated and ordered gradient blocks and the changed extremal sectors and conditioning law; neither use of orthant Gaussian moments nor general regional vector concentration is new.

## value

PASS

Exact observability of gradients rather than values on a canonical restricted region is a distinct problem. The result gives a complete squared-restriction spectrum, both extremal eigenspace dimensions and a sharp linear eigenvalue-ratio asymptotic, in contrast to the same-domain scalar quadratic law. This changes both the best-observed subspace and dimension dependence, not just a normalization or a numeric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
