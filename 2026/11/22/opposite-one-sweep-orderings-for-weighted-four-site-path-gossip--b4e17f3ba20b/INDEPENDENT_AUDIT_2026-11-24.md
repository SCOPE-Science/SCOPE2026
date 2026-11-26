# Independent mathematical audit

## correctness

PASS

Reversal transposes the product and the two outer factors commute, leaving two singular-spectrum classes. In the orthonormal disagreement basis whose first two vectors are the unit outer-edge differences, the outer updates are diagonal, with only their own entries changed from 1 to α=1−2p and γ=1−2r. The central update Q is I−qvv^T, with |v_1v_2|=1/2. In the difference between the two squared Frobenius norms all terms except the interaction of those two coordinates cancel, giving Q_12²(1−α²)(1−γ²)=δ. The second Gram coefficient is the squared Frobenius norm of the three-dimensional adjugate, and the same comparison gives δ: the outer adjugate diagonals are (1,α,α) and (γ,1,γ), while adj(Q)_12=−Q_12. Adjugate identities hold also when a rate is 1/2. Gram determinants agree by multiplicativity, giving δλ(1−λ). All eigenvalues of each disagreement Gram are below 1 since norm preservation would require all three edge equalities on a mean-zero input. The batched factor β is positive since (in the batched order) some endpoint entry is zero whereas J has all entries positive. The serial polynomial is positive throughout [β,1), excluding a Gram root there, and proving W_S<W_B. The arithmetic case and common transfer polynomial agree; cyclic determinant invariance requires no nonsingularity. The proof and exact replay handle general strengths, not just the numerical grid.

## originality

PASS

Credit the known equal-strength path isotropic specialization and transfer-spectrum precedent. The stronger remaining result is the strict opposing choice of one-sweep optimum across the full open cube of strengths on the path, with the cubic identity; neither the half-strength path theorem nor the weighted star theorem covers this statement.

## value

PASS

The shortest path with a nontrivial scheduling choice and disjoint interactions exhibits disjoint optimal schedule classes for two natural disagreement objectives for every interior strength triple. Identical periodic transfer eigenvalues cannot detect the strict, exactly quantified one-sweep design tradeoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
