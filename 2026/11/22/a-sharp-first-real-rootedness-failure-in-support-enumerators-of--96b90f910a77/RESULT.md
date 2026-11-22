# A sharp first real-rootedness failure in support enumerators of standard-example posets

## Finding
For every integer \(m\geq1\), let the standard-example poset \(S_m\) have minima \(a_1,\ldots,a_m\) and maxima \(b_1,\ldots,b_m\), with \(a_i<b_j\) exactly when \(i\neq j\). Its preorder-polytope support enumerator \(H_m(t)\) has the complete gamma expansion
\[
H_m(t)=\sum_{j=0}^{m}\left(\binom mj^2-m\mathbf1_{\{j=1\}}\right)t^j(1+t)^{2m-2j}.
\]
Equivalently, \(\Gamma_m(q)=\sum_{j=0}^{m}\binom mj^2q^j-mq\). Among the standard examples with \(1\le m\le12\), the support enumerator \(H_m\) is real-rooted precisely for \(1\le m\le11\): the first failure occurs at \(m=12\), where \(\Gamma_{12}\) has ten distinct negative real roots and two nonreal conjugate roots. No claim is made about every \(m\ge13\).

## Assumptions and scope
For a finite poset \(P\) on \(E\), an ideal \(I\) is downward closed. Define the preorder polytope
\[
\mathcal Q_P=\{x\in\mathbb R_{\ge0}^{E}:\sum_{e\in I}x_e\le |I|\text{ for every ideal }I\},\qquad
H_P(t)=\sum_{x\in\mathcal Q_P\cap\mathbb Z^{E}}t^{|\operatorname{supp}(x)|}.
\]
The \(\gamma\)-polynomial of the palindromic \(H_P\) on \(2m\) elements is defined by \(H_P(t)=(1+t)^{2m}\Gamma_P(t/(1+t)^2)\). These are support-enumerator polynomials, not the Ehrhart \(h^*\)-polynomial of the preorder polytope. The statement applies to labelled standard-example posets but depends only on their isomorphism types, including \(m=1\) and \(m=2\).

## Proof
**Gamma census.** Zhong's matching theorem for finite preorders [2, Theorem 1 and its matching proof] identifies \(\gamma_{P,j}\) with the number of pairs \((N,T)\) of disjoint \(j\)-element subsets of \(E\) admitting a bijection \(N\to T\) along strict comparabilities. In \(S_m\), all strict comparabilities run from minima to maxima, so \(N=\{a_i:i\in A\}\) and \(T=\{b_j:j\in B\}\), where \(|A|=|B|=j\). Such a bijection is a matching in the complete bipartite graph on \(A,B\), except for the forbidden diagonal pairs \((i,i)\).

For \(j=0\) there is the empty matching; for \(j=1\), exactly the \(m\) diagonal source–target choices are forbidden among \(m^2\). For \(j\ge2\), Hall's criterion holds for every \(A,B\): the neighborhood of a singleton source has at least \(j-1\ge1\) targets, while the union of neighborhoods of any two distinct sources equals all \(j\) targets. Thus each of the \(\binom mj^2\) choices of \((A,B)\) is matchable. This proves the displayed gamma and support enumerator formulas for every \(m\ge1\).

**Exact root cutoff.** Write \(f_m(q)=\Gamma_m(q)\). All its nonzero coefficients are positive for \(m\ge2\), so it has no nonnegative real root. For \(m=1\), \(f_1=1\); for \(m=2\), \(f_2=(1+q)^2\). For each \(3\le m\le12\), perform rational Sturm division on \(f_m,f'_m\), keeping the negative of each remainder and normalizing each polynomial only by a strictly positive rational factor. Remove zero entries when counting sign variations. The resulting variation values at \(-\infty\) and \(0\), respectively, are

| \(m\) | \(V(-\infty)\) | \(V(0)\) | Distinct negative roots |
|---|---:|---:|---:|
| 3 | 3 | 0 | 3 |
| 4 | 4 | 0 | 4 |
| 5 | 5 | 0 | 5 |
| 6 | 6 | 0 | 6 |
| 7 | 7 | 0 | 7 |
| 8 | 8 | 0 | 8 |
| 9 | 9 | 0 | 9 |
| 10 | 10 | 0 | 10 |
| 11 | 11 | 0 | 11 |
| 12 | 11 | 1 | 10 |

The exact calculations and recurrence are reproduced by `standard_example_verify.py`, with rational fractions and integer sign normalization. At \(m=12\),
\[
\begin{split}
f_{12}(q)={}&1+132q+4356q^2+48400q^3+245025q^4+627264q^5\\
&+853776q^6+627264q^7+245025q^8+48400q^9+4356q^{10}+144q^{11}+q^{12}.
\end{split}
\]
The rational Sturm chain of \(f_{12}\) terminates in a nonzero constant, so its roots are simple. Ten are real and negative, and the remaining two form a nonreal conjugate pair. For \(3\le m\le11\), the negative real-root count equals the full polynomial degree. Finally, \(H_m(t)=(1+t)^{2m}f_m(t/(1+t)^2)\). Every negative real root \(q\) of \(f_m\) yields two negative real solutions of \(t=q(1+t)^2\), with possible coalescence at \(q=-1/4\); a nonreal root of \(f_m\) cannot arise from any real \(t\). The transformation therefore preserves the real-rootedness equivalence, proving the first failure at \(m=12\).

## Verification
Run `python standard_example_verify.py` using Python 3.9 or later; it needs no third-party libraries. It independently enumerates disjoint matchable endpoint pairs for \(1\le m\le7\), directly enumerates lattice points against all order-ideal inequalities for \(1\le m\le4\), and evaluates rational Sturm sequences for \(2\le m\le12\). The final output is `VERIFY_OK`. The exact Sturm certificate decides the finite sharp cutoff, whereas the Hall argument proves the all-\(m\) polynomial formula.

## Relationship to prior work
Athanasiadis–Chapoton [1, Proposition 9.2] prove the gamma expansion \(\sum_j\binom mj^2q^j\) and real-rootedness for the **complete** two-level order (ordinal sum of two \(m\)-element antichains). Zhong [2] proves gamma positivity and the universal matching interpretation, and explicitly discusses Patel's eight-element counterexample to real-rootedness in general. Hence neither gamma positivity nor the existence of general counterexamples is new here. The present result isolates the deleted-diagonal standard examples and establishes their exact gamma formula and sharp first family-specific real-rootedness failure. Zhong [3] analyzes two-row Ferrers and comb families, not the standard-example incidence relation.

## Limitations
This proves the first failure within the sequence \(S_1,S_2,\ldots\) at \(S_{12}\), not the failure of every larger \(S_m\), nor minimality among arbitrary posets. The universal matching theorem and the complete two-level formula are prior results used as inputs. Priority relative to unindexed or inaccessible exact standard-example support-enumerator studies remains provisional. The finite checker is a certificate for orders at most twelve; it is not an infinite-root theorem.

## References
1. C. A. Athanasiadis and F. Chapoton, *Polytopes and posets associated to preorders*, arXiv:2605.26916v1 (first public 2026-05-26), https://arxiv.org/html/2605.26916v1, especially §5 and Proposition 9.2.
2. Y. Zhong, *Gamma-positivity of support enumerators of preorders*, arXiv:2611.16858v1 (first public 2026-11-12), https://arxiv.org/html/2611.16858v1, especially Theorem 1, §2 and Example 4.
3. Y. Zhong, *Support enumerators of two-row grids and comb posets*, arXiv:2611.11259v1 (first public 2026-11-08), https://arxiv.org/html/2611.11259v1, especially §1 and §6.
