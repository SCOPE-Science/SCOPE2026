# Terminal anchored-component moments and a marked Poisson–Borel uncovering process

## Finding

Let \(T_n\) be uniform among the \(n^{n-2}\) labeled trees on \([n]\). Fix \(D\geq1\), set \(B=[n-D]\), and designate the terminal vertices \(h_j=n-j+1\), \(1\leq j\leq D\). A *pendant branch anchored at* \(h_j\) is a nonempty \(S\subseteq B\) for which the induced subgraph \(T_n[S]\) is connected and exactly one edge of \(T_n\) joins \(S\) to its complement, with other endpoint \(h_j\). Let \(Y_{n,j,r}\) count such branches of size \(r\).

For arbitrary finitely supported nonnegative multiplicities \(m_{j,r}\), write \(R=\sum_{j,r}r m_{j,r}\) and \(M=\sum_{j,r}m_{j,r}\). The exact joint factorial-moment identity is

\[
\boxed{\mathbb E\prod_{j,r}(Y_{n,j,r})_{\underline{m_{j,r}}}
=\frac{(n-D)_{\underline R}\,\tau(n-R)}{n^{n-2}}\prod_{j,r}\left(\frac{r^{r-1}}{r!}\right)^{m_{j,r}}.}
\]

Here \(\tau(s)=s^{s-2}\) for \(s\geq2\), \(\tau(1)=1\), and the right side is zero for \(R>n-D\); all factorials and falling factorials have their usual integer definitions. For any fixed \(D\) and any finite collection of branch sizes, these counts jointly converge to **independent** Poisson variables with means

\[
\lambda_r=\frac{r^{r-1}e^{-r}}{r!},\qquad \sum_{r\geq1}\lambda_r=1.
\]

For \(1\leq d\leq D\), let \(\mathcal F_{n,d}\) be the multiset of vertex counts of **all** components of \(T_n[[n-d]]\) except the one containing vertex \(1\). Then the entire finite sequence converges jointly:

\[
\boxed{(\mathcal F_{n,1},\ldots,\mathcal F_{n,D})\ \xrightarrow{d}\
(\mathcal P_1,\mathcal P_1\uplus\mathcal P_2,\ldots,
\mathcal P_1\uplus\cdots\uplus\mathcal P_D).}
\]

The \(\mathcal P_j\) are independent finite random multisets consisting of a Poisson\((1)\) number of iid Borel\((1)\) marks, with \(\Pr(B=r)=\lambda_r\). Equivalently, the multiplicities of mark size \(r\) in each \(\mathcal P_j\) are independent Poisson\((\lambda_r)\). In particular the terminal nonroot cluster count and mass have joint **independent increments** across the finitely many reverse uncover times.

## Assumptions and scope

All trees are unrooted, simple, and uniformly sampled from the labeled Cayley model; vertex \(1\) is distinguished solely to select a unique giant component. \(D\) is fixed as \(n\to\infty\); finite factorial moments require \(n>D\). For the terminal forest, \(d\) always denotes exactly the last \(d\) vertices \(\{n-d+1,\ldots,n\}\) withheld, not independently sampled vertex deletions. Convergence of finite multisets is in the discrete topology on finite integer multisets; it implies joint convergence of their total counts and their finite total masses.

## Proof

**Exact enumeration.** Suppose a particular ordered collection of \(M\) disjoint pendant branch vertex sets \(S_{j,r,a}\subseteq B\), of prescribed sizes, is selected. Its cardinality assignments number \((n-D)_{\underline R}/\prod_{j,r}(r!)^{m_{j,r}}\). Each set admits exactly \(r^{r-1}\) rooted labeled trees: choose a Cayley tree on its \(r\) vertices and choose the endpoint of its unique edge to \(h_j\). The remaining \(n-R\) vertices (including every \(h_j\)) support \(\tau(n-R)\) arbitrary labeled trees. Connecting every selected rooted branch to its designated anchor produces exactly one complete tree and exhausts the prescribed event. Conversely, distinct such branches in a tree cannot overlap or contain one another: either possibility contradicts their unique boundary-edge condition and connectedness. Division by \(n^{n-2}\) gives the boxed exact identity, with no independence assumption.

