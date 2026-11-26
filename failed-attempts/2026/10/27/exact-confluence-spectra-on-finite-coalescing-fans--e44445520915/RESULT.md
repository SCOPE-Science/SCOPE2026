# Exact confluence spectra on finite coalescing fans

## Finding

Let \(m\geq1\), and let \(P_m\) be the finite poset consisting of \(m\) labelled pairwise incomparable points \(a_1,\ldots,a_m\), all strictly below one greatest point \(t\). For any binary relation \(R\subseteq P_m^2\), impose **downward confluence** and **forward confluence**, respectively:
\[
 x\le y\ \land\ yRz\quad\Longrightarrow\quad
 \exists w\,(xRw\ \land\ w\le z),\tag{DC}
\]
\[
 x\le y\ \land\ xRz\quad\Longrightarrow\quad
 \exists w\,(yRw\ \land\ z\le w).\tag{FC}
\]
These are exactly the two order–accessibility interaction axioms used for the modal accessibility relation in Definition 12 of Sedlár–Vigiani (2026), and in the earlier local intuitionistic modal frames of Balbiani–Gao–Gencer–Olivetti (2024).

Set \(A=\{a_1,\ldots,a_m\}\), \(T=R(t)\), and \(L=T\cap A\). The complete **coalescing-fan normal form** is:

1. If \(t\notin T\), then \(R(a_i)=L\) for every \(i\). Every \(L\subseteq A\), including the empty set, is admissible.
2. If \(t\in T\) and \(L\ne\varnothing\), then the \(m\) rows \(R(a_i)\) are arbitrary, independently chosen supersets of \(L\) in \(P_m\).
3. If \(T=\{t\}\), then the \(m\) rows \(R(a_i)\) are arbitrary, independently chosen **nonempty** subsets of \(P_m\).

These cases are mutually exclusive and exhaustive, and every relation in them satisfies both confluence conditions. With \(U=2^{m+1}\), the number \(C_m\) of such binary relations and the number \(H_m\) that are additionally reflexive are
\[
\boxed{C_m=2^m+(U-1)^m+(U+2)^m-U^m},
\qquad
\boxed{H_m=(2^m+2)^m}.\tag{1}
\]

For \(m=1,\ldots,5\), the exact counts are
\[
 (C_m)=(7,89,5119,1211297,1171027327),
 \quad (H_m)=(4,36,1000,104976,45435424).
\]
The number with distinguished top row exactly \(R(t)=\{t\}\) is \((U-1)^m\). In particular, for a uniformly chosen doubly confluent \(R\),
\[
\Pr\bigl(R(t)=\{t\}\bigr)
=1-\frac{m}{2^m}+O\!\left(\frac{m^2}{4^m}\right),
\qquad
\Pr(R\text{ reflexive})=2^{-m}\left(1+O\!\left(\frac{m}{2^m}\right)\right).\tag{2}
\]
Thus almost all these modal-frame relations have the singleton top-successor row, while reflexive members form an asymptotically \(2^{-m}\)-fraction.

## Assumptions and scope

The order has exactly the comparable pairs \(a_i\le t\), along with all reflexive pairs; the \(a_i\) are distinct labelled minimal worlds and \(t\) is their unique common top. It is a non-chain as soon as \(m\ge2\), but every principal upper cone is linearly ordered. No seriality, reflexivity, transitivity, symmetry, functionality, restriction on valuations, or condition on an inconsistent-world predicate is built into \(C_m\). Reflexivity is imposed **only** for \(H_m\).

The classification counts **accessibility relations on a fixed ordered set**, not full modal models, valuations, theories, isomorphism types with varying underlying orders, or the number of distinguishable formulas. Where an additional inconsistent-world set \(F\) is part of a Nelson model, its separate condition is not enumerated here. The two confluence conditions themselves are the entire property being counted.

## Proof

Write \(R(x)=\{z:xRz\}\). For each \(i\), the only nontrivial source-order comparison involving \(a_i\) is \(a_i<t\). The instances with \(x=y\) are automatic, taking \(w=z\).

Fix \(i\). Apply (DC) with \(x=a_i\), \(y=t\). For a leaf \(a_j\in L\subseteq T\), the only element \(w\) satisfying \(w\le a_j\) is \(w=a_j\); hence \(L\subseteq R(a_i)\). If \(t\in T\), applying (DC) to \(z=t\) forces \(R(a_i)\ne\varnothing\). Conversely, these are all requirements from (DC): for \(z=t\), any element of the nonempty row witnesses \(w\le t\); for \(z\in L\), the leaf \(z\) itself is a witness.

Now apply (FC) with \(x=a_i\), \(y=t\). If \(t\in T\), choosing \(w=t\) witnesses (FC) for **every** \(z\in R(a_i)\), since all points are below \(t\). If \(t\notin T\), any \(z\in R(a_i)\) must be a leaf \(a_j\), because its permissible upper witnesses are \(a_j\) and \(t\), and \(t\notin T\). The witness is therefore \(a_j\in T=L\). Equivalently, \(R(a_i)\subseteq L\). Together with (DC), this yields \(R(a_i)=L\). Conversely, that equality meets both conditions (including \(L=\varnothing\), where the relation is empty). If \(t\in T\), the stated nonempty-row or superset constraints are sufficient. This proves the normal form in both directions.

