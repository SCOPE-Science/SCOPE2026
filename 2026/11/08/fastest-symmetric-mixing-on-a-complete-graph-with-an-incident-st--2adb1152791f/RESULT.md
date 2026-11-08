# Fastest symmetric mixing on a complete graph with an incident star of deleted edges

## Finding

Let \(a\ge1\) and \(b\ge2\) be integers and set \(N=1+a+b\). From \(K_N\), choose a distinguished vertex \(v\) and delete its edges to exactly \(b\) vertices. Write \(A\) for its remaining \(a\) neighbors and \(B\) for its \(b\) nonneighbors. All edges within \(A\cup B\) remain. Among all real symmetric nonnegative row-stochastic matrices \(P\) supported on this graph (with holding permitted), define \(\mu_*(a,b)=\min_P\|P-J_N/N\|_2\).

Write \(D=a(b+1)+4b\), \(H=4b-2a^2-ab-a\), and \(N=a+b+1\). Then

\[
\mu_*(a,b)=\begin{cases}
\sqrt{\dfrac{b}{(a+1)(a+b)}},& b\le a^2,\\[5pt]
\sqrt{1-\dfrac{N(b-a)(a-1)}{a(b-1)^2}},&b>a^2\text{ and }H\le0,\\[5pt]
\dfrac{4b-a^2}{D},&b>a^2\text{ and }H>0.
\end{cases}
\]

These three formulas agree at their shared boundaries. One globally optimal matrix is specified by giving probability \(x\) to each edge from \(v\) to \(A\), probability \(w\) to each edge between \(A\) and \(B\), probability \(y\) between distinct \(A\)-vertices, and probability \(z\) between distinct \(B\)-vertices:

\[
(x,w)=\begin{cases}
(1/(a+1),\;1/(a+b)), & b\le a^2,\\
((b-a)/(a(b-1)),\;(a-1)/(a(b-1))), &b>a^2,\ H\le0,\\
((a+2b)/D,\;(a+2)/D),&b>a^2,\ H>0,
\end{cases}
\qquad y=\frac{1-x-bw}{a},\quad z=\frac{1-aw}{b}.
\]

All diagonal entries are the nonnegative stochastic remainders. Explicitly, the holding probabilities are \(1-ax\) at \(v\), \(y\) at each vertex of \(A\), and \(z\) at each vertex of \(B\). Thus within \(A\) and within \(B\), every entry, diagonal included, is constant. Existence of this optimal matrix is asserted; uniqueness among all optimizers is not asserted.

In the regime \(b>a^2\), the optimal family has zero \(A\)-to-\(A\) probability and zero holding at \(A\), because \(x+bw=1\). The second transition \(H=0\) separates a balanced pair of opposite nontrivial eigenvalues from a regime in which only the positive nontrivial eigenvalue determines the optimum. In particular, the third regime occurs only for \(a=1,2,3\), respectively at \(b\ge2\), \(b\ge6\), and \(b\ge22\). For \(a\ge4\), the third regime never occurs.

## Assumptions and scope

The graph is simple, connected, and undirected; \(a,b\) are arbitrary integers in the stated ranges. Transition probabilities may be zero on existing edges and may include self-loops. Symmetry \(P=P^\top\), entrywise nonnegativity, and row sums one are required. There are no restrictions to a heuristic Markov kernel, equitable-quotient kernels, or uniform edge probabilities in the optimization. The objective is the centered spectral norm / second-largest eigenvalue modulus, not a hitting time or a total-variation mixing time at a fixed step.

## Proof

**1. Symmetrization and exact eigenvalue reduction.** The operator norm \(\|P-J_N/N\|_2\) is convex and invariant under permuting the \(A\) vertices and independently permuting the \(B\) vertices. Averaging any feasible optimizer over \(S_a\times S_b\) therefore retains feasibility and does not increase the objective. Thus a global optimum may be chosen invariant under these permutations.

An invariant matrix has edge probabilities \(x,y,z,w\) as defined above and holding probabilities \(1-ax\), \(1-x-(a-1)y-bw\), and \(1-(b-1)z-aw\), respectively. Necessarily
\[x,w\ge0,\quad ax\le1,\quad x+bw\le1,\quad aw\le1.\]
On the \(A\)-sum-zero and \(B\)-sum-zero subspaces its eigenvalues are, respectively,
\[1-x-ay-bw\quad\text{and}\quad1-aw-bz.\]
For every feasible \(x,w\), choosing \(y=(1-x-bw)/a\) and \(z=(1-aw)/b\) is feasible and makes both these eigenvalues zero without changing the three-block constant-vector restriction. Hence the global minimization is *exactly* the two-variable optimization for the latter restriction: no hidden internal eigenspace constraint is lost.

