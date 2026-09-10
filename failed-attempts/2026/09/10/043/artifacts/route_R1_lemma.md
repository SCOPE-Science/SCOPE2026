# Route R1 — Distortion vs nonlinear Poincaré (rigorous elementary lemma)

**Lemma (Linial–London–Rabinovich form).** Let G=(V,E) be connected d-regular
(n=|V|), A its normalized adjacency, X a Banach space,
γ = γ(A,‖·‖_X²) < ∞. Let f:G→X have Lipschitz constant L and lower constant
l>0 (‖f(u)−f(v)‖ ≥ l·d_G(u,v)), distortion D=L/l. Then

  D² ≥ Ā/γ,  Ā := n⁻² Σ_{u,v} d_G(u,v)².

*Proof.* Poincaré: n⁻²Σ‖f(u)−f(v)‖² ≤ (γ/dn)Σ_{edges}‖diff‖² ≤ γL²
(each edge has d_G=1 so ‖diff‖≤L). Lower: LHS ≥ l²Ā. Divide by l². ∎

**Corollary (average-distance form).** For d=3, |B_r(u)| ≤ 1+3(2^r−1) < 3·2^r.
With r=⌊log₂(n/6)⌋, fewer than half the pairs lie at distance <r, so
Ā ≥ r²/2 and D ≥ r/√(2γ) = Ω(log n/√γ).

**Use for target.** R1 gives D ≥ c·log n_k/√γ_k(X). Since log n ≥ √(log n)
for log n≥1, the target D ≥ c*·K⁻¹√(log n_k)/(1+log K) follows for all
large k **if** one has a uniform envelope
  sup_{X:2-UC const≤K} γ(G_k,X) ≤ C·K²(1+log K)²·log n_k   (†)
with explicit C. Mendel–Naor supply only per-X finiteness sup_k γ<∞ with
X-dependent inexplicit constants — no (†). R1 itself is textbook, not original.
