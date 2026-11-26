# Independent mathematical audit

## correctness

PASS

I reduced to moduli, ordered the two opposite-pair means and the within-pair spreads, and independently expanded the squares of the four edge differences. In centered coordinates (t,x,y) this gives denominator 4(t^2+x^2+y^2); the point, three-vertex, and whole-graph radii give the frozen six numerator branches. For x<=t/2, bounding the negative x^2 coefficient by its value at t/2 gives strict positive slack away from zero, with y=t+v on the high-y branch. For x>=t/2 and y<=t/2 the normalized numerator is the Rayleigh form whose upper-left block is [[5/72,1/6],[1/6,1/2]], with a decoupled y coefficient 1/9. Its characteristic polynomial is (144z^2-82z+1)/144, and its largest eigenvalue has the admissible simple ray (1,beta,0). For the middle and high y branches, shifting x to t/2+u and y to t/2+v or t+v gives the printed slack matrices. My exact expansions gave the leading two-by-two determinants (127-sqrt(1537))/13824 and (383+sqrt(1537))/10368, with positive first pivots, positive third diagonal, and nonnegative couplings to v. They give strict slack for each nonzero cone vector, including ties at branch boundaries. Subtracting the minimum value on the unique ray yields exactly the claimed profile and arbitrary nonnegative offset. Equality in the modulus reduction forces phases to agree across every positive-positive edge; the extremizer has connected positive support even at zero offset, so this proves necessity and sufficiency for complex data. The numerical value 0.7463084686187879 agrees. The bundled checker was inspected, not run; its sampled inequality checks are not the proof.

## originality

PASS

The supported distinct result is the individual-signal quadratic edge-variation norm and all complex equality cases for centered ordinary balls on C4. Closest available results address other exponents, other graph families, a different norm or a two-input map. Priority is not certified.

## value

PASS

The four-cycle is the smallest simple cycle and a natural non-complete, non-star test for exact graph maximal-variation inequalities. Its quadratic constant is strictly below its first-variation constant, contrary to transferring the finite-graph p=1 pattern directly. The exact value and connected-support equality ray give a useful benchmark for sharp graph-specific bounds and for testing broader conjectures. The result neither claims a full cycle theorem nor conflates the energy with a strong vertex norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
