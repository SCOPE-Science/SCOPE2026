# Independent mathematical audit

## correctness

PASS

The derivative formula has been reconstructed: for u=Ax/||Ax||, t=u^TA^{-1}u, reflection R=I-2uu^T, RDG_A=(I-uu^T)-(t/2)A, symmetric. Nonexpansivity of the derivative iff 4I-tA-2uu^T is PSD. Normalizing minimal eigenvalue1 and k=max, k<4, Sherman–Morrison gives 2 E[h/(4h-t)]<=1 for h=reciprocal eigenvalues with mean t. This integrand is strictly convex; chord bound is attained by extreme eigenspaces, producing Q_k(t)=3kt²-4(k+1)t+8. Its constrained minimum changes sign at k=2+sqrt(3), with an exact critical eigenvector. At k=4 a rank-2 determinant -1/3 witnesses expansion, for k>4 an extreme eigenvector suffices. Homogeneity/continuity at zero and path integration give global iff, with strictly smaller modulus below threshold. The radial square identity subtracts 3(x^TAx)^2/(4x^TA²x)>0 for every nonzero x.

## originality

PASS

Best-of-knowledge new result is sharp all-dimensional pairwise nonexpansiveness threshold for the standard quadratic subgradient/Polyak projector. Bauschke et al. 2014 Proposition7.1 already gives the formula; its Section8 nonexpansivity examples do not give the extreme-eigenvalue condition-number classification. 2013 quasi-Bregman fixed-point contraction is weaker; Pauwels gives general Lipschitz estimates. Resultary returned identical record as a self-match, unrelated conditions on optimization algorithms otherwise.

## value

PASS

Pairwise nonexpansiveness versus radial contraction is a significant distinction for subgradient projection operators. A universal sharp spectral phase boundary and explicit extremal two-dimensional obstruction give meaningful classification for a classical nonlinear map in arbitrary dimension, not a reparameterization of a known theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
