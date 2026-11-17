# Independent mathematical audit

## correctness

PASS

First Lanczos Ritz value equals Gaussian Rayleigh quotient, hence signed bias B=n E_w log(sum_i w_i exp(x_i))−sum_i x_i, w~Dirichlet(1/2,...,1/2). Jensen gives B>=0; strict separate convexity ∂²_i B=nE[p_i(1−p_i)]>0 forces all worst spectra to endpoints 1,κ (no interior extremizer). Endpoint sums T~Beta(j/2,(n−j)/2) give exact B_j. For n=2, integrate arcsine to obtain 4logcosh(logκ/4). Beta moments give small-δ tie-breaking to j=floor(n/2), and dominated convergence/digamma gives high-κ unique j=1. Independent SciPy beta quadratures for n=2,4,5 at representative κ confirmed closed n2 formula and near/far multiplicity crossover.

## originality

PASS

Best-of-knowledge: strict coordinatewise convexity identifies exact worst-case one-node Gaussian Lanczos expected logdet bias by a max over beta integrals, with conditioning-dependent unique extremal multiplicity. The full-text accessible 2026 Mbingui–Tambue–Karambal stochastic Krylov preprint develops Lanczos/Hutch++ trace error bounds and algorithms, not the inspected condition-number-sharp one-node expectation law. The related single-probe paper considers multiple nodes. Priority risk remains from classical Jensen/Dirichlet logsumexp extremal literature.

## value

PASS

The least expensive nontrivial stochastic Lanczos log-determinant rule has a natural, previously unquantified worst systematic overestimate at a fixed spectral condition number; the exact finite-dimensional upper envelope and shift from balanced to singleton spikes provide sharp calibration and conceptual information about bias regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
