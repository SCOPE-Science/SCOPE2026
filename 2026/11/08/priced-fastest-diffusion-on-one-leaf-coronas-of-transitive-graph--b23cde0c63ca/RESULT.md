# Priced fastest diffusion on one-leaf coronas of transitive graphs: a sharp allocation law and sunlet rigidity

## Finding

Let \(H\) be a connected simple graph on \(n\geq3\) vertices and \(e\) edges, whose automorphism group is transitive on both vertices and edges. Write \(\mu=\lambda_2(L_H)>0\), where \(L_H\) is the unweighted combinatorial Laplacian. Attach one new degree-one vertex to each vertex of \(H\), obtaining \(G=H\circ K_1\). Assign independent nonnegative conductances to every edge of \(G\). Core edges cost one unit per unit conductance and pendant edges cost \(c>0\). Under the budget constraint \(\sum_{E(H)}w_e+c\sum_{i=1}^n y_i\leq B\), with \(B>0\), the exact maximum algebraic connectivity is

\[
 \boxed{\Lambda(H,c,B)=\frac{B}{2e/\mu+nc+2\sqrt{enc/\mu}}.}
\]

Put \(\alpha=e/\mu\), \(\beta=nc\), and \(z=\Lambda(H,c,B)\). An optimal allocation gives every core edge the conductance
\[
 \boxed{w_*=\frac{z}{\mu}\left(2+\sqrt{\frac{\beta}{\alpha}}\right)}
\]
and every pendant edge the conductance
\[
 \boxed{y_*=z\left(1+\sqrt{\frac{\alpha}{\beta}}\right).}
\]
Both are strictly positive; this is the unique allocation invariant under all automorphisms of \(H\). Uniqueness among arbitrary individual-edge allocations is not asserted for a general transitive core.

For the sunlet \(S_m=C_m\circ K_1\), \(m\geq3\), the preceding optimal allocation is **unique even without any symmetry restriction**. With \(\ell_m=4\sin^2(\pi/m)\), the optimal leaf-to-cycle conductance ratio and fraction of total budget invested in leaves are exactly
\[
 \frac{y_*}{w_*}=\sqrt{\frac{\ell_m}{c}}\frac{1+\sqrt{c\ell_m}}{2+\sqrt{c\ell_m}},\qquad
 \frac{mc y_*}{B}=\frac{\sqrt{c\ell_m}(1+\sqrt{c\ell_m})}{2+2\sqrt{c\ell_m}+c\ell_m}.
\]
At fixed \(c,B>0\), as \(m\to\infty\),
\[
 \frac{y_*}{w_*}\sim\frac{\pi}{m\sqrt c},\qquad
 \frac{mc y_*}{B}\sim\frac{\pi\sqrt c}{m},\qquad
 \Lambda(C_m,c,B)\sim\frac{2\pi^2 B}{m^3}.
\]
Thus all pendant links remain necessary at every finite size, although their collectively optimal budget fraction vanishes at a precisely determined inverse-linear rate.

## Assumptions and scope

