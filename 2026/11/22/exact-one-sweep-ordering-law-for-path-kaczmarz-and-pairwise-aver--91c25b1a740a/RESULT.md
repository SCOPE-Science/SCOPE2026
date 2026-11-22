# Exact one-sweep ordering law for path Kaczmarz and pairwise averaging

## Finding
Let \(n\ge 2\), let \(e_j\) be the standard basis of \(\mathbb R^n\), and let
\[
P_i=I-\tfrac12(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T},
\qquad 1\le i\le n-1.
\]
For any permutation \(\pi\) of the \(n-1\) edges, put
\(A_\pi=P_{\pi(n-1)}\cdots P_{\pi(1)}\), \(J=\mathbf1\mathbf1^{\mathsf T}/n\), and
\(E(\pi)=\|A_\pi-J\|_F^2\). This is the expected squared disagreement after one sweep when the initial error has covariance \(I-J\).

Encode the relative order of consecutive edges by the binary word of length \(n-2\): \(b_j=0\) if edge \(j\) precedes edge \(j+1\), and \(b_j=1\) otherwise. If its maximal constant runs have lengths \(\ell_1,\ldots,\ell_r\), then the **exact error for every permutation** is
\[
E(\pi)=\sum_{q=1}^{r}\sum_{k=1}^{\ell_q}\frac{1-4^{-k}}3.
\tag{1}
\]
The sum is empty when \(n=2\). Consequently,
\[
\boxed{\min_\pi E(\pi)=\frac{n-2}{4}},\qquad
\boxed{\max_\pi E(\pi)=\frac{n-2}{3}-\frac{1-4^{-(n-2)}}9}.
\tag{2}
\]
For \(n\ge4\), the minimizers are exactly the two alternating binary words, equivalently the two red–black precedence classes (up to commuting disjoint contacts). The maximizers are exactly the left-to-right and right-to-left complete sweeps. The worst-to-best ratio tends to \(4/3\) as \(n\to\infty\).

## Assumptions and scope
Every adjacent pair is averaged **once** with the arithmetic mean. Each edge occurs in exactly one position of a deterministic, nonadaptive permutation. The initial error is mean-zero with covariance \(I-J\), or equivalently the objective averages squared error over an orthonormal basis of the mean-zero subspace. No arbitrary fixed initial error, repeated edges, relaxed weights, or multi-sweep asymptotic claim is covered. Since the matrices are symmetric, doubly stochastic and fix \(\mathbf1\), \(\|A_\pi-J\|_F^2=\|A_\pi\|_F^2-1\).

## Proof
Put \(v_i=e_i-e_{i+1}\) and \(P_i=I-v_iv_i^{\mathsf T}/2\). The path-edge Gram identities are
\[
\langle v_i,v_j\rangle=
\begin{cases}2&i=j,\\-1&|i-j|=1,\\0&|i-j|>1.\end{cases}
\tag{3}
\]
Before the averaging of edge \(i\), let \(A_{<i}\) denote the product of all earlier projections, in chronological application order. Define \(L_i\) as the longest integer \(L\ge0\) for which the edges \(i-L,i-L+1,\ldots,i-1,i\) occur in this increasing order, and \(R_i\) as the longest \(R\ge0\) for which \(i+R,i+R-1,\ldots,i+1,i\) occur in this decreasing order. These are truncated at the path endpoints.

A backward expansion through the earlier factors gives the exact row
\[
v_i^{\mathsf T}A_{<i}=v_i^{\mathsf T}
 +\sum_{k=1}^{L_i}2^{-k}v_{i-k}^{\mathsf T}
 +\sum_{k=1}^{R_i}2^{-k}v_{i+k}^{\mathsf T}.
\tag{4}
\]
To verify (4), apply the earlier projections in reverse chronological order to the initial row \(v_i^{\mathsf T}\). Projection onto an edge at distance greater than one from the current support does nothing. A new contributing edge on either side must be the next adjacent edge beyond the current support, and its coefficient is exactly one half its inner neighbor's coefficient, by (3). Such an edge can contribute only if each edge along the route toward \(i\) was previously used later than its outward neighbor, which is precisely the defining chain condition for \(L_i\) or \(R_i\). An edge used too early cannot later contribute, because its projection never recurs. The supports expanding left and right do not interact. Induction along the reversed factor list proves (4), including any interleaving of the two sides.

