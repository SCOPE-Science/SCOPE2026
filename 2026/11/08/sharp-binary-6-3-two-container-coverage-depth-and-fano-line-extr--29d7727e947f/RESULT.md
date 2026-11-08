# Sharp binary \([6,3]\) two-container coverage depth and Fano-line extremizers

## Finding

Let \(G\) be any rank-three binary generator matrix with six columns, partitioned into two labeled containers \(A,B\) of three columns each; zero and repeated columns are permitted. In every round, independently choose one of the three *positions* uniformly with replacement from each container. Let \(\tau\) be the first number of rounds by which the sampled columns span \(\mathbb F_2^3\). Then

\[
\min_{G,A,B}\mathbb E[\tau]=\frac{125}{56},\qquad
\min_{G,A,B}2\mathbb E[\tau]=\frac{125}{28}.
\]

Equality holds if and only if, after optionally interchanging the containers, there is a two-dimensional subspace \(U\leq\mathbb F_2^3\) such that the first container contains exactly the three nonzero elements of \(U\), and the second contains exactly three of the four vectors in \(\mathbb F_2^3\setminus U\). Thus every optimizing layout uses six distinct nonzero columns. There are precisely \(7\cdot4=28\) unordered container-multiset pairs, or \(56\) labeled container-multiset pairs, in a fixed coordinate realization of \(\mathbb F_2^3\). Permuting the three positions in either container does not change the result.

For every equality layout, the *entire* optimal recovery-time survival law is

\[
\Pr(\tau>0)=1,\qquad
\Pr(\tau>t)=3\left(\frac29\right)^t+3\left(\frac19\right)^t
\quad(t=1,2,\ldots).
\]

The next greater achievable expected number of rounds is \(127/56\). These claims include all binary \([6,3]\) linear codes, not only simple or projective codes.

## Assumptions and scope

This is the noiseless *synchronous* distributed-coverage model: there are two containers, exactly one read from each per round, draws are uniform and independent across rounds and containers, and the decoder succeeds as soon as the accumulated generator columns have rank three. Distinct positions with identical columns remain distinct sampling possibilities. Every considered \(G\) has rank exactly three. The result optimizes jointly over all generator matrices and balanced assignments of their six columns.

The case is a first balanced two-container, rank-three binary setting beyond MDS existence. A binary \([6,3]\) MDS code does not exist: an MDS generator would require all triples of six nonzero vectors in \(\mathbb F_2^3\) to be independent, whereas a set containing no three collinear in the Fano plane has at most four points.

## Proof

**Subspace reduction.** Identify \(\mathbb F_2^3\) with the integers \(0,1,\ldots,7\), using three-bit vectors and bitwise XOR for addition. There are seven hyperplanes \(H_h=\{v:h\cdot v=0\}\), indexed by nonzero \(h\), seven one-dimensional subspaces \(L_v=\{0,v\}\), indexed by nonzero \(v\), and the zero subspace \(Z=\{0\}\). Let \(a_W\) and \(b_W\) count columns from \(A,B\) in \(W\), with multiplicity, and put \(\rho_W=a_Wb_W/9\).

For each integer \(t\geq0\), the chance that all columns read up to round \(t\) lie in \(W\) is \(\rho_W^t\), with the convention \(0^0=1\). The subspace-lattice Möbius coefficients for proper subspaces in dimension three over \(\mathbb F_2\) are \(+1\) for hyperplanes, \(-2\) for lines, and \(+8\) for \(Z\), when computing the indicator of *failure* to span. Consequently,

\[
\Pr(\tau>t)=\sum_{h\ne0}\rho_{H_h}^{\,t}
 -2\sum_{v\ne0}\rho_{L_v}^{\,t}+8\rho_Z^{\,t}.
\]

Rank \(G=3\) implies \(\rho_W<1\) for every proper subspace. Summing the geometric series over all \(t\geq0\) therefore gives the exact rational evaluation rule

\[
\mathbb E[\tau]=
\sum_{h\ne0}\frac{9}{9-a_{H_h}b_{H_h}}
-2\sum_{v\ne0}\frac{9}{9-a_{L_v}b_{L_v}}
+\frac{72}{9-a_Zb_Z}.
\tag{1}
\]

**Exhaustive finite optimization.** Every possible three-column container is, up to permutation of its positions, one of the \(\binom{10}{3}=120\) multisets drawn from eight binary vectors. Since exchanging the two containers preserves \(\tau\), it is sufficient to examine the unordered pairs of these multisets. The standalone `checker.py` enumerates every such pair, rejects precisely those with combined rank below three, and evaluates (1) using only exact integer and rational arithmetic. There are \(5922\) full-rank unordered pairs and \(55\) distinct expectation values. Exactly \(28\) pairs attain the least value \(125/56\); exactly \(42\) pairs attain the next value \(127/56\). For every evaluated pair, the checker tests the stated geometric equality criterion in both possible container orders and proves that it is equivalent to attaining the minimum. Thus no omitted zero-vector, repeated-vector or alternative partition type can improve or tie the result. The finite certificate is exhaustive, because sorting columns within a container and swapping containers remove only symmetries of the sampling law.

