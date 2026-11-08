# Compact-word spectral duality for row and column tuple radii

## Finding

Let \(H\) be a complex Hilbert space, \(d\ge 2\), and \(T=(T_1,\ldots,T_d)\) a bounded operator tuple on \(H\). Define two completely positive maps on \(\mathcal B(H)\):
\[
\Phi_T(X)=\sum_{j=1}^d T_jXT_j^*,\qquad
\Psi_T(X)=\sum_{j=1}^d T_j^*XT_j.
\]
If all \(T_j\) are compact, then these maps are compact as operators on the Banach space \(\mathcal B(H)\), and their nonzero spectra are complex conjugates with **matching algebraic multiplicities**:
\[
\sigma(\Psi_T)\setminus\{0\}
=\overline{\sigma(\Phi_T)\setminus\{0\}}.
\]
Consequently their row and column joint spectral radii agree:
\[
\rho_{\rm row}(T)=\rho_{\rm col}(T)=\sqrt{r(\Phi_T)}.
\]
When this number is nonzero, both maps admit a nonzero positive **compact eigenoperator** at their common spectral radius.

The radius equality persists under the strictly weaker **compact-word condition**: there is an integer \(m\ge1\) such that every product of \(m\) entries from \(T\) is compact. Under that condition, the nonzero spectra of \(\Phi_T^m\) and \(\Psi_T^m\) are complex conjugates with matching algebraic multiplicities. If their common spectral radius is positive, each of these powers has a positive compact eigenoperator at that radius. For compact tuples on separable \(H\), simultaneous finite-dimensional compressions converge to the common row/column radius.

The condition is substantive: for the \(d\) left creation isometries on full Fock space, the row radius is \(1\) and the column radius is \(\sqrt d\).

## Assumptions and scope

Here \(r(F)\) denotes the ordinary spectral radius of a bounded linear map \(F\) on a complex Banach space. For each word \(w=(i_1,\ldots,i_n)\), put \(T_w=T_{i_1}\cdots T_{i_n}\). Define
\[
\rho_{\rm row}(T)=\lim_{n\to\infty}
\left\|\sum_{|w|=n}T_wT_w^*\right\|^{1/(2n)},\quad
\rho_{\rm col}(T)=\lim_{n\to\infty}
\left\|\sum_{|w|=n}T_w^*T_w\right\|^{1/(2n)}.
\]
These limits exist by submultiplicativity of the corresponding completely positive maps. The compact-word condition requires **all** \(d^m\) length-\(m\) words to be compact, not merely one product or a compact sum. Zero common radius is allowed; the positive-eigenoperator conclusion is asserted only for strictly positive radius. For finite-section convergence, take separable \(H\) and finite-rank orthogonal projections \(P_N\) increasing strongly to \(I\).

## Proof

**1. Compactness of the completely positive maps.** Let \(F_j\) be finite-rank approximants to compact \(T_j\) with \(\|F_j-T_j\|\to0\). The maps \(X\mapsto\sum_jF_jXF_j^*\) and \(X\mapsto\sum_jF_j^*XF_j\) have finite-dimensional ranges: their outputs are supported, respectively, on the finite-dimensional spans of \(\operatorname{ran}F_j\) and \(\operatorname{ran}F_j^*\). Moreover, on the operator-norm unit ball,
\[
\|T_jXT_j^*-F_jXF_j^*\|
\le \|T_j-F_j\|(\|T_j\|+\|F_j\|).
\]
The analogous bound holds with adjoints reversed. Hence \(\Phi_T\) and \(\Psi_T\) are norm limits of finite-rank maps on \(\mathcal B(H)\), and are compact.

**2. Nonzero spectral duality.** Given a finite-rank tuple \(F\), choose a finite-dimensional subspace \(E\) containing the ranges of all \(F_j\) and \(F_j^*\). Both completely positive maps have range in the finite-dimensional corner \(\mathcal B(E)\). Their nonzero eigenvalues and algebraic multiplicities are exactly those of their restrictions to that invariant corner: relative to \(\mathcal B(H)=\mathcal B(E)\oplus Z\), the superoperators have block forms \(\begin{psmallmatrix}M&*\\0&0\end{psmallmatrix}\). On \(\mathcal B(E)\) equipped with the Hilbert–Schmidt inner product, \(\Psi_F=\Phi_F^*\) as linear maps, so their nonzero spectra are complex conjugate with matching algebraic multiplicities.

Now approximate a compact tuple by finite-rank tuples as in Step 1. The two corresponding superoperators converge in norm and both limiting superoperators are compact. For each nonzero eigenvalue of a compact operator, choose a small circle isolating it from the other spectrum and from zero. The associated Riesz projections of the approximants eventually have the same finite rank and converge in norm. Applying this simultaneously to the two finite-rank superoperators and their conjugate isolated spectral disks transfers the conjugate eigenvalue multisets, including algebraic multiplicities, to the limit. Reversing the roles yields equality of the entire nonzero multisets.

