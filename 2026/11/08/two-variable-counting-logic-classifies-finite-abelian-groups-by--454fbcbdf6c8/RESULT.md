# Two-variable counting logic classifies finite abelian groups by their 2-primary part and cubic torsion

## Finding

**Theorem.** For all finite abelian groups \(G,H\), including the trivial group, represent multiplication only by the ternary relation \(R(x,y,z)\iff xy=z\) and name the identity by a constant \(e\). Let \(P_G\) be the Sylow-2 subgroup; let \(O_G\) be the complementary odd-order subgroup; and put \(G[3]=\{g\in G:g^3=e\}\). With arbitrarily nested counting quantifiers and precisely two reusable variable names,
\[
G\equiv_{C^2}H\quad\Longleftrightarrow\quad
P_G\cong P_H,\qquad |O_G|=|O_H|,\qquad |G[3]|=|H[3]|.
\]
In particular, \(C_2\times C_{25}\equiv_{C^2} C_2\times C_5^2\), although these groups are nonisomorphic, whereas all finite abelian 2-groups are distinguished up to isomorphism by \(C^2\).

## Assumptions and scope

The structures are **finite abelian groups** in the **relational**, not functional, language \((e,R)\) with equality and the single ternary predicate \(R(a,b,c)\iff ab=c\). No order predicate, parameters, additional constants, inverse or multiplication functions are present. The identity constant is named. The logic \(C^2\) allows arbitrary finite counting thresholds and unbounded quantifier rank, but only variables \(x,y\). The direct factors \(P_G,O_G\) are canonical for finite abelian groups. The three invariants displayed in the theorem are mathematical data, not additional symbols in the language.

## Proof

**Necessity.** The group cardinality is expressed using counting quantifiers. The formula
\[
\vartheta_3(x):=\exists y\bigl(R(x,x,y)\wedge R(x,y,e)\bigr)
\]
holds precisely when \(x^3=e\). Consequently \(|G[3]|\) is a \(C^2\)-invariant. Define \(\vartheta_0(x)\) to be \(x=e\), and recursively define \(\vartheta_{k+1}(x)\) to be \(\exists y(R(x,x,y)\wedge\vartheta_k(y))\), with the bound name in \(\vartheta_k\) changed as necessary to keep only \(x,y\). Induction shows \(\vartheta_k(x)\iff x^{2^k}=e\). Thus the sizes \(|G[2^k]|\) are \(C^2\)-invariants for all \(k\ge0\). For finite abelian groups, these sizes uniquely determine the multiset of cyclic 2-power factors: if \(P_G\cong\prod_i C_{2^{\lambda_i}}\), then \(\log_2|G[2^k]|=\sum_i\min(k,\lambda_i)\), whose consecutive differences recover the numbers of factors of length at least \(k\). Hence \(P_G\cong P_H\). The total size divided by \(|P_G|\) determines \(|O_G|\).

