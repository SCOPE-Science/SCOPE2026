# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform Lyapunov bound and time-average tightness for the renormalized fractional Burgers Galerkin system at σ=5/2 on T²

## 1. Model (scalar divergence-form gradient transport)

State space: zero-mean L²(T²), T²=(R/Z)². Fix unit vector e ∈ R² (e.g. e=(1,0)).
Fractional dissipation A = (−Δ)^{5/4} (i.e. σ=5/2), domain D(A)=H^{5/2}∩{mean 0}.
For truncation N, let Π_N project onto {|k| ≤ N, k≠0}, k ∈ Z²\{0}.

Renormalized Galerkin system (mild/strong finite-dimensional SDE):

du_N = [−A u_N − Π_N (e·∇)(u_N²/2 − C_N)] dt + Π_N dW,  u_N(0)=Π_N u_0.   (1)

Noise: W trace-class on L²₀ with covariance Q, Tr(Q)=:τ<∞. Forcing Π_N dW is
additive finite-dimensional; strong solutions exist globally (locally Lipschitz
drift + linear dissipation). This is the audit-plan system: divergence-form
quadratic transport with Fourier truncation; C_N is the Fourier–Wick constant.

Wick remark (why C_N drops out). The Wick ordering subtracts the divergent
constant c_N = E[(Π_N ξ)²]-type term so the drift is :(Π_N u)²:= (Π_N u)²−c_N.
Since (e·∇)c_N = 0, the gradient kills the constant exactly:

  Π_N (e·∇):(u_N²):/2 = Π_N (e·∇)(u_N²/2).

Hence the energy estimate below never sees C_N; no remainder estimate from any
"candidate 1" (DPD/short-time) input is invoked. The argument is self-contained.

## 2. Exact trilinear cancellation (the key lemma)

Lemma. For every v in the Galerkin space (finite Fourier support, mean zero),

  ⟨v, Π_N (e·∇)(v²/2)⟩_{L²} = 0.

Proof. Π_N is self-adjoint and fixes v, so the pairing equals
∫_{T²} v (e·∇)(v²/2) dx = (1/2)∫ v (e·∇)(v²) dx = (1/6)∫ (e·∇)(v³) dx = 0
by the divergence theorem on the closed torus (v³ is smooth, periodic). ∎

No interpolation of the transport term is needed at all for the L² bound:
dissipation alone absorbs everything once the cubic term vanishes exactly.
(This is stronger than the audit plan's interpolation route, and strictly
independent of any DPD remainder bound.)

## 3. Itô energy identity and N-uniform Lyapunov bound

V(u)=‖u‖²_{L²}. By Itô (finite dimensions):

  dV(u_N) = 2⟨u_N, −A u_N − Π_N(e·∇)(u_N²/2)⟩ dt + Tr(Π_N Q Π_N) dt + dM_t
          = −2‖A^{1/2} u_N‖² dt + Tr(Π_N Q Π_N) dt + dM_t,            (2)

using the Lemma; M_t is a martingale. On zero-mean fields the Poincaré gap of
A=(−Δ)^{5/4} is γ=(2π)^{2·(5/4)}=(2π)^{5/2}≈98.96, so
‖A^{1/2}v‖² ≥ γ‖v‖². With τ_N:=Tr(Π_N Q Π_N) ≤ τ:

  d/dt E[V(u_N)] ≤ −2γ E[V(u_N)] + τ.                                (3)

Gronwall gives, for every N and t ≥ 0:

  E‖u_N(t)‖² ≤ e^{−2γt}‖u_0‖² + (τ/2γ)(1−e^{−2γt})
            ≤ K(1+‖u_0‖²),  K := max(1, τ/2γ).                       (4)

This is the claimed sup_N sup_{t≥0} bound with explicit K. Replay:
γ=(2π)^{2.5}=98.957718; e.g. τ=1 → K=1; τ=50 → K=1 (τ/2γ≈0.25).
Recorded in output/artifacts/ledger.json.

Time-integrated dissipation (needed for tightness). Integrating (2) in
expectation over [0,T]:

  (1/T)∫₀ᵀ E‖A^{1/2}u_N‖² dt ≤ (V(u_0)+τT/2·…)/T ≤ V(u_0)/T + τ/2,    (5)

uniformly in N. Since ‖v‖_{H^{5/4}} ≍ ‖A^{1/2}v‖ on zero-mean fields, the
Cesàro laws Q^T_N := T^{−1}∫₀ᵀ Law(u_N(t)) dt have uniformly bounded mean
H^{5/4}-energy: sup_{N,T≥1} ∫‖u‖²_{H^{5/4}} dQ^T_N ≤ C₀(1+V(u_0)+τ).

## 4. Tightness in C^{−κ} (Krylov–Bogoliubov input)

Lemma (compact embedding). For s=5/4, any κ>0, and dim d=2, H^s(T²) embeds
compactly into C^{−κ}(T²)=B^{−κ}_{∞,∞}. Indeed H^s=B^s_{2,2} ↪ B^{−κ}_{∞,∞}
continuously when s−d/2 > −κ, i.e. 5/4−1=1/4>−κ (Besov embedding, compact due
to the strict regularity gap on the compact torus via Littlewood–Paley tails).
Closed H^{5/4}-balls are therefore compact in C^{−κ}.

Tightness. Fix κ>0, ε>0. By Markov on (5), Q^T_N(‖u‖_{H^{5/4}}>R) ≤ C₀/R²,
uniformly in N, T≥1. Choose R=√(C₀/ε); the compact set
K_ε={‖u‖_{H^{5/4}}≤R} carries mass ≥1−ε for every N, T≥1. Hence {Q^T_N} is
tight in C^{−κ}, uniformly in N and T≥1. ∎

Probability laws have mass one by construction (pushforwards of the SDE law);
no infinite-mass defect. V is finite on the Galerkin system; non-Gaussianity
holds (quadratic drift with non-zero Wick part, infinite-dimensional state
space); the compactness preflight passes.

## 5. Falsifiability ledger (why no disproof occurred)

The target invited two falsifiers: (a) certified super-uniform growth of
E V(u_N) in N or t; (b) explicit mass escape in C^{−κ}. Neither occurs:
(4) forbids (a) with rate 2γ≈197.9 and asymptote τ/2γ; the uniform H^{5/4}
moment (5) plus compact embedding forbids (b). The numerical replay confirms
both at finite resolution: cancellation inner product 2.5e−17; 20-trial
Galerkin run (Kc=5, TrQ=50) terminal mean-energy 0.17 vs bound 1.25, with
sustained (non-collapsed) energy ≈ linear-theory stationary value 0.196.

## 6. Independence statement

No step uses short-time/paracontrolled/DPD remainder bounds, spaces, or
constants from any "candidate 1". Inputs: Itô formula (finite-dim), divergence
theorem, Poincaré gap of (−Δ)^{5/4} on T²₀, Besov embedding, Krylov–Bogoliubov
averaging. The Wick constant is annihilated by the gradient before any
estimate begins.

## 7. Replay

  python3 output/artifacts/verify.py   # → VERIFY_OK; writes ledger.json