**3. Radii and positive eigenoperators.** For a positive bounded map \(F\) on the unital \(C^*\)-algebra \(\mathcal B(H)\), \(\|F\|=\|F(I)\|\). Iteration therefore gives
\[
\rho_{\rm row}(T)^2=r(\Phi_T),\qquad
\rho_{\rm col}(T)^2=r(\Psi_T).
\]
The spectral duality of Step 2 makes these radii equal. The real Banach space of self-adjoint bounded operators has a closed, normal, generating positive cone. Applying the positive compact-operator spectral theorem (Krein–Rutman) at nonzero spectral radius to each compact completely positive map gives nonzero positive eigenoperators \(A,B\) satisfying
\[
\Phi_T(A)=r(\Phi_T)A,\qquad
\Psi_T(B)=r(\Psi_T)B.
\]
As the right sides have nonzero coefficients, \(A\) and \(B\) are compact by Step 1, since each map has compact-operator-valued output.

**4. Compact words.** Suppose every length-\(m\) product is compact. The tuple of all such products, \(U=(T_w)_{|w|=m}\), is a compact tuple. Direct expansion yields \(\Phi_U=\Phi_T^m\) and \(\Psi_U=\Psi_T^m\). Applying Steps 1–3 to \(U\), then taking \(m\)-th roots of the nonnegative spectral radii, establishes all compact-word assertions. This genuinely extends compact entries: for example, \(T_1\) may be the direct sum of an identity on \(\mathbb C\) and an infinite-rank, square-zero operator on \(\ell^2\oplus\ell^2\), with \(T_2=0\). Then \(T_1\) is noncompact but every word of length two is compact, and the common radius is one.

**5. Finite sections and the obstruction.** For compact entries on separable \(H\), \(P_NT_jP_N\to T_j\) in operator norm. The two finite-dimensional completely positive maps therefore converge to the compact maps in Step 1. Compact spectral perturbation, including the quasinilpotent case by upper semicontinuity, gives convergence of their spectral radii to the common radius. On full Fock space over \(d\) letters, creation isometries \(L_j\) have orthogonal ranges, whence \(\sum_{|w|=n}L_wL_w^*\) is a nonzero projection, while \(\sum_{|w|=n}L_w^*L_w=d^nI\). Their radii are exactly \(1\) and \(\sqrt d\), respectively.

## Verification

A standalone numerical checker, `check.py`, verifies the finite-dimensional adjoint identity between the completely positive superoperators, equality of their spectra with multiplicities, agreement of their spectral radii, and the exact two-step word expansion. The last tested run passed 1,584 assertions. These finite checks are diagnostics, not substitutes for compact-operator spectral perturbation or the positive eigenoperator theorem. To reproduce: run `python check.py` with NumPy installed. The proof above is independent of those computations.

## Relationship to prior work

Scherer, Shalit, and Shamovich (2026), Example 5.2 and Remark 5.3, explicitly establish row–column radius equality for **matrix tuples** and exhibit a separating infinite-dimensional row-isometry tuple. Their paper does not assert conjugate nonzero spectra with algebraic multiplicity for compact Kraus tuples, a positive compact Perron eigenoperator, or the compact-word extension. The present argument therefore uses their definitions, agrees with their finite-dimensional identity, and explains one infinite-dimensional compactness boundary at which their counterexample cannot occur. Tornes (2026) proves operator-space identification from spectral radii tested on arbitrary tuples; his rigidity theorem does not specialize to compact-word spectral duality. The 2014 compact completely positive interpolation study of Hsu–Kuo–Tsai concerns existence of positive interpolation maps on compact-operator ideals, not equality of spectral multisets of this paired family. These are implication comparisons, not claims that absence from a search establishes publication priority.

## Limitations

The result concerns the specific row and column radii; it does not assert analogous equality for arbitrary distinct operator-space structures. The spectral-multiset duality is shown for compact entries or for the **powers** of the paired maps under compact-word hypotheses, not necessarily for the unpowered maps when individual entries are noncompact. No eigenoperator is claimed when the spectral radius is zero. The finite-section conclusion requires compact entries, and finite diagnostics cannot establish any infinite-dimensional assertion. Possible broader elementary-operator or completely-positive-map spectral theorems not explicitly using row/column terminology remain a priority risk; no independent verification is claimed.

## References

1. M. Scherer, O. M. Shalit, E. Shamovich, *On the spectral radius of operator tuples*, arXiv:2605.09354v1 (2026), Sections 1 and 5, especially Example 5.2 and Remark 5.3. https://arxiv.org/html/2605.09354v1
2. M. Tornes, *On the Shalit–Shamovich Spectral Radius*, arXiv:2610.00816v1 (2026), MSC 47A13. https://arxiv.org/html/2610.00816v1
3. O. M. Shalit and E. Shamovich, *A spectral radius for matrices over an operator space*, Advances in Mathematics 479 (2025), 110449; preprint arXiv:2501.01325.
4. M.-H. Hsu, D. L.-W. Kuo, M.-C. Tsai, *Completely positive interpolations of compact, trace-class and Schatten-p class operators*, J. Functional Analysis 267 (2014), 1205–1240; doi:10.1016/j.jfa.2014.05.013.
