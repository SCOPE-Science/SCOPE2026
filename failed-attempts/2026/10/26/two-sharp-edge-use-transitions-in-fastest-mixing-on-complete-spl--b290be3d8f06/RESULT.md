# Two sharp edge-use transitions in fastest mixing on complete split graphs

## Finding
Let \(G_{r,m}=K_r\vee\overline{K}_m\), where \(r,m\) are integers at least two: there are \(r\) mutually adjacent core vertices and \(m\) mutually nonadjacent peripheral vertices, and every core vertex is adjacent to every peripheral vertex. Among all symmetric, entrywise nonnegative, row-stochastic matrices \(P\) whose off-diagonal support is contained in this graph, the optimal second-largest eigenvalue modulus is
\[
\mu^*(G_{r,m})=\begin{cases}
\dfrac{m}{m+2r},&2\le m\le 2r,\\[3pt]
1-\dfrac r m,&m\ge 2r.
\end{cases}
\]
Both formulas agree at \(m=2r\). Every automorphism-invariant optimizer assigns a single probability \(a\) to each core-to-peripheral edge and a single probability \(b\) to each core-to-core edge. These **are all** the invariant optimizers:
\[
\begin{aligned}
2\le m\le2r:\quad&a=\frac{2}{m+2r},\\
&\frac{2\max\{r-m,0\}}{r(m+2r)}\le b\le
\frac{2r-m}{(r-1)(m+2r)};\\[3pt]
m\ge2r:\quad&a=\frac1m,\qquad b=0.
\end{aligned}
\]
At the common boundary the descriptions coincide. This yields **sharp structural necessities even without imposing symmetry on \(P\)**. If \(2\le m<r\), every optimal matrix uses at least one positive-weight core-to-core edge. If \(r\le m<2r\), both an optimizer with no core-to-core transitions and one with positive core-to-core transitions exist. If \(m\ge2r\), every optimal matrix has zero transition probability on every core-to-core edge. Neither uniqueness of an unrestricted optimizer nor a classification of all unrestricted optimizers is asserted.

## Assumptions and scope
A symmetric stochastic \((r+m)\)-by-\((r+m)\) matrix has nonnegative entries, satisfies \(P\mathbf1=\mathbf1\), and satisfies \(P=P^\mathsf T\). Its diagonal entries (holding probabilities) are unrestricted except for nonnegativity. Off-diagonal entries must vanish at nonedges, but edge probabilities are permitted to vanish. The uniform distribution is stationary. The objective is
\[
\mu(P)=\max_{2\le j\le r+m}|\lambda_j(P)|
=\left\|P-\frac{\mathbf1\mathbf1^\mathsf T}{r+m}\right\|_2,
\]
where the eigenvalues are real and ordered with one copy of the trivial eigenvalue \(1\) removed. All statements quantify over every integer \(r,m\ge2\). They concern the two-sided asymptotic spectral measure, not total-variation mixing time, arbitrary prescribed stationary measures, or nonsymmetric chains.

## Proof
**1. Reduction without losing global optimality.** The permutation groups on the two vertex classes act by graph automorphisms. The convex function \(P\mapsto\|P-\mathbf1\mathbf1^\mathsf T/(r+m)\|_2\) is unchanged by conjugating \(P\) by these permutations. Averaging any feasible \(P\) over \(S_r\times S_m\) produces a feasible invariant matrix with no larger objective. Thus a global optimum can be found with probabilities \(a\) and \(b\) as in the finding. Its holding probabilities are \(1-ma-(r-1)b\) at a core vertex and \(1-ra\) at a peripheral vertex. Feasibility is precisely
\[
a,b\ge0,\qquad ma+(r-1)b\le1,\qquad ra\le1.
\]

**2. Entire invariant spectrum.** Decompose \(\mathbb R^{r+m}\) orthogonally into the constant line, the peripheral sum-zero subspace, the core sum-zero subspace and the nonconstant two-class-constant line. Applying the transition matrix to each subspace gives eigenvalues, with respective multiplicities,
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1&1\\
1-ra&m-1\\
1-ma-rb&r-1\\
1-(m+r)a&1.
\end{array}
\]
Both nonconstant sum-zero subspaces are nonempty because \(r,m\ge2\). Hence the objective is exactly the maximum of the absolute values of the last three expressions.

**3. Sharp lower bound.** In particular every invariant feasible matrix satisfies
\[
\mu(P)\ge f(a):=\max\{|1-ra|,\;|1-(m+r)a|\},\qquad
0\le a\le\min\left\{\frac1r,\frac1m\right\}.
\]
The unconstrained minimum of \(f\) occurs uniquely when its two relevant signed eigenvalues balance, at \(a_0=2/(m+2r)\), with value \(m/(m+2r)\). On the feasible interval, \(1-ra\ge0\); to the left of \(a_0\), this term decreases strictly with \(a\) and dominates the decreasing objective. Since \(a_0\le1/r\) always and \(a_0\le1/m\) exactly when \(m\le2r\), the unique constrained minimizer is
\[
 a^*=\min\left\{\frac2{m+2r},\frac1m\right\},
\]
and its sharp lower-bound value is \(m/(m+2r)\) when \(m\le2r\) and \(1-r/m\) otherwise. The second formula uses \(m\ge2r\) to bound \(|1-(m+r)/m|=r/m\) by \(1-r/m\).