**Poisson mark convergence.** For fixed \(D\) and fixed integer array \(m_{j,r}\),

\[
\frac{(n-D)_{\underline R}\tau(n-R)}{n^{n-2}}\longrightarrow e^{-R}.
\]

All finite joint factorial moments therefore tend to those of independent Poisson variables of means \(\lambda_r\). The multivariate probability-generating-function/moment method for nonnegative integer vectors yields the asserted finite-dimensional convergence. The tree function identity \(\sum_{r\geq1}r^{r-1}(e^{-1})^r/r!=1\) follows by taking the nonnegative solution of \(u=e^{u-1}\) reached from the power series below its radius of convergence; the coefficients form the total-progeny distribution of a critical Poisson\((1)\) Galton–Watson branching process, so the limiting Poisson mark process is almost surely finite and has finite total mass.

**Tight root deficit.** Let \(Z_{n,d}=(n-d)-|C_{n,d}(1)|\), with \(C_{n,d}(1)\) the component of vertex \(1\) in \(T_n[[n-d]]\). Exact Cayley decomposition, equivalently Theorem 9 of Hackl–Panholzer–Wagner (2023), gives for \(0\leq q\leq n-d-1\):

\[
\Pr(Z_{n,d}=q)=\binom{n-d-1}{q}
\frac{d\,(n-d-q)^{n-d-q-1}(d+q)^{q-1}}{n^{n-d-1}}.
\]

For \(q=0\), the factor \(d(d+q)^{q-1}\) equals \(1\). Fixing \(d,q\) and taking \(n\to\infty\) gives \(e^{-d-q}d(d+q)^{q-1}/q!\). The probability mass function is proper because its generating function is \(\exp\{d(T(z/e)-1)\}\), where \(T(w)=\sum_{r\geq1}r^{r-1}w^r/r!\). Consequently the finite family \((Z_{n,d})_{1\leq d\leq D}\) is tight; this also recovers, but does not claim novelty for, the published fixed-\(d\) marginal compound-Poisson limit.

**Separation of hidden anchors.** For specified distinct vertices, Cayley's forest-extension count gives the exact distance law

\[
\Pr(\mathrm{dist}_{T_n}(u,v)=\ell)
=\frac{(n-2)_{\underline{\ell-1}}(\ell+1)}{n^{\ell}}
\leq\frac{\ell+1}{n}, \quad 1\leq\ell\leq n-1.
\]

Indeed a chosen simple length-\(\ell\) path has \(\ell+1\) vertices; its chance of occurring is \((\ell+1)/n^{\ell}\), and there are \((n-2)_{\underline{\ell-1}}\) ordered possible internal vertex lists. Thus any two of the fixed \(D\) hubs are asymptotically farther apart than every fixed \(K\), by the union bound.

**Identification across reverse times.** Fix \(K\) and work on the event that every terminal root deficit is at most \(K\), and every pair of designated hubs has distance exceeding \(K+1\). Each nonroot component after deleting \(h_1,\ldots,h_d\) has at most \(K\) vertices. It contains no designated hub of higher index (otherwise its path to any deleted hub, which must exist because the full tree is connected, gives a short hub-to-hub path). Its one or more external edges in the original tree necessarily end at deleted hubs. There can be only one such edge, since two distinct outside anchors, or two outside edges at one anchor, create a cycle or a path contradicting the prescribed component's maximal connectedness. Thus it is a globally anchored branch counted by precisely one \(Y_{n,j,r}\), \(j\leq d\). Conversely, every anchored branch of size at most \(K\), with \(j\leq d\), is a component of the corresponding forest, and for \(n>2K+D\) cannot contain vertex \(1\) on this event. Consequently the entire sequence of truncated component multisets agrees with the partial-union sequence of counted anchored marks on this event. First let \(n\to\infty\), then \(K\to\infty\): root-deficit tightness, hub separation, and summability of \(\lambda_r\) remove the truncation and establish the joint multiset convergence.

