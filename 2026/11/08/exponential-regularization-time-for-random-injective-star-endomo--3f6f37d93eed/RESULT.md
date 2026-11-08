# Exponential regularization time for random injective star endomorphisms

## Finding

For each integer \(n\ge2\), write \(S_n\) for the simple undirected star with vertex set \(\{0,1,\ldots,n-1\}\), center \(0\), and edges \(\{0,i\}\) for \(1\le i<n\). Let \(M_n=\operatorname{IEnd}(S_n)\) be the monoid of all injective partial graph endomorphisms under composition. Select \(F_n\) uniformly from \(M_n\). An element \(f\) of a monoid is *regular* if there exists an element \(g\) of that monoid with \(fgf=f\). Define its positive-power regularization time by
\[
 T_n=\min\{t\ge1:F_n^t\text{ is regular in }M_n\}.
\]
Then the minimum is finite, and
\[
 \boxed{\lim_{n\to\infty}\Pr\!\left(T_n>x\sqrt{n-1}\right)=e^{-x}\quad\text{for every real }x\ge0.}
\]
Equivalently, \(T_n/\sqrt{n-1}\) converges in distribution to the exponential random variable of mean one. Thus the typical number of powers required before regularity has order \(\sqrt n\), with nonconcentrated fluctuations.

The theorem also supplies the **complete exact finite-size survival function**. Put \(m=n-1\), and for integers \(0\le k\le m\) and \(1\le t\le m\) define
\[
 a_{m,k}=\binom mk\frac{(m+1)!}{(m+1-k)!},\quad
 p_{m,k}(t)=\begin{cases}\displaystyle\frac{k}{m+1}\prod_{i=1}^{t-1}\frac{k-i}{m+1-i},&k\ge t,\\0,&k<t,\end{cases}
\]
and
\[
 N_m=\sum_{k=0}^m a_{m,k}+\sum_{k=0}^m\binom mk^2 k!+m(m+1).
\]
Then for every integer \(1\le t\le m\),
\[
 \boxed{\Pr(T_n>t)=\frac{\displaystyle\sum_{k=t}^m a_{m,k}p_{m,k}(t)-m!\,[z^{m-t}]\exp\!\left(\sum_{s=1}^t z^s\right)}{N_m}.}
\]
For \(t\ge m\), this probability is zero; for \(t=0\), it is one. Taking differences gives every exact positive-power regularization-time multiplicity. The published static regularity criterion and monoid cardinality are not claimed as new; the exact power-hitting distribution and its limit law are the contributions.

## Assumptions and scope

The graph has \(n\) **labeled** vertices; the uniform law is on actual partial injections, not isomorphism classes, and the graph-homomorphism condition is imposed only on edges with both endpoints in the domain. The product \(f^t\) means \(t\)-fold composition of the same partial map, rather than a product of independent random maps. The theorem uses the published criterion (Dimitrova–Fernandes–Koppitz, Theorem 2.3) that \(f\in M_n\) is regular precisely when \(0\in\operatorname{dom}f\), or \(\operatorname{im}f=\{0\}\), or \(0\notin\operatorname{im}f\). The empty partial map is regular by the last condition.

Write \(m=n-1\), and let \(A_m\) be the set of members of \(M_n\) whose domain excludes the center. Each \(f\in A_m\) is an arbitrary partial injection from the \(m\) leaves to the \(m+1\) vertices. Its rank is \(k=|\operatorname{dom}f|\) and its deficiency among the leaves is \(J=m-k\). For such \(f\), let \(L(f)\) be the number of directed arrows in the maximal chain ending at the center \(0\), and \(L(f)=0\) when \(0\) is not in the image. Uniqueness and finiteness follow from injectivity and \(0\notin\operatorname{dom}f\).

## Proof

**1. The domain-excluding-center case dominates.** Fix \(0\le j\le m\) and \(k=m-j\). Choosing \(k\) domain leaves and injecting them into \(m+1\) possible images gives exactly
\[
 w_{m,j}=\binom mj\frac{(m+1)!}{(j+1)!}
\]
partial maps in \(A_m\) with deficiency \(j\). The ratio of successive weights is
\[
 \frac{w_{m,j+1}}{w_{m,j}}=\frac{m-j}{(j+1)(j+2)}.
\]
This ratio is strictly decreasing in \(j\); it exceeds one for \(j<(1-o(1))\sqrt m\) and is below one for \(j>(1+o(1))\sqrt m\). More precisely, for fixed \(\varepsilon\in(0,1)\), comparing the weights between \((1\pm\varepsilon/2)\sqrt m\) and \((1\pm\varepsilon)\sqrt m\) produces an \(e^{-c_\varepsilon\sqrt m}\) upper bound for either remote tail relative to a modal weight. The lower and upper tails each contain at most \(m+1\) terms; therefore
\[
 \Pr\left(\left|\frac{J}{\sqrt m}-1\right|>\varepsilon\ \middle|\ F_n\in A_m\right)\longrightarrow0.
\]
The ratio also bounds the upper tail beyond \(2\sqrt m\) geometrically, uniformly enough to imply \(\mathbb E[J\mid F_n\in A_m]=O(\sqrt m)\).

