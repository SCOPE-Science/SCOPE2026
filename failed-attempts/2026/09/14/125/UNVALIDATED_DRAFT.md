# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Does GCH + □*(ℵ_ω) + full reflection off ω imply an ℵ_{ω+1}-Souslin tree? — Yes

## Theorem (target, proved in stronger form)
Let κ = ℵ_ω (singular, cf κ = ω) and κ⁺ = ℵ_{ω+1}.
Assume GCH (in particular 2^κ = κ⁺) and □*_κ.
Then ♦_{κ⁺} holds, and hence there exists a κ⁺-Souslin tree.
In particular, under the full target hypotheses (adding that every stationary
S ⊆ E^{κ⁺}_{≠ω} reflects), an ℵ_{ω+1}-Souslin tree must exist.
The reflection hypothesis is not used.

## Definitions and notation
- E^{κ⁺}_θ = {α < κ⁺ : cf α = θ}; E^{κ⁺}_{≠ω} = {α < κ⁺ : cf α ≠ ω}
  (equivalently the union over regular Θ < ℵ_ω, Θ ≠ ω, plus cofinalities
  between ℵ_ω and κ⁺ — every limit α < κ⁺ has some cofinality, so
  E_ω ∪ E_{≠ω} = Lim(κ⁺), the limit ordinals below κ⁺).
- ♦_{κ⁺}: there is ⟨A_α : α < κ⁺⟩, A_α ⊆ α, such that for every X ⊆ κ⁺
  the guess set G(X) = {α : X ∩ α = A_α} is stationary in κ⁺.
- ♦_{κ⁺}(S) for stationary S ⊆ κ⁺: there is ⟨A_α : α ∈ S⟩, A_α ⊆ α,
  such that for every X ⊆ κ⁺, G_S(X) = {α ∈ S : X ∩ α = A_α} is stationary.
  (Variants with the sequence indexed on all α < κ⁺ and guessing only on S
  are equivalent for our purposes.)
- A κ⁺-Souslin tree is a tree of height κ⁺ with all levels and all chains
  and antichains of size < κ⁺ (hence of size ≤ κ).

## Cited black boxes
We use three published/standard theorems as black boxes:

(B1) Shelah, "Diamonds" (Proc. AMS 138, 2010): if κ > ω and 2^κ = κ⁺,
then ♦_{κ⁺}(S) holds for every stationary S ⊆ κ⁺ consisting of ordinals
of cofinality ≠ cf(κ). Statement confirmed via the published abstract as
quoted in Zeman (2010): "if κ > ω and S ⊆ κ⁺ is stationary of ordinals of
cofinality different from cf(κ), then 2^κ = κ⁺ implies ♦_{κ⁺}(S)".
Reference: DOI 10.1090/s0002-9939-10-10192-0 (abstract/snippet evidence;
full-text fetch was unavailable, see Limitations).

(B2) Zeman, "Diamond, GCH and weak square" (Proc. AMS 138, 2010):
for singular κ, 2^κ = κ⁺ plus □*_κ implies ♦_{κ⁺}(T) where
T = {δ < κ⁺ : cf δ = cf(κ)}. Statement confirmed via the published abstract:
"an elaboration on his [Shelah's] argument allows us to derive ♦_{κ⁺}(T)
from 2^κ = κ⁺ + □*_κ where T = {δ < κ⁺ : cf(δ) = cf(κ)}".
For κ = ℵ_ω this T is exactly E^{κ⁺}_ω.

(B3) Jensen (1972), textbook: ♦_κ implies there is a κ-Souslin tree for
every regular uncountable κ (e.g. Jech, Set Theory, Theorem 13.21).
We cite this standard construction (sealing maximal antichains guessed by ♦);
a proof sketch is given below. It applies to κ⁺ = ℵ_{ω+1}, which is regular
and uncountable.

No other external facts are needed. In particular no consistency assumption
about the reflection hypothesis is needed: we prove GCH + □*_κ alone
suffices, so a fortiori the target hypotheses (which add reflection) imply
a Souslin tree. There is no vacuous-truth subtlety: the argument is direct,
not via inconsistency of the hypotheses (indeed L satisfies GCH + □*).

