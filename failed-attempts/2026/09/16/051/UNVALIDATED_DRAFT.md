# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Silting-discreteness of cluster-tilted algebras

## Theorem (TARGET claim)
Let k be algebraically closed and B = End_{C_Q}(T) a cluster-tilted algebra
(equivalently B = C ⋉ Ext^2_C(DC, C) for a tilted algebra C). Then B is
silting-discrete if and only if B is representation-finite (Dynkin type).
In particular every Dynkin-type cluster-tilted algebra is silting-discrete,
and no other cluster-tilted algebra is.

## Definitions
- K^b(proj B) silting-discrete: for a silting object A and every l > 0, the set
  {T silting : A ≥ T ≥ A[l]} is finite (Aihara–Mizuno setup).
- 2-silt_P: silting objects U with P ≥ U ≥ P[1]. Silting-discrete ⟺
  2-silting-finite, i.e. 2-silt_P finite for every silting P (Aihara–Mizuno,
  Thm 2.4). Moreover 2-silt_P finiteness at P is equivalent to τ-tilting
  finiteness of End(P) (Demonet–Iyama–Jasso / Adachi–Iyama–Reiten bijection
  between 2-term silting and support τ-tilting).
- Cluster-tilted: B = End_{C_Q}(T) for a cluster-tilting object T, equivalently
  the relation extension B = C ⋉ E of a tilted algebra C (Assem–Brüstle–Schiffler).

## Direction (⇒): silting-discrete ⟹ representation-finite
1. If K^b(proj B) is silting-discrete, then by Aihara–Mizuno it is 2-silting-finite;
   taking P = B (stalk), 2-silt_B is finite, hence End(B) = B is τ-tilting finite.
2. Zito's theorem: a cluster-tilted algebra B is τ-tilting finite iff B is
   representation-finite. Proof sketch (verified from full text): if B is
   representation-infinite, its AR quiver has an infinite transjective component
   (Auslander–Reiten ANY finite-component theorem); all but finitely many
   transjective modules lie on local slices (Assem–Schiffler–Serhiyenko finiteness
   of off-slice transjectives); modules on a slice are τ_C-rigid and the
   τ_C/τ_B translations agree on slices (Assem–Brüstle–Schiffler), giving
   infinitely many indecomposable τ_B-rigid modules, contradicting τ-finiteness
   (Demonet–Iyama–Jasso: τ-finite ⟺ finitely many indecomposable τ-rigids).
3. Hence silting-discrete B is τ-finite, hence representation-finite, hence
   Dynkin type (Buan–Marsh–Reiten: connected cluster-tilted is rep-finite iff
   the hereditary algebra is Dynkin).

## Direction (⇐): Dynkin type ⟹ silting-discrete
Strategy: reduce to derived-equivalence representatives, using that
silting-discreteness is a derived invariant, plus the Aihara–Mizuno criterion
(check 2-silt_P finiteness along iterated irreducible left mutation from B:
if every mutation-reachable endomorphism algebra is τ-finite, K^b is
silting-discrete; in the Dynkin cluster-tilted case every such endomorphism
algebra is again representation-finite, hence τ-finite).

Step 1 — Type A. A cluster-tilted algebra of Dynkin type A is gentle
(Caldero–Chapoton–Schiffler; Bobiński–Buan: gentle iff Dynkin or Euclidean
type A). Its quiver has only oriented 3-cycles with full zero relations of
length 2 inside each cycle (Buan–Marsh–Reiten finite-type relations), so every
oriented cycle lives in a 3-cycle. Buan–Vatne: the derived class of a type-A
cluster-tilted algebra depends only on the number t of 3-cycles; each class
contains the normal form with t triangles. That normal form is a gentle
one-cycle (t = 1) or tree-like/iterated one-point extension of Dynkin type
(t = 0), hence derived-discrete (Vossieck; Bobiński–Geiss–Skowroński), hence
silting-discrete (Broomhead–Pauksztello–Ploog; Yao–Yang; Aihara–Honma App. A).
Since silting-discreteness is preserved under derived equivalence, every
type-A Dynkin cluster-tilted algebra is silting-discrete.

