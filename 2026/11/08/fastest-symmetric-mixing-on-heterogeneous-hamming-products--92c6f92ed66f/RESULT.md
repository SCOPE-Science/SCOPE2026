# Fastest symmetric mixing on heterogeneous Hamming products

## Finding

Let \(d\ge2\) and let \(q_1,\ldots,q_d\ge2\) be integers, with at least two of the sizes unequal. On the Cartesian product of complete graphs \(G=K_{q_1}\square\cdots\square K_{q_d}\), consider all real symmetric, entrywise nonnegative, row-stochastic matrices whose off-diagonal support is contained in the edges of \(G\). Self-loops are allowed. Define the second-largest eigenvalue modulus by \(\mu(P)=\|P-J/N\|_2\), where \(N=\prod_i q_i\) and \(J\) is the all-ones matrix.

Put
\[
C=\sum_{i=1}^{d}\left(1-\frac1{q_i}\right),\qquad
\theta=\min\left\{\frac{2}{d+1},\frac1C\right\}.
\]
Then the *globally* minimum SLEM, allowing arbitrary nonuniform edge weights, is
\[
\boxed{\mu_*(G)=\max\left\{\frac{d-1}{d+1},\,1-\frac1C\right\}.}
\]
An optimal matrix is obtained by assigning probability \(\theta/q_i\) to each individual edge changing coordinate \(i\), probability \(1-C\theta\) to each self-loop, and zero to every other entry. This is the unique optimum invariant under independent permutations of the symbols in each coordinate. Its holding probability is positive exactly when \(C<(d+1)/2\); it vanishes exactly when \(C\ge(d+1)/2\). No uniqueness is asserted among arbitrary non-invariant minimizers.

For the contrasting alphabet sizes \((2,Q)\) with any integer \(Q\ge4\), the unrestricted optimum has \(\mu_*=1/3\). If one instead forces an identical probability on every non-loop edge, the best possible SLEM is \(1-2/Q\), which tends to \(1\) as \(Q\to\infty\). Thus optimization of coordinate-specific probabilities removes an unbounded-in-\(Q\) deterioration in the spectral relaxation time proxy.

## Assumptions and scope

The vertices are words \(v=(v_1,\ldots,v_d)\) with \(v_i\in\{0,\ldots,q_i-1\}\). Two distinct words are adjacent exactly when they differ in one coordinate. There are no edge-capacity lower bounds, no prescribed nonuniform stationary distribution, and no transitions that change several coordinates simultaneously. Symmetry and stochasticity force the uniform stationary distribution. The quantity minimized is the spectral SLEM, not the exact finite-time total-variation mixing time. Throughout \(d\ge2\) and at least two alphabet sizes are different; identical-size Hamming graphs are recalled only as known consistency checks.

## Proof

**1. Reduction without loss of generality.** Let \(H=\prod_{i=1}^{d}S_{q_i}\) act on words by independently permuting each coordinate's symbols. It preserves the graph and acts transitively on vertices. For any feasible \(P\), average all its conjugates under \(H\). The average \(\overline P\) remains symmetric, stochastic, nonnegative and supported on \(G\). Since \(J/N\) commutes with these permutations and the operator norm is convex,
\[
\mu(\overline P)=\|\overline P-J/N\|_2\le\mu(P).
\]
Every \(H\)-invariant feasible matrix has one edge value \(a_i\ge0\) for changes of coordinate \(i\), and constant holding probability \(1-\sum_i(q_i-1)a_i\ge0\). Define \(x_i=q_i a_i\) and \(c_i=(q_i-1)/q_i\). The complete feasibility condition is
\[
x_i\ge0,\qquad\sum_i c_i x_i\le1.
\]

**2. Exact spectrum.** For each coordinate \(i\), the complete-graph Laplacian has eigenvalue \(0\) on the constants and eigenvalue \(q_i\) on its zero-sum subspace. The tensor sum representation
\[
\overline P=I-\sum_i a_i\,I\otimes\cdots\otimes(q_i I-J_i)\otimes\cdots\otimes I
\]
therefore has all eigenvalues \(1-\sum_{i\in S}x_i\) indexed by subsets \(S\subseteq\{1,\ldots,d\}\), with multiplicity \(\prod_{i\in S}(q_i-1)\). The empty subset is the constant eigenvector, with eigenvalue \(1\). For nonempty subsets, the minimum subset sum is \(m=\min_i x_i\) and the maximum is \(X=\sum_i x_i\), whence
\[
\mu(\overline P)=\max\{1-m,\,X-1\}.
\]
The formula remains valid when some \(x_i=0\), in which case an additional eigenvalue \(1\) occurs on a nonconstant subspace.

