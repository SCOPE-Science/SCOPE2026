# Independent mathematical audit

## correctness

PASS

Uniformity of both marginals forces p11=p22=q/2 and p12=p21=(1-q)/2. For J=[[0,1],[-1,0]], L=J U J^T; conjugating any word by J exchanges U and L. For a word P and its exchanged word the average Gram matrix is (tr(P^T P)/2)I, by the two-dimensional identity for symmetric matrices G+J G J^T=(tr G)I. For P=U² the squared Frobenius norm is 2+4k²; for P=LU, with entries 1,k,-k,1-k², it is 2+k^4. Multiplying by the common two-step squared damping e^{-8ah} gives the claimed factor for every vector. The difference of the endpoint factors before damping is k²(4-k²)/2, so the unique minimizing q is 0 on (0,2) and 1 on (2,infinity), with all q tied at k=2. Conditioning on the entering state gives the exact N-fold recursion for independent repetitions of the same block law. This is conservation of expected energy at block boundaries, not pathwise conservation. Since both undamped endpoint factors exceed one and are distinct when k differs from 2, the open interval between their logarithms divided by 8h is nonempty and positive, and gives exactly the claimed stability separation. The explicit examples satisfy it (for k=1, 3/2<e<3; for k=3, 19<e³<83/2). Replay: the Gram calculation and conditional iteration above; supporting VERIFICATION.md and verify.py were read for scope, not executed. Does not cover arbitrary cross-block dependence, Lyapunov exponents or approximation error.

## originality

PASS

Best-of-knowledge pass for the exact all-coupling mean-square law and sharp policy classification at fixed marginals, not for the hyperbolicity boundary k=2, basic Gram-matrix methods, or the independent-step stability law. The strongest inspected overlapping statements differ in objective or feasible dependence class.

## value

PASS

Two steps are the smallest block in which changing dependence while holding both marginals fixed is possible. In this exact shear benchmark the better policy reverses with shear strength, and fixed marginals and individual Hurwitz generators still permit the choice of coupling to change strict stability into strict instability, in either direction of the repeat-versus-switch preference. The result identifies when this happens for every initial direction and all block horizons, rather than presenting a selected vector or finite trajectory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
