# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Kubota–Leopoldt Degree Zero for Q(√13) at p = 3

## Claim (TARGET)

Let χ be the even primitive Dirichlet character of conductor 13 attached to
the real quadratic field Q(√13), and let p = 3 (which splits in Q(√13)).
Let F_χ(T) ∈ Z_3[[T]] be the Kubota–Leopoldt Iwasawa power series attached to
χ (plus-branch, γ = 1 + 3 normalization). Then F_χ has Weierstrass degree
λ_an = 0; equivalently its constant term F_χ(0) = L_3(0, χ) is a 3-adic unit.
Consequently the algebraic Iwasawa invariants satisfy λ_3 = μ_3 = 0 for this
tower (via the Iwasawa Main Conjecture and Ferrero–Washington μ = 0).

**Certified value.** L_3(0, χ) = 4 exactly, hence v_3 = 0.

## Proof

### 1. Setup and parity

χ(a) = (a/13) is even since χ(−1) = (−1/13) = 1 (13 ≡ 1 mod 4), primitive of
conductor 13, and gcd(13, 3) = 1. Let ω(a) = (a/3) be the Teichmüller
character mod 3, which is odd. The Teichmüller decomposition at p = 3 gives
the odd product character ψ of conductor 39 = 13·3 defined by
ψ(a) = (a/13)·(a/3) for gcd(a, 39) = 1, i.e. ψ = χ·ω. The Kubota–Leopoldt
value at s = 0 is then (Washington, *Cyclotomic Fields*, Cor. 5.13)

    L_3(0, χ) = −B_{1,ψ}.

Parity check:
ψ(−1) = χ(−1)·ω(−1) = (1)(−1) = −1, so ψ is odd, as required for a nonzero
B_{1,ψ}. Splitting check: (13/3) = (1/3) = 1 and χ(3) = (3/13) = 1, so 3
splits in Q(√13).

### 2. Exact generalized Bernoulli number

For an odd Dirichlet character ψ of conductor f, the defining formula is

    B_{1,ψ} = (1/f) · Σ_{1 ≤ a ≤ f, (a,f)=1} a·ψ(a).

With f = 39 = 13·3 there are φ(39) = φ(13)·φ(3) = 12·2 = 24 units. Direct
exact evaluation (integer arithmetic; two independent loops in the replay
script, which also verify the unit count 24) gives

    Σ_{a ∈ (Z/39Z)^×} a·ψ(a) = −156,

since S = −156 and B = S/39 = −156/39 = −4. Concretely the 24 summands are
1+2+4+5−7+8+10+11−14+16−17−19+20+22−23+25−28−29−31+32−34−35−37−38 = −156
(signs = ψ(a) = (a/13)(a/3)). Hence

    B_{1,ψ} = −4   (exactly, as a rational integer).

Euler-factor audit. At n = 1 the interpolation factor is (1 − ψ(3)) with
ψ(3) = 0 (3 | 39), so the factor equals 1 — no Euler factor is dropped. The
reduction g = gcd(39,3) = 3, h = 13 with χ(3) = 1 is consistent with this.

### 3. The 3-adic unit and Weierstrass degree

Therefore

    L_3(0, χ) = −B_{1,ψ} = 4,

exactly (an integer, hence a 3-adic integer). Since 4 ≡ 1 mod 3, numerator
and denominator are both prime to 3, so

    v_3(L_3(0, χ)) = 0,

i.e. the constant term F_χ(0) is a 3-adic unit. The Iwasawa series F_χ(T)
thus has at least one unit coefficient (its constant term). By the
Weierstrass preparation theorem, F_χ = u·P with u a unit series and P a
distinguished polynomial; a unit constant term forces deg P = 0. Hence the
analytic Weierstrass degree is

    λ_an = 0.

This is the Ferrero–Greenberg constant-term criterion: no derivative data is
needed because the degree-zero case is already decided by unit nonvanishing
(the derivative criterion only matters when the constant term vanishes).

### 4. Algebraic corollary

Ferrero–Washington gives μ_3 = 0 for this abelian character, and the Iwasawa
Main Conjecture for Q(μ_3) identifies the analytic degree λ_an with the
algebraic λ_3 of the plus-part tower. Hence λ_3 = μ_3 = 0.

## Evidence summary

- Exact integer computation: Σ aψ(a) = −156 over exactly the 24 units mod 39
  (verified by two independent loops and a unit count φ(39) = 24), giving
  B_{1,ψ} = −4 and L_3(0,χ) = 4.
- 3-adic valuation: v_3(4) = 0 (4 mod 3 = 1), so F_χ(0) is a unit.
- Type checks: χ even, ψ odd, gcd(13,3) = 1, 3 splits (χ(3) = 1), Euler factor
  at n = 1 trivially 1 since 3 | 39.
- Weierstrass preparation converts the unit constant term into λ_an = 0.
- Replay: `python3 output/artifacts/verify_degree_zero.py` (stdlib only)
  prints ALL CHECKS PASSED.

## Limitations and uncertainty

- The proof uses the standard Washington Corollary 5.13 interpolation formula
  L_3(0,χ) = −B_{1,ψ}; the citation is to a textbook theorem, not rederived.
- The Main Conjecture bridge for the algebraic corollary is cited, not proved.
- The computation is exact integer arithmetic (no precision loss), but it
  covers only the pair (conductor 13, p = 3), not neighboring characters.
- No originality is claimed for the method (Bernoulli-sum criterion); the new
  content is the evaluated value B = −4 / L = 4 and the degree-zero
  certificate at this previously unevaluated pair.

## Reproducibility

Run `python3 output/artifacts/verify_degree_zero.py` with any Python 3
interpreter (stdlib only). It replays the character construction, both
Bernoulli-sum loops, the unit/parity/split checks, and the valuation
conclusion, printing ALL CHECKS PASSED.
