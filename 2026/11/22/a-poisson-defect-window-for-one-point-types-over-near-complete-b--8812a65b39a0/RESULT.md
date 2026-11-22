# A Poisson defect window for one-point types over near-complete bipartite posets

## Finding
Let \(\mathbb P\) be the countable universal homogeneous partial order. For each \(n\ge1\), form a finite named height-two poset \(P_n\) on two specified antichains \(A_n,B_n\), each of size \(n\): retain each possible comparison \(a<b\), for \(a\in A_n,b\in B_n\), independently with probability \(1-q_n\). Let \(T_n\) be the number of **complete nonalgebraic one-types** over the individually named elements of \(P_n\). These are distinct types with the new point unequal to every parameter, without quotienting the named parameters by automorphisms.

**Poisson defect window and sharpness.** If \(n^2q_n\to\lambda\in[0,\infty)\), then
\[
 \frac{T_n}{4^n}\ \xrightarrow{\ d\ }\ \left(\frac34\right)^{Z_\lambda},
 \qquad Z_\lambda\sim\operatorname{Poisson}(\lambda).
\]
Every fixed positive integer moment converges. In particular,
\[
 \lim_{n\to\infty}\mathbb E\frac{T_n}{4^n}=e^{-\lambda/4},\qquad
 \lim_{n\to\infty}\operatorname{Var}\left(\frac{T_n}{4^n}\right)
 =e^{-7\lambda/16}-e^{-\lambda/2}.
\]
The window is sharp within the near-complete regime \(q_n\to0\): if \(n^2q_n\to0\) the normalized count tends to \(1\) in probability, whereas if \(n^2q_n\to\infty\) it tends to \(0\) in probability.

**Inhomogeneous universality.** The finite-\(\lambda\) law persists for independently omitted cross-comparisons with probabilities \(q_{ij}^{(n)}\), provided \(a_n,b_n\to\infty\), \(\sum_{ij}q_{ij}^{(n)}\to\lambda\), and the largest total omission probabilities in any single row and any single column both tend to zero. Normalize the type count by \(2^{a_n+b_n}\) in this rectangular setting.

The deterministic structural identity driving these limits is the following: if a complete \(a\)-by-\(b\) height-two poset is altered by deleting exactly \(k\) comparisons forming a matching, with \(0\le k\le\min(a,b)\), then its nonalgebraic one-type count is
\[
 \boxed{T(a,b,k)=2^{a+b-2k}3^k+2^a+2^b-2+2k.}
\]
This identity is an elementary specialization of an existing general height-two type-count formula; the new claim is the sharp **distributional** defect window, its moment law and inhomogeneous universality, not a claim of novelty for the general ideal/filter representation or for the matching specialization alone.

## Assumptions and scope
A height-two parameter poset is specified by labelled disjoint antichains \(A,B\) and a bipartite comparison graph \(G\subseteq A\times B\), with strict comparisons precisely \(a<b\) when \((a,b)\in G\). Even when some parameter is isolated, its intended side remains specified; the induced partial order is unambiguous. All omitted comparisons are independent in the random models. In the balanced model \(a=b=n\), \(q_n\in[0,1]\) is the **omission** probability, not the retention probability.

An admissible nonalgebraic one-type is an ideal/filter pair \((L,U)\) in which \(L\) is the set of parameters below the new point, \(U\) those above it, and every point of \(L\) is strictly below every point of \(U\). The Fraïssé extension property realizes each such finite extension; homogeneity identifies realizations of the same pattern with a single complete type. Algebraic types \(x=a\) are excluded throughout.

In the rectangular inhomogeneous statement, the assumptions mean
\[
 \max_{1\le i\le a_n}\sum_{j=1}^{b_n}q_{ij}^{(n)}\to0,
 \qquad \max_{1\le j\le b_n}\sum_{i=1}^{a_n}q_{ij}^{(n)}\to0.
\]
The Poisson parameter \(\lambda\) can be zero. Only distributional and fixed-moment convergence is asserted; there is no large-deviation or convergence-rate claim.

## Proof
**1. A disjoint trichotomy.** For any finite bipartite comparison graph \(G\) with sides \(A,B\), divide the one-point extensions by the statuses of the new point \(x\):

