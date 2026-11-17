# An exact right-spine versus degree-class covariance profile for random binary search trees

## Finding
For a uniformly permutation-generated binary search tree with \(n\ge 2\) distinct ordered keys, let \(R_n\) count vertices on the rightmost root-to-key-\(n\) path, including both endpoints. Let \(N_{n,d}\) count nodes with exactly \(d\) children. Define
\[
c_n=\frac{(n-2)(n+1)}{12n(n-1)}.
\]
Then the **entire three-class covariance profile** is
\[
\left(\operatorname{Cov}(R_n,N_{n,0}),\operatorname{Cov}(R_n,N_{n,1}),\operatorname{Cov}(R_n,N_{n,2})\right)=(c_n,-2c_n,c_n).
\]
All three values vanish for \(n=1,2\); for every \(n\ge3\) the signs are strictly positive, negative, positive, respectively. They approach \((1/12,-1/6,1/12)\). This exhibits a nonzero limiting mixed covariance between the search path for the largest key and the global leaf count, even though their marginal fluctuation scales grow differently. Moreover,
\[
\mathbb E[R_nN_{n,0}]=\frac{n+1}{3}H_{n+1}-\frac14-\frac1{6n(n-1)}\qquad(n\ge2).
\]

## Assumptions and scope
Choose one of the \(n!\) permutations of \(\{1,\dots,n\}\) with equal probability and insert its keys in order into an initially empty ordinary, unbalanced binary search tree. Each vertex has zero, one, or two children. Define \(R_0=0\), \(N_{0,d}=0\); for \(n=1\), \(R_1=N_{1,0}=1\) and \(N_{1,1}=N_{1,2}=0\). Let \(H_n=\sum_{j=1}^n j^{-1}\) (\(H_0=0\)). The path length counts *vertices*; the alternative edge-depth statistic \(R_n-1\) has the same covariances. No other distribution on binary tree shapes is claimed.

## Proof
Let \(L_n=N_{n,0}\), \(h_n=\mathbb E R_n\), \(\ell_n=\mathbb E L_n\), and \(q_n=\mathbb E(R_nL_n)\), with all these zero at \(n=0\). When \(n=1\), all equal one. For \(n\ge2\), the root key is uniform, so the left and right subtree sizes \(a,b\) satisfy \(a+b=n-1\), and \(b\) is uniform in \(\{0,\dots,n-1\}\). Conditional on these sizes the two subtrees are independent uniform binary search trees. Exactly
\[
R_n=1+R_b,\qquad L_n=L_a+L_b.
\]
Therefore the recurrences, valid at \(n\ge2\), are
\[
nh_n=n+\sum_{b=0}^{n-1}h_b,\qquad n\ell_n=\sum_{b=0}^{n-1}(\ell_{n-1-b}+\ell_b),
\]
\[
nq_n=n\ell_n+\sum_{b=0}^{n-1}\bigl(q_b+\ell_{n-1-b}h_b\bigr).
\]
The last recurrence also holds at \(n=1\), since \(q_1=\ell_1=1\). Solving the first two recurrences (including \(\ell_1=1\)) gives \(h_n=H_n\) and \(\ell_n=(n+1)/3\) for \(n\ge2\).

Introduce ordinary generating functions \(H(z)=\sum_{n\ge0}h_nz^n\), \(L(z)=\sum_{n\ge0}\ell_nz^n\), \(Q(z)=\sum_{n\ge0}q_nz^n\). They satisfy
\[
H(z)=\frac{-\log(1-z)}{1-z},\qquad L(z)=\frac1{3(1-z)^2}-\frac{1-z}3,
\]
\[
Q'(z)=L'(z)+\frac{Q(z)}{1-z}+L(z)H(z),\qquad Q(0)=0.
\]
Direct differentiation verifies the unique formal-power-series solution
\[
Q(z)=\frac{1-\log(1-z)}{3(1-z)^2}-\frac1{4(1-z)}-\frac{1-z}{12}-\frac{(1-z)\log(1-z)}6.
\]
Using \([z^n](1-z)^{-2}(1-\log(1-z))=(n+1)H_{n+1}\) and \([z^n](1-z)\log(1-z)=1/[n(n-1)]\) for \(n\ge2\), we obtain
\[
q_n=\frac{n+1}3 H_{n+1}-\frac14-\frac1{6n(n-1)}.
\]
Subtract \(h_n\ell_n=(n+1)H_n/3\), use \(H_{n+1}-H_n=1/(n+1)\), and simplify:
\[
\operatorname{Cov}(R_n,L_n)=\frac112-\frac1{6n(n-1)}=\frac{(n-2)(n+1)}{12n(n-1)}=c_n.
\]
Finally every nonempty binary tree satisfies \(N_{n,0}=N_{n,2}+1\) and \(N_{n,0}+N_{n,1}+N_{n,2}=n\). Taking covariances with \(R_n\) proves \((c_n,-2c_n,c_n)\). The algebra gives zero at \(n=2\), and the \(n=1\) tree is deterministic. Strict signs and limiting constants follow immediately. This is an all-\(n\) proof; finite checks below are supplemental.

## Verification
The standalone file `verify.py` implements two independent finite checks using exact rational arithmetic and no libraries beyond Python's standard library. First, a recurrence computation verifies the joint moment/covariance identity for all \(2\le n\le160\) (159 checks). Second, explicit construction of the search tree for *every* permutation up to \(n=9\) verifies all three degree covariances (27 comparisons over 409,113 permutations, including \(n=1\)). Run `python verify.py` with Python 3. The tests do not prove the infinite statement; the formal generating-function derivation above does. The recurrence output for \(n\ge2\) also validates \(h_n=H_n\) and \(\ell_n=(n+1)/3\).

## Relationship to prior work
Holmgren and Janson (arXiv:1406.6883), especially Section 8.1, give the degree-class means/variances and joint laws of fringe-subtree counts, and their Section 8.1 mentions right paths in a recursive-tree correspondence. Their inspected results do not state a finite-\(n\) mixed covariance with the distinguished root-to-largest-key path; sums of independent fringe counts and a distinguished extreme-key path are not interchangeable. Bóna and Pittel (arXiv:1412.2796) analyze vertex rank *from descendant leaves*, which differs from the depth of the maximum key. This result uses classical root splitting but gives an explicit cross-statistic not determined by separate marginals. A bounded search did not establish exhaustive historical novelty.

## Limitations
The claim is restricted to ordinary random-permutation binary search trees and to an extreme-key search path, not a generic uniformly selected key. Equalities between degree-class covariances for a fixed \(n\) follow from deterministic binary-tree degree identities; only the mixed leaf/right-spine covariance requires a new calculation. Older literature on joint records and permutation local patterns or mixed search-tree statistics could imply the answer without the present terminology. No independent validation or uniqueness-of-priority certification is asserted.

## References
- Holmgren, C. and Janson, S., *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees* (first posted 2014-06-26), arXiv:1406.6883, especially Theorem 1.12 and Section 8.1, https://arxiv.org/abs/1406.6883.
- Bóna, M. and Pittel, B., *On a random search tree: asymptotic enumeration of vertices by distance from leaves* (first posted 2014-12-08), arXiv:1412.2796, https://arxiv.org/abs/1412.2796.
- Devroye, L., *Limit laws for local counters in random binary search trees* (1991), cited in Holmgren and Janson, Section 8.1; a marginal-outdegree antecedent.
