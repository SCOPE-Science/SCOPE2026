# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# LERF status of G4 = ⟨a,b,c | u⁴⟩, u = ab²a⁻¹b⁻³c — PROOF that G4 IS LERF

## 1. Answer

**Yes.** G4 is subgroup separable (LERF): every finitely generated H ≤ G4
is closed in the profinite topology, i.e. an intersection of finite-index
subgroups. The proof is a Tietze collapse plus virtual freeness.

## 2. The relator and the Tietze collapse

Let F = F(a,b,c), u = a b² a⁻¹ b⁻³ c (reduced word of length 8:
a,b,b,a⁻¹,b⁻¹,b⁻¹,b⁻¹,c), and G4 = ⟨a,b,c | u⁴ = 1⟩.
Facts checked in `artifacts/verify_g4.py`:
u is cyclically reduced, involves all of a,b,c, and is not a proper power
(c occurs exactly once).

Put t = b³ab⁻²a⁻¹ ∈ F(a,b). Then t⁻¹ = ab²a⁻¹b⁻³, so

    u = t⁻¹ c.                                                      (1)

**Lemma (Tietze).** G4 ≅ ⟨a,b,w | w⁴ = 1⟩ ≅ F(a,b) ∗ C4,
via c = t w (equivalently w = t⁻¹c = u).

*Proof.* Start from ⟨a,b,c | u⁴⟩. Add a new generator w with defining
relator w = t⁻¹c. Modulo this relator, u = w by (1), so u⁴ = w⁴; replace
the relator u⁴ by w⁴ (a consequence modulo the new relator, and vice
versa). The relator w = t⁻¹c expresses c = tw with c occurring once, so
delete generator c, substituting c = tw everywhere. Remaining:
⟨a,b,w | w⁴⟩. Explicit mutually inverse homomorphisms:

    φ: ⟨a,b,c|u⁴⟩ → ⟨a,b,w|w⁴⟩, a↦a, b↦b, c↦tw;
    ψ: ⟨a,b,w|w⁴⟩ → ⟨a,b,c|u⁴⟩, a↦a, b↦b, w↦t⁻¹c.

φ(u) = t⁻¹tw = w, so φ(u⁴) = w⁴ = 1 (φ well defined);
ψ(w) = t⁻¹c = u, so ψ(w⁴) = u⁴ = 1 (ψ well defined);
φψ = id (φ(t⁻¹c) = t⁻¹tw = w) and ψφ = id (ψ(tw) = tt⁻¹c = c).
All word identities verified by free reduction in the artifact script. ∎

Henceforth identify G4 = F(a,b) ∗ ⟨w | w⁴⟩. Write G = G4, F2 = F(a,b).

**Corollary (torsion).** u (i.e. w) has exact order 4. Indeed w⁴ = 1 gives
order | 4, and the retraction π: G → C4 = ⟨z|z⁴⟩, a↦1, b↦1, w↦z, sends
w ↦ z of order 4 (equivalently π(u) = z on the original presentation:
a,b ↦ 1, c ↦ z gives u ↦ z since u contains c once and a,b cancel).
So the order is exactly 4, as the topic states.

## 3. The Magnus subgroup ⟨b,c⟩ is free of rank 2

Under φ, ⟨b,c⟩ maps to ⟨b, tw⟩ ≤ F2 ∗ C4. The retraction
ρ: F2 ∗ C4 → F2 killing w (a↦a, b↦b, w↦1) sends ⟨b,tw⟩ onto ⟨b,t⟩ ≤ F2.
If W(b,tw) = 1 in G then W(b,t) = 1 in F2, so freeness of ⟨b,t⟩ implies
freeness of ⟨b,tw⟩ (hence of ⟨b,c⟩, φ being an isomorphism).

**Lemma.** ⟨b,t⟩ ≤ F(a,b), t = b³ab⁻²a⁻¹, is free of rank 2.

*Proof.* Write B = b, T = t = b³ab⁻²a⁻¹, T⁻¹ = ab²a⁻¹b⁻³.
Let W be a nontrivial reduced word over {B±¹, T±¹}, in the form
W = Bⁿ⁰ T^e¹ Bⁿ¹ ⋯ T^ek Bⁿk with k ≥ 1, ei = ±1, interior ni ≠ 0
(if k = 0, W = Bⁿ⁰ ≠ 1 unless trivial). Expand each T^ei as an explicit
word and concatenate. Adjacent-block boundaries:
BⁿT joins b-runs (bⁿb³), TBⁿ, BⁿT⁻¹, T⁻¹Bⁿ (b⁻³bⁿ) likewise;
TT meets as a⁻¹b³ and T⁻¹T⁻¹ as b⁻³a (no cancellation, distinct letters);
T T⁻¹ and T⁻¹T are whole-word inverse pairs (= 1), excluded by reducedness
except with nonzero B-block between. Each T±¹ carries exactly two
a-letters. At a junction T±¹BⁿT±¹ the joined b-run can vanish for at most
one exponent (n = −3 for TT, n = 3 for T⁻¹T⁻¹, n = 0 excluded for
T B⁰T⁻¹ = inverse pair, etc.), and then at most one a-pair
(a⁻¹a or aa⁻¹) cancels; e.g.
T B⁻³T = b³ab⁻⁴a⁻¹ ≠ 1, T⁻¹B³T⁻¹ = ab⁴a⁻¹b⁻³ ≠ 1,
T BⁿT⁻¹ = b³ab⁻²(a⁻¹bⁿa)b²a⁻¹b⁻³ ≠ 1 (n ≠ 0),
T⁻¹BⁿT = ab²(a⁻¹bⁿa)b⁻²a⁻¹... ≠ 1 (n ≠ 0).
So starting from 2k a-letters, each of the (k−1) interior junctions kills
at most 2, leaving ≥ 2 a-letters surviving; W reduces to a nontrivial word
containing a. Hence no nontrivial reduced W is trivial: ⟨B,T⟩ ≅ F2. ∎

