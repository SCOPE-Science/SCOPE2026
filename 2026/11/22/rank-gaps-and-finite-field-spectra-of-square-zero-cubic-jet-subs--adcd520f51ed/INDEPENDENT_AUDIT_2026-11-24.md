# Independent mathematical audit

## correctness

PASS

Reconstructed the count in the scalar-fixing unital convention. Nilpotent generators have zero constant term; V and W=Sym²V give radical-action blocks B, Q and R=Sym²B. The composition equation is B²=0 and QB+RQ=0. For B of rank r write V=U⊕Z⊕X with B:X→U an isomorphism and Z representing ker(B)/im(B). Ordinary symmetric monomials give rank R=c_r in all characteristics, including squares in characteristic two, and R²=0. Q is arbitrary on X, forced on U by −RQ on X, and arbitrary with values in ker R on Z. Hence its dimension is rs+a_r(s−c_r)=H_{d,r}. Modulo im R the Z block gives all a_r→b_r maps, with q^(H−a_rb_r) lifts each. Radical rank is r+c_r plus that quotient-map rank; choosing its kernel and an injection from the quotient gives the stated factor. Choosing image, containing kernel, and an isomorphism counts B. Since b_r≥a_r, the intervals and successive gap formula follow, with admissible successive indices 0≤r<floor(d/2). This gives the d=6 and d=12 examples. For r>0 the number of admissible B is O_q(q^(2r(d−r))) and the Q count loses at least rs in the exponent relative to r=0; the stated concentration bound follows. Independent bounded replay for d=2 checked 1024 and 59049 substitutions, with spectra (1,21,66) and (1,104,840); from /workspace/branches/cf93377f-805f-4ae4-9e11-8bdac6eb7eaa/ run python3 repro_record3.py 2 and python3 repro_record3.py 3 (outputs in repro_q2.txt and repro_q3.txt). Frozen verify.py was inspected, not run.

## originality

PASS

On bounded evidence the exact labeled symmetric-square rank census, its gap geometry and concentration are distinct. The strongest prior is very close in method, but counts a different quadratic multiplication and has a different rank polynomial and forbidden ranks. No novelty is attributed to the general dual-number intertwiner technique.

## value

PASS

The commutative cubic-jet radical is a natural first nonlinear truncation, and composition-square-zero is a natural nilpotence constraint. The all-characteristic coefficient count classifies not only existence but exact fibers and genuinely different holes in the full rank support. The unchanged linear-algebra method is not itself the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
