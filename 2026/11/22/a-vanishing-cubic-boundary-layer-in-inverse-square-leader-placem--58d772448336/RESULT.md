# A vanishing cubic boundary layer in inverse-square leader placement on matching-weighted bipartite networks

## Finding

For each integer \(n\ge3\) and each real \(t>0\), form a weighted graph on \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\). Every edge \(u_iv_j\) with \(i\ne j\) has conductance one, while each edge \(u_iv_i\) has conductance \(t\); there are no within-part edges. Let \(L\) denote its unnormalized weighted graph Laplacian. For each two-vertex leader set \(S\), ground both leaders perfectly, let \(F\) be the remaining vertices, and minimize the exact inverse-square spectral objective
\[
J_2(S)=\operatorname{tr}\bigl((L_{FF})^{-2}\bigr).
\]
Here the original Laplacian diagonal is retained when grounding.

There is a unique threshold \(\theta_n\in(0,1/2)\) with the following **complete global optimizer classification**:

* If \(0<t<\theta_n\), the only minimizing leader sets are the \(n\) matching pairs \(\{u_i,v_i\}\).
* If \(t=\theta_n\), exactly the \(n\) matching pairs and the \(n(n-1)\) same-part pairs minimize, for a total of \(n^2\) pairs.
* If \(t>\theta_n\), exactly the \(n(n-1)\) same-part pairs minimize.

Every unmatched cross-part pair is strictly suboptimal for every \(t>0\). The threshold is the unique positive zero of the explicitly defined degree-six polynomial \(Q_n\) in the Proof section. It has the sharp expansion
\[
\boxed{\theta_n=\frac12-\frac{3}{4n^3}-\frac{3}{8n^4}+O(n^{-5})}.
\]

For the first inverse-power objective \(J_1(S)=\operatorname{tr}(L_{FF}^{-1})\), the corresponding known threshold \(\gamma_n\) has \(\gamma_n=1/2-1/(2n^2)+O(n^{-3})\). Therefore the objectives choose disjoint optimal pair types throughout a **nonempty interval** \((\gamma_n,\theta_n)\) for all sufficiently large \(n\), and its width is
\[
\boxed{\theta_n-\gamma_n=\frac{1}{2n^2}+O(n^{-3})}.
\]
There is an exact small-network witness already at \(n=3\) and \(t=9/20\): the difference \(J_1(\mathrm{matched})-J_1(\mathrm{same})=745/72618>0\), whereas \(J_2(\mathrm{matched})-J_2(\mathrm{same})=-83084401/5273373924<0\). In this network first-order coherence favors same-part leaders, while inverse-square coherence favors matched leaders.

## Assumptions and scope

The result concerns an undirected positively weighted bipartite network of order \(2n\), exactly two perfectly grounded leaders, and the squared inverse of the *combinatorial*, not normalized, grounded Laplacian. All weights except those on the prescribed perfect matching equal one. A standard relative-velocity-damped second-order consensus model has position variance proportional to \(J_2\); the theorem itself requires only the stated algebraic objective. All conclusions include tie multiplicities. They do not assert the same classification for finite-gain leaders, other weights, different leader budgets, or higher inverse powers.

## Proof

Write
\[
d=n-1+t,\quad h=t-1,\quad f(z)=\frac{2(d^2+z)}{(d^2-z)^2}.
\]
The full weighted adjacency off-diagonal block is \(J_n+hI_n\), and the common weighted degree is \(d\). By simultaneous permutation of matched indices and interchange of the bipartition classes, all unordered leader pairs fall into exactly three orbits: same-part, matched cross-part, and unmatched cross-part. Every grounded Laplacian is positive definite, since the full graph is connected and at least one vertex is grounded.

**Exact orbit costs.** Denote their respective inverse-square traces by \(S_n(t)\), \(M_n(t)\), and \(U_n(t)\). For a bipartite block matrix \(\begin{psmallmatrix}dI_a&-B\\-B^T&dI_b\end{psmallmatrix}\), each singular value \(s\) of \(B\) contributes \((d+s)^{-2}+(d-s)^{-2}=f(s^2)\); its remaining \(|a-b|\) eigenvalues are \(d\).

