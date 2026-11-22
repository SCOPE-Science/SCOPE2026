# Sharp first closure-defect stratum for Rees commutator margins

## Finding

Let \(G\) be a finite group, \(Z=Z(G)\), \(z=|Z|\), \(Q=G/Z\), and \(q=|Q|\). Let \(I\) and \(\Lambda\) be nonempty finite index sets of sizes \(c\) and \(r\), and let \(P=(p_{\lambda i})\in G^{\Lambda\times I}\) be a Rees sandwich matrix with no zero entries. Set \(T=M[G;I,\Lambda;P]\), with multiplication
\[
(i,g,\lambda)(j,h,\mu)=(i,gp_{\lambda j}h,\mu).
\]
For either of the two commutator words \(\omega_1(x,y)=x^{-1}y^{-1}xy\) and \(\omega_2(x,y)=(yx)^{-1}xy\) (local inverses), let \(M\) be the associated set of marginal elements. Define the *ordered closure defect*
\[
B(P)=|\{(a,b)\in M\times M:ab\notin M\}|.
\]

**First-defect theorem.** If \(r,c\geq2\), then either \(B(P)=0\) or
\[
B(P)\geq 4z^2(r-1)(c-1).
\]
The bound is attainable for every finite nonabelian \(G\) and every \(r,c\ge2\). The equality cases admit the following exhaustive normal form. Pick distinguished first indices, write \(u_{\lambda i}=p_{\lambda i}Z\in Q\), and normalize in the quotient by
\[
N_{\lambda i}=u_{\lambda 1}^{-1}u_{\lambda i}u_{1i}^{-1}u_{11}.
\]
Thus the first row and first column of \(N\) are identity elements. Positive equality holds precisely when there are a nonidentity \(t\in Q\), and sets \(A\) and \(C\) such that
\[
A\in\big\{\{\lambda\}:2\le\lambda\le r\big\}\cup\{\{2,\ldots,r\}\},\qquad
C\in\big\{\{i\}:2\le i\le c\big\}\cup\{\{2,\ldots,c\}\},
\]
and \(N_{\lambda i}=t\) exactly for \((\lambda,i)\in A\times C\), while all remaining entries of \(N\) are the identity. A repeated singleton/full choice when \(r=2\) or \(c=2\) represents the same pattern, not two patterns.

Set \(\kappa=2^{\mathbf{1}_{r=2}+\mathbf{1}_{c=2}}\). For \(q>1\), among *normalized quotient matrices* (first row and column equal to the identity) the zero-defect stratum consists of exactly one matrix and the first positive stratum consists of exactly
\[
\frac{rc(q-1)}{\kappa}
\]
matrices. For normalized \(G\)-valued sandwich matrices, these counts are respectively \(z^{(r-1)(c-1)}\) and \(z^{(r-1)(c-1)}rc(q-1)/\kappa\). For arbitrary labeled \(G\)-valued sandwich matrices, they are respectively
\[
z^{rc}q^{r+c-1},\qquad
z^{rc}q^{r+c-1}\frac{rc(q-1)}{\kappa}.
\]
Consequently, for independent uniform sandwich entries, the respective probabilities are
\[
\Pr(B(P)=0)=q^{-(r-1)(c-1)},\qquad
\Pr\!\left(B(P)=4z^2(r-1)(c-1)\right)
=\frac{rc(q-1)}{\kappa}q^{-(r-1)(c-1)}.
\]
These count *labeled matrices*, not isomorphism classes of semigroups. If \(q=1\) (equivalently \(G\) is abelian), every matrix has \(B(P)=0\). If \(r=1\) or \(c=1\), also \(B(P)=0\).

## Assumptions and scope

Only finite groups and finite, nonempty row/column index sets are counted. No commutativity assumption is placed on \(G\) or \(Q\). The Rees semigroup has no sandwich zeros. Defective pairs are **ordered** pairs of marginal elements, so \(M\times M\) has size \(r^2c^2z^2\). The normal-form labels refer to a fixed choice of first row and first column; different labels can yield isomorphic semigroups, which is not accounted for in the matrix counts.

## Proof

