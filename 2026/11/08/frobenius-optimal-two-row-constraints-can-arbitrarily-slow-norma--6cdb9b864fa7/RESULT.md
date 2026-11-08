# Frobenius-optimal two-row constraints can arbitrarily slow normalized-row Kaczmarz

## Finding
For the six-row unit-normalized family below, minimizing the row-interpolative-decomposition (ID) residual is incompatible with maximizing the sharp expected progress of the corresponding subspace-constrained randomized Kaczmarz method. Every Frobenius-optimal two-row choice has progress constant \(s^2\), whereas the unique progress-optimal choice has constant \(1/2\). Their ratio \(1/(2s^2)\) is unbounded. Exact stochastic trajectories with the same consistent right-hand side confirm the difference beyond comparing theoretical upper bounds.

## Assumptions and scope
Fix \(0<s<1/\sqrt2\), put \(c=\sqrt{1-s^2}\), and let \(e_1,e_2,e_3,e_4\) be the Euclidean coordinate basis. In this order, the rows of \(A\in\mathbb R^{6\times4}\) are
\[
a_1=a_2=e_2^\top,\quad a_3=a_4=e_3^\top,\quad
a_5=(ce_1+se_4)^\top,\quad a_6=(ce_1-se_4)^\top.
\]
All rows have norm one. Moreover
\[
A^\top A=\operatorname{diag}(2c^2,2,2,2s^2),
\quad\kappa_2(A)=1/s,
\]
so \(A\) has full column rank for every admissible \(s\).

For an index set \(I\subset\{1,\ldots,6\}\) of exactly two rows, define the orthogonal projector \(P_I=I_4-A_I^\dagger A_I\), the ID objective \(F(I)=\|AP_I\|_F^2\), and the sharp fixed-distribution one-step error-improvement constant
\[
\delta(I)=\frac{\lambda_{\min}^+(P_IA^\top AP_I)}{\operatorname{tr}(P_IA^\top AP_I)}.
\]
Here \(\lambda_{\min}^+\) is the smallest positive eigenvalue, acting on the range of \(P_I\), not the zero eigenvalues of the full ambient matrix. For the consistent system \(b=Ax^\star\), \(x^\star=e_2+e_4\), initialize \(x^0=A_I^\dagger b_I\). The standard singleton norm-squared projected Kaczmarz step chooses \(j\notin I\) independently with probabilities \(\|P_Ia_j\|_2^2/F(I)\) and sets
\[
x^{t+1}=x^t-\frac{a_j^\top x^t-b_j}{\|P_Ia_j\|_2^2}P_Ia_j.
\]
Projected-zero rows have probability zero. A selected row with zero *current residual* gives a null step. We separately analyze the convention in which such a row is rejected and resampled. All computations and statements concern exact arithmetic and the unrelaxed singleton method.

## Proof
**One-step progress is exactly spectral.** Let \(e=x-x^\star\in\operatorname{range}(P_I)\). Each nonzero projected-row update is an orthogonal projection, so averaging its squared-norm decrease over the fixed sampling distribution gives
\[
\mathbb E[\|e^+\|_2^2\mid e]
=\|e\|_2^2-\frac{\|AP_Ie\|_2^2}{F(I)}.
\]
Consequently the largest constant \(\delta\) valid in \(\mathbb E[\|e^+\|_2^2\mid e]\le(1-\delta)\|e\|_2^2\) for every admissible error is exactly \(\delta(I)\). The minimum positive eigenvalue is attained on the residual subspace.

**All fifteen two-row choices.** Set \(u_+=ce_1+se_4\) and \(u_-=ce_1-se_4\), so \(\langle u_+,u_-\rangle=c^2-s^2\) and \(\|u_--\langle u_+,u_-\rangle u_+\|^2=4c^2s^2\). There are four possible types of two-row selection:

- A pair \(\{e_2,e_3\}\), with either duplicate index for each: \(F=2\) and projected positive eigenvalues \(2c^2,2s^2\), hence \(\delta=s^2\).
- One of \(e_2,e_3\) with one of \(u_+,u_-\): \(F=2+4c^2s^2>2\) and projected positive eigenvalues \(2,4c^2s^2\), hence \(\delta=4c^2s^2/(2+4c^2s^2)<1/2\).
- The duplicated pair \(\{e_2,e_2\}\) or \(\{e_3,e_3\}\): rank-one constraints and \(F=4\); three-dimensional residual range entails \(\delta\le1/3\).
- The pair \(\{u_+,u_-\}\): \(F=4\); its residual range is \(\operatorname{span}\{e_2,e_3\}\), with both eigenvalues exactly \(2\), hence \(\delta=1/2\).

