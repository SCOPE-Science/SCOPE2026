# Sharp rank-two stabilization for uniformly random permutations

## Finding
For each integer \(n\ge 1\), sample a uniform permutation \(\pi\in\mathfrak S_n\) as a structure with two strict total orders \(<_P\) (positions) and \(<_V\) (values). Let \(M(\pi)\) be the set of occupied-quadrant masks defined below. Then for any two nonempty finite permutations \(\pi,\sigma\),
\[
\pi\equiv_2\sigma\quad\Longleftrightarrow\quad M(\pi)=M(\sigma),
\]
where \(\equiv_2\) denotes agreement on every first-order sentence of quantifier rank at most two. There is a unique rank-two theory occurring with probability tending to one, characterized by
\[
M_\star=\{3,5,7,10,11,12,13,14,15\}.
\]
It has a shortest finite representative of exactly nine vertices, for instance \(\pi_\star=(3,2,5,9,1,6,4,8,7)\). For some positive absolute constants \(c,C\) and all sufficiently large \(n\),
\[
c\frac{\log n}{n}\le \Pr\{M(\Pi_n)\ne M_\star\}\le C\frac{\log n}{n}.
\]
More precisely, if \(H_j=\sum_{i=1}^j1/i\) and \(a_n=\sum_{i=2}^{n-1}\big[n\binom{n-1}{i-1}\big]^{-1}\), then for \(n\ge4\),
\[
\frac{1+H_{n-1}}n\le\Pr\{M(\Pi_n)\ne M_\star\}\le \frac{4H_{n-1}+32}{n}+6a_n,
\qquad a_n=O(n^{-2}).
\]
Consequently every fixed first-order sentence of quantifier rank at most two has limiting probability either zero or one, and its almost-sure truth value agrees with its truth in \(\pi_\star\). This rank boundary is sharp: there exists a rank-three first-order sentence whose probability tends to \(1-e^{-1}\).

## Assumptions and scope
The language has only equality and the two binary strict-order predicates \(<_P,<_V\); there are no named points, constants, built-in successors, counting quantifiers, or predicates for extra geometric information. The rank of a sentence is the maximum nesting depth of ordinary quantifiers; all quantifier alternations are allowed. The permutation distribution is uniform on all \(n!\) orderings. Each element is represented by its position \(i\) and value \(\pi(i)\). For a point \(x\), let its four quadrants be SW (earlier position, smaller value), NW (earlier position, larger value), SE (later position, smaller value), and NE (later position, larger value). Set the mask \(m(x)=\sum_{q\in\{\mathrm{SW},\mathrm{NW},\mathrm{SE},\mathrm{NE}\}}2^{b(q)}\mathbf1\{\exists y\text{ in quadrant }q\text{ of }x\}\), where \(b(\mathrm{SW})=0\), \(b(\mathrm{NW})=1\), \(b(\mathrm{SE})=2\), and \(b(\mathrm{NE})=3\). Define \(M(\pi)=\{m(x):x\in\pi\}\). Empty quadrants have zero bits, and an element equal to \(x\) occupies none of its quadrants.

