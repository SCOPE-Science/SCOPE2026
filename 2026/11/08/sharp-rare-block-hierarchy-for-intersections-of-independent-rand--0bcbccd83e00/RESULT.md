# Sharp rare-block hierarchy for intersections of independent random equivalence relations

## Finding
Let \(r\ge2\) be a fixed number of independently sampled, uniformly random equivalence relations on the labelled universe \([n]\), and let \(E_\cap\) be their intersection. Let \(L_n\) be the maximum size of a class of \(E_\cap\). For every fixed integer \(m\ge2\) with \(r(m-1)>m\),
\[
\Pr(L_n\ge m)\sim \binom{n}{m}\left(\frac{B_{n-m+1}}{B_n}\right)^r
\sim \frac{W(n)^{r(m-1)}}{m!\,n^{r(m-1)-m}},
\]
where \(B_n\) is the \(n\)-th Bell number and \(W(n)e^{W(n)}=n\). Conditioned on \(L_n\ge m\), the intersection relation has exactly one class of size \(m\) and no larger class, with probability tending to one. Conditional on this unique-class event, its \(m\)-element location is precisely uniform.

These probabilities are the satisfaction probabilities of the explicit first-order sentences
\[
\chi_{r,m}:=\exists x_1\cdots\exists x_m\left[\bigwedge_{i<j}x_i\ne x_j\ \wedge\ \bigwedge_{a=1}^{r}\bigwedge_{i<j} E_a(x_i,x_j)\right].
\]
The two first rare regimes are \(\Pr(\chi_{3,2})\sim W(n)^3/(2n)\) and \(\Pr(\chi_{2,3})\sim W(n)^4/(6n)\). The remaining fixed \(r,m\) satisfying the stated inequality form an entire hierarchy of smaller rare events. For \(r=m=2\) the event is not rare; this known case is not part of the new asymptotic assertion.

## Assumptions and scope
The random equivalence relations are mutually independent and each of the \(B_n\) partitions of \([n]=\{1,\ldots,n\}\) is equally likely. The intersection is defined by \(E_\cap(x,y)\iff\bigwedge_{a=1}^{r}E_a(x,y)\). Both \(r\) and \(m\) are fixed as \(n\) grows; \(m\le n\) once \(n\) is large. This is a model of labelled finite first-order structures, not a model of uniform isomorphism classes or arbitrary distributions on partitions.

## Proof
**1. Exact first moment.** For every \(m\)-subset \(S\subseteq[n]\), let \(I_S\) indicate that its members belong to a single class of \(E_\cap\). In one partition, requiring all of \(S\) to belong to a single block is equivalent to contracting the \(m\) elements into one, yielding exactly \(B_{n-m+1}\) eligible partitions. Independence across the \(r\) partitions gives
\[
\Pr(I_S=1)=\left(\frac{B_{n-m+1}}{B_n}\right)^r.
\]
Set \(X_m=\sum_{|S|=m} I_S\). Then \(\{L_n\ge m\}=\{X_m\ge1\}\), and
\[
\mu_{n,r,m}:=\mathbb E X_m=\binom{n}{m}\left(\frac{B_{n-m+1}}{B_n}\right)^r.
\]

**2. Exact second factorial moment.** For distinct \(m\)-subsets \(S,T\), write \(\ell=|S\cap T|\). If \(\ell=0\), one partition must identify the elements of \(S\) and, separately, of \(T\), leaving \(n-2m+2\) contracted points. If \(1\le\ell\le m-1\), their union of size \(2m-\ell\) must be a single block, leaving \(n-2m+\ell+1\) points. Thus, for all \(n\ge2m\),
\[
\mathbb E(X_m)_2=\binom{n}{m}\left[\binom{n-m}{m}\left(\frac{B_{n-2m+2}}{B_n}\right)^r+\sum_{\ell=1}^{m-1}\binom{m}{\ell}\binom{n-m}{m-\ell}\left(\frac{B_{n-2m+\ell+1}}{B_n}\right)^r\right].
\]
Here \((X_m)_2=X_m(X_m-1)\); terms with impossible disjointness are absent for smaller \(n\).

