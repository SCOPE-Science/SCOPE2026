# Independent mathematical audit

## correctness

PASS

The frozen theorem is mathematically correct. Subtract x_star=−H^(−1) c_bar and work in the orthonormal Hessian eigenbasis, obtaining scalar dynamics r_j e−eta delta_(i,j). In an epoch the weights are 1,r_j,…,r_j^(n−1). The off-diagonal covariance is zero for IID and −s_j²/(n−1) for a random permutation by the zero-sum offsets; diagonal entries are s_j² in either case. This gives the two epoch variances as eta² s_j² Q_n and eta² s_j²(nQ_n−W_n²)/(n−1). With independent fresh epochs and zero-mean noise, sum the variances against S_(n,K) and add the same squared propagated initialization. The risk weights lambda_j/2 require no independence across eigenmodes. Subtracting reproduces the Finding; geometric sums factor Q_n−W_n² as 2(1−r^n)(r^n−r)/((1−r)^2(1+r)), with sign opposite to r throughout the stable range except at r=0. Opposite symmetric offsets supported in either signed eigenmode realize both mixed-spectrum signs for fixed H, eta, n and K. RR variance is bounded by n/(n−1) times IID variance since W_n²≥0, and summing with the shared nonnegative bias preserves the universal factor two even if the IID risk vanishes. The centered scalar n=2 ratio is (1−r)^2/(1+r²) and tends to two as r approaches −1 from above. Frozen check.py is a finite rational-path check and was inspected, not executed; the all-parameter result follows from the covariance proof.

## originality

FAIL

Demonstrated prior coverage, not an inference from a search hit or access failure. The published common-Hessian overshoot theorem 4354fb22c6bf gives the identical finite-epoch risk formula, same modewise threshold and stronger if-and-only-if spectral classification. The linear-offset and center versions coincide by c_i=−Hb_i up to arbitrary additive constants that cancel from the dynamics and objective gaps. The remaining factor-two observation, including sharpness, is a direct consequence of its displayed variances (4)–(6). There is no independent new remainder to repair.

## value

FAIL

The exact common-Hessian reversal is a meaningful question, but its answer and finite-epoch spectral classification are already supplied by the earlier specific theorem. As an incremental mathematical contribution the factor bound subtracts a nonnegative square from its variance formula, and the sharpness is the direct n=2 endpoint limit of that formula. This is a useful restatement for exposition, not a surviving substantive mathematical gap or independently valuable new finding under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
