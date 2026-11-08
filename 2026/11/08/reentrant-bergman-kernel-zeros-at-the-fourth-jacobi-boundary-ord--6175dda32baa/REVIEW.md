# Scientific review: Reentrant Bergman-kernel zeros at the fourth Jacobi boundary order

## Correctness — PASS

The monomial norm is the exact Beta integral \(B(n+t,5)\), giving the fifth-degree numerator \(Q_t\) of the scalar kernel. The Cayley transform maps its interior-disk zeros to right-half-plane zeros of \(T_t\). The exact Routh array has first-column signs governed solely by \(t-2\) and the quartic \(p(t)=2t^4+12t^3+12t^2-18t-5\), whose unique positive zero is \(\tau=(\sqrt{15+2\sqrt{19}}-3)/2\). The sign variation proves counts \(1,0,2\) on the three open parameter regimes. Explicit factorization at \(t=2\), a Hurwitz argument at \(t=\tau\), and positivity on the positive scalar axis settle all boundaries and root types. The extracted standalone script verifies exact symbolic identities and eight numerical instances; finite tests are not used as proof of the universal counts.

## Originality — PASS, with residual priority risk

The closest radial-weight source, Perälä (arXiv:1703.05976, sections 2–3), proves broad qualitative finite-zero statements and gives constructions; it does not imply the particular Jacobi parameter thresholds. Miña-Díaz (arXiv:2212.08118, theorem 1.1 and proof) treats finite Blaschke-power weights, not the independent fourth-order boundary factor. Beberok (DOI 10.21136/CMJ.2017.0073-16, sections 2–4) uses Jacobi polynomials and Routh-Hurwitz methods for different multidimensional ellipsoid domains, without an all-real-parameter classification for the present disk kernel. Earlier classifications for boundary orders one and two are not a stronger theorem covering the fourth-order result; they do not exhibit the nonreal return transition. Actual published-record queries covered the radial-weight name, the polynomial numerator, Schur-stability aliases and the threshold \(t=2\). No directly implying theorem was located; an unlocated generalized Eulerian root-location classification remains possible.

## Mathematical value — PASS

The theorem identifies a nonmonotone Lu Qi-Keng phase diagram for a natural beta/Jacobi radial weight. The sharp parameter values govern two different boundary-crossing mechanisms: departure of one negative real zero and entrance of two nonreal conjugate zeros. A formerly zero-free region can become zero-bearing again when the origin exponent increases, a qualitative contrast to the previously classified lower-order Jacobi weights. The result is a complete natural one-parameter classification, not a single numerical example.

## Limits

The theorem covers boundary order four only; it gives no high-order universal zero count and no numerical conditioning theorem. An undiscovered general Schur-stability theorem might give an alternative derivation or take priority. Supplementary code checks finite parameter choices but the mathematical argument is uniform.

Self-review: passed. Independent audit: not yet performed.