**1. Reduce membership to a quotient rectangle.** Proposition 2.2 of Shen--Wang identifies the common marginal set:
\[
M=\{(i,\zeta p_{\lambda i}^{-1},\lambda):i\in I,\lambda\in\Lambda,\zeta\in Z\}.
\]
For \(a=(i,\zeta p_{\lambda i}^{-1},\lambda)\) and \(b=(j,\xi p_{\mu j}^{-1},\mu)\), multiplication and the same membership rule give
\[
ab\notin M\iff
u_{\lambda i}^{-1}u_{\lambda j}u_{\mu j}^{-1}u_{\mu i}\ne 1_Q,
\]
where \(u_{\lambda i}=p_{\lambda i}Z\). The result does not depend on \(\zeta,\xi\), so each failing ordered quadruple \((\lambda,\mu,i,j)\) contributes exactly \(z^2\) pairs.

**2. Obtain an exact computable census.** For fixed ordered rows \((\lambda,\mu)\), define the quotient ratios
\[
v_{\lambda\mu}(i)=u_{\lambda i}u_{\mu i}^{-1}\in Q,
\quad
n_{\lambda\mu}(t)=|\{i:v_{\lambda\mu}(i)=t\}|.
\]
The displayed rectangle is identity if and only if \(v_{\lambda\mu}(i)=v_{\lambda\mu}(j)\). Thus
\[
\boxed{\frac{B(P)}{z^2}=
\sum_{\lambda,\mu\in\Lambda}\left(c^2-\sum_{t\in Q}n_{\lambda\mu}(t)^2\right).}
\]
Rows are equivalent if their quotient ratio is constant across all columns. This is an equivalence relation even for nonabelian \(Q\): if \(u_{\lambda i}=a u_{\mu i}\) and \(u_{\mu i}=b u_{\nu i}\), then \(u_{\lambda i}=ab u_{\nu i}\).

**3. Prove the sharp bound and equality rigidity.** If the matrix is not flat (the quotient rectangles are not all identity), there are at least two row-equivalence classes. Writing their sizes as positive integers \(s_1,\ldots,s_k\), the number of ordered pairs of inequivalent rows is
\[
r^2-\sum_{j=1}^{k}s_j^2\ge2(r-1).
\]
Equality means the class sizes are \(r-1,1\). For each inequivalent ordered pair of rows, the ratios assume at least two distinct values; the inequality
\[
c^2-\sum_t n_{\lambda\mu}(t)^2\ge2(c-1)
\]
follows by maximizing the sum of squares among nonconstant partitions of \(c\), and equality means precisely one exceptional column and a constant value on the other \(c-1\) columns. Summing proves the lower bound.

Equality in both inequalities forces precisely one exceptional row (when \(r=2\), either row can be called exceptional); all other rows differ from a reference row by a constant left multiplier, and the exceptional row's quotient ratios differ from a constant at precisely one column. Applying suitable left row multipliers and right column multipliers in \(Q\), the matrix therefore becomes the identity matrix with exactly one entry replaced by a nonidentity \(t\). Conversely that one-cell perturbation has exactly \(2(r-1)\) inequivalent ordered row pairs and exactly \(2(c-1)\) failing ordered column pairs per such row pair. It realizes equality.

**4. Convert the rigidity to the stated normalized forms.** Multiplying a row on the left and a column on the right by group elements preserves whether each quotient rectangle is identity (it conjugates the rectangle by a column multiplier). The normalization \(N_{\lambda i}=u_{\lambda 1}^{-1}u_{\lambda i}u_{1i}^{-1}u_{11}\) is one such transformation. If one entry of a flat matrix \(u_{\lambda i}=a_\lambda b_i\) is changed, normalization makes the affected set in the interior exactly a Cartesian product \(A\times C\): the affected row set is either the altered interior row or all interior rows if the first row was altered; the same dichotomy holds for columns. The nonidentity entries in this product all have one common value, by direct cancellation of the fixed \(a_\lambda,b_i\). Conversely each displayed rectangle pattern is obtained by an appropriate one-cell modification of a flat matrix and hence is extremal. This proves necessity and sufficiency of the normalized forms.

