# Nontrivial VC-splitting of G2 = <a,b,c | (aba^-1 b^2 c^3)^3>

## Context

Let F(a,b,c) be free on a,b,c and w2 = aba^-1 b^2 c^3. The group
G2 = <a,b,c | w2^3 = 1> is a three-generator one-relator group with
torsion of order 3. The admitted target asks a two-sided question:
either prove G2 is one-ended with trivial JSJ decomposition over
virtually cyclic subgroups, or exhibit one explicit nontrivial splitting
as an amalgamated free product or HNN-extension over an infinite cyclic
or infinite dihedral subgroup, with full proof. This record resolves the
second horn. The nearest general background is the Magnus/Moldavanski
HNN rewriting for one-relator groups, the McCool-Schupp exposition, and
the JSJ theory of one-relator groups with torsion (Logan; Gardam-Kielak-
Logan in the two-generator case). None decides this specific three-
generator word.

## Definitions

- w2 = a b a^-1 b^2 c^3, letter-length 8, exponent sums (a,b,c)=(0,3,3).
- S = d b^2 c^3 in generators b,c,d, letter-length 6, exponent sums
  (b,c,d)=(2,3,1).
- J = <b,c,d | S^3 = 1>, a three-generator one-relator group with torsion.
- HNN-extension <J,a | a b a^-1 = d>: base J, stable letter a,
  associated subgroups <b> and <d> identified by b |-> d.

## Result

Theorem. G2 admits the nontrivial splitting G2 ~= <J,a | a b a^-1 = d>
with J = <b,c,d | (d b^2 c^3)^3 = 1>, an HNN-extension over the infinite
cyclic subgroup <b> ~= <d>. Hence G2 splits nontrivially over an infinite
cyclic (hence virtually cyclic) subgroup. The first horn of the target
(one-ended with trivial VC-JSJ) is therefore false for G2.

## Proof / evidence

1. Word check. w2 is reduced and cyclically reduced (first letter a,
last letter c), involves each generator, has exponent sums (0,3,3) with
gcd 3 hence non-primitive, and is not a proper power (length 8 excludes
block lengths 1,2,4). Verified by hand and computationally.
2. Tietze move. Add d with d = a b a^-1. Then w2 = d b^2 c^3 = S
literally, so G2 ~= <a,b,c,d | S^3=1, a b a^-1 d^-1=1>. The relator S^3
uses only b,c,d while a occurs only in the conjugating relation, giving
G2 ~= <J,a | a b a^-1 = d>. S is cyclically reduced of length 6 with
exponent sums (2,3,1), not a proper power.
3. Edge groups infinite cyclic in J. Abelianizing J imposes
3*(2,3,1)=(6,9,3) on (b,c,d). The forms theta(b,c,d)=b+c-5d and
eta(b,c,d)=b-c+d vanish on S (2+3-5=0; 2-3+1=0), defining J -> Z with
theta(b)=1 and eta(d)=1. Hence b,d have infinite order in J and
<b>,<d> are infinite cyclic: a genuine HNN with cyclic edge groups.
4. Nontriviality. The maps psi(a,b,c)=(1,0,0) (a-coordinate) and
chi(a,b,c)=(0,1,-1) are well defined on G2 since psi(w2)=0 (a-sum 0)
and chi(w2)=3-3=0; chi(b)=1 and psi(a)=1 give b,a infinite order in G2.
psi kills vertex generators b,c and d=aba^-1 but not a, so no conjugate
of J equals G2. By Britton's lemma / Bass-Serre theory the stable letter
is hyperbolic on the Bass-Serre tree: no global fixed point, so the
splitting is nontrivial over <b>.

## Limitations

The proof establishes the second horn (nontrivial HNN over infinite
cyclic <b>) and hence nontrivial VC-JSJ. It does not determine whether
G2 is one-ended, nor compute the full JSJ decomposition; neither is
required once a splitting is exhibited.

## Reproducibility

Word combinatorics and homomorphism arithmetic were rechecked by the
auditor by hand and by re-executing inputs/artifacts/verify_g2.py
(ALL CHECKS PASSED). All integer witnesses above can be verified by
exponent-sum arithmetic.

## References

- J. McCool, P. E. Schupp, On one relator groups and HNN extensions,
  J. Austral. Math. Soc. 16 (1973), 249-256 (Moldavanski HNN rewriting).
- A. D. Logan, The JSJ-decompositions of one-relator groups with torsion,
  Geom. Dedicata 180 (2016), 171-185; arXiv:1412.5357.
- G. Gardam, D. Kielak, A. D. Logan, JSJ decompositions and polytopes for
  two-generator one-relator groups, arXiv:2101.02193.
