# One-sided product-idempotence rank spectra in finite group-labelled transformation monoids

## Finding

Let \(G\) be any finite group of order \(q\ge1\), and let \(n\ge1\). In \(W_n(G)=G\wr\mathcal T_n\), consider ordered pairs of idempotents \((E,H)\) for which the one-sided product \(H\circ E\) is also idempotent; no commutativity is assumed. If \(\operatorname{rk}\) counts free \(G\)-orbits in an image, define
\[
\Phi_{n,G}(X,Y,Z)=\sum_{\substack{E^2=E,\ H^2=H\\(H\circ E)^2=H\circ E}}
 X^{\operatorname{rk}E}Y^{\operatorname{rk}H}Z^{\operatorname{rk}(H\circ E)}.
\]
Then the **complete joint rank polynomial** is
\[
\boxed{\begin{aligned}
\Phi_{n,G}(X,Y,Z)
={}&\sum_{\substack{a,b,c,d\ge0\\a+b+c+d=n\\a+b\ge1,\ a+c\ge1}}
\frac{n!}{a!b!c!d!}
\sum_{\substack{0\le t\le\min(b,c)\\a+t\ge1}}
\binom ct\frac{b!}{(b-t)!}
(a+t)^{b-t}(a+b)^{c-t}\\[-2pt]
&\qquad\cdot((a+b)(a+c))^d
q^{b+c+2d-t}
X^{a+b}Y^{a+c}Z^{a+t}.
\end{aligned}}
\]
In particular, this rank distribution depends on \(G\) **only through its order** \(q\), even if \(G\) is nonabelian. For \(n\ge2\), the one-sided product condition is strictly weaker than commutativity of the two idempotents. At \(n=1\) the two conditions coincide, since there is only one idempotent.

The number of individual idempotents is
\[
I_n(q)=\sum_{r=1}^n\binom nr(rq)^{n-r}.
\]
For fixed \(n\), as \(q\to\infty\) through finite group orders, independent uniform idempotents satisfy
\[
\boxed{\Pr((H\circ E)^2=H\circ E)\longrightarrow\frac1n.}
\]
The finite formula applies at every group order, including \(q=1\).

## Assumptions and scope

Write a group-labelled transformation as \(E=(f,g)\), with a full function \(f:[n]\to[n]\) and labels \(g_i\in G\), acting on the free right \(G\)-set \([n]\times G\) by \((i,v)\mapsto(f(i),g_i v)\). Thus
\[
(H\circ E)(i,v)=(h(f(i)),\,k_{f(i)}g_i v)
\]
for \(H=(h,k)\). Consequently, \(E\) is idempotent precisely if \(f\) is idempotent and \(g_i=1_G\) for every \(i\in\operatorname{im}f\). The ranks are numbers of orbit indices, not cardinalities of the underlying free \(G\)-set. Ordered pairs and their direction of composition are essential. For \(G\) trivial the model reduces to the ordinary full transformation monoid. The exponent notation \(0^0=1\), if it arises in an intermediate combinatorial count, follows the empty-choice convention; the displayed inner sum itself has \(a+t\ge1\).

## Proof

**1. Fix the two image sets.** Let \(R=\operatorname{im}f\), \(S=\operatorname{im}h\) for two idempotent underlying functions. Partition \([n]\) into \(A=R\cap S\), \(B=R\setminus S\), \(C=S\setminus R\), \(D=[n]\setminus(R\cup S)\), with sizes \(a,b,c,d\). Write \(r=a+b\), \(s=a+c\). There are exactly \(n!/(a!b!c!d!)\) such ordered partitions. The functions fix \(R\) and \(S\) pointwise, respectively.

**2. Characterize a base idempotent product.** Since \(p=h\circ f\), its image is \(h(R)=A\cup h(B)\). Let \(T=h(B)\cap C\) and \(t=|T|\). Thus \(\operatorname{im}p=A\cup T\), of size \(a+t\). The condition \(p^2=p\) is equivalent to \(p(x)=x\) for every \(x\in A\cup T\). This holds automatically on \(A\). For every \(x\in T\), it means
\[
f(x)\in B_x:=\{b\in B:h(b)=x\}.
\]
Each \(B_x\) is nonempty by definition of \(T\); these fibers are disjoint. No condition is imposed on \(f(x)\) for \(x\in C\setminus T\), so each has \(r\) choices. For each \(x\in D\), the values \(f(x)\in R\) and \(h(x)\in S\) have \(rs\) choices independently.

**3. Count the constrained maps on \(B\).** Fix a subset \(T\subseteq C\) of size \(t\). Summing over all maps \(h|_B:B\to A\cup T\) with every point of \(T\) hit, and weighting by the number of choices for the constrained \(f|_T\), gives
\[
\sum_{h|_B}\prod_{x\in T}|B_x|=(b)_t(a+t)^{b-t},
\]
where \((b)_t=b!/(b-t)!\). To prove this, mark one preimage \(b_x\in B_x\) for each \(x\in T\). There are \((b)_t\) injections \(x\mapsto b_x\); the remaining \(b-t\) members of \(B\) may each map anywhere in \(A\cup T\). The marking bijectively counts each map with multiplicity \(\prod|B_x|\). There are \(\binom ct\) choices of \(T\). Multiplying by the unconstrained \(r^{c-t}(rs)^d\) gives the base-pair count in a fixed image partition and fixed \(t\).

