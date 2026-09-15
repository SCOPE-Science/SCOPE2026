# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Relative-to-absolute virtual specialness across the JSJ of one-ended torsion-free hyperbolic groups — conditional dichotomy

## 1. Statement

**Theorem (conditional dichotomy).** Let $G$ be a one-ended torsion-free hyperbolic
group with nontrivial Bowditch JSJ decomposition over infinite cyclic subgroups,
with rigid vertex groups $G_v$ and QH vertex groups. For each rigid $v$ let
$\mathcal P_v$ be representatives of $G_v$-conjugacy classes of incident edge
stabilizers (infinite cyclic). Suppose that for every rigid $v$:

- (i) $(G_v,\mathcal P_v)$ is relatively hyperbolic and admits a weakly
  relatively geometric action on a CAT(0) cube complex in the sense of
  Groves–Manning Definition 1.9, with cyclic peripherals satisfying the
  separability Assumptions 1.1–1.2 on hyperplane–peripheral intersections and
  double cosets;
- (ii) after finite-index passage the family $\mathcal P_v$ can be made
  malnormal in $G_v$; equivalently there are finite-index
  $\dot P \triangleleft P$ for each $P\in\mathcal P_v$ such that every
  peripherally finite Dehn filling with kernels $N\triangleleft \dot P$ is
  hyperbolic and virtually compact special in the sense of Einstein Theorem 2.

Then $G$ is virtually compact special. Consequently there is a dichotomy:
either $G$ is virtually compact special, or some rigid pair
$(G_v,\mathcal P_v)$ fails (i) or (ii), and such a failure is the sole
obstruction (every other step of the proof is unconditional).

**Proof strategy and status of citations.** The deep relative-cubulation and
Dehn-filling inputs — Groves–Manning (weakly) relatively geometric cubulation
theory and Einstein's virtually-special filling theorem — are used as black
boxes whose hypotheses are exactly (i)–(ii). What is proved here is the
assembly: QH vertices are unconditionally virtually special; under (i)–(ii)
each rigid vertex is virtually compact special by the cited criteria; the
finite JSJ graph of groups with quasiconvex cyclic edges then combines via
Wise's quasiconvex hierarchy theorem plus Agol's theorem to give virtual
compact specialness of $G$. The dichotomy is the contrapositive plus the
observation that no other conditional input is used. No effective index is
claimed.

## 2. JSJ preliminaries (unconditional)

We use the Bowditch JSJ splitting of a one-ended torsion-free hyperbolic group
over infinite cyclic subgroups (Bowditch; Guirardel–Levitt formulation). Facts
used, all standard and unconditional:

1. The JSJ is a finite graph of groups with $G$ as fundamental group;
   nontrivial by hypothesis.
2. Edge groups are infinite cyclic and quasiconvex in $G$ (infinite cyclic
   subgroups of hyperbolic groups are quasiconvex).
3. Each vertex group $G_v$ is quasiconvex in $G$, hence hyperbolic and
   torsion-free. Non-elementary vertices are of two kinds: rigid (does not
   split further over cyclics relative to incident edges) and QH (quadratically
   hanging: finite-type surface group with incident edge groups corresponding
   to boundary components, up to the usual exceptional cases which are free or
   free-abelian-of-rank-one and equally harmless). Any elementary (cyclic)
   vertex group is virtually compact special trivially.
4. Virtual compact specialness is a commensurability invariant in the relevant
   sense: if $H\le G$ has finite index and $H$ has a finite-index subgroup
   acting freely cocompactly essentially on a compact special cube complex,
   then so does $G$ (pass to a common finite-index subgroup / finite cover),
   and finite-index subgroups of virtually compact special groups are
   virtually compact special (finite covers of special complexes are special).
   Hence all finite-index passages below are harmless for the conclusion.

## 3. Lemma A — QH vertices are unconditionally virtually compact special

**Lemma A.** Each QH vertex group of the above JSJ is virtually compact
special (indeed, a finite-type surface or free group, hence compact special
up to an elementary finite-cover argument).

*Proof.* In the torsion-free hyperbolic cyclic JSJ, a QH vertex group is the
fundamental group of a compact surface $\Sigma$ with boundary components
identified with incident edge stabilizers (exceptional cases: thrice-punctured
sphere / pair of pants gives a free group of rank 2; once-punctured torus and
four-punctured sphere are ordinary surface groups; cylinders/Möbius cases give
cyclic groups). Free groups and surface groups of finite type act freely
cocompactly on compact special cube complexes (Haglund–Wise; Wise: surface
groups are virtual retracts of right-angled Artin groups / directly cubulated
and special). Closed hyperbolic surface groups are compact special; bounded
cases deformation-retract to graphs with surface relations and are likewise
compact special after the standard subdivision / VH-structure. Free and cyclic
groups are compact special. Hence every QH vertex group is (virtually)
compact special with no hypothesis on rigid vertices. ∎

## 4. Lemma B — rigid vertices under (i)–(ii) (cited relative-to-absolute criterion)

**Lemma B.** Assume (i) and (ii) for a rigid vertex $v$. Then $G_v$ is virtually
compact special.

*Proof (assembly of cited black boxes).* By (i), $(G_v,\mathcal P_v)$ is
relatively hyperbolic with cyclic peripherals and admits a weakly relatively
geometric action on a CAT(0) cube complex satisfying Groves–Manning
separability Assumptions 1.1–1.2. This is exactly the cubical input of the
Groves–Manning / Einstein theory: hyperplane stabilizers intersect peripherals
in separable (hence virtually special-compatible) subgroups and double cosets
are separable, so the relatively geometric action descends to cubulations of
long fillings.

