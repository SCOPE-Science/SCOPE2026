# Scientific review

## Correctness — PASS
The exact domain is all **labelled** binary words of length \(2m\), Hamming weight \(m\), and least positive cyclic period \(2m\), for odd \(m\ge3\). A nonprimitive balanced word repeats a balanced block an odd number \(r\ge3\) of times; hence the deletion size is bounded by \(S_m\). Character orthogonality and binary Krawtchouk duality yield the exact central-layer transform and a minimum absolute even-frequency value \(M_m\). The explicit inequalities \(S_m<M_m\), verified separately at the five small odd cases and proved exponentially thereafter, prohibit extra Fourier zeros. Complement symmetry accounts for all odd-frequency zeros. Diagonalization of unnormalized XOR convolution proves rank and inverse statements. In the prime case, removing exactly the two period-two alternating words gives the signed formula; counting even/odd-position selections produces exact multiplicities, attainment of the minimum, and sharp conditioning. Stirling's formula and a vanishing relative deletion bound give the all-odd asymptotic.

An exact bitmask-period test followed by integer Walsh butterflies verifies all frequencies for \(m=3,5,7,9\); an independently structured integer binomial-multiplicity checker verifies the prime spectral formula for \(p=3,5,7,11,13\). Both passed. The infinite assertions rest on the proof, not finite enumeration.

## Originality — PASS under bounded scientific comparison
Ruskey–Sawada establishes fixed-density primitive necklace enumeration through the Möbius formula, but does not compute the Walsh spectrum on all labelled fixed-weight primitive words. Kopparty–Kumar–Saks establishes indexing of necklaces and period characterizations, not Fourier cancellation or invertibility. Standard Krawtchouk theory covers the undeleted central layer; that calculation alone does not rule out further zeros after all nonprimitive balanced words are removed. Accessible related results on Fourier sampling of Hamming slices address restricted Fourier matrices, not convolution by the primitive fixed-weight indicator. The earlier unrestricted-primitive-word support theorem does not imply the fixed-weight support theorem because restriction to a prescribed Hamming layer changes both the convolution kernel and Fourier cancellations.

A targeted mathematical-results comparison, full relevant archival primary-paper sections, and recorded local prior-claim comparisons did not identify the same inclusion-and-deletion nonvanishing result, prime signed multiplicity law, or condition-number asymptotic. Residual historical risks include uncatalogued equivalent harmonic-analytic treatments and folklore applications of Krawtchouk estimates; no independent priority certification is claimed.

## Mathematical value — PASS
The classical fixed-density necklace problem naturally asks what Fourier information survives restricting to **aperiodic balanced words**. A large structured deletion from the central layer could introduce new multiplier zeros. The result proves this never happens at odd half-length, characterizes the entire recoverable translation-invariant subspace for infinitely many dimensions, and gives sharp prime-order reconstructive stability and an exponential all-odd asymptotic. This is not just necklace enumeration or a mere finite example; it quantifies a meaningful information-recovery boundary between unrestricted periodicity and fixed-content primitivity.

## Residual limitations
The theorem does not classify even half-lengths, general noncentral weights, nonbinary alphabets, or exact finite positive minima for odd composite half-lengths. Source comparisons are bounded, so the priority judgment should not be read as exhaustive.

Self-review: passed. Independent audit: not yet performed.
