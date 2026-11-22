# Exact product-rank law for the dihedral restriction monoid of a finite cycle

## Finding
For every integer \(n\ge3\), let \(\Omega=\mathbb Z/n\mathbb Z\), let \(G=D_{2n}\) act on \(\Omega\) by \(x\mapsto\pm x+a\), and let \(\mathcal D_n\) be the set of distinct partial bijections \(g|_D\) for \(g\in G\), \(D\subseteq\Omega\), including the empty map. The operation is partial-function composition. Write
\[
Q_n(t)=\sum_{f,h\in\mathcal D_n}t^{\operatorname{rank}(f\circ h)}.
\]
Introduce the even-cycle indicator \(\epsilon=\mathbf1_{2\mid n}\) and
\[
a=1-\frac1{2n},\quad S=a+\frac n2+\epsilon\frac n4,\quad v=\frac{1+\epsilon}{2},
\]
\[
B_n(t)=2^na+n2^{n-2}(1+t)+\epsilon n2^{n-4}(1+t)^2,
\]
\[
C_n(t)=S^2+nv^2(t-1)+\epsilon\frac n8(t-1)^2.
\]
**Complete two-factor rank theorem.** For every integer \(n\ge3\),
\[
\boxed{Q_n(t)=4n^2\left[(3+t)^n-2B_n(t)+C_n(t)\right].}
\]
Thus \(Q_n(t)\in\mathbb Z[t]\) has nonnegative coefficients, and \(|\mathcal D_n|=2n(2^n-S)\). In particular, this formula counts *distinct restrictions*: the empty map, singleton maps, and the antipodal rank-two maps for even \(n\) each contribute only once, not according to their numbers of dihedral extensions.

For independently uniform \(F,H\in\mathcal D_n\), define \(R_n=\operatorname{rank}(F\circ H)\). Then
\[
\boxed{\mathbb E R_n=n\left(\frac{2^{n-1}-v}{2^n-S}\right)^2,}
\]
and
\[
\boxed{d_{\mathrm{TV}}\left(\mathcal L(R_n),\operatorname{Binomial}(n,1/4)\right)\le\frac{2S}{2^n}=O(n2^{-n}).}
\]
In particular, \((R_n-n/4)/\sqrt{3n/16}\) converges in law to a standard normal random variable as \(n\to\infty\). The exponentially small total-variation error contrasts with the polynomial-size error for products of uniform partial *translations on a finite chain*.

## Assumptions and scope
All maps and domains are labeled; restrictions are identified if and only if the resulting partial functions are equal. The rank is the cardinality of the domain of a partial bijection. Products have the convention \((f\circ h)(x)=f(h(x))\), but the ordered-pair rank enumerator is invariant under interchanging the names of the factors. The cycle is undirected; when \(n=3\) the dihedral action is the full symmetric action on three points, and all formulas still apply. The theorem is about an ordered pair of independent uniform **distinct** monoid elements, not pairs of independently uniform dihedral group elements with independently uniform domains. The exact formulas include \(t=0,1\) and every rank from zero through \(n\). The asymptotic is for \(n\to\infty\).

## Proof
**1. Multiplicities of dihedral extensions.** For each subset \(D\subseteq\Omega\), a partial map \(g|_D\) has \(s(D)=|\{u\in G:u(x)=x\text{ for every }x\in D\}|\) distinct extensions in \(G\). The pointwise stabilizer sizes are \(2n\) for \(D=\varnothing\), two for every singleton, two for an antipodal pair \(\{x,x+n/2\}\) when \(n\) is even, and one for all remaining domains. Indeed, any nonidentity rotation fixes no vertex, and a nonidentity reflection has at most two fixed vertices, with two only at an antipodal pair in an even cycle. Set \(c(D)=1/s(D)\). Assigning weight \(c(D)\) to each representation \((g,D)\) counts each distinct partial map once.

