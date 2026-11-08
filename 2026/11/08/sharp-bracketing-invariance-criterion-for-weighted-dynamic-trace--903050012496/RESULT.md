# Sharp bracketing-invariance criterion for weighted dynamic traces of symmetric three-valued choice

## Finding

Let \(V=\{0,1,k\}\). In the three-valued nondeterministic disjunction of Aldini–Graziani–Mezzina–Vergottini, the only nonsingleton cells are \(1\mathbin{\widetilde\lor}k=k\mathbin{\widetilde\lor}1=\{1,k\}\); the other cells are \(0\mathbin{\widetilde\lor}0=\{0\}\), \(0\mathbin{\widetilde\lor}1=\{1\}\), \(0\mathbin{\widetilde\lor}k=\{k\}\), \(1\mathbin{\widetilde\lor}1=\{1\}\), and \(k\mathbin{\widetilde\lor}k=\{k\}\).

For each integer \(n\ge1\), take any ordered full binary tree \(T\) with \(n\) distinct variables at the leaves, every internal vertex labeled by \(\widetilde\lor\). A *dynamic evaluation trace* assigns each leaf a value from \(V\) and every internal vertex one of the allowed outputs of its two child values. Give each trace weight \(a^{n_0}b^{n_1}c^{n_k}\), where \(n_0,n_1,n_k\) are the numbers of leaves assigned \(0,1,k\). Let \(Z_T(a,b,c)\) be the sum of the weights over all traces, including all root outputs. The weights \(a,b,c\) are arbitrary nonnegative real numbers.

**Theorem.** The quantity \(Z_T(a,b,c)\) is independent of the binary bracketing \(T\), simultaneously for every \(n\ge1\), **if and only if** \(b=c\) or \(bc=0\). If \(b=c=t\), the complete root-value trace vector, for every bracketing, is
\[
\left(a^n,\frac{(a+3t)^n-a^n}{3},\frac{(a+3t)^n-a^n}{3}\right),
\]
and consequently
\[
Z_T(a,t,t)=\frac{a^n+2(a+3t)^n}{3}.
\]
If \(bc=0\), then \(Z_T(a,b,c)=(a+b+c)^n\) for every bracketing. Otherwise, bracketing dependence begins **exactly at four leaves**. For the left comb \(T_\ell=(((p\widetilde\lor q)\widetilde\lor r)\widetilde\lor s)\) and balanced tree \(T_\mathrm{bal}=((p\widetilde\lor q)\widetilde\lor(r\widetilde\lor s))\),
\[
Z_{T_\ell}(a,b,c)-Z_{T_\mathrm{bal}}(a,b,c)=bc(b-c)^2>0
\]
whenever \(b,c>0\) and \(b\ne c\). The four-leaf defect is independent of \(a\).

In particular, with unit weights \(a=b=c=1\), all bracketings have exactly \((2\cdot4^n+1)/3\) dynamic traces, split into root-value counts \(1,(4^n-1)/3,(4^n-1)/3\). Despite this numerical bracketing sensitivity at unequal weights, the underlying set-valued disjunction is associative as a *hyperoperation* (its reachable root-value sets are bracketing-independent).

## Assumptions and scope

The leaves of each tree are **distinct propositional variables**; hence all its non-leaf subformulas are syntactically distinct. Each internal output is selected independently in the *dynamic* Nmatrix semantics. A trace records the value at every vertex, not merely its final root value. The three weights apply only to leaf assignments, not internal resolutions. Zero weights are permitted. The theorem concerns all finite full binary trees and all positive integers \(n\); it makes no assertion for static valuations, repeated identical subformulas, general acyclic sharing, negations, or any other connective.

## Proof

**1. Trace convolution.** For a subtree \(A\), denote its root-value weight-sum vector by \(u(A)=(u_0,u_1,u_k)\). A leaf contributes \(x=(a,b,c)\). From the displayed six cells of the Nmatrix, the vector for the join of two subtrees is \(u\star v\), with
\[
\begin{split}
(u\star v)_0&=u_0v_0,\\
(u\star v)_1&=u_0v_1+u_1v_0+u_1v_1+u_1v_k+u_kv_1,\\
(u\star v)_k&=u_0v_k+u_kv_0+u_kv_k+u_1v_k+u_kv_1.
\end{split}
\]
Each product counts a pair of child traces and each allowed output contributes one separate parent trace. Distinct subformulas ensure these choices are independent. Thus the convolution is an exact enumeration, not an approximation.

**2. General associator.** Expanding the three displayed polynomials gives, for any three real root-count vectors \(u,v,w\),
\[
(u\star v)\star w-u\star(v\star w)
=\left(0,-v_1\Delta,v_k\Delta\right),
\qquad \Delta=u_1w_k-u_kw_1.
\]
The ordinary hyperoperation is instead set-associative: deleting zeros, a list of inputs consisting only of \(1\)'s has reachable output \(\{1\}\), only \(k\)'s has \(\{k\}\), and any list containing both has reachable outputs \(\{1,k\}\). This can also be checked directly in all \(27\) ordered triples. The difference concerns multiplicities of resolution histories, not possible outcomes.