If both leaders are in the same part, there are two extra eigenvalues \(d\), \(n-3\) singular values \(|h|\), and one whose square is \(h^2+(n-2)(n+2h)\). Therefore
\[
S_n=\frac{2}{d^2}+(n-3)f(h^2)+f\bigl(h^2+(n-2)(n+2h)\bigr).
\]
For a matched cross-part pair, the remaining cross block is \(J_{n-1}+hI_{n-1}\), whose singular values are \(|h|\) (multiplicity \(n-2\)) and \(d-1\). Thus
\[
M_n=(n-2)f(h^2)+f\bigl((d-1)^2\bigr).
\]
For an unmatched cross-part pair, the remaining cross block can be reordered to \(J_{n-1}+h\operatorname{diag}(I_{n-2},0)\). It has \(n-3\) singular values \(|h|\); the remaining two are the absolute eigenvalues of the two-dimensional symmetric compression
\[
B_*=\begin{pmatrix}n-2+h&\sqrt{n-2}\\\sqrt{n-2}&1\end{pmatrix}.
\]
Its trace is \(T=d-1\), its determinant is \(h\), and the product of \((d^2-\lambda^2)\) over its eigenvalues is
\[
P=d^4-d^2(T^2-2h)+h^2>0.
\]
Putting \(A=2d^2-T^2+2h\) and summing the two rational terms yields
\[
U_n=(n-3)f(h^2)+\frac{4d^2(A^2-2P)}{P^2}-\frac{2A}{P}.
\]
These are complete exact formulas for the objective of **every** leader pair, not sample approximations.

**Unique matched-to-same transition.** Let
\[
D_n=n^2d^2(n+2t-2)^2(2n+2t-3)^2>0,
\qquad Q_n(t)=D_n\bigl(M_n(t)-S_n(t)\bigr).
\]
Cancellation shows that \(Q_n\) is a polynomial of degree six. The fully explicit coefficients in powers of \(t\), after setting \(u=n-3\ge0\), are displayed in `CERTIFICATES.md`: its constant coefficient is strictly negative, its coefficients of orders two through six are strictly positive, and its linear coefficient may have either sign. Descartes' rule of signs therefore gives at most one positive zero. Since \(Q_n(0)<0\) and
\[
Q_n(1/2)=(n-1)^2(6n^2-6n+1)>0,
\]
exactly one zero \(\theta_n\) exists in \((0,1/2)\), with \(M_n<S_n\) below it and \(M_n>S_n\) above it. All denominators remain positive throughout the domain.

**Why unmatched pairs never win.** If \(0<t<1\), the reordered unmatched follower block \(B_U=J_{n-1}+h\operatorname{diag}(I_{n-2},0)\) dominates the matched block \(B_M=J_{n-1}+hI_{n-1}\) entrywise and strictly. Both associated positive-definite grounded matrices have nonnegative inverse Neumann series. Entrywise monotonicity of the inverse, with a strict affected entry, implies \(U_n>M_n\). If \(t\ge1\), exact cancellation gives
\[
U_n-S_n=\frac{R_n(t)}{d^2(n+2t-2)^2H_n(t)^2},
\quad H_n=2n^2+4nt-5n+2t^2-4t+2>0.
\]
The expansion of \(R_{u+3}(v+1)\) in \(u=n-3\ge0\) and \(v=t-1\ge0\) has strictly positive coefficients (all displayed in `CERTIFICATES.md`), so \(U_n>S_n\) for \(t\ge1\). Because \(\theta_n<1/2\), these two bounds exclude unmatched pairs globally. The three-orbit reduction then supplies the complete list of all optimizers and tie multiplicities.

