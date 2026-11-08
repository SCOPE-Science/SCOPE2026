# Jordan-profile rigidity on the Witt nilradical and a sharp ambient resonance

## Finding

Let \(p>3\) be prime, let \(k\) be **any** field of characteristic \(p\), and let \(W=\operatorname{Der}_k(k[x]/(x^p))\) be the \(p\)-dimensional rank-one restricted Witt Lie algebra. Its standard positive-degree nilradical is \(\mathfrak n=x^2k[x]/(x^p)\,\partial_x\), of dimension \(p-2\). For every nonzero \(f\partial_x\in\mathfrak n\), let \(i\in\{2,\ldots,p-1\}\) be the smallest exponent with nonzero coefficient in \(f\). Set \(T_f=\operatorname{ad}(f\partial_x)|_{\mathfrak n}\).

For every integer \(r\ge1\), the exact rank of the \(r\)-th power is

\[
\operatorname{rank}(T_f^r)=\max\{0,p-2-r(i-1)\}-\mathbf 1_{\{i+r(i-1)\le p-1\}}.
\]

Consequently, the **entire nilpotent Jordan partition**, not merely the first adjoint rank, depends only on the initial exponent \(i\), not on the leading coefficient or any higher coefficient of \(f\). For \(f=0\), every positive power has rank zero. The Jordan blocks can equivalently be read from the chains with step \(i-1\) in \(\{2,\ldots,p-1\}\setminus\{i\}\), together with one singleton block.

For a finite field \(k=\mathbb F_q\) with \(q\) a power of \(p\), there is exactly one zero element and exactly \((q-1)q^{p-i-1}\) nonzero elements with initial exponent \(i\). Thus the complete labeled Jordan-partition distribution is specified by

\[
\mathcal J_{p,q}=Z_{(1^{p-2})}+\sum_{i=2}^{p-1}(q-1)q^{p-i-1}Z_{\lambda_{p,i}},
\]

where \(Z_\lambda\) is a formal marker for a partition, and \(\lambda_{p,i}\) is uniquely determined by the power ranks above. Terms with identical partitions are **added**, not regarded as separate partition types.

This valuation-rigidity fails sharply if the adjoint operators act on the **full Witt algebra** instead of \(\mathfrak n\). For \(f=x^2\) and \(g=x^2+x^3\), the restricted adjoints on \(\mathfrak n\) have the same partition, but the adjoints on \(W\) have partitions, respectively,

\[
\operatorname{Jtype}(\operatorname{ad}_W(f\partial_x))=\operatorname{sort}(p-3,3),
\qquad
\operatorname{Jtype}(\operatorname{ad}_W(g\partial_x))=(p-1,1).
\]

This distinction occurs over **every** field of characteristic \(p>3\), not just finite fields.

## Assumptions and scope

The Witt algebra uses the ordinary derivation \(\partial_x\) on the truncated polynomial algebra \(k[x]/(x^p)\); it is well-defined because the characteristic is \(p\). The Lie bracket is the usual commutator of derivations. The words "Jordan partition" mean the ordinary linear-algebra Jordan block sizes of the *nilpotent* operator on the specified vector space, over the given field (all blocks have eigenvalue zero, so algebraic closure is unnecessary). The nilradical \(\mathfrak n\) consists of coefficient polynomials divisible by \(x^2\). The field may be imperfect. The finite-field census counts actual labeled elements, not automorphism orbits.

The formula treats all \(r\ge1\) and every possible nonzero initial exponent \(2\le i\le p-1\). Its first-power specialization recovers the known centralizer dimensions in the nilradical. It does **not** assert valuation-rigidity of ambient-Witt Jordan types.

## Proof

**1. Bracket and invariant splitting.** Write \(e_j=x^j\partial_x\), \(0\le j\le p-1\), with any \(e_j=0\) for \(j\ge p\). The defining bracket is

\[
[e_h,e_j]=(j-h)e_{h+j-1}.
\]

