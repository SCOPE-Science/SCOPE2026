# Independent mathematical audit

## correctness

PASS

Synchronous binary majority on 14-vertex cube-corner (8 degree3) and cube-face-center (6 degree4) incidence graph was reconstructed from explicit 24 edges. Degree3 corners take strict majority; degree4 faces retain incumbent at a 2:2 tie. Writing F(c,a)=(C(a),R(c,a)) reduces two-periodic points bijectively to 64^2 face-word pairs, of which exact enumeration yields 412 phases=46 fixed+366 primitive two phases=183 two-cycles. Independently computed all 2^14 integer states from adjacency, their first-entry/period arrays: t=0:(46,366),1:(2122,4682),2:(3360,1536),3:(2136,480),4:(1368,96),5:(192,0), hence sharp F^7=F^5 and witness with tau=5. Independently constructed 48 coordinate-signed-permutation graph automorphisms; verified commutation on every state and grouped fixed points into 6 classes [1,1,8,12,12,12], and unphased two-cycles into 13 classes [1,4,6,8,8,12,12,12,12,12,24,24,48], agreeing with the claim. This is exhaustive on this *fixed* graph, not extrapolation to other graphs. Inspected separate repository verify_faces.py and original RESULT.md.

## originality

PASS

Best-of-knowledge novel complete fixed canonical 14-vertex tie-retaining majority dynamics classification. General theorems that undirected symmetric threshold networks ultimately have period <=2 are background, not a census of exact basins/transient depth or orbit classes on this incidence graph.

## value

PASS

The rhombic dodecahedral graph is a canonical Catalan-solid incidence graph exhibiting both odd and even degrees; tie retention on exactly its degree-four shore creates nontrivial memory. The complete exact recurrent and basin distribution, sharp five-step transient cutoff and octahedral symmetry reduction give a motivated dynamical fingerprint useful for contrasting polyhedral duals. A finite 14-vertex classification can be mathematically valuable without a general family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
