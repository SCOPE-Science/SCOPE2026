# A sharp terminal-fecundity sensitivity staircase in plus-class population matrices

## Finding
Let a population have \(n\geq3\) age/stage classes with strictly positive survival to the next class, terminal-class retention, and offspring entering class one. In every growing, irreducible Leslie-plus projection matrix specified below, the absolute sensitivities \(G_j=\partial\lambda/\partial f_j\) of the Perron growth factor to fertility are strictly decreasing through classes \(1,\ldots,n-1\). The terminal sensitivity can occupy **any** rank, and its precise rank is given by the following identity for each \(1\leq j<n\):
\[
\frac{G_n}{G_j}=\frac{\prod_{i=j}^{n-1}s_i}{\lambda^{n-j-1}(\lambda-t)}.
\]
In particular, the terminal class has the strictly largest sensitivity precisely when
\[
\lambda^{n-2}(\lambda-t)<\prod_{i=1}^{n-1}s_i.
\]
For the natural one-parameter family with only terminal-class fertility \(F=f_n>0\), growth \(\lambda>1\) yields a **complete and sharp sensitivity-rank staircase**. Put \(P_j=\prod_{i=j}^{n-1}s_i\). Exactly those classes \(j<n\) satisfying \(P_j>1-t\) have one positive-growth crossing with the terminal class. For each such class there is one and only one \(\lambda_j>1\) satisfying
\[
\lambda_j^{n-j-1}(\lambda_j-t)=P_j,
\]
and the unique fertility crossing is
\[
F_j=\frac{\lambda_j^{n-1}(\lambda_j-t)}{P_1}.
\]
The thresholds are strictly ordered by increasing \(j\). As \(F\) increases, the terminal class falls below the eligible classes one at a time in increasing age order, with no other reversals. All \(n\) strict sensitivity ranks occur within the growing regime if and only if
\[
P_1>1-t.
\]
This is a criterion about **absolute fertility sensitivities**; it is not an elasticity ranking or a comparison of feasible composite life-history interventions.

## Assumptions and scope
For an integer \(n\geq3\), define the nonnegative matrix
\[
A=\begin{pmatrix}
f_1&f_2&\cdots&f_n\\
s_1&0&\cdots&0\\
0&s_2&\ddots&0\\
\vdots&\ddots&\ddots&\vdots\\
0&\cdots&s_{n-1}&t
\end{pmatrix}.
\]
Only the first row, first subdiagonal, and bottom-right entry can be nonzero. Assume \(0<s_i\leq1\) for \(1\leq i<n\), \(0\leq t<1\), and \(f_i\geq0\), with \(f_n>0\) so that \(A\) is irreducible. Its positive Perron eigenvalue \(\lambda\) is simple. The growth regime is \(\lambda>1\). Perturbing each first-row entry individually defines \(G_j=\partial\lambda/\partial f_j\), including the analytic one-sided extension at a zero fertility. Terminal retention \(t\) is a within-class survival probability, distinct from terminal fecundity \(F\). For the staircase clause, set \(f_1=\cdots=f_{n-1}=0\) and vary \(F=f_n\) while retaining all survival parameters fixed. This special family is irreducible for every \(F>0\); periodicity if \(t=0\) does not destroy simplicity of its positive Perron eigenvalue.

## Proof
Let \(w>0\) and \(v>0\) be right and left Perron eigenvectors, so \(Aw=\lambda w\) and \(v^T A=\lambda v^T\). Simplicity gives the standard first-order eigenvalue perturbation identity
\[
G_j=\frac{v_1w_j}{v^T w}.
\]
Thus the sensitivity ranks are **exactly** the ranks of right-eigenvector coordinates. Reading rows \(2,\ldots,n\) of \(Aw=\lambda w\) gives
\[
\frac{w_{j+1}}{w_j}=\frac{s_j}{\lambda}\quad(1\leq j\leq n-2),
\qquad\frac{w_n}{w_{n-1}}=\frac{s_{n-1}}{\lambda-t}.
\]
Since \(\lambda>1\geq s_j\), the first \(n-1\) sensitivity values strictly decrease. Multiplying the recurrence proves the displayed ratio formula for \(G_n/G_j\), including its equality cases and all rank comparisons. In particular, \(G_n>G_1\) is precisely the stated product inequality; if it holds, \(G_n\) is uniquely largest, and if not, \(G_1\) is largest (tied with \(G_n\) at equality).

Now suppose only \(F=f_n\) is nonzero. The top eigenvector equation \(\lambda w_1=F w_n\) and the recurrence above yield the exact, strictly increasing growth–fertility relation
\[
F=H(\lambda):=\frac{\lambda^{n-1}(\lambda-t)}{P_1},\quad\lambda>t,
\]
with growth precisely for \(F>F_0=(1-t)/P_1\). For each \(j<n\), let \(h_j(z)=z^{n-j-1}(z-t)\). On \(z\geq1\), \(h_j\) is continuous, strictly increasing from \(1-t\) to infinity. Therefore an equality \(G_n=G_j\) in the strictly growing regime exists exactly when \(P_j>1-t\), and then occurs uniquely at \(\lambda_j>1\). Its corresponding \(F_j=H(\lambda_j)\) is unique because \(H\) is strictly increasing; for \(F<F_j\) with \(F>F_0\), \(G_n>G_j\), and for \(F>F_j\), \(G_n<G_j\).

