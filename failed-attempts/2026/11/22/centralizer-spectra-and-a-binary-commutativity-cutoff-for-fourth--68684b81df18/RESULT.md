# Centralizer spectra and a binary commutativity cutoff for fourth-order substitution monoids

## Finding
Let \(k=\mathbb F_q\), where \(q\) is a prime power, and let
\[
M_4(q)=\operatorname{End}_{k\mathrm{-alg}}(k[t]/(t^4))
=\{f(t)=at+bt^2+ct^3\pmod {t^4}:a,b,c\in k\},
\]
with multiplication by composition. There are exactly \(q^3\) elements. For \(f=(a,b,c)\), the cardinality \(|C(f)|=|\{g\in M_4(q):f\circ g=g\circ f\}|\) has the complete *structural* census below. Rows with equal cardinalities must be merged when \(q\) is small.

If \(q\) is even:

| Condition on \(f=(a,b,c)\) | Number of elements | \(|C(f)|\) |
|:---|---:|---:|
| \(a\in\{0,1\},\ (b,c)=(0,0)\) | \(2\) | \(q^3\) |
| \(a\in\{0,1\},\ (b,c)\ne(0,0)\) | \(2(q^2-1)\) | \(2q^2\) |
| \(a\notin\{0,1\}\) | \((q-2)q^2\) | \(q\) |

If \(q\) is odd:

| Condition on \(f=(a,b,c)\) | Number of elements | \(|C(f)|\) |
|:---|---:|---:|
| \(a\in\{0,1\},\ b=c=0\) | \(2\) | \(q^3\) |
| \(a\in\{0,1\},\ b=0,\ c\ne0\) | \(2(q-1)\) | \(3q^2\) |
| \(a\in\{0,1\},\ b\ne0\) | \(2q(q-1)\) | \(q^2+q\) |
| \(a=-1,\ c=-b^2\) | \(q\) | \(q^2\) |
| \(a=-1,\ c\ne-b^2\) | \(q(q-1)\) | \(3q\) |
| \(a\notin\{0,1,-1\}\) | \((q-3)q^2\) | \(q\) |

Thus, writing \(K_4(q)=|\{(f,g)\in M_4(q)^2:f\circ g=g\circ f\}|\),
\[
\boxed{K_4(q)=
\begin{cases}
5q^4-4q^2,&\operatorname{char}k=2,\\
3q^4+9q^3-11q^2,&\operatorname{char}k\ne2.
\end{cases}}
\]
The commuting probability is \(K_4(q)/q^6\). Its leading constant as the field order grows is \(5\) along fields of characteristic two and \(3\) along odd-characteristic fields, after multiplying by \(q^2\).

In addition, if \(M_N(q)=\operatorname{End}_{k\mathrm{-alg}}(k[t]/(t^N))\), for any integer \(N\ge1\), then
\[
\boxed{M_N(q)\text{ is commutative}\iff
\begin{cases}
N\le4,&q=2,\\
N\le2,&q>2.
\end{cases}}
\]
In particular \(M_4(2)\) has eight elements and is commutative; the same is false for every \(q>2\), including nonprime fields.

## Assumptions and scope
All endomorphisms are unital and fix the coefficient field \(k\) pointwise; no field-semilinear endomorphisms are included. The composition order is ordinary substitution \(f\circ g=f(g(t))\) modulo \(t^N\). No restriction that \(a\ne0\) is imposed: the noninvertible substitutions are essential to the full spectrum. The centralizer is a monoid centralizer, not a group centralizer. The enumeration applies to all finite fields, including extension fields. The commutativity cutoff concerns the entire endomorphism monoid, not just its unit group.

## Proof
**Parameterization and multiplication.** The nilradical of \(k[t]/(t^N)\) is \((t)\), and every \(k\)-algebra endomorphism sends \(t\) to a uniquely determined element of \((t)\). Conversely, substitution by any such element respects \(t^N=0\) and defines an endomorphism. At \(N=4\), writing \(g=(u,v,w)\), direct polynomial expansion gives
\[
 f\circ g=\bigl(au,\ av+bu^2,\ aw+2buv+cu^3\bigr).
\]
Define \(P(z)=z-z^2\) and \(Q(z)=z-z^3\). Equating the second and third coefficients of \(f\circ g\) and \(g\circ f\) yields exactly
\[
 P(a)v=bP(u),\qquad Q(a)w+2b(u-a)v=cQ(u).\tag{1}
\]
For a fixed \(f\), counting all solutions \((u,v,w)\in k^3\) to (1) therefore gives \(|C(f)|\), with no invertibility assumptions.

**Characteristic two.** For \(a\notin\{0,1\}\), both \(P(a)\) and \(Q(a)=a(1-a)^2\) are nonzero. For each of the \(q\) choices of \(u\), (1) determines one \(v\) and one \(w\), giving \(q\) centralizing substitutions. For \(a\in\{0,1\}\), (1) becomes \(bP(u)=0=cQ(u)\), since \(2=0\). If \((b,c)=(0,0)\), every \((u,v,w)\) works. Otherwise the field property forces \(u\in\{0,1\}\), because the zero sets of both \(P\) and \(Q\) are precisely \(\{0,1\}\) in characteristic two. Then \(v,w\) are arbitrary, giving \(2q^2\) solutions. The first table follows, including the collision \(q^3=2q^2\) at \(q=2\).