- Family I has no parameter of \(A\) above \(x\) and no parameter of \(B\) below \(x\). Thus \(L\subseteq A\), \(U\subseteq B\), and every pair of \(L\times U\) must be an existing comparison. Conversely every such pair is legal.
- Family II has at least one point of \(A\) above \(x\). Since distinct points of \(A\) are incomparable, no point of \(A\) can be below \(x\). Moreover, no point of \(B\) can be below \(x\): this would force a maximal point below a minimal point through \(x\). Put \(S=\{a\in A:x<a\}\ne\varnothing\) and \(V=\{b\in B:x\parallel b\}\). Then the extension is legal exactly when every pair of \(S\times V\) is an **omitted** comparison of \(G\).
- Family III is the order dual: at least one point of \(B\) is below \(x\); no point of \(B\) is above \(x\), no point of \(A\) is above \(x\), and each selected incomparable lower point must have an omitted comparison to each selected upper point below \(x\).

The three families are disjoint and exhaustive. With \(a=|A|,b=|B|\), and independent retention probability \(p\), summing the families yields the exact expected count
\[
\begin{aligned}
\mathbb E_p T(a,b)
={}&\sum_{i=0}^{a}\binom ai(1+p^i)^b\\
&+\sum_{s=1}^{a}\binom as(1+(1-p)^s)^b
 +\sum_{t=1}^{b}\binom bt(1+(1-p)^t)^a.
\end{aligned}
\tag{1}
\]
The first term chooses a lower-point subset of size \(i\) and then chooses each upper-point status; each chosen upper point requires \(i\) independent present comparisons. The second and third terms analogously require independent *absent* comparisons. Formula (1) is a useful finite evaluation, not a separate originality claim.

**2. Exact deleted-matching formula.** Suppose the \(k\) missing comparisons are pairwise disjoint in both endpoint sets. In Family I, an omitted pair cannot have both its endpoints selected, giving exactly three choices of their two binary statuses instead of four; all other parameters have two choices each. Hence this family has \(2^{a+b-2k}3^k\) types. In Family II, when every upper parameter lies above \(x\), there are \(2^a-1\) nonempty choices of \(S\). A nonempty set \(V\) of incomparable upper parameters must have \(S\times V\) entirely missing. Since the missing edges form a matching, this is possible only when \(S\) and \(V\) are the two single endpoints of one missing edge, giving exactly \(k\) additional possibilities. Thus Family II contributes \(2^a-1+k\). Dually Family III contributes \(2^b-1+k\). Their sum proves the displayed identity for every \(a,b,k\), including \(k=0\).

**3. General independent rare defects.** Write \(K_n\) for the total number of deleted comparisons in the rectangular inhomogeneous model. Its mean \(\lambda_n=\sum_{ij}q_{ij}^{(n)}\) tends to \(\lambda\). The largest \(q_{ij}^{(n)}\) tends to zero because the row sums do; therefore \(\sum_{ij}(q_{ij}^{(n)})^2\to0\). The elementary Poisson approximation for sums of independent Bernoulli variables yields \(K_n\Rightarrow Z_\lambda\).

The probability of any two deleted edges meeting at a lower vertex is at most
\[
 \frac12\sum_i\left(\sum_j q_{ij}^{(n)}\right)^2
 \le\frac{\lambda_n}{2}\max_i\sum_jq_{ij}^{(n)}\longrightarrow0.
\]
The corresponding upper-vertex bound is identical with rows and columns interchanged. Hence, with probability tending to one, **all omitted comparisons form a matching**. On that event the exact identity from Step 2 applies and gives
\[
 \frac{T_n}{2^{a_n+b_n}}
 =\left(\frac34\right)^{K_n}
 +\frac{2^{a_n}+2^{b_n}-2+2K_n}{2^{a_n+b_n}}.
\]
The remainder converges to zero in probability because \(a_n,b_n\to\infty\) and \(K_n\) is tight. The continuous-mapping and Slutsky arguments prove the inhomogeneous distributional limit and therefore the balanced Poisson window.

For fixed positive integer moments, note that the general height-two ideal/filter identity
\[
 T(G)=2i(G)+i(\overline G)-2^{a}-2^{b}
\tag{2}
\]
expresses the count via numbers of independent vertex subsets of the comparison graph and its bipartite complement. Since each independent-set count is at most \(2^{a+b}\), the normalized count is bounded between zero and three for **every** graph and every \(a,b\). Boundedness converts distributional convergence into convergence of all fixed moments. The Poisson probability generating function gives \(\mathbb E(3/4)^{Z_\lambda}=e^{-\lambda/4}\) and \(\mathbb E(3/4)^{2Z_\lambda}=e^{-7\lambda/16}\), proving the stated variance.