## Verification

The standalone `check.py` enumerates every Prüfer code for all sizes \(3\leq n\leq7\), reconstructs the corresponding labeled tree, and independently checks mixed factorial moments of pendant anchored components, the exact root-deficit probability mass function, and the marked-hub distance distribution using `fractions.Fraction` arithmetic. It reports 101 exact comparisons passed. This finite test corroborates the algebra but is not the proof of the all-order factorial formula or the infinite convergence theorem.

## Relationship to prior work

The process and the underlying fixed-time component enumeration are due to Hackl, Panholzer and Wagner (2022, 2023). Their 2023 Lemma 8 enumerates arbitrary disjoint components of a **single** uncovered forest; in particular its specialization to exactly one hidden vertex already implies the \(D=1\) case of the factorial-moment identity above. Theorem 9 gives the fixed-\(d\) one-dimensional root-deficit compound-Poisson law, and Theorem 10 gives an expected component count. These results supply important nearby components and already determine the terminal one-time marginal. The contribution here, beyond the known single-anchor specialization, is the exact **multi-anchor (\(D\) at least two) and all-order mark-resolved factorial-moment identity** together with a precise **finite-sequence** temporal joint limit of offroot component-size multisets. The earlier single-time counts cover one anchor but do not state distinct-anchor mixed factorial moments or temporal independent increments; the new enumeration supplies those with a direct proof. Stufler (2016) proves general rerooted conditioned-Galton–Watson local limits, which plausibly imply much of the unmarked asymptotic local behavior, but do not give the exact finite-size multivariate factorial identity. Berzunza Ojeda and Holmgren (2020) prove a continuum limit under **edge deletion** and rescaling, not the present bounded-vertex terminal process. Pitman (2001), especially Theorems 12–13 and Proposition 15, gives exact fringe-subtree and multirooted-forest component-set laws derived from Cayley–Hurwitz identities. These provide especially close general enumeration principles; the prescribed terminal-hub multi-moment formula may be derivable from them by additional decompositions, but their statements do not identify the present exact anchored observable or its joint reverse-uncovering marked limit.

## Limitations

This is not a functional limit when the number of hidden vertices grows with \(n\), does not give convergence rates, and does not establish joint behavior in critical windows. The fixed-\(d\) compound-Poisson marginal is known and not presented as new. General local weak-limit results may imply some asymptotic consequences by another route; older Cayley–Hurwitz fringe-forest identities may imply the exact moment formula by a not-yet-explicit reduction. Historical priority requires specialist comparison, and the elementary enumeration is not presented as a new general Cayley principle. No independent mathematical audit has been performed.

## References

- B. Hackl, A. Panholzer and S. Wagner, *Uncovering a Random Tree*, AofA 2022, DOI `10.4230/LIPIcs.AofA.2022.10`, first public 2022-06-08. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.AofA.2022.10
- B. Hackl, A. Panholzer and S. Wagner, *The Uncover Process for Random Labeled Trees*, La Matematica 2 (2023), 861–892, DOI `10.1007/s44007-023-00060-3`. https://link.springer.com/article/10.1007/s44007-023-00060-3
- B. Stufler, *Local limits of large Galton–Watson trees rerooted at a random vertex*, arXiv:1611.01048 (2016). https://arxiv.org/abs/1611.01048
- G. Berzunza Ojeda and C. Holmgren, *Invariance principle for fragmentation processes derived from conditioned stable Galton–Watson trees*, arXiv:2010.07880 (2020). https://arxiv.org/abs/2010.07880
- J. Pitman, *Random mappings, forests, and subsets associated with Abel–Cayley–Hurwitz multinomial expansions*, Séminaire Lotharingien de Combinatoire 46 (2001), Article B46h, Sections 5.2–5.3. https://www.mat.univie.ac.at/~slc/s/s46pitman.pdf
