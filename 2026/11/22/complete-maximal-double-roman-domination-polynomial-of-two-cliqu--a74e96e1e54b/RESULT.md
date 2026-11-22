# Complete maximal double Roman domination polynomial of two-clique prisms

## Finding

For every integer \(n\ge 4\), let \(G_n=K_2\square K_n\) be two labelled \(n\)-cliques \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with matching edges \(a_i b_i\). A maximal double Roman dominating function is a labelling \(f:V(G_n)\to\{0,1,2,3\}\) satisfying both double Roman defender conditions and the requirement that the zero-labelled set is **not** a dominating set.

Write \(\omega(f)=\sum_v f(v)\) and \(P_n(z)=\sum_f z^{\omega(f)}\), summed over all such named-vertex labellings. Define
\[
 a=z+z^2+z^3,\qquad E_n=a^n-z^n,
\]
\[
 B_n=(1+z+z^2+z^3)^n-a^n-(1+z)^n+z^n-nz^2(1+z)^{n-1}+nz^{n+1},
\]
\[
 T=2z^2+2z^3+z^4.
\]
Then the complete weight polynomial is
\[
\boxed{\begin{aligned}
P_n(z)={}&E_n^2+2z^n(z^2+z^3)^n\\
&+2E_n B_n\\
&+2nz^2a\bigl(T^{n-1}-(za)^{n-1}\bigr)\\
&+2\bigl((2z^3+z^4)^n-(z^3+z^4)^n-z^{3n}\bigr).
\end{aligned}}
\]
In particular,
\[
\boxed{\gamma_{dR}^{m}(G_n)=n+4,\qquad [z^{n+4}]P_n(z)=2n^2.}
\]
Exactly the following \(2n^2\) minimum functions occur: choose which clique has no zeros; put a single label \(2\) and \(n-1\) labels \(1\) there, choosing its position freely; put a single label \(3\) and \(n-1\) labels \(0\) in the other clique, again choosing its position freely. The two positions need not match. Every integer weight in the entire interval \([n+4,6n]\) occurs, and no weight outside it occurs.

The total number of admissible functions is
\[
\boxed{P_n(1)=9^n-1+2(3^n-1)\bigl(4^n-3^n-2^n+1-n2^{n-1}+n\bigr)+6n\bigl(5^{n-1}-3^{n-1}\bigr).}
\]

## Assumptions and scope

Graphs are finite, simple and undirected. The product is Cartesian: all distinct vertices in the same clique are adjacent, and the only inter-clique edges are the matching edges. A label \(0\) needs either a label-\(3\) neighbor or two **distinct** label-\(2\) neighbors. A label \(1\) needs a label-\(2\) or label-\(3\) neighbor. Labels \(2\) and \(3\) have no separate defender requirement. The zero set is not dominating precisely when some positive vertex and all its neighbors are positive. All labellings on named vertices are counted separately, with the two cliques distinct. The displayed family formulas apply for every integer \(n\ge4\).

## Proof

**1. Rigidity of the zero set.** Suppose a zero occurs in each clique. Every positive vertex has a zero neighbor within its own clique. Thus the zero set dominates all positive vertices and of course dominates itself, contradicting maximality. Hence at least one clique is zero-free. If only clique \(A\) is zero-free and \(B\) contains a zero, the zero set is not dominating if and only if \(B\) contains at least one positive vertex: its matched partner in \(A\) is a witness. Count this case and double by symmetry, leaving the both-zero-free case to subtract overlap exactly once.

**2. Both cliques zero-free.** Each has labels from \(\{1,2,3\}\). If each clique has at least one label at least \(2\), every label \(1\) has a defender in its own clique; the polynomial is \(E_n^2\). If exactly one clique has no high label, that clique is all \(1\). Its vertices require their matched partners to be high, so the opposite clique must consist entirely of labels \(2\) or \(3\). These two exclusive orientations contribute \(2z^n(z^2+z^3)^n\). Two all-one cliques are infeasible.

**3. Zeroes only in \(B\).** Since \(A\) is positive and some \(b_i=0\), the matched \(a_i\) cannot be defended by \(b_i\), so \(A\) must have at least one high label; its polynomial is \(E_n\). Let \(s\) and \(t\) denote the numbers of \(2\)- and \(3\)-labels in \(B\). We distinguish three disjoint regimes.

If \(t\ge1\), or \(t=0,s\ge2\), every \(0\) and \(1\) in \(B\) is defended within \(B\), independent of the choice of \(A\). The polynomial for such \(B\) with at least one zero is \(B_n\): start with all words containing a zero, subtract the words with no \(3\) and at most one \(2\). This gives exactly the displayed expression for \(B_n\), and the contribution is \(E_n B_n\).

