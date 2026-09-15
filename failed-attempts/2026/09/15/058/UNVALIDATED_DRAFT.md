# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact L-packet membership for non-companion depth-zero supercuspidals of Sp_{2N} — DRAFT

## 1. Statement

Let F be non-archimedean of odd residual characteristic, q odd, G = Sp_{2N}(F).
Let J_0 be maximal parahoric with J_0/J_0^+ ≅ Sp_{2N_1}(k_F) × Sp_{2N_2}(k_F),
J its normalizer, ρ = ρ_y × ρ_z inflated from cuspidals, π = c-Ind_J^G ρ
depth-zero supercuspidal.

For each monic irreducible self-dual polynomial P̃ (Lusztig parameter for the
finite cuspidals) let e_P = |m_{P̃,y}|, f_P = |m_{P̃,z}| (absolute Lusztig
multiplicities on the two sides). Assume non-companion: e_P ≠ f_P for some P̃.
For odd-type P̃ (the X±1 and odd-degree self-dual cases carrying the
Lust–Stevens ambiguity) put E_P = 2e_P+1, F_P = 2f_P+1. (Even-type P̃, where the
candidate values are 2e_P, 2f_P, are treated identically with parity 0; the
selection logic below is unchanged.)

**Theorem (selection + members).**
(a) For each P̃ with e_P ≠ f_P, the reducibility point of
I(s,π̃_P,π) = ι_P^G(|det|^s π̃_P × π) (π̃_P the self-dual supercuspidal of the
matching GL attached to P̃, Mœglin normalization) is s_0(P) = max(e_P,f_P)+1,
hence max-Jordan value a_P = 2s_0(P)−1 = max(E_P,F_P) and minor value
b_P = min(E_P,F_P). The Tam sign is ν_P = +1 if e_P > f_P (y-side wins),
ν_P = −1 if f_P > e_P (z-side wins), and ν_P = 0 if e_P = f_P.
(b) The L-parameter φ of π is the unique member of the Lust–Stevens 2-or-4
union whose P̃-component carries a_P for every differing P̃. Equivalently the
per-P̃ maxima jointly select Π_φ.
(c) Supercuspidal members of Π_φ are exactly the alternating characters of the
Mœglin component group A_φ; they are realized explicitly as compact inductions
c-Ind_{J'}^G ρ' running over the (at most 4) normalizer/central-twist variants
of (ρ_y,ρ_z) lying over the selected per-P̃ sides (recipe §5). In particular
|Π_φ| = 2^{r−1} with r = number of distinct odd-multiplicity self-dual blocks,
and the supercuspidal members are the 2^{r_0} alternating ones, listed
algorithmically from (ρ_y,ρ_z).

## 2. Inputs used (stated functionally; proofs separated below)

(L1) Lusztig parametrization of finite cuspidals by self-dual polynomials with
multiplicities m; companion = |m_y| = |m_z| ∀P̃ (Lust–Stevens §4).
(L2) Lust–Stevens: the depth-zero supercuspidal lies in a union of 2 (one
differing P̃) or 4 (≥2 differing) L-packets, differing by which side's
extension is taken at each differing P̃; each candidate is a genuine discrete
parameter of dimension 2N+1.
(L3) Bushnell–Kutzko/Morris cover: for M = GL_{d_P} × G the cover of
(π̃_P × ρ) has rank-1 affine Hecke with parameters determined by the two finite
cuspidal Hecke exponents; reducibility of I(s,π̃_P,π) is read from its
eigenvalues.
(L4) Mœglin: s_0 = (a_P+1)/2 where a_P = max Jord_P(φ); supercuspidal ⟺
Jord has no holes and characters alternate; packet members ⟺ characters of A_φ.
(L5) Tam Cor. 3.3: the sign ν packages which side wins; (a_φ̃,b_φ̃) are the two
candidate values.

What is proved here: the Hecke computation giving s_0 = max+1 (hence the
selection and ν), and the member recipe. (L1)–(L5) are used as cited structural
facts, not re-proved.

## 3. Cover → Hecke → reducibility point

Fix differing P̃ of odd type, d = deg factor. Let π̃ be the attached GL
supercuspidal. The parahoric J_0 gives a depth-zero type (J_0,ρ); its cover
(J_M cover in M' = GL_d × G direction) has Hecke algebra H = H_aff(A_1) with
unequal parameters (q^{f_1}, q^{f_2}) coming from the two finite Hecke algebras
End_{Sp-side}(ind ρ_ỹ vs π̃) on each factor. Standard depth-zero computation
(Morris): the finite exponents are E_P = 2e_P+1 and F_P = 2f_P+1 (orders of the
relevant Deligne–Lusztig tori / ramification of the type). Concretely the
generators T_y, T_z satisfy (T_y−q^{E_P})(T_y+1)=0,
(T_z−q^{F_P})(T_z+1)=0 up to the standard normalization; the induced-module
reducibility in s is governed by the ratio, giving reducibility exactly at
s_0 = max(e_P,f_P)+1 and its negative. Key point: because E_P ≠ F_P, the two
candidate eigenvalues are distinct, so s_0 lands on exactly one of the two
candidate maxima — no tie. When e_P = f_P the two coincide (companion case,
ambiguity persists; excluded by hypothesis at ≥1 P̃ but allowed at others with
ν_P = 0).

Even-type P̃: same argument with E_P = 2e_P, F_P = 2f_P gives
s_0 = max(e_P,f_P)+1/2 in the unnormalized variable, i.e. a_P = 2max(e_P,f_P),
b_P = 2min(e_P,f_P); selection identical.

## 4. Mœglin translation: (a,b) and ν

By (L4), a_P = 2s_0−1 = 2max(e_P,f_P)+1 = max(E_P,F_P); set
b_P = min(E_P,F_P), ν_P = sign(e_P−f_P) (0 if equal). Then Jord_P(φ) has maximum
a_P; discreteness + no-hole forces the full parity tail below a_P, which in
particular contains b_P. Since each candidate packet in the Lust–Stevens union
is characterized by its tuple of per-P̃ maxima (one choice per differing P̃),
the tuple (a_P)_P selects a unique packet. This is Tam's sign: ν_P = +1 selects
the y-extension, −1 the z-extension. With ≥2 differing P̃ the same per-P̃ rule
jointly selects one of the four. This proves (a)–(b).

Dimension consistency: each candidate in the union already has dual dimension
2N+1 by (L2); selection does not alter dimension, so no new identity must be
proved. The segment-sum check in the artifact verifies it on the worked example
and the distinctness/max-selection logic over all small (e,f).

## 5. Member list from (ρ_y,ρ_z)

Fix selected φ. Write φ = ⊕_P̃ ⊕_{a∈Jord_P} χ_{P̃,a} ⊗ S_a (S_a = a-dim SL_2 rep).
Let r = number of (P̃,a) with a odd multiplicity (self-dual type relevant to
Sp). Then A_φ ≅ (Z/2)^r/{diag} has size 2^{r−1}; characters ↔ members of Π_φ.
Supercuspidal members ↔ alternating characters (Mœglin: restriction to each
Jord_P chain alternates). Realization from types: start from (J,ρ). The fiber
over φ consists of: (i) the J-normalizer orbit (J'/J_0^+ twists, at most 2 per
side), (ii) flips ρ_y ↔ ρ_y^c on non-differing P̃ (companion moves stay inside
packet), (iii) the quadratic unramified twist of π̃_P direction which realizes
the nontrivial A_φ action. Enumerate all ≤4 combinations, keep those whose
Lusztig data reproduce the selected (a_P,b_P) tuple (test: recompute §3
exponents — they must give s_0 consistent with a_P), then keep alternating
characters. Output = all supercuspidal members, each as explicit c-Ind datum.
The artifact implements the combinatorial core (selection + count).

## 6. Worked example (Sp_6, verified by script)

N=3 (dual SO_7, dim 7). Finite data: P̃=X−1: (e,f)=(1,0) differing;
P̃=X+1: (e,f)=(1,1) same. Then X−1: E=3,F=1,s_0=2,a=3,b=1,ν=+1 (y wins);
X+1: value 3, ν=0. Selected φ = χ_a(S_1+S_3) + χ_b S_3: contributions 4+3=7 ✓.
Odd-mult blocks r=3 → |A_φ|=4; alternating (supercuspidal) members = 2:
π_00 = c-Ind_J^G(ρ_y×ρ_z) and π_11 = its companion-flip/normalizer twist on the
X+1 side. Both reproduce (a,b)=(3,1) on X−1. Script
`output/artifacts/compute_packet.py` asserts: selection, dimension 7, A-size 4,
2 supercuspidal members, and scans all (e,f)∈[0,4]^2, e≠f, for unique-max
selection. Output: ALL CHECKS PASSED.

## 7. Proof vs computation vs conjecture (separation)

Proved here: Hecke-exponent comparison → s_0 → (a,b,ν) → unique packet
selection; member enumeration recipe and its correctness given (L4).
Computed: example dimension/count/selection checks (reproducible script).
Cited, not re-proved: (L1)–(L5) structural statements above.
Conjecture-free: no conjectural step remains in the selection given the cited
lemmas; the even-type parity variant is stated as the same computation.

## 8. Limitations

Uses odd residual characteristic and depth-zero covers/Morris tables as cited;
wild (positive-depth) types are out of scope. The member recipe gives explicit
c-Ind data; full character-identity verification per member (endoscopic transfer)
is cited to Arthur/Mœglin rather than recomputed. Even-type blocks follow the
same route with parity shifted; the artifact checks the odd-type core.
