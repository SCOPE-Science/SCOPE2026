# Independent mathematical audit

## correctness

PASS

Slater and stationarity yield clip(v/s) with s≥1; the unconstrained box projection suffices if it is ball feasible. Otherwise the squared norm of clip(v/s) drops strictly wherever it reaches the target with a nonzero free coordinate; a plateau at the target would require that all free inputs vanish and that the original box projection already be ball feasible. For a strict active pattern with k saturated outputs, the free output is √(r²−k)v_J/||v_J||₂ and its Jacobian is s⁻¹(I−uuᵀ). Apart from clipping coordinate planes, the switch on each clipping region lies in a level set of its clipped squared norm; at an active tie the saturated i satisfies (r²−k)v_i²=∑_{j in J}v_j². These are null sets for r²<n, with the r²=k degeneracy forcing all free inputs to vanish. With a=|u_i|, the maximum row sum is 1−a²+a∑_{j≠i}|u_j|; its Cauchy–Schwarz bound is attained by equal tail magnitudes whenever a lies in the stated interval. The interval is feasible since c_k>1/√m, and the change 2a²−1 gives the single clamped maximizer. One free coordinate contributes zero derivative. Euclidean nonexpansiveness ensures Lipschitz regularity; mollification with the a.e. derivative bound gives the global ℓ∞ bound. Conversely choose a strictly feasible equal-tail vector, scale the free input by s>1 and make the saturated inputs strictly larger than s. Test along the signs of the chosen row, then take s↓1 and approach any capped maximizer from inside; the identity regime separately gives one. At r=√5 in n=13 only k=0 and k=1 can beat the unrestricted bound for m≤11; both are upper-capped and F₁>F₀ reduces to 7>4√3. An independent arithmetic check gives excess 0.000500015579. For r≤1 only ordinary ball clipping is needed; at r↑√n the feasible intervals collapse to the equal-magnitude vectors and the largest limit is 2−2/n, while at redundancy coordinate clipping gives one.

## originality

PASS

The ball-only modulus and box coefficient are known, and generic convex-projector bounds are available. The new content supported by the comparison is the exact constrained mixed-face maximum, including the strictly winning capped face and the approach to redundancy.

## value

PASS

Individual-coordinate error budgets and a joint energy cap naturally coexist. The exact global perturbation factor for the associated Euclidean projector, not merely an evaluation algorithm, quantifies their interaction. The tiny thirteen-dimensional gap is useful as a counterexample to the no-saturation simplification, not for its size, and the actual jump at redundancy separates stability of the sharp modulus from continuity of the sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
