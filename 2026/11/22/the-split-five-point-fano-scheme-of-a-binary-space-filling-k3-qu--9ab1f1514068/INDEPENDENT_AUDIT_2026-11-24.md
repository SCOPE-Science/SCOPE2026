# Independent mathematical audit

## correctness

PASS

PASS for the complete corrected RESULT.md in repairs/1, not for the frozen embedded line list. The frozen third line X2=X0, X3=X0+X1 is false: on (s,t,s,s+t) the binary quartic restricts to s^2 t^2+s t^3, which is nonzero (yet vanishes at all three binary points). Its replacement X2=X0+X1, X3=X0 is forced by the frozen (0,1) RREF basis: (v2,v3)=(1,0) implies (v0,v1)=(1,1); the other two pairs and two zero-entry cells give the other four listed lines. I also used six different charts, the open nonvanishing coordinate minors, and independently computed their quotient dimensions over F2 by standard monomials: 3,3,2,2,3,2, respectively in lexicographic pair order. The substituted corrected lines give exactly that many distinct rational points on each chart. The evaluation map onto their product of residue fields is surjective by the Chinese remainder theorem and a dimension isomorphism, proving the scheme statement independently. A projective singularity test on all four coordinate patches also yielded the unit ideal everywhere. In the repaired proof the full scheme's tangent spaces vanish by adjunction on the smooth quartic, O(-2) for each geometric line, so the geometric census from the disjoint cells does suffice once reducedness is handled separately. All extension counts and the zeta formula follow. Replay: python -B /workspace/branches/independent_checks.py 1.

## originality

PASS

The surviving distinct finding is exhaustion of all geometric lines on this exact smooth quartic, not the list or incidence of the five base-field lines, the construction of the quartic, or rigidity of lines on smooth quartics in general. I compared both same-equation and coordinate-equivalent rational censuses, the defining primary construction, and stronger numerical line bounds and results on other quartics. The corrected geometric assertion is not covered by their stated conclusions.

## value

PASS

This is the geometrically smooth binary base example of a space-filling quartic construction, so the Fano scheme of embedded lines is a natural invariant of a specified, independently motivated K3. The geometric census rules out hidden extension-field lines that binary enumeration and the known line-incidence lattice could miss. It supplies all degree-one curves and their field of definition for arithmetic and intersection-theoretic use without pretending to determine the rest of the Picard group. Correcting an equation keeps this genuine increment intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