**4. Count group-label lifts.** For fixed idempotent base maps \(f,h\), the individual idempotence conditions force \(g_i=1_G\) on \(R\) and \(k_i=1_G\) on \(S\), leaving \(q^{(n-r)+(n-s)}\) initially free label pairs. Since the product base map \(p\) is idempotent, its group-labelled product is idempotent precisely when \(k_{f(x)}g_x=1_G\) for all \(x\in A\cup T\). At \(x\in A\) this is automatic. At \(x\in T\), the chosen \(f(x)=b_x\in B\) supplies the single relation \(g_x=k_{b_x}^{-1}\). The points \(b_x\) are pairwise distinct because the nonempty fibers \(B_x\) are disjoint, so these are \(t\) independent relations, with exactly one factor \(q\) removed per relation. In particular, no group commutativity is needed. The number of lifts is exactly
\[
q^{2n-r-s-t}=q^{b+c+2d-t}.
\]
Multiplication of the choices in Steps 1–4 and summation proves the boxed polynomial, including all rank boundaries.

For commuting idempotents, \((H\circ E)^2=H^2\circ E^2=H\circ E\). If \(n\ge2\), take the constant base maps to two distinct indices with all labels equal to \(1_G\). Then \(H\circ E=H\) and \(E\circ H=E\), so the pair satisfies the directed product condition but does not commute. If \(n=1\), the base map is the identity and idempotence forces its single label to be \(1_G\); both conditions hold for the sole ordered pair.

**5. Large-group-order limit.** The individual-idempotent formula follows by choosing \(r\) fixed image indices, mapping the other \(n-r\) indices to them, and freely labelling each nonroot index. It has leading term \(nq^{n-1}\). The maximum degree in \(q\) in the pair-count polynomial is \(2n-2\), achieved only when \(a=1,b=c=0,d=n-1,t=0\), yielding coefficient \(n\). Therefore \(\Phi_{n,G}(1,1,1)=nq^{2n-2}+O_n(q^{2n-3})\) and \(I_n(q)^2=n^2q^{2n-2}+O_n(q^{2n-3})\). Division proves the stated limit.

## Verification

The standalone standard-library script `verification/verify.py` computes the formula independently in two ways: direct enumeration of all pairs of idempotent underlying transformations on up to four points, with a label-lift factor, and direct multiplication of **all** group-labelled idempotents for \(G=C_2\) at \(n=2,3,4\), for \(G=S_3\) at \(n=2,3\), and for \(G=C_6\) at \(n=3\). It compares every coefficient of \(X^rY^sZ^u\), not merely totals. For \(n=3\), the recorded totals are \(493\) for \(C_2\) and \(11989\) for both \(S_3\) and \(C_6\); for \(n=4\), \(C_2\) gives \(16521\). The script also checks the leading \(q\)-degree and coefficient at \(1\le n\le10\). The captured output is `verification/check_output.txt`, with terminal marker `VERIFY_OK_GROUP_WREATH_SKEW_IDEMPOTENCE`. The universal proof is Steps 1–5, not an extrapolation from finite tests.

## Relationship to prior work

Dolinka, Gould and Yang (2014) establish the free-\(G\)-act endomorphism/wreath-product framework and study the biordered set and maximal subgroups. Al-Aadhami's thesis, Section 4.3.1, gives the individual-idempotent count \(I_n(q)\). A published result entitled *Exact one-sided idempotence rank spectrum in the full transformation monoid* gives joint rank data for the case \(G\) trivial. A published result entitled *Simultaneous untwisting of commuting retractions on homogeneous finite group-sets* treats **commuting** idempotent families; commutativity is a strictly narrower condition than one-sided product idempotence for \(n\ge2\). The formula here makes no commutativity assumption and requires an additional independent constrained-lift calculation depending on \(t=|\operatorname{im}(h\circ f)\setminus\operatorname{im}f|\), which is not determined by the three ranks alone. The general finite-group formula and its nonabelian group-order universality were not identified in the inspected works.

## Limitations

The result covers finite **groups** as the label alphabet, not arbitrary finite monoids; inversion in Step 4 is essential. It does not classify the four structural skew-pair types, or products of three or more idempotents. The large-\(q\) limit holds for each fixed \(n\); no joint \(n,q\) asymptotic is asserted. Some older treatments of skew idempotent pairs were accessible only as abstracts; historical priority remains subject to additional inspection.

## References

1. I. Dolinka, V. Gould and D. Yang, *Free idempotent generated semigroups and endomorphism monoids of free \(G\)-acts*, arXiv:1402.4042v1, first posted 2014-02-17, https://arxiv.org/abs/1402.4042; full author-hosted manuscript https://www-users.york.ac.uk/~varg1/DolinkaGouldYang_1.S2.pdf.
2. A. D. H. Al-Aadhami, *Combinatorial Questions for \(S\wr_n\mathcal T_n\) for a Semigroup*, University of York thesis (2017), Section 4.3.1, https://etheses.whiterose.ac.uk/id/eprint/19494/.
3. *Exact one-sided idempotence rank spectrum in the full transformation monoid*, published mathematical record (2026), record ID SCOPE-20261025-0e04e0804e5b.
4. *Simultaneous untwisting of commuting retractions on homogeneous finite group-sets*, published mathematical record (2026), record ID SCOPE-20261025-19779e27b698.
5. T. S. Blyth and M. H. Almeida Santos, *Skew Pairs of Idempotents in Transformation Semigroups*, Acta Math. Sinica 22 (2006), 1705–1714, DOI:10.1007/s10114-005-0703-5; abstract and preprint catalog https://www.dm.fct.unl.pt/en/investigacao/pre-publicacoes/2005/skew-pairs-idempotents-transformation-semigroups.
