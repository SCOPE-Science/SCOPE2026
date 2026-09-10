# Fallback Φ: Bessel-potential (L^{-1/4}) snowflake of H₃(Z₅)

H = Heisenberg mod 5, (x,y,z), generators a^±1=(±1,0,0), b^±1=(0,±1,0),
order 125, BFS diameter 6 (distance multiset logged in verification JSON).

Φ: first 64 nontrivial normalized-Laplacian eigenvectors fᵢ (L=I−A/4),
coordinate i ↦ fᵢ/λᵢ^{1/4}, i.e. Euclidean realization of the kernel L^{−1/2}:

‖Φ(u)−Φ(v)‖² = Σᵢ (fᵢ(u)−fᵢ(v))²/√λᵢ.

Verified over all 7750 pairs: L=d_H^{1/2}/‖Φ diff‖ ∈ [1.0729…, 1.9757…],
max/min = 1.8414… ≤ 8, min denominator 0.8608 > 0.

Margin to threshold 8: factor ≈ 4.34. Table: output/artifacts/Phi_64x125.csv (64×125).
Verifier: output/artifacts/verify_fallback.py → fallback_verification.json (VERIFY_PASS).
Distances cross-check: output/artifacts/H3Z5_distances.npy.
