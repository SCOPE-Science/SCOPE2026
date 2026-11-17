# Self-review

## Correctness — PASS

The map preserves Lebesgue measure and is mixing. The piecewise-affine branch formula yields the mean and second moment by sums of powers. The critical transfer identity is not assumed: the image of the step-length observable is continuous, symmetric and piecewise affine with corners at fixed points of the expanding map, so a second transfer step scales every derivative jump by the exact factor \(b^{-2}\), leaving only an affine term; symmetry and mean preservation determine that term. Exact branchwise integration gives the first-lag covariance, and transfer duality gives all higher lags. The finite-window variance then follows from stationarity. The Gaussian conclusion additionally uses a bounded reverse-martingale/coboundary decomposition, rather than treating covariance summability as sufficient. The resulting rational asymptotic variance is strictly positive for every integer \(b\ge2\). A standard-library, exact-rational program independently tests short lags for several slopes.

## Originality — PASS, with priority limitations

Closest inspected sources: Jiménez-López and García-Garrido, *Trajectory arclength reveals chaos* (arXiv:2602.07660v3), Section 2.2, which studies continuous Hamiltonian arclength with correlation-based fluctuation bounds; Daquin et al., *Global dynamics visualisation from Lagrangian Descriptors* (arXiv:2206.04467), Section 4, which introduces finite-sum step-length descriptors for mappings; and Jenkinson, Pollicott and Vytnova, *Rigorous Computation of Diffusion Coefficients for Expanding Maps* (2018), which treats general computation and a different exact linear-observable example under doubling. These results motivate or permit statistical analysis but none of the inspected statements yields the absolute-step-length all-slope law or its negative/zero/positive covariance transition. A published result on conditional circular self-displacement phases is related but not identical: modular displacement alone omits interval-branch information required by the absolute difference. Only its discoverable summary was accessible, so the detailed implication comparison retains a stated risk. Historical novelty is a best-knowledge judgment and is not independently certified.

## Mathematical value — PASS

Path-length averages have been proposed as numerical signatures of dynamical behavior; their limiting variance and temporal correlations govern finite-window reliability. This theorem supplies an infinite, natural family of fully explicit calibration models, including an unexpected change from negative to zero to positive correlations as a single intrinsic expansion parameter varies. Exact zero correlations at both slopes two and four are not claimed to imply independence. The closed full-lag formula, finite-window variance, and Gaussian scale are jointly useful and go beyond generic rate bounds; the coordinate dependence is disclosed rather than hidden.

## Limitations and residual risks

The result is for integer expansion, Lebesgue sampling, a specific interval-coordinate Euclidean displacement rather than circular geodesic distance, and distributional Gaussian fluctuations rather than pointwise orbit fluctuations. Other literature might contain an unindexed equivalent formula. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
