# Independent mathematical audit

## correctness

PASS

For f(θ)=exp(−tθ^α) on [0,π], α>1 ensures f′(0)=0 and an integrable f″=O(θ^(α−2)) at zero. Two integrations by parts give πm²b_m=(−1)^m f′(π)−∫f″cos(mθ)dθ. The remainder tends to zero, and f′(π)<0 gives strict eventual parity signs and an absolutely convergent Fourier series. The exact circulant identity Λ_{N,k}/N=Σ_{j∈ℤ}b_{|k+jN|} preserves parity for even N. All modes with k and N−k at least the tail threshold have the baseline sign; each of the finitely many remaining positive low frequencies pairs with its distinct mirror for sufficiently large N. Its nonzero b_k dominates an O(N⁻²) alias tail; if b_k=0, every alias other than b_k has the strict baseline sign. The zero mode is positive by its row sum. This yields exactly N/2−1+2J negatives and no zero eigenvalues eventually. On the stated weak-damping interval, h=−f″ is positive on (0,π), even at the upper t endpoint, and πm²b_m=∫h[cos(mθ)−(−1)^m]dθ gives strict parity signs for every m≥1. Aliasing then proves the stated count at every even N, including N=2. This is an analytic proof; the frozen finite floating-point checker is only corroboration. There is no uniform cutoff or odd-grid assertion.

## originality

PASS

The checked continuum and finite-cycle results give overlapping Gaussian signs, individual negative witnesses, or moving positivity thresholds. None gives the full even-grid weak-damping inertia or the fixed-parameter finite index correction for all real α>1. The comparison establishes a distinct statement, not historical priority.

## value

PASS

Non-positive definiteness alone does not distinguish a single unstable direction from a negative subspace of dimension asymptotically N/2. The result provides the full signature at a concrete all-size weak-damping boundary and an exact, parameter-dependent finite correction to the asymptotic count, with a resolution of exceptional continuum zeros. This gives a benchmark for discretizations of the intrinsic kernel beyond earlier existence or recovery-threshold results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
