# A quadratic cyclic-core regression for origins in a uniform random mapping

## Finding
Let \(f:[n]\to[n]\) be uniformly random (all \(n^n\) maps equally likely), let \(C_n\) be the number of vertices on directed cycles of \(f\), and let \(L_n\) be the number of vertices of indegree zero. For \(n\ge2\), and \(1\le m<n\), write \(t=n-m\). The conditional factorial moments, for every integer \(0\le r\le t\), are
\[
\mathbb E[(L_n)_r\mid C_n=m]=(t)_r(1-r/n)^{t-1}.
\]
For \(m=n\), the conditional leaf count is zero. In particular, with \(g_n(m)=\mathbb E[L_n\mid C_n=m]\),
\[
g_n(m)=(n-m)(1-1/n)^{n-m-1},\qquad
 g_n(m)-g_n(m+1)=\frac mn(1-1/n)^{n-m-2}>0
\]
for \(1\le m<n\), where \(g_n(n)=0\). The strict decreasing regression is not approximately linear on the natural \(\sqrt n\) scale: for every deterministic integer sequence \(1\le m_n\le n\) with \(m_n/\sqrt n\to z\ge0\),
\[
 g_n(m_n)-n/e\longrightarrow (1-z^2)/(2e).
\]
Its exact cross-covariance is
\[
\operatorname{Cov}(C_n,L_n)=n(1-1/n)^n\bigl(\mathbb E C_{n-1}-\mathbb E C_n\bigr)<0
\]
and its sharp scale is
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(C_n,L_n)}{\sqrt n}=-\frac{1}{e}\sqrt{\frac\pi8}.
\]
These formulas describe the dependence of the cyclic core on origin production in the standard functional-digraph model, rather than a new model of mappings.

## Assumptions and scope
The integer \(n\ge2\), map values \(f(1),\ldots,f(n)\) are independent uniforms on \([n]=\{1,\ldots,n\}\); loops and cycles of every length are permitted. A vertex of indegree zero is an *origin*, or an off-cycle leaf. All cyclic vertices have indegree at least one. The descending factorial is \((u)_r=u(u-1)\cdots(u-r+1)\), with \((u)_0=1\). Only the deterministic-sequence quadratic limit and the covariance asymptotic take \(n\to\infty\). No joint normal limit or independence claim is made.

## Proof
**Conditional forest enumeration.** Given that the cyclic vertex set is a fixed \(m\)-element set \(R\) and the cyclic arcs form any fixed permutation of \(R\), the other \(t=n-m\) vertices form a uniformly chosen directed forest pointing toward the roots \(R\). For \(m<n\), repeatedly delete the smallest nonroot vertex which has no children, recording its parent, until just one nonroot remains. This is a bijection from such rooted forests to arbitrary sequences of \(t-1\) labels in \([n]\), followed by a root label in \(R\). For the inverse, at each step delete the smallest remaining nonroot absent from the remaining parent sequence and attach it to the first recorded parent; attach the final nonroot to the chosen root. The root label is independent of the uniform prefix. A nonroot is indegree zero precisely if its label never appears in the \(t-1\) prefix. Thus the conditional origin count is the number of empty boxes in a designated set of \(t\) boxes when \(t-1\) independent draws are uniformly distributed among \(n\) boxes. The factorial-moment formula follows by choosing ordered distinct designated boxes and avoiding their labels.

For completeness, inclusion–exclusion yields the entire finite joint law: for \(m<n\), \(0\le\ell\le t\),
\[
\Pr(C_n=m,L_n=\ell)=\frac{(n)_m m}{n^n}\binom t\ell
 \sum_{j=0}^{t-\ell}(-1)^j\binom{t-\ell}j(n-\ell-j)^{t-1}.
\]
For \(m=n\), \(\Pr(C_n=n,L_n=0)=n!/n^n\). Indeed there are \(\binom nm m!\) choices of the cyclic subset and cyclic permutation, and exactly \(m n^{n-m-1}\) forests for each fixed cyclic set. Hence
\[
\Pr(C_n=m)=\frac{m(n)_m}{n^{m+1}},\qquad
\Pr(C_n\ge m)=\frac{(n)_m}{n^m}\quad(1\le m\le n).
\]

**Strict regression.** Set \(a=1-1/n\). The conditional first moment is \(g_n(m)=(n-m)a^{n-m-1}\). Subtracting successive values gives the displayed positive difference, including \(m=n-1\) by \(a^{-1}=n/(n-1)\). In particular, increasing the number of cyclic points strictly lowers the expected number of origins at every finite size.

**Quadratic Rayleigh-window profile.** If \(m_n=O(\sqrt n)\), write \(u=m_n/n\); Taylor expansion uniformly for bounded \(m_n/\sqrt n\) gives
\[
\log\frac{g_n(m_n)}{n/e}=\log(1-u)+1+(n-m_n-1)\log(1-1/n)
=\frac{1}{2n}-\frac{m_n^2}{2n^2}+o(1/n).
\]
Exponentiating and multiplying by \(n/e\) proves the claimed limit. The same limit for \(z=0\) includes any \(m_n=o(\sqrt n)\) with \(m_n\ge1\).

