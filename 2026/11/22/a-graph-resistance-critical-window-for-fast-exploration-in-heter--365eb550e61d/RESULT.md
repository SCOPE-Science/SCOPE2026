# A graph-resistance critical window for fast exploration in heterogeneous metapopulations

## Finding

Let \(G\) be any fixed connected, positively weighted, undirected habitat graph on \(n\ge2\) patches. For positive local recruitment-to-extinction ratios \(b=(b_1,\ldots,b_n)^T\), put \(s=\sum_i b_i\), \(L\) for its combinatorial graph Laplacian, and \(L^+\) for the Moore–Penrose inverse. Let \(a=1+g>0\), where \(g\) is explorer mortality relative to colonization rate, and \(f>0\) the explorer-movement parameter. With source-local explorer birth and equal patch capacities, the effective kernel and invasion factor are

\[
K_f=(aI+fL)^{-1},\qquad \mathcal R_f=\rho(K_f\operatorname{diag}(b)).
\]

**Fast-exploration theorem.** For each fixed graph and fixed positive \(a,b\),

\[
\mathcal R_f=\frac{s}{na}+\frac{b^TL^+b}{s f}+O_{G,a,b}(f^{-2})\quad(f\to\infty).
\]

The correction \(b^TL^+b/s\) is positive exactly when the local ratios are not all equal. Define

\[
Q_G=\frac{na\,b^TL^+b}{s^2},\qquad
h_f=\frac{na}{s}\left(1-\frac{\eta}{f}\right),\quad \eta\in\mathbb R.
\]

For all sufficiently large \(f\), the scaled linear invasion factor \(h_f\mathcal R_f\) is strictly greater than one when \(\eta<Q_G\) and strictly less than one when \(\eta>Q_G\). No assertion is made for \(\eta=Q_G\). For an existing edge of positive conductance, or a newly added edge of positive conductance after it is introduced, the topology-dependent coefficient satisfies

\[
\frac{\partial Q_G}{\partial w_{uv}}=-\frac{na}{s^2}(\phi_u-\phi_v)^2,\quad
L\phi=b-\frac{s}{n}\mathbf 1,\quad\mathbf1^T\phi=0.
\]

Here the derivative is taken for a conductance varying within a connected graph, with all other data fixed. It is strictly negative exactly when the two endpoint potentials differ.

**Three-habitat invasion reversal.** Take \(n=3\), \(b=(3,2,1)^T\), \(a=2\), \(f=10\), and multiply all recruitment rates by \(h=49/50\). On the unit-weight path \(1-2-3\), \(h\mathcal R_f>1\). Add the unit-weight corridor \(1-3\) without changing any local rate: on the triangle, \(h\mathcal R_f<1\). Correspondingly, \(Q_{\rm path}=1/3\), \(Q_{\rm triangle}=1/9\). The fixed finite-parameter example matches the fast-exploration asymptotic comparison with \(h=1-(1/5)/10\).

## Assumptions and scope

The source microscopic model distinguishes settled individuals from explorers. Settled densities \(p_i\in[0,1]\) obey

\[
\dot p_i=-e_i p_i+(1-p_i)\sum_j c_j(K_f)_{ij}p_j.
\]

Assume positive local extinction rates \(e_i\), positive explorer-production rates \(c_i\), equal patch capacities, symmetric positive movement weights along a connected graph, and source-local explorer birth \(C_{ij}=\delta_{ij}\). This last birth choice is explicitly permitted as an alternative in Section II.2 of Bernardi et al.; it differs from neighboring-patch birth \(C\propto A\), for which adding edges also changes explorer production. Set \(b_i=c_i/e_i\) and \(a=1+\gamma/\lambda\ge1\) in the original ecological interpretation (the algebra also holds for any \(a>0\)). The quasi-stationary explorer reduction is presumed valid. The source paper's theorem identifies the strict linear invasion threshold with the Perron root of \(K_f\operatorname{diag}(b)\); we use the same threshold. Varying \(h_f\) means scaling every \(c_i\) by the same positive factor while keeping \(e_i\) fixed. There is no limit in the number of patches: \(n\) is fixed while \(f\to\infty\).

