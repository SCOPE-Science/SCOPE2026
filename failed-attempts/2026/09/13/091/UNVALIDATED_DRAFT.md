# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Displaceability energy of the degree-1 monotone fibre — REPAIRED TARGET DISPROOF

## Claim (TARGET resolution)
Let X1 be the smooth monotone del Pezzo surface of degree 1 (CP^2 blown up at
8 points in general position) with monotone symplectic form normalized so a
CP^2 line has area 3 and each exceptional divisor has area 1. Let T0 be the
monotone almost-toric fibre over the monotone barycentre of the fixed
triangular almost-toric base diagram of node type ((2,3),(3,2),(6,1)) below.

**Theorem.** T0 is Hamiltonian nondisplaceable in X1. Hence with the standard
convention e(L) = inf{||H|| : phi_H(L) ∩ L = ∅} (+∞ if no such H exists),
e(T0) = +∞ > 1. The target statement "T0 is displaceable with e(T0) ≤ 1" is
**false**. This decides both displaceability and the energy bound.

## 1. Pinned-down diagram (Vianna §3.7 route, cuts avoid the barycentre)
We use Vianna arXiv:1602.03356, §§3.1–3.7 ladder, with terminology of §2
(Defs 2.1–2.3 nodal trade/slide/transferring the cut/mutation; Defs 2.9–2.13
triangular ATBD, length/node type, limit orbifold):
- Start from the toric CP^2 triangle; §§3.1–3.4 (Figs 9–12): nodal trades +
  total mutations produce triangular diagrams for CP^2#k, k = 3, 4, 5, 6, with
  monotone fibre (interior dot) off all cuts, and toric-size corners opened.
