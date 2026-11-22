# Generic decrement density and a silver-ratio resonance in Beatty-induced nested forcing

## Finding
For a real parameter \(0<\alpha<1\), define
\[q_\alpha(n)=1+\lfloor\alpha n\rfloor\quad(n\ge1),\]
and its induced forcing by \(f_\alpha(1)=0\) and
\[f_\alpha(n)=q_\alpha(n)-q_\alpha(n-q_\alpha(n-1)),\qquad n\ge2.\]
The nested recursion \(q(n)=q(n-q(n-1))+f(n)\), \(q(1)=1\), then has solution \(q=q_\alpha\).

**Generic decrement law.** If \(0<\alpha<1/2\) and \(1,\alpha,\alpha^2\) are linearly independent over \(\mathbb Q\), then
\[\lim_{N\to\infty}\frac1N\#\{2\le n\le N:f_\alpha(n+1)-f_\alpha(n)=-1\}=\alpha(1-2\alpha)>0.\]
The independence assumption holds, in particular, for every transcendental \(\alpha\) in that interval, hence for Lebesgue-almost every such parameter.

**Quadratic resonance.** For \(\alpha=\sqrt2-1\), one has \(f_\alpha(n+1)-f_\alpha(n)\in\{0,1\}\) for every positive integer \(n\), despite \(\alpha<1/2\). The previously established fact that forcing is slow for \(1/2\le\alpha<1\) is not claimed as new.

## Assumptions and scope
Here \(\lfloor t\rfloor\) means the greatest integer at most \(t\), \(\{t\}=t-\lfloor t\rfloor\), and a slow integer sequence has successive differences in \(\{0,1\}\). Every index in the nested recursion is positive: since \(1\le q_\alpha(n)\le n\), the index \(n-q_\alpha(n-1)\) lies in \(\{1,\ldots,n-1\}\). The forcing is nonnegative, since \(q_\alpha\) is nondecreasing and this index does not exceed \(n\). The generic density assertion does not cover rational or quadratic irrational parameters.

## Proof
Put \(s_j=q_\alpha(j)-q_\alpha(j-1)\in\{0,1\}\) for \(j\ge2\). For \(n\ge2\), write \(t_n=n-q_\alpha(n-1)\). Then \(t_{n+1}-t_n=1-s_n\), and exact subtraction gives
\[f_\alpha(n+1)-f_\alpha(n)=s_{n+1}-(1-s_n)s_{t_n+1}.\tag{1}\]
Thus every difference lies in \(\{-1,0,1\}\), and it is negative precisely when \(s_n=s_{n+1}=0\) and \(s_{t_n+1}=1\). The first difference, \(f_\alpha(2)-f_\alpha(1)=\lfloor2\alpha\rfloor\), belongs to \(\{0,1\}\).

Assume \(\alpha<1/2\), set \(m=n-1\) and \(u=\{\alpha m\}\). Since \(s_j=1\) exactly when \(\{\alpha(j-1)\}\ge1-\alpha\), the two consecutive zero increments mean precisely
\[0\le u<1-2\alpha.\tag{2}\]
Moreover, \(t_n=m-\lfloor\alpha m\rfloor=(1-\alpha)m+u\). If \(v=\{\alpha(1-\alpha)m\}\), then the last condition for a decrement is
\[\{v+\alpha u\}\ge1-\alpha.\tag{3}\]
Equations (2)--(3) are exact and have no asymptotic error.

When \(1,\alpha,\alpha^2\) are linearly independent over \(\mathbb Q\), so are \(1,\alpha,\alpha(1-\alpha)\). By the two-dimensional Weyl--Kronecker equidistribution theorem, the pairs \((\{\alpha m\},\{\alpha(1-\alpha)m\})\) equidistribute in \([0,1)^2\). The set (2)--(3) is Jordan measurable; for each fixed \(u\in[0,1-2\alpha)\), the allowed set of \(v\) has length exactly \(\alpha\), because translation modulo one preserves Lebesgue measure. Its area is therefore \(\alpha(1-2\alpha)\). Equidistribution proves the density assertion, and its positivity excludes slow forcing for these parameters.

At \(\alpha=\sqrt2-1\), the relations \(\alpha^2=1-2\alpha\) and \(\alpha(1-\alpha)=3\alpha-1\) hold. For \(0\le u<1-2\alpha=\alpha^2\) one has \(v=\{3\alpha m\}=\{3u\}\) and
\[0\le(3+\alpha)u<(3+\alpha)\alpha^2=1-\alpha<1.\]
Hence \(\{v+\alpha u\}=(3+\alpha)u<1-\alpha\), contradicting (3). There are no negative increments; (1) and the initial difference show that \(f_\alpha\) is slow for every index. This proves the exceptional assertion.

## Verification
The standalone `verify.py` checks the exact finite-index indicator (1)--(3) against explicit floor-defined \(q_\alpha\), tests 250,000 indices for each of two transcendental parameters, the quadratic resonance and two parameters at or above one half, and compares observed frequencies with the generic formula. These finite tests are supplementary; the all-index statements are proved above by exact identities and equidistribution.

Run `python3 verify.py` with Python's standard library. Floating-point tests have no role in the proof and do not certify arbitrary real parameters.

## Relationship to prior work
Deane and Gentile, *A diluted version of the problem of the existence of the Hofstadter sequence* (first public preprint, 23 November 2023), define the recursion and establish existence for slow forcing. Their follow-up *Some subsets of set F in the diluted Hofstadter problem* (22 September 2025 preprint), Lemma 2.7, proves that the induced forcing is slow for \(1/2\le\alpha<1\). That theorem is explicitly excluded from the new contribution. The generic negative-step density below one half and the explicit silver-ratio exceptional parameter give complementary, quantitatively different behavior not found in the inspected cited theorems. No search establishes absolute priority.

## Limitations
The density formula requires rational independence of \(1,\alpha,\alpha^2\), and gives no classification of all rational and quadratic irrational exceptions. The exceptional slowness theorem does not assert a simple closed form for the forcing. No general stability or dynamical limit theorem is claimed for arbitrary inputs. Unindexed equivalent prior work remains possible. Independent validation has not been performed.

## References
- J. H. B. Deane and G. Gentile, *A diluted version of the problem of the existence of the Hofstadter sequence*, arXiv:2311.13854 (first posted 2023-11-23), https://arxiv.org/abs/2311.13854.
- J. H. B. Deane and G. Gentile, *Some subsets of set F in the diluted Hofstadter problem*, arXiv:2509.17764 (first posted 2025-09-22), https://arxiv.org/abs/2509.17764.
- H. Weyl, the classical multidimensional equidistribution criterion (used only in its standard irrational-linear-independence form).