**5. Count the first two strata.** When \(r>2\), there are \(r\) distinct choices of \(A\): the \(r-1\) interior singletons and the full interior. When \(r=2\), the singleton equals the full interior and there is just one choice, or \(r/2\) choices. Therefore the number of distinct \(A\) is \(r/2^{\mathbf{1}_{r=2}}\), and similarly for \(C\). Every pair of supports and every \(t\in Q\setminus\{1\}\) gives a different normalized matrix, proving the count \(rc(q-1)/\kappa\). Zero defect forces all normalized entries to be identity by the rectangle criterion, giving one normalized quotient matrix. In the unnormalized quotient, arbitrary first-row and first-column entries (overlap counted once) yield \(q^{r+c-1}\) lifts of each normalized matrix. Every quotient entry has \(z\) lifts to \(G\); hence the unnormalized \(G\)-counts acquire \(z^{rc}\), whereas fixing the first row and column to the group identity leaves \(z^{(r-1)(c-1)}\) choices. Division by \(|G|^{rc}=(zq)^{rc}\) gives the two probability formulas.

## Verification

The accompanying standalone `check.py` independently compares the exact row-ratio formula with direct Rees multiplication for random \(S_3\) and dihedral-order-eight sandwich matrices (including center-size factors). It exhaustively checks all \(74,896\) binary-valued matrices in sizes \(2\) through \(4\) rows and columns, including equality rigidity. It separately enumerates the complete first positive stratum for unnormalized \(S_3\) matrices in sizes \(2\times2\), \(2\times3\), \(3\times2\), and normalized \(S_3\) matrices in sizes \(2\times4\) and \(3\times3\). An additional 400 nonabelian random instances check invariance under explicit normalization and the prescribed extremal shapes. Successful execution reports `MARGINAL_DEFECT_CHECK_OK`, `EXTREMIZER_COUNT_OK`, and `NORMALIZED_PATTERNS_OK`. These finite checks are not substitutes for Steps 1--5, which prove all finite-group and dimension cases.

## Relationship to prior work

Shen and Wang (arXiv:2611.10680, Proposition 2.2) establish the common marginal subset of a completely simple Rees semigroup and characterize **whether** it is a subsemigroup by requiring every quotient rectangle to be trivial. Their Example 2.3 supplies a \(2\times2\) nonclosed example. The present statement takes that criterion as a credited premise, then determines the *first two exact counts* of defective-product strata, the universal sharp positive gap, and every normalized equality case in arbitrary finite dimensions. The paper's later Corollary 2.14 concerns qualitative closure in all completely regular semigroups, not the quantitative finite Rees defect spectrum.

Araújo, Araújo and Kinyon (2025) study marginal inverse subsemigroups and their closure, not non-inverse completely simple Rees defect counts. Radović and Mudrinski (arXiv:2208.05237) analyze congruence commutators and nilpotency/solvability of completely simple semigroups rather than the number of products leaving the commutator-margin subset. The rectangle partition inequalities used above are elementary combinatorics and are not claimed as new outside the present semigroup classification. Historical priority of the combined quantitative result remains subject to unindexed sources.

## Limitations

No classification of **all** possible positive defect values is claimed: only the least positive value and the two corresponding strata (zero and least positive) are determined. The formulas count labeled sandwich matrices, not isomorphism classes. No extension to Rees zero matrices, infinite groups, or arbitrary completely regular semigroups is asserted. An independent external mathematical audit has not been performed.

## References

1. Lin Shen and Shoufeng Wang, *Marginal Congruences and Elements for Two Commutator Words in Completely Regular Semigroups*, arXiv:2611.10680v1 (first publicly posted 2026-11-07), Proposition 2.2, Example 2.3, Corollary 2.14. https://arxiv.org/abs/2611.10680
2. Gonçalo Araújo, João Araújo and Michael Kinyon, *Marginal subsemigroups and commutators in inverse semigroups*, Semigroup Forum 111 (2025), 351--361, DOI 10.1007/s00233-025-10548-9. https://doi.org/10.1007/s00233-025-10548-9
3. Jelena Radović and Nebojša Mudrinski, *Commutators in completely simple semigroups*, arXiv:2208.05237v3 (2023 preprint; journal version 2025). https://arxiv.org/abs/2208.05237