Thus ⟨b,tw⟩ ≅ F2 (ρ restricts to an isomorphism onto ⟨b,t⟩ on the level
of word calculus: any relation among (b,tw) pushes to one among (b,t)),
of rank exactly 2 (b ≠ 1 and [b,tw] ≠ 1; the four commutator normal forms
[c1]–[c4] in the artifact are nontrivial and distinct). Transporting back
along φ⁻¹, ⟨b,c⟩ ≤ G4 is free of rank 2, confirming the admitted
hypothesis (Freiheitssatz instance) by an elementary argument.

## 4. G is virtually free

Let π: G = F2 ∗ C4 → C4, a ↦ 1, b ↦ 1, w ↦ z, and N = ker π.
π is surjective, so N ⊲ G, [G:N] = 4.
N is torsion-free: finite-order elements of F2 ∗ C4 are conjugates of
w^k; π sends gw^kg⁻¹ to z^k (abelian target), nontrivial for 4 ∤ k, so N
contains none. By the Kurosh subgroup theorem N is free; by Schreier
(finite index in finitely generated G) N is finitely generated
(in fact rank 8: χ(G) = (1−2) + 1/4 − ... = −7/4, χ(N) = 4χ(G) = −7,
rk = 1 − χ = 8; not needed). So G is virtually free (finite normal
extension of a f.g. free group).

## 5. Virtually free implies LERF

Used classical facts (textbook; no new literature needed):
(Hall 1949) Free groups are LERF: every f.g. subgroup is a free factor of
a finite-index subgroup, hence profinite-closed.
(Schreier) Finite-index subgroups of f.g. groups are f.g.
(Kurosh) Torsion-free subgroups of a free product of free and finite
groups are free.

**Lemma (finite extension).** If N ⊲ G, [G:N] < ∞, and N is LERF, then G
is LERF.

*Proof.* Let H ≤ G be f.g. Then [H : H∩N] ≤ [G:N] < ∞, so H∩N is f.g.,
hence closed in N's profinite topology. Claim: a subset A ⊆ N closed in
N is closed in G. Indeed, N\A is a union of cosets x_jU_j with
U_j ⊲ N of finite index (basic profinite opens). Let
C_j = core_G(U_j) = ⋂_{g∈G} gU_jg⁻¹ ⊲ G; this is a finite intersection
([G:U_j] < ∞, finitely many conjugates), of finite index, with
C_j ≤ U_j. So each x_jU_j (x_j ∈ N) is a finite union of G-cosets
x_jsC_j, which are open in G's profinite topology. With
W = ⋃_{j,s} x_jsC_j G-open, N\A = W ∩ N, and N is G-clopen (a
finite-index subgroup is open, its complement a union of the other
cosets), G\A = (G\N) ∪ (W∩N) is G-open. So A is G-closed.
Apply to A = H∩N: it is G-closed. Left translation by h is a
G-profinite homeomorphism (h(xK) = (hx)K for K ⊲ G finite index), so each
h(H∩N) is G-closed. H is the finite union ⊔_{j=1}^k h_j(H∩N) with
k = [H:H∩N] ≤ [G:N] = 4. Finite unions of closed sets are closed. So H
is G-closed, i.e. an intersection of finite-index subgroups of G. Since
H was arbitrary f.g., G is LERF. ∎

## 6. Conclusion

G4 ≅ F(a,b) ∗ C4 is a finite (normal, index-4) extension of a finitely
generated free group, hence LERF by Hall's theorem and the Lemma. Every
finitely generated H ≤ G4 is an intersection of finite-index subgroups of
G4. This establishes horn 1 of the target: G4 **is** subgroup separable.
No explicit (H, g) separator exists, because none can.

## 7. Verification record

- `artifacts/verify_g4.py` (run: `python3 output/artifacts/verify_g4.py`,
  ALL CHECKS PASSED): |u| = 8, cyclically reduced, uses {a,b,c}, not a
  proper power; t·t⁻¹ = 1, φ(u) = w, ψ(w) = u, ψ(φ(c)) = c, φ(ψ(w)) = w
  as reduced words; retraction sends u ↦ z (order 4); the four
  ⟨b,tw⟩-commutator normal forms are nontrivial and pairwise distinct.
- The LERF deduction itself is the human-readable proof above (Sections
  2–5); the script checks only the combinatorial identities, which is all
  the computation the proof needs. Cited theorems (Hall, Kurosh,
  Schreier) are standard textbook results applied, not re-proved.
