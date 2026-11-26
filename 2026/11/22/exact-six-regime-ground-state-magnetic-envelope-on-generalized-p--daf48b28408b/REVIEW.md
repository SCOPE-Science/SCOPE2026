# Independent mathematical audit

## correctness

PASS

On a labeled n-cycle, the two previous inner colors and the previous outer color suffice to count each of the three types of edge once as the next cell is appended, and the number of preferred colors on that cell. A closed walk with a fixed starting index gives exactly the cyclic cell constraints. For n≥5 the unoriented step-two edges do not double-count. I independently computed the minimum cycle mean at h=-1,0,5/4,7/4,3 using exact integer arc costs and all start states and lengths 1 through 27. The resulting means are 1/2,0,-1,-3/2,-3. This is a proof for walks of arbitrary length: any closed walk is a concatenation in edge counts of simple directed cycles, each of length at most 27, and its mean is a convex combination of theirs. Interpolating lower bounds at consecutive critical fields and using 0≤K≤2n on the outer rays gives the full six-line bound, per cell. Independently enumerating 1-, 4- and 5-cell words produces witnesses at (period,P,K)=(4,2,0),(4,0,2),(5,0,4),(4,1,4),(5,3,6),(1,3,2). These periods tile every n divisible by 20 and adjacent witnesses attain jointly at ties. Truncation and wrap-around change the excess energy by O_h(1). At any differentiability field, the affine line from an arbitrary minimizer touches G_n, so its slope lies between the two secants at h±epsilon; take n→∞ and then epsilon→0. For n divisible by 20 this argument is exact inside each interval, including the two open rays. It establishes occupations per cell, not per vertex.

## originality

PASS

The minimum-mean-cycle calculation is a method, not itself the discovery. The surviving distinct result is the exact family-wide envelope with its five critical fields, commensurate equality and slope plateaux. The closest checked exact prior is for the same Hamiltonian on GP(10,2) and has a different interior diagram. The closely related Potts transfer matrices and weighted chromatic results do not furnish the required envelope on this graph sequence at fixed H/J.

## value

PASS

This solves the zero-temperature magnetic response of a named infinite family rather than tabulating an isolated periodic graph. The extra intermediate plateau and the split between its two transition fields distinguish the limiting response from the natural dodecahedral member. The finite witnesses and universal lower bound give exact energies at a useful sequence of finite sizes as well as rigorous asymptotic occupations elsewhere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
