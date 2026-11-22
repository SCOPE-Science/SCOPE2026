# Exact optimal cyclic coordinate orderings on arbitrary weighted odd rings

## Finding
Let \(n\ge5\) be odd and let \(A=D-W\) be a real symmetric positive-definite matrix whose off-diagonal graph is the cycle \(C_n\). Here \(D=\operatorname{diag}(d_0,\ldots,d_{n-1})\), each \(d_i>0\), and \(W_{i,i+1}=W_{i+1,i}=w_i>0\), with indices modulo \(n\), and all other entries of \(W\) zero. For any permutation \(\sigma\) of the coordinate-update order, let \(T_\sigma\) be the error propagator of one exact cyclic coordinate-descent (Gauss–Seidel) sweep for the quadratic \(\tfrac12x^{\mathsf T}Ax-b^{\mathsf T}x\). Define the *clockwise ascent count*
\[
a(\sigma)=\#\{i\in\{0,\ldots,n-1\}:\text{coordinate }i\text{ is updated before }i+1\}.
\]
Then \(1\le a(\sigma)\le n-1\), and **the full characteristic polynomial, not merely the convergence factor, depends on \(\sigma\) only through \(a(\sigma)\) up to reversal**. Moreover the asymptotic convergence factor \(\rho(T_\sigma)\) is strictly increasing in \(\lvert n-2a(\sigma)\rvert\). Thus *all and only* the fastest orders have
\[
a(\sigma)\in\left\{\frac{n-1}{2},\frac{n+1}{2}\right\},
\]
independently of every positive edge weight and every diagonal value subject to positive definiteness. Exactly \(2n\,\left\langle {n-1\atop (n-3)/2}\right\rangle\) labelled update orders are optimal, with brackets denoting a classical Eulerian number.

Set \(r=\rho(D^{-1}W)\in(0,1)\) and \(P=\prod_{i=0}^{n-1}w_i\). The optimal convergence factor is the **unique** \(\lambda_*\in(r^2,1)\) satisfying
\[
\det(\sqrt{\lambda_*}D-W)=P\left(\lambda_*^{-1/2}+\lambda_*^{1/2}-2\right).
\]
More generally, an order with ascent count \(a\) has the unique convergence factor \(\lambda_a\in(r^2,1)\) satisfying
\[
\det(\sqrt{\lambda_a}D-W)=P\left(\lambda_a^{a-n/2}+\lambda_a^{n/2-a}-2\right).
\]
This is an exact strict odd-cycle obstruction to attaining the Jacobi-squared factor \(r^2\).

## Assumptions and scope
The graph is a single **undirected simple cycle of odd length at least five**, with strictly positive conductances; the symmetric coefficient matrix \(A=D-W\) is positive definite. Diagonal entries need not be constant, and diagonal dominance is sufficient but not necessary. Every coordinate is updated exactly once per sweep, with exact minimization (relaxation parameter one). Rates refer to the spectral radius of the complete linear error propagator, *not* to finite-horizon norm contraction or actual wall-clock cost. The theorem covers arbitrary right-hand sides because the error propagator does not depend on the right-hand side. It does not assert the same result for even cycles, other sparsity graphs, over-relaxation, or time-varying orders.

## Proof
**1. Characteristic determinant.** Fix an update order and simultaneously permute rows and columns of \(A\) accordingly. Write \(A=D+L+U\) with \(L\) strictly lower and \(U\) strictly upper triangular. Then \(T=-(D+L)^{-1}U\) and, since \(\det(D+L)=\prod_i d_i\),
\[
\det(\lambda I-T)=\frac{\det(\lambda(D+L)+U)}{\prod_i d_i}.
\]
In the Leibniz expansion of the numerator, the only nontrivial permutation cycles supported by the graph are two-cycles using one edge, and the two orientations of the whole graph cycle. Every chosen two-cycle contributes \(-\lambda w_i^2\), regardless of the update order. The diagonal terms contribute \(\lambda d_i\). The clockwise full cycle contributes \(-P\lambda^a\), and its reverse contributes \(-P\lambda^{n-a}\). Applying the same expansion to \(\det(\sqrt\lambda D-W)\) and subtracting the full-cycle terms gives the exact identity for every \(\lambda>0\):
\[
\boxed{\det(\lambda(D+L)+U)=\lambda^{n/2}\left[\det(\sqrt\lambda D-W)-P\bigl(\lambda^{a-n/2}+\lambda^{n/2-a}-2\bigr)\right].}
\]
This proves complete characteristic-polynomial invariance under equal counts \(a\) or \(n-a\).

**2. Exactly one candidate convergence root.** The nonnegative irreducible matrix \(D^{-1}W\) is similar to the symmetric matrix \(K=D^{-1/2}WD^{-1/2}\). Positive definiteness of \(D-W\) implies its Perron root \(r\) is strictly below one. For \(\lambda\ge r^2\), the symmetric matrix \(\sqrt\lambda D-W\) is positive semidefinite, becoming positive definite for \(\lambda>r^2\). Its determinant grows strictly from zero as \(\lambda\) increases from \(r^2\) to one, since
\[
\det(sD-W)=\det(D)\prod_{j=1}^n(s-\mu_j),\qquad s>r,
\]
where every \(\mu_j\le r\) is a real eigenvalue of \(K\). For any odd \(n\) and admissible integer \(a\), put \(m=\lvert a-n/2\rvert\ge1/2\). The right-hand side \(P(\lambda^{-m}+\lambda^{m}-2)\) is strictly positive and strictly decreasing on \((0,1)\). It is positive at \(\lambda=r^2\) and zero at one, whereas the determinant runs from zero to the strictly positive \(\det A\). Therefore the scalar equation has exactly one solution \(\lambda_a\in(r^2,1)\).