## Proof

**1. Exact kernel reduction.** The source fast-exploration equations (5)–(11), with equal site capacities and symmetric movement, give \(F=aI+fL\). With birth-feasibility matrix \(C=I\), equation (9) reduces to \(K_f=F^{-1}\). Connectedness and \(a>0\) make \(F\) an irreducible nonsingular \(M\)-matrix, so \(K_f\) is strictly entrywise positive. Hence \(K_f B\), with \(B=\operatorname{diag}(b)\), has a unique positive simple Perron root, equal to the invasion factor of the linearized ecological equation.

**2. Uniform-mode expansion.** Write \(P=\mathbf1\mathbf1^T/n\). The Laplacian is symmetric, has simple zero eigenvalue on \(\mathbf1\), and has strictly positive remaining eigenvalues. Resolving the inverse by spectral projectors gives, in operator norm as \(f\to\infty\),

\[
K_f=\frac{1}{a}P+\frac1f L^++O(f^{-2}).
\]

Therefore \(K_f B=A_0+f^{-1}A_1+O(f^{-2})\) with \(A_0=\mathbf1b^T/(na)\) and \(A_1=L^+B\). The unique nonzero eigenvalue of \(A_0\) is \(\lambda_0=s/(na)>0\), with right eigenvector \(\mathbf1\) and left eigenvector \(b^T\). Finite-dimensional simple-eigenvalue analytic perturbation gives

\[
\lambda_1=\frac{b^TA_1\mathbf1}{b^T\mathbf1}=\frac{b^TL^+b}{s}.
\]

The other eigenvalues tend to zero, while the positive Perron root tends to \(\lambda_0\), so the perturbed eigenvalue is the Perron root for all large \(f\). This proves the expansion including its fixed-parameter \(O(f^{-2})\) remainder. Since \(L^+\) is positive definite on \(\mathbf1^\perp\), its energy vanishes if and only if \(b\) is constant. If \(b_i=b_*\) for all \(i\), every row of \(K_f\) sums to \(1/a\), and the exact Perron root is \(b_*/a\) at every \(f>0\).

**3. Critical-window test.** Multiply the expansion by \(h_f=(na/s)(1-\eta/f)\). Direct multiplication, with no interchange of \(f\) and \(n\) limits, yields

\[
h_f\mathcal R_f=1+\frac{Q_G-\eta}{f}+O(f^{-2}),\qquad Q_G=\frac{na\,b^TL^+b}{s^2}.
\]

For fixed unequal constants \(Q_G,\eta\) the sign is eventually the sign of \(Q_G-\eta\), proving both strict alternatives. The equality case requires the next coefficient and is deliberately excluded.

**4. Edge sensitivity.** Let \(r=b-(s/n)\mathbf1\); then \(b^TL^+b=r^TL^+r\). The mean-zero solution \(\phi=L^+r\) minimizes the electrical Dirichlet energy subject to \(L\phi=r\). Differentiating the invertible Laplacian restricted to \(\mathbf1^\perp\) when the conductance of edge \(uv\) is increased gives

\[
\frac{d}{dw_{uv}}(r^TL^+r)=-r^TL^+(e_u-e_v)(e_u-e_v)^TL^+r=-(\phi_u-\phi_v)^2.
\]

Multiplication by \(na/s^2\) proves the formula. This is a topology sensitivity of the correction, not an assertion that corridor construction universally reduces invasion for other birth matrices.

**5. Exact three-patch witness.** Put \(H_G=aI+fL_G\). Since \(H_G\) is positive definite and \(B\) positive diagonal, \(h\mathcal R_f<1\) is equivalent to positive definiteness of \(H_G-hB\), by congruence with \(I-hH_G^{-1/2}BH_G^{-1/2}\). Likewise a negative eigenvalue of \(H_G-hB\) implies \(h\mathcal R_f>1\). For the stated parameters, the successive leading principal minors on the path are exactly