**3. Sufficiency when \(b=c\).** The plane \(u_1=u_k\) is closed under \(\star\). Write a symmetric vector as \((r,s,s)\) and another as \((R,S,S)\). Their product is
\[
(rR,\ rS+sR+3sS,\ rS+sR+3sS).
\]
The coordinates \(r\) and \(r+3s\) therefore multiply separately. By induction on the tree, starting with leaf vector \((a,t,t)\), one obtains \(r=a^n\) and \(r+3s=(a+3t)^n\) at every root. Solving for \(s\) proves the root-vector and total formulas without restricting the tree shape.

**4. Sufficiency when \(bc=0\).** If either \(b=0\) or \(c=0\), only \(\{0,k\}\) or \(\{0,1\}\), respectively, has positive leaf weight. On each of these two sets the connective is deterministic and behaves as maximum in the displayed order with \(0\) least. Every positive-weight leaf assignment thus has exactly one trace, of weight the product of its leaf weights. The binomial expansion yields \((a+b+c)^n\), independently of bracketing. (At zero total weight the formula remains valid.)

**5. Necessity and smallest obstruction.** Put \(x=(a,b,c)\) and \(p=x\star x\). Its two nonzero-outcome coordinates are
\[
p_1=2ab+b^2+2bc,\qquad p_k=2ac+c^2+2bc,
\]
so \(p_1c-p_kb=-bc(b-c)\). Apply the associator in step 2 with \(u=p\), \(v=w=x\). Its sum of three coordinates is
\[
(b-c)(p_kb-p_1c)=bc(b-c)^2.
\]
The left side is exactly \(Z_{T_\ell}-Z_{T_\mathrm{bal}}\), since \(p=x\star x\) and \(\star\) is commutative. It is positive whenever \(b,c>0\) and \(b\ne c\); hence all-size bracketing invariance requires \(b=c\) or \(bc=0\). For fewer than four leaves, the only distinct three-leaf shapes are \((x\star x)\star x\) and \(x\star(x\star x)\), equal by commutativity; one- and two-leaf shapes are unique. This proves sharpness at four leaves.

## Verification

Run the standalone standard-library program `nmatrix_trace_checker.py` with Python 3. It directly enumerates all legal internal node choices for every plane full-binary shape with up to five leaves, compares all root counts with the formula, tests every shape up to seven leaves for equal weights and one-supported-boundary weights, and independently checks the four-leaf polynomial on a \(5\times5\times5\) integer weight grid. It also verifies the associator identity on \(3^9=19683\) triples of nonnegative small vectors and set-valued associativity on all \(27\) truth-value triples. Its reported total is `All checks passed: 29537`. These are finite tests corroborating the independent polynomial proof, not substitutes for the unrestricted result.

## Relationship to prior work

Aldini, Graziani, Mezzina, and Vergottini introduced the symmetric three-valued choice Nmatrix and proved soundness/completeness of associated dynamic and static sequent calculi. Their subsequent five-valued *deterministic* refinement has an associative disjunction (their Lemma 1), but that result concerns a different carrier and an ordinary function. No formula for weighted counts of independently resolved three-valued dynamic histories, nor the sharp criterion for shape invariance of those counts, occurs in the inspected text. The Nmatrix and dynamic valuation notions are prior work; the explicit combinatorial invariant and its classification are the contribution here. General frameworks for Nmatrices (Avron–Lev) do not by themselves state a shape-sensitive weighted counting theorem for this specific operation. The possibility of equivalent results in other weighted-hyperalgebra terminology remains open for historical attribution.

## Limitations

The result is a mathematical count of valuation histories, not a probability distribution on actual machine executions without a specified scheduler. Normalized nonnegative weights are allowed but not required. The result does not characterize all trace-count distributions for arbitrary unequal weights at arbitrary tree shapes, nor does it characterize static valuations or formulas with repeated subformulas. Bibliographic searches are not a proof of historical uniqueness; independent validation has not been performed.

## References

1. Alessandro Aldini, Pierluigi Graziani, Claudio Antares Mezzina, and Gandolfo Vergottini, *A Logical 3-valued Semantics for Nondeterministic Choice* (first publicly available July 22, 2026), arXiv:2607.20178, https://arxiv.org/abs/2607.20178; EPTCS 449 (2026), pp. 1–17, DOI 10.4204/EPTCS.449.1.
2. Arnon Avron and Iddo Lev, *Non-deterministic Multiple-valued Structures*, Journal of Logic and Computation 15 (2005), 241–261, DOI 10.1093/logcom/exi001 (general Nmatrix framework).
3. Arnon Avron and Beata Konikowska, *Proof Systems for Reasoning about Computation Errors*, Studia Logica 91 (2009), 273–293, DOI 10.1007/S11225-009-9175-4 (earlier Kleene–McCarthy Nmatrix, not the symmetric operation used here).
