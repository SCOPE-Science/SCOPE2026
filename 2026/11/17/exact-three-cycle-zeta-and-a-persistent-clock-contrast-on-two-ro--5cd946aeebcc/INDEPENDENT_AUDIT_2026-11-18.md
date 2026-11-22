# Independent mathematical audit

## correctness

PASS

For synchronous threshold-one three-state Greenberg–Hastings on the simple-neighbor graph with vertices (row∈Z2,column∈Zn), n>=3, Moore adjacency is all distinct sites at horizontal distance≤1 except self; the two vertical offsets collapse to one opposite-row site. The only third-return nonzero histories must advance 0→1→2→0 everywhere; otherwise the connected cycle constraints yield the all-zero fixed state. Thus each color in each column must have a successor-state neighbor, an exact three-slice local condition, and global labelled period-three states biject with length-n closed walks of a fully specified 81×81 overlapping-column adjacency. Independently constructed the 81x81 binary transfer from the literal update, counted exactly 585 directed edges and factored det(xI-T)=x^74(x^2+3x+9)^2(x^3-6x^2-9x-18). Its Newton/trace identity yields S_n=a_n+4*3^n*cos(2πn/3), a_0=3,a_1=6,a_2=54, a_n=6a_{n-1}+9a_{n-2}+18a_{n-3}; the cubic Perron root ~7.516067898568. Independent ORIGINAL-dynamics enumeration of all 3^(2n) configurations at n=3,4,5 gave 540,3024,23490 third-return states, exactly the transfer counts; transfer counts also independently checked n=6,7,8. Since 7.516...<9, the fraction of immediate period-three globally rotating states tends to zero. Disjoint pairs of columns give at least floor(n/2) independent rainbow triangles with failure (7/9)^floor(n/2), proving a perpetual local three-clock with probability tending one (not globally periodic). Infinite family rests on exact finite matrix identity plus an elementary independent local-obstruction probability bound; finite samples alone do not imply the result.

## originality

PASS

PASS best of knowledge: prior broad 3-color GHM work characterizes synchronization and activity via universal coverings on arbitrary connected graphs, but does not count all labelled immediate three-cycles for the two-row MOORE simple graph or compute degree-seven spatial zeta/persistent-local versus globally-periodic contrast. Durrett–Steif's 1991 GHM studies nearest-neighbor integer lattices, one-dimensional entropy and finite boxes, not this quotient. The indexed Wireworld two-row torus theorem is a four-state conductor rule with eight-offset incidence MULTIPLICITY, hence a different rule and a different characteristic polynomial. No reviewed stronger same-object theorem implies the new all-n count.

## value

PASS

Complete exact all-length temporal-three orbit census and spatial zeta for a natural minimal-width excitable lattice plus a sharp qualitative contrast: random initial configuration almost surely contains a perpetual rotating 3-cycle at some local triangle, yet chance of global immediate three-return vanishes exponentially. This answers two distinct natural questions—local pacemaking and synchronized global clocks—using an exact finite-state invariant and meaningful asymptotic distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