\[
\left(\frac{453}{50},\frac{101953}{1250},-\frac{448897}{62500}\right),
\]

whereas on the triangle they are

\[
\left(\frac{953}{50},\frac{352453}{1250},\frac{1053103}{62500}\right).
\]

The path matrix has a negative eigenvalue (negative determinant) and the triangle matrix is positive definite (Sylvester's criterion), giving the claimed strict invasion reversal. The mean-zero Laplacian equation with \(b-(s/3)\mathbf1=(1,0,-1)^T\) has potentials \((1,0,-1)^T\) on the path and \((1/3,0,-1/3)^T\) on the triangle. Their energies are \(2\) and \(2/3\) respectively, hence \(Q_{\rm path}=1/3\), \(Q_{\rm triangle}=1/9\) at \(a=2,s=6\). All identities use exact rationals.

## Verification

The accompanying `verify.py` uses only Python's standard-library `fractions.Fraction`. It reproduces the six exact Sylvester minors and both graph energies and verifies \(1/9<1/5<1/3\). Run `python verify.py` after extracting the files. This is a finite reproducibility check: the all-graph theorem is established by the spectral perturbation and edge-energy arguments above, not by enumerating examples.

## Relationship to prior work

Bernardi et al. (2026), equations (5)–(11), derive the underlying kernel and their Theorem 1 supplies its Perron invasion criterion; both are prerequisites, not new claims here. Section II.2 explicitly mentions both source-local explorer birth and neighbor-born explorers. Nicoletti et al. (2023) establish the microscopic network explorer framework and demonstrate a different neighboring-patch-birth regime where adding connections can improve metapopulation capacity. Altenberg (2011/2012) and Chen et al. (2022) establish general dispersal-induced spectral reduction/monotonicity. The novel candidate is the **explicit graph-resistance coefficient** of this particular source-local Bernardi kernel, its **sharp critical recruitment window**, and an **exact same-rate corridor-induced change of invasion verdict**. The monotonicity of more mixing is not claimed as new; general perturbation theory and Laplacian energy calculus are standard proof tools. Existing general spectral theorems imply qualitative behavior but do not furnish these model-specific evaluated statements without additional calculations.

## Limitations

The asymptotic result holds for fixed connected graphs and fixed coefficients; constants in the error term may depend on graph size, spectral gap and local rates. The critical equality case \(\eta=Q_G\) is unresolved here. The exact counterexample changes a movement edge only, not the birth matrix; it need not hold under neighboring-patch explorer production. The theorem classifies deterministic **linear invasion near extinction**, not stochastic ultimate survival or interacting multispecies persistence. Historical priority beyond the inspected literature requires independent assessment.

## References

- Bernardi, D., Doimo, A., Nicoletti, G., Padmanabha, P., Rinaldo, A., Suweis, S., Azaele, S., and Maritan, A. *Habitat heterogeneity and dispersal network structure as drivers of metacommunity dynamics* (first public 2026-02-06), https://arxiv.org/abs/2602.06640 . Section II, Section III and Appendix A.
- Nicoletti, G., Padmanabha, P., Azaele, S., Suweis, S., Rinaldo, A., and Maritan, A. *Emergent encoding of dispersal network topologies in spatial metapopulation models*, PNAS (2023), https://doi.org/10.1073/pnas.2311548120 .
- Altenberg, L. *Resolvent Positive Linear Operators Exhibit the Reduction Phenomenon* (2011 preprint / 2012 publication), https://arxiv.org/abs/1108.4546 .
- Chen, S., Shi, J., Shuai, Z., and Wu, Y. *Two Novel Proofs of Spectral Monotonicity of Perturbed Essentially Nonnegative Matrices with Applications in Population Dynamics*, SIAM Journal on Applied Mathematics (2022), https://doi.org/10.1137/20M1345220 .