**2. A restriction-monoid convolution identity.** For any finite permutation group \(G\curvearrowright\Omega\) and its monoid of restrictions, we have
\[
\sum_{f,h}t^{\operatorname{rank}(f\circ h)}=|G|^2\sum_{D,E\subseteq\Omega}c(D)c(E)t^{|D\cap E|}.
\]
To prove this, represent both partial maps by \((g,D)\) and \((u,E)\). Their composition has rank \(|E\cap u^{-1}D|=|u(E)\cap D|\). Sum over \(g\in G\), giving one factor \(|G|\). For each \(u\), change variables \(E'=u(E)\). Pointwise stabilizer sizes satisfy \(s(u(E))=s(E)\); consequently the domain sum is identical for each \(u\), giving the second factor \(|G|\). The weights ensure the left side counts each distinct pair of partial maps precisely once. This proves the identity, including the empty domain and domains with nonunique extensions.

**3. Explicit correction from repeated extensions.** Put \(b(D)=1-c(D)\). Only three types of domains have \(b(D)\ne0\): the empty domain has weight \(a\); every singleton has weight \(1/2\); and each of the \(n/2\) antipodal pairs, when present, has weight \(1/2\). Hence
\[
\sum_D b(D)=S,\qquad \sum_{D\ni x}b(D)=v\quad(x\in\Omega).
\]
For each unordered pair \(\{x,y\}\), the sum of \(b(D)\) over domains containing that pair is \(1/2\) if it is antipodal and \(0\) otherwise. Consequently
\[
\sum_{\{x,y\}\subseteq\Omega}\left(\sum_{D\supseteq\{x,y\}}b(D)\right)^2=\epsilon\frac n8.
\]
Expand \(c(D)c(E)=(1-b(D))(1-b(E))\). The uncorrected sum is \((3+t)^n\), because each vertex may lie in neither, the first only, the second only, or both sets. Its single-weight correction is
\[
\sum_{D,E}b(D)t^{|D\cap E|}=\sum_D b(D)2^{n-|D|}(1+t)^{|D|}=B_n(t).
\]
For the double correction note that \(|D\cap E|\le2\) whenever \(b(D)b(E)\ne0\), so
\[
t^{|D\cap E|}=1+(t-1)|D\cap E|+(t-1)^2\binom{|D\cap E|}{2}.
\]
Summing the constant, linear and quadratic terms and applying the displayed subset identities yields exactly \(C_n(t)\). The general convolution identity with \(|G|=2n\) now gives the stated polynomial. Evaluating at \(t=1\) gives \(|\mathcal D_n|=2n(2^n-S)\).

**4. Uniform sampling, mean and sharp approximation scale.** A uniform distinct partial map is obtained by choosing a dihedral symmetry uniformly in \(G\), independently choosing its domain with probability \(c(D)/(2^n-S)\), and then restricting. Each resulting partial map has the same total probability because its number of representations is \(s(D)\). For two independently sampled partial maps, the convolution identity shows their product rank is distributed exactly as \(|D\cap E|\) for independent domains with this probability law. (The intervening independent uniform symmetry sends the second domain to an independent domain with the same invariant distribution.) Hence the inclusion probability of one specified vertex is \(p=(2^{n-1}-v)/(2^n-S)\), giving \(\mathbb E R_n=np^2\).

Compare that domain law with the uniform law on the \(2^n\) subsets. One can sample a uniform subset and accept it with probability \(c(D)\). The conditional accepted distribution is the needed law, and the unconditional rejection probability is \(S/2^n\). Coupling with a rejected sample replaced by a fresh draw shows the total-variation distance of these two domain laws is at most \(S/2^n\). Independently couple both domains; the difference between the two intersection-size distributions is at most \(2S/2^n\). For uniformly independent subsets, every vertex survives their intersection with independent probability \(1/4\), yielding \(\operatorname{Binomial}(n,1/4)\). Finally this binomial law has the standard Gaussian limit, which the total-variation bound transfers to the normalized product ranks.

## Verification
The standalone `verify.py` explicitly generates *distinct* restrictions of all dihedral symmetries for \(n=3,4,5,6,7\), composes **every ordered pair** of partial maps, and compares each coefficient with the rational-arithmetic polynomial formula. It independently checks the exact monoid size and product-rank mean. The resulting coefficient vectors by increasing rank are:

- \(n=3\): \((229,567,324,36)\).
- \(n=4\): \((1569,4032,2976,768,64)\).
- \(n=5\): \((11571,32625,27000,9000,1500,100)\).
- \(n=6\): \((56989,169128,168156,77760,19440,2592,144)\).
- \(n=7\): \((297753,912723,1000188,555660,185220,37044,4116,196)\).

The captured output is in `verification_output.txt`. These are finite corroborations, not an infinite proof; universal and asymptotic statements follow from the preceding argument.

## Relationship to prior work
Fernandes and Paulista's full study of cycle partial isometries (2022) already establishes the *dihedral restriction representation*, including the exceptional duplication of empty, singleton and antipodal maps, and enumerates individual maps. Those inputs are credited, not claimed as new. Fernandes and Quinteiro's 2015 work provides an archived treatment of the related chain partial-isometry monoids; the cycle-specific primary source is 2022 and this is stated explicitly to avoid misdating it. The published rank-uniform convolution theorem for the **full symmetric inverse monoid** concerns uniformly sampled partial bijections of fixed rank; restricting to the dihedral submonoid with its nonuniform extension stabilizers is not an instance of its rank-uniform hypothesis. The previously obtained finite-*chain* partial-translation product-rank distribution pertains to a different monoid, with a different limiting error rate. Previously reported cycle inverse-monoid formulas classify self-inverse elements or nilpotent *single elements*; those invariants do not determine the product-rank spectrum of independently sampled elements.

## Limitations
This theorem treats exactly two unrestricted factors, not the all-length product semigroup distribution, fixed individual-factor ranks, or the distribution of the resulting partial map itself. Its novelty assessment compares the principal cycle and restriction-monoid literature and relevant existing product-rank results, but cannot rule out all equivalent older formulas, including formulas implicit in group-action restriction convolution theory. The 2015 archival antecedent is for chain partial isometries; the specific cycle restriction theorem first located is dated 2022. The finite checker is not a substitute for the universal proof.

## References
1. V. H. Fernandes and T. M. Quinteiro, *Presentations for monoids of finite partial isometries*, arXiv:1502.04829 (first posted 2015-02-17), https://arxiv.org/abs/1502.04829.
2. V. H. Fernandes and P. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (first posted 2022-05-04), https://arxiv.org/abs/2205.02196.
3. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *On three submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.01519, https://arxiv.org/abs/2301.01519.
4. *Rank-uniform convolution and coupon-collector collapse in the symmetric inverse monoid*, public result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-rank-uniform-convolution-and-coupon-collector-collapse-in-the-sy--1110b14cea6d.
5. *The product-rank law of finite-chain partial translations*, public result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-product-rank-law-of-finite-chain-partial-translations--849553a20428.
