# Exact Euclidean projection, matching distance law, and parity-dependent deep holes of chainlink polytopes

## Finding

Let \(s\ge3\) be an integer, let \(\ell>0\), and let \(a_i\ge2\ell\) be real numbers, with indices read cyclically. Define the enclosing box \(B=\prod_{i=1}^s[0,a_i]\) and the chainlink body
\[
C=\left\{x\in B:x_i-x_{i+1}\le a_i-\ell\ \text{for all }i\in\{1,\ldots,s\}\right\}.
\]
Set \(d_i(x)=(x_i-x_{i+1}-a_i+\ell)_+\). The exact Euclidean nearest-point map for **every** \(x\in B\) is
\[
\boxed{\Pi_C(x)=x-\tfrac12\sum_{i=1}^s d_i(x)(e_i-e_{i+1})}.
\]
The squared distance is \(D(x)^2=\tfrac12\sum_i d_i(x)^2\), and its sharp maximum on the box is \(\ell^2\lfloor s/2\rfloor/2\). The maximizers form exactly two alternating box vertices for even \(s\), or the union of \(s\) coordinate line segments for odd \(s\).

For \(X\) uniformly distributed by volume in \(B\), write \(D=D(X)\), \(q_i=\ell^2/(2a_i a_{i+1})\), and
\[
\psi_\ell(t)=\frac{2}{\ell^2}\int_0^\ell(\ell-u)e^{-tu^2/2}\,du,\qquad t\ge0.
\]
With \(\mathcal M(C_s)\) the set of all matchings of the cycle (including the empty matching), the complete Laplace transform is
\[
\boxed{\mathbb E e^{-tD^2}=\sum_{M\in\mathcal M(C_s)}\prod_{i\in M}q_i(\psi_\ell(t)-1)}.
\]
In particular
\[
\boxed{\mathbb E D^2=\frac{\ell^4}{24}\sum_{i=1}^s\frac{1}{a_i a_{i+1}}}.
\]
The atom at zero is \(\sum_{M\in\mathcal M(C_s)}(-1)^{|M|}\prod_{i\in M}q_i\), a volume ratio already obtainable from the original matching inclusion--exclusion formula, not a new volume theorem.

## Assumptions and scope

The Euclidean norm is the ordinary coordinate norm in \(\mathbb R^s\), not an affine-normalized norm. Parameters \(a_i\) and \(\ell\) are real, with \(0<2\ell\le\min_i a_i\). Index \(s+1\) means index \(1\). A matching is a set of edges \((i,i+1)\) with no common endpoint. \((r)_+=\max(r,0)\). The projection assertion concerns points **in the specified box**; it does not claim the same formula for arbitrary points outside that box.

## Proof

**1. Active edges are a matching.** If \(d_i(x)>0\), then \(x_i>a_i-\ell\ge\ell\) and \(x_{i+1}<\ell\), since \(x_i\le a_i\). Hence \(d_i>0\) and \(d_{i+1}>0\) cannot both hold. Neither can \(d_{i-1}>0\) and \(d_i>0\). Thus the active edges form a cycle matching and their normal vectors \(e_i-e_{i+1}\) are pairwise orthogonal.

**2. The projection candidate is feasible.** Let \(A=\{i:d_i(x)>0\}\) and define \(p=x-\tfrac12\sum_{i\in A}d_i(x)(e_i-e_{i+1})\). For each active edge \(i\), its two corrected coordinates satisfy
\[
p_i=x_i-\tfrac12 d_i\ge a_i-\ell\ge\ell,\quad
p_{i+1}=x_{i+1}+\tfrac12d_i\le\ell,\quad
p_i-p_{i+1}=a_i-\ell.
\]
Here \(d_i\le\ell-x_{i+1}\) and \(x_i=a_i-\ell+x_{i+1}+d_i\) establish both endpoint bounds; they also show \(0\le p_i\le a_i\), \(0\le p_{i+1}\le a_{i+1}\). Disjoint active edges do not share corrected coordinates. For an inactive constraint at edge \(j\), if \(j-1\) is active then \(p_j\le\ell\le a_j-\ell\), so \(p_j-p_{j+1}\le a_j-\ell\). If \(j+1\) is active then \(p_{j+1}\ge\ell\), so \(p_j-p_{j+1}\le a_j-\ell\). If neither neighbor is active, both coordinates are unchanged and the constraint held originally. Hence \(p\in C\).

