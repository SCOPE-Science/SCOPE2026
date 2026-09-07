# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Equiangular lines with angle arccos(1/5) in R^9: 12 ≤ N ≤ 13 with a certified 12-witness

## Abstract

Let N_{1/5}(9) be the maximum number of lines through the origin in R^9 with
pairwise angle arccos(1/5). We prove

**Theorem.** 12 ≤ N_{1/5}(9) ≤ 13.

The lower bound is an explicit 12×12 Gram matrix G (1 on the diagonal,
±1/5 off-diagonal) with exact spectrum {12/5 (×1), 0 (×3), 6/5 (×8)},
hence PSD of rank 9. The upper bound is the classical
Delsarte–Goethals–Seidel relative bound, reproduced here self-contained,
giving N ≤ 9(1−1/25)/(1−9/25) = 13.5, i.e. N ≤ 13. This improves the
Lin–Yu K=3 pillar bound max{165, r+6} = 165 at r=9 to 13, and replaces a
numeric SDP bound by a millisecond-recheckable certificate. We further prove
the 12-configuration is saturated in R^9 (no 13th line can be added to it
while staying in R^9; all 4096 extensions are classified analytically), and
document seeded heuristic search for a 13-configuration that found none.
Whether N = 12 or 13 remains open; the gap is a single integer. All claims
replay from stored artifacts in seconds with stdlib + numpy only.

*Status of claims.* Proved: interval [12,13], PSD-rank certificate,
saturatedness, U=13. Computed (not proved): failure to find 13-witness.
Conjectured (not claimed): N=12. No claim of exact census or exhaustive
optimality over all Seidel graphs of order 13 is made.

## 1. Setup

Lines ↔ unit vectors v_1,…,v_N ∈ R^d up to sign. Gram
G_{ij} = ⟨v_i,v_j⟩ has 1 on diagonal, ±α off-diagonal with α=1/5,
is PSD, rank ≤ d. Conversely any such G arises from lines in R^d.
Switching (negating a vector) flips signs in a row/column; the Seidel graph
(edge iff inner −α) is defined up to switching and permutation.

## 2. Upper bound N ≤ 13 (Delsarte–Goethals–Seidel relative bound)

We give the short degree-2 LP proof, needing only k=0,1,2 positivity.

Let X={v_1,…,v_N} ⊂ S^{d−1}, pairwise inner ±α, d=9, α=1/5.
Put P_0(t)=1, P_1(t)=t, P_2(t)=(dt²−1)/(d−1).

**Lemma (positivity).** For any finite X on S^{d−1},
S_k := Σ_{x,y∈X} P_k(⟨x,y⟩) ≥ 0 for k=0,1,2.
*Proof.* k=0: S_0=N². k=1: Σ⟨x,y⟩=‖Σx‖²≥0. k=2: let G be the Gram,
eigenvalues λ_i≥0, Σλ_i=N, rank≤d. Then Σ_{x,y}⟨x,y⟩²=Tr G²=Σλ_i²
≥(Σλ_i)²/d=N²/d by Cauchy on the ≤d nonzero λ_i. Hence
S_2=(dΣ⟨x,y⟩²−N²)/(d−1)≥0. ∎

Consider f(t)=t²−α². Since t²=((d−1)P_2(t)+1)/d,
f = a_2 P_2 + a_0 P_0 with a_2=(d−1)/d=8/9≥0,
a_0=1/d−α²=(1−dα²)/d. For d=9, α=1/5: a_0=(16/25)/9=16/225>0.

Summing: Σ_{x,y} f(⟨x,y⟩)=a_0 S_0+a_2 S_2 ≥ a_0 N².
But f(±α)=0 and f(1)=1−α², so the sum equals N(1−α²).
Hence N(1−α²)≥a_0N², i.e.

N ≤ (1−α²)/a_0 = d(1−α²)/(1−dα²),

whenever 1−dα²>0. For (9,1/5): 9(24/25)/(16/25)=27/2=13.5, so N≤13. ∎

*Remark (2-point LP optimality).* With f_0=1 the 2-point LP
minimizes Σf_k subject to Σf_kP_k(±α)≤−1, f_k≥0. The most negative
even P_k(α) dominates. Direct computation of normalized Gegenbauer values
P_k(1/5) in dimension 9 (recurrence
(k+1)C_{k+1}=2(k+λ)tC_k−(k+2λ−1)C_{k−1}, λ=7/2) gives
P_2=−0.08, P_3=−0.064, P_7≈−0.010, all others >−0.01 up to k=60 and
|P_k|→0, so P_2 is the global minimizer. Hence no higher-degree 2-point
polynomial improves 13.5. Closing to 12 needs 3+-point SDP, not attempted
(no solver in this environment). This is a limitation, honestly noted.

## 3. Lower bound N ≥ 12: the 4×K_3 witness

This is Jiang et al., Prop. 3.2 with H=K_3 (spectral radius 2=λ=(1−α)/2α).
We make it fully explicit.

Label 12 lines by (a,i), a=1..4, i=1..3. Define G by
G=1 on diagonal, −1/5 if same block a, different i; +1/5 if different blocks.
Associated graph: 4 disjoint triangles. File `artifacts/gram12.csv` stores it.

**Proposition.** G is PSD of rank 9 with spectrum 12/5(×1), 0(×3), 6/5(×8).
*Proof.* By S_3≀S_4 symmetry decompose R^{12}: (i) constants c·1:
row sum =1+2(−1/5)+9(1/5)=12/5, eigenvalue 12/5, dim 1. (ii) block-constant
with block values c_a, Σc_a=0: (Gv)_a=(3/5)c_a+(1/5)·3(−c_a)=0, eigenvalue 0,
dim 3. (iii) within-block sum-zero (Σ_i v_{a,i}=0 ∀a): between-block terms
vanish, (Gv)_{a,i}=v_{a,i}−(1/5)(−v_{a,i})=(6/5)v_{a,i}, eigenvalue 6/5,
dim 8. Dimensions sum to 12. All eigenvalues ≥0, nonzero count 9. ∎