If \(t=0,s=1\), choose the unique label-\(2\) vertex \(b_j\) in \(n\) ways. The paired \(a_j\) is any positive label, giving factor \(a\). For each \(i\ne j\), a label \(1\) at \(b_i\) allows any positive \(a_i\), of weight polynomial \(za\), while a zero at \(b_i\) needs the second label-\(2\) defender at \(a_i\) (or a label \(3\) there), giving \(z^2+z^3\). Their sum is \(T=za+z^2+z^3\). At least one of these \(b_i\) must be zero; subtract the no-zero choices. The contribution is therefore \(nz^2a(T^{n-1}-(za)^{n-1})\). A high label in \(A\) is automatic because at least one zero in \(B\) forces its matched label to be high.

Finally, if \(t=s=0\), each \(b_i\) is \(0\) or \(1\). The former forces \(a_i=3\); the latter forces \(a_i\in\{2,3\}\). Each of the \(n\) paired columns has weight polynomial \(2z^3+z^4\). There must be at least one zero in \(B\), and at least one positive \(b_i\) to witness maximality. Subtract the all-one and all-zero words, obtaining \((2z^3+z^4)^n-(z^3+z^4)^n-z^{3n}\). These three regimes partition the case. Double their sum and add the both-zero-free case to prove the polynomial identity without any asymptotic or finite-test assumption.

**4. Minimum and all optimizers.** The both-zero-free term has minimum weight \(2n+2\). In the first one-sided regime \(B_n\) has minimum degree \(3\), uniquely realized (up to location) by one \(3\) and remaining zeros; \(E_n\) has minimum degree \(n+1\), realized by one \(2\) and remaining ones. This gives weight \(n+4\), with \(n^2\) choices per oriented pair of cliques. The one-\(2\) regime has minimum degree \(2n+1\), and the zero-high regime has minimum degree \(3n\). For every \(n\ge4\), both exceed \(n+4\). The claimed minimum and complete optimizer classification follow.

**5. Weight spectrum and total count.** Holding a single \(3\) in \(B\), other \(B\)-labels zero, and varying positive \(A\)-words containing at least one high label yields every weight from \(n+4\) through \(3n+3\). The both-zero-free words with high labels in both cliques realize every weight from \(2n+2\) through \(6n\). These intervals overlap for \(n\ge4\), and the minimum bound excludes lower weights. The upper bound is \(6n\) because no vertex exceeds label \(3\). Substituting \(z=1\) in the polynomial and simplifying gives the displayed closed total count.

## Verification

`verification/direct_enumeration.cpp` independently examines every one of the \(4^{2n}\) possible labellings for \(n=3,4,5,6\), checking the graph adjacency, every zero/one defender condition, and whether the zero set dominates. `verification/formula_check.py` computes every coefficient by independent polynomial convolutions, checks the closed total formula through \(n=14\), and checks the minimum and contiguous spectrum. `verification/crosscheck.py` compares **all** coefficients from the direct enumerator against the symbolic formula for \(3\le n\le6\); the test returns `CROSSCHECK_OK`. These finite tests check implementation and boundaries but are not the proof for all \(n\).

| \(n\) | Minimum weight | Minimum functions | Total admissible functions |
| ---: | ---: | ---: | ---: |
| 4 | 8 | 32 | 30,032 |
| 5 | 9 | 50 | 402,068 |
| 6 | 10 | 72 | 5,175,000 |
| 7 | 11 | 98 | 64,994,588 |

## Relationship to prior work

Abdollahzadeh Ahangar, Chellali, Sheikholeslami and Valenzuela-Tripodoro introduce maximal double Roman domination and prove general inequalities and algorithms, including results for paths, cycles and trees. Their fully inspected open-access preprint does not supply a weight polynomial or optimizer classification for the matched two-clique prism. Rupnik Poklukar and Žerovnik survey the invariant and nearby double Roman variants. The cocktail-party graph and the quasi-total double Roman problem on complete prisms are different, respectively in the underlying graph and the defense/maximality requirements; their known exact values do not imply this theorem. Literature and research-record searches did not identify identical or stronger covering statements; this is not a proof that no such earlier theorem exists.

## Limitations

The stated formula and classification concern the Cartesian product of two complete layers with exactly a perfect matching between them, with \(n\ge4\), under the standard maximal double Roman definition. Neither arbitrary graph products nor nonmaximal double Roman functions are classified. The original article appeared in print before its 2024 public preprint, so its precise earliest online-publication day is not asserted here. Historical publication-priority searches are necessarily incomplete; independent mathematical validation has not been performed.

## References

1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami and J. C. Valenzuela-Tripodoro, *Maximal double Roman domination in graphs*, Applied Mathematics and Computation 414 (2022), article 126662, DOI: https://doi.org/10.1016/j.amc.2021.126662; accessible full-text preprint https://arxiv.org/abs/2402.07013 (posted 2024-02-10).
2. D. Rupnik Poklukar and J. Žerovnik, *Double Roman Domination: A Survey*, Mathematics 11 (2023), 351, public 2023-01-09, https://doi.org/10.3390/math11020351, especially section 4.8.
3. Institutional repository record for the primary paper, public author-copy availability dated 2024-02-07, https://rodin.uca.es/handle/10498/30718?show=full.
