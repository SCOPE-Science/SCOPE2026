# Sharp quadratic saturation kernels and exact random-mapping laws for bounded unary orbit types

## Finding
Fix an integer \(d\geq1\). In the language with equality and a total unary function \(f\), a **depth-\(d\) one-point type** is the complete equality pattern of the terms \(x,f(x),\ldots,f^d(x)\). The realizable types, uniformly over finite structures, consist of a no-repetition type \(\infty\) and types \((t,c)\) with \(t\geq0\), \(c\geq1\), and \(t+c\leq d\), where \(t\) is the transient length and \(c\) the eventual period. There are exactly \(1+d(d+1)/2\) types.

Call a nonempty finite function \(f:X\to X\) **\(d\)-saturating** if every one of these types occurs at some point of \(X\). Then:

1. The least possible cardinality of \(X\) is exactly \(d^2+1\). There are exactly \(d\) isomorphism classes at that cardinality, and the number of such maps on the labeled set of size \(d^2+1\) is
\[
(d^2+1)!\,\frac{2d-1}{d}.
\]
2. The following explicit exponential generating function gives the number \(s_d(n)\) of labeled \(d\)-saturating functions on \(n\) vertices:
\[
\begin{aligned}
T(z)&=ze^{T(z)},\qquad H_{-1}(z)=0,\qquad H_j(z)=z\exp(H_{j-1}(z))\quad(j\ge0),\\
G_d(z)&=\frac{1}{1-T(z)}\prod_{c=1}^{d}\left(1-\exp\left[-\frac{T(z)^c-H_{d-c-1}(z)^c}{c}\right]\right),\\
B_d(z)&=\exp\left(\sum_{c=1}^{d}\frac{H_{d-c}(z)^c}{c}\right)
\prod_{c=1}^{d}\left(1-\exp\left[-\frac{H_{d-c}(z)^c-H_{d-c-1}(z)^c}{c}\right]\right),\\
s_d(n)&=n!\,[z^n]\bigl(G_d(z)-B_d(z)\bigr).
\end{aligned}
\]
3. For a uniformly random total function \(f:[n]\to[n]\), and each **fixed** \(d\), the saturation probability has the exact nonzero limit
\[
\lim_{n\to\infty}\frac{s_d(n)}{n^n}
=\prod_{c=1}^{d}\left(1-\exp\left[-\frac{1-h_{d-c}^{c}}{c}\right]\right),\quad h_0=0,\quad h_{j+1}=\exp(h_j-1).
\]
For depths \(d=1,2,3,4\), the limiting probabilities are approximately \(0.6321205588\), \(0.1843547061\), \(0.0372209321\), and \(0.0056496835\).

## Assumptions and scope
All structures are finite nonempty sets with one arbitrary **total** unary function, with no named constants or additional predicates. All quantifier-free formulas use only one free variable \(x\), Boolean connectives, equality, and iterates of \(f\) of exponent at most \(d\); the result concerns complete atomic equality types and not quantifier rank or unrestricted first-order types. The graph of a unary function has one outgoing edge at every vertex; each weakly connected component contains a unique directed cycle, with rooted in-trees feeding its cycle vertices. The transient length of \(x\) is its distance to this cycle, and its eventual period is that cycle's length. Coefficients of formal power series are taken at \(z=0\). All asymptotics keep \(d\) fixed.

## Proof
**Type classification.** Starting at any vertex, the sequence \(x,f(x),\ldots,f^d(x)\) either has no equal pair, or its first repeated entry occurs at a unique index \(t+c\leq d\), repeating entry \(t\). Thereafter equality is entirely determined by \(t\) and \(c\), so the distinct possible patterns are exactly the displayed types. A path of length \(t\) into a directed \(c\)-cycle realizes \((t,c)\), and a directed cycle of length \(d+1\) realizes \(\infty\). Each type is a complete quantifier-free equality description for the prescribed terms.

**Sharp kernel and classification.** For each \(c\in\{1,\ldots,d\}\), saturation forces the type \((d-c,c)\). It therefore forces a directed cycle of length \(c\) with a vertex at transient distance at least \(d-c\) from that cycle; this needs at least \(d\) vertices. Distinct cycle lengths require disjoint components, so \(|X|\geq d^2\). If equality holds, there is for each \(c\) exactly one component, a \(c\)-cycle with one directed incoming chain of length exactly \(d-c\). Every orbit repeats by time \(d\), contradicting realization of \(\infty\). Thus \(|X|\geq d^2+1\).

For each choice \(e\in\{1,\ldots,d\}\), take all these \(d\) components and extend the chain of the \(e\)-cycle by exactly one leaf (for \(e=d\), attach a leaf to one of the cycle vertices). This realizes every \((t,c)\) and \(\infty\), hence attains \(d^2+1\). Conversely, any saturation-minimal map consists of exactly the forced \(d^2\) vertices plus one vertex, and the only way to realize \(\infty\) is to extend one of the forced longest chains. Different \(e\) are inequivalent because the cycle lengths are preserved. When \(e=d\), every component is rigid and the automorphism group is trivial; when \(e<d\), the untouched bare \(d\)-cycle gives exactly \(d\) rotational automorphisms, and all other components are rigid. By orbit-stabilizer, the labeled count is \((d^2+1)![1+(d-1)/d]\).