**3. Dominance of single witnesses.** For each fixed integer \(d\ge0\), the Bell-number asymptotic gives \(B_{n-d}/B_n\sim (W(n)/n)^d\). Hence
\[
\mu_{n,r,m}\sim\frac{W(n)^{r(m-1)}}{m!\,n^{r(m-1)-m}}\longrightarrow0
\]
under \(r(m-1)>m\). The disjoint term of the second moment, divided by \(\mu_{n,r,m}\), is \(O(\mu_{n,r,m})\). The \(\ell\)-overlap term for \(1\le\ell\le m-1\), after the same division, is
\[
O_{r,m}\left(\frac{W(n)^{r(m-\ell)}}{n^{(r-1)(m-\ell)}}\right)=o(1).
\]
Therefore \(\mathbb E(X_m)_2=o(\mu_{n,r,m})\). The first two Bonferroni inequalities yield
\[
\mu_{n,r,m}-\tfrac12\mathbb E(X_m)_2\le\Pr(X_m\ge1)\le\mu_{n,r,m},
\]
proving the probability asymptotics. Also \(\Pr(X_m\ge2)\le\tfrac12\mathbb E(X_m)_2=o(\mu_{n,r,m})\), so a rare occurrence has only one \(m\)-subset witness with conditional probability tending to one.

**4. Exact exceptional shape.** The event that a class has size at least \(m+1\) is bounded above by \(\mathbb E X_{m+1}\). Applying the same contraction and Bell-ratio estimate gives
\[
\frac{\mathbb E X_{m+1}}{\mu_{n,r,m}}\sim\frac{W(n)^r}{(m+1)n^{r-1}}\longrightarrow0.
\]
Together with the previous step, this proves that the exceptional intersection relation has a unique class of exactly \(m\) points and all other classes smaller than \(m\), with conditional probability tending to one. Since the model is invariant under all permutations of \([n]\), the location of this unique class is exactly uniform among \(m\)-subsets on the event of the asserted shape.

## Verification
The standalone `checker.py` directly generates all set partitions on universes of size three through five and enumerates ordered pairs and triples of partitions. For every displayed test, it counts the occurrence event, the exact first moment, and the exact second factorial moment. It independently compares the latter two counts to the contraction formulas and verifies the Bonferroni bounds using exact rational arithmetic. Running `python checker.py` prints `ALL_FINITE_CHECKS_OK`. This checks the finite identities on those instances, not the infinite asymptotic argument. The latter uses the standard fixed-shift Bell-ratio theorem and the explicit proof above.

## Relationship to prior work
Pittel (2000) proves that the intersection of two independent uniform partitions is nontrivial with probability tending to one, whereas for at least three partitions its intersection is trivial with probability tending to one; he proves that for two partitions a block of size three or larger is unlikely, and gives the large-parameter Poisson law for blocks of size two. These qualitative and Poisson claims are not presented as new here. The present hierarchy resolves the *relative rare-event asymptotics*, including their leading constants, for every fixed exceptional block size, and identifies the conditional unique-witness shape. In particular, the published \(o(1)\) statement about blocks of size at least three is refined to a relative asymptotic.

Canfield (2001) gives exact global enumeration formulas for tuples of partitions with a prescribed meet condition. Those identities cover exact finite counting of intersection shapes and constitute important stronger background coverage; they do not explicitly give the fixed-arity rare-block asymptotics or conditional unique-block law derived here. The issue of whether a broader already-published asymptotic theorem implicitly subsumes this formulation remains a historical-priority risk, not resolved by title searches alone.

Koponen (2026) studies finite structures, their limit theories, and prospects for first-order convergence under random expansions. This motivates investigating quantitative logical satisfaction probabilities of finite structures bearing multiple equivalence relations, but its principal theorem is not invoked in the proof.

## Limitations
The conclusions are limited to fixed integers \(r,m\) with \(r(m-1)>m\), and to independent uniform labelled partitions. They assert neither uniformity for increasing \(r,m\), nor a full first-order convergence theorem for all formulas in the multiple-equivalence vocabulary. The classification of other larger classes on the rare event is restricted to showing that no other class reaches size \(m\); smaller classes may remain numerous. Historical priority remains an open caveat because general partition enumeration and asymptotic tools could yield this hierarchy indirectly.

## References
1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first public October 12, 2026), sections 1--2, in particular the random-expansion discussion.
2. B. Pittel, *Where the Typical Set Partitions Meet and Join*, Electronic Journal of Combinatorics 7 (2000), R5, DOI:10.37236/1483, especially Theorems 3--4 and the asymptotic Bell-ratio discussion.
3. E. R. Canfield, *Meet and Join within the Lattice of Set Partitions*, Electronic Journal of Combinatorics 8 (2001), R15, DOI:10.37236/1559, especially Theorem 1 and the meet-count identity.
4. L. Moser and M. Wyman, *An asymptotic formula for the Bell numbers*, Transactions of the Royal Society of Canada 49 (1955), 49--54, used for fixed-shift Bell-ratio asymptotics.
