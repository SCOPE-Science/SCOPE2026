# Independent mathematical audit

## correctness

PASS

Verified normalization by the series, then μ=tS′/S−2 and v=tμ′ by exponential-family differentiation. The decreasing birth ratio gives v−μ=Cov(X,r_X)<0 by the independent-copy covariance identity and nondegeneracy. Reconstructed A, T and all four exponential coefficients of N using formal differentiation with z=e^t. Exact coefficients vanish through degree 9, are negative in degrees 10–14, then positive through degree 25; the shifted Q_k at n=26+u have strictly positive coefficients, establishing the positive tail. Thus N/t^14 is strictly increasing from minus to plus infinity (the negative t⁻⁴ and positive t terms suffice at the ends); its unique zero changes F′ from negative to positive. Independent rational Taylor and interval calculations certify both the quoted t* bracket and the quoted minimum interval. Since (log R)′=(v−μ)/t, R is strictly decreasing; the small-t normalization and large-t μ=t+(t−2)/(t²−t+1)+O(e^(−t)/t) give limits 1 and 1/2. The normalization also yields the quoted expansions for F. Replay: python3 /workspace/branches/review_replay.py 2 (symbolic and sign checks); interval replay at /workspace/branches/293d66c6-a087-406a-b657-88584f045100/record2_replay.py. The supplied checker was inspected, not executed.

## originality

PASS

The published model definition and general weighted-Poisson underdispersion are prior. The supported distinct contribution is the proof of the model's global dispersion shape and certified unique minimum, together with the explicit sharp mean-matched zero calibration for that same law. The general sign theorem plus exponential-family differentiation already supplies the direction of zero-ratio monotonicity; that general mechanism is not new.

## value

PASS

The Fano factor and the zero probability at matched mean are natural diagnostics for deciding whether this count family behaves like an ordinary Poisson law. The theorem corrects a published qualitative characterization, gives a nontrivial global shape and a sharp worst departure, and distinguishes that nonmonotone profile from the monotone zero calibration. These population facts are useful without making a claim about the original datasets or fit procedures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