**Exact counting formula.** The exponential generating function of rooted labeled in-trees is \(T=ze^T\); that of such trees of height at most \(j\) is \(H_j=z\exp(H_{j-1})\), starting with \(H_{-1}=0\). A connected functional component with cycle length \(c\), whose in-trees are chosen from a class with EGF \(U\), has EGF \(U^c/c\). Taking sets of components yields the classical EGF of all functions, \(\exp(\sum_{c\geq1}T^c/c)=1/(1-T)\).

For a given \(c\le d\), the type \((d-c,c)\) occurs if and only if at least one \(c\)-cycle component has an in-tree reaching height \(d-c\). The EGF for those qualifying components is \((T^c-H_{d-c-1}^c)/c\); the Poisson/SET subtraction of structures with none of these components gives the corresponding factor in \(G_d\). The factors for different \(c\) are independent at the component-species level, so \(G_d\) counts maps realizing **all repetition types**, with no restriction on \(\infty\).

Now exclude those maps without the type \(\infty\). Such a map has **no** cycles longer than \(d\), and every in-tree attached to a cycle of length \(c\le d\) has height at most \(d-c\). For each \(c\), the type \((d-c,c)\) still requires at least one \(c\)-cycle with maximum height **equal to** \(d-c\). The unrestricted bounded-height components have total EGF \(\exp(\sum H_{d-c}^c/c)\), and the mandatory full-height factor is \(1-\exp(-(H_{d-c}^c-H_{d-c-1}^c)/c)\). Their product is precisely \(B_d\). Therefore \(G_d-B_d\) counts exactly the saturating maps.

**Asymptotic law.** The solution \(T=ze^T\) has its unique dominant square-root singularity at \(\rho=e^{-1}\), with \(T(\rho)=1\) and \(1-T(z)\sim\sqrt{2(1-z/\rho)}\). Every finite-height function \(H_j\) is entire and evaluates at \(\rho\) according to \(H_{j}(\rho)=h_{j+1}\). Thus the product multiplying \((1-T)^{-1}\) in \(G_d\) tends at \(\rho\) to the stated strictly positive constant. Standard transfer for this square-root singularity gives its coefficient relative to \([z^n](1-T)^{-1}=n^n/n!\) tending to that constant. Since \(B_d\) is entire, \([z^n]B_d\) is negligible compared to \(n^n/n!\). This proves the probability limit. It is equivalently the asymptotic product of independent Poisson occupancy probabilities for the required short-cycle/height classes; no independence assumption for finite \(n\) is used.

## Verification
The accompanying standalone standard-library script `verify.py` computes the exact EGF coefficients over rational numbers, independently enumerates **all** \(n^n\) labeled functions for \(1\leq n\leq6\) and \(d\in\{1,2,3\}\), compares realization of every orbit type to the formula, and tests all \(d\) extremal constructions through \(d=11\). Execute `python verify.py`. The observed result is `VERIFY_OK 84`. For \(d=1\), counts for \(n=0,\ldots,6\) are \(0,0,2,18,174,2100,31030\); for \(d=2\), they are \(0,0,0,0,0,180,4500\). This finite computation corroborates, but is not substituted for, the general proof and asymptotic transfer.

## Relationship to prior work
Kuželka (2026) establishes general exact model-counting tractability for fixed one-variable unary-function sentences and constructs forward orbit profiles and cycle/in-tree generating functions. In particular, the existence of each depth-\(d\) atomic profile is expressible in that fragment, so tractability itself is **not** claimed here. The present theorem supplies a specific sharp uniform minimal carrier, complete classification at that carrier, a closed all-profile count, and its random-mapping limit, which are not stated in the inspected primary text. Classical functional-digraph species and singularity methods are credited to the Flajolet–Odlyzko tradition and the 1996 Soria seminar account. They underlie but do not automatically supply the conjunction-of-all-profiles formulas without the component-height analysis above.

## Limitations
No originality certification, independent mathematical audit, or claim about richer unary signatures, multiple free variables, unbounded term depth, or a joint limit in which \(d\) increases with \(n\) is made. The full historical random-mapping literature is extensive; an older equivalent saturation formulation remains a priority risk. The Flajolet–Odlyzko conference chapter was available at abstract level during comparison; the 1996 Soria account was examined directly. The general proof uses standard labeled-species and singularity-transfer results explicitly identified above, while the script checks only finite sizes.

## References
1. Ondřej Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580, first version August 31, 2026. Full text (v2): https://arxiv.org/html/2608.30580v2 . In particular Sections 3 and 8.1.2–8.1.6.
2. Philippe Flajolet and Andrew M. Odlyzko, *Random Mapping Statistics*, in *Advances in Cryptology—EUROCRYPT '89*, Lecture Notes in Computer Science 434, 1990, pp. 329–354. DOI: https://doi.org/10.1007/3-540-46885-4_34 . Abstract consulted.
3. Michèle Soria, *Distribution of Image Points in Random Mappings*, Algorithms Seminar, November 10, 1996. https://algo.inria.fr/seminars/sem96-97/soria.html . Accessible text inspected, in particular the random-mapping component EGF and limiting-distribution discussion.