Writing \(S_k=\sum_{j=1}^k4^{-j}=(1-4^{-k})/3\) and \(S_0=0\), equations (3) and (4) yield
\[
\tfrac12\|v_i^{\mathsf T}A_{<i}\|^2=1-S_{L_i}-S_{R_i}.
\tag{5}
\]
Indeed on each arm the diagonal squared-coefficient sum and the nearest-neighbor cross terms cancel to minus \(S\); there are no cross-arm inner products. Since \(P_i\) is an orthogonal projection, the loss of the squared Frobenius norm at contact \(i\) equals the left side of (5). Summing over all \(n-1\) contacts, starting with \(\|I\|_F^2=n\), proves
\[
E(\pi)=\sum_{i=1}^{n-1}(S_{L_i}+S_{R_i}).
\tag{6}
\]
For a constant run of \(\ell\) zero bits, its leftward chains contribute \(S_1,\ldots,S_\ell\) once each; for a run of one bits the analogous rightward chains contribute the same sequence. Each chain belongs to exactly one run, so (6) proves (1).

Now \(S_1=1/4\) and \(S_k>1/4\) for \(k\ge2\). Because the word has \(n-2\) bits, the minimum is \((n-2)/4\), with equality exactly when every constant run has length one, i.e. the word alternates. Conversely the run-cost \(F(\ell)=\sum_{k=1}^{\ell}S_k\) is strictly superadditive for positive integers: \(F(a+b)>F(a)+F(b)\), since \(S_k\) is strictly increasing. Thus merging any two runs increases the cost, and the maximum occurs only when all \(n-2\) bits agree. Evaluation of \(F(n-2)\) gives (2). For \(n\ge4\) the two constant orientations force a total edge order. The alternating orientations specify the two optimal partial orders, and disjoint-edge swaps within each class do not change the product. Finally division of the two formulas in (2) gives the limit \(4/3\).

## Verification
The standalone script `verify.py` requires only Python 3 and its standard library. Run `python verify.py` beside this file. It computes every one-pass matrix exactly using rational arithmetic, checks the run formula for every permutation for \(2\le n\le8\), exhaustively checks all binary orientation words for \(2\le n\le12\), and checks 240 seeded permutations at larger sizes. It also verifies extremal classes and representative exact fractions. The executed script returned `PASS: 8200 exact-arithmetic sweep identities and sharp-bound cases`. This finite test supplements, but does not replace, the argument for all \(n\).

## Relationship to prior work
Oswald and Zhou (first posted 2015) study shuffled and preshuffled Kaczmarz/SOR through broad spectral-norm bounds and existence of useful permutations, not an exact one-sweep isotropic Frobenius error for all orders of a path-incidence system. Their optimization criterion and quantifiers differ from (1). Boyd, Ghosh, Prabhakar and Shah (2006) analyze independent randomized pairwise gossip and long-run averaging rates rather than a fixed permutation that contacts every path edge once. Dai, Soltanalian and Pelckmans (2014) optimize independent Kaczmarz row-sampling probabilities through a one-step worst-direction bound, not permutation scheduling. The 2005 tomography-view ordering paper by Kazantsev, Matej and Lewitt and the 1993 ordering paper by Herman and Meyer are relevant to the idea of ordering projections, but available inspected descriptions concern tomography experiments or heuristics; accessible full text did not establish an equivalent all-path run identity. That incomplete historical comparison is a publication-priority risk, not a proof of novelty.

## Limitations
The result is specific to adjacent-difference projections on an unweighted path and to isotropic mean-zero mean-square error after a single permutation sweep. Optimal schedules for a fixed nonisotropic initial error can differ. It neither proves a superior worst-direction contraction nor the best ordering after repeated sweeps. All uniqueness assertions are about precedence classes; commuting disjoint edges create multiple equivalent literal permutations. Mathematical verification is analytical plus finite exact checks, not independent certification. The 2005 ordering source could not be read in full.

## References
1. P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, arXiv:1510.04727, first posted 2015-10-15, https://arxiv.org/abs/1510.04727.
2. S. Boyd, A. Ghosh, B. Prabhakar and D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory 52 (2006), 2508–2530, https://doi.org/10.1109/TIT.2006.874516.
3. L. Dai, M. Soltanalian and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863, first posted 2014-02-12, https://arxiv.org/abs/1402.2863.
4. I. G. Kazantsev, S. Matej and R. M. Lewitt, *Optimal Ordering of Projections using Permutation Matrices and Angles between Projection Subspaces*, Electronic Notes in Discrete Mathematics 20 (2005), 205–216, https://doi.org/10.1016/j.endm.2005.05.064.
5. G. T. Herman and L. B. Meyer, *Algebraic reconstruction techniques can be made computationally efficient*, IEEE Transactions on Medical Imaging 12 (1993), 600–609, https://doi.org/10.1109/42.241889.
