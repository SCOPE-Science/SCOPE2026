# Independent mathematical audit

## correctness

PASS

PASS: The Gaussian transform of two tempered monochromatic tones is absolutely convergent; with u=e^{-π(x+a)²}, v=e^{-π(x-a)²}, one full beat period T=(2a)^{-1}, and real Hermitian Frobenius input/normalized L² two-bin output, Fourier-mode orthogonality exactly splits the lift into the 2×2 swapped diagonal block and two equal off-diagonal scalar blocks. Singular values are u²+v², v²-u² and √2uv twice. Since v>u>0, smallest m_a(x)=min{2e^{-2π(x²+a²)}sinh(4πax), √2e^{-2π(x²+a²)}}. The ratio is √2sinh(4πax) and crosses 1 once at x_C=asinh(1/√2)/(4πa); the difference branch has exactly one maximum x_D tanh(4πax_D)=a, while the other branch strictly decreases. Therefore unique global optimizer min(x_C,x_D) and regime threshold a_*²=asinh(1/√2)/(4π√3). At equality both positions coincide. Independently solved xD,xC at a=.08,a_*,.35 and checked that a grid had no superior candidate. A single bin has a nonzero Hermitian diagonal kernel, and its weighted-diagonal swap preserves rank-one intensity coefficients generically. The proof is exact; a sampled frequency grid cannot by itself establish global optimization.

## originality

PASS

PASS (best-of-knowledge): Earlier two-line Gabor phase-retrieval results establish qualitative uniqueness for bandlimited L² signals, but do not optimize Gaussian symmetric frequency placement or a 4-dimensional real Hermitian singular spectrum for two tempered plane waves. Another published Gaussian-bin result derives a different 3-tone, 8-sample spectrum and optimizes relative sampling time stagger, not this two-tone bin offset. Standard Gaussian Fourier integrals and 2×2 singular-value calculus are shared methods; the precise sharp design and normalization-dependent threshold were not located in examined sources.

## value

PASS

PASS: For minimal two-frequency-line phaseless measurements of a natural two-tone model, conditioning directly governs stability of a specified linear lift. The unique optimal symmetric offset and exact separation threshold are motivated design rules; they determine quantitative tradeoffs beyond qualitative identifiability and give a meaningful boundary, not an arbitrary parameter choice. No broader nonlinear universal stability is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
