# Independent mathematical audit

## correctness

FAIL

The exact integral and leading asymptotic are correct, but the frozen P₂ decimal is false. Put a=(y²+8)/(4√2) and H=√(a²+1+y²). At s=2 the inner x integral is exactly 1/[H(H+a)], so symmetry gives P₂=(1/π)∫_0^∞1/[H(H+a)]dy. Independent high-precision integration yields 0.113286148578841749617298…; the integral over [0,30] is 0.113224898589171211338918…, and the omitted tail is 0.0000612499896705382783802703…. This reproduces and explains the wrong headline decimal: verify.py:41 truncates y at 30 without a tail correction, and verification_output.txt:1 reports that truncated value. Replay with python -B /workspace/branches/audit-replay.py 5 (mpmath; no frozen script executed). Checking the analytic rest independently, the Euclidean compression has off-diagonal √(2/3) and residual row (0,1/√3); the sketched update gives discriminant (y²+8+4√2x)/3. Gaussian regression, changing W to W(I+ηηᵀ)^(1/2), gives the stated normalized density. In the Laplace coordinates t=u/s and y=w/√s, the integrand after factoring out 3^(-(s+1)/2) is bounded by (1+(2√2u/3+w²/2)/4)^(-2) for s≥4, integrable over u≥0 and real w. This justifies the stated prefactor by dominated convergence; the failure is in the asserted finite-s numerical conclusion, not the integral or rate.

## originality

FAIL

The surviving exact law and asymptotic are directly covered by an indexed broader Gaussian symmetric model, while its s=2 value is an evaluation of the covered probability (also within an independent general s=2 formula). The distinct Resultary records carry 2026-11-08 path dates, after the frozen record's 2026-10-18 path date. This establishes mathematical coverage at review, not historical priority or derivation in either direction. The older primary literature independently establishes the phenomenon and the extraction method, not this sharp rate.

## value

FAIL

The general question of exact real-Gaussian spectral pollution is worthwhile, but this record's corrected single example gives no scientific contribution distinct from the broader indexed law. The only prospective remainder, a corrected decimal for one sketch size, is ordinary quadrature of the covered formula. The small example can be illustrative, but neither it nor the changed decimal by itself gives an independent result warranting a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
