# Sharp fastest-mixing weights on clique-corona networks with pendant clusters

## Finding
For integers \(m\ge3\) and \(q\ge1\), let \(G_{m,q}=K_m\circ\overline{K_q}\): its \(m\) core vertices form a clique, and each core vertex is joined to its own \(q\) distinct degree-one pendant vertices. Among all real symmetric, entrywise nonnegative stochastic matrices supported on edges and diagonal positions of \(G_{m,q}\), the smallest second-largest eigenvalue modulus is
\[
\mu_{m,q}=1-\frac{m}{(m-1)+q(\sqrt m+\sqrt{m-1})^2}.
\]
A minimizing matrix assigns the same transition probability \(a_{m,q}\) to every core-to-own-pendant edge and the same probability \(b_{m,q}\) to every edge between distinct core vertices, where
\[
D=(m-1)+q(\sqrt m+\sqrt{m-1})^2,\qquad
 a_{m,q}=\frac{\sqrt m(\sqrt m+\sqrt{m-1})}{D},\qquad
 b_{m,q}=\frac{1+q\bigl(1+\sqrt{m/(m-1)}\bigr)}{D}.
\]
Every core holding probability is zero; each pendant holding probability equals \(1-a_{m,q}\). This is the **unique invariant optimum** under all graph automorphisms. Global optimality holds over every feasible symmetric matrix, without any invariance assumption; uniqueness outside the invariant class is not asserted.

The invariant edge weights have a sharp ordering transition:
\[
a_{m,q}>b_{m,q}\ \text{if }q<m-1,\qquad
 a_{m,q}=b_{m,q}\ \text{if }q=m-1,\qquad
 a_{m,q}<b_{m,q}\ \text{if }q>m-1.
\]
Thus at \(q=m-1\) both transition probabilities equal \(1/[2(m-1)]\). For fixed \(q\), the optimal SLEM tends to \(4q/(4q+1)\) as \(m\to\infty\). For fixed \(m\),
\[
\lim_{q\to\infty}q(1-\mu_{m,q})
=\left(\frac{\sqrt{m/(m-1)}}{1+\sqrt{m/(m-1)}}\right)^2.
\]

## Assumptions and scope
A feasible transition matrix \(P\) has one state per vertex, is symmetric and nonnegative, satisfies \(P\mathbf 1=\mathbf 1\), and has \(P_{uv}=0\) for distinct nonadjacent vertices. Diagonal holding transitions are permitted. For \(N=m(q+1)\), write \(J_N\) for the all-ones matrix and define \(\mu(P)=\|P-J_N/N\|_2\), the maximum absolute value of all eigenvalues except one stationary eigenvalue. The minimum is taken over the full feasible class, not only automorphism-invariant chains. There are no reversibility constraints beyond the stated symmetry and uniform stationary measure. For clarity, \(q\) counts distinct pendant leaves, not a clique attached to each core.

## Proof
**1. Symmetry and eigenblocks.** Averaging a feasible \(P\) over permutations of the \(m\) core-and-leaf clusters and permutations within each pendant cluster preserves feasibility. The spectral norm expression for \(\mu\) is convex and invariant under permutations, so averaging cannot increase \(\mu\). Any invariant feasible matrix has a core–pendant probability \(a\), a core–core probability \(b\), pendant holding \(1-a\), and core holding \(1-qa-(m-1)b\), with
\[
0\le a\le1/q,\qquad 0\le b\le\frac{1-qa}{m-1}.
\]
The spectrum decomposes into \(1\), \(1-(q+1)a\), the value \(1-a\) with multiplicity \(m(q-1)\) when \(q>1\), and two eigenvalues of the real symmetric block
\[
M(a,b)=\begin{pmatrix}
1-qa-mb&\sqrt q\,a\\
\sqrt q\,a&1-a
\end{pmatrix},
\]
each repeated \(m-1\) times. This follows by separating leaf vectors of zero sum within a cluster, the cluster-uniform direction, and the \(m-1\) core-index directions of zero sum.

**2. Universal dual Rayleigh bound.** Set
\[
s=\sqrt{\frac{m}{m-1}},\quad T=1+q(1+s)^2,\quad
 t=\sqrt q(1+s),\quad v=\binom{1}{t}.
\]
Since \(b\le b_{\max}(a)=(1-qa)/(m-1)\) and \(1/(m-1)=s^2-1\),
\[
\frac{v^{\mathsf T}M(a,b)v}{v^{\mathsf T}v}
\ge\frac{-(s^2-1)(1-qa)+2q(1+s)a+q(1+s)^2(1-a)}{T}
=1-\frac{s^2}{T}.
\]
The coefficient of \(a\) cancels exactly: \(q(s^2-1)+2q(1+s)-q(1+s)^2=0\). Because \(m-1\ge2\), the transverse block occurs, so its largest eigenvalue gives \(\mu(P)\ge1-s^2/T\) for every invariant \(P\), hence for every feasible \(P\) by symmetry averaging.

