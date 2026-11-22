# Independent mathematical audit

## correctness

PASS

For n>=7 count cyclic nonadjacent triples by three positive gaps: T=n(n-4)(n-5)/6; exact occupied pair counts are 0 at distance 1, n-5 at distance 2 and n-6 otherwise. Centering the circulant second moments and taking its Fourier transform gives gamma(n,k)=4[3/n-((n-6)(1+2cos theta)-2cos 2theta)/T] for k!=0, with the zero constant mode forced by the fixed particle number. The quadratic F_n(c)=3/n+[4c^2-2(n-6)c-(n-4)]/T decreases on the sampled domain for n>=10, and the short n=7,8,9 cases follow from exact root isolations/vertex distances. Its sampled positive spectrum is minimal at k=1,n-1 and maximal at the alternating modes. n=6 has two complementary configurations, covariance rank one and Walsh Gram eigenvalue 6. Expanding the exact extrema gives the squared condition ratio 1+8/n+O(n^-2). Independently generated all admissible triples and recomputed exact covariance, Fourier eigenvalues and extremal frequency comparisons at n=7..15 with separate code; these finite tests supplement the all-n quadratic proof. Checked Python verifier source (not trusted solely as a log).

## originality

PASS

Best-of-knowledge original sharp conditional three-particle covariance spectrum and mode-conditioning classification beyond classical gap counts and full-size Lucas-cube law.

## value

PASS

The fixed-three layer is the first nontrivial spatial hard-core microcanonical triple ensemble, and singularity changes sharply at six versus seven sites. The all-length exact extremal Fourier modes and condition ratio 1+8/n+O(n^-2) are concrete stability invariants for degree-one sampling, sharply contrasting with the grand-canonical Lucas-cube regime. The claim is not just an elementary count; it identifies the sharp spectrum and its real nullity boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