**Odd characteristic: generic and resonant multipliers.** If \(a\notin\{0,1,-1\}\), then \(P(a)Q(a)\ne0\) and, for each \(u\), (1) uniquely determines \(v,w\). Thus \(|C(f)|=q\). For \(a=-1\), the first equation gives \(v=-bP(u)/2\) and the second becomes
\[
(b^2+c)Q(u)=0.
\]
Since \(Q(u)=0\) exactly at the three distinct elements \(0,1,-1\), there are \(q\) allowed \(u\)'s if \(c=-b^2\), and three otherwise. The variable \(w\) is free, giving \(q^2\) or \(3q\).

For \(a=0\) or \(1\), both \(P(a)\) and \(Q(a)\) vanish. If \(b=c=0\), every substitution commutes. If \(b=0,c\ne0\), then \(u\) must be one of the three roots of \(Q\), while \(v,w\) are free, so \(|C(f)|=3q^2\). If \(b\ne0\), then \(P(u)=0\) forces \(u\in\{0,1\}\). At \(u=a\) the second equation imposes no condition on \(v\), giving \(q^2\) choices of \((v,w)\); at the other root it forces \(v=0\), giving \(q\) choices. Hence \(|C(f)|=q^2+q\). Counting the choices of \((a,b,c)\) in these six disjoint cases proves the second table.

**Commuting-pair count.** In a finite monoid, the number of ordered commuting pairs equals \(\sum_f|C(f)|\). Weighting the three even-characteristic rows gives \(5q^4-4q^2\). Weighting the six odd-characteristic rows gives \(3q^4+9q^3-11q^2\). Division by \(|M_4(q)|^2=q^6\) gives the probability and the two characteristic-dependent asymptotic leading constants.

**Sharp cutoff.** For \(N\le2\), every substitution is \(t\mapsto at\), so the monoid is commutative. For \(q>2\), choose \(a\in k\setminus\{0,1\}\). At \(N\ge3\), the substitutions \(f(t)=at\) and \(g(t)=t^2\) fail to commute because their quadratic coefficients are \(a\) and \(a^2\). Over \(\mathbb F_2\), the formula at \(N=4\) proves full commutativity, and reduction modulo \(t^N\) then proves it for all \(N\le4\). At \(N\ge5\), choose \(f(t)=t+t^2\) and \(g(t)=t+t^3\); the fourth-degree coefficient in \(g\circ f-f\circ g\) is \(1\) in characteristic two. This proves noncommutativity for every \(N\ge5\) and completes the equivalence.

## Verification
The complete coefficient equations above constitute the proof for every finite field, not merely the fields tested. The standalone `verify.py` independently computes truncated composition rather than using (1), enumerates all ordered pairs at field orders \(2,3,4,5,7,9\), and compares each element-centralizer histogram against the structural census, merging coincident sizes. In particular the tests use explicit quadratic extension fields at orders \(4\) and \(9\). The actual recorded output is in `verify_output.txt`. The ordered commuting counts for these field orders, respectively, are \(64,387,1216,2725,9751,25353\). These finite checks are reproducibility checks and do not replace the quantified proof.

## Relationship to prior work
Enochs, Jenda and Ozbek (2015), Theorems 2.1 and 5.1, classify exponent-support submonoids of formal series and their invertible portions, rather than finite-field centralizer cardinalities. Jennings (1954) studies the multiplier-one substitution *group*; Johnson (1988) studies its finite quotients and lower central series. Neither group-only setup includes the noninvertible elements \(a=0\) counted here. The separate study *Conjugacy and centralizer spectra of finite fourth-order substitution groups* concerns the unit group of \(k[t]/(t^5)\) in characteristic at least five, not the full endomorphism monoid of \(k[t]/(t^4)\). The present claim is precisely a complete all-endomorphism, finite-field commutativity and centralizer census, together with the sharp field-dependent truncation threshold.

## Limitations
This does not classify individual centralizing substitutions beyond the solution equations, and does not give centralizer spectra for higher truncation lengths. Over \(q=3\), some different structural rows have equal centralizer sizes; the table is intentionally not asserted to have six *distinct* sizes there. The exact monoid census may have a historical equivalent under finite jet semigroups or power-series semigroup nomenclature that has not been identified; originality is assessed from the specifically inspected sources, not proved by absence of search results. No independent external validation has been performed.

## References
1. E. Enochs, O. Jenda, F. Ozbek, *Submonoids of the formal power series*, arXiv:1510.05984v1, first posted 2015-10-20, https://arxiv.org/abs/1510.05984 (complete public text inspected).
2. S. A. Jennings, *Substitution groups of formal power series*, *Canadian Journal of Mathematics* 6 (1954), 325–340, https://doi.org/10.4153/CJM-1954-031-9 (full text inspected).
3. D. L. Johnson, *The group of formal power series under substitution*, *Journal of the Australian Mathematical Society* 45 (1988), 296–302, https://doi.org/10.1017/S1446788700031001 (full text inspected).
4. W. Jabłoński, *An explicit example of an iteration group in the ring of formal power series*, *Aequationes Mathematicae* 98 (2024), 837–850, https://doi.org/10.1007/s00010-024-01070-4 (characteristic-zero group case).
5. *Conjugacy and centralizer spectra of finite fourth-order substitution groups*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-conjugacy-and-centralizer-spectra-of-finite-fourth-order-substit--21c11f1dc6ee (complete result read; different truncation and group rather than monoid).
