# Independent mathematical audit

## correctness

PASS

The SPD spectral inequality lambda^2<=(kappa+1)lambda-kappa leads to x*Ax/(||Ax||||x||)>=2sqrt(kappa)/(kappa+1). A symmetric squared-norm embedding compresses E=S^TS-I to operator norm <=epsilon on the Krylov-next subspace, giving Re(y*Gy)>=(c-epsilon)||ABy||||By||>0, hence G invertible, F positive definite and Re eigenvalue(F,G)>0 for every m. For nonscalar A the endpoint eigenvector plane gives G=q(2q-epsilon(q^2+1)), F=q^2(q^2+1-2epsilon q)>0 (q=sqrt kappa); G vanishes at epsilon=c and is negative above. When kappa=1, c=1 and all permitted distortions are safe. Independent symbolic exact identities and 180 seeded 5x5 multi-step SPD Krylov samples confirmed the computations, but finite sampling is not treated as a universal proof.

## originality

FAIL

A published 2026-10-12 result already states and proves the identical sharp threshold, same positivity-for-all-dimensions conclusion, singular boundary and negative two-mode counterexample. Its theorem covers complex Hermitian positive-definite A and arbitrary full-rank B, strictly broader than the submitted real SPD polynomial Krylov subclass. The later proof merely rewrites the same Kantorovich angle and sketch perturbation argument; fixed-A extremizer placement is an immediate endpoint-eigenspace specialization.

## value

FAIL

A sharp deterministic right-half-plane robustness radius for sketched harmonic Ritz extraction is a mathematically meaningful quantity, but the full theorem and sharp witness were already published October 12. The later version gives no independent mathematical classification, structural mechanism, new domain or sharp constant. Its each-fixed-A sharpness is an immediate application of the already published endpoint two-mode construction, not a substantive gap-filling extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
