# Universal apex saturation in Kemeny-optimal double-cone walks and an unbounded cyclic baseline gap

## Finding
Let \(H\) be a connected simple graph on \(n\ge3\) vertices, regular of degree \(d\), and both vertex- and edge-transitive. Form its **double cone** \(G=\overline{K_2}\vee H\) by adding two *nonadjacent* apexes, each joined to every vertex of \(H\). Consider every symmetric, entrywise nonnegative, row-stochastic transition matrix \(P\) whose off-diagonal support is contained in the edges of \(G\), allowing arbitrary holding probabilities. A disconnected chain is assigned infinite objective. Define the Kemeny spectral sum
\[
\mathcal K(P)=\sum_{j=2}^{n+2}\frac{1}{1-\lambda_j(P)},
\]
where \(1=\lambda_1(P)\ge\lambda_2(P)\ge\cdots\) are the real transition eigenvalues; this is the stationary-target mean hitting-time convention that excludes an additional constant sometimes included for return visits.

**Theorem.** The unrestricted global minimizer exists and is **unique**. Its transition probabilities are
\[
\boxed{\ P_{uv}=\begin{cases}
1/n,&\text{if one of }u,v\text{ is an apex and the other lies in }H,\\
(n-2)/(nd),&\text{if }\{u,v\}\text{ is an edge of }H,\\
0,&u=v.
\end{cases}\ }
\]
All other entries are zero. In particular, all graph edges are used, no vertex holds, and the optimal apex probability depends only on the number of base vertices, even though the base graph may have very different eigenvalues.

For cyclic bases \(H=C_n\), writing \(r_n=1-2/n\) and
\[
q_n=\frac{1-\sqrt{1-r_n^2}}{r_n},
\]
the exact minimum is
\[
\boxed{\mathcal K_n^*=1+\frac{n}{n+2}-\frac n2+
\frac{n^2}{2\sqrt{n-1}}\frac{1+q_n^n}{1-q_n^n}.}
\]
It satisfies \(\mathcal K_n^*=\tfrac12 n^{3/2}+O(n)\). For \(n\ge4\), compare the feasible **maximum-degree walk** assigning transition probability \(1/n\) on every edge (and putting the remaining probability on the base diagonal). With \(q_0=2-\sqrt3\), its exact Kemeny sum is
\[
\mathcal K_n^{\mathrm{md}}=1+\frac n{n+2}-\frac n2+
\frac{n^2}{2\sqrt3}\frac{1+q_0^n}{1-q_0^n}.
\]
Thus, unlike the optimum, its objective grows quadratically, and
\[
\boxed{\frac{\mathcal K_n^{\mathrm{md}}}{\mathcal K_n^*}\sim\sqrt{\frac n3}.}
\]
The gap is zero at \(n=4\) and strictly positive for every \(n\ge5\).

## Assumptions and scope
The graph is simple, undirected and connected, with \(n\ge3\), positive regular degree \(d\), and transitivity on both vertices and edges of its base. Apexes are distinct and nonadjacent. Edge probabilities are symmetric, stochastic and nonnegative; diagonal probabilities are unconstrained apart from the row sums. Neither symmetry among individual edge probabilities nor positivity of every available edge is assumed in the optimization. No edge prices, nonuniform stationary measures, nonreversible policies or external holding constraints are included. The claimed uniqueness is over **all** admissible individual off-diagonal weights, not merely over the two edge-orbit parameters.

## Proof
**1. Strict convexity and global uniqueness.** Set \(L(P)=I-P\). For a connected feasible chain, \(L(P)\) is positive definite on \(\mathbf1^\perp\). If \(Q\) has orthonormal columns spanning that subspace, then \(\mathcal K(P)=\operatorname{tr}[(Q^TL(P)Q)^{-1}]\). Along a nonzero symmetric perturbation \(D\) of this positive definite matrix, the second derivative is
\[
2\operatorname{tr}(A^{-1}DA^{-1}DA^{-1})>0.
\]
To verify the strict inequality, diagonalize \(A\) or write \(A^{-1/2}DA^{-1/2}=B\), giving \(2\operatorname{tr}(BA^{-1}B)>0\) for \(D\ne0\). Different edge-weight arrays give different Laplacians and hence different restrictions to \(\mathbf1^\perp\); the latter is injective for zero-row-sum matrices. Thus the objective is strictly convex in all individual feasible edge weights whenever it is finite. A connected feasible chain exists; on the compact stochastic polytope, the inverse trace diverges when a nontrivial Laplacian eigenvalue approaches zero, so the minimum is attained at a connected chain. It is unique.

