# Independent mathematical audit

## correctness

PASS

Checked RESULT.md lines 5–67. Evaluation at the n−2 survivors is invertible on the degree-m space by multiplying the interpolant by z^m and counting distinct nonzero polynomial roots. For extended weights, nw−1 has only the two complementary modes ±v. The two erased zero constraints are independent, since n is odd and 0<2πδ/n<π. Solving them gives the stated shifted cosine. Because 2v=−1 mod n, the adjusted index permutes the grid, and the cosine exceeds cos(πδ/n) exactly on 0<k<δ; equality occurs only at erased indices. Thus δ=1 means the original erasures differ by ±2. Summing the finite cosine progression gives H; unit total mass gives the sharp signed-error norm. Orthogonality gives squared cosine sum n/2 and hence the conditional variance for independent centered homoscedastic errors. Each separation class has n unordered pairs (odd n avoids a double-counted diametrical class). The csc² multiplication identity at π/(2n), followed by an odd-n reindexing and reflection, gives the half-sum of sec² equal to (n²−1)/2. This verifies both the mean variance and its normalization relative to the intact grid. The discrete uniform δ/n converges to Uniform(0,1/2); the map's singular endpoint has measure zero. Inverting it gives the stated tail including t=3/2, and the t^(−1/2) asymptotic implies infinite mean without asserting moment convergence. Inspected VERIFICATION.md, requirements.txt, verify.py and the recorded output without executing the source. Independently solved all real sine/cosine moment systems at n=5,7,11,19: exactly n positive patterns per size; respective average variance divided by σ² was 0.8, 0.7142857142857141, 0.6363636363636365, and 0.5789473684210524. The universal checks are analytic, not extrapolations of these bounded tests.

## originality

PASS

The supported distinct content is the exact near-Nyquist two-erasure sign/mass classification and the mean observation-noise floor with a limiting relative-amplification tail. Fourier moment systems, uniqueness by interpolation, and broad positivity theory are prior ingredients. The closest moved-node, kernel and frame comparisons do not imply this statement.

## value

PASS

Near-Nyquist exact integration after two sensor losses is natural and has no spare weights to mitigate noise. The exact sign law and conditional variance quantify the instability of specific missing patterns. The limiting relative variance law distinguishes typical behavior from the nonvanishing mean absolute variance, which is driven by the high-amplification patterns. These give structural guidance not provided by uniqueness or qualitative instability alone; no claim is made about arbitrary missingness, degrees or noise models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