Every rank-two constraint leaves a two-dimensional residual range; for two positive eigenvalues, their minimum divided by their sum is at most \(1/2\). The classification shows that only \(I_\star=\{5,6\}\) attains equality. The four and only four ID minimizers have one index from \(\{1,2\}\) and one from \(\{3,4\}\). This proves both optimality assertions and the ratio
\[
\frac{\delta(I_\star)}{\delta(I_{\rm ID})}
=\frac{1}{2s^2}=\frac{\kappa_2(A)^2}{2}.
\]

**Actual independent-sampling dynamics.** For any ID-minimizer, the constrained initialization is \(x^0=e_2\); its error has norm one and is in direction \(-e_4\). Both remaining active projected rows are \(u_+,u_-\), chosen independently with probability \(1/2\). The first projection leaves squared error \(c^2\). After it, if the next row is the same, the error is unchanged; if it is the other, squared norm is multiplied by \((c^2-s^2)^2\). The signs of successive independently sampled rows match or differ with equal probability, so for every integer \(t\ge1\),
\[
\mathbb E\|x^t-x^\star\|_2^2
=c^2\left(\frac{1+(c^2-s^2)^2}{2}\right)^{t-1}
=c^2(1-2c^2s^2)^{t-1}.
\]
For \(I_\star=\{5,6\}\), the initialization is \(x^0=e_4\), with initial error \(-e_2\). The four projected candidate rows consist of two copies of \(e_2\) and two of \(e_3\). Each iteration has probability \(1/2\) of clearing the remaining error entirely, hence the exact law \(\mathbb E\|x^t-x^\star\|_2^2=2^{-t}\) for all integers \(t\ge0\).

**Rejecting zero-residual draws.** If the algorithm resamples whenever a selected row has zero current residual, the first ID-minimizer step is unchanged. Subsequently, only the opposite \(u\)-row has nonzero residual; alternating these two projections gives squared error \(c^2(c^2-s^2)^{2(t-1)}\) for \(t\ge1\). For \(I_\star\), only the \(e_2\)-rows have nonzero initial residual, so the error is zero after the first accepted update. At iteration zero both initial errors have squared norm one. This distinction ensures that resampling and nonresampling conventions are not conflated.

## Verification
The accompanying `verify_unitrows.py` uses exact rational arithmetic via SymPy. Four rational parameter pairs are checked. For each pair it reconstructs the complete matrix and enumerates all fifteen two-row choices, including rank-deficient constrained pairs, and checks the optimality, projected spectra, Frobenius scores and condition-number identity. It also reconstructs the second-moment recurrence for independent sampling and branches the exact reject-zero sampling process; it tests six consecutive iteration indices for both selected constraint types. The run reports: `PASS: exact spectra, all 60 constrained pairs, and 96 exact moment identities`. These finite checks support the algebra but do not establish the entire open parameter interval; the preceding symbolic argument does.

Run with `python -m pip install -r requirements.txt` followed by `python verify_unitrows.py` using Python 3.

## Relationship to prior work
Sun–Qi–Han–Xie, arXiv:2605.29304v1 (2026), Remark 3.1 and Remark 3.3, state the projected norm-squared sampling rule and its scaled-condition convergence factor. Their Section 3.2 proposes the Frobenius residual / row-ID objective as a practical surrogate for minimizing that condition factor. The example above compares the *globally optimal* solution to their surrogate against the *globally optimal* sharp one-step rate, so it does not depend on any particular heuristic implementation. The work of Lok–Rebrova establishes the subspace-constrained randomized Kaczmarz framework and related convergence estimates. Cortinovis–Kressner investigate Frobenius-optimality and approximation guarantees for adaptive column subset selection, which do not itself optimize the projected Kaczmarz contraction. The exact unit-row reversal, exhaustive two-row classification and trajectory formulas are the present result; basic Kaczmarz theory and row-ID objective are prior work.

## Limitations
Only one explicit normalized six-row, four-column family and two constrained rows are classified. The exact expectations assume consistent data, a particular common right-hand side, and either precisely stated row-sampling convention. The ratio compares sharp one-step worst-case contraction constants, not total wall-clock time or the performance of every acceleration, QR pivot heuristic, or randomized sketch. Condition number becomes unbounded as \(s\downarrow0\), although each fixed \(s>0\) retains full rank. No claim of historical priority beyond the checked literature is certified; broader older row-selection inequalities might imply portions of the comparison.

## References
1. Y. Sun, H.-D. Qi, D. Han and J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1 (first public 28 May 2026), https://arxiv.org/html/2605.29304 .
2. L. Lok and E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889, https://arxiv.org/abs/2309.04889 .
3. L. Lok and E. Rebrova, *Subspace-Constrained Randomized Coordinate Descent for Linear Systems with Good Low-Rank Matrix Approximations*, arXiv:2506.09394, https://arxiv.org/abs/2506.09394 .
4. A. Cortinovis and D. Kressner, *Adaptive Randomized Pivoting for Column Subset Selection, DEIM, and Low-Rank Approximation*, arXiv:2412.13992, https://arxiv.org/abs/2412.13992 .
