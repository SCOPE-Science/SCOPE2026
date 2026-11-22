# A sharp single crossing of cherry–distance-shell covariances in uniform Cayley trees

## Finding
Let \(T_n\) be uniform among the \(n^{n-2}\) unrooted trees labelled by \([n]\), with \(n\ge4\). Let \(C_n\) count **unordered pairs of degree-one vertices with the same neighbor**, with a center incident to \(r\) leaves contributing \(\binom r2\). For \(1\le k<n\), let \(M_{n,k}\) count unordered pairs of vertices at graph distance \(k\). Write
\[
 p_{m,k}=\begin{cases}
 (k+1)(m-2)_{\underline{k-1}}/m^k,&1\le k<m,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad c_n=\binom n2\frac{(n-2)^{n-3}}{n^{n-2}}.
\]
A falling factorial of length zero is one. Then \(\mathbb E C_n=c_n\), \(\mathbb E M_{n,k}=\binom n2p_{n,k}\), and \(\operatorname{Cov}(C_n,M_{n,1})=0\). For all \(2\le k<n\),
\[
 \boxed{\operatorname{Cov}(C_n,M_{n,k})=c_n\Delta_{n,k},\quad
 \Delta_{n,k}=\binom{n-2}{2}p_{n-2,k}+2(n-3)p_{n-2,k-1}
 +\mathbf1_{\{k=2\}}-\binom n2p_{n,k}.}
\]
The sequence \(\Delta_{n,2},\dots,\Delta_{n,n-1}\) begins strictly positive, ends strictly negative and has **exactly one positive-to-negative transition**, with at most one zero integer shell between the two signs. If \(k_n^-\) is the first strictly negative shell, then
\[
 \boxed{\lim_{n\to\infty}\frac{k_n^-}{\sqrt n}=\sqrt2.}
\]
For every nondecreasing function \(f:\{1,\dots,n-1\}\to\mathbb R\),
\[
 \operatorname{Cov}\!\left(C_n,\sum_{u<v}f(d_{T_n}(u,v))\right)\le0,
\]
with strict inequality for strictly increasing \(f\). In particular this **recovers** the already known strict negative cherry–Wiener-index covariance; its previously published exact scalar formula and asymptotic are not new claims here. The new result is the full shell-resolved mixed moment, single-crossing classification, sharp crossover scale and the corresponding inequality for all monotone distance costs.

## Assumptions and scope
Trees are unrooted, uniformly vertex-labelled, simple and unweighted, not plane, recursive, or uniformly binary phylogenetic trees. The center of a cherry is not constrained to degree three. All finite formulas and signs hold for integer \(n\ge4\), and the limit is on the \(\sqrt n\) scale. An integer shell of exactly zero covariance is possible. No full joint distribution, central limit law or assertion for other tree models is made.

## Proof
**1. Fixed-path enumeration.** Fix distinct vertices \(u,v\). A path of length \(k\) with these endpoints has \((n-2)_{\underline{k-1}}\) ordered choices of internal vertices. For a fixed path of \(k+1\) vertices, the Cayley forest-extension formula gives \((k+1)n^{n-k-2}\) trees containing that path: contract its component, assign one of its \(k+1\) vertices as attachment site for each external connection, and apply the weighted matrix-tree formula. The formula remains correct when \(k=n-1\), because the path spans the vertex set and has one completion. Division by \(n^{n-2}\) yields \(p_{n,k}\) and \(\mathbb EM_{n,k}=\binom n2p_{n,k}\).

**2. Marked-cherry size bias and exact shells.** Mark an unordered leaf pair \(\{a,b\}\) and its common neighbor \(c\). Deleting \(a,b\) is a bijection to a tree on \([n]\setminus\{a,b\}\) and a marked center \(c\) among its \(n-2\) vertices. The number of marked triples-with-trees is \(\binom n2(n-2)(n-2)^{n-4}=\binom n2(n-2)^{n-3}\), so the expected number of cherries is \(c_n\). Under size bias by \(C_n\), the residual \((n-2)\)-vertex tree is uniform and the attachment center is uniformly marked.

Old–old pairs at distance \(k\) have expected count \(\binom{n-2}2p_{n-2,k}\). For each of the two new leaves, old vertices other than the attachment center contribute \((n-3)p_{n-2,k-1}\) expected pairs at distance \(k\ge2\); the two new leaves contribute one pair at distance two. Thus the conditional shell mean for \(k\ge2\) is
\[
 \mu_{n,k}=\binom{n-2}{2}p_{n-2,k}+2(n-3)p_{n-2,k-1}
 +\mathbf1_{\{k=2\}}.
\]
Because \(C_n\)-size bias satisfies \(\mathbb E[C_nM_{n,k}]=c_n\mathbb E^*[M_{n,k}]\), the displayed covariance identity follows. For \(k=1\), \(M_{n,1}=n-1\) deterministically, giving covariance zero.

