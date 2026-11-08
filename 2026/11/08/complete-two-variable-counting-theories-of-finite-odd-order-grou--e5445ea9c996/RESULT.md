# Complete two-variable counting theories of finite odd-order groups in relational multiplication

## Finding

For a finite group \(G\), let \(\mathcal R(G)=(G;e,R)\) be the structure with named identity \(e\), equality, and a **ternary relation**, not a multiplication function, with \(R(a,b,c)\) meaning \(ab=c\). Let \(\mathrm C^2\) be two-variable first-order logic with exact counting quantifiers and unbounded quantifier depth. For odd-order groups define
\[
\tau_3(G)=|\{g\in G\setminus\{e\}:g^3=e\}|.
\]

**Theorem.** For **all** finite groups \(G,H\) of odd order, including the trivial group,
\[
\mathcal R(G)\equiv_{\mathrm C^2}\mathcal R(H)
\quad\Longleftrightarrow\quad
(|G|,\tau_3(G))=(|H|,\tau_3(H)).
\]
This is equivalence of complete unrestricted-depth theories within the stated class, not finite-quantifier-rank equivalence or equivalence in a functional group signature.

For example, \(C_{25}\) and \(C_5\times C_5\) are nonisomorphic but \(\mathrm C^2\)-equivalent in this language; both have \((|G|,\tau_3(G))=(25,0)\). The elementary abelian group \(C_3^3\) and the nonabelian unitriangular group \(\mathrm{UT}_3(\mathbb F_3)\) are also equivalent, with \((27,26)\). Three first-order variables suffice to distinguish the latter two through commutativity.

## Assumptions and scope

Every group here is finite, not necessarily abelian, with odd cardinality. The identity is named by a constant. The multiplication graph is a ternary **relation** \(R\), and terms such as \(xy\) are used in the *metamathematical proof*, not as permitted logical terms. The language has no inverse or multiplication function, no order, no extra group-element constants, and no second-order predicates. Counting quantifiers may specify an arbitrary nonnegative integer; exact counting abbreviates a lower bound and the failure of the next lower bound. Only variable names \(x\) and \(y\) may be bound or reused.

Put \(T=\{g\ne e:g^3=e\}\), \(N=G\setminus(T\cup\{e\})\), \(t=|T|\), and \(s=|N|=|G|-1-t\). Empty classes are allowed. These three subsets will be referred to as \(I=\{e\}\), \(T\), and \(N\).

## Proof

**1. Distinguishability of the two invariants.** The counting sentence \(\exists^{=n}x\,(x=x)\) determines \(n=|G|\). The two-variable unary formula
\[
\theta(x):=(x\ne e)\land\exists y\,[R(x,x,y)\land R(x,y,e)]
\]
holds exactly if \(x\ne e\) and \(x^3=e\), so the sentence \(\exists^{=t}x\,\theta(x)\) determines \(t\). Hence logical equivalence implies equality of both invariants.

**2. Odd-order square roots.** If \(|G|\) is odd, every \(x\in G\) has exactly one square root \(\rho(x)\). Indeed, a square root \(y\) of \(x\) has odd order, \(\langle y^2\rangle=\langle y\rangle\), and therefore \(y\in\langle x\rangle\); the unique square root inside the odd cyclic group \(\langle x\rangle\) is \(x^{(\operatorname{ord}(x)+1)/2}\). Likewise the inverse and square of any nonidentity element remain nonidentity and have the same order as that element.

If \(x\in T\), then \(x^2=x^{-1}=\rho(x)\ne x\). If \(x\in N\), the four points
\[
x,\qquad x^2,\qquad x^{-1},\qquad \rho(x)
\]
are all distinct and lie in \(N\): equality of any two of the last three, or equality with \(x\), forces \(x^3=e\) or \(x=e\). This gives \(s\ge4\) whenever \(N\ne\varnothing\).

**3. Every atomic two-variable type is covered by a uniform table.** Fix the first variable \(x\), and let the second variable \(y\) range over \(G\). Two-variable atomic formulas are equalities between \(x,y,e\) and instances of \(R\) with all three arguments selected from \(x,y,e\). The group laws reduce every such atom, for \(x,y\ne e\) and \(x\ne y\), to the three possible nontrivial conditions
\[
y=x^2,\qquad y=x^{-1},\qquad y^2=x.
\]
All other atoms are fixed by identity/equality cases or have constant truth value. From Step 2 these conditions coincide in exactly one distinct \(y\) if \(x\in T\), and select three distinct elements if \(x\in N\).