**2. Symmetry is proved, not assumed.** Each automorphism of \(H\), together with the interchange of the two apexes, preserves the feasible set and the objective. The unique optimal matrix must be invariant under all such conjugations. Vertex- and edge-transitivity of \(H\) yield exactly two off-diagonal classes: probability \(a\) on each apex-base edge, and \(b\) on each base edge. Their constraints are
\[
0\le a\le1/n,\qquad b\ge0,\qquad 2a+db\le1.
\]
Each apex has holding probability \(1-na\), and each base vertex has holding probability \(1-2a-db\).

**3. Exact spectrum.** Let \(0=\eta_1<\eta_2\le\cdots\le\eta_n\le2d\) be the Laplacian eigenvalues of \(H\). The nonzero eigenvalues of \(L(P)\), with multiplicities, are
\[
na,\quad (n+2)a,\quad 2a+b\eta_2,\ldots,2a+b\eta_n.
\]
Indeed, the apex difference and apex-versus-base contrast generate the first two eigenmodes, while every mean-zero base eigenvector extended by zeros on both apexes gives the remaining mode. They exhaust the orthogonal complement of constants. Therefore
\[
\mathcal K(a,b)=\frac1{na}+\frac1{(n+2)a}+\sum_{i=2}^n\frac1{2a+b\eta_i}.
\]
Since every \(\eta_i>0\), increasing \(b\) strictly reduces the objective at fixed \(a>0\). Thus any optimum must have \(b=(1-2a)/d\), saturating every base row.

**4. A strictly decreasing one-parameter objective.** Put \(s_i=\eta_i/d\), so \(0<s_i\le2\), and \(c=1/n+1/(n+2)\). Substitution gives
\[
F(a)=\frac ca+\sum_{i=2}^n\frac1{s_i+2a(1-s_i)},\qquad 0<a\le1/n.
\]
Its derivative is
\[
F'(a)=-\frac c{a^2}-\sum_{i=2}^n\frac{2(1-s_i)}{[s_i+2a(1-s_i)]^2}.
\]
For \(s_i\le1\), the corresponding term is nonpositive. For \(1<s_i\le2\), the corresponding term is positive but at most \(2(s_i-1)\le2\), since \(s_i+2a(1-s_i)=1+(s_i-1)(1-2a)\ge1\). Hence, uniformly over every permitted base and \(a\),
\[
F'(a)\le-\frac c{a^2}+2(n-1)
\le -cn^2+2(n-1)=-\frac4{n+2}<0.
\]
Consequently \(a=1/n\) is the unique minimizer, and \(b=(n-2)/(nd)\). Both holding classes vanish. Strict convexity in Step 1 upgrades this to the unique unrestricted optimum.

**5. Exact cyclic formula and its scale.** For \(H=C_n\), \(d=2\), and \(\eta_k=2-2\cos(2\pi k/n)\). At the optimum, the nontrivial base-mode eigenvalues are \(1-r_n\cos(2\pi k/n)\), \(1\le k<n\). For \(0<r<1\) define \(q=(1-\sqrt{1-r^2})/r\). The Poisson-kernel Fourier expansion gives
\[
\sum_{k=0}^{n-1}\frac1{1-r\cos(2\pi k/n)}
=\frac n{\sqrt{1-r^2}}\frac{1+q^n}{1-q^n}.
\]
One proof is to expand \((1-r\cos\theta)^{-1}=(1-r^2)^{-1/2}\sum_{j\in\mathbb Z}q^{|j|}e^{ij\theta}\) and use the root-of-unity filter; the only surviving Fourier indices are multiples of \(n\). Subtract the \(k=0\) term \(1/(1-r_n)=n/2\) and add the two apex modes \(1+n/(n+2)\) to obtain the exact expression. Since \(\sqrt{1-r_n^2}=2\sqrt{n-1}/n\) and \(q_n^n=O(e^{-c\sqrt n})\) for some \(c>0\), its leading term is \(n^{3/2}/2\), with error \(O(n)\).