**3. Sharp global lower bound and attainment.** Because each \(c_i>0\), feasibility yields \(mC\le\sum_i c_i x_i\le1\), hence \(m\le1/C\). Also \(X\ge dm\). Consequently every feasible invariant chain obeys
\[
\mu\ge\max\{1-m,\,dm-1\},\qquad 0\le m\le1/C.
\]
The two affine functions meet at \(m=2/(d+1)\). Their maximum decreases up to that point and increases afterward. Its constrained minimum is attained at \(m=\theta\). Taking \(x_i=\theta\) for every \(i\) is feasible and satisfies \(X=d\theta\), so its SLEM meets the lower bound with equality. The resulting value is
\[
\begin{cases}
(d-1)/(d+1),& C\le(d+1)/2,\\
1-1/C,& C\ge(d+1)/2.
\end{cases}
\]
This agrees with the displayed maximum formula. The group average proves the bound for *every* unsymmetrized chain, not just for those with constant orbit weights.

**4. Uniqueness within the specified symmetry.** In the branch \(C\le(d+1)/2\), an optimum must have \(m\ge2/(d+1)\) from \(1-m\le\mu_*\), while \(X\le2d/(d+1)\) from \(X-1\le\mu_*\). Thus \(d m\le X\) forces every \(x_i=2/(d+1)\). In the branch \(C\ge(d+1)/2\), optimality forces \(m\ge1/C\); feasibility and \(\sum_i c_i= C\) then force every \(x_i=1/C\). At the shared boundary these conclusions coincide. Thus the invariant optimal design is unique. Its diagonal is \(1-C\theta\), giving the stated strict-positive versus zero-holding threshold.

**5. Exact heterogeneous benchmark.** For \((q_1,q_2)=(2,Q)\), \(C=3/2-1/Q<3/2\), so \(\theta=2/3\) and \(\mu_*=1/3\). The optimal coordinate edge probabilities are \(1/3\) and \(2/(3Q)\), and holding is \(2/(3Q)\). If all non-loop edges must instead have a common probability \(a\), feasibility demands \(0\le a\le1/Q\). The nonconstant eigenvalues are \(1-2a\), \(1-Qa\), \(1-(Q+2)a\). Thus its SLEM is \(\max\{1-2a,(Q+2)a-1\}\). For \(Q\ge4\) the unconstrained intersection \(a=2/(Q+4)\) lies at or above \(1/Q\), so the best common weight is \(a=1/Q\), giving SLEM \(1-2/Q\).

## Verification

The independent mathematical steps are the operator-norm averaging inequality, the tensor-product eigenbasis, the scalar convex minimax with its capacity constraint, and equality of the constructed chain with the lower bound. All hold symbolically for all stated integer parameters. The provided standalone `verify.py` performs exact rational matrix/basis checks for seven sample tuples, rational-grid minimax checks for six tuples, and exact equal-edge comparison checks for \(Q\in\{4,\ldots,20\}\). Its expected result is `VERIFY_OK`. Neither the finite checks nor any search result is used as an infinite proof or a publication-priority certificate.

## Relationship to prior work

Boyd, Diaconis and Xiao introduced the global symmetric stochastic SLEM optimization and its semidefinite formulation. Boyd, Diaconis, Parrilo and Xiao established automorphism averaging and gave explicit answers for edge-/distance-transitive examples, including equal-alphabet Hamming graphs \(H(d,q)\), in their Sections 2.2, 3.2 and 3.3.3. Their equal-alphabet formula agrees with the above on substituting \(q_i=q\), but that case is not claimed new. The heterogeneous products here are generally not edge-transitive: edge directions corresponding to distinct coordinate clique sizes need not lie in the same orbit. Consequently the one-edge-weight formula for distance-transitive graphs does not cover them. The present optimization is a closed all-dimension, all-heterogeneous-alphabet formula with distinct direction weights, an exact holding threshold and a quantified failure of the uniform-edge restriction. The general symmetry-reduction method is used as prior machinery, not claimed as a discovery here.

## Limitations

The statement concerns spectral contraction of symmetric Markov chains with uniform stationary distribution. It does not determine worst-case finite-step total-variation mixing, optimize nonreversible chains, cover nonuniform target measures, or assert uniqueness of all possible non-invariant optimizers. General symmetry-reduction literature supplies the method and closely related homogeneous examples; a comprehensive specialist publication-priority determination has not been made. No independent mathematical audit has been performed.

## References

1. S. Boyd, P. Diaconis, and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689, DOI: 10.1137/S0036144503423264, https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955, first posted 2007-09-06, https://arxiv.org/abs/0709.0955, subsequently SIAM Journal on Optimization **20** (2009), 792–819.