Consequently the complete pair-atomic-type inventory for a fixed \(x\) is as follows (the listed cases are mutually exclusive):

- For \(x=e\): one choice \(y=e\); \(t\) choices \(y\in T\); and \(s\) choices \(y\in N\).
- For \(x\in T\): one choice \(y=e\), one \(y=x\), one \(y=x^2=x^{-1}=\rho(x)\), \(t-2\) other choices from \(T\), and \(s\) choices from \(N\).
- For \(x\in N\): one choice \(y=e\), one \(y=x\), one choice each for \(y=x^2\), \(y=x^{-1}\), and \(y=\rho(x)\), \(s-4\) other choices from \(N\), and \(t\) choices from \(T\).

The exceptional choices inside a row have the same complete atomic type for any two groups of odd order, and all remaining choices have the same generic type. Thus for each stationary class, every target class and **every** complete two-variable atomic type, the number of available targets depends solely on \((n,t)\). Note that this assertion includes the relation in both argument orders; no commutativity assumption is made.

**4. Induction over all counting formulas.** Maintain the following assertion for every formula using only \(x,y\): its truth on an assignment of its free variables is determined by the unary classes \(I,T,N\) and the complete atomic two-variable type, with identical determination in all odd-order groups having the same pair \((n,t)\). Atomic formulas satisfy the assertion by Step 3; Boolean connectives preserve it. If one variable is counted or quantified, at most the other variable stays free. For any stationary value, Step 3 gives the exact number of values of the counted variable in each unary class and each atomic-pair-type case, so the number making the subformula true depends only on the stationary class and \((n,t)\). The resulting formula again has the asserted uniform truth behavior. Sentences are covered as the zero-free-variable case. This proves the reverse implication without any bound on nesting depth or counting thresholds.

The groups with \(|G|=1\) are identical, and their empty nonidentity classes cause no exception. The theorem follows.

## Verification

The standalone standard-library program `verify.py` builds multiplication tables for thirteen concrete odd-order groups, validates the group axioms for each table, verifies the exact square/inverse/square-root pair-atomic profiles, and compares two-variable counting refinement signatures on five representative pairs. The samples include both positive and negative equivalence cases, abelian/nonabelian groups and orders \(3,5,7,9,21,25,27\). Run `python verify.py` from the extracted package directory; expected output is in `verification_output.txt` and ends with `VERIFY_OK 13 finite_groups`.

The **infinite** result rests on the full atomic-type classification and formula induction above. The computation is corroboration only; it does not quantify over arbitrary groups or infinitely many formulas.

## Relationship to prior work

Kopczyński and Tan [1] characterize models and cardinality spectra of two-variable counting logic through regular and biregular graph constraints. Kiefer, Schweitzer and Selman [2, §2, §5] develop complete two-variable atomic-type invariants and identification theory for arbitrary finite relational structures. These are foundational, substantially broader frameworks; the present statement isolates the explicit *group-relative* two-integer complete invariant using the odd-order unique-square-root property. Neither inspected text reports this exact odd-group equivalence criterion.

Bova and Martin [3, §2] study first-order queries on finite **abelian** groups in a **functional** vocabulary with additive and inverse terms, so their model-checking theorem does not imply the present collapse in the weaker relational language. Existing counting-free finite-group classifications use a different logic and are not the same theorem. No exhaustive historical-priority claim is made.

## Limitations

The result is restricted to odd-order finite groups and a ternary relational multiplication signature. It does not characterize even-order groups, counting logic in a language with multiplication or inverse as function symbols, or \(\mathrm C^3\) and higher logics. The data \((|G|,\tau_3(G))\) do not determine group isomorphism. In a functional signature, a single-variable term can express arbitrary fixed powers, so the conclusion cannot simply be transferred. Independent mathematical review has not been carried out; historical precedence beyond the inspected sources remains a risk.

## References

[1] E. Kopczyński and T. Tan, *Regular graphs and the spectra of two-variable logic with counting*, arXiv:1304.0829, first made public 2013-04-03; reviewed manuscript version 4 (2014-06-11), especially introduction and §§1–2. https://arxiv.org/abs/1304.0829

[2] S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first made public 2015-03-30, especially pp. 5–6 and §5. https://arxiv.org/abs/1503.08792

[3] S. Bova and B. Martin, *First-Order Queries on Finite Abelian Groups*, CSL 2015, DOI:10.4230/LIPIcs.CSL.2015.41, especially pp. 41–44, first published 2015-09-07. https://doi.org/10.4230/LIPIcs.CSL.2015.41
