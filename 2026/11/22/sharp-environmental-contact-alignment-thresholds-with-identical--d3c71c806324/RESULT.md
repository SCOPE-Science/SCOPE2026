# Sharp environmental-contact alignment thresholds with identical local epidemic scores

## Finding

Let \(n\ge 2\) human groups interact by homogeneous complete mixing, with one shared environmental pathogen reservoir. With common human recovery and reservoir decay normalized to one, the linearized next-generation matrix is

\[
K_\pi=\begin{pmatrix}
\frac{a}{n}{\bf1}{\bf1}^{\mathsf T}&u\\
(v_{\pi(1)},\ldots,v_{\pi(n)})&0
\end{pmatrix},
\qquad a>0,\quad u_i,v_i>0,
\]

where \(\pi\) permutes the assignments of human-to-reservoir shedding intensities \(v_i\) while the reservoir-to-human exposure intensities \(u_i\) remain attached to their groups. Put \(U=\sum_i u_i\), \(V=\sum_i v_i\), and \(Q_\pi=\sum_i u_i v_{\pi(i)}\). For every permutation, the invasion factor \(R_\pi=\rho(K_\pi)\) is the **unique** solution \(\lambda>\max\{a,\sqrt{Q_\pi}\}\) of

\[
(\lambda-a)(\lambda^2-Q_\pi)=\frac{aUV}{n}.
\tag{1}
\]

For fixed multisets of shedding and exposure intensities, \(R_\pi\) is largest when the two intensities are similarly ordered, and smallest when they are oppositely ordered. If both lists are nonconstant, these extrema differ strictly. Thus the entire finite assignment problem, for arbitrary \(n\), is solved by sorting.

When \(0<a<1\), the exact invasion test, including equality, is

\[
R_\pi\;\begin{cases}<1\\=1\\>1\end{cases}
\quad\Longleftrightarrow\quad
Q_\pi+\frac{aUV}{n(1-a)}\;\begin{cases}<1\\=1\\>1.\end{cases}
\tag{2}
\]

In particular, whether **any** reassignment can suppress invasion, and whether **every** reassignment suppresses it, follows by substituting the oppositely sorted and similarly sorted dot products into (2). The row sums of the next-generation matrix are \((a+u_1,\ldots,a+u_n,V)\) for every permutation. Consequently even the full vector of local row-sum reproduction scores and both marginal intensity lists can remain unchanged while the global invasion verdict reverses.

This reversal already occurs with two human groups, the smallest size permitting distinct assignments. Set \(n=2\), \(a=1/2\), \(u=(9/10,1/10)\), and the shedding multiset \(\{9/10,1/10\}\). Matching high to high gives an exact invasion-test value \(33/25>1\) and \(R=1.10921716\ldots>1\); matching high to low gives \(17/25<1\) and \(R=0.89851493\ldots<1\). In both cases every local score is the same: \((7/5,3/5,1)\).

## Assumptions and scope

The groups and reservoir are compartments of a deterministic linearized SIS-with-environment or SIR-with-environment model; the theorem evaluates the **next-generation spectral invasion factor**, not the eventual stochastic outbreak probability. All mixing, shedding, exposure, and decay rates are time-independent. Human recovery and environmental decay are normalized to rate one, so \(K_\pi\) is a dimensionless next-generation matrix. The within-human transmission block has equal entries \(a/n\), including self-group contacts. The reservoir has no independent self-reproduction. All \(u_i,v_i\) and \(a\) are strictly positive; assignment means permutation, not continuous reallocation of intensities.

The matched and reversed assignments attain the extrema with repeated entries allowed. If one list is constant, every assignment has the same invasion factor. For \(a\ge1\), every assignment has \(R_\pi>1\); formula (2) is claimed only for \(0<a<1\).

## Proof

**Exact eigenvalue reduction.** The matrix \(K_\pi\) is irreducible and nonnegative, with positive human-to-human entries, and hence has a positive Perron eigenvector \((z_1,\ldots,z_n,w)\), \(w>0\). Write \(S=\sum_i z_i\). The human eigenvector equations imply

\[
\lambda z_i=\frac{a}{n}S+u_iw,
\qquad (\lambda-a)S=Uw.
\]

The latter identity gives \(\lambda>a\), and hence \(S=Uw/(\lambda-a)\). The reservoir equation then yields

\[
\lambda w=\sum_i v_{\pi(i)}z_i
=\frac{aVS}{n\lambda}+\frac{Q_\pi w}{\lambda}.
\]

Substituting for \(S\) gives (1) and \(\lambda^2=Q_\pi+aUV/[n(\lambda-a)]>Q_\pi\). Conversely, for any root of (1) beyond \(\max\{a,\sqrt{Q_\pi}\}\), take \(w=1\) and \(z_i=[aU/(n(\lambda-a))+u_i]/\lambda\). These are strictly positive, satisfy the complete eigenvalue equations, and therefore the root is exactly the Perron eigenvalue. On this interval the left side of (1) is strictly increasing from zero to infinity, proving existence and uniqueness.