**4. Sharpness outside the finite window.** For the balanced independent model, let \(X,Y\) be independent \(\operatorname{Bin}(n,1/2)\) variables. From the first term of (1), the normalized expected Family I contribution equals \(\mathbb E[(1-q_n)^{XY}]\). Hoeffding's inequality gives \(\Pr(X<n/3\text{ or }Y<n/3)\le2e^{-n/18}\); outside that event, \((1-q_n)^{XY}\le e^{-q_nn^2/9}\). For each of Families II and III, because \(q_n^s\le q_n\) for \(s\ge1\), (1) gives the normalized expectation bound \(((1+q_n)/2)^n\). Therefore
\[
 0\le \mathbb E\frac{T_n}{4^n}
 \le2e^{-n/18}+e^{-q_nn^2/9}
 +2\left(\frac{1+q_n}{2}\right)^n.
\tag{3}
\]
If \(q_n\to0\) and \(q_nn^2\to\infty\), the right-hand side tends to zero; Markov's inequality proves convergence to zero in probability. If \(q_nn^2\to0\), a union bound shows that with probability tending to one no comparison is missing. On that event \(T_n=4^n+2^{n+1}-2\), and normalization tends to one. This proves both sides of the sharp window.

## Verification
The standard-library script `verify.py` independently enumerates all three statuses of a new point relative to each named parameter and checks the necessary ideal/filter and cross-order conditions. It compares this direct count with the disjoint-family formula on 682 bipartite comparison graphs with both sides of size at most three. It also checks the exact deleted-matching formula for 46 triples with \(1\le a,b\le4\), the exact expectation (1) against complete edge-set enumeration at 14 rational-probability test cases, and complete versus fully matching-deleted endpoints through five points per side. Its recorded execution output is in `verification_output.txt`. These are finite consistency checks; the general identities and limits are proved above.

## Relationship to prior work
The one-point extension/ideal-filter correspondence and the \(\#\mathrm P\)-completeness of generic-poset one-type counting have been established. In particular, a published height-two study already gives the general formula (2) and a sharp local signed change under adding one comparison. Another published analysis treats the exact one-missing-comparison case and the first finite nonmonotonicity example. Their general formula logically makes the finite deleted-matching calculation accessible; **neither that finite calculation alone nor the ideal/filter trichotomy is presented as original here**.

The subject here is instead an independent-edge random model, its parameter-scale transition, a nondegenerate Poisson **law for the normalized logical-type count**, all fixed moments, and the extension to nonuniform independent defects with vanishing row/column intensities. The closest inspected height-two results address exact counts and deterministic modifications, not this random-defect distribution. Earlier work on random bipartite posets investigates order dimension rather than the finite-parameter type count. The Poisson approximation itself is standard; the contribution is the verified mapping from rare order-relation defects to the type-count law and its sharpness. No search establishes absolute historical priority.

## Limitations
This is a result about the number of complete nonalgebraic one-types, with uniformly random **named parameter structures**, not about sampling a new point from the countable universal poset. The near-complete sharpness claim requires \(q_n\to0\); for large omission probabilities the behavior is different. No limit theorem is claimed for the intermediate regime \(q_n\asymp1/n\), for unrestricted random finite posets, or for two- and higher-arity types. The exact matching identity and the general height-two independent-set formula are elementary or known ingredients. Historical originality is provisional; the result has not undergone independent review.

## References
1. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1, first posted 2010-09-03; Chapter 3.1 develops the countable generic partial order and its extension property. https://arxiv.org/abs/1009.0566
2. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892v1, first posted 2010-09-15; its one-point extension data are relevant background. https://arxiv.org/abs/1009.2892
3. P. Erdős, H. A. Kierstead and W. T. Trotter, *The dimension of random ordered sets*, Random Structures & Algorithms 2 (1991), 253–275, DOI:10.1002/rsa.3240020302; develops the random bipartite-poset model for a different invariant.
4. *One comparability can increase finite-poset one-point type counts exponentially*, published mathematical record 828ff1d8f784 (2026); gives the one-missing-relation count and deterministic comparison.
5. *Sharp one-comparability sensitivity and local counting hardness for random-poset one-types*, published mathematical record 9c2af418ff79 (2026); its equation (3) gives the general height-two independent-set type count.
6. *Finite-parameter 1-type counting in the random poset is #P-complete*, published mathematical record 3b955f4020e1 (2026); establishes the finite-parameter type/ideal-filter framework.