By (ii), after replacing each $P$ by a finite-index normal $\dot P$, every
peripherally finite filling
$G_v(N_1,\dots,N_k)=G_v/\langle\!\langle N_1,\dots,N_k\rangle\!\rangle$ with
$N_i\triangleleft \dot P_i$ is hyperbolic and virtually compact special —
the conclusion of Einstein Theorem 2 applied to the data of (i). (The
malnormalization in (ii) is the standard passage making the peripheral family
almost malnormal, which is the hypothesis that makes the Malnormal Special
Quotient Theorem and its Einstein refinement applicable; for cyclic
peripherals this is a finite-index peripheral refinement, preserving relative
hyperbolicity by Osin's peripheral-refinement results.)

Finally, virtual compact specialness of all sufficiently long (peripherally
finite) hyperbolic fillings of a relatively hyperbolic group with virtually
special (here cyclic) peripherals promotes to virtual compact specialness of
the group itself. This recovery step is the established
Groves–Manning–Einstein / Wise–Agol filling-to-group promotion: a relatively
hyperbolic group whose long fillings are uniformly hyperbolic and virtually
compact special, cubulated compatibly with the relatively geometric action,
is itself virtually compact special (via the Malnormal Special Quotient
Theorem, hierarchical-hyperbolicity/virtual-specialness promotion, and
Agol's theorem; cf. Einstein Theorem 2 and the Groves–Manning relatively
geometric virtual-specialness criterion). Since the hypotheses of those
theorems are exactly (i)–(ii), $G_v$ is virtually compact special. Finite
index changes of peripherals or passage of $G_v$ to a finite-index subgroup
in (ii) preserve this conclusion by §2(4). ∎

*Remark on proof vs. citation.* Lemma B is deliberately stated as the
conditional packaging of the cited deep theorems: its content is that (i)–(ii)
are precisely the hypotheses those theorems require. We do not reprove
Groves–Manning or Einstein; the original work of this note is the JSJ assembly
(Lemmas A, C and the dichotomy).

## 5. Lemma C — combination across the JSJ (unconditional given vertex specialness)

**Lemma C.** Let $G$ be torsion-free hyperbolic splitting as a finite graph of
groups with quasiconvex vertex groups that are virtually compact special and
infinite cyclic (hence quasiconvex) edge groups. Then $G$ is virtually compact
special.

*Proof.* Reduce the finite graph of groups to an iterated sequence of
amalgams $A*_C B$ and HNN extensions $A*_C$ with $A,B$ hyperbolic virtually
compact special and $C$ infinite cyclic quasiconvex, each intermediate
fundamental group hyperbolic (it embeds as a quasiconvex subgroup datum of
the ambient hyperbolic $G$; quasiconvexity of vertex/edge groups in $G$
restricts correctly). Each such splitting over a quasiconvex subgroup gives a
(quasiconvex) hierarchy step. Since virtually compact special hyperbolic
groups admit malnormal quasiconvex hierarchies (Wise; Agol–Groves–Manning
malnormalization), grafting the vertex hierarchies along the JSJ edges yields
a finite quasiconvex hierarchy for (a finite-index subgroup of) $G$
terminating in virtually compact special groups. By Wise's quasiconvex
hierarchy theorem — a hyperbolic group with a quasiconvex hierarchy
terminating in virtually special groups is virtually compact special — combined
with Agol's theorem (hyperbolic cubulated groups with the hierarchy are
virtually compact special), $G$ is virtually compact special. Torsion-freeness
removes orbifold/finite-stabilizer complications. ∎

## 6. Main proof and dichotomy

Assume (i)–(ii) at every rigid vertex. By Lemma A each QH vertex group is
virtually compact special; by Lemma B each rigid vertex group is virtually
compact special; cyclic vertices if present are too. Edge groups are infinite
cyclic, quasiconvex. The JSJ is a finite graph of groups satisfying the
hypotheses of Lemma C. Hence $G$ is virtually compact special.

Dichotomy: the argument above uses, beyond unconditional JSJ/quasiconvexity/
QH-specialness/hierarchy-combination facts, only hypotheses (i)–(ii) at rigid
vertices. Logically,
$(\forall v\, (i)_v \wedge (ii)_v) \Rightarrow G$ virtually compact special.
The contrapositive is: if $G$ is not virtually compact special, then for some
rigid $v$, (i)$_v$ or (ii)$_v$ fails. In that sense a rigid-pair failure is the
sole possible obstruction: every QH and combination step is unconditional, so
no other failure can block the conclusion. This is the claimed conditional
dichotomy (it does not assert when (i)–(ii) hold, nor give an effective
index). ∎

## 7. Limitations and what is not claimed

- Conditional: the theorem assumes (i)–(ii), which encode the deep
  Groves–Manning cubulation/separability and Einstein filling hypotheses.
  Deciding when a given rigid pair satisfies them is outside the scope.
- Black boxes: Groves–Manning Definition 1.9 / Assumptions 1.1–1.2, Einstein
  Theorem 2, Bowditch/Guirardel–Levitt JSJ quasiconvexity, Haglund–Wise QH
  specialness, and Wise QHT + Agol are cited, not reproved.
- No effective bound on the index of a special subgroup, no construction of
  the cube complex, and no converse (rigid failure need not imply $G$ is not
  virtually special; the dichotomy states only that it is the sole possible
  obstruction within this route).
- Torsion-free and one-ended hyperbolic hypotheses are used essentially
  (quasiconvexity, JSJ form, specialness without torsion).
