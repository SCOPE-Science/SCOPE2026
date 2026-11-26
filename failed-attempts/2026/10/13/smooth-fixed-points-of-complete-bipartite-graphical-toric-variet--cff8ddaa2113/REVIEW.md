# Independent mathematical audit

## correctness

FAIL

The literal biconditional in RESULT.md line 7, also repeated in SLOGAN.txt, omits a necessary restriction. Orient every edge of K_{2,2} from A to B. There are exactly two source layers, A and B, so all strictly interior layers are vacuously singletons. But its Hasse graph is K_{2,2}; the three-dimensional normal cone has four facets, so it is neither simplicial nor smooth. The following sentence about at least four layers does not follow from the stated singleton condition. The proof and verifier actually exclude the two-layer case. With at least three layers, a nonsingleton interior layer yields a four-cycle with the two neighbors, and singleton interiors yield a tree. Three layers with singleton interior would leave the middle color class of size one, excluded here. Thus the correct test is at least four layers AND singleton interiors. Tree edge differences are a basis of the root lattice, with the dual basis giving rays of the normal cone. The count and EGF for this corrected class check out: even lengths have one endpoint of each color; odd lengths force the entire non-endpoint color into ordered singleton blocks and split the residual endpoint color into two nonempty blocks. In the EGF the even part starts with xy and the odd parts start with xy times x or y. The frozen output for six pairs is consistent with the corrected counts; the verifier uses len(blocks)>=3 and does not verify the literal unqualified condition. Frozen code inspected, not executed.

## originality

FAIL

A distinct catalogue record explicitly supplies the corrected layer characterization and the same central all-parameter count, in simple-vertex language, as part of a stronger degree-spectrum result. Simplicity is equivalent to the claimed toric smoothness in this graph and lattice: a simple vertex has the tree cover graph, whose primitive edge differences give a basis. Reindexing j=r-1 identifies the finite sum and both odd-endpoint terms verbatim in mathematical content. The EGF and normalized balanced limit are elementary transforms of those exact coefficients, not a surviving independent result. This is a statement-level finding of equivalent coverage, not a finding about historical priority.

## value

FAIL

The smooth locus at fixed points is a natural invariant, but the corrected census is already exactly available for simple vertices, and the EGF and balanced normalization are routine encodings of it. At this scope there is no separate valuable new mathematical remainder to repair; in particular the record gives no classification away from fixed points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
