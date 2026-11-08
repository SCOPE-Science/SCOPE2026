# Divisor classification of Frobenius-adjoint expansions of finite Łukasiewicz chains

## Finding
For every integer \(n\ge2\), let \(m=n-1\). All Frobenius-adjoint expansions of the fixed \(n\)-element Łukasiewicz chain are indexed **bijectively** by the positive divisors \(d\mid m\). The unique expansion indexed by \(d\) is
\[
f_d(j)=d\left\lfloor\frac j d\right\rfloor,\qquad
 g_d(j)=d\left\lceil\frac j d\right\rceil
\qquad (0\le j\le m).
\]
Thus the exact number of distinct ordered operator pairs is \(\tau(n-1)\), the positive-divisor counting function. Their shared fixed-point set is \(C_d=\{0,d,2d,\ldots,m\}\), and
\[
f_{d_1}\le f_{d_2}\text{ pointwise}\quad\Longleftrightarrow\quad d_2\mid d_1.
\]
In particular, the expansion order is the **dual** of the positive-divisor lattice (under the stated order on \(f\)).

## Assumptions and scope
The chain \(L_m=\{0,1,\ldots,m\}\) has the standard Łukasiewicz operations
\[
x\wedge y=\min(x,y),\quad x\vee y=\max(x,y),\quad
 x\odot y=\max(0,x+y-m),\quad x\to y=\min(m,m-x+y).
\]
The integers are rescaled by \(m\) to obtain the conventional chain in the interval \([0,1]\). We count pairs \(f,g:L_m\to L_m\) satisfying, for **every** \(x,y\in L_m\), exactly the source's Frobenius-adjoint axioms:
\[
\begin{aligned}
f(x)&\le x,\\
f(g(x)\to y)&=g(x)\to f(y),\\
f(g(x)\vee y)&=g(x)\vee f(y),\\
g(x\wedge g(y))&=g(x)\wedge g(y),\\
g(x)\le y&\iff x\le f(y).
\end{aligned}
\]
No additional monadic axioms are assumed. A *positive divisor* includes \(1\) and \(m\). For \(m=1\) the unique pair is the identity. The underlying chain is **fixed and labelled**: these counts do not include permutations, products, or other finite residuated structures.

## Proof
**1. The two maps have one common image and are rounding operators.** An adjunction \(g\dashv f\) makes both maps isotone. Because \(f(x)\le x\), the adjunction implies \(x\le g(x)\): indeed \(x\le f(g(x))\le g(x)\). We also have \(f(0)=0\). Substituting \(y=0\) into the join-Frobenius identity and using \(f(0)=0\) gives
\[
f(g(x))=g(x).
\]
For any \(x\), write \(b=f(x)\). Adjunction implies \(g(b)\le x\). Since \(g(b)\) is fixed by \(f\), isotonicity yields \(g(b)=f(g(b))\le f(x)=b\); but \(b\le g(b)\). Hence \(g(f(x))=f(x)\). These two equalities imply the common image
\[
C=f(L_m)=g(L_m)=\mathrm{Fix}(f)=\mathrm{Fix}(g).
\]
The adjunction implies \(f(m)=m\) and \(g(0)=0\), while \(f(0)=0\), so \(0,m\in C\). For any \(j\), isotonicity and the inequalities \(f\le\mathrm{id}\le g\) show
\[
f(j)=\max\{c\in C:c\le j\},\qquad g(j)=\min\{c\in C:j\le c\}.
\]
The maxima and minima exist because both endpoints lie in \(C\).

**2. The common image is an MV-subalgebra, hence a divisor subchain.** For \(b,c\in C\), we have \(b=g(b)\) and \(c=f(c)\). Applying the residuum-Frobenius identity gives
\[
f(b\to c)=b\to f(c)=b\to c,
\]
so \(C\) contains \(0,m\) and is closed under \(\to\). In any Łukasiewicz chain, \(\neg b=b\to0=m-b\), \(b\oplus c=\neg b\to c=\min(m,b+c)\), and \(b\ominus c=\neg(\neg b\oplus c)=\max(0,b-c)\). Therefore \(C\) is closed under truncated sum and subtraction.

Let \(d\) be the least strictly positive member of \(C\). Closure under \(\oplus\) implies \(0,d,2d,\ldots\) up to the first saturation at \(m\) lie in \(C\). Write \(m=qd+r\), with \(0\le r<d\). Since \(qd\in C\) and \(m\in C\), the difference \(m\ominus qd=r\in C\); minimality of \(d\) forces \(r=0\), so \(d\mid m\). For any \(c\in C\), Euclidean division \(c=kd+r\) and closure under subtraction similarly force \(r=0\). Thus
\[
C=C_d:=\{0,d,2d,\ldots,m\}.
\]
By step 1, \(f,g\) are exactly lower and upper rounding to \(C_d\). No additional pairs can occur.

