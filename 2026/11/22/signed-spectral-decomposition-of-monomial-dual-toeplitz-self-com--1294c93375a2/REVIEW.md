# Independent mathematical audit

## correctness

PASS

Normality of multiplication by z^m gives K=P M Q M* P-P M* Q M P, with this sign for S*S-SS*. At angular index k, Q contributes only the two normalized input harmonics of indices k-m and k+m; subtracting the local harmonic projection gives the signed difference of their rank-one forms. Conjugation exchanges the two signs at opposite indices, and the two projected generators coincide at zero. For k>=m the first generator is already harmonic before projection, and the remaining squared norm is b_k. The moment quotient r_m(k)=h_{k+m}/h_k is strictly increasing by its product of increasing consecutive ratios. For 1<=k<m the radial exponents k, 2m-k, 2m+k are distinct on a measure with full radial support; their projected vectors have strictly positive Gram determinant. The signed block has trace A_k-B_k and determinant G_k^2-A_k B_k, yielding the claimed opposite-sign roots and infinite kernel. The product expansion to second order gives b_k~m^2(alpha+1)k^(-2); counting the two tails gives the stated signed counts and s_n, compactness, sharp p>1/2 and trace zero. Summing r_m(k+m)-r_m(k) telescopes; adding twice the central discriminant roots yields the exact trace norm. For alpha=0, m=2, exact h_j=1/(j+1) gives the displayed central roots and decreasing b_k=4/((k+3)(k+5)), so the central operator norm really exceeds the whole tail. Independent finite check: 924 angular cases, including nonintegral weights, computing S*S and SS* as successive exact compressed multiplications; python3 /workspace/branches/reproduce_records_1_to_4.py. This corroborates block identities; the analytic argument proves the infinite spectrum. The frozen checker and verification record were inspected, not executed or counted as independent evidence.

## originality

PASS

Best-of-knowledge pass for the exact spectrum of this complement compression, especially its rank-two central blocks and their contributions to the nuclear and operator norms. The leading asymptotics, ideal cutoff and tail moment differences substantially overlap the harmonic-subspace calculation and are not standalone novelty across compressions. The nearest accessible catalogue statements concern different operators; identified full-text attempts for especially relevant papers and records were unsuccessful, not negative evidence.

## value

PASS

Exact signed central spectra resolve a natural operator invariant not fixed by tail classification and can change the global norm, already on the ordinary disk. Their inclusion yields a complete spectrum and an explicit nuclear norm for all beta weights and monomial degrees; the result is not just a restatement of shared Schatten asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
