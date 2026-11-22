# Strict bond anticorrelation in a one-defect \(K_{3,3}\) random-cluster gas

## Finding
On the complete bipartite graph \(K_{3,3}\), assign one fixed edge fugacity \(w>0\) and all eight remaining edge fugacities \(v>0\). In the random-cluster Gibbs measure with component weight \(0<q<1\), **every pair of distinct bond-occupation indicators has strictly negative covariance**. The assertion holds for every independent choice of the three positive real parameters \(q,v,w\), with no restriction on the defect strength.

More precisely, for each of the 36 unordered pairs of edges \(e\ne f\), there is a nonzero polynomial \(C_{ef}(q,v,w)\) with positive integer coefficients on its support such that
\[
\operatorname{Cov}(\mathbf1_e,\mathbf1_f)=-\frac{x_ex_f q^2(1-q)C_{ef}(q,v,w)}{Z(q,v,w)^2}<0,
\]
where \(x_0=w\), \(x_e=v\) for \(e\ne0\), and \(Z\) is the positive partition function. The polynomials form exactly eight symmetry classes, completely specified by the accompanying exhaustive symbolic certificate.

## Assumptions and scope
Label the left vertices \(0,1,2\), the right vertices \(3,4,5\), and the nine edges in lexicographic order \(E=((0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5))\). Edge \(0\) is the exceptional bond. For \(A\subseteq E\), write \(k(A)\) for the number of connected components of the graph on all six vertices, including isolated ones. The random-cluster probability of \(A\) is
\[
\mathbb P(A)=\frac{q^{k(A)}w^{\mathbf1_{0\in A}}v^{|A\setminus\{0\}|}}{Z(q,v,w)},\qquad
Z(q,v,w)=\sum_{A\subseteq E}q^{k(A)}w^{\mathbf1_{0\in A}}v^{|A\setminus\{0\}|}.
\]
All 36 pairs, including incident and disjoint pairs and pairs containing the exceptional edge, are covered. The statement is specific to the one-defect activity family on \(K_{3,3}\); it does not assert the multivariate all-edge-weight Rayleigh property or a theorem for larger complete bipartite graphs.

## Proof
Fix a distinct edge pair \(e,f\). Remove the activities of these two selected edges from the monomial weights and define four **conditional coefficient polynomials**, indexed by \(a,b\in\{0,1\}\):
\[
F_{ab}^{ef}=\sum_{\substack{A\subseteq E\\\mathbf1_e(A)=a,\ \mathbf1_f(A)=b}}
 q^{k(A)}v^{|A\setminus\{e,f,0\}|}w^{\mathbf1_{0\in A\setminus\{e,f\}}}.
\]
Then the multiaffine partition polynomial in the activities \(x_e,x_f\) is \(Z=F_{00}+x_eF_{10}+x_fF_{01}+x_ex_fF_{11}\). Therefore
\[
\operatorname{Cov}(\mathbf1_e,\mathbf1_f)=\frac{x_ex_f}{Z^2}(F_{00}F_{11}-F_{10}F_{01}).
\]
(The four polynomials depend on the other edge activities but not on \(x_e,x_f\).)

Exhaustive exact integer polynomial operations on all \(2^9=512\) edge subsets establish, for each pair,
\[
F_{10}F_{01}-F_{00}F_{11}=q^2(1-q)C_{ef}(q,v,w).
\]
Every \(C_{ef}\) is nonzero with all its nonzero coefficients **strictly positive integers**. The coefficient certificate `CERTIFICATE.json` records all powers and coefficients for eight different polynomials, plus the complete partition of the 36 pairs. `verify.py` independently constructs the component number for each subset by union–find; builds the four polynomials in the integer polynomial ring \(\mathbb Z[q,v,w]\); calculates their difference using exact convolution; divides by the claimed factor; confirms the polynomial identity coefficient-by-coefficient; and checks every coefficient of the quotient. This is an **exhaustive finite symbolic identity in independent indeterminates**, not an extrapolation from parameter samples. Hence for every real \(0<q<1\), \(v,w>0\), the right side is strictly positive; substitution in the covariance identity proves the strict sign.

The symmetry-orbit sizes are \(4,4,2,4,8,8,4,2\). Their nonzero quotient-monomial counts in the same order are \(26,25,65,58,67,64,65,58\). The certificate records every exponent/coefficient, so no unproved positivity assertion is delegated to numerical approximations.

## Verification
Run `python verify.py CERTIFICATE.json` with standard-library Python (3.9 or newer). The program recomputes all 36 exact polynomial factorizations and compares every coefficient and orbit against `CERTIFICATE.json`. In addition, for three distinct rational parameter triples and each of the 36 pairs, it computes the partition sums and the covariance numerator directly from all 512 edge subsets using exact rational arithmetic, and verifies equality to the symbolic certificate. The expected success message is `K33_ONE_DEFECT_SYMBOLIC_CERTIFICATE_PASSED 36 PAIRS 8 ORBITS 108 RATIONAL_MOMENT_CHECKS`. The analytic part of the proof is the multiaffine moment identity plus the sign of \(q^2(1-q)C_{ef}\); all remaining nonstandard identities have finite, exhaustive certificates and executable reproduction code.

## Relationship to prior work
Wagner (2006) proves negative-dependence results for Potts-Rayleigh series–parallel matroids and their two-sums. \(K_{3,3}\) is not series–parallel, so those statements do not imply this example. Mani (2011) studies a general sufficient coefficientwise Z-Rayleigh criterion; the present certificate only concerns a one-edge-disordered two-variable specialization and does not assert the unrestricted multivariate property. Zhao–Zhou (2026) cover matroids with rank or corank at most three; the cycle matroid of \(K_{3,3}\) has rank five and corank four. Cao–Fu (2026) treat complete bipartite graphs for uniform spanning forests and connected spanning subgraphs, two different measures not covering arbitrary intermediate \(0<q<1\) and the independent exceptional edge fugacity. The 2026 random-cluster literature treats broader conjectures under alternative graph, activity, or high-degree assumptions. The present finite, coefficientwise certificate addresses the specific low-degree non-series-parallel graph and the whole one-defect family.

## Limitations
This is a theorem for a fixed six-vertex graph, not an infinite graph family. It is exact for \(0<q<1\) and positive activities of the form \((w,v,v,v,v,v,v,v,v)\), not arbitrary distinct activities on all nine edges. The result is motivated by the open general negative-dependence problem, but neither establishes nor refutes the full conjecture. Historical priority cannot be established by a bounded literature search; some related papers were accessible only in partial form. Independent audit is not yet performed.

## References
1. David G. Wagner (2006), *Negatively correlated random variables and Mason’s conjecture*. https://arxiv.org/pdf/math/0602648
2. Arun P. Mani (2011), *An extension of matroid rank submodularity and the Z-Rayleigh property*. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p113/pdf
3. Ying Cao and Houshan Fu (2026), *Negative edge correlation in complete bipartite graphs*. https://arxiv.org/abs/2610.36749
4. Qinghong Zhao and Xiangqian Zhou (2026), *Every rank-three matroid is Z-Rayleigh*. https://arxiv.org/pdf/2611.15512
5. Recep Altar Çiçeksiz and Mohan Ravichandran (2026), *Negative Correlations for Forests and the q<1 Random Cluster Model*. https://arxiv.org/abs/2610.00549
6. Tang and Zhang (2026), *Negative correlation for random cluster below one on high degree regular graphs*. https://arxiv.org/abs/2609.11578
