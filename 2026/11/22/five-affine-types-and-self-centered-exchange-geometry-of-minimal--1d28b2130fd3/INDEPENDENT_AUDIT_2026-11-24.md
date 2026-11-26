# Independent mathematical audit

## correctness

PASS

The independent exhaustive replay checked all 8,191 nonempty subsets. A connected dominating set is indeed upward-closed: every added vertex is adjacent to a member of the original dominating set, so the enlarged induced subgraph stays connected as well as dominating. Single-deletion minimality is therefore equivalent to inclusion-minimality. Counts by sizes 1–13 are (0,0,0,260,975,1625,1703,1287,715,286,78,13,1), with exactly 260 deletion-minimal sets, all of size four. The replay used unrestricted one-in/one-out exchanges and obtained 1,911 edges; all-source BFS visits all 260 vertices and every eccentricity equals four. The affine maps with quadratic-residue multipliers preserve differences and hence both the original graph and exchange adjacency. The computed orbit and shell rows are 0x17: 78,14,(1,14,79,115,51); 0x1b: 39,20,(1,20,70,116,53); 0x2b: 78,14,(1,14,70,132,43); 0x2d: 39,12,(1,12,74,128,45); 0x8d: 26,15,(1,15,69,133,42). Thus the polynomial and all five exchange rows match the frozen claim, not just a summary of minimum cardinality.

## originality

PASS

The exact result supported as distinct is the joint inclusion-minimal census and full metric/orbit classification of its one-swap graph. The same graph has a close same-day exact reconfiguration result for locating domination, but that has a different feasible family and different edge counts. The general enumeration methods do not supply these exact outputs or structural class. No historical priority is inferred beyond the bounded evidence.

## value

PASS

Connected domination asks for a connected backbone reaching every vertex, a natural invariant of a canonical finite-field graph. A reconfiguration researcher would need exact swap reachability, eccentricities, and their symmetry types on this host independently of its minimum size. In particular the nonregular but self-centered exchange graph is an exact geometric feature, and the uniform size of all inclusion-minimal sets rules out larger minimal backbones. These are not read off the minimum value or the graph's construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
