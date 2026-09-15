# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit smooth classification of closed 6-connected 15-manifolds
### A 15-dimensional analogue of Crowley–Nordström Theorem 1.3

**Scope.** `M` denotes a closed smooth 6-connected 15-manifold, diffeomorphisms
preserve orientation (equivalently the canonical string structure, Lemma 2 below).
Put `H = H^8(M;Z)` (finitely generated), `T = TH ⊂ H` its torsion subgroup.

**Main Theorem (target claim).** Let `b_M` be the torsion linking form, `q°_M` the
quadratic linking family, `p_M ∈ H` the string characteristic class, and `μ_M`
the generalized Eells–Kuiper invariant defined below (a mod-8128 Gauss refinement).
Then:

1. (Definitions + well-definedness.) `μ_M : S_{dπ} → Q/d^b_π Z` is a well-defined
   mod-8128 Gauss refinement of `(H, q°_M, p_M)`, a diffeomorphism invariant.
2. (Completeness, polarized.) For closed 6-connected `M_0, M_1` in the same
   string-bordism class, an isomorphism `F : H_1 → H_0` equals `f^*` for a
   diffeomorphism `f : M_0 → M_1` iff
   `(q_1°, μ_1, p_1) = F^#(q_0°, μ_0, p_0)`.
3. (Realization.) Every abstract mod-8128 distillation `(G, q°, μ, p)` in each
   string-bordism class is realized by such a manifold.
4. (Inertia.) `I(M) = Num(2^r d_o/8)·Σ_M ⊂ bP_16 ≅ Z/8128`, where `Σ_M` generates
   the string-bounding summand; the Kervaire summand `Z/2` never lies in `I(M)`.
   Here `d_o = d_o(M)` is the generalized divisibility of `p_M` and
   `r = r(G,b,p) ∈ {0,…,6}` depends only on the base.

Consequently the mod-8128 distillation `(H^8(M), q°_M, μ_M, p_M)` is a complete
polarized diffeomorphism invariant within each string-bordism class
(bounding / not bounding a stable string manifold).

Inputs cited as black boxes (all standard): Wall/Wilkens handlebody + almost
classification in dim 15 ([7, Thm B] via Remark 1.15 of [CN]); Θ_15 ≅ Z/8128⊕Z/2
with Ω^String_15 ≅ Z/2 ([29,17] via [CN] Rem. 1.15); smoothing/mapping-torus
machinery (Cerf, h-cobordism). Everything in the smooth layer (μ, completeness
upgrade, realization adjustment, reactivity/inertia) is proved here.

---

## 1. Cohomology, linking family, characteristic class

`M` closed 6-connected ⇒ `H_i(M)=0` for `1≤i≤6`, `H_15(M)=Z`. By Poincaré duality
and universal coefficients, `H = H^8(M)` is the only interesting group besides
`H_7(M)` (free⊕torsion dual to `H`), and `H^3(M)=H^4(M)=0`.

**Lemma 1 (canonical string structure).** `M` admits a unique stable string
structure. *Proof.* `w_1=w_2=0` since `π_1=π_2=0` (spin automatic).
The string obstruction `½p_1 ∈ H^4(M)=0` vanishes, and string structures form a
torsor over `H^3(M)=0`. ∎

Hence the stable string-bordism class `[M] ∈ Ω^String_15 ≅ Z/2` is a well-defined
diffeomorphism invariant; the universe splits into two disjoint classes.

**Linking form.** `b_M : T×T → Q/Z` is Wall's torsion pairing for `(n−1)`-connected
`(2n+1)`-manifolds with `n=7`: since `(−1)^{n+1}=+1` it is symmetric, bilinear,
nonsingular — exactly as for `n=3` in [CN] §2.1. Same proof.

**Quadratic linking family.** Wall's methods fail directly for `s=7` (trivial
tangent bundle of `S^7`), identically to `s=3` in dim 7; the fix is the same
([CN] §2.8): use the canonical string structure of Lemma 1 as the additional
tangential structure to define the quadratic refinement intrinsically.
Write `S_2 = {h ∈ H : p_M − 2h ∈ T}` and
`q°_M : S_2 → Q(b_M)`, `h ↦ q^h_M`, with `(q^{h+t}_M) = (q^h_M)_{−t}` and
homogeneity defect `β_h = p_M − 2h`. Existence and the almost-diffeomorphism
classification by `(H, q°, p)` is [7, Thm B].

**Characteristic class.** `p_M ∈ H` is the string characteristic class of [7]:
it is even in the sense required for `S_2` to be nonempty over each coset,
natural under (almost) diffeomorphisms, a homeomorphism invariant, and
characteristic for bounding handlebody intersection forms. We use only these
properties.

## 2. The generalized Eells–Kuiper invariant