## Proof
**Step 1 (exact two-round types).** In a two-move Ehrenfeucht--Fraïssé game, after the first choice \(x\), the second choice can be equal to \(x\), or can lie in precisely one of the four quadrants. Thus two choices \(x,x'\) permit the same second-round atomic relations if and only if they have the same mask. Duplicator wins from the empty position precisely when every point-mask of either structure is realized in the other structure. This is exactly equality of the sets \(M\). By the Ehrenfeucht--Fraïssé characterization, it is equivalent to agreement on all rank-two sentences. For a direct logical witness of a mask \(s\), define \(Q_s(x)\) to assert, for each of the four quadrants, existence or nonexistence of a point in it according to \(s\). Each \(Q_s\) has rank at most one, and \(\exists x\,Q_s(x)\) has rank at most two. Thus differing mask sets can be distinguished directly.

**Step 2 (generic masks and minimum witness).** Among the sixteen possible four-bit masks, the nine masks in \(M_\star\) are the four adjacent pairs \(3,5,10,12\), four triples \(7,11,13,14\), and full mask \(15\). For the displayed witness, direct quadrant inspection gives mask set exactly \(M_\star\); the embedded checker reconstructs the nine masks individually. Any model with this mask set needs at least one distinct point for each of the nine masks, so nine is a sharp minimum.

**Step 3 (rare nongeneric masks).** Mask zero is impossible for \(n\ge2\). Each one-quadrant mask forces a vertex to be both an endpoint of the positional order and an endpoint of the value order; the union of these four events has probability at most \(4/n\). For masks \(9\) or \(6\), a vertex at some interior position \(i\) has all preceding values smaller and all subsequent values larger, or the reversed inequality. At each \(i\), either condition has probability exactly \([n\binom{n-1}{i-1}]^{-1}\). Hence \(\Pr\{6\in M\text{ or }9\in M\}\le2a_n\), where \(a_n=O(n^{-2})\): bound the two endpoint terms of \(\sum_{k=1}^{n-2}\binom{n-1}{k}^{-1}\) by \(2/(n-1)\) and its interior terms using \(\binom{n-1}{k}\ge\binom{n-1}{2}\).

**Step 4 (presence of adjacent-pair masks).** The first and last positional elements realize masks \(12\) and \(3\), respectively, unless their values are also global minima or maxima. Likewise the value-minimum and value-maximum elements realize \(10\) and \(5\), respectively, unless they are positional endpoints. A union bound gives probability at most \(8/n\) that at least one of these four masks is missing.

**Step 5 (three-quadrant record masks).** Consider mask \(13\), corresponding to a left-to-right record maximum with a smaller value both before and after it and a larger value after it. Let \(R_n\) be the number of left-to-right record maxima of a uniform permutation. The first record cannot realize mask \(13\); the last record is the global maximum and also cannot realize it. Hence \(R_n\le2\) implies that mask \(13\) is absent. If \(R_n\ge3\), the second record has a smaller earlier element and a larger later element. It fails to realize mask \(13\) only if no later element has smaller value: then its earlier values are all smaller, and all its later values are larger. This is one of the direct-sum pivot events counted by \(a_n\). Consequently
\[
\Pr(R_n\le2)\le\Pr(13\notin M)\le\Pr(R_n\le2)+a_n.
\]
The record count has the law of a sum of independent Bernoulli indicators with success probabilities \(1,1/2,\ldots,1/n\), so \(\Pr(R_n\le2)=(1+H_{n-1})/n\) exactly. Reflecting the permutation diagram in horizontal or vertical axes, and transposing it, preserves the uniform distribution and exchanges the four triple masks. Therefore the same bound holds for each of \(7,11,13,14\).

**Step 6 (presence of the full mask).** Fix the element at positional index \(i=\lfloor n/2\rfloor\). Conditional on its value rank \(j\), the set of the other \(j-1\) smaller values is a uniform subset of the other positions. The probability that a prescribed positional side contains none of them is at most \(\rho^{j-1}\), with \(\rho=\max\{i-1,n-i\}/(n-1)\le3/4\) for \(n\ge4\). The analogous bound for larger values is \(\rho^{n-j}\). Averaging the uniformly distributed \(j\) and applying a union bound over four quadrants shows \(\Pr(15\notin M)\le16/n\).

**Step 7 (sharp stabilization).** Steps 3--6 and a union bound give the stated upper bound \((4H_{n-1}+32)/n+6a_n\), while Step 5 gives the lower bound \((1+H_{n-1})/n\). Since \(H_{n-1}\sim\log n\), both bounds are of the asserted sharp order. The exact rank-two profile in Step 1 and the nine-point witness imply the zero-one law at rank two and the minimum representative.

**Step 8 (rank-three optimality).** Write \(\operatorname{Succ}_P(x,y)\) for \(x<_Py\) and absence of a positional intermediate point, and similarly \(\operatorname{Succ}_V(x,y)\). Then \(\exists x\exists y\,(\operatorname{Succ}_P(x,y)\wedge\operatorname{Succ}_V(x,y))\) has quantifier rank three. It asserts that a consecutive increasing pair of values occurs in consecutive positions. Let \(X_n\) count such pairs. For every fixed \(r\ge1\), imposing any specified \(r\) edges among the \(n-1\) possible directed value adjacencies glues those edges into consistently oriented runs, leaving \((n-r)!\) permutations. Thus \(\mathbb E(X_n)_r=(n-1)_r/(n)_r\to1\). The factorial-moment criterion yields \(X_n\Rightarrow\operatorname{Pois}(1)\), and the displayed rank-three sentence has limit \(1-e^{-1}\), neither zero nor one. The Poisson succession law itself is classical; the contribution of the finding is the exact rank-two type and its sharp finite-size stabilization.

## Verification
The accompanying standalone Python 3 file `checker.py` enumerates all permutations of sizes one through eight. It independently constructs two-move quadrant signatures, checks agreement with direct bitmasks, verifies the exact record-count identity and the direct-sum-pivot upper bound for the absence of mask \(13\), and confirms the nine-point representative. Its final output is `ALL_FINITE_CHECKS_OK`. The exhaustive finite checks are not used as a substitute for the proofs of the infinite bounds and Poisson limit, which are given above.

## Relationship to prior work
Foy and Woods (1990) initiated asymptotic probability questions for pairs of linear orders and established nonconvergence at unrestricted first-order depth. Albert, Bouvel and Féray (2020) developed the two-order permutation language and its expressibility. Falgas-Ravry, Markström, Räty and Skerman (2026) studied full first-order limit laws in proper small permutation classes, proving quantitative laws in polynomial-growth classes and density of the limiting spectrum in exponential-growth classes. Those statements do not give the finite-rank classification, nine-point representative, or logarithmic-over-linear stabilization rate for uniform permutations from the entire symmetric group. The generic countable homogeneous two-order structure and elementary record-count facts are background, not themselves claimed as new.

## Limitations
The theorem concerns ordinary quantifier rank at most two, with an explicit rank-three counterexample; it does not assert a limit law for unrestricted first-order logic or for signatures containing primitive successor symbols. Its novelty assessment is limited by the unavailable full text of Foy and Woods (1990), an especially relevant historical source, and potential equivalent earlier classifications. Its complete manuscript was not accessible through the available routes; this source was not classified as noncovering based on its abstract. The proof and finite checker have not undergone an independent mathematical audit.

## References
- V. Falgas-Ravry, K. Markström, E. Räty and F. Skerman, *On first-order limiting probabilities for small permutation classes*, arXiv:2610.34328 (first public 2026-10-25), https://arxiv.org/abs/2610.34328.
- M. Albert, M. Bouvel and V. Féray, *Two first-order logics of permutations*, Journal of Combinatorial Theory A 171 (2020), 105158, https://doi.org/10.1016/j.jcta.2019.105158.
- J. Foy and A. R. Woods, *Probabilities of sentences about two linear orderings*, in *Feasible Mathematics*, 1990, pp. 181--193, https://doi.org/10.1007/978-1-4612-3466-1_10.
- J. Linman and M. Pinsker, *Permutations on the random permutation*, arXiv:1405.4297 (2014), https://arxiv.org/abs/1405.4297.
