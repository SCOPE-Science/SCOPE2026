# Independent mathematical audit

## correctness

PASS

For X_a(u), telescoping p^h=1+sum_{j=1}^h phi(p^j) gives mean k+1 on the units. Let P_j be averaging within reduction classes modulo p^j and P_0 averaging over all units. The centered data matrix is H=M(sum_{j=1}^k P_j-kP_0), symmetric, so the covariance is H^2/M. The orthogonal difference of the j-th and (j-1)-st images sees eigenvalue M(k-j+1)^2 of the covariance, with dimension the difference of the reduction-image dimensions. Constants form the kernel. Counting products with min(i,j)=l in P_i P_j=P_min(i,j) gives the stated entry formula. For the empirical law, masses at j^2 with j<k agree, the deficit at k^2 is 1/(pM), and the missing tail is (p-1)/(pM); their sum is exactly the extra mass 1/M at zero. The empty positive spectrum for p=2,k=1 and the missing first contrast level when p=2 are correctly treated, including the condition number when there is a positive spectrum. The uploaded integer/rational checker was inspected read-only; the all-parameter result follows from the proof.

## originality

FAIL

Zhao–Cao's Dirichlet-character Menon identity already gives the full Fourier diagonal of the unit-indexed data kernel for every modulus, not merely the scalar first moment. Centering and squaring make the proposed covariance spectrum a direct corollary. The arithmetic entry formula and the exact total variation are routine consequences of this same diagonal, not a surviving independent claim.

## value

FAIL

The covariance model and comparison distribution are natural, and the calculation is a useful exposition. But the proposed exact invariant mechanically follows from the known full data-kernel Fourier diagonal, and the finite TV identity just counts the mass transferred to the constant mode. No separate unknown and independently useful exact invariant remains in the frozen contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
