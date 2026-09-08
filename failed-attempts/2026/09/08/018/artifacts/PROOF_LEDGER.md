# Proof ledger (lane-83)

## Tangle lemma (proved by induction; machine-verified n = 1..6, 12/12 E-closures)
Let T_n be the n-half-twist tangle (vertical chain, all crossings same handedness
as built), V = identity (rails through), H = cup-cap. With the calibrated
A-smoothing = rails-through (verified: trefoil/Hopf anchors), single skein step:
  T_{n+1} = A·T_n + A^{-1}·(T_n with cup-cap composed).
Since V·e = H and H·e = d·H (d = -A^2-A^{-2}):
  T_n = A^n·V + b_n·H,  b_{n+1} = A^{n-1} - A^{-3}·b_n,  b_1 = A^{-1},
hence b_n = sum_{k=0}^{n-1} (-1)^k A^{n-2-4k}. Machine check: E-closures
P^V_n = A^n·d + b_n and P^H_n = A^n + b_n·d agree with direct state-sum
brackets for n = 1..6 (script asserts equality; see checks.log).

## Closed-diagram consequences (machine-verified)
For D_n = closure of T_n against fixed tangle F (here: two fixed pretzel boxes
plus cyclic connectors), linearity gives <D_n> = A^n·X + b_n·Y with FIXED
X = <closure(V+F)>, Y = <closure(H+F)>. Verified exactly for families
P(3,3,n), P(5,3,n), P(2,5,n), n = 1..6 (script asserts <D_n> - A^n X - b_n Y = 0).
Eliminating (X,Y) gives the three-term recurrence
  c_0<D_n> + c_1<D_{n+1}> + c_2<D_{n+2}> = 0,
  c_0 = A^{n+1}b_{n+2}-A^{n+2}b_{n+1}, etc. (2x2 minors),
with residual exactly 0 for n = 1..5 on P(3,3,n) (machine-checked).
Two-step form: b_{n+2} = A^{n+1} - A^{n-4} + A^{-6}b_n (from one-step twice).

## Why the tail stabilizes (degree-gap argument + measured combs)
Top combs measured per family (exact, from aux state sums):
  top(X) = {(M,+1),(M-8,+2)}, top(Y) = {(M-2,-1),(M-10,-1)}.
Top of <D_n> (n>=2): A^nX gives (n+M,1); b_nY gives (n+M-4,-1) then (n+M-8,+1+2=+3
combined with X's second term). The top-comb SHAPE is rigid in n (uniform shift);
only b_1 (single term, n = 1) breaks the pattern. After writhe normalization
f_n = (-A)^{-3w_n}<D_n> (uniform shift) and V-subsampling (exponents mod 4, parity
class fixed along n -> n+2 steps), the tail triple is constant for m>=1 (a2) and
m>=0 (a1) within each parity subclass — exactly the observed thresholds, which are
<= the target bounds m1<=1, m2<=2. Worked f-tops for P(3,3,n), n=1..4 (see WORKLOG/
DRAFT): combs (32,-1),(28,1),(24,-2)... vs (40,-1),(36,1),(32,-3)... show the rigid
shape at n>=2 with the n=1 anomaly in the third slot.

## Count rule (empirical, 140/140 + extensions to c=17)
|a2| = #{twist boxes of length >= 2} holds on all 122 alternating P-knot rows and
all 18 integer-V link rows, plus spot runs P(3,3,n) to n=11 (c=17). No proof in full
generality is claimed; a Tutte-expansion proof sketch (third tail coefficient counts
length>=2 twist blocks via spanning-tree activity) is given as conjecture route.

## Gap classification (empirical, complete in scope)
a1 = 0 iff single twist region (torus knots T(2,N), N odd >= 3): tail (1,0,1).
a2 = 0 iff no length>=2 box (P(1,1,1) knot; unlink-type links excluded).
Otherwise signs alternate and all of a0,a1,a2 nonzero in scope.