**3. Every divisor provides a valid expansion.** Fix \(d\mid m\). Define \(f_d,g_d\) by the displayed floor/ceiling formulas. Both maps have values in \(C_d\), and for any \(x,y\) we have \(g_d(x)\le y\iff x\le f_d(y)\), because both sides assert the existence of an element of \(C_d\) between \(x\) and \(y\). Evidently \(f_d(x)\le x\).

Write \(b=g_d(x)\in C_d\). The function \(f_d\) commutes with adjoining a fixed member of \(C_d\) by maximum:
\[
f_d(\max(b,y))=\max(b,f_d(y)).
\]
Moreover, \(m-b\) is a multiple of \(d\), so integer division shows
\[
f_d(b\to y)= f_d(\min(m,m-b+y))
 =\min(m,m-b+f_d(y))=b\to f_d(y).
\]
Finally, writing \(b=g_d(y)\) this time, upper rounding obeys
\[
g_d(\min(x,b))=\min(g_d(x),b).
\]
All Frobenius conditions and the adjunction hold for every pair of elements. Distinct divisors give distinct fixed-point sets and therefore distinct pairs.

**4. Counting and order.** One expansion corresponds to each positive divisor \(d\mid m\), giving \(\tau(m)=\tau(n-1)\). For \(d_1,d_2\mid m\), the inequality \(f_{d_1}\le f_{d_2}\) is equivalent to \(C_{d_1}\subseteq C_{d_2}\): necessity follows by evaluating both maps on every \(c\in C_{d_1}\), and sufficiency follows from the maximum-below characterization. Finally, \(C_{d_1}\subseteq C_{d_2}\iff d_2\mid d_1\). This proves the anti-isomorphism.

## Verification
The standalone standard-library program `verify_fgc_mv.py` enumerates **all nondecreasing deflationary self-maps** \(f\) of the chain of each size \(2\le n\le10\). For each, it constructs the **unique** possible left adjoint \(g\) directly from the order relation, then independently checks the five displayed axioms for every ordered pair of elements. The exact surviving \((f,g)\) sets equal the predicted divisor-indexed pairs. Across these sizes, the observed expansion counts are \(1,2,2,3,2,4,2,4,3\), respectively. The largest search considers \(16{,}796\) deflationary monotone maps.

Run from the package directory using `python3 verify_fgc_mv.py`; no third-party packages or files are needed. Finite enumeration supports correctness of small cases but is not an infinite proof: the universally quantified theorem is established by steps 1–4.

## Relationship to prior work
Wang, Shi and Wang (2026) introduce the exact Frobenius-adjoint axioms and establish structural identities for the resulting residuated lattices (particularly Proposition 3.13); their Example 3.17 constructs an expansion of the three-element Łukasiewicz chain, but no full divisor-parametrized classification or arbitrary-size count appears in the inspected article. The fixed-point consequences are reconstructed above from the primitive axioms.

Existing work on **monadic MV-algebras** and subalgebra divisibility provides relevant background, but the monadic axioms are not identical to these Frobenius-adjoint axioms; the 2026 source explicitly exhibits an expansion belonging to the latter and not the former. A published classification for **Gödel chains** likewise concerns a different residual operation: Gödel subchains can have arbitrary interior steps, whereas the Łukasiewicz residual enforces divisibility. This distinction is essential; the Gödel classification does not imply the present count.

## Limitations
Only finite standard Łukasiewicz **chains** with their fixed standard algebraic structure are classified; no statement is made about products, infinite MV-algebras, arbitrary finite residuated lattices, or monadic expansions. The divisor-subalgebra structure is classical. Historical originality remains subject to older results potentially using equivalent terminology; this is not an independently audited priority claim.

## References
1. Juntao Wang, Jieqiong Shi and Mei Wang, *Frobenius Galois expansions of substructural logics: Algebraization, Kalman equivalence and positive cone semantics*, arXiv:2609.09529 (first public September 8, 2026), §3.2, equations (2)–(7), Proposition 3.13, Example 3.17. https://arxiv.org/abs/2609.09529
2. Cecilia Cimadamore and José Patricio Díaz Varela, *Monadic MV-algebras I: A study of subvarieties*, Algebra Universalis **71** (2014), 71–100. DOI:10.1007/s00012-014-0266-3. Distinct monadic axioms and established MV-subalgebra context.
3. *Frobenius-adjoint and monadic expansions coincide on Gödel algebras*, published published-finding corpus mathematical record (October 4, 2026). Its chain statement concerns Gödel, not Łukasiewicz, residuation.