There are only two other mutually exclusive classes of members of \(M_n\). When \(0\) is in the domain and maps to itself, the map on the leaves is an arbitrary partial injection between leaves; its total count is \(B_m=\sum_{j=0}^m\binom mj^2(m-j)!\). In rank \(k=m-j\), its count is exactly \(w_{m,j}(j+1)/(m+1)\). Consequently,
\[
 \frac{B_m}{|A_m|}=\mathbb E\left[\frac{J+1}{m+1}\ \middle|\ F_n\in A_m\right]=O(m^{-1/2}).
\]
When \(0\) maps to a leaf, injectivity and edge preservation allow at most one other domain vertex, necessarily sent to \(0\); there are exactly \(m(m+1)\) such maps. Because \(|A_m|\ge(m+1)!\), this third type is negligible. Hence \(\Pr(F_n\in A_m)\to1\).

**2. Exact hub-chain tail and its exponential limit.** Conditional on \(F_n\in A_m\) and rank \(k=m-j\), the image is a uniform \(k\)-subset of the \(m+1\) vertices, and the domain/image bijection is uniform. The chance that \(0\) has one predecessor is \(k/(m+1)\). Given that the first \(i\) backwards arrows exist, the next one exists with probability \((k-i)/(m+1-i)\). Therefore, for each integer \(r\ge1\),
\[
 \Pr(L(F_n)\ge r\mid J=j,F_n\in A_m)
 =\frac{k}{m+1}\prod_{i=1}^{r-1}\frac{k-i}{m+1-i},
\]
where a product containing a nonpositive numerator is interpreted as zero. On the event \(J/\sqrt m\to1\), putting \(r=\lfloor x\sqrt m\rfloor\) for any fixed \(x>0\), the logarithm of this product is
\[
 \log\frac{k}{m+1}+\sum_{i=1}^{r-1}\log\!\left(1-\frac{j+1}{m+1-i}\right)
 =-\frac{r(j+1)}m+o(1)\longrightarrow-x.
\]
The error is uniform when \(J/\sqrt m\) lies in any fixed compact neighborhood of one; the complementary probability tends to zero by Step 1. Thus
\[
 \Pr(L(F_n)\ge\lfloor x\sqrt m\rfloor\mid F_n\in A_m)\to e^{-x},
\]
with the \(x=0\) case immediate. This establishes \(L(F_n)/\sqrt m\Rightarrow\operatorname{Exp}(1)\) under type \(A_m\).

**3. Cycles force the exact regularization time.** Each type-\(A_m\) map has a functional digraph consisting of vertex-disjoint directed chains and cycles. If it has at least one cycle, the image of every positive power contains a leaf. Meanwhile \(0\) is in the image of its \(t\)-th power if and only if \(t\le L(f)\), and \(0\) is in no power's domain. By the published regularity criterion, such a map satisfies exactly
\[
 T(f)=L(f)+1.
\]
To bound the exceptions, an acyclic partial injection on \(m+1\) labeled vertices with rank \(k\) consists of \(m+1-k\) ordered-path components. The unsigned Lah-number count is
\[
 \binom mk\frac{(m+1)!}{(m+1-k)!}.
\]
Exactly a fraction \((m+1-k)/(m+1)\) of these maps omit \(0\) from their domain, by symmetry, since each has \(m+1-k\) vertices outside its domain. Dividing by the total number \(w_{m,m-k}\) of type-\(A_m\) maps at rank \(k\) gives
\[
 \Pr(f\text{ has no directed cycle}\mid J=j,f\in A_m)
 =\frac{j+1}{m+1}.
\]
Averaging and using Step 1 shows that the probability of no cycle is \(O(m^{-1/2})\). Therefore \(T(F_n)=L(F_n)+1\) with probability \(1-o(1)\) under type \(A_m\). Combined with Step 1 and Step 2, this proves the asserted exponential limit law. If the center is in the domain, the first power is already regular. Otherwise, sufficiently high powers have the center absent from their image, proving that the minimum defining \(T_n\) always exists.

