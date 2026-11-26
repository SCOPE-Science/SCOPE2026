# Independent mathematical audit

## correctness

FAIL

Assertion 1, RESULT.md line 12, is false as written: irreducible does not imply degree three. Over F_2 take (a,b,c,d)=(1,1,0,1). Then ad−bc=1 and f(T)=T²+T+1 is irreducible, but e_2²=e_2 gives a nonzero idempotent. Thus the issue persists even among perfect tables. The proof at lines 44–48 wrongly infers c≠0 from unqualified irreducibility. The exact correction would be ‘f has degree three and is irreducible’: c=0 gives a fixed line at infinity for a perfect table, and for c≠0 the finite fixed lines are the roots of f. When the cubic is irreducible, f(d/c)=(ad−bc)/c is nonzero, implying perfectness. With the degree condition the counts and group calculation do check: Frobenius orbits give (q−1)(q³−q)/3 tables; independence of the two squares forces all natural-basis changes to be monomial; a fixed antidiagonal change would give a root s, and the only nonidentity diagonal changes have s³=1, t=s² and a=d=0. The exceptional noncube ratios give 2(q−1)²/3 tables, exactly one orbit, and Burnside yields the stated class formulas. The frozen verify.py was read, not run. Its determinant and c≠0 guards (lines 51–60 and 79–87) mean the finite tests do not test bare irreducibility as stated.

## originality

FAIL

The complete K=0 column of a distinct published joint-law record covers the marked-table fraction and determines the exact filtered class counts and automorphism dichotomy directly by orbit–stabilizer. The degree-corrected criterion is the immediate affine version of the fixed-line cubic already used there. The other record is dated later; this is demonstrable equivalent coverage, not a priority or provenance judgment. Correcting the missing degree condition would not leave a new substantive result to repair.

## value

PASS

The exact census and distinction between marked frequency and unmarked class count answer useful structural questions over all finite fields, including the single exceptional symmetry class. This assessment concerns the mathematical content of the census, not a claim that the incorrect degree-free assertion is useful or that the covered corrected remainder merits repackaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