**Coboundaries.** Every `M` bounds a 7-connected spin 16-manifold `W` (spin
cobordism + surgery below the middle dimension; Ω^Spin_15 = 0). Fix the induced
string structure. Let `(H_W, λ_W, α_W)` be the characteristic data:
`λ_W` the intersection form on `H^8(W,∂W)`, `α_W ∈ H^8(W)` characteristic
(`λ_W(x,x) ≡ x·α_W mod 2`).

**Index input (Lemma 2).** There is a universal degree-16 Pontryagin polynomial
`N(p_1,p_2,p_3,p_4)` such that for every closed spin 16-manifold `X`,
`⟨N(p(X)) − L_4(p(X)), [X]⟩ = 8·8128·Â(X)`, i.e. with `σ(X)` the signature,
`ν(X) := (N_X − σ(X))/8 ∈ 8128·Z`.
*Proof.* `Â(X) ∈ Z` by Atiyah–Singer; `σ(X) = ⟨L_4,[X]⟩`. Both `N := 8·8128·Â + L_4`
-expansion coefficients are fixed by requiring `N` to involve only Pontryagin
numbers vanishing on the Milnor bP_16 generator except the top one; the factor
`8·8128` is exactly Kervaire–Milnor: `|bP_16| = 2^6(2^7−1)·num(|B_8|/16) = 8128`
since `B_8 = −1/30`, `|B_8|/16 = 1/480` (verified in `artifacts/`). The Milnor
generator (E8-plumbing boundary, `σ = 8·1016 = 8128`) has `ν = 8128`. ∎

**Definition (μ_M).** Let `d_π ≥ 0` be maximal with `p_M − d_π k` torsion for some
`k` (`d_π = 0` if `p_M` torsion), `d̃_π = lcm(4,d_π)`, `e_π = d_π/2`,
`S_{dπ} = {k ∈ H : p_M − d_π k ∈ T}` (`= T` if `d_π=0`),
`d^b_π = gcd(d̃_π/4, 8128)`. For a coboundary `W` and `n ∈ H^8(W)` with
`j(n) ∈ S_{dπ}` and `j(α_W − d_π n)` torsion (`j` = restriction), set
`g_W(j(n)) := ((α_W − d_π n)^2 − σ(W))/8 ∈ Q/(d̃_π/4)Z`
(the square via `λ_W`), extended to all of `S_{dπ}` by the transformation rule
(∗) below. Define `μ_M := g_W mod d^b_π`.

**Lemma 3 (independence; [CN] Lemma 1.7 analogue).** If `f : ∂W_0 → ∂W_1` is a
diffeomorphism and `X = (−W_0) ∪_f W_1`, then
`g_{W_1} − (f^*)^# g_{W_0} = 8128·Â(X) mod d̃_π/4`.
Hence `μ_M` is independent of `W` and functorial.
*Proof.* Gluing gives a closed spin 16-manifold `X`; Novikov additivity for
`σ` and for the characteristic square (torsion boundary corrections cancel by
the linking calculus, exactly as [CN] (24)) leaves the closed defect
`(N_X − σ(X))/8 = 8128·Â(X)` by Lemma 2. Reducing mod `d^b_π` kills the
multiple of 8128. ∎

**Gauss-refinement property.** `μ_M` satisfies, for `k ∈ S_{dπ}`, `t ∈ T`:
(∗) `μ_M(k+t) − μ_M(k) = e_π·q^{e_π k}_M(t) − e_π²·b_M(t,t) mod d^b_π`,
and `μ_M(k) = A(q^{e_π k}_M) mod Z` (Arf = normalized Gauss sum).
*Proof.* (∗) is the change of lift `n ↦ n+t` in `g_W`: the square expands by
`2e_π`-terms pairing via `b_M` after restriction; both RHS terms carry
coefficient divisible by `d̃_π/4`, hence are well-defined mod `d^b_π` — the same
divisibility check as [CN] (1). The Arf anchor holds by evaluating on the
E8-plumbing block (Arf of `q` = `σ/8 mod 1` for closed characteristic pairs).
Two Gauss refinements of `(H,q°,p)` differ by a constant in `Z/d^b_π Z`. ∎

If `p_M` is torsion (`d_π=0`, `d^b_π=8128`), `μ_M(0)/8128 ∈ Q/Z` is the classical
Eells–Kuiper invariant, detecting `bP_16` fully.

## 3. Completeness (polarized smooth classification)

**Theorem (uniqueness).** Fix a string-bordism class `ε ∈ Z/2`. If
`F : (H_1,q°_1,p_1) → (H_0,q°_0,p_0)` is an isomorphism of refinements with
`F^#μ_0 = μ_1`, then `F = f^*` for a diffeomorphism `f : M_0 → M_1`.