The set of eligible \(j\) is a terminal interval of indices because \(P_{j+1}=P_j/s_j\geq P_j\). If \(j\) and \(j+1\) are eligible, at \(\lambda_j\) one has \(G_n=G_j>G_{j+1}\), since \(G_{j+1}/G_j=s_j/\lambda_j<1\). As the ratio \(G_n/G_{j+1}\) decreases strictly with \(\lambda\), its crossing must occur at the strictly larger value \(\lambda_{j+1}\). Therefore the thresholds and fertility crossings are strictly ordered, and the staircase is exhaustive. All \(n-1\) crossings are above replacement exactly when the smallest product \(P_1\) exceeds \(1-t\). If \(P_1\leq1-t\), the terminal class cannot be the most sensitive at any \(\lambda>1\), showing the necessity. This proves every assertion.

To demonstrate feasibility without relying on field calibration, take \(n=4\), \(s_1=s_2=s_3=0.9\), \(t=0.95\), and only \(F=f_4>0\). The three distinct critical Perron growth factors are \(1.35\), \(1.492656621852381\ldots\), and \(1.85\), corresponding to crossing terminal fertility values \(1.35\), \(2.4755819897330675\ldots\), and \(7.816820987654322\ldots\). Thus all four strict ranks occur as fertility is raised through the increasing-population regime.

## Verification
The accompanying standard-library-only `check.py` independently solves the scalar characteristic equation by bisection for random matrices, compares central finite-difference eigenvalue sensitivities with ratios of Perron-vector coordinates, and checks the exact terminal-rank frontiers and the four-class example. Invocation: `python3 check.py`. The replayed checker reported 10,685 numerical assertions passed. These numerical experiments **supplement**, but do not replace, the algebraic proof. All computations are deterministic with a fixed pseudorandom seed, and no external packages or data are needed.

## Relationship to prior work
Carslake, Townley and Hodgson (2009), Table 2, reported as empirical rule S2 the nonincreasing first-to-penultimate fertility sensitivity for growing Leslie-plus models. The present proof establishes strictness under positive progression, and gives explicit and exhaustive terminal-rank thresholds and a fertility-driven staircase not stated in that empirical rule. Demetrius's classic Leslie-matrix recruitment-sensitivity ranking and standard Perron perturbation identities form background; they do not themselves state this terminal-retention phase diagram. Giaimo and Traulsen (2021) prove structural **elasticity** inequalities and a stronger elasticity-flow balance, including earlier conjectures from Carslake et al.; those are not equivalent to an **absolute fertility-sensitivity** rank staircase. Giaimo and Traulsen (2022) give broader age-specific sensitivities for **stage-classified** populations; the stage-with-age and additive-entry perturbations differ from this exact finite-class threshold statement. The result is consequently a narrow explicit structural specialization of established matrix-population methods, not an assertion that all such sensitivity methods are new.

## Limitations
This is an exact theorem about a finite nonnegative linear projection matrix, not an empirical ranking of conservation actions. A unit absolute increase in a fertility entry may be biologically more or less costly than increases in other entries, and an elasticity ranking can disagree. The one-parameter staircase assumes fertility occurs only in the terminal class, though the static ranking identity allows arbitrary nonnegative fecundities. It says nothing about stochastic environmental variation, transient growth, density dependence, uncertain observation, or age-specific demographic heterogeneity. The exact threshold may be derivable from standard eigenvector formulas in uninspected older treatments; the historical novelty assessment is therefore provisional. No independent scientific audit has been conducted.

## References
1. Carslake, D., Townley, S., and Hodgson, D. J. (2009). *Patterns and rules for sensitivity and elasticity in population projection matrices*. *Ecology* 90, 3258–3267. DOI: 10.1890/08-1188.1. Lawful manuscript: https://wrap.warwick.ac.uk/id/eprint/3104/1/WRAP_Carslake_300410-carslake_et_al_2009_post-print.pdf
2. Giaimo, S. and Traulsen, A. (2021). *Applying symmetries of elasticities in matrix population models*. *Theoretical Ecology* 14, 359–366. DOI: 10.1007/s12080-021-00513-x. https://link.springer.com/article/10.1007/s12080-021-00513-x
3. Giaimo, S. and Traulsen, A. (2022). *Age-specific sensitivity analysis of stable, stochastic and transient growth for stage-classified populations*. *Ecology and Evolution* 12, e9561. DOI: 10.1002/ece3.9561. https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.9561
4. Kirkland, S. J. and Neumann, M. (1994). *Convexity and concavity of the Perron root and vector of Leslie matrices with applications to a population model*. *SIAM Journal on Matrix Analysis and Applications*. DOI: 10.1137/S0895479893249228.
