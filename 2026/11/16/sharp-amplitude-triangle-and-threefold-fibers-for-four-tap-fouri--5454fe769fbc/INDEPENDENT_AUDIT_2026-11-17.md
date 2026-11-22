# Independent mathematical audit

## correctness

PASS

Fix global phase a=A>0 and R3 fixes d=De^{iδ}. Let U=Ac,V=d conj(b), z=U+V=R2, k=(D²-A²)e^{2iδ}, |U|=AC=r, |V|=BD=s. Directly expanding first autocorrelation verifies Ad R1=A²e^{2iδ}conj(z)+U(z-U)+k conj(U). When z!=0 two circle intersections at most; equality of their R1 values equivalent to (s²-r²)z=k conj(z)^2. Nondegeneracy requires |r-s|<|k|<r+s (after solving |z|=|s²-r²|/|k|). When z=0, r=s and U constrained to circle; cubic U³+AdR1 U-kr²=0 bounds fiber by three, and two distinct nontrivial solutions occur iff 0<|k|<2r. Triple requires R1=R2=0 and |k|=r=s, achieved by three cubic roots. Explicit independent exact symbolic computation for j=0,1,2 verified all R0..R3=(65/4,0,0,2) for f_j=1-(3/2)ω^(-j)z+3ω^j z²+2z³ with ordered squared moduli (1,9/4,9,4). Nontrivial equivalence excludes reversal except at A=D,B=C, handled separately; lengths <=3 follow a single real-linear middle-tap equation. Completeness relies on the all-case analytic two-circle/cubic proof, not finite checks.

## originality

PASS

PASS is confined to the all-positive four-magnitude necessary-and-sufficient triangle, global three-phase upper bound, and exact triple locus. Beinert–Plonka already gave 2016 nonuniqueness for lengths>3 and a 2020 four-tap threefold example. Their explicit primary 2020 Example 24.3 is acknowledged and NOT counted as new. General autocorrelation factorization and phase retrieval constructions do not supply the four-magnitude sharp classification in inspected results.

## value

PASS

Given a natural signal-recovery side-information model, the exact open region deciding ambiguity and the sharp maximum-fiber locus are useful structural statements: they identify when positive four-tap data provably do or do not determine phase. This goes beyond old isolated examples and generic almost-everywhere assertions while remaining a self-contained classification; no unsupported downstream stability claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