**3. Matching construction and the remaining spectrum.** Choose
\[
a_*=\frac{s(1+s)}{T},\qquad b_*=\frac{1-qa_*}{m-1}.
\]
Then \(a_*>0\), \(qa_*<1\), \(b_*>0\), and the core holding probability vanishes. Direct substitution gives
\[
M(a_*,b_*)v=(1-s^2/T)v.
\]
Because its off-diagonal entry is positive and \(v\) is componentwise positive, this eigenvalue is the larger eigenvalue of \(M\). The trace of \(M\) at \(b=b_*\) is \(1-a_*-b_*\ge0\), since \(b_*\le1-a_*\), so its other eigenvalue has absolute value no greater than the larger one. The larger eigenvalue is at least \(1-a_*\) by the diagonal Rayleigh quotient, and thus also dominates the within-cluster leaf eigenvalues.

For the remaining nontrivial cluster-uniform eigenvalue \(\ell=1-(q+1)a_*\), if \(\ell\ge0\), then \(\ell\le1-a_*\). If \(\ell<0\) and \(q\ge2\), then \(|\ell|\le1/q\le1-a_*\) because \(a_*\le1/q\). For \(q=1\), \(a_*\le1/2\): indeed \(T-2s(1+s)\ge 2-s^2=(m-2)/(m-1)>0\). Hence \(\ell\ge0\) also in that case. Therefore every nonstationary eigenvalue has modulus at most \(1-s^2/T\), attaining the lower bound. Multiplying numerator and denominator by \(m-1\) yields the stated radical formulas.

**4. Invariant uniqueness and parameter transition.** The Rayleigh inequality in step 2 is strict if \(b<b_{\max}(a)\), since the first coordinate of \(v\) is nonzero. Equality at the optimum forces \(v\) to be an eigenvector of \(M(a,b_{\max}(a))\). Its second component gives uniquely \(a=s(1+s)/T\), and then \(b=b_*\). Thus the invariant optimum is unique. Finally,
\[
a_*-b_*=\frac{(m-1-q)(1+s)}{(m-1)T},
\]
which gives the stated sharp ordering transition. The two asymptotic statements follow from \(s\to1\) as \(m\to\infty\) and division of \(1-\mu_{m,q}=s^2/T\) by \(q\) as \(q\to\infty\), respectively.

## Verification
Run `python verify.py` after installing SymPy and NumPy. The verifier checks the symbolic Rayleigh cancellation, the claimed eigenvector and normalization identities, full stochastic matrices for \(3\le m\le8\) and \(1\le q\le7\) (also the known boundary \(m=2\)), and randomly sampled feasible competitors. These finite tests are reproducibility checks, not replacements for the preceding proof, which covers all integer \(m\ge3,q\ge1\) and all feasible symmetric matrices. The example \((m,q)=(3,2)\) has \(a_*=b_*=1/4\) and \(\mu_{3,2}\approx0.8623724357\).

## Relationship to prior work
Boyd, Diaconis and Xiao formulate the general FMMC semidefinite program and give the four-vertex path as a small exact example. Boyd, Diaconis, Parrilo and Xiao prove symmetry reduction and give exact or semianalytic results for several other families. Their general optimization framework applies here, but the inspected full-text examples and stated formulas do not contain the present two-parameter clique-corona value, the positive Rayleigh witness, or the edge-weight transition at \(q=m-1\). The present derivation uses and credits the known convex symmetry principle; the novelty claim concerns only the explicit corona-family classification. The graph \(K_2\circ\overline{K_1}\) is a four-vertex path and is excluded from the novel parameter range.

## Limitations
The result is for symmetric discrete-time chains with uniform stationary distribution and permitted holding probabilities; it does not optimize nonreversible chains, a fixed nonuniform stationary distribution, total-variation mixing at fixed times, or all possible constraints on self-loops. Uniqueness is proved only among graph-automorphism-invariant minimizers. The inspected literature and searchable research records do not establish publication priority conclusively; a specialist source outside the search corpus could contain an equivalent result. No independent mathematical audit has been performed.

## References
- S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264 (full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf).
- S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, preprint first posted 2007-09-06, https://arxiv.org/abs/0709.0955; SIAM J. Optimization 20 (2009), 792–819.
- S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, https://arxiv.org/abs/2111.05816 (general mixing bounds, not an inspected exact corona-family classification).