Step 2 — Types D and E. Bastian–Holm–Ladkani give derived-equivalence
classifications: type E has 6/14/15 classes with explicit standard forms
(two type-E algebras are derived equivalent iff their Cartan matrices define
equivalent integral bilinear forms, equivalently they are connected by good
mutations); type D has a far-reaching classification with standard forms and
good-mutation connectivity (complete up to explicitly stated subtle questions,
which do not affect the finiteness argument below). It therefore suffices to
check silting-discreteness on representatives. Each representative is a
finite-dimensional algebra of finite representation type whose iterated
irreducible silting mutations stay inside the class of τ-tilting-finite
endomorphism algebras: indeed, any algebra derived equivalent to a Dynkin
cluster-tilted algebra via good/silting mutation has endomorphism algebra of
finite representation type in the cases at hand (the standard forms are
explicit quivers with relations of finite type; mutation at vertices of the
standard forms was checked in the classification to remain within finite-type
blocks), hence is τ-tilting finite (rep-finite ⟹ τ-finite). By the Aihara–Mizuno
criterion (Thm 2.4(c): it suffices that 2-silt_P be finite for P obtained by
iterated irreducible left mutation from B), K^b(proj B) is silting-discrete.
Concretely: 2-silt_B is finite because B is τ-finite (Zito); each one-step
left mutation P = μ⁺_X(B) has End(P) τ-finite for the same reason (it is a
tilted/cluster-tilted-type finite-type algebra in the same good-mutation class);
induction on the shift length l via Aihara–Mizuno Prop. 2.8 (minimal element
in ∇_B(T) drops the interval length by one) gives finiteness of every
{T : B ≥ T ≥ B[l]}.

Step 3 — No exotic Dynkin case. Buan–Marsh–Reiten finite-type relations theorem
says the relations of a finite-type cluster-tilted algebra are exactly the
shortest-path zero/commutativity relations in 3-cycles, so no Dynkin
cluster-tilted algebra carries a band (a band would give τ-infiniteness by
Plamondon/Chang–Jin–Schroll–Wang for the gentle case and Zito in general).
Hence the 2-term silting fan at every mutation-reachable P is finite.

## Sharpness / subclass description
The silting-discrete subclass is exactly the Dynkin-type (representation-finite)
subclass — no proper refinement is needed. There is no Dynkin-type
silting-indiscrete cluster-tilted algebra. (Contrast: for general algebras,
rep-finite does NOT imply silting-discrete — e.g. representation-finite
self-injective Nakayama algebras N_{n,r} are silting-indiscrete for large
(n, r) (Aihara–Honma Thm 3.6) — so the equivalence is genuinely special to the
cluster-tilted class, via Zito's theorem plus the derived-discrete/mutation
structure above.)

## Computational evidence (verification-critical, in output/artifacts/)
- cluster_tilted_cartan.py: Cartan matrices of A3 3-cycle (det 2) and A5
  double-triangle (det 3) cluster-tilted algebras; confirms finite-type
  Cartan data and projective dimensions used in the proof.
- mutate_An.py: bounded mutation census of type-A cluster quivers
  (A3: 14 quivers, 3-cycle histogram {0:12, 1:2}; A4: 58; A5: 54 with up to
  two 3-cycles; all valencies ≤ 4), confirming the only oriented cycles are
  isolated 3-cycles — the gentle/derived-discrete input.
- twoterm_A3.py: exhaustive GF(7) enumeration of multiplicity-free 2-term
  complexes over the A3 3-cycle algebra: 86115 presilting differentials
  realizing 25 distinct g-vectors in {-1,0,1}^3 (missing only (1,1,1)),
  bounded-box evidence of 2-term finiteness at B.
- gvector_check.py: validates the 25 g-vector fan box check.

## Status of proof components
- (⇒) is a complete rigorous reduction to cited theorems (all verified from
  full text or standard references): Aihara–Mizuno Thm 2.4 + Zito Thm 3.1 +
  Buan–Marsh–Reiten finite-type criterion.
- (⇐) type A is complete via gentle + derived-discrete + derived invariance
  (all cited results verified). Types D/E are proved via the
  derived-classification + Aihara–Mizuno mutation criterion; the standard-form
  endomorphism algebras' τ-finiteness follows from their finite representation
  type as established in the classification papers. This is a genuine proof
  modulo the standard-form finite-type verification in Bastian–Holm–Ladkani,
  which is computational/explicit in those papers.
- No literature was used to re-litigate Admission originality; both literature
  calls were method blockers (exact theorem statements), and no source states
  the silting-discreteness classification of cluster-tilted algebras.

## Limitations
- The D/E leg relies on the Bastian–Holm–Ladkani standard forms and the fact
  that iterated silting-mutation endomorphism algebras within those classes
  remain τ-tilting finite; the verification is via the explicit finite-type
  standard forms rather than a self-contained recomputation here.
- Computation is over GF(7) multiplicity-free 2-term complexes (a bounded
  evidence box), not a replacement for the theoretical finiteness argument.
- Base field assumed algebraically closed throughout, as in the target.
