# Scientific review

## Correctness — PASS

On the three-dimensional normalized-Laplacian band, complex Fourier modes are orthonormal. Applying a real cosine/sine rotation and a second orthogonal rotation that adds/subtracts the two site vectors reduces the full four-by-three unweighted measurement Gram matrix to one scalar and one two-by-two symmetric block. The displayed spectrum follows from the latter block's exact trace and determinant, including antipodal and coincident limits. A negative evaluation of the two-by-two characteristic polynomial at \(2(1-q)^2/(1+q^2)\) locates its two roots and proves the strict monotonicity of the smaller. The other scalar branch decreases, so their unique crossing is the global E-optimum; the positive quadratic root, the finite-grid bracketing rule, and the short-time asymptotics are checked algebraically. Direct matrix construction with 10,968 comparisons passed. No finite enumeration is used to establish the infinite theorem.

## Originality — PASS relative to inspected literature

The September 2026 graph Paley–Wiener preprint, especially its finite-dimensional Section 4 and path experiments, gives the general raw time-evolution analysis matrix but not an explicit two-site E-optimal cycle-angle law. The November 2024 noisy graph-dynamics paper uses MSE/traces of inverse Gram matrices and heuristic/numerical placement rather than this exact smallest-eigenvalue classification. The nearest published mathematical finding on finite cycles studies spectral **demixing**, with separate outputs for each Laplacian eigenspace: it explicitly excludes optimization of the unweighted time-trajectory matrix. Its time-independent sensor prescription does not imply the new \(q\)-dependent crossing. Searches for cycle heat two-time E-optimal placement, three-mode formulas, and finite graph dynamical frames identified no dominating published theorem. Residual risk: an equivalent three-mode sensor-design solution may exist in the older optimal experiment-design literature under another normalization. Priority has not been independently confirmed.

## Mathematical value — PASS

This is the smallest Fourier band that exhibits an eigenvalue-multiplicity obstacle on cycles. Two raw time levels and two sensors are measurement-minimal for this three-dimensional space. The exact E-optimal law reveals a nontrivial sensor-layout shift: the optimal cosine is \(1/2\) at strong diffusion but tends to \(1\) quadratically as the observation times collide. This distinction from spectrally demixed design has practical consequences for worst-case stable reconstruction, and the exact neighboring-cosine rule handles every finite cycle. The claim is not merely restating a finite-dimensional singular-value criterion; it solves its all-parameter optimization in a natural nontrivial case.

## Closest sources and limitations

- Bulai, Cabrelli, Cordero, Molter, Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472 (2026), especially pp. 19–25.
- Aldroubi, Bailey, Krishtal, Miller, Petrosyan, *Reconstructing Graph Signals from Noisy Dynamical Samples*, arXiv:2411.12670 (2024), particularly the placement and MSE formulation.
- *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, published October 2026; relevant result explicitly distinguishes its demixed norm from raw time samples.

The assertion applies only to the specified three-dimensional band, normalized heat dynamics, two sensors, two time levels and uniform measurement weights. It does not solve higher bands, condition-number minimization or MSE minimization. There is no independent publication-priority certification.

Self-review: passed. Independent audit: not yet performed.
