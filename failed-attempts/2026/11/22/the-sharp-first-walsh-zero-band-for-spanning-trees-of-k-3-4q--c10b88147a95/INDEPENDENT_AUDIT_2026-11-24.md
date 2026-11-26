# Independent mathematical audit

## correctness

PASS

For the unnormalized Walsh coefficient on labelled edge sets, signed matrix-tree weights give exactly the signed tree sum. The deleted left vertex leaves an invertible right diagonal block with entries d in {±1,±3}, so the stated two-dimensional Schur test is equivalent to vanishing. Substituting all sign patterns gives the stated 3Q matrices: no negatives gives zero, singles give rank one with distinct kernels, doubles have determinant 180 and positive diagonals, and the triple has determinant 300 and positive diagonals. The base B is positive definite. Summing gives strict definiteness when 4|S|<n, and at equality singularity exactly when every nonzero local Q is a single of the same left type. The q right neighbors are distinct, q>=1 makes the three left choices disjoint, and characters diagonalize the specified counting convolution. The exact analytic proof covers every n>=2; the nested checks/verify_k3n.py was inspected as corroborative code, not executed or needed for the general theorem. The direct independent derivation from the earlier pointwise formula is given below.

## originality

FAIL

An earlier distinct Resultary record on exactly the same K_{3,n} Walsh coefficients gives a pointwise formula from which both the zero band and the equality supports follow directly by coordinatewise comparison. The overlap is mathematical implication, not a title match: the earlier Finding concerns projection norms, but its Proof §1 supplies the decisive identity for every sign assignment.

## value

FAIL

The low-degree invertibility question is natural, but for this fixed graph family the proposed standalone contribution reduces to bounding each coordinate of an already known coefficient formula by its smallest possible single-column value and checking equality of the three singleton sign patterns. The counting and Fourier consequence are immediate once that is done. It supplies neither a new nontrivial invariant calculation beyond that direct deduction nor a broader rigidity mechanism or graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