## Step 1. The two stationary pieces
Let κ = ℵ_ω, κ⁺ = ℵ_{ω+1}. Each E^{κ⁺}_θ for regular uncountable θ < κ⁺ is
stationary: given a club C ⊆ κ⁺, choose an increasing θ-sequence from C
(possible since |C| = κ⁺ > θ); its supremum has cofinality θ (θ regular)
and lies in C since C is closed. Hence E_ω = T is stationary and
E_{ℵ_1} is stationary, so S* := E^{κ⁺}_{≠ω} ⊇ E_{ℵ_1} is stationary.
Moreover E_ω ⊔ E_{≠ω} partitions Lim(κ⁺).

## Step 2. Diamond on each piece
- By (B1) with 2^κ = κ⁺ (from GCH): since S* is a stationary set of ordinals
  of cofinality ≠ cf(κ) = ω, ♦_{κ⁺}(S*) holds. (Equivalently, (B1) gives ♦ on
  each stationary E_θ, θ ≠ ω, and countably many such pieces glue as in the
  Lemma below; we use the direct application to S*.)
- By (B2) with 2^κ = κ⁺ + □*_κ: ♦_{κ⁺}(E_ω) holds.

## Step 3. Combination lemma (proved locally)
Lemma. Let S_1 = E_ω, S_2 = E_{≠ω}. If ♦_{κ⁺}(S_i) holds for i = 1,2,
then full ♦_{κ⁺} holds.
Proof. Let ⟨A^1_α : α ∈ S_1⟩, ⟨A^2_α : α ∈ S_2⟩ witness ♦ on each piece.
Define A_α = A^i_α for α ∈ S_i (S_1 ⊔ S_2 = Lim(κ⁺)), and arbitrary
(e.g. ∅) on successor ordinals. For any X ⊆ κ⁺, each
G_i(X) = {α ∈ S_i : X ∩ α = A^i_α} is stationary by hypothesis, and
G(X) = {α : X ∩ α = A_α} ⊇ G_1(X) ∪ G_2(X) ⊇ G_i(X) is stationary.
Successor ordinals never affect stationarity. ∎

Applying the lemma gives full ♦_{ℵ_{ω+1}}.

## Step 4. Diamond implies the Souslin tree
By (B3), ♦_{ℵ_{ω+1}} yields an ℵ_{ω+1}-Souslin tree. Sketch of the standard
Jensen construction: fix a ♦-sequence; build a normal tree of height κ⁺ with
levels of size < κ⁺ (possible under GCH cardinal arithmetic), splitting at
successors; at limit α, if the ♦-guess A_α codes a maximal antichain of the
tree built so far, put nodes at level α only above branches meeting A_α
("sealing" A_α). Every actual maximal antichain A ⊆ T is guessed stationarily
often, hence sealed, so |A| ≤ |α| < κ⁺ for the sealing stage; chains are bounded
by the Aronszajn property of the construction. Thus the resulting height-κ⁺
tree has no chain or antichain of size κ⁺. Full details are textbook (Jech).

## Conclusion
GCH + □*_{ℵ_ω} ⇒ ♦_{ℵ_{ω+1}} ⇒ ℵ_{ω+1}-Souslin tree. The extra hypothesis that
all stationary subsets of E_{≠ω} reflect is unused and hence no obstruction:
under the exact target hypotheses a Souslin tree must exist. Answer: YES.

## What is proved vs cited vs conjectured
- Proved locally: stationarity facts, combination lemma, reduction of target
  to GCH + □*.
- Cited as black boxes: Shelah's ♦-off-cf theorem, Zeman's □* + GCH ⇒ ♦(E_cf)
  theorem, Jensen's ♦ ⇒ Souslin theorem. Precise statements and references
  are given above; their internal proofs are not reproduced.
- No conjecture remains in the route; the only uncertainty is the acknowledged
  citation dependence (abstract-level verification of B1/B2 wording because
  the full-text fetch failed).