**Extrema and strictness.** Holding \(a,U,V,n\) fixed, implicit differentiation of (1) gives

\[
\frac{\mathrm d\lambda}{\mathrm d Q}=
\frac{\lambda-a}{\lambda^2-Q+2\lambda(\lambda-a)}>0.
\]

For \(u_i<u_j\) and \(v_k<v_\ell\), changing crossed pairs \((u_i,v_\ell),(u_j,v_k)\) to aligned pairs changes \(Q\) upward by \((u_j-u_i)(v_\ell-v_k)>0\). Repeated uncrossings prove the rearrangement extrema and strict separation when both lists are nonconstant. This also handles arbitrary ties through non-strict swaps.

**Exact invasion classification.** For \(0<a<1\), put \(C=aUV/n\). If \(Q_\pi\ge1\), the Perron root is automatically greater than one, and the right side of (2) is greater than one. If \(Q_\pi<1\), then \(1>\max\{a,\sqrt{Q_\pi}\}\); strict monotonicity of \((\lambda-a)(\lambda^2-Q_\pi)\) on the admissible root interval shows that \(R_\pi\lessgtr1\) exactly when \((1-a)(1-Q_\pi)\gtrless C\), which is (2) with the appropriate reversed order of test-function signs. Equality follows by direct substitution. Finally the human row sums are \(a+u_i\), while the reservoir row sum is \(V\), all unaffected by the permutation.

**Sharp smallest witness.** With the displayed two-group parameters, \(U=V=1\). The paired and crossed dot products are respectively \(41/50\) and \(9/50\), and the common human-mediated loop term is \(1/2\). Their total loop gains are therefore \(33/25\) and \(17/25\). Formula (2) proves the strict opposite invasion verdicts without relying on decimal approximations. With one human group there is only one assignment, so two groups are necessary and sufficient for such a permutation-driven reversal.

## Verification

The self-contained Python program `check.py` independently evaluates the Perron factor by direct positive-matrix iteration and by bisection of (1), compares all permutations of many small random assignment problems against the sorted extrema, and uses exact rational arithmetic for the two-group threshold reversal. Run from the extracted package with `python3 check.py`. It executed successfully with **5,090** supplementary checks. These finite computational tests are not used to establish the all-size statements, which follow from the proof above.

## Relationship to prior work

Caiza, Qin, and Paré (2026) introduce local basic reproduction metrics for population–infrastructure epidemics, prove row-sum bounds, and obtain a two-by-two formula under layerwise-uniform *both* intra- and inter-layer row sums. Their layerwise assumption fails here when the exposure vector \(u\) is nonconstant. Equations (1)–(2) instead give an exact all-assignment threshold for the heterogeneous single-reservoir case despite the lack of equitable layerwise coupling.

Qu and Wang (2016) study correlations of infection rates with degree on ordinary contact networks, including stochastic simulations and a wheel-network special case. Li, Wang, and Van Mieghem (2013) establish spectral threshold context for directed networks. Tuschhoff and Kennedy (2025) examine epidemiological consequences of correlated susceptibility and transmissibility in a heterogeneous stochastic SIR model. These works support the importance of correlation, but the specific fixed-local-score reservoir assignment classification and exact loop-gain reversal are not asserted in their accessible descriptions or the inspected relevant sections. A full-content comparison with the last study could not be completed, so historical priority remains subject to that limitation. The spectral and rearrangement arguments use classical mathematical tools; no novelty is claimed for those tools themselves.

## Limitations

The theorem is an exact invasion-threshold result in a deliberately constrained rank-one human mixing model. It does not establish the same sorting rule for arbitrary heterogeneous human-contact matrices, multiple independent reservoirs, nonlinear endemic equilibria, finite stochastic populations, or intervention costs. Equality in (2) is a critical spectral threshold, not a proof of endemic persistence at criticality. The novelty assessment is literature-bounded; independent scientific assessment has not occurred.

## References

1. J. I. Caiza, J. Qin, P. E. Paré, “Local Reproduction Numbers for Analysis and Optimal Mitigation of Epidemic Processes,” arXiv:2610.09066, publicly released 2026-10-06. https://arxiv.org/abs/2610.09066
2. B. Qu and H. Wang, “SIS Epidemic Spreading with Correlated Heterogeneous Infection Rates,” arXiv:1608.07327, publicly released 2016-08-25. https://arxiv.org/abs/1608.07327
3. C. Li, H. Wang, and P. Van Mieghem, “Epidemic threshold in directed networks,” arXiv:1303.0783, publicly released 2013-03-01. https://arxiv.org/abs/1303.0783
4. B. M. Tuschhoff and D. A. Kennedy, “Heterogeneity in and correlation between host transmissibility and susceptibility can greatly impact epidemic dynamics,” Journal of Theoretical Biology 611 (2025), 112186, DOI:10.1016/j.jtbi.2025.112186. https://doi.org/10.1016/j.jtbi.2025.112186
