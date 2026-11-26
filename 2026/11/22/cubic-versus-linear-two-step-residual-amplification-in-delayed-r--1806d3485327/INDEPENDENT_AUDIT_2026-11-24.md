# Independent mathematical audit

## correctness

PASS

Re-audited the repaired result and benchmark. In the residual coordinates B=AAᵀ=diag(K,1), the first size (1+t)/(1+Kt) gives multipliers −(K−1)/(1+Kt) and (K−1)t/(1+Kt). Since r₁−r₀=−α₀Br₀, the RD step size is (1+K²t)/(1+K³t); its multipliers are −(K−1)/(1+K³t) and (K−1)K²t/(1+K³t). Their products, squared and weighted by t/(1+t) and 1/(1+t), give the displayed gain, continuous and positive with zero endpoint limits. At z=K³t the high-mode contribution divided by K is bounded by z/(1+z)² and converges to it at fixed z. Both step sizes lie in [1/K,1], so the low-mode contribution divided by K is at most 1/K globally. The test z=1 gives the matching lower limit, and since the profile has a unique strict maximum there and vanishes at both tails, every maximizing z converges to 1. For DR the dual-quadratic identification gives the existing exact m=2 formula. Its y=Kt profile is y/(1+y)⁴ and is uniformly dominated by y/(1+y)²; the maximum is at y=1/3 with value 27/256. Square roots give 1/2 and 3√3/16 in the claimed norms. K=κ₂(A)²; asymptotics are in K, at fixed two-update horizon. The frozen rational checker was inspected, not executed; the all-parameter proof does not rely on the recorded finite diagnostics.

## originality

PASS

The corrected novelty claim is the exact RD maximum and maximizing start scale, not the algorithm, the two-mode multipliers, or the repeated-Cauchy comparison. The frozen account of DR overlap was too weak: the earlier Finding gives the very same variational formula, not merely a safety threshold. The actual same-rule RD findings concern long-run fixed-matrix decay, not this high-condition finite-horizon extremum.

## value

PASS

The sharp residual-difference growth constant and the scale of the worst initial spectral energy answer a concrete startup-spike question that eventual convergence and one-step objective results do not address. The scalar high-mode optimum and uniform control of the competing mode explain the separation from the credited cubic DR benchmark in κ₂(A). This is a finite-horizon worst-start result, not a typical-start or numerical stability guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