Fix \(f=\sum_{h=i}^{p-1}a_hx^h\), \(a_i\ne0\). For \(j\ge2\),

\[
T_f(e_j)=\sum_{h=i}^{p-1}(j-h)a_h e_{h+j-1}.
\]

Define \(U_i=\operatorname{span}_k\{e_j:2\le j\le p-1,\ j\ne i\}\). Since the coefficient of \(e_i\) in \(f\partial_x\) is nonzero, \(\mathfrak n=k(f\partial_x)\oplus U_i\) as vector spaces. Also \(T_f(f\partial_x)=0\). Every exponent in \(T_f(U_i)\) is at least \(i+1\), because the inputs have exponent at least two. Hence \(U_i\) is invariant under \(T_f\). This is the critical splitting: replacing \(e_i\) by the *actual element* \(f\partial_x\) removes the otherwise resonant column.

**2. Powers and nonvanishing leading coefficients.** Put \(s=i-1\). For any \(j\in\{2,\ldots,p-1\}\setminus\{i\}\) and any positive integer \(r\) with \(j+rs\le p-1\), direct induction from the bracket gives

\[
T_f^r(e_j)=a_i^r\!\left(\prod_{t=0}^{r-1}(j+ts-i)\right)e_{j+rs}
+\text{terms of strictly larger exponent}.
\]

No displayed factor vanishes in characteristic \(p\): all intermediate indices lie between \(2\) and \(p-1\); the only possible equality \(j+ts=i\) would require \(j=i,t=0\) or \(j=1,t=1\), both excluded. Moreover, distinct starting indices \(j\) produce distinct leading exponents \(j+rs\), so the surviving vectors are linearly independent. If \(j+rs>p-1\), the degree filtration forces \(T_f^r(e_j)=0\). The vector \(f\partial_x\) is killed already by \(T_f\). Thus the rank of \(T_f^r\) is exactly the number of \(j\in\{2,\ldots,p-1\}\setminus\{i\}\) satisfying \(j+rs\le p-1\). Counting these integers gives the stated formula, including the boundary where the first maximum vanishes.

The ranks of all powers of a nilpotent operator uniquely determine its Jordan partition. Equivalently, their first differences count the blocks of each minimum length. The stated chain description follows from the rank sequence of the step-\(s\) shift on the indices other than \(i\), plus the killed summand \(k(f\partial_x)\).

**3. Finite fields.** At initial exponent \(i\), the coefficient at that degree has \(q-1\) choices and there are \(p-1-i\) freely chosen higher coefficients, yielding \((q-1)q^{p-i-1}\) elements. The zero polynomial contributes one further element. Every element is counted once. This proves the formal Jordan distribution, with collisions of partitions grouped by addition.

**4. Why the ambient Witt space behaves differently.** On \(W\), the adjoint of \(e_2\) sends \(e_j\) to \((j-2)e_{j+1}\). It has the two nonzero chains \(e_0\to e_1\to e_2\) and \(e_3\to e_4\to\cdots\to e_{p-1}\), giving partition \(\operatorname{sort}(3,p-3)\). For \(u=e_2+e_3\), write \(S=\operatorname{ad}_W(u)\); then

\[
S(e_j)=(j-2)e_{j+1}+(j-3)e_{j+2}.
\]

A direct calculation yields \(S^3(e_0)=2e_4+6e_5+3e_6\), with out-of-range terms set to zero. For every \(p>3\), the leading coefficient \(2\) is nonzero. Subsequently the leading term advances one exponent per application with coefficients \(2,3,\ldots,p-4\), all nonzero in characteristic \(p\). It follows that \(S^{p-2}(e_0)\ne0\), while \(S^{p-1}=0\) because the first three applications already raise the initial degree from zero to at least four, and all applications raise degree at least one.

