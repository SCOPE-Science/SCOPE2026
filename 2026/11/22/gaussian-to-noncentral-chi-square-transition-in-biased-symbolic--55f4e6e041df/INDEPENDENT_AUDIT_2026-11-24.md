# Independent mathematical audit

## correctness

PASS

Parseval for ordered histogram squares, with N self-matches subtracted and division by two for unordered pairs, gives the stated collision identity. At fairness the overlap equality constraints are forests of residue chains with exactly k independent constraints; the centering is therefore exact. Translated Walsh supports differ only at boundedly many boundaries. At fairness only a matching translated support has nonzero covariance, yielding unit long-run variance per anchored shape. Near fairness a bounded finitely dependent triangular-array CLT follows by taking independent blocks of growing length o(√N) with fixed separating gaps; the discarded centered rows have variance o(N), and covariance varies continuously in p. Means of the normalized sums are −2θ for singleton supports and vanish for higher degrees. Squaring gives (k−d)/2^{k+1} per shape (half the word-covariance eigenvalue), with one singleton and 2^{d−1} shapes for d≥1. Fourth-power uniform integrability follows by splitting into finitely many independent subsequences and bounding higher moments. The resulting mean and variance, including k=1, agree with (2). Expanding the collision histogram around Nπ leaves a centered quadratic term O_p(N), uniformly in p by the finite-dependence L² bound. The linear score π(W_i) factors over the window; unshared digits give A, shared digits give B, yielding the stated lag covariance. Since B−A²=p(1−p)(2p−1)²>0, the variance is positive for the stated fixed p. For δ→0, with X_j=(−1)^{B_j}, the score is the product of (1/2−δX_j). The centered degree-one terms sum to −kδ·2^{1−k} times the centered digit sum up to O_k(|δ|) endpoints; the sum of higher-degree centered terms has L² size O_k(√N δ²). The centered collision remainder divided by N^{3/2}|δ| vanishes under √N|δ|→∞. The digit CLT, allowing either sign of δ_N, gives (4). Independently obtained exact overlap probabilities matched the 1,364 entries of the fair Walsh-transformed word covariance for k=1,…,5; that is finite consistency evidence, not a triangular-array limit proof. Frozen checker and output inspected, checker not executed.

## originality

PASS

Credit the uniform full spectrum, entire θ=0 law, proof structure, and the standard fixed-law Gaussian mechanism as existing coverage or technique. The surviving contribution is the evaluated bias crossover for overlapping windows: the bias direction in the known spectrum, the exact overlap-dependent biased variance, and a varying-law Gaussian limit outside the local window that matches its quadratic variance degeneration. The central spectrum alone and general fixed-law U-statistic results do not supply this three-regime comparison.

## value

PASS

The same natural recurring-word statistic changes normalization at a scale where weak bias and dependence among overlapping windows both matter. The evaluated crossover identifies which of the prior fair modes carries the signal, gives the correct biased noise level for the actual overlapping design, and justifies a Gaussian approximation when a fixed-bias limit is not uniform enough. Taken together these facts answer a concrete interpretation and scaling question; the fair law or the existence of a fixed-bias CLT alone would not be a valuable new result here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