To enumerate, put \(U=|\mathcal P(P_m)|=2^{m+1}\). When \(t\notin T\), one choice of \(L\subseteq A\) uniquely determines the whole relation, contributing \(2^m\). When \(T=\{t\}\), each of the \(m\) rows is any nonempty subset of \(P_m\), contributing \((U-1)^m\). When \(t\in T\) and \(|L|=k\ge1\), there are \(\binom{m}{k}\) choices for \(L\), and each row is independently one of \(2^{m+1-k}\) supersets of \(L\). The resulting count is
\[
C_m=2^m+(U-1)^m+
\sum_{k=1}^m\binom{m}{k}2^{m(m+1-k)}.
\]
The binomial theorem gives
\[
\sum_{k=0}^m\binom{m}{k}2^{m(m+1-k)}=(U+2)^m;
\]
subtracting the \(k=0\) term \(U^m\) proves the first identity in (1).

For a reflexive relation, \(t\in T\) and every leaf \(a_i\) belongs to its own successor row. Fix \(L\subseteq A\) with \(|L|=k\). If \(a_i\in L\), its row has \(2^{m+1-k}\) possibilities; if \(a_i\notin L\), the compulsory elements are \(L\cup\{a_i\}\), leaving \(2^{m-k}\) possibilities. Thus the number for this \(L\) is
\[
2^{k(m+1-k)+(m-k)^2}=2^{m^2-(m-1)k}.
\]
Summing over \(k\) and invoking the binomial theorem gives
\[
H_m=\sum_{k=0}^m\binom{m}{k}2^{m^2-(m-1)k}=(2^m+2)^m.
\]

For the asymptotics, let \(q=1/U=2^{-(m+1)}\). Direct binomial expansion, using \(mq\to0\), gives
\[
\frac{C_m}{U^m}=(1-q)^m+(1+2q)^m-1+2^m/U^m
=1+mq+O(m^2q^2).
\]
The final term \(2^m/U^m=2^{-m^2}\) is absorbed in the error for \(m\ge2\). The exact top-singleton count \((U-1)^m\) therefore yields
\[
\frac{(U-1)^m}{C_m}
=\frac{(1-q)^m}{1+mq+O(m^2q^2)}
=1-2mq+O(m^2q^2),
\]
which is the first estimate in (2). Also
\[
\frac{H_m}{C_m}
=\frac{2^{-m}(1+4q)^m}{1+mq+O(m^2q^2)}
=2^{-m}(1+O(mq)),
\]
proving the second estimate. Every asymptotic is for integer \(m\to\infty\) with absolute implicit constants.

## Verification

The standalone `checker.py` directly evaluates both existential conditions for **every** binary relation on \(P_m\) when \(m\in\{1,2,3\}\), independently tests the normal-form predicate, and separately tests reflexivity. This exhausts \(16\), \(512\), and \(65536\) relations, respectively. The numbers satisfying confluence are \(7\), \(89\), and \(5119\); the reflexive subcounts are \(4\), \(36\), and \(1000\).

The checker also verifies the count in every exact distinguished-row stratum through \(m=3\) and tests agreement of the two algebraically different counting sums through \(m=30\). It runs with Python's standard library and prints `VERIFY_OK`. These tests corroborate the finite identities; the unrestricted theorem is proved by the case analysis and binomial calculation above, not by extrapolation from the checks.

## Relationship to prior work

Sedlár and Vigiani (2026), §3.2 Definition 12, introduce the two confluence conditions in the modal extensions of generalized Nelson logics and establish soundness/completeness over their model classes. Their full text includes the frame conditions and semantic applications but no exact enumeration of the coalescing-fan accessibility structures. Balbiani, Gao, Gencer and Olivetti (2024), §2 Definition 2, introduce the same relational conditions in local intuitionistic modal logic, including a separately motivated reflexive \(\mathbf T\) extension; their finite countermodel proof does not classify or enumerate relations over the coalescing fan.

The published *Endpoint normal form and exact census for finite-chain KI frames* gives the corresponding complete spectrum for **linearly ordered** worlds. It does not subsume this theorem for \(m\ge2\): the minimal worlds of \(P_m\) are incomparable, and the chain argument rests on a total order with row minima and maxima. Moreover, the enumeration here includes a separate exact reflexive spectrum and the limiting conditional top-row law. It is not obtained merely by substituting a parameter in the chain formula.

Confluence is also expressible in terms of order-compatible set-valued maps (an Egli–Milner-style comparison); that well-known equivalence explains why a normal form may exist but does not alone determine the exact fan census. No claim is made that the abstract confluence axioms themselves are new.

## Limitations

This classification is for a one-top antichain cone. The proof does not enumerate doubly confluent relations on arbitrary finite rooted trees, arbitrary preorders, or models with extra accessibility restrictions. It does not prove any new completeness, finite-model property, or complexity bound for generalized Nelson logics. No model valuations or designated inconsistent states are counted.

The closest inspected literature treats the generic confluence class or chain instances, rather than this non-chain fan spectrum. A differently named general theorem for monotone multivalued relations on rooted stars could in principle imply the count and remains a residual priority risk. Independent external validation has not been performed.

## References

1. Igor Sedlár and Pietro Vigiani, *Modal Extensions of Generalised Nelson Logics*, arXiv:2610.10008v1, first posted 7 October 2026, particularly §3.2 Definition 12 and §§4–5. https://arxiv.org/abs/2610.10008
2. Philippe Balbiani, Han Gao, Çiğdem Gencer and Nicola Olivetti, *Local Intuitionistic Modal Logics and Their Calculi*, arXiv:2403.06772v1, first posted 11 March 2024, particularly §2 Definition 2. https://arxiv.org/abs/2403.06772
3. *Endpoint normal form and exact census for finite-chain KI frames*, public mathematical record dated 4 October 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-endpoint-normal-form-and-exact-census-for-finite-chain-ki-frames--df6301f11b97