**Sufficiency.** Suppose these three invariants agree. Use an isomorphism to identify \(P_G=P_H=P\). Write \(G=P\times O\) and \(H=P\times O'\). Partition the odd components into the three categories
\[
T_0=\{e\},\qquad T_3=\{u\ne e:u^3=e\},\qquad T_*=\{u:u^3\ne e\}.
\]
Their cardinalities agree between \(O\) and \(O'\), because \(|O|=|O'|\) and \(|O[3]|=|O'[3]|\). For every fixed \(a\in P\) and category \(T\), form the vertex class \(\{a\}\times T\); classes with empty categories are omitted. Matching classes have the same cardinality.

Consider a fixed \(x=(a,u)\) in such a class and a potential target \(y=(b,v)\) in another. Every atomic formula built from \(R,e,=\) using only \(x,y\) is determined by unary identity/square-to-identity tests, equality, and these three binary tests:
\[
y=x^2,\qquad x=y^2,\qquad y=x^{-1}.
\]
For example, \(R(x,x,y)\), \(R(y,y,x)\), and \(R(x,y,e)\) express those tests. The remaining substitutions of \(e,x,y\) into \(R\) reduce to these, identity conditions or tautologies because the operation is a group operation.

Squaring is a bijection of every finite odd-order abelian group. For a fixed odd element \(u\), the only possible odd coordinates \(v\) satisfying the three displayed tests are respectively \(u^2\), the unique square root \(u^{1/2}\), and \(u^{-1}\). All three belong to the same category as \(u\). When \(u=e\), all coincide with \(u\). When \(u\in T_3\), all coincide with \(u^{-1}\ne u\). When \(u\in T_*\), all three are distinct from one another and from \(u\): any equality would imply \(u^3=e\), and an equality with \(u\) would imply \(u=e\). Hence the complete incidence multiplicity of every possible atomic two-variable type from \(x\) into \(\{b\}\times T'\) depends only on \(a,b,T,T'\), the multiplication table of \(P\), and the category sizes, not on the finer group structure of \(O\). Equality \(x=y\) contributes precisely one target when \(a=b\), also uniformly; unary tests are uniform on each class.

The corresponding partitions of \(G\) and \(H\) therefore have identical class sizes and identical refined two-variable atomic-type counts between each pair of classes. An induction on the formation of \(C^2\)-formulas completes the argument: Boolean combinations preserve matching two-variable types, while quantifying one of the two variable names counts elements in each matching class with a specified atomic type and previously determined one-variable truth value. Thus the truth of every one-free-variable formula is constant on matching classes and every sentence has the same truth value in \(G\) and \(H\). This establishes \(G\equiv_{C^2}H\).

## Verification

The standalone standard-library program `verify_abelian_c2.py` enumerates every isomorphism type of finite abelian group of order at most \(128\) by prime-power partitions: \(247\) types overall. It compares all \(351\) pairs of distinct types at the same order against the theorem's three-part invariant, using shared-palette two-variable atomic-type refinement. It also compares all \(27\) ternary-relation substitutions of \(x,y,e\) against the compact atomic signature for groups through order \(36\), and checks examples at larger orders (including \(324\)). Running `python verify_abelian_c2.py` emits `VERIFY_OK`; the exact output is provided in `verify_abelian_c2.out`. These finite checks support the proof but do **not** replace the unrestricted symbolic argument.

## Relationship to prior work

Gomaa's dissertation, *Model Theory and Complexity Theory* (2007), Chapter 3 (especially §§3.1, 3.3, 3.7), uses the same ternary relational group vocabulary but studies first-order distinguishing resources, giving general five-variable upper bounds for nonisomorphic finite abelian groups; it does not state this exact two-variable counting classification. Kiefer, Schweitzer and Selman (2015), §2.1 and §5, develop general \(C^2\) equivalence/refinement methods for finite relational structures, not this group-specific decomposition. Kopczyński and Tan (2013), §§1 and 5–6, establish a general model-theoretic and graph-theoretic framework for \(C^2\) and its spectra, rather than the displayed group invariant. The odd-order specialization \(P=\{e\}\) is not presented separately as the distinctive contribution here: the informative extension is the exact interaction with the 2-primary component for even-order abelian groups.

## Limitations

No claim is made for arbitrary nonabelian even-order groups, for signatures in which multiplication is a **function**, or for logics using three or more variable names. The distinction between the relational and functional signatures is essential. The cited general literature does not settle historical priority by itself; unindexed specialized work may contain an equivalent classification. Computational verification reaches finite orders only, while the stated theorem follows from the proof above.

## References

1. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland PhD dissertation (public repository record dated 2007-07-06), Chapter 3, §§3.1, 3.3, 3.7. https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440
2. E. Kopczyński and T. Tan, *Regular graphs and the spectra of two-variable logic with counting*, arXiv:1304.0829 (first posted 2013-04-03), §§1, 5–6. https://arxiv.org/abs/1304.0829
3. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first posted 2015-03-30), §§2.1, 5. https://arxiv.org/abs/1503.08792
4. W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, DOI:10.1142/S0218196710006047 (journal abstract accessible; the earlier dissertation supplies the examined full-text treatment).