Graphs are finite, simple, connected and undirected. The Laplacian is the unnormalized weighted combinatorial Laplacian: \(L_{ii}=\sum_{j\sim i}w_{ij}\) and \(L_{ij}=-w_{ij}\) for adjacent distinct vertices. Algebraic connectivity means its second-smallest eigenvalue. Edge weights are independent variables allowed to be zero, and all costs and budgets in the statement are strictly positive. A graph is vertex-and-edge transitive if its automorphism group acts transitively on each of its vertex and edge sets; the condition does not mean the enlarged corona is vertex-transitive. The result is for the continuous-time heat equation \(u'(t)=-Lu(t)\), not the second-largest eigenvalue modulus of a discrete-time stochastic transition matrix. Holding probabilities and discrete-time row constraints are not part of the optimization.

## Proof

**1. Unrestricted global reduction by symmetry.** For any weighted Laplacian \(L\) with \(L\mathbf1=0\), \(\lambda_2(L)=\min_{v\perp\mathbf1,\|v\|=1}v^TLv\), the minimum of linear functions of the edge conductances; hence \(\lambda_2\) is concave in those conductances. Average any feasible edge assignment over the automorphism group of \(H\), acting simultaneously on its associated pendant vertices. This averaging preserves the budget and cannot decrease \(\lambda_2\). Transitivity makes all core edges equal to some \(w\geq0\) and all pendant edges equal to some \(y\geq0\). It follows that the optimum over *all independent edge weights* equals that of this two-parameter family. Since positive connectivity is attainable, every optimizer uses the full budget, and the symmetric optimum has \(w,y>0\).

**2. The exact two-parameter spectral gap.** In the ordering with all core vertices followed by all pendants, the uniform-weight corona Laplacian is
\[
 L=\begin{pmatrix}wL_H+yI&-yI\\-yI&yI\end{pmatrix}.
\]
For every eigenvalue \(\nu\) of \(L_H\), the corresponding invariant two-plane carries the matrix \(\bigl(\begin{smallmatrix}w\nu+y&-y\\-y&y\end{smallmatrix}\bigr)\). Its two eigenvalues are
\[
 \rho_\pm(\nu)=\frac{w\nu+2y\pm\sqrt{w^2\nu^2+4y^2}}{2}.
\]
When \(\nu=0\), they are \(0,2y\). The lower branch \(\rho_-(\nu)\) is strictly increasing for \(\nu>0\), lies strictly between \(0\) and \(y\), and is always below the upper branch and \(2y\). Consequently \(\lambda_2(L)=\rho_-(\mu)\) for all \(w,y>0\).

**3. Scalar cost minimization.** Fix a prospective gap \(z>0\). The condition \(\rho_-(\mu)\geq z\) is equivalent to positive semidefiniteness of the \(2\times2\) block in step 2 after subtracting \(zI\). Set \(t=y-z>0\). The determinant condition becomes
\[
 \mu w\,t\geq z(z+2t),\qquad\text{so}\qquad
 w\geq \frac{2z+z^2/t}{\mu}.
\]
The budget therefore obeys
\[
 B\geq ew+ncy\geq z(2\alpha+\beta)+\frac{\alpha z^2}{t}+\beta t
 \geq z\left(2\alpha+\beta+2\sqrt{\alpha\beta}\right).
\]
The last inequality is sharp arithmetic-geometric mean, with equality at the **unique** \(t=z\sqrt{\alpha/\beta}\), and equality in the determinant condition fixes \(w\). Solving for \(z\) gives the claimed optimum and two conductances. The strict equality conditions also prove uniqueness in the invariant two-parameter class.

**4. Rigidity of every sunlet optimizer.** Specialize to \(H=C_m\), and write \(\theta=2\pi/m\), \(\ell_m=2-2\cos\theta\). The uniform optimum has a real two-dimensional eigenspace \(F\) for its gap \(z\), spanned by vectors with core coordinates \(A\cos(j\theta)\) or \(A\sin(j\theta)\) and pendant coordinates \(D\cos(j\theta)\) or \(D\sin(j\theta)\), respectively. Here \(A\ne0\) and \(D/A=y_*/(y_*-z)>1\).

Let \(L'\) be *any* globally optimal weighted sunlet Laplacian, and let \(P=I-\mathbf1\mathbf1^T/(2m)\). Since \(\lambda_2(L')=z\), the matrix \(L'-zP\) is positive semidefinite. Averaging it over the cyclic rotations gives \(L_*-zP\), where \(L_*\) is the unique rotation-invariant optimum from step 3. The latter annihilates \(F\). A sum of positive-semidefinite matrices can vanish quadratically on \(F\) only if each summand annihilates \(F\); in particular \((L'-zP)F=0\). Thus *both* sine and cosine vectors above are eigenvectors of \(L'\) with eigenvalue \(z\).

At the pendant attached to position \(j\), the eigenvalue equations give \(y_j(D-A)f_j=zDf_j\) for each of the two trigonometric modes. Since \(\sin(j\theta)\) and \(\cos(j\theta)\) never vanish simultaneously, \(y_j=zD/(D-A)=y_*\) for every \(j\). The core equations then show that the weighted cycle Laplacian with edge conductances \(w_j\) has both first sine and first cosine modes as eigenvectors with eigenvalue \(w_*\ell_m\). Combining the two real modes gives the complex mode \(f_j=e^{ij\theta}\), so for every \(j\),
\[
 w_j(1-e^{i\theta})+w_{j-1}(1-e^{-i\theta})=w_*\ell_m.
\]
Taking imaginary parts yields \(\sin\theta(w_{j-1}-w_j)=0\). As \(m\geq3\), \(\sin\theta\ne0\); all \(w_j\) coincide. The real part then forces \(w_j=w_*\). This proves global uniqueness, including at small sizes and without assuming symmetrical competitors.

**5. Sunlet asymptotics.** Since \(\ell_m=4\sin^2(\pi/m)=4\pi^2/m^2+O(m^{-4})\), substitute \(e=n=m\), \(\mu=\ell_m\) into the formulas from step 3. Elementary expansions yield the exact ratios and the three stated limits. No limiting interchange with optimization is needed, because optimization is solved exactly before taking the limit.

## Verification

Run `python verify.py` with Python 3, NumPy and SymPy installed. The verifier reconstructs Laplacian matrices on cycles, complete graphs and balanced complete bipartite cores, checks exact budgets and proposed gaps, compares randomized unrestricted feasible edge-weight assignments, and conducts exact rational / symbolic PSD checks for selected cycles. Its output on the supplied program was `VERIFY_OK 1263`. These finite tests are independent checks of the expressions and boundary normalizations, not substitutes for the universal spectral and rigidity proofs above.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006, sections 1 and 5) formulate continuous-time fastest mixing with general positive edge prices and establish convex/spectral methods, including the ordinary cycle; their inspected examples do not solve the one-private-leaf corona's priced optimization. Barik, Pati and Sarma (2007, theorem 3.2 and corollary 3.5) establish Laplacian eigenvalue transfer for unweighted corona graphs, not independently optimized conductances under a budget. Boyd, Diaconis, Parrilo and Xiao (2007) treat a distinct, discrete-time symmetric stochastic-chain objective and automorphism reductions. The present theorem combines spectral transfer with exact priced optimization and, for cycles, an unrestricted optimizer-rigidity argument. Previously established discrete-time sunlet results concern second-largest eigenvalue **modulus**, subject to row-stochastic/holding constraints; they do not give the continuous-time formula or its unrestricted edge-weight uniqueness.

## Limitations

For general vertex-and-edge-transitive cores the theorem guarantees an optimal invariant allocation and uniqueness among invariant allocations; it does not classify noninvariant optima. Global uniqueness is proved here only for cycle cores. The graph is a one-leaf-per-core corona; multiple private leaves, asymmetric pendant prices, other objectives, and arbitrary nontransitive base graphs are outside scope. The novelty comparison is limited to located and inspected literature; equivalent unindexed or inaccessible results cannot be excluded. No independent mathematical validation is claimed.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48(4) (2006), 681–699; published electronically 2006-11-02; DOI: 10.1137/S0036144504443821. https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf
2. S. Barik, S. Pati and B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM Journal on Discrete Mathematics 21(1) (2007), 47–56; published electronically 2007-01-12; DOI: 10.1137/050624029. https://doi.org/10.1137/050624029
3. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first submission 2007-09-06). https://arxiv.org/abs/0709.0955