**3. One sign transition at every order.** At the first nontrivial shell,
\[
 \Delta_{n,2}=\frac{2(n-3)(n-1)}{n(n-2)}>0.
\]
At the terminal shell \(k=n-1\), a tree with a marked cherry cannot be a spanning path, so \(\Delta_{n,n-1}=-\binom n2p_{n,n-1}<0\). For integers \(3\le k\le n-2\), direct cancellation of the positive falling-factorial factors shows \(\operatorname{sgn}\Delta_{n,k}=\operatorname{sgn}(H_n(k)-1)\), where
\[
 H_n(x)=\frac{(n-x-1)\left(n-x+2-\frac4{x+1}\right)}
 {n(n-1)\left(\frac{n-2}{n}\right)^x},\qquad 3\le x\le n-2.
\]
For \(n\ge8\), both numerator factors are positive on the displayed interval. The functions \(\log(n-x-1)\) and \(\log(n-x+2-4/(x+1))\) are strictly concave there: the former is elementary, and the latter follows because its positive argument has second derivative \(-8/(x+1)^3<0\). Subtracting the logarithm of the denominator changes the sum by an affine function of \(x\), hence \(\log H_n\) remains strictly concave. Directly,
\[
 H_n(3)-1=\frac{n^2-8n+4}{(n-2)^2(n-1)}>0\quad(n\ge8).
\]
At \(x=n-2\), the numerator is less than four and the denominator exceeds four, since \(((n-2)/n)^{n-2}\ge e^{-2}\) and \(n(n-1)e^{-2}>4\) for \(n\ge8\). Consequently \(H_n(n-2)<1\). The superlevel set \(\{x:H_n(x)\ge1\}\) is an interval by log-concavity, starts above one and ends below it; hence the integer shells have exactly one positive-to-negative transition and at most one zero. Direct exact evaluation of the displayed \(\Delta_{n,k}\) gives positive \(k=2\) and negative \(k=3,\ldots,n-1\) for \(n=4,5,6,7\), covering the smaller cases.

For each fixed \(t>0\), expanding the two numerator factors and the logarithm of the denominator at \(x=t\sqrt n\) gives
\[
 H_n(t\sqrt n)=1+\frac{2-t^2}{n}+o(n^{-1}).
\]
Applying this at every fixed \(t<\sqrt2\) and \(t>\sqrt2\), then using the single-crossing theorem, proves \(k_n^-/\sqrt n\to\sqrt2\). Integer rounding changes \(x\) by at most one and does not change this conclusion.

**4. All monotone pairwise-distance costs.** Every tree has \(\binom n2\) unordered pairs, so \(\sum_{k=1}^{n-1}\Delta_{n,k}=0\). The one-sign transition and positive second shell imply all proper partial sums \(S_j=\sum_{k\le j}\Delta_{n,k}\) are nonnegative, and some are strictly positive. Discrete summation by parts yields
\[
 \sum_{k=1}^{n-1}f(k)\Delta_{n,k}
 =-\sum_{j=1}^{n-2}(f(j+1)-f(j))S_j\le0.
\]
If \(f\) is strictly increasing, the positive partial sum after the second shell makes the inequality strict. Choosing \(f(k)=k\) recovers the known cherry–Wiener negativity, but its prior scalar exact formula and leading asymptotic are credited below rather than claimed anew.

## Reproducibility and proof limits
The existing `check_cherry_distance.py` independently reconstructs all labeled trees from Prüfer words for \(n=4,5,6,7\), directly measures cherries and distance shells, and checks the exact covariance by rational arithmetic; it also checks shell signs and summation identities through \(n=200\). Its finite computations corroborate, rather than prove, the all-order log-concavity and asymptotic steps. The tree conventions and identities in the script are unchanged.

## Relationship to earlier results and exact scope of novelty
A published October 13, 2026 theorem, *Exact negative cherry–Wiener covariance in uniform Cayley trees* (https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-exact-negative-cherry-wiener-covariance-in-uniform-cayley-trees--50ec71e1b4aa/RESULT.md), **already proves** for the same unrooted labeled model and exactly the same cherry statistic that \(\operatorname{Cov}(C_n,\operatorname{Wie}(T_n))<0\) for \(n\ge4\), gives its exact finite formula, and derives the asymptotic \(-e^{-2}\sqrt{\pi/2}\,n^{5/2}/4\). Those statements, the marked-cherry deletion method and the fixed-path enumeration are prior mathematical inputs, not fresh discoveries here. That theorem computes the conditional **total** Wiener sum, which is the distance-weighted sum of shell means; that scalar alone does not determine the entire sequence of shell covariances, the single sign transition or its sharp \(\sqrt{2n}\) location. The present claim is the latter shell-resolved refinement and its general monotone-functional inequality.

Erdős and Rényi, *Asymmetric graphs* (1963), Section 5, Theorem 6, define exactly this broad cherry event and count its occurrence and moments, but not covariance with the full distance profile. Berzunza Ojeda and Janson, *The distance profile of rooted and unrooted simply generated trees* (2022), Sections 8 and 13, give leaf marking and distance-profile/Wiener scaling limits for much broader tree laws, but do not state the cherry-marked finite shell formula or its sign crossing. Related conditional marked-path leaf laws use different markings and do not imply the cherry-marked shell result. These are statement-level distinctions, not claims of exhaustive priority; specialized older enumerators may encode the same mixed law implicitly.

## References
- P. Erdős and A. Rényi, *Asymmetric graphs*, Acta Math. Acad. Sci. Hungar. 14 (1963), 295–315, Sections 5, Theorem 6. https://users.renyi.hu/~p_erdos/1963-04.pdf.
- *Exact negative cherry–Wiener covariance in uniform Cayley trees* (published October 13, 2026), https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-exact-negative-cherry-wiener-covariance-in-uniform-cayley-trees--50ec71e1b4aa/RESULT.md.
- G. Berzunza Ojeda and S. Janson, *The distance profile of rooted and unrooted simply generated trees*, Combin. Probab. Comput. 31 (2022), 368–410, https://doi.org/10.1017/S0963548321000304.
- S. Janson, *The Wiener Index of simply generated random trees*, Random Struct. Algorithms 22 (2003), 337–358, https://doi.org/10.1002/rsa.10074.
