# Distal exponent target — reconstruction notes (untrusted Rug material distinguished from proofs)

## Definitions (Anderson §2; Chernikov–Galvin–Starchenko)
- Φ(x;y) finite set of formulas, |x|=d. B ⊂ M^{|y|} finite, |B|=n.
- π*_Φ(n) = max_{|B|=n} |S_Φ(B)| (dual shatter = # Φ-types).
- vc*(Φ) = limsup log π*_Φ(n)/log n (dual VC-density).
- Distal cell decomposition T: cells from fixed finite Ψ(x;y_1..y_k),
  validity filter θ_ψ; T(B) = {Δ∈Ψ(B) : B∩I(Δ)=∅}; cells cover M^d,
  none crossed by Φ(x;B).
- π_T(n) = max_{|B|=n}|T(B)|; exponent r: π_T(n)=O(n^r);
  distal density = inf_T limsup log π_T(n)/log n.
- Key inequalities: |T(B)| ≥ |S_Φ(B)| for every abstract T (Prop 2.7),
  so distal density ≥ vc*(Φ). With Φ={x=y}, densities ≥ d exist.

## Known upper bounds (Anderson Thm 3.1 + Thm 4.1; CGS)
- 1-dim (weakly o-minimal): exponent 1 with k=2 parameters
  (convex-components + downwards-closed atoms argument).
- Induction (Thm 3.1): if |x|=1 needs k params, and |x|=d0 has exponent r,
  then |x|=d≥d0 has exponent k(d−d0)+r. Proof: fiber T1 over x1 with
  parameters (x′,y_1..y_k), then base T_ψ over x′; count
  |B|^k tuples × O(|B|^{e(d−1)}) ⇒ e(d)=k+e(d−1).
- o-minimal expansion of group/field: d=2 optimal exponent 2 (CGS vertical
  decomposition, [5] Thm 4.1; proof uses definable choice, works over groups).
  Hence d0=2, r=2, k=2 ⇒ e(d)=2(d−2)+2=2d−2 for d≥2.
- Lower bound: vc* ≤ d (o-minimal, [26]) and examples attain d, so
  d ≤ t(d) ≤ 2d−2 for the uniform exponent; gap ∈ [d, 2d−2].

## Why the gap is hard (state of the art)
- CGS (cutting lemma paper): "generalized vertical decomposition gives
  optimal bound for M^2, but determining exact bounds in higher dimensions
  remains open, even in the semialgebraic case." So target = known open problem.
- Over R (ordered field, semialgebraic): DS-sequence refinement gives for
  d=3: |T(B)|=O(|B|^{3β(|B|)})=O(|B|^{3+ε}) ∀ε>0 (β = inverse-Ackermann type),
  hence distal *density* 3; for d=4: O(|B|^{4+ε}), density 4; induction then
  gives density ≤ 2d−4... wait Anderson text says density 3 if d=3 and
  2d−4 if d≥4 — check: e(4)=4 ⇒ e(d)=2(d−4)+4=2d−4. Yes.
  Crucially these are DENSITY bounds (infimum, ε-slop), NOT pure O(n^3) /
  O(n^{2d−3}) exponent bounds. Problem 2.12: attainment of infimum unknown.
- Target demands pure exponent: "admits T with |T(B)|=O(|B|^{t(d)})" with
  t(d)≤2d−3, i.e. for d=3 a single T with O(n^3). Known R-results do NOT give
  this (β factor unbounded). A fortiori unknown for arbitrary o-minimal
  expansions of RCF (exp, restricted analytic, ...), where DS hypotheses
  (bounded description complexity / uniform812y intersection multiplicity
  with effective β control) are not established.
- Lower-bound side: type counting caps at d (Prop 2.7 gives |T|≥|S| but
  |S|=O(n^d)), so witnessing 2d−2 needs a *definability-overhead* argument:
  for EVERY finite uniform Ψ,θ some B forces Ω(n^{2d−2}) valid cells or an
  invalid (crossed) cell. No such family is known; natural candidates
  (hyperplane arrangements) admit O(n^d) vertical decompositions (see
  computation below), so they do not separate.

## Reduction observation (trivial, not claimed original)
- By Thm 3.1 with k=2: pure e(3)≤3 ⟹ pure e(d)≤2d−3 ∀d≥3.
  Contrapositively, any proof of the target's "≤2d−3" clause must establish
  pure-O(n^3) base in dimension 3 for arbitrary o-minimal RCF expansions —
  strictly stronger than all published density-3 results. This is the blocker.
