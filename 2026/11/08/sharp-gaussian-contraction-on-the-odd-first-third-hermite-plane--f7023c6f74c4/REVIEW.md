# Independent mathematical audit

## correctness

PASS

On real E=span(H1=x,H3=x³−3x), exact Gaussian Wick contractions give fourth moments (3,6,42,324,3348) and input squared norm 1+6t². OU attenuation gives K_r(t)=r²N_r(t)/(1+6t²)², r=ρ² and N_r=3+24rt+252r²t²+1296r³t³+3348r⁴t⁴. Differentiation gives K_r′=24r²q_r(t)/(1+6t²)³. The exact quartic discriminant is −110224800r⁶P6(r²); independently verified P6 has zero positive roots by exact SymPy Sturm counts, hence q_r has precisely one positive and one negative simple real root for r>0, and the unique positive root is the global maximizer. Monotonicity in r, explicit strict inequalities at 1/3 and 1/2, and exact degree-ten resultant factor B(r²) with one root in (1/9,1/4) give unique contraction r*=0.413963744988… and ρ*=0.643400143758… >1/√3. At ρ=0, zero operator; real inputs and probabilists’ Hermite normalization are essential. The assigned algebraic certificate script was inspected and key discriminant/derivative/Sturm results independently recalculated.

## originality

PASS

Nelson–Gross unrestricted Gaussian hypercontractivity gives sufficient bound ρ≤1/√3 on all L² inputs; it does not calculate this restricted first/third odd Hermite two-eigenmode norm, mixed unique extremizer or strict larger cutoff. Resultary searches found other exponent-pair or other chaos-subspace optimizations but no dominating same E,L²→L⁴ theorem. Weissler 1979 is potentially relevant but its full text could not be accessed after authorized institutional route returned vpn_disconnected, so this best-of-knowledge PASS explicitly retains material historical priority risk.

## value

PASS

The first nontrivial real odd two-eigenmode OU space is a canonical restricted hypercontractivity problem. Its exact sharp mixed-mode norm, uniquely optimizing coefficient ratio, and algebraic contraction threshold quantify an improvement over full-space Nelson and are not a routine restatement of generic hypercontractivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
