# Independent mathematical audit

## correctness

PASS

For a fixed zero-sum planar edge list, oriented shoelace gives 2Aσ=Σ_{i<j}εij det(ei,ej). For disjoint pairs permutation-sign covariances vanish; for each i<j<k shared-index covariances are (+1/3,−1/3,+1/3). Closure Σ_{j≠i}det(ei,ej)=0 yields triple sum T=−B for B=Σdet(ei,ej)^2, so Var(A)=B/12=det Q/12 by Cauchy–Binet. If eigenvalues Q are λ1,λ2, detQ<=S²/4 with isotropic equality, zero iff collinear. Haar V2(R^n) closed planar edges (u_j+iv_j)^2 are exchangeable, and the conditional second-row spherical moment E[u2²v2²|a]=(1−a)/((n−1)(n+1)) and a~Beta(1,(n−2)/2) with E[a²(1−a)]=8(n−2)/[n(n+2)(n+4)] imply Var(A_n)=4(n−2)/[3(n+1)(n+2)(n+4)] for n>=3. Ratio V_{n+1}/V_n transitions from >1 at n3 to <1 for n>=4, hence unique n4 maximum 1/90. Independently exact shoelace permutation checks returned variances 9, 41/3,1/3 for three closed input lists. Signed algebraic area, not hull area.

## originality

PASS

Cantarella, Deguchi and Shonkwiler (arXiv:1206.3161), §6 Proposition 15, already analyze edge-set ensembles for *squared chords* and expected radius of gyration, not second moment of oriented signed polygonal area. Cantarella et al. arXiv:1702.01027 already imply n=3 special 1/105 via spherical product formula; that case is expressly not claimed new. The fixed-edge signed-area variance detQ/12 and all n>=4 Haar–Stiefel law are distinct from chord and unsigned convex hull statistics. Published Resultary Nov8 equilateral edge-rearrangement chord-variance theorem likewise treats chord moments, not algebraic signed area.

## value

PASS

A permutation-exact oriented area variance determined by just the second-moment matrix is a natural sharp identity for any closed edge set. Pushing it through canonical Haar–Stiefel polygon sampling produces a nontrivial exact all-size law and a unique four-edge variance maximizer, relevant to random polygon geometry beyond the known triangle moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