**Exact negative covariance.** Let \(O_v\) denote the indicator that vertex \(v\) has no incoming arcs. Then \(\Pr(O_v=1)=a^n\). Conditional on \(O_v=1\), every map value lies in \([n]\setminus\{v\}\); the restrictions of \(f\) to these \(n-1\) vertices form an independent uniformly random mapping of \(n-1\) points. Vertex \(v\) is not cyclic, and its outgoing arc cannot create a directed cycle through it. Therefore \(\mathbb E[C_n\mid O_v=1]=\mathbb E C_{n-1}\). Summing \(\mathbb E[C_nO_v]\) over vertices and subtracting \(\mathbb E C_n\mathbb E L_n\) proves the exact covariance identity. Its sign is strictly negative because the survival tails above imply the cyclic count is strictly stochastically increasing with the size of the mapping; more explicitly \(\Pr(C_n\ge m)=\prod_{j=0}^{m-1}(1-j/n)\) is strictly increasing in \(n\) for \(m\ge2\).

**Asymptotic covariance constant.** The survival formula gives
\[
\Pr(C_n/\sqrt n>x)\to e^{-x^2/2}\quad(x\ge0),
\]
so \(C_n/\sqrt n\) converges to a Rayleigh random variable \(R\) with density \(re^{-r^2/2}\). The product survival bound \(\Pr(C_n\ge m)\le\exp[-m(m-1)/(2n)]\) gives uniformly bounded moments of every fixed order of \(C_n/\sqrt n\). Moreover, the telescoping strict-regression formula and \(a^{n-m-2}\le a^{-1}\le2\) show \(|g_n(m)-n/e|\le K+m^2/n\) for some absolute \(K\), uniformly in \(n\ge2\), \(1\le m\le n\). Therefore the fixed-sequence quadratic limit and these moment bounds yield, by truncation and uniform integrability,
\[
\frac{\operatorname{Cov}(C_n,L_n)}{\sqrt n}
=\operatorname{Cov}\bigl(C_n/\sqrt n,g_n(C_n)-n/e\bigr)
\longrightarrow -\frac{1}{2e}\operatorname{Cov}(R,R^2).
\]
The Rayleigh moments \(\mathbb E R=\sqrt{\pi/2}\), \(\mathbb E R^2=2\), and \(\mathbb E R^3=3\sqrt{\pi/2}\) give \(\operatorname{Cov}(R,R^2)=\sqrt{\pi/2}\), yielding \(-\sqrt{\pi/8}/e\).

## Verification
The accompanying standalone `verify.py` enumerates every mapping for \(1\le n\le6\), independently counts cyclic points and zero-indegree vertices, and checks all joint frequencies against the inclusion–exclusion formula. It also checks conditional factorial moments, conditional means, the exact covariance identity, and strict negativity, using exact rational arithmetic. It performs 200 assertions/comparisons and passes with Python 3 and no third-party packages. Enumeration is finite corroboration and cannot certify identities for all \(n\); those follow from the explicit coding and analytical proof above. Run `python3 verify.py` in a directory containing this file and the script.

## Relationship to prior work
The cyclic-set/rooted-forest decomposition and Prüfer coding are classical and are not claimed as new. Arney and Bender (1982) studied origins and cyclic statistics under degree and origin constraints, including bivariate generating-function tools; Soria (November 10, 1996) supplied generating functions for leaf statistics in random mappings. Hansen and Jaworski (2006, 2010) treated cyclic-point counts and random mappings constructed from uniform rooted forests. Those results supply the foundational model and make the conditional occupancy representation accessible. The narrower proposed contribution is the explicit *finite-size strictly decreasing conditional origin regression*, its nontrivial order-one quadratic profile on the natural Rayleigh window, and the exact negative cross-covariance with a sharp \(\sqrt n\) coefficient. These statements are not directly reported in the inspected passages; this is not a guarantee that older general generating functions could not imply them upon additional extraction.

## Limitations
Historical priority, especially implicit coverage by multivariate random-mapping generating functions, remains uncertain. The 1997 paper by Drmota and Soria on images and preimages could not be inspected in full through available access; it may contain relevant multivariate results. The statement concerns uniform independent random functions, not mappings with constrained indegrees, other functional graph ensembles, or a joint central limit theorem for the unnormalized statistics. Independent external verification has not been performed.

## References
- James Arney and Edward A. Bender, *Random mappings with constraints on coalescence and number of origins*, Pacific Journal of Mathematics 103 (1982), 269–297. https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-p.pdf
- Michèle Soria, *Distribution of Image Points in Random Mappings*, Algorithms Seminar, November 10, 1996. https://algo.inria.fr/seminars/sem96-97/soria.html
- Jennie C. Hansen and Jerzy Jaworski, *A New Random Mapping Model*, arXiv:math/0603529, first posted March 22, 2006. https://arxiv.org/abs/math/0603529
- Jennie C. Hansen and Jerzy Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/
- Michael Drmota and Michèle Soria, *Images and Preimages in Random Mappings*, SIAM Journal on Discrete Mathematics 10 (1997), 246–269, doi:10.1137/S0895480194268421 (historical risk; full text not reviewed).
