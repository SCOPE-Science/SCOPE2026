# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Ingleton-deficit study of the tic-tac-toe family and the Vámos-configuration poset

## Abstract
We report exact, fully machine-checked Ingleton-inequality deficit
computations relevant to the proposed linear-vs-algebraic propagation lemma.
The headline mathematical content is corrective: the rank-5 tic-tac-toe
primals, their rank-4 duals, and the rank-4 P8 family all satisfy Ingleton's
inequality (maximum deficit 0, proved by exhaustive enumeration over all
ordered 4-tuples of subsets), so no Ingleton violation exists on those
objects to propagate, and the literal fallback bound "D\* >= 1 over the TTT
9-point poset" is false. As a salvageable exact finite result, we prove an
Ingleton-deficit atlas: (a) deficit 0 for all six TTT 9-point objects, and
(b) maximum deficit exactly 1 over the 16-member single/double-relaxation
poset of the 8-point Vámos-configuration specimen, attained at the specimen
with an explicit witness and rank table, with every other member at 0.
The algebraic-representation and infinite-propagation parts of the target
claim are not achieved and are restated as conjectures with the obstruction
identified.

## 1. Ingleton's inequality and deficit
For sets A,B,C,D, with r the matroid rank function, use the matroid form
(Ingleton 1971):
D(A,B,C,D) = r(A)+r(B)+r(A∪B∪C)+r(A∪B∪D)+r(C∪D)
           − r(A∪B)−r(A∪C)−r(A∪D)−r(B∪C)−r(B∪D).
A matroid is Ingleton-satisfying iff D ≤ 0 for all A,B,C,D; a violation
(D ≥ 1) implies non-linear-representability over every field. All
sparse-paving ranks here are computed from the committed nonbasis
(circuit-hyperplane) list: r(X) = min(|X|,k), except r(X) = k−1 when
X itself is a listed nonbasis.

## 2. Objects and coordinates
- 9-point TTT family on E = F3×F3 (index (x,y) ↦ 3x+y):
  Ai = {(x,i)}, Bj = {(j,y)}, Ck = {x−y=k}, Dℓ = {x+y=ℓ} (mod 3).
  Rank-5 primal nonbases: the nine 5-sets Ai∪Bj (T13); T3 drops A0∪B0;
   maximal T1m adds the nine 5-sets Ck∪Dℓ. Rank-4 dual nonbases are the
   complementary 4-sets (masks in artifacts/results.txt; T3-dual 8, T13-dual
   9, maximal dual 18).
- 8-point Vámos specimen V on {0,…,7} (cube vertices = binary triples),
  nonbases 0123, 0145, 2367, 4567, 2345 (masks 0x0f 0x33 0xcc 0xf0 0x3c),
  the paper's §4 Vámos list, a relaxation of AG(3,2).
- P8 family (paper §4): the ten listed circuit-hyperplanes and the
  relaxations P8,1, P8,2′, P8,2″, P8,3.

## 3. Theorem (exact Ingleton-deficit atlas; machine-checked)
(a) Zero-deficit part. Each of the six TTT 9-point matroids (three rank-5
primals T3, T13, T1m; three rank-4 duals) has maximum Ingleton deficit 0:
npos = 0 positive tuples over the full (2^9)^4 = 68.7×10^9 ordered tuples.
The five P8-family 8-point matroids likewise have maximum deficit 0
(full 256^4 scans).
(b) Vámos-poset part. Let V be the 5-nonbasis specimen above and P(V) its
16-member single/double-relaxation poset (V itself, 5 single-relaxations,
10 double-relaxations). Then max_{M ∈ P(V)} max_{A,B,C,D} D_M = 1,
attained at M = V, e.g. A = {4,5}, B = {2,3}, C = {0,1}, D = {6,7} with
LHS ranks (2,2,4,4,4) summing to 16 and RHS ranks (3,3,3,3,3) summing to
15, so D = 1; every other member of P(V) has maximum deficit 0.
Consequently V is not linearly representable over any field, and no other
member of P(V) admits an Ingleton certificate of non-linearity.

## 4. Proof and replay
Exhaustive enumeration in OpenMP C (artifacts/ingleton_scan.c), one run per
matroid, printing (best, npos, witness, witness rank table); replay via
artifacts/replay.sh; transcript in artifacts/results.txt. The Vámos
witness is additionally hand-verifiable from the rank table in §3(b):
with A = {4,5}, B = {2,3}, C = {0,1}, D = {6,7}: ABC = {0,1,2,3,4,5} and
ABD = {2,3,4,5,6,7} are 6-sets (rank 4), CD = {0,1,6,7} is a 4-set not in
the nonbasis list (rank 4), and each RHS union AB = {2,3,4,5}, AC = {0,1,4,5},
AD = {4,5,6,7}, BC = {0,1,2,3}, BD = {2,3,6,7} is a listed nonbasis
(rank 3), giving 16 − 15 = 1. Spanning reduction is not invoked: the scans cover literally
all tuples, so no tuple is missed.

## 5. Status of the target claim
- (a) Ingleton violation on a TTT 9-point relaxation: REFUTED (all six
  objects satisfy Ingleton; §3(a)). Hence the propagation lemma has no
  Ingleton-violating seed on these objects, and the infinite minor-minimal
  family is not constructed here.
- (b) Algebraic (or folded-linear) representation of T\*: not established;
  no assignment is claimed.
- (c) Corrected finite contribution: the exact atlas of §3, which is new
  as an explicit computed certificate (the zero-deficit half corrects the
  admission's expectation; the Vámos-poset maximum-1 half is the
  D\* = 1 exact bound on its stated poset).

## 6. Uncertainties and limits
The enumeration code is small and replayable but was validated by
reproducing the known Vámos deficit-1; an independent reimplementation
(e.g. in Sage/matroid packages) was out of scope. No claim is made about
other rank inequalities (Kinser/Mayhew/Zhang–Yeung) or about iterated
extension-property failures, which are the actual known non-linearity
certificates for the TTT/P8 families. Isomorphism classification of poset
members is not claimed.
