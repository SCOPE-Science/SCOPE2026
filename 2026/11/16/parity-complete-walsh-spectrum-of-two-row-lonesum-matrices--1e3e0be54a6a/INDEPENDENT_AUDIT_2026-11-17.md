# Independent mathematical audit

## correctness

PASS

Ryser forbidden 2×2 pattern for two rows gives union A={00,01,11}^n and B={00,10,11}^n with intersection {00,11}^n. Their one-column character sums multiply to W=3^c00[(-1)^c01+(-1)^c10]-2^n 1(c01=c10=0). Odd total frequency weight gives exact cancellation. Even positive mixed count yields ±2*3^c00; no mixed columns gives 2*3^c00-2^n nonzero for n>=2 because powers 3 and 2 cannot agree, and frequency with two 01 columns realizes |W|=2. Fourier support equals all even frequencies, giving rank/nullity half, pseudo-inverse 1/2, condition number (2*3^n-2^n)/2 and optimal p1/pinf projection (I+translation-by-one)/2. Independently enumerated all matrices and transforms n=1..5, counts 4,14,46,146,454 and surviving counts 1,8,32,128,512. n=1 correctly excluded.

## originality

PASS

Best-of-knowledge PASS for full Walsh Fourier support and sharp spectral gap. Kim-Krotov-Lee and Cameron et al establish lonesum forbidden submatrices and unweighted acyclic K2n orientation counts, not every signed edge-frequency transform. Published K2n indegree-parity results use vertex parity feasibility rather than edge-frequency Walsh transform; SCOPE matching-tree and K3n sources concern other indicators/families.

## value

PASS

Two-row lonesum matrices form the first nontrivial natural class of reconstructible binary matrices and K2n acyclic orientations. The full signed spectrum and exact recoverable range determine natural operator-theoretic invariants absent from the unweighted counting theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