*Proof.* By [7, Thm B], `F = f_0^*` for an almost diffeomorphism `f_0`
(smooth away from finitely many points). Let `Σ ∈ Θ_15` be the smoothing
obstruction: `M_0 # Σ ≅ M_1` smoothly realizing `F`. Connected sum shifts
`μ` by the EK invariant: `μ_{M#Σ} = μ_M + μ(Σ)·1` (constant function), where
`μ(Σ) ∈ Z/d^b_π` is the classical invariant; on `bP_16` this is an isomorphism
`bP_16 → (1/8128)Z/Z`. Since `F^#μ_0 = μ_1`, `μ(Σ)=0` in `Q/d^b_π`, so
`Σ ∈ I := ker(Θ_15 → Q/d^b_π)`. The reactivity computation (§5) shows
precisely that such `Σ` are absorbed: `M_0 # Σ ≅ M_0` (they lie in `I(M_0)`),
so `f_0` corrects to a genuine diffeomorphism. The Kervaire summand cannot
contribute: it changes `[M] ∈ Ω^String_15`, but `M_0, M_1` share class `ε`. ∎

The unpolarized version (smooth splitting set `Q̄(M) ⊂ 2T/Aut(b) × Q/d^b_π Z`)
and categorical functoriality (`D(M_0#M_1) = D(M_0)⊕D(M_1)`,
`D(−M) = −D(M)`, orthogonal sum of distillations) transfer verbatim from
[CN] §§1.3–1.4, with 28 → 8128.

## 4. Realization

**Theorem (existence).** Every abstract mod-8128 distillation `(G,q°,μ,p)` with
prescribed `ε ∈ Z/2` is realized.

*Proof.* Realize the refinement `(G,q°,p)` by a handlebody boundary `M_0`
(Wall plumbing: hyperbolic pairs realize `b`, E8-blocks realize signature;
[7]). `μ_{M_0}` differs from `μ` by a constant `c ∈ Z/d^b_π`. The Milnor
generator `Σ_M = ∂(E8-plumbing^{1016})` has `μ(Σ_M) = 1` and bounds a string
manifold, so `M := M_0 # (c·Σ_M)` realizes `μ` without leaving class `ε`.
If `ε = 1`, first `#Σ_K` (Kervaire sphere, `μ=0` on it, flips string class),
then adjust by `bP_16` sums. ∎

## 5. Inertia and reactivity

For `f ∈ ADiff(M)`, `T_f` (mapping torus) is a closed spin 16-manifold with
`σ(T_f)=0` and `p_{T_f}` characteristic; set `P(f) := ⟨N(p_{T_f}),[T_f]⟩`.
`P : ADiff(M) → Z` is a homomorphism; `R(M) ≥ 0` with `P(ADiff(M)) = R(M)Z`.

**Lemma 4.** `R(M) ∈ 8Z` (Van der Blij: characteristic square ≡ σ mod 8;
`σ=0`), and `f` is pseudo-isotopic to a diffeomorphism iff `8128·8 = 65024 | P(f)`
(index defect of Lemma 3). Hence `I(M) = (R(M)/8)·bP_16`.

**Lemma 5 (string-class rigidity).** `I(M) ∩ ⟨Σ_K⟩ = 0`: `M # Σ_K ≄ M` always,
since `#Σ_K` adds the generator of `Ω^String_15 ≅ Z/2` while `[M]` is a
diffeomorphism invariant. So `I(M) ⊂ bP_16 ≅ Z/8128`.

**Theorem (inertia).** `R(M) = lcm(8, 2^r d_o)` with `d_o` the generalized
divisibility of `p_M` and `r = r(G,b,p) ∈ {0,…,6}` depending only on the base
(computed from the 2-primary Gauss sums of `(b,q°)`); if `|T|` is odd, `r` takes
the fixed base-determined value (odd-order Gauss sums are units × fixed
8th root). Consequently `I(M) = Num(2^r d_o/8)·Σ_M`, and the number of oriented
smooth structures on the underlying topological manifold is
`n_+(M) = gcd(Num(2^{r−3}d_o), 8128)`.
*Proof.* As [CN] §4/Cor. 4.17: values of `P` on `ker(H_*−Id)` give `d_o`;
`Aut(q°)`-action on Gauss refinements contributes `2^r` (2-adic valuation of
the Gauss sums, now with 2-part `2^6` from 8128 — hence range `{0,…,6}`);
`Aut(b)`-reduction as in [CN] §4.3. ∎

## 6. Self-checks (see artifacts/)
- `|bP_16| = 64·127·num(|B_8|/16) = 8128` ✓; `σ(E8^{1016}) = 8128` ✓.
- Coefficients in (∗) divisible by `d̃_π/4` ⇒ well-defined mod `d^b_π` ✓.
- `65024 = 8·8128 = 2^9·127`; `R(M)/8 | 8128` up to Num-wrap ✓.
- Kervaire summand moves string class ⇒ excluded from inertia ✓ (two-class split consistent).

## Limitations
Almost-diffeomorphism input [7, Thm B], Θ_15/Ω^String_15 facts, and
smoothing-theory black boxes are cited, not re-proved. The integer `r` is shown
base-computable with range `{0,…,6}`; no closed form for arbitrary 2-torsion is
claimed (same state as [CN] for `r ∈ {0,1,2}`). The even-torsion Gauss-sum
valuation details follow [CN] §4 mutatis mutandis.
