# Two-variable logical rigidity of finite rectangular distributive lattices

## Finding
Let \(C_m\) denote the \(m\)-element chain for a positive integer \(m\). Equip the Cartesian product \(P_{m,n}=C_m\times C_n\) with its coordinatewise reflexive order \(\leq\). The first-order signature consists of this **one binary relation** and equality; neither chain coordinate, minimum, maximum, meet, join, nor a counting operation is named.

**Theorem.** For every four positive integers \(m,n,p,q\),
\[
P_{m,n}\equiv_{\mathrm{FO}^{2}}P_{p,q}
\quad\Longleftrightarrow\quad
\{m,n\}=\{p,q\}\text{ as multisets}.
\]
Here \(\mathrm{FO}^{2}\) uses at most two reusable variables, with arbitrarily nested quantifiers and no counting quantifiers. Thus the unrestricted two-variable theory identifies every member of this natural infinite family up to isomorphism. One-variable logic identifies none of them: every nonempty \(P_{m,n}\) has the same \(\mathrm{FO}^{1}\) theory.

A more explicit invariant reconstructs the two factors. Let \(h\) be the maximum number of strict comparabilities on a chain below a point (equivalently, the rank of the maximum). If the poset has no incomparable pair, it is \(P_{1,h+1}\). Otherwise, let \(s\) be the largest rank of a point incomparable with *some rank-one point*. Then
\[
\{m,n\}=\{h-s+1,\ s+1\}.
\]
Both \(h\) and \(s\) are recoverable through families of actual two-variable sentences. In particular, nonisomorphic rectangles admit explicit distinguishing sentences of quantifier rank at most \(\max(m+n-2,p+q-2)+3\).

## Assumptions and scope
All chain lengths are positive and finite. Use the strict abbreviation \(x<y\) for \(x\leq y\wedge x\ne y\), and \(I(x,y)\) for \(x\ne y\wedge\neg(x<y)\wedge\neg(y<x)\). These abbreviations contain only the variables \(x,y\).

The equivalence is **relative to rectangular products of two chains**. The result does not characterize which arbitrary finite posets satisfy the same two-variable theory as a rectangle, nor does it assert unrestricted two-variable identification of every finite distributive lattice or of products with three or more factors.

## Proof
**Step 1: Two-variable rank formulas.** For \(z\in\{x,y\}\), define \(H_0(z)\) as \(z=z\). Define \(H_{t+1}(x)\) recursively by \(\exists y\,(y<x\wedge H_t(y))\), and \(H_{t+1}(y)\) by \(\exists x\,(x<y\wedge H_t(x))\). Inner quantifiers rebind the other variable, so there are never more than two distinct variable symbols. Let \(R_t(z)=H_t(z)\wedge\neg H_{t+1}(z)\). In a finite poset, \(H_t(z)\) says that a strict descending chain of length \(t\) begins at \(z\); consequently \(R_t\) says that its maximum downward chain length is exactly \(t\). In \(P_{m,n}\) the rank of \((i,j)\), with zero-based coordinates, is exactly \(i+j\). In particular, the maximum rank is \(h=m+n-2\), and the elements satisfying \(R_1\) are precisely \((1,0)\) when \(m\geq2\), and \((0,1)\) when \(n\geq2\).

**Step 2: The atom-incomparability spectrum.** For each integer \(t\geq1\), consider the two-variable sentence
\[
E_t:=\exists x\,\exists y\,\bigl(R_1(x)\wedge I(x,y)\wedge R_t(y)\bigr).
\]
Suppose first \(m,n\geq2\). A point \((i,j)\) is incomparable with \((1,0)\) precisely when \(i=0\) and \(j\geq1\). Its possible ranks are therefore exactly \(1,\ldots,n-1\). Symmetrically, points incomparable with \((0,1)\) have ranks exactly \(1,\ldots,m-1\). Consequently,
\[
\{t\geq1:P_{m,n}\models E_t\}
=\{1,2,\ldots,\max(m,n)-1\}.
\]
If \(\min(m,n)=1\), the product is a chain, so every \(E_t\) is false and no incomparable pair exists.

**Step 3: Reconstruction.** The two-variable sentences \(\exists x\,H_t(x)\) identify the largest possible \(t\), namely \(h\). The two-variable sentence \(\exists x\,\exists y\,I(x,y)\) distinguishes chains from nonchains. For a chain the unordered pair is \(\{1,h+1\}\). For a nonchain, Step 2 identifies the largest true \(E_t\) index \(s=\max(m,n)-1\), hence its larger factor is \(s+1\), and the smaller is \(h-s+1\). Therefore two rectangular products with the same unrestricted \(\mathrm{FO}^{2}\) theory must have the same unordered factor sizes. Conversely, equal unordered factor sizes yield an order isomorphism, so the structures satisfy the same formulas.

