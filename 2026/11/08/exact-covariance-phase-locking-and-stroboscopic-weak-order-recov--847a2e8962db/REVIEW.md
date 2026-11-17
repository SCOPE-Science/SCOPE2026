# Independent mathematical audit

## correctness

PASS

Solving the stated implicit quadratic-potential update gives z_{k+1}=R_θ(z_k+σe₂ΔW_k), θ=2 arctan(ωh/2). Orthogonal rotation makes E||z||² increase by σ²h, proving the trace law. Independent noise increments yield C_N=σ²h Σ_{j=1}^N R_{jθ}e₂e₂ᵀR_{jθ}ᵀ, whose traceless complex sum S=Σ e^{2ijθ}=e^{i(N+1)θ} sin(Nθ)/sinθ gives the claimed spectrum and all isotropizing h via θ=mπ/N (N≥2). At fixed T=Nh, θ/h=ω−ω³h²/12+O(h⁴), and the right-endpoint Euler–Maclaurin formula produces first-order tensor σ²[fω(T)−fω(0)]/2. It vanishes exactly at ωT∈πZ; then frequency drift gives σ²ω²T diag(1,−1)/24 at order h², with numerical mean error also O(h²). Fixed N, h→∞ sends θ→π and normalized covariance to rank-one projector, whereas exact normalized →I/2. Independent covariance recursions matched the spectral tensor in 20 parameter cases; 8 fixed-time asymptotic cases corroborated, not proved, infinite-family claims.

## originality

PASS

Best-of-knowledge PASS with unusually explicit preceding-method risk: Chen et al. already establish the *same harmonic-oscillator numerical scheme* and exact expected energy trace, and the 2006 Hong–Scherer–Wang stochastic midpoint rule is likely the same map under normalization. Their results are prior art, not new algorithm claims. The inspected accessible original describes only general O(h) weak error and fixed-T=1 numerical moments; no exact finite-N isotropy list or half-period stroboscopic coefficient was located. The full 2006 midpoint article remained inaccessible; it could contain equivalent phase computations and remains material risk, not automatically a failed O assessment.

## value

PASS

A positive-semidefinite moment method can exhibit perfectly isotropic noise at isolated phase steps despite not matching exact covariance, and its leading error unexpectedly drops from first to second order at a physically motivated set of times. Exact constants and large-step anisotropy expose practical diagnostics for moment observables without claiming all-observable weak order two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
