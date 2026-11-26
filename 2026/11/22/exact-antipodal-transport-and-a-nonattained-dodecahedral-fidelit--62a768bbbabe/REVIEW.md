# Independent mathematical audit

## correctness

PASS

Reconstructed the adjacency spectra and parity factors from exact Cartesian coordinates: with antipodes ordered in pairs, adjacency has blocks (B,C;C,B), and B+C and B-C have exactly the even and odd characteristic-polynomial factors in the table. Independently checked the unique graph-distance antipode for each vertex and the degree-three geometric eigenspace (eigenvalues 1, 0, sqrt(5), sqrt(5) on cube, octahedron, icosahedron, dodecahedron). Its projector has entries 3(u·v)/(N r^2), with r the vertex radius, so strict Cauchy–Schwarz excludes PGST for every distinct non-antipodal pair; the tetrahedron follows from A=J-I. The bounded exact reproduction is replayable with python -B /workspace/branches/platonic_reconstruction.py (SymPy); it passed the four parity, shell and geometric projector checks and both derivative and peak-value identities. The uploaded scripts were inspected but not run. Vertex transitivity gives diagonal weights m_lambda/N and hence the stated amplitudes. For the dodecahedron the two frequencies 1 and sqrt(5) have dense joint phase torus; strict convexity in cos(sqrt(5)t) reduces to endpoints. The negative endpoint has squared numerator at most 144, and the positive endpoint polynomial has only one interior stationary point x=-1/2, where the derivative changes from positive to negative and the squared numerator is 243. Equality additionally requires sqrt(5)t/(2pi) integral, impossible for nonzero rational t/(2pi) giving cos t=-1/2. For icosahedral antipodes odd Pell indices give q even, p odd, p-sqrt(5)q=1/(p+sqrt(5)q); evaluating at t=pi q gives the stated cos^4 limit. Exact transfer would require 6t and 2sqrt(5)t to be multiples of 2pi, which forces t=0 and fails the parity-phase condition. The single-frequency cube, octahedron and tetrahedron attain the stated values at pi/2, pi/3 and pi/4.

## originality

PASS

The nonattained dodecahedral antipodal supremum 243/400 survives statement-level comparison and needs an actual joint-phase optimization, not a known upper bound or a generic transfer criterion. The classification combines older cases and general tools with graph-specific conclusions; it is not credited as five new cases. Checked narrow and broad result statements for the exact uniform-adjacency model. No compared distinct source supplies the dodecahedral sharp cap or the complete classification; priority remains best-of-knowledge. The cube and octahedral cases are not original contributions.

## value

PASS

Uniform adjacency dynamics on the canonical Platonic skeletons give a natural finite benchmark. The exact nonattained subunit cap for the dodecahedron is not a norm estimate, a table lookup or a consequence of excluding perfect transfer. Its sharp value distinguishes this graph from proper PGST on its icosahedral dual, resolving an operationally meaningful limit in the fixed Hamiltonian model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