**Step 4: Variable-width and quantifier-rank bounds.** A formula in the one-variable fragment uses only atomic \(x=x\) and \(x\leq x\), both true on every nonempty poset; by induction on syntax, all nonempty rectangles have the same one-variable sentences. Two variables are therefore the minimum uniform number of variables needed for identification within this family.

The recursion gives quantifier rank \(t\) to \(H_t\) and at most \(t+1\) to \(R_t\). The maximum-rank sentences distinguish different \(h\) with rank at most \(\max(h,h')+2\). A two-variable incomparability sentence separates chains and nonchains with rank two. If two nonchains share \(h\) but have different larger factors, choose \(t\) equal to the smaller of their two larger-factor sizes: \(E_t\) holds in exactly the rectangle with larger factor larger than \(t\). Its quantifier rank is at most \(t+3\leq h+3\). This proves the displayed uniform upper bound. No optimality assertion is made for that depth bound.

## Verification
The standalone \(\texttt{verify\_rectangle\_invariants.py}\) enumerates all 324 **ordered** rectangular parameter pairs with \(1\leq m,n\leq18\), directly calculates down-rank and every incomparable pair, and checks the formula for the exact atom-incomparability spectrum, the maximum incomparable rank gap, and reconstruction of both factors. It examined 1,877,922 ordered incomparable pairs and passed every assertion.

An independently written \(\texttt{verify\_fo2\_types.py}\) simultaneously refines the set-valued two-variable first-order types of all 45 isomorphism classes with \(1\leq m\leq n\leq9\). The numbers of distinct theories after rounds one through six are \(4,8,17,32,44,45\); all 45 are separated by round six. Its set-valued update checks **ordinary** two-variable logic rather than counting logic. The embedded text outputs are exact captured executions. These finite experiments corroborate but do not replace the symbolic proof for arbitrary positive dimensions.

Run with a standard Python 3 interpreter:

```text
python3 verify_rectangle_invariants.py
python3 verify_fo2_types.py
```

No third-party packages or external files are required.

## Relationship to prior work
Schwentick and Zeume, *Two-Variable Logic with Two Order Relations* (2012; public preprint 2011), determine finite-satisfiability complexity in substantially richer order signatures, not exact unrestricted two-variable equivalence in the single coordinatewise partial-order signature of the present theorem. Manuel and Zeume, *Two-Variable Logic on 2-Dimensional Structures* (2013), study two-order/successor signatures, data words and satisfiability boundaries, rather than recovering the factor lengths of an unlabeled rectangular poset. Those results supply logical context but do not entail the stated identification invariant.

Classical theory of finite distributive lattices identifies products of chains as natural examples, but standard order-isomorphism classification is a different problem from logical identification with two reusable variables and no named coordinates. The proof here uses the rank spectrum of points incomparable with rank-one elements, not the availability of lattice operations or arbitrary-variable formulas. The literature search did not establish historical priority; a more general model-theoretic identification theorem not retrieved here might imply this special case.

## Limitations
The theorem does not prove that two variables characterize any rectangle among **all** finite posets, that this method reconstructs the individual factor multiplicities for products of three or more chains, or that the depth bound is sharp. The verification is exhaustive only for its stated finite ranges and is not an infinite proof. Search and access limitations leave a residual risk of stronger earlier coverage; no independent audit has been performed.

## References
1. Thomas Schwentick and Thomas Zeume, *Two-Variable Logic with Two Order Relations*, arXiv:1110.1439, first public version 2011-10-07; *Logical Methods in Computer Science* 8(1:15), 2012, DOI:10.2168/LMCS-8(1:15)2012. https://arxiv.org/abs/1110.1439
2. Amaldev Manuel and Thomas Zeume, *Two-Variable Logic on 2-Dimensional Structures*, *Computer Science Logic 2013*, pp. 484–499, DOI:10.4230/LIPIcs.CSL.2013.484. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2013.484
3. Nathalie Caspard, Bruno Leclerc and Bernard Monjardet, *Finite Ordered Sets*, Chapter 5, *Ordered Sets and Distributive Lattices*, Cambridge University Press, online 2012-02-05. https://doi.org/10.1017/CBO9781139005135