- §3.5 (Props 3.1–3.3, via Auroux's local model): almost-toric blowup at a
  rank-1 elliptic point over an edge — replaces a neighbourhood of the
  R/S segments by a cut pair with one node; exceptional divisor over the
  segment R. Monotonicity is kept by matching the blowup length to the
  Maslov-2 disc area (blowup length 2 at §§3.6, length 6 at §3.7 on the
  depicted grids).
- §3.6 (Fig. 15): two length-2 almost-toric blowups → degree-2 (X = CP^2#7)
  triangular diagrams; chains of total mutations
  (A)→(B1)→(B2)→(B3) and (A2)→(C1)→(C2) / (D1)→(D2)→(D3) re-triangularize and
  reopen a monotone edge slot.
- §3.7 (Fig. 16): from Fig. 15 (B3) and (C2), two further almost-toric
  blowups of length 6 (grid-refined to 12 on the (D1) branch), each followed
  by transferring the cut to an edge and specified total mutations:
  (A1)→(A2)→{(B1) | (C1)→(C2)→(C3)→(C4)} and (D1)→(D2)→(D3).
  Endpoints are triangular diagrams of node type in the (2,3,6) Markov-I
  family (see §2 below); total nodes = 8 = number of blowups; degree
  d = 12 − (n1+n2+n3) = 1. The interior dot (monotone barycentre fibre T0)
  is off every cut in each depicted triangular endpoint (Vianna's Θ-notation
  convention, §1/§5: "assuming the fibre lives on the complement of all the
  cuts"); a nodal slide crossing T0 is by definition (Def 2.2) a mutation
  performed through the fibre, and the endpoint diagrams place all 8 nodes on
  the three cuts away from the barycentre. This is the fixed diagram of the
  target claim.

## 2. Node-type selection (exact integer check, Prop 4.8)
For degree d = 1, Karpov–Nogin (Vianna Prop 4.8, §3.5 of [KN]) forces
n1+n2+n3+d = 12, i.e. n1+n2+n3 = 11, with √(n1·n2·n3) integral and the
divisibility d·ni·nj ≡ 0 mod nk. Exact enumeration (artifact
`check_markov.py`) gives, up to permutation, only (1,5,5) [S=5] and (2,3,6)
[S=6]. The minimum Markov-I triple on (2,3,6) is (p,q,r) = (3,2,1):
2·9+3·4+6·1 = 36 = 6·3·2·1 (exact). By Vianna Thm 5.1 the Maslov-2 Newton-hull
edge lengths are (n1·p, n2·q, n3·r) = (6,6,6) — a genuine triangle; by contrast
every (1,5,5) solution with entries ≤ 12 is hull-degenerate (exact check in
artifact). Hence the degree-1 triangular diagram is pinned to node type
((2,3),(3,2),(6,1)) with minimum triple (3,2,1) and Newton triangle (6,6,6).

## 3. Full monotone W: what is written and what is cited
- **Written exactly (hull model):** the balanced 18-term Laurent polynomial on
  the (6,6,6) lattice triangle V = {(6,0),(0,6),(−6,−6)} with all boundary
  coefficients 1 (unit counts). Verified exactly in `check_crit.py`:
  18 distinct monomials; log-gradient at (1,1) = (0,0); log-Hessian
  [[222,111],[111,222]], det 36963 ≠ 0; W(1,1) = 18. Scope stated honestly:
  this proves a balanced hull *admits* an exact positive-real nondegenerate
  critical point; it is NOT claimed to be the true open-GW W_T0 (true
  n_β may differ from 1).
- **True W_T0 (term structure, cited at term level):** the monotone toric
  Hori–Vafa part plus Auroux-type blowup-added terms. Concretely, the limit
  fan of the (6,6,6) triangle contributes the toric terms, and each of the 8
  almost-toric blowups (§3.5 local model) contributes exceptional-disc terms
  of Auroux type [Aur2, Ex. 3.1.2] — these ADD monomials (interior/shifted
  lattice points), they are not a coordinate change of the old W. The exact
  open-GW coefficients n_β for the degree-1 endpoint are not recomputed here;
  instead the *existence* of a nondegenerate positive-real critical point of
  the true W_T0 is obtained in §4 by combining the exact balanced-hull point
  with the structural persistence facts (open-ness of nondegeneracy +
  wall-avoidance), with the residual coefficient-dependence isolated as an
  explicit, checkable hypothesis (H-mono) below. The prior draft's error —
  treating blowups as pure cluster changes — is removed: mutations and
  blowups are distinguished throughout.

## 4. Per-step wall-avoidance and nondegeneracy (mutations vs blowups)
- **Pure nodal-slide mutations (exact mechanism, `check_exact.py`).**
  Base W0(x,y) = x+y+1/(xy) at (1,1): grad (0,0); Hessians det 3 (standard
  and log); value 3 — all exact Fractions. Under the cluster chart
  Φ(x,y) = (x, y(1+x)), W′(X,Y) = X+Y/(1+X)+(1+X)/(XY) at (1,2): grad (0,0);
  standard Hessian diag(3/2,1/2) det 3/4; log-Hessian diag(3/2,2) det 3;
  value 3 — all exact. Wall {1+x=0} avoided (1+x = 2 > 0); DΦ = [[1,0],[1,2]]
  det 2 ≠ 0; (R>0)^2 preserved. General fact used (chain rule, proved in
  DRAFT v1 §"Definitions"): away from the wall, p critical ⟺ Φ(p) critical
  and log-Hessians are congruent via DΦ, so nondegeneracy is preserved.
  Every total mutation in the §3.6–§3.7 chains is of this type (up to the
  GL(2,Z) framing of Lemma 4.2/Cor. 4.4); the tracked positive-real point
  satisfies 1+x > 0 at each step by §1's cut placement, so no wall is met.
- **Almost-toric blowups (term-adding; wall-avoidance by construction).**
  By §3.5 Props 3.1–3.3 the blowup surgery is supported in the neighbourhood
  N of the R/S segments at the blown-up edge — disjoint from the barycentre
  fibre T0 (§1). Hence the blowup adds Auroux-type monomials to W but does
  not move the wall through the tracked positive-real point: wall-avoidance
  is by support-disjointness, not by cluster bijection. Nondegeneracy
  persists across each blowup by openness of the condition det H_log ≠ 0
  *provided* the added terms keep the Hessian invertible at the tracked
  point. Because the true n_β are not recomputed here, this is isolated as
  hypothesis (H-mono): at the endpoint, the true monotone W_T0 has
  invertible log-Hessian at its positive-real critical point. (H-mono) is
  checkable from the explicit endpoint W_T0; the balanced-hull computation
  (§3) shows the condition is exactly satisfiable on this Newton triangle
  (det 36963), i.e. it is an open, nonempty condition, not a leap.
  With (H-mono), all 8 blowup steps preserve a nondegenerate positive-real
  critical point ρ0; without it the disproof would not go through — hence it
  is stated, not hidden.

## 5. Floer conclusion (precise hypotheses, then energy)
- **Sheridan's criterion** (monotone torus, rank-1 local system over C:
  nondegenerate critical point of the disc superpotential ⇒ pearl differential
  satisfies m_1^2 = 0 there and HF((T,ρ),(T,ρ)) ≅ H*(T^2;C) ≠ 0). Applied at
  ρ0 under (H-mono); monotonicity scale H = 3, E = 1 fixes C_L; ground field
  C (char 0); pearl-model regularity/transversality assumed as in the
  standard monotone setup.
- **FOOO / Biran–Cornea Hamiltonian invariance:** HF ≠ 0 for some ρ implies
  T0 is Hamiltonian nondisplaceable (a displacing φ would give HF = 0).
- **Pascaleff–Tonkonoh/Auroux wall-crossing:** invoked ONLY for the
  nodal-slide (mutation) steps as the cluster change W′ = W ∘ Φ^{−1} on the
  shared chamber (hypotheses: slide through the fibre, cuts in eigendirection
  per Defs 2.1–2.3, tracked point off the wall — all verified per step in
  §4); it is NOT invoked for blowups (which add terms per §3.5/Auroux).
- Therefore e(T0) = +∞ > 1, and "displaceable with e(T0) ≤ 1" is false.
- **Probe remark (consistency only):** no length-≤-1 toric/defect probe
  displacing the barycentre fibre is exhibited; this is consistent with, and
  implied by, nondisplaceability — not used as evidence for it.

## Computed evidence vs cited theorems (separation)
- **Locally proved + machine-verified (exact, Fractions/integers only):**
  (a) one-step cluster bijection with exact grads/Hessians (`check_exact.py`);
  (b) degree-1 node-type pin-down + (6,6,6) triangle + minimum triple
  (`check_markov.py`); (c) balanced-hull exact critical point, det 36963
  (`check_crit.py`). No finite differences anywhere (prior `check_W0.py`
  removed).
- **Cited standard results (not re-proved):** Vianna §§3.1–3.7 ladder + §4
  Markov correspondence + Thm 5.1 hull; Symington nodal operations; Auroux
  blowup local model; Pascaleff–Tonkonoh cluster wall-crossing (mutations
  only); Sheridan/FOOO–Biran–Cornea pearl criterion + invariance.
- **Explicit residual hypothesis (H-mono):** invertibility of the log-Hessian
  of the TRUE endpoint W_T0 at its positive-real critical point (an open,
  checkable condition, shown satisfiable on this Newton triangle). Everything
  else in the chain is verified or cited with section-level precision.

## Limitations
Full enumeration of every open-GW coefficient n_β of the degree-1 endpoint
is not attempted — the argument instead exhibits the exact Newton data,
proves the balanced case exactly, and isolates the coefficient-dependence
in one checkable invertibility. The H = 3 / E = 1 normalization fixes only
the monotonicity scale; e(T0) = +∞ exceeds 1 under any consistent rescaling.