**3. Identification with spectral radius.** For a symmetric positive-definite \(A\), a full exact coordinate sweep strictly decreases the positive quadratic error energy for every nonzero input: each coordinate update is an orthogonal projection in the \(A\)-inner product; equality throughout a complete sweep would require \(Ae=0\), hence \(e=0\). Compactness of the \(A\)-unit sphere gives \(\|T\|_A<1\), thus \(\rho(T)<1\). The matrices \(-(D+L)^{-1}U\) are entrywise nonnegative because \(-L\) and \(-U\) are nonnegative and \((D+L)^{-1}\) is a finite nonnegative lower-triangular series after diagonal normalization. By Perron–Frobenius, \(\rho(T)\) is a nonnegative real eigenvalue. The unique positive root \(\lambda_a>r^2\) from Step 2 is an eigenvalue, so \(\rho(T)\ge\lambda_a\). If strict inequality held, the positive eigenvalue \(\rho(T)\in(\lambda_a,1)\) would give a second root of the scalar equation, contradiction. Hence \(\rho(T)=\lambda_a\).

**4. Strict order ranking.** For fixed \(\lambda\in(0,1)\), the function \(m\mapsto\lambda^{-m}+\lambda^m-2\) is strictly increasing for \(m>0\). Its crossing with the strictly increasing determinant therefore moves strictly to the right when \(m\) increases. Since odd \(n\) forces \(m\ge1/2\), equality of the smallest \(m\) occurs precisely at the two stated ascent counts. This also proves the strict \(r^2\) gap.

**5. Exact number of optimizers.** The circular list of \(n\) distinct coordinate-update ranks has \(a\) clockwise ascents. Rotate the vertex labels so that the smallest rank is first. The boundary from the last entry to this smallest rank is a descent, and the edge from the smallest rank to the next is an ascent, so the remaining \(n-1\) ranks have exactly \(a-1\) ordinary ascents. There are \(\left\langle {n-1\atop a-1}\right\rangle\) such linear arrangements and \(n\) rotations. Hence there are \(n\left\langle {n-1\atop a-1}\right\rangle\) orders with count \(a\). Eulerian symmetry equates the two central counts for odd \(n\), yielding the stated total.

## Verification
For the unit-weight five-cycle with \(D=3I\), all \(120\) permutations fall into just two spectral-radius classes. The \(110\) optimal permutations have \(a\in\{2,3\}\), with their nonzero Perron root given by
\[
243\lambda^3-135\lambda^2+14\lambda-1=0,
\qquad 0.4473<\lambda_*<0.4474.
\]
The ten slowest permutations have \(a\in\{1,4\}\), with positive Perron root given by
\[
243\lambda^4-136\lambda^3+15\lambda^2-1=0,
\qquad 0.4679<\lambda_{\mathrm{slow}}<0.4680.
\]
The rational inequalities above are checked exactly. The standalone `verify_cycle.py` checks four exact symbolic heterogeneous determinant identities, both five-cycle characteristic polynomials and their rational root brackets, then independently constructs the sequential update matrices for **every permutation** of heterogeneous five- and seven-cycles (\(120+5040\) cases). The seven-cycle has exactly \(4228\) optimal permutations. These finite tests corroborate, but do not replace, the all-dimensional proof in the preceding section.

## Relationship to prior work
Varga, *Orderings of the successive overrelaxation scheme* (1959), establishes a general order-independent Jacobi-squared lower bound for suitable irreducible nonnegative symmetric iteration matrices and characterizes equality by consistency; on a nonbipartite odd cycle, the bound is not attained. The result here classifies **all** nonattaining odd-cycle orderings, derives the exact convergence factor for each orientation class, and counts every optimizer with arbitrary positive weights and diagonals. Varga's *p-cyclic matrices* paper treats consistently ordered cyclic matrices, not this weighted odd-cycle exhaustive ranking. Oswald and Zhou (public preprint October 15, 2015) study randomized equation ordering and general contraction bounds, not exact deterministic optimal-order classes. Heller (1957) is a relevant historical source for equal-spectrum ordering questions; its full text was not accessible during this literature inspection, so possible overlap with the characteristic-polynomial portion remains a priority risk. Its narrower described focus, as reported in Varga's 1959 introduction, does not establish the strict optimality ranking used here.

## Limitations
This is a self-review, not independent validation. The strict spectral-radius comparison need not order one-sweep operator norms, early-iteration errors, or parallel computational cost. The theorem requires one chordless odd ring and strictly positive ring weights. The Heller historical paper and any unindexed equivalent literature may affect publication priority; no claim is made about exhaustive literature coverage or historical priority.

## References
1. R. S. Varga, "Orderings of the successive overrelaxation scheme," *Pacific Journal of Mathematics* 9(3) (1959), 925–939. https://doi.org/10.2140/pjm.1959.9.925 ; open full text: https://msp.org/pjm/1959/9-3/pjm-v9-n3-p28-s.pdf
2. R. S. Varga, "p-cyclic matrices: a generalization of the Young–Frankel successive overrelaxation scheme," *Pacific Journal of Mathematics* 9(2) (1959), 617–628. https://doi.org/10.2140/pjm.1959.9.617 ; open full text: https://www.math.kent.edu/~varga/pub/paper_11.pdf
3. P. Oswald and W. Zhou, "Random Reordering in SOR-Type Methods," arXiv:1510.04727, first public October 15, 2015. https://arxiv.org/abs/1510.04727
4. J. Heller, "Ordering properties of linear successive iteration schemes applied to multi-diagonal type linear systems," *J. Soc. Indust. Appl. Math.* 5 (1957), 238–243. https://doi.org/10.1137/0105016 (full text not inspected).
