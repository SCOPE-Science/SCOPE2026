# Central subsets of Brandt power semigroups recover conjugacy-class and normal-subgroup counts

## Finding
Let \(G\) be a finite group and \(I\) a nonempty finite index set of size \(n\). Let \(B_I(G)=(I\times G\times I)\sqcup\{0\}\) be the Brandt inverse semigroup and \(\mathcal P^*(B_I(G))\) the semigroup of **nonempty** subsets under setwise product. For each nonempty conjugation-invariant subset \(H\subseteq G\), put
\[
D_H=\{(i,h,i):i\in I,\ h\in H\},\qquad D_H^0=D_H,\quad D_H^1=D_H\cup\{0\}.
\]
Then its entire center is exactly
\[
Z(\mathcal P^*(B_I(G)))=\{\{0\}\}\ \cup\ \{D_H^\varepsilon:\varnothing\ne H\subseteq G,\ gHg^{-1}=H\ (g\in G),\ \varepsilon\in\{0,1\}\}.
\]
If \(k(G)\) is the number of conjugacy classes and \(\nu(G)\) is the number of normal subgroups of \(G\), then
\[
|Z(\mathcal P^*(B_I(G)))|=2^{k(G)+1}-1,\qquad
|\operatorname{Idem} Z(\mathcal P^*(B_I(G)))|=1+\begin{cases}2\nu(G),&n=1,\\\nu(G),&n\ge2.\end{cases}
\]
Its entire multiplication is explicit: \(\{0\}\) is absorbing, and for nonempty conjugation-invariant \(H,K\) and \(\varepsilon,\delta\in\{0,1\}\),
\[
D_H^\varepsilon D_K^\delta=\begin{cases}D_{HK}^{\max(\varepsilon,\delta)},&n=1,\\D_{HK}^1,&n\ge2.\end{cases}
\]
In particular, the center's cardinality recovers \(k(G)\); together with its idempotent count (and the known index regime), it recovers \(\nu(G)\). Its multiplication changes sharply between \(n=1\) and \(n\ge2\), whereas its cardinality is independent of \(n\).

## Assumptions and scope
The group \(G\) is finite, with no assumption of commutativity. The index set \(I\) is nonempty and finite. The zero \(0\) belongs to the Brandt semigroup, but the empty subset does **not** belong to \(\mathcal P^*\). For nonzero Brandt elements,
\[
(i,g,j)(k,h,\ell)=\begin{cases}(i,gh,\ell),&j=k,\\0,&j\ne k.\end{cases}
\]
A central subset commutes under setwise product with *every* nonempty subset; testing all singleton subsets is equivalent, by distributivity over unions. A conjugation-invariant subset is a union of full conjugacy classes. \(k(G)\) includes the identity conjugacy class; \(\nu(G)\) counts the trivial subgroup and \(G\) itself, with repetitions identified if \(G\) is trivial.

## Proof
**Step 1: eliminate off-diagonal elements.** Suppose a central nonempty set \(A\) contains \((i,h,j)\) with \(i\ne j\). Fix any \(\ell\in I\) and multiply by the singleton \(\{(j,1_G,\ell)\}\). The left product contains \((i,h,\ell)\). Every *nonzero* member of the reverse product has first index \(j\), so it cannot contain \((i,h,\ell)\). This contradiction forces every nonzero element of \(A\) to be diagonal.

**Step 2: diagonal fibers coincide.** Let \(H_i=\{h\in G:(i,h,i)\in A\}\). With \(y=(k,g,\ell)\), the nonzero part of \(A\{y\}\) is precisely \(\{(k,hg,\ell):h\in H_k\}\); that of \(\{y\}A\) is \(\{(k,gh,\ell):h\in H_\ell\}\). Equality for every \(k,\ell,g\) gives \(H_k g=gH_\ell\). Taking \(g=1_G\), all \(H_i\) equal the same \(H\). If \(H\) is empty, \(A=\{0\}\); otherwise \(gHg^{-1}=H\) for every \(g\). Presence of zero in \(A\) is optional.