For the maximum-degree walk with \(n\ge4\), the base row has residual holding probability \(1-4/n\). Its base eigenvalues are \((4-2\cos(2\pi k/n))/n\); the same Fourier identity with \(r=1/2\) yields the stated formula with \(q_0=2-\sqrt3\). The leading term is \(n^2/(2\sqrt3)\), with error \(O(n)\). Dividing proves the \(\sqrt{n/3}\) performance ratio. For \(n=4\), both constructions give \(a=b=1/4\); for \(n\ge5\), they differ on existing base edges, so uniqueness makes the comparison strict.

## Verification
The standalone `verify.py` reconstructs double-cone transition matrices on cycles, cliques, hypercubes and the Petersen graph. It independently diagonalizes full transition matrices and base Laplacians, compares the exact spectral formula and finite cyclic resolvent sums, checks strict improvement toward the apex-row boundary, and solves small instances over individual edge probabilities by numerical constrained optimization. It also tests both leading asymptotic coefficients and the baseline gap on larger cycles. Run `python verify.py` with Python 3, NumPy and SciPy installed. The finite tests do **not** establish unrestricted uniqueness, the all-graph statement or either infinite asymptotic; Steps 1–5 provide those proofs.

## Relationship to prior work
Patel, Agharkar and Bullo developed convex and semidefinite formulations for minimizing reversible-chain Kemeny constants, but their inspected full work does not determine the double-cone optimum or its cyclic scaling. Boyd, Diaconis, Parrilo and Xiao analyzed symmetric fastest mixing through graph automorphisms and, for individual graph families, explicit spectral minimax formulas. A later published three-phase theorem for **double cones** uses their spectrum to optimize the *second-largest eigenvalue modulus*: that objective is different from the inverse-eigenvalue **sum** here, so its three-phase allocation does not settle the claimed universal Kemeny saturation. The Laplacian invariant-subspace decomposition is shared background, not claimed new. For example, when \(H=K_n\), the prior SLEM formula assigns apex probability \(1/(n+1)\), whereas the Kemeny optimizer here assigns \(1/n\); the two objectives genuinely choose different kernels. Zhang, Sheng, Hu and Chen study Kemeny constants of fixed simple-random-walk network families; optimizing all symmetric transition weights on double cones is a different problem. The Kemeny definition, convexity, and symmetry reduction are prior tools; the new claims concern the full optimizer, explicit cycle constant and divergent baseline ratio.

## Limitations
The result assumes a regular connected vertex- and edge-transitive base, two nonadjacent apexes, uniform stationary distribution and symmetric stochastic matrices with free diagonal. It does not address arbitrary asymmetric bases, nonuniform prescribed stationary measures, irreversible chains, or separate edge prices. The numerical verifier is supportive rather than a certificate for the infinite claim. A literature search cannot exclude every unindexed or inaccessible equivalent result.

## References
- S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first posted September 6, 2007, https://arxiv.org/abs/0709.0955. Relevant for graph automorphisms and spectral mode reduction, but a distinct minimax objective.
- R. Patel, P. Agharkar, and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), 3156–3167, DOI 10.1109/TAC.2015.2426317; lawful full text https://motion.me.ucsb.edu/pdf/2014b-pab.pdf. Relevant for the reversible Kemeny inverse-trace objective and its convexity.
- Z. Zhang, Y. Sheng, Z. Hu, and G. Chen, *Optimal and suboptimal networks for efficient navigation measured by mean-first passage time of random walks*, arXiv:1211.4295v1, first posted November 19, 2012, https://arxiv.org/abs/1211.4295. Relevant to the Kemeny interpretation on fixed random-walk networks.
- *A three-phase fastest-mixing law for double cones over transitive graphs*, previously published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-three-phase-fastest-mixing-law-for-double-cones-over-transitiv--7fd543281a6a. Relevant for the same graph family under the SLEM rather than Kemeny objective.