**3. Nearest-point certificate.** The residual \(x-p=\sum_{i\in A}(d_i/2)(e_i-e_{i+1})\) is a nonnegative combination of outward normals to inequalities tight at \(p\). Therefore \(\langle x-p,z-p\rangle\le0\) for all \(z\in C\). Expanding \(\|x-z\|^2\) shows \(\|x-z\|^2\ge\|x-p\|^2\), with equality only at \(z=p\). Orthogonality of active normals gives \(\|x-p\|^2=\sum_{i\in A}d_i^2/2\).

**4. Complete deep-hole classification.** Since every defect is at most \(\ell\) and at most \(\lfloor s/2\rfloor\) defects are positive, the stated distance bound holds. Equality requires a maximum cycle matching of positive edges and \(d_i=\ell\) for each. This last equality is equivalent to \(x_i=a_i\) and \(x_{i+1}=0\). For even \(s\), the cycle has exactly two perfect matchings, which pin down precisely two alternating box vertices. For odd \(s\), there are exactly \(s\) maximum matchings, each covering all but one coordinate and leaving that coordinate free in its full box interval. These and only these are the farthest-point segments.

**5. Exact stochastic law.** Fix any matching \(M\). The event that every edge in \(M\) is violated involves disjoint pairs of independent uniform coordinates. For an edge \(i\), put \(u=d_i>0\). Its unnormalized area density within the box's \((i,i+1)\) coordinate rectangle is \(\ell-u\) for \(0<u<\ell\), so \(\Pr(d_i>0)=q_i\); conditional on positivity, \(d_i/\ell\sim\operatorname{Beta}(1,2)\). The marked defects for all edges of any such matching are independent **under their joint violation event**. Expand
\[
e^{-tD^2}=\prod_i\bigl[1+\mathbf1_{\{d_i>0\}}(e^{-td_i^2/2}-1)\bigr].
\]
Every term indexed by a nonmatching vanishes. Integrating each matching term factors into \(q_i(\psi_\ell(t)-1)\), giving the Laplace identity. Differentiating at zero, or using \(\mathbb E[(d_i/\ell)^2\mid d_i>0]=1/6\), gives \(\mathbb E D^2=\sum_i q_i\ell^2/12\), as displayed. At \(t\to\infty\), dominated convergence gives the zero-distance atom. No independence is asserted conditional on an **exact** (exclusive) active set.

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. It checks independent quadratic-program solutions against the stated pointwise projection and matching-law moments, plus finite box-corner deep-hole cases. These computations test but do not replace the universal analytic proof. The formulas, proof and dependencies are complete within this package.

## Relationship to prior work

Kantarcı Oğuz, Özel and Ravichandran introduced chainlink polytopes and established the cycle-matching inclusion--exclusion formula for their **volume** (Proposition 6.8, first preprint 2022-11-15). Their corner-factorization is used explicitly in Step 5, but their result does not state the global Euclidean nearest-point map, the sharp Hausdorff gap and complete deep-hole locus, or the Laplace law of squared metric error. Other recent work studies coordinate-sum sections and radial vertex shells, different metrics and random variables. The present result is an exact Euclidean projection and random correction law from the enclosing box, not a claim to the known volume computation.

## Limitations

The admissible link condition \(2\ell\le\min a_i\) is essential for the provided feasibility proof; outside it the formula need not hold. The random law concerns uniform points in the enclosing box, not uniform points in the chainlink body, and the nearest-point identity is not claimed outside the box. An unindexed or otherwise unavailable equivalent result remains a historical priority risk. No independent mathematical audit has been performed.

## References

1. E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (2022-11-15), especially definition and Proposition 6.8. https://arxiv.org/abs/2211.08382
2. *Tilted-matching law and Gaussian section fluctuations of chainlink polytopes* (2026), available indexed abstract at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-tilted-matching-law-and-gaussian-section-fluctuations-of-chainli--34949f1e593d (different section observable).
3. *The first Euclidean radial vertex shell of chainlink polytopes* (2026), available indexed abstract at https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-first-euclidean-radial-vertex-shell-of-chainlink-polytopes--ba6c425a7f01 (different vertex radius observable).
