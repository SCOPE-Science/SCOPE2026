# Independent mathematical audit

## correctness

PASS

On a labelled simple cycle of length at least three, the two neighbors are distinct and the centered triple checks are exactly the two feasibility conditions. Summing b−1+h(a,b)−h(b,c) telescopes to w−n; all 20 allowed triples have nonnegative reduced cost and precisely the 16 displayed edges have cost zero. Thus the all-one word attains the minimum and the critical closed walks count all minimizers without quotienting rotations. Independently, merging identical successor rows first gives classes {00,10}, {01}, {02}, {11,21}, {12,22}, {20}; the resulting rows for {01} and {02} then coincide. On the five quotient classes A={00,10}, G={01,02}, D={11,21}, E={12,22}, F={20}, the equations for I−xZ reduce by unit-pivot elimination to A=xG, F=x(A+G), E=xF, D=G+xA and (1−x−2x³−x⁴)G=0. The eliminated directions contribute only zero eigenvalues. The trace identity gives the logarithmic series; the length-one and length-two traces are both 1 and must be removed. A fresh brute force check using the feasibility predicate alone gave weight n and multiplicities 7, 13, 16, 31, 64 at lengths 3–7. The quartic has a primitive nonnegative companion matrix (a loop and a spanning directed 4-cycle), so the unique leading eigenvalue is positive and simple, and its trace contribution has coefficient 1. Replay: reconstruct the zero-edge rows from RESULT.md lines 35–71, then use the quotient equations or the integer determinant recipe. The finite check is corroboration only; the result does not count nonoptimal words or dihedral orbits.

## originality

PASS

The known minimum n and TPRDF definition are credited; the independently compared advance is the complete multiplicity of indexed minimizers, including the quartic recurrence and generating function. No inspected equivalent, dominating result, or exact independent table covers it. This is a bounded best-of-knowledge judgment.

## value

PASS

The known optimum fixes only the cost. This count determines the degeneracy of optimum defensive assignments on the canonical degree-two graph, resolves all lengths, and gives an explicit growth rate and leading constant. The critical transition description is also independently usable to generate or recognize all optimum labelings, not just a list of numerically reproduced counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