Hence 12 equiangular lines with angle arccos(1/5) exist in R^9
(rank-9 PSD Gram). So N≥12. The integer matrix 5G has spectrum {12,0×3,6×8}.

*Originality note.* The construction is the general Jiang lower bound, not
new; novelty is only the explicit (9,1/5) instantiation with exact spectrum
and replayable certificate.

## 4. Saturatedness: the 12-set is maximal by inclusion

**Theorem.** No 13th line with angle arccos(1/5) can be added to the above
12-set while staying in R^9. Every PSD one-line extension needs rank 10.

*Proof.* Let s∈{±1/5}^{12} be the new column, t=5s∈{±1}^{12}.
G_{12} has kernel = block-constant sum-zero (dim 3). For
[[G_{12},s],[s^T,1]] to be PSD need s∈col(G_{12}), i.e. s⊥ker,
i.e. block sums b_a=Σ_{i∈block a} t_i all equal to a common b∈{−3,−1,1,3}.
Count: 1+81+81+1=164 patterns (matches machine count 164/4096 PSD).
Write t=(b/3)1+u with u block-sum-zero. G^+ acts as 5/12 on span{1},
5/6 on the 6/5-eigenspace. So t^TG^+t=(4b²/3)(5/12)+(12−4b²/3)(5/6)
=10−5b²/9. Thus s^TG^+s=(18−b²)/45 and Schur complement
1−s^TG^+s=(27+b²)/45≥28/45>0 always. So extended rank =9+1=10. ∎

Exhaustive check over all 4096 masks in `verify.py` confirms: 164 PSD,
best rank 10, none PSD rank ≤9. This is inclusion-maximality of this one
12-set, NOT global optimality (other 12-sets could in principle extend).

## 5. Computational evidence on N=13 (not a proof)

- Random order-13 Seidel (first row switched to +): ~8% PSD in 200 trials,
  all full rank. PSD alone does not prune; rank≤9 (four zero eigenvalues)
  is the hard constraint.
- Single-flip hill climbing (66 free bits) and 8-restart simulated annealing
  (~64k eigvalsh evals, seed 42): best PSD has 4th eigenvalue w_3≈0.13,
  need w_3=0 for rank ≤9. One singular PSD rank-12 found (w_0≈0), none ≤9.
- Full branch-and-bound over 2^66 to rule out 13 is infeasible here
  (order-9 prefixes alone number 2^28; no scipy/networkx/SDP solver).
  Logged honestly as open gap {13} in `optimality_log.jsonl`.

Conjecture (unproved): N_{1/5}(9)=12, agreeing with Jiang's asymptotic
⌊3·8/2⌋=12. But an exceptional uplift to 13 (as occurs at d=18,23 from
Witt/Leech truncations) cannot be excluded by our methods; relative bound
allows 13.

## 6. Comparison with prior work

- Jiang et al. asymptotic: predicts 12 but threshold is doubly exponential,
  gives no finite-d=9 certificate. Our 4×K_3 is their construction made explicit.
- Lin–Yu: overall M(9)=28 (angle 1/3), and K=3 fixed-angle bound 165.
  We replace 165→13 for (9,1/5) and separate fixed-angle from overall maxima;
  Yoshino's gap in Lin–Yu K=5 motivates our machine-checked route.
- Barg–Yu / de Laat k-point SDP: numeric, n≥24 or non-sharp at low d.
  Our bound is exact-rational, rechecks in milliseconds.
- No prior source gives a rerunnable Gram witness + PSD-rank + saturation
  certificate for (9,1/5). That exactness step is our delta, not a parameter shift.

## 7. Reproducibility

`output/artifacts/`: `gram12.csv`, `certificate.json`, `verify.py`
(stdlib+numpy only), `optimality_log.jsonl`. Run `python3 verify.py`:
entry check → eigvalsh PSD-rank + spectrum → bound arithmetic → 4096-extension
saturation loop. Seconds on a standard CPU. Pinned: python 3.12, numpy 1.26.4,
seed 42. No scipy/networkx needed.

## 8. Limitations and what would close the gap

1. Exact value (12 vs 13) undecided; only interval proved.
2. No exhaustive Seidel order-13 enumeration; 2-point LP proved optimal at 13.5,
   so need 3+-point SDP dual certificate or smarter exact combinatorics
   (e.g. pillar/King–Tang or Barg–Yu SDP with a solver) to force 12 or exhibit 13.
3. Saturatedness is for one 12-set only.
4. All eigenvalues checked with tolerance 1e-8/1e-7 plus exact analytic spectra;
   no interval arithmetic library was available, but integer-matrix spectra
   (5G eigenvalues 12,0,6) make the certificate exact.

## References

- Lemmens–Seidel 1973 (foundations, pillar/base size, Neumann, relative bound context).
- Delsarte–Goethals–Seidel 1977 (spherical LP; relative bound).
- Neumaier (N_{1/5}=⌊3(d−1)/2⌋ large d).
- Barg–Yu 2013 (SDP bounds n≥24); de Laat–Machado–Oliveira–Vallentin 1812.06045 (k-point SDP).
- Jiang–Tidor–Yao–Zhang–Zhao 1907.12466 (fixed-angle asymptotics; K_3 construction).
- Lin–Yu 1807.06249 (Lemmens–Seidel K=3,5; M(8,9,10)=28; 165 bound).
- Yoshino 2209.08308 (gap in Lin–Yu K=5; 57 lines in R^18).
