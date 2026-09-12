# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Unique Cartan for the Bernoulli crossed product by G_{5/2}

## Claim (TARGET, affirmative)
Let G_{5/2} be the Popa–Shlyakhtenko strongly treeable ICC group of fixed
cost 5/2 with L(G_{5/2}) ≅ L(F_{5/2}), and let G_{5/2} ↷ (X,μ) be the
Bernoulli free ergodic pmp action. Then
M = L^∞(X) ⋊ G_{5/2} is a II_1 factor whose canonical Cartan subalgebra
L^∞(X) is unique up to unitary conjugacy. In particular there is no second
Cartan of M non-conjugate to L^∞(X); the disproof alternative is false.

## Objects and explicit model
- Popa–Shlyakhtenko groups (arXiv:1805.10707, Def 2.1): increasing finite
  Q_n, H_n = Q_n × F_{k_n}, G_{n+1} = G_n ∗_{Q_n} H_{n+1},
  G({Q_i},{k_i}) = ∪_n G_n.
- If Q = ∪Q_n is ICC, L(G) ≅ L(F_t) with t = 1 + Σ k_n/|Q_n|
  (Cor 2.8, Thm 2.9); every free pmp action is treeable of cost
  C(G) = 1 + Σ k_n/|Q_n| (Lemma 3.5, Cor 3.6); G is OE-free (Thm 3.7).
- Explicit t = 5/2 model: Q_n = S_n (so Q = S_∞ is ICC), k_0 = 1, k_2 = 1,
  else 0. Then t = 1 + 1/1! + 1/2! = 5/2, and cost = 5/2 (see
  artifacts/cost_check.py). The k_0 ≠ 0 case is covered by Remark 2.11(3°);
  ICC-ness and the isomorphism L(G_{5/2}) ≅ L(F_{5/2}) are as in Thm 1.1/2.9.
- Bernoulli action of an infinite group is free ergodic pmp; M is a II_1
  factor and A = L^∞(X) is a Cartan subalgebra.

## Proof by ME transfer of Popa–Vaes Cartan rigidity
1. G_{5/2} is measure equivalent (ME) to a free group. Indeed, by Cor 3.8(ii),
   groups G({Q},{k}) with finite Σ k_n/|Q_n| are pairwise ME; pick a finite-cost
   model of cost parameter 2 (e.g. Q_n = S_n, k_1 = 1 gives
   1 + 1/1 = 2). By OE-freeness (Thm 3.7), that model's actions realize every
   treeable ergodic relation of cost 2, hence are orbit equivalent to an
   F_2-action; so G_{5/2} is ME to F_2 (ME is transitive).
2. Cartan rigidity transfers across ME. Popa–Vaes (arXiv:1201.2824,
   Thms 1.1/1.3): weakly amenable nonamenable bi-exact groups (e.g. F_2) are
   C-rigid and Cs-rigid, and so is every group ME to them. Hence G_{5/2} is
   C-rigid: for EVERY free ergodic pmp action, L^∞(X) is the unique Cartan up
   to unitary conjugacy. This agrees with Prop 4.7(b) of Popa–Shlyakhtenko
   (G_t sofic and Cartan rigid via ME to free groups + PV Thm 11.3).
3. Apply to Bernoulli: M = L^∞(X) ⋊ G_{5/2} has unique Cartan L^∞(X).
   The mechanism is the Popa–Vaes treeable-cocycle/deformation-rigidity plus
   intertwining dichotomy (relative amenability vs. A ≺_M B ⋊ Σ), applied via
   the ME transfer — not group-factor solidity of L(G_{5/2}) ≅ L(F_{5/2}),
   which alone does not decide crossed-product Cartans.

## Why the negative alternative fails
Existence of a second non-conjugate Cartan would contradict C-rigidity of
G_{5/2} just established; hence the "disprove" branch (new non-uniqueness
witness for treeable-group measure-space factors) does not occur at cost 5/2.

## Scope notes / limitations
- Proves uniqueness for every free ergodic pmp action of G_{5/2}, hence the
  Bernoulli case; orbit-equivalence classification consequences beyond the
  target are not pursued.
- Uses published theorems (Popa–Shlyakhtenko 1805.10707; Popa–Vaes 1201.2824,
  1111.6951) as black boxes plus an explicit finite computation; no new
  deformation estimate is claimed.
- Self-checks: cost arithmetic verified by script; ICC hypothesis checked via
  S_∞ model; Bernoulli freeness/ergodicity standard for infinite groups.
