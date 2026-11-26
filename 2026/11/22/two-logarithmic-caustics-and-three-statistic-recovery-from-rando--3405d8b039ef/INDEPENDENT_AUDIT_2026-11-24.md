# Independent mathematical audit

## correctness

PASS

Checked the frozen result, verification notes and diagnostic code without executing the uploaded code. The orthographic shadow support function in the plane is the restriction of the ellipsoid support function, so S,T are eigenvalues of the compression of diag(A,B,C). Squared normal coordinates have Dirichlet(1/2,1/2,1/2) density with prefactor 1/(2 pi); evaluating the secular numerator at the three eigenvalues inverts the interlacing variables, with Jacobian (S-T)/[(A-B)(A-C)(B-C)]. This verifies the joint density and the t Jacobian in r=s/t. Independently checking the singular integrals, at the corner (B,C) put y=t-C, x=s-B=C(r-B/C)+r y; the marginal integrand is a smooth factor times 1/sqrt(x y), with leading factor C/[2 pi sqrt((A-B)(A-C))]. At (A,B) put y=B-t, x=A-s=-B(r-A/B)+r y and the corresponding factor is B/[2 pi sqrt((A-C)(B-C))]. In each case translate y to its allowed lower endpoint. The resulting integral of 1/sqrt(u(u+const*|r-r0|)) contributes log(1/|r-r0|) divided by sqrt(r0), with bounded remainders. Away from these two corners the interior endpoints have only simple square-root singularities; the two neighborhoods are disjoint even when their ratio levels coincide, so the coefficients add. At s=B+u,t=B-v the endpoint integral over u+v < B*eps uses the beta factor pi and then the integral of u+v, giving B^2/[4(A-B)(B-C)]. At s=A-u,t=C+v the region u/C+A v/C^2<eps gives the stated C^(3/2)/[2 sqrt(A(A-B)(B-C))] coefficient; in both cases rescaling controls the remainder for fixed strict gaps. Substituting the only two squared shapes, (1/p,1/(pq)) and (1/q,1/(pq)), at the higher caustic gives coefficient ratio p sqrt(q)>1. Coincident caustics force B^2=AC and determine the shape already. These are exact pointwise results for the squared visible ratio and recover no absolute scale; the recorded floating-point diagnostics are not used as proof.

## originality

PASS

Pass the explicit normalized two-sided logarithmic strengths and coefficient-based resolution of the two shape candidates, together with the calculation of the endpoint tails in this law. Do not credit the classical forward apparent-shape kernel, projected-ellipse geometry or preferred principal-ratio locations as new. The actual accessible alternatives concern a population mixture or observables other than squared shadow aspect ratio. The old cited primary passages could not be checked in full; this is best-of-current-knowledge, not a priority certification for every amplitude or tail formula.

## value

PASS

The two natural caustic locations leave a genuine middle-axis ambiguity. A single measurable feature of the same one-dimensional projection law provably resolves it, despite the loss of the orientation and the absolute scale, and the merged case is classified too. The local amplitudes and sharp endpoints also tell how probability concentrates near the geometrically special views. This is a nontrivial fixed-shape inverse theorem, not merely presentation of a known forward density; it asserts neither mixture identifiability nor a practical finite-sample estimator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