The vectors \(S(e_j)\) for \(j\in\{0,1,3,4,\ldots,p-2\}\) have distinct, nonzero lowest exponents \(1,2,4,5,\ldots,p-1\). Thus \(\operatorname{rank}S\ge p-2\). The two independent vectors \(u\) and \(e_{p-1}\) lie in the kernel, so \(\operatorname{rank}S=p-2\) and \(\dim\ker S=2\). A nilpotent operator on a \(p\)-space with two Jordan blocks and nilpotency index \(p-1\) has partition \((p-1,1)\), completing the ambient counterexample.

## Verification

Run `python3 check.py` from the directory containing this document and the attached source. The checker constructs matrices **directly from the original Witt bracket**, takes powers, and performs finite-field row reduction without using a precomputed Jordan normal form. It exhausts \(\mathbb F_5\), \(\mathbb F_7\), and the quadratic extension \(\mathbb F_{25}\) (implemented with \(\alpha^2=2\)). It separately tests 500 pseudorandom elements for each of \(p=11\) and \(p=13\), and checks the ambient contrast for \(p=5,7,11,13\). All comparisons passed; the exact scientific output is in `check_output.txt`.

Finite exhaustive verification only proves the enumerated cases; general validity comes from the displayed splitting and leading-coefficient argument. The extension-field tests check that no accidental prime-field simplification was used.

## Relationship to prior work

Yao and Chang, *Nilpotent commuting varieties of the Witt algebra* (arXiv:1301.5667v1), Lemma 2.3 and Remark 2.4, already determine **first centralizers** of nilpotent Witt elements, including the restriction to the standard Borel nilradical. Their Theorems 3.6 and 4.3 study irreducible components of commuting-pair varieties. Those results are credited: the \(r=1\) consequence of the present rank formula is not independently new. The present claim concerns **all iterated adjoint powers**, the entire Jordan partition over arbitrary characteristic-\(p\) fields, its exact finite-field distribution and the ambient resonance boundary; none is stated in that inspected text.

Yao and Chang, *Borel subalgebras of the Witt algebra* (arXiv:1212.4349v1), fix the relevant positive Borel and its nilpotent ideal but do not state iterated adjoint Jordan partitions in the inspected material. The 2011 nilpotent-orbit study by Yao and Shu and Yao's 2015 higher commuting-tuple paper are closer broader context. Only public abstracts were accessible for those two, so coverage by their full text remains an explicitly acknowledged priority risk. McNinch's *Adjoint Jordan Blocks* (arXiv:math/0207001) concerns quasisimple algebraic groups of classical/reductive type, not the positive-degree Cartan-type Witt nilradical.

## Limitations

The scope is the standard nilradical of the rank-one restricted Witt algebra for prime \(p>3\). The theorem does not classify Jordan types in arbitrary Witt subalgebras, higher-rank Jacobson–Witt algebras or all nilpotent elements of the full Witt algebra. The ambient statement gives an exact two-element contrast, not a complete ambient Jordan-type census. The originality assessment is provisional because specialized orbit literature unavailable in full could imply part of the claim. No independent mathematical audit is claimed.

## References

1. Yu-Feng Yao and Hao Chang, *Borel subalgebras of the Witt algebra* \(W_1\), arXiv:1212.4349v1, first posted 2012-12-18, especially Sections 2 and 4.
2. Yu-Feng Yao and Hao Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1, first posted 2013-01-23, especially Lemma 2.3, Remark 2.4, and Theorem 4.3; Journal of Pure and Applied Algebra 218 (2014), 1783–1791.
3. Yu-Feng Yao and Bin Shu, *Nilpotent Orbits in the Witt Algebra* \(W_1\), Communications in Algebra 39 (2011), 3232–3241, DOI:10.1080/00927872.2010.501772 (abstract accessible, full-text comparison unresolved).
4. Yu-Feng Yao, *On nilpotent commuting varieties of r-tuples in the Witt algebra*, Journal of Pure and Applied Algebra 219 (2015), 4042–4054, DOI:10.1016/j.jpaa.2015.02.005 (abstract accessible).
5. George J. McNinch, *Adjoint Jordan Blocks*, arXiv:math/0207001, 2002 (different algebraic-group domain).