**4. Attainment and the complete invariant optimal set.** For \(m\le2r\) substitute \(a=a_0\). The remaining spectral requirement \(|1-ma-rb|\le m/(m+2r)\), together with \(0\le b\le(1-ma)/(r-1)\), is exactly
\[
\max\left\{0,\frac{2(r-m)}{r(m+2r)}\right\}
\le b\le
\min\left\{\frac{2}{m+2r},\frac{2r-m}{(r-1)(m+2r)}\right\}.
\]
Because \(m\ge2\), the second term inside the minimum never exceeds the first. The interval is nonempty. For \(m<r\), its upper end minus its positive lower end is exactly \(\frac{m(r-2)+2r}{r(r-1)(m+2r)}>0\); for \(m\ge r\), its lower end is zero and its upper end is nonnegative. Its upper endpoint makes the core holding probability exactly zero. Every value in the interval is feasible and attains the lower bound. Conversely, the strict uniqueness of the lower-bound minimizing \(a\), followed by the same inequalities, forces this interval for any invariant optimizer. For \(m>2r\), the minimizing \(a=1/m\) saturates the core row; feasibility forces \(b=0\), and the third eigenvalue is zero. The boundary \(m=2r\) also forces \(b=0\). This completes the exact global optimum and invariant-optimizer classification.

**5. Edge-use statements for unrestricted optimizers.** Given any unrestricted optimal matrix, its average over all core and peripheral permutations is an invariant optimizer. The averaged core-edge probability is the arithmetic mean of the nonnegative original core-edge probabilities. When \(m<r\), every invariant optimizer has strictly positive \(b\), so every unrestricted optimizer must use some core-to-core edge. When \(m\ge2r\), the averaged \(b\) is zero, hence nonnegativity forces **every** individual core-to-core entry to be zero. In the intermediate range \(r\le m<2r\), both \(b=0\) and \(b>0\) belong to the explicit optimal interval, proving both possibilities. No unproved uniqueness inference is made.

## Verification
The standalone program `verify.py` requires the versions of NumPy and SciPy given in `requirements.txt`. From its own directory, run `python verify.py`. It uses exact rational arithmetic to check admissibility, spectral endpoint identities and all three interval types on \(561\) parameter pairs, including three eligible values of \(b\) each. It additionally compares \(77\) explicitly constructed dense symmetric matrices against the full analytic eigenspectrum, solves \(209\) independent invariant linear programs, and evaluates \(420\) randomly perturbed feasible non-invariant matrices. The captured output is in `verification_output.txt`. These are finite consistency checks. The infinite-family theorem is established by the preceding algebraic argument, not by any extrapolation from those checks.

## Relationship to prior work
Boyd, Diaconis, Parrilo and Xiao (2007 preprint; 2009 journal article) prove convex symmetry reduction and derive a general eigenvalue-block description for complete multipartite graphs. Their Section 5.4.2 supplies an explicit optimal formula for **complete bipartite** graphs, not the present general solution for split graphs with core-clique edges. The subregime \(m\ge r\) has an optimal transition matrix with \(b=0\); its optimal value coincides with their complete-bipartite result and is **not separately claimed as new**. What their stated bipartite formula does not cover is the regime \(m<r\), where positive core-to-core transitions are compulsory, together with the complete interval of invariant optimizers and the two sharp structural edge-use transitions.

For comparison, let \(\mu^*_{\mathrm{bip}}\) denote the optimal SLEM after deleting every core-to-core edge, leaving \(K_{r,m}\). In the previously solved complete-bipartite problem, when \(r>m\) the value is
\[
\mu^*_{\mathrm{bip}}=
\max\left\{1-\frac mr,\;\frac r{r+2m}\right\}
>\frac m{m+2r}=\mu^*(G_{r,m}).
\]
In particular, with fixed \(m\ge2\) and \(r\to\infty\), the optimal bipartite SLEM tends to \(1\), while the complete split graph's optimal SLEM tends to \(0\). This is a substantive network-design difference, not a mere reparametrization of the bipartite result.

The later friendship-graph work of Jafarizadeh concerns triangles sharing a single vertex and partially fixed reversible transition weights. Such windmills are not these complete split graphs with a core clique and a peripheral independent class. General geometric mixing estimates for arbitrary graphs address bounds, not this exact two-sided optimizer classification. The closest literature is therefore methodologically relevant, with specialized prior coverage remaining a legitimate originality risk.

## Limitations
The assertion of originality is based on identified accessible literature and mathematical-record searches; it is not a uniqueness-of-literature certificate. The model assumes a symmetric transition matrix, a uniform stationary distribution and permitted zero edge probabilities. The complete set of non-invariant optimal matrices is not classified. The result does not identify exact total-variation mixing times or address arbitrary weighted/noncomplete cross graphs. Numerical checks cover only displayed finite ranges. Independent mathematical validation has not been performed.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, initially posted 2007-09-06; SIAM Journal on Optimization 20 (2009), 792–819, especially Section 5.4.2. https://arxiv.org/abs/0709.0955 ; full text https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf
2. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://web.stanford.edu/~boyd/papers/fmmc.html
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain on Friendship Graph: Trade-Off between Transition Probabilities among Friends and Convergence Rate*, arXiv:2501.02117v1 (2025). https://arxiv.org/abs/2501.02117
4. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, Probability Theory and Related Fields 188 (2024), 1017–1062. https://doi.org/10.1007/s00440-023-01257-x