For the centered block-constant subspace, the weighted Laplacian \(L=I-P\) has two nonzero eigenvalues \(\lambda_-\le\lambda_+\), which satisfy
\[
\lambda_-+\lambda_+=(a+1)x+(a+b)w=:S,\qquad
\lambda_-\lambda_+=Na xw.
\]
This follows directly from the three-state symmetric quotient
\[
Q=\begin{pmatrix}
1-ax&\sqrt a x&0\\
\sqrt a x&1-x-bw&\sqrt{ab}w\\
0&\sqrt{ab}w&1-aw
\end{pmatrix}
\]
whose fixed eigenvector is \((1,\sqrt a,\sqrt b)^\top/\sqrt N\). The centered objective is \(\max(|1-\lambda_-|,|1-\lambda_+|)\).

For clarity, let \(e_A\) and \(e_B\) denote the normalized all-ones vectors of their respective blocks. In the orthonormal basis
\[
 u=\frac{\sqrt a\,e_v-e_A}{\sqrt{a+1}},\qquad
 v=\sqrt{\frac bN}\,\frac{e_v+\sqrt a\,e_A}{\sqrt{a+1}}-\sqrt{\frac{a+1}{N}}e_B,
\]
of the two-dimensional block-constant subspace orthogonal to all ones, the Laplacian restriction is exactly
\[
 L_\perp=\begin{pmatrix}
 (a+1)x+\dfrac{bw}{a+1}&-\dfrac{\sqrt{abN}}{a+1}w\\
 -\dfrac{\sqrt{abN}}{a+1}w&\dfrac{aN}{a+1}w
 \end{pmatrix}.
\]
In particular, fixing \(w\) and varying \(x\) changes only its first diagonal entry. This identity underlies the fixed-\(w\) minimization in Step 3.

**2. Universal lower bound and its first equality phase.** Let \(e_v\) be the distinguished coordinate vector. Since \(P_{B,v}=0\) and \(P e_v\) sums to one, Cauchy--Schwarz on the \(a+1\) available entries of \(P e_v-J_N e_v/N\) yields
\[
\|(P-J_N/N)e_v\|_2^2\ge\frac{b}{N(a+1)}.
\]
Also \(\|e_v-\mathbf1/N\|_2^2=(N-1)/N\). Thus
\[
\mu(P)^2\ge \frac{b}{(a+1)(a+b)}.
\]
For \(b\le a^2\), take \(x=1/(a+1)\), \(w=1/(a+b)\). The row feasibility inequality \(x+bw\le1\) is equivalent to \(b\le a^2\). The two nonzero Laplacian eigenvalues satisfy \(S=2\) and their completed-step eigenvalues are exactly opposite, each of modulus \(\sqrt{b/((a+1)(a+b))}\). With internal eigenvalues zero, the lower bound is attained.

**3. Reduction beyond the first boundary.** Suppose \(b>a^2\). Then \(b>a\ge1\) and the constraints imply \(0\le w\le1/b\), \(0\le x\le1-bw\). Define
\[
 w_B=\frac{a-1}{a(b-1)},\qquad x_B=\frac{b-a}{a(b-1)},\qquad
 x_0(w)=\frac{2-(a+b)w}{a+1}.
\]
For fixed \(w\), the restriction \(P-J_N/N\) is a real symmetric \(2\times2\) matrix with \(x\) affecting only one diagonal entry, and trace \(2-S\). For any fixed other diagonal entry and fixed off-diagonal, its operator norm is minimized over all real values of that entry at trace zero. This follows immediately from
\[
\left\|\begin{pmatrix}u&c\\c&d\end{pmatrix}\right\|_2
=\frac{|u+d|}{2}+\sqrt{\frac{(u-d)^2}{4}+c^2}.
\]
Trace zero corresponds to \(x=x_0(w)\). If \(w\le w_B\), the unconstrained fixed-\(w\) lower bound has square
\[
1-\frac{Na}{a+1}w\,[2-(a+b)w].
\]
Because \(w_B<1/(a+b)\) when \(b>a^2\), this lower bound decreases on \([0,w_B]\); its value at \(w_B\) is
\[
\mu_B=\sqrt{1-\frac{N(b-a)(a-1)}{a(b-1)^2}}.
\]
If \(w>w_B\), then \(x_0(w)>1-bw\). The objective decreases as \(x\) increases up to \(x_0(w)\), hence the best feasible choice for that \(w\) is \(x=1-bw\), and it has positive centered trace. The norm is then \(1-\lambda_-(w)\), where \(\lambda_-(w)\) denotes the smaller positive eigenvalue of the quotient Laplacian along that boundary.