**Two different boundary scales.** Substituting \(t=1/2-a/n^3-b/n^4\) into \(Q_n\) gives, after multiplication by \(n^{-7}\), successive coefficients \(6-8a\) and \(28a-8b-18\) in orders \(n^{-3}\) and \(n^{-4}\). The unique root has \(a=3/4\), \(b=3/8\); the nonzero derivative near the root validates the stated remainder. The first-power threshold is the unique positive zero of the cubic
\[
P_n(t)=2(n+2)t^3+(4n^2-n-14)t^2+2(n-2)(n^2-n-4)t-(n-2)(n^2-3),
\]
which follows by replacing \(f(z)\) above with \(2d/(d^2-z)\). This polynomial has value \(n-1\) at \(t=1/2\) and derivative \(2n^3+O(n^2)\) there, so its root is \(\gamma_n=1/2-1/(2n^2)+O(n^{-3})\). Subtraction proves the asserted disagreement interval and width for sufficiently large \(n\); the rational witness establishes a finite, strict disagreement independently.

## Verification

The bundled `verify.py` with `requirements.txt` performs exact polynomial cancellation and coefficient-sign checks, confirms the rational witness and the two asymptotic coefficients, and constructs exact grounded Laplacians independently for integer sizes \(3\le n\le6\) and five rational matching weights. It verifies the three orbit formulas and, for \(3\le n\le5\), every unordered leader pair against the corresponding orbit representative (500 exact grounded-matrix checks). The code can be run with `python verify.py` after installing the specified dependency. The proof for all \(n\) and all real \(t>0\) is the analytic orbit reduction, polynomial sign certificates and monotone resolvent argument, not finite enumeration.

## Relationship to prior work

Fitch and Leonard's 2014 joint-centrality framework establishes general first-order leader-placement formulas using resistance and biharmonic distance, but does not give this inverse-square threshold. The previously published *A cubic two-leader coherence transition on matching-weighted bicliques* establishes the first-power cubic \(P_n\) on the same weighted graph; the present sixth-degree threshold and cubic boundary-layer scale do not follow from its first-power statement. Patterson and Bamieh study second-order stochastic coherence on fractal graphs rather than a two-leader weighted biclique. Mackin and Patterson derive general higher-order coherence objectives and note that optimal leaders can differ by dynamical order, but do not supply this graph-specific classification or its sharp scale. A generic symbolic inverse formula also does not imply the sign certificates, all-pair classification, or asymptotic separation without additional reasoning.

## Limitations

The theorem is restricted to the uniform off-matching weight and uniform positive matching conductance; it is not an arbitrary weighted-graph classification. The phrase "second-order" denotes the squared inverse grounded Laplacian objective, which is proportional to position variance for a specified relative-velocity-damped second-order model, not every possible second-order noise model. The strict separation theorem is asymptotic (all sufficiently large \(n\)), while an explicit small-size witness is supplied; no claim of an all-size ordering of the first- and second-power thresholds is required. The work has undergone an internal mathematical check, not independent validation. An equivalent result in unindexed literature remains possible.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public 2014-07-07, https://arxiv.org/abs/1407.1569. Relevant accessible full-text sections were inspected for general spectral formulas and its solved families.
2. *A cubic two-leader coherence transition on matching-weighted bicliques*, publicly available mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-cubic-two-leader-coherence-transition-on-matching-weighted-bic--06bc40f827e8. Its complete `RESULT.md` was inspected for the exact first-power theorem and proof.
3. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592, first public 2013-10-09, https://arxiv.org/abs/1310.2592. Relevant accessible full-text sections inspected, including the second-order spectral coherence setting.
4. E. Mackin and S. Patterson, *Submodularity in Systems with Higher Order Consensus with Absolute Information*, arXiv:1905.09156, first public 2019-05-22, https://arxiv.org/abs/1905.09156. Relevant accessible full-text sections inspected for the general higher-order leader-selection setting and examples.
5. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first public 2014-12-20, https://arxiv.org/abs/1412.6595. Relevant accessible full-text sections cover path and cycle graphs, not the matching-weighted complete bipartite family.