**Step 3: converse and multiplication.** Conversely, each \(D_H^\varepsilon\) as above commutes with all nonzero singletons: its nonzero products match by \(Hg=gH\). For \(n\ge2\), a mismatched diagonal index makes zero occur on *both* sides irrespective of \(\varepsilon\); for \(n=1\), zero occurs on both sides exactly when already present in the factor (with a nonzero singleton). They also commute with \(\{0\}\). Thus they are central. For two diagonal full-support subsets the nonzero product is \(D_{HK}\), and a cross-index pair produces zero exactly when \(n\ge2\), unless a factor already contains it. This proves the displayed multiplication rules, including the commutativity \(HK=KH\), which follows from conjugation invariance.

**Step 4: enumerate and identify idempotents.** Each conjugacy class may independently be included or excluded in a conjugation-invariant \(H\); exclude the empty choice. There are \(2^{k(G)}-1\) possibilities and two optional zero flags, plus \(\{0\}\), giving \(2^{k(G)+1}-1\). A finite nonempty subset \(H\) of a group satisfies \(H^2=H\) if and only if it is a subgroup: closure under multiplication makes it a finite subsemigroup, hence contains inverses and identity. Under conjugation invariance these are exactly the normal subgroups. For \(n=1\), each normal subgroup yields two idempotent central subsets. For \(n\ge2\), \((D_H^0)^2=D_{H^2}^1\) necessarily contains zero, so only \(D_H^1\) can be idempotent. Include the absorbing \(\{0\}\) in both counts.

## Verification
Run `python3 verify.py` with Python 3.9 or newer (stdlib only). It constructs Brandt multiplication tables and directly tests the exact centrality criterion, **exhaustively over every nonempty subset** for eight small configurations: \(G\) trivial with \(n=1,2,3\), \(G=C_2\) and \(G=C_3\) with \(n=1,2\), and \(G=S_3\) with \(n=1\). It separately verifies the predicted center's closure and idempotent counts. The reference output is in `verification_output.txt`; all 11,203 assertions passed. Finite checks are corroboration; the unrestricted theorem follows from the four proof steps above.

## Relationship to prior work
Liu and Tringali (2026, arXiv:2610.29525v1) establish rigidity of singleton images under power-semigroup isomorphisms for inverse semigroups; their main theorems concern **isomorphism reconstruction** and do not classify central subsets of Brandt power semigroups. Their §1 recalls earlier Tamura and Shafer questions and the special completely \(0\)-simple case of the power-semigroup isomorphism problem. The present result is instead an explicit internal **center and idempotent enumeration** with a group-conjugacy interpretation. The standard Brandt multiplication and the observation that conjugation-invariant subsets commute under setwise product are background facts, not novelty claims. The exact full-center structure and two-index-regime multiplicative bifurcation are the proposed contribution.

## Limitations
The statement concerns *finite* \(G\) and \(I\), and nonempty subsets only. Its center cardinality alone does not reconstruct the group, and the result does not classify automorphisms of the full power semigroup. Prior-art comparison was limited to accessible mathematical sources and published records, so an unlocated equivalent older formulation remains possible.

## References
- Shuolin Liu and Salvatore Tringali, *Kobayashi’s problem for power semigroups of inverse semigroups*, arXiv:2610.29525v1 (first posted 2026-10-21), §§1, 4–5. https://arxiv.org/abs/2610.29525
- Shuolin Liu and Salvatore Tringali, *Power Semigroups and Two Rigidity Theorems for Groups*, arXiv:2606.01917 (first posted 2026-06-01). https://arxiv.org/abs/2606.01917
- John M. Howie, *Fundamentals of Semigroup Theory*, Oxford University Press, 1995, Chapter 5 (standard Brandt inverse-semigroup construction).
