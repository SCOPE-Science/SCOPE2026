# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Blow-up divisors cannot cover Lagrangian boundaries:
# a topological obstruction for Sp(4,R) projective loci in dimension four

## Statement
Let G = Sp(4,R), Q_Sieg the Siegel parabolic (Lagrangian stabilizer), so
G/Q_Sieg is the 3-dimensional Lagrangian Grassmannian L with pi_1(L) = Z.
Let E = RP^3 be the exceptional divisor of the real blow-up of a 4-manifold
at a point (e.g. a fixed point of the standard Sp(4,Z)-action on T^4), with
pi_1(E) = Z/2. Then:

(a) There is no covering map h: E -> L.
(b) The blow-up divisor action is the projectivized isotropy action on lines
    (the Klingen/line-stabilizer quotient G/Q_line = RP^3), not the Siegel
    projective action; Q_Sieg and Q_line are non-conjugate maximal parabolics
    whose quotients are already distinguished by pi_1 (Z vs Z/2).
(c) Consequently the "volume-preserving blow-up of a fixed point realizes the
    Lagrangian locus as a covering" construction is impossible as stated.

## Proof
(a) A covering map induces an injective homomorphism on fundamental groups.
Any homomorphism Z/2 -> Z sends the generator g to an element k with
2k = 0; since Z is torsion-free, k = 0, so Hom(Z/2,Z) = 0 and no injection
Z/2 -> Z exists. Hence no covering RP^3 -> L exists.

(b) The real blow-up replaces a point by the space of lines through it,
P(T_p M) = RP^3; the induced action on the divisor is the projectivized
derivative, i.e. the line action G/Q_line. The Siegel quotient parametrizes
Lagrangian planes, a different G-space; pi_1 distinguishes them.

(c) Follows from (a)-(b): E has the wrong topology and the wrong parabolic
dynamics for the Siegel/Lagrangian clause.

## Dimension census (checked by output/artifacts/verify_obstruction.py)
dim Sp(4,R) = 10; Borel = 6 (G/B 4-fold); Siegel Q = gl(2) [4] + Sym^2 [3]
= 7, so dim G/Q = 3 = v(G). The Klingen maximal parabolic is likewise
dimension 7 with 3-dimensional quotient RP^3 — the numerology does not
single out the Lagrangian quotient.

## Scope notes
- This is a proved obstruction lemma (counterexample to the target's concrete
  Lagrangian realization), not a proof of the full target nor a vague idea.
- The pi_1 values and Hom computation are classical; the application blocking
  the stated blow-up-to-Lagrangian construction in this rigidity context is
  the new increment. Literature check (one consolidated search, 20 results)
  found no prior publication of this applied obstruction.
- Limitation: it refutes the named example/route, not the abstract existence
  claim for some other (M, N, Q); the volume-variety obstruction for the
  Gr(2,4) variant is supporting evidence, stated as argument rather than a
  second formal theorem.
