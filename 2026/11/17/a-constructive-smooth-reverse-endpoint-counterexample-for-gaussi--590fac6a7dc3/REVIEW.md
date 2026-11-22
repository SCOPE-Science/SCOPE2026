# Independent mathematical audit

## correctness

PASS

The normalized antiholomorphic Gaussian monomial h_n with C_n=2^(n/2+1)(n²+1/2)^(n+1)/sqrt(n!) has Toeplitz weighted backward shifts w_k=(1+2n²)^-k sqrt(binom(n+k,k)), with w_0=1 and ratios <=sqrt(n+1)/(1+2n²)<1. Its conjugate packet does not affect the e_n-to-e_0 coefficient. Direct Gaussian convolution yields heat packet C_n bar z^n/(1+n²)^(n+1)*exp(-n²|z|²/(1+n²)); radial maximization and Stirling give ∥H p_n∥∞<=4e/(2πn)^1/4. Taking n_j=(j+1)^12 scales the j-th packet heat bound O(j/(j+1)^3), making the tail uniformly O(J^-1) and in C_0. At finite stage every required separation inequality is an eventually strict Gaussian-decay condition; the least passing integer center exists. Those conditions imply local C^∞ convergence, coherent-kernel L² admissibility and form-domain inclusion for translated e_{n_j}. The main matrix coefficient is j and all past/future off-diagonal terms are summable <2^-j-4. Independently evaluated high-precision heat maxima and weighted-shift ratios at n=1,2,4,16,4096; peaks and ratios obey asserted envelopes. This does not compute the infinite centers; their existence follows from the proved decay, not numerical search. No extrapolation from the finite code alone was used.

## originality

PASS

The published reverse endpoint counterexample is existential via Baire methods; the claimed novelty is a fully deterministic smooth real construction with quantitative uniform heat-tail and divergent witness coefficients. An earlier explicit smooth Fock witness is in the opposite bounded-operator/unbounded-heat direction, so is not stronger coverage. Full original Virtanen text was not obtained and priority remains best-of-knowledge.

## value

PASS

The abstract failure of the reverse Berger-Coburn endpoint is known, but replacing an existence/Baire argument by one uniquely specified real smooth symbol and an effective center recursion with quantitative uniform heat-tail and explicit unbounded matrix coefficients is a substantive constructive refinement for a natural operator-theoretic endpoint. It supplies verifiable witness structure not mechanically contained in existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