As an independent consistency check, the same program also computes the exact expected recovery time for *each* of the \(5922\) pairs by rational first-step recursion over all \(64\) possible pairs of observed-position subsets, without using (1). It verifies agreement for every pair. The finite certificate does not attempt to infer an infinite statement from tested parameters: this theorem has exactly eight ambient vectors and two triples, and all of them are enumerated.

**Tail law for equality.** Set \(A=U\setminus\{0\}\) and choose three distinct \(B\)-columns outside \(U\). The three pairwise differences of the three \(B\)-vectors are precisely the three nonzero elements of \(U\). If at least two different \(A\)-columns have been observed, their span is \(U\), and any \(B\)-column completes rank three. Hence failure at a positive time \(t\) forces all \(t\) observations from \(A\) to equal one fixed \(a\in U\setminus\{0\}\), in three possible ways. For each such \(a\), the \(B\)-history must either be constant (three choices) or use both members of the unique pair of \(B\)-columns with difference \(a\) (\(2^t-2\) choices). The number of failing histories is therefore \(3(2^t+1)\), out of \(9^t\) equally likely histories. This proves the claimed survival law; summation yields

\[
\mathbb E[\tau]
=1+3\frac{2/9}{1-2/9}+3\frac{1/9}{1-1/9}
=\frac{125}{56}.
\]

## Verification

Run `python checker.py` using Python 3.10 or later, without third-party libraries. The checker independently enumerates all \(120\) possible column triples, all \(5922\) admissible unordered pairs, verifies exact rational expectations by two different algorithms for every pair, checks the complete equality classification and the next-best value, and checks the explicit survival probabilities through eight rounds by exact dynamic counting. All computations needed for the finite exhaustive optimization are included; no external data, remote service or unprovided certificate is required.

## Relationship to prior work

Kong, Elishco, Wang and Duman (2026) defined the synchronous multi-container full-message-recovery model and derived a general Möbius-inversion formula for any given generator matrix and layout (their Theorem II.3). That general formula supports the subspace reduction above, but does not optimize over binary \([6,3]\) codes and balanced two-container layouts. Their conclusion explicitly identifies constrained-layout and small-field non-MDS code optimization as open directions. Their MDS optimality result is inapplicable here because a binary \([6,3]\) MDS code does not exist.

Bertuzzo, Ravagnani and Yaakobi (2025) treat small-field coverage depth with uniform reads in a single container, deriving formulas for classical code families; Bar-Lev, Sabary, Gabrys and Yaakobi (2023) introduced the single-container coverage-depth problem. Neither single-container result supplies the two-container layout optimum or its equality classification. A published finding on exact rank-two coverage-depth optimization concerns rank two rather than three. This result uses existing probability machinery but determines a distinct exact optimization and a Fano-geometric equality family.

For comparison, a hypothetical \([6,3]\) MDS generator under the same \(3+3\) sampling arrangement would have expected rounds \(17/8\); the sharp binary non-MDS penalty is \(125/56-17/8=3/28\) rounds. This is a comparison to an unavailable binary MDS structure, not a claim that such a code exists.

## Limitations

The global minimum and its classification are proved only for binary rank-three, six-column codes partitioned into two three-column containers. This result does not optimize larger dimensions, arbitrary container capacities, asynchronous scheduling, nonuniform sampling, channel noise, or random-access recovery. The exhaustive finite proof is exact and self-contained, but it is not an independent human proof audit. Historical-priority verification is necessarily limited to the inspected literature and indexed records; an unindexed equivalent statement may exist.

## References

1. Xiangliang Kong, Ohad Elishco, Chen Wang and Tolga M. Duman, *The Coverage Depth Problem in Distributed DNA Data Storage*, arXiv:2610.02931v1 (first public release 2026-10-02), https://arxiv.org/abs/2610.02931 . In particular Section II.B, Theorem II.3; Section V; and Appendix B.
2. Matteo Bertuzzo, Alberto Ravagnani and Eitan Yaakobi, *The Coverage Depth Problem in DNA Storage Over Small Alphabets*, arXiv:2507.20639v1 (2025), https://arxiv.org/abs/2507.20639 .
3. Daniella Bar-Lev, Omer Sabary, Ryan Gabrys and Eitan Yaakobi, *Cover Your Bases: How to Minimize the Sequencing Coverage in DNA Storage Systems*, arXiv:2305.05656 (2023), https://arxiv.org/abs/2305.05656 .