**4. Exact finite-size distribution.** For an integer \(t\ge1\), a map with center in the domain is already regular. For a map with center absent from the domain, regularity persists under further powers: once the center is missing from the image it can never return, and if the image is exactly \(\{0\}\) then the next power is empty. Thus \(T(f)>t\) is equivalent to nonregularity of \(f^t\), which occurs exactly when the center is in the image **and** at least one leaf is also in the image. The number of maps with center in the image of the \(t\)-th power is \(\sum_{k=t}^m a_{m,k}p_{m,k}(t)\), by Step 2. The overcount consists of maps whose \(t\)-th power has image exactly \(\{0\}\). Such a map must have (i) one directed path ending at the hub, with exactly \(t\) arrows, and (ii) no cycles, with every other path containing at most \(t\) vertices. If the hub's path uses \(t\) ordered leaves, it has \((m)_t\) possibilities. The other \(m-t\) labels form a set of oriented lists of sizes \(1,\ldots,t\); the exponential generating function for these chain forests is \(\exp(\sum_{s=1}^t z^s)\). The overcount is therefore exactly \((m)_t(m-t)![z^{m-t}]\exp(\sum_{s=1}^t z^s)=m![z^{m-t}]\exp(\sum_{s=1}^t z^s)\). Subtracting and dividing by the full monoid order \(N_m\) proves the displayed exact survival formula. Since no path into the hub contains more than \(m\) arrows, all members are regular by the \(m\)-th power.

## Verification

The accompanying standalone `verify.py` uses the Python standard library only. It enumerates actual injective partial star endomorphisms on \(2\) through \(6\) labeled vertices; independently calculates powers, regularity, hub predecessor chains, directed cycles, ranks, and all conditional tail frequencies; and checks the exact count, cycle-free formulas, and the complete finite-size regularization-time survival formula. It additionally numerically evaluates the rank-mixture survival probabilities at \(m=100,400,1600\), comparing them with the exponential limit. Execution terminates with `VERIFY_OK`. The finite checks corroborate the result but are not substitutes for the proof above.

## Relationship to prior work

Dimitrova, Fernandes, and Koppitz (arXiv:2401.11741v1, Theorem 2.3) established the criterion for regular elements, the three types of star partial injections (Proposition 1.11), and monoid cardinalities. Their later presentation paper (arXiv:2410.21084v1) concerns defining relations and generators. None of those inspected results states a first-regular-power distribution.

Ganyushkin and Mazorchuk (arXiv:math/0511431v1) studied partial-injection cycle/chain decompositions, including orbit-length counts (Theorems 3–5), deficiency ratios (Lemmas 3–5), and nilpotent counts. Janson and Mazorchuk (2005) further established sharp asymptotic counting and deficiency statistics for the unrestricted symmetric inverse semigroup. Laradji and Umar (2013, Proposition 2.6/Lemma 2.8) previously derived bounded-path-size nilpotent generating functions, including the familiar factor \(\exp(\sum_{s=1}^t z^s)\); the bounded-chain-forest generating function alone is not new. This provides substantial combinatorial antecedents and explains why a square-root scale is plausible. However, the inspected orbit counts concern the general symmetric inverse semigroup and do not state the law for the first regular power of a uniformly chosen injective **star endomorphism**. The theorem above additionally combines the star-specific regularity obstruction with the conditional terminal-chain distribution, a complete corrected finite-size survival formula, and an exact cycle-free probability. Its novelty is provisional pending a broader literature comparison; it must not be interpreted as first discovery of Lah-number, bounded-path generating functions or general chain counts.

## Limitations

The limit is for fixed star topology with a growing number of labeled leaves and the uniform distribution on injective partial endomorphisms. It makes no claim about noninjective partial maps, other graph families, or products of independent maps. The related general partial-injection literature may contain an alternative formulation or a dominating theorem not found in the source material inspected; this residual publication-priority risk remains. Independent mathematical audit has not been performed.

## References

1. I. Dimitrova, V. H. Fernandes, and J. Koppitz, *On partial endomorphisms of a star graph*, arXiv:2401.11741v1 (first public 2024-01-22), especially Propositions 1.10–1.11 and Theorem 2.3. https://arxiv.org/pdf/2401.11741
2. I. Dimitrova, V. H. Fernandes, and J. Koppitz, *Presentations for monoids of partial endomorphisms of a star graph*, arXiv:2410.21084v1 (first public 2024-10-28). https://arxiv.org/pdf/2410.21084
3. O. Ganyushkin and V. Mazorchuk, *Combinatorics and distributions of partial injections*, arXiv:math/0511431v1 (first public 2005-11-17), particularly Sections 2–5. https://arxiv.org/pdf/math/0511431

4. S. Janson and V. Mazorchuk, *Some remarks on the combinatorics of ISn*, Semigroup Forum 70 (2005), 391–405, Section 5 on deficiency, stable rank and order. https://www2.math.uu.se/~svantejs/papers/sj168.pdf
5. A. Laradji and A. Umar, *On the number of subpermutations with fixed orbit size*, Ars Combinatoria 109 (2013), 447–460, Section 2 on bounded-path nilpotent generating functions. https://combinatorialpress.com/article/ars/Volume%20109/volume-109-paper-34.pdf