**4. Second boundary and one-sided phase.** Along \(x=1-bw\), \(\lambda_-(w)\) is the smallest eigenvalue of an affine symmetric \(2\times2\) Laplacian restriction, hence concave. Put
\[
D=a(b+1)+4b,\quad w_S=\frac{a+2}{D},\quad x_S=\frac{a+2b}{D}.
\]
The block-constant vector taking values \(a+2b\) at \(v\), \(b-1\) on \(A\), and \(-(a+2)\) on \(B\), is perpendicular to constants and has squared norm \(ND\). Both existing interblock edge types see squared difference \(N^2\). Therefore for every feasible \(x,w\) its Rayleigh quotient gives the universal bound
\[
\lambda_-\le\frac{aN(x+bw)}{D}\le\frac{aN}{D}.
\]
At \((x_S,w_S)\), direct substitution into the quotient eigenvalue equation gives \(\lambda_-=aN/D\), so \(w_S\) is a global maximizer of the concave boundary function.

A direct subtraction yields
\[
 w_S-w_B=\frac{H}{a(b-1)D},\qquad H=4b-2a^2-ab-a.
\]
If \(H\le0\), then \(w_S\le w_B\), and concavity forces \(\lambda_-(w)\) to be nonincreasing on \([w_B,1/b]\). Hence the minimum centered norm beyond \(w_B\) is attained at \(w_B\), where the quotient eigenvalues are \(\pm\mu_B\). Combined with Step 3, this proves the middle formula.

If \(H>0\), then \(w_S>w_B\), and the Rayleigh bound gives \(\mu(P)\ge1-aN/D=(4b-a^2)/D\) for all feasible kernels. At \((x_S,w_S)\), the quotient Laplacian eigenvalues are \(aN/D\) and \((a+2)(a+2b)/D\), so its two nontrivial Markov eigenvalues are
\[
\frac{4b-a^2}{D},\qquad -\frac{aN}{D}.
\]
The first dominates in modulus exactly when \(H\ge0\), proving attainment and the third formula. These parameters are feasible: \(x_S+bw_S=1\), \(x_S\le1/a\), \(aw_S\le1\) in the stated regime. At \(H=0\) the two expressions agree.

## Verification

The accompanying standalone `verify.py` uses only Python's standard-library `fractions.Fraction`. Executing `python3 verify.py` checks exact rational feasibility, full stochastic matrices for small orders, block-internal eigenvalues, quotient characteristic coefficients, each regime's asserted norm and boundary inequalities, including 1,462 deterministic parameter combinations. Its reported success condition is `EXACT_VERIFY_OK`. This is a finite consistency check; the proof above supplies the universal quantification.

## Relationship to prior work

Boyd, Diaconis and Xiao formulate symmetric fastest mixing as spectral-norm/semidefinite optimization and show automorphism averaging; Boyd, Diaconis, Parrilo and Xiao derive structural reductions and exact results for edge-transitive and distance-transitive families, with examples including complete bipartite graphs, paths, two cliques joined by one bridge, and trees. Neither inspected primary document states the present complete-graph-minus-incident-star three-regime value and optimal kernel. The general SDP formulation is a method for *computing* an optimum, not an evaluated parameter classification for these graphs.

For a single missing edge, the known lower-bound equality for complete graphs minus matchings covers \(b=1\); that case is outside the claimed new range. The missing-neighbor lower bound used in Step 2 is presented solely as a proof ingredient, not as a separate novelty claim. The assessed contribution is the exact complete solution for every \(b\ge2\), including the two additional transition mechanisms and optimal constructive kernels.

## Limitations

The classification assumes symmetric stochastic transitions and uniform equilibrium, not general reversible chains with nonuniform stationary law. The displayed kernels establish existence, not uniqueness of arbitrary optimal matrices. Publication-priority novelty is subject to additional specialized literature that may not be indexed or accessible; no independent audit has been performed.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667--689. Public electronic version October 29, 2004. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf ; DOI 10.1137/S0036144503423264.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first posted September 6, 2007. https://arxiv.org/pdf/0709.0955 ; subsequently SIAM J. Optim. 20 (2009), 792--819.
