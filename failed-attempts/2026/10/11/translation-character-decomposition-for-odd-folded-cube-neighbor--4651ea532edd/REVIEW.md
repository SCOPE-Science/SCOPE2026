# Independent mathematical audit

## correctness

PASS

Reconstructed graph as T_n=F2^n/<1> with open-neighborhood facets D-translates, D={coordinate classes e_i}. Two distinct neighborhoods meet in zero or two vertices; unique center for all >=3-vertex faces gives a valid two-dimensional collapse. Standard cube two-skeleton antipodal covering and Matsushita even-walk fundamental-group theorem give simple connectivity for odd n; Euler count yields reduced H2 rank 2^{n-3}(n²-5n+8)-1 and no other reduced homology. Every nonzero translation is a free vertex involution: class of e_i+e_j preserves exactly 2^{n-2} edges with orientation reversal, giving reduced Lefschetz trace 2^{n-2}-1; others -1. Fourier inversion using Krawtchouk K2 gives exact reported multiplicities, including Clebsch n=5 weights 0,2,4 dimensions 6,1,3. Independently enumerated n=3 and n=5 face vectors and all signed fixed-face traces; inspected source verify_translation.py and verify_local.py. The theoretical proof, not finite enumeration, is what covers every odd n.

## originality

FAIL

There is an EXACT translation-equivariant simplicial isomorphism to a published hypercube Čech complex, not merely similar Betti numbers. Put m=n-1 EVEN; represent each antipodal class by x in F2^m with last coordinate 0. Folded open-neighborhood facets are translates of D={e_1,...,e_m,ones_m}. The invertible F2-linear map A=I+J (J all-one matrix) has A²=I because m is even, and A(D)=ones_m+{0,e_1,...,e_m}. Hence the entire folded complex is isomorphic, with its translation action conjugated by A, to the intrinsic radius-one closed-neighborhood Čech complex of Q_m. The PUBLISHED full hyperoctahedral H2 character theorem for Q_m explicitly determines the entire T_m-restricted character, and its original character gives exactly these even-weight multiplicities after A-dual relabeling. Another published source writes the translation multiplicities explicitly. Therefore every assertion of the final translation-module decomposition is a transported special case of stronger published results; novelty decisively fails. The preexisting nonequivariant folded wedge calculation also already covers the total H2 dimension.

## value

PASS

The complete rational translation representation of a natural nonbipartite folded-cube graph complex is an interpretable object, and the weight-stratified multiplicities would be worthwhile if new. Homological concentration, rational character and symmetry decomposition are substantial natural invariants; rejection here is due to exact prior coverage, not lack of mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
