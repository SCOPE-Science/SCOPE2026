# Maximal commuting subalgebras and a parity incidence law in Frobenius-skew nilpotent radicals

## Finding
Let \(q\) be any prime power, \(m\ge2\), \(K=\mathbb F_{q^m}\), \(Q=q^m\), and \(\sigma(a)=a^q\). In the associative Ore quotient
\[
R=K[t;\sigma]/(t^4),\qquad ta=\sigma(a)t,
\]
let \(J=tR=Kt\oplus Kt^2\oplus Kt^3\), considered as a nonunital \(\mathbb F_q\)-algebra. Define its *all-element commuting graph* to have the \(Q^3\) elements of \(J\) as vertices, with an edge between distinct commuting elements; hence maximal cliques include the center.

All inclusion-maximal pairwise-commuting subsets are precisely the following \(\mathbb F_q\)-subalgebras:

1. \(J^2=Kt^2\oplus Kt^3\), with \(Q^2\) elements.
2. For every \(a\in K^\times\) and \(b\in K\),
\[
H(a,b)=\{ua t+(ub+v a\sigma(a))t^2+ct^3:\ u,v\in\mathbb F_q,\ c\in K\},
\]
with \(q^2Q\) elements.

For a fixed projective \(\mathbb F_q\)-line \(L=\mathbb F_q a\), normalize the representative \(a\). Two parameters \(b,b'\) give the same \(H\) if and only if \(b-b'\in\mathbb F_q a\sigma(a)\). Different projective lines always give different \(H\). Thus there are exactly
\[
\boxed{1+\frac{Q-1}{q-1}\frac Qq}
\]
maximal cliques (and equally many maximal commutative nonunital subalgebras). When \(m>2\), \(J^2\) is the unique *largest* clique; when \(m=2\), all maximal cliques have the same size \(Q^2=q^2Q\).

Write \(W_a=\mathbb F_q a\sigma(a)\). Every \(H(a,b)\) meets \(J^2\) in \(W_a t^2+Kt^3\), of cardinality \(qQ\). Two distinct \(H\)'s with the same first projective line have intersection \(W_a t^2+Kt^3\). For distinct first lines \(\mathbb F_q a\ne\mathbb F_q a'\),
\[
H(a,b)\cap H(a',b')=(W_a\cap W_{a'})t^2+Kt^3.
\]
The map of projective lines \([a]\mapsto[a\sigma(a)]=[a^{q+1}]\) is bijective when \(m\) is odd and exactly \((q+1)\)-to-one when \(m\) is even. Consequently, in odd extension degree, intersections of maximal cliques from distinct first lines have exactly \(Q\) elements; in even extension degree, some distinct first lines produce the larger \(qQ\)-element intersection, with precisely \(q+1\) lines in each such incidence class.

There is also an exact commuting-pair census:
\[
\boxed{\#\{(x,y)\in J\times J:xy=yx\}
=Q^3\bigl((q^2+q+1)Q-q(q+1)\bigr).}
\]
Hence the commuting probability for independent uniform \(x,y\in J\) is
\[
\boxed{\operatorname{cp}(J)=\frac{(q^2+q+1)Q-q(q+1)}{Q^3}.}
\]
The same commuting-pair probability, maximal abelian-subgroup numbers, and maximal-subgroup intersection sizes hold in the finite algebra group \(1+J\), through the bijection \(x\mapsto1+x\).

For completeness, the *element-centralizer spectrum* is as follows. If the coefficient of \(t\) is nonzero, the centralizer has size \(q^2Q\); this occurs \((Q-1)Q^2\) times. If both coefficients of \(t\) and \(t^2\) vanish, the centralizer has size \(Q^3\); this occurs \(Q\) times. For the remaining \((Q-1)Q\) elements with first coefficient zero, second nonzero:

- If \(m\) is odd, every centralizer has size \(qQ^2\).
- If \(m\) is even, put \(E=(Q-1)/(q+1)\). Exactly \(EQ\) such elements have centralizer size \(q^2Q^2\), and exactly \((Q-1-E)Q\) have centralizer size \(Q^2\).

Some displayed centralizer sizes coincide at small parameters; then their multiplicities are added. In particular, \(Z(J)=Kt^3\) for \(m>2\), whereas \(Z(J)=\mathbb F_qt^2+Kt^3\) for \(m=2\).

## Assumptions and scope
All prime powers \(q\ge2\) and all integers \(m\ge2\) are covered, in every characteristic. The fixed field of \(\sigma\) is precisely \(\mathbb F_q\), and \(t^4=0\) in \(R\). The statement concerns the nilpotent radical \(J\), not the full unit group of \(R\) or a graph on the noncentral elements only. A maximal clique means inclusion-maximal, not necessarily maximum cardinality. Products are noncommutative Ore products throughout.

## Proof
**Coefficient reduction.** For \(x=at+bt^2+ct^3\) and \(y=At+Bt^2+Ct^3\), multiplication modulo \(t^4\) gives
\[
xy=a\sigma(A)t^2+(a\sigma(B)+b\sigma^2(A))t^3.
\]
Thus \(x,y\) commute exactly when
\[
a\sigma(A)=A\sigma(a),\qquad
 a\sigma(B)+b\sigma^2(A)=A\sigma(b)+B\sigma^2(a). \tag{1}
\]
The \(c,C\) coordinates are irrelevant to commutation.

**Centralizer with nonzero first coefficient.** Suppose \(a\ne0\). The first equality in (1) says \(\sigma(A/a)=A/a\), hence \(A=ua\) with unique \(u\in\mathbb F_q\). Substituting \(B=ub+v\) in the second gives \(a\sigma(v)=v\sigma^2(a)\). The nonzero solution \(v_0=a\sigma(a)\) has the property that every solution satisfies \(\sigma(v/v_0)=v/v_0\); therefore the full solution space is \(\mathbb F_qv_0\). Hence the element-centralizer is exactly \(H(a,b)\).

**Abelianness and maximality.** Take two elements of \(H(a,b)\) with first two coefficients \((ua,ub+v a\sigma(a))\) and \((wa,wb+z a\sigma(a))\), where \(u,v,w,z\in\mathbb F_q\). Substitution in (1) shows that they commute: the \(b\)-terms cancel and each remaining term cancels by \(a\sigma(a\sigma(a))=(a\sigma(a))\sigma^2(a)\). Their product has first coefficient zero and second coefficient \(uw a\sigma(a)\), so it is again in \(H(a,b)\); closure under addition and scalar multiplication is immediate. Since \(H(a,b)\) is exactly the centralizer of an element with first coefficient \(a\ne0\), no commuting set properly containing it exists. On the other hand \(J^2\) has zero multiplication internally and is abelian. No element with first coefficient \(a\ne0\) commutes with all of \(J^2\), since that would demand \(a\sigma(B)=B\sigma^2(a)\) for every \(B\in K\); putting \(B=1\) gives \(a=\sigma^2(a)\), which would then force \(\sigma(B)=B\) for all \(B\), contrary to \(m\ge2\). Thus \(J^2\) is maximal. Any other maximal commuting set contains an element with nonzero first coefficient, and equals its centralizer. These arguments also show these are precisely the maximal commutative \(\mathbb F_q\)-subalgebras.

**Distinctness and intersections.** The first-coordinate image of \(H(a,b)\) is \(\mathbb F_q a\). Fixing its representative \(a\), equality of two such subalgebras is equivalent to \(b-b'\in W_a\), giving \(Q/q\) distinct translates. Intersection with \(J^2\) is obtained by setting \(u=0\), yielding \(W_at^2+Kt^3\). Comparing two families with the same first line but different offset, a common nonzero \(u\) would imply equality of the offset classes, so only the first-coefficient-zero intersection remains. With distinct first lines, the common first coefficient must be zero, leaving precisely \((W_a\cap W_{a'})t^2+Kt^3\). The cyclic projective group \(K^\times/\mathbb F_q^\times\) has order \(N=1+q+\cdots+q^{m-1}\). The map \([a]\mapsto[a^{q+1}]\) has kernel of size \(\gcd(N,q+1)\). Since \(q\equiv-1\pmod{q+1}\), \(N\equiv1\pmod{q+1}\) for odd \(m\), and \(q+1\mid N\) for even \(m\). The kernel size is respectively one and \(q+1\), giving all incidence claims.

**Centralizer spectrum.** An element with first coefficient \(a\ne0\) has \(q^2Q\) commuting partners by the explicit formula above; count \((Q-1)Q^2\). When \(a=0\), the commutation conditions reduce to \(b\sigma^2(A)=A\sigma(b)\), while \(B,C\) are arbitrary. If \(b=0\), the whole \(J\) centralizes the element. If \(b\ne0\), the equation \(\sigma^2(A)=(\sigma(b)/b)A\) has either only the zero solution or exactly \(q^g\) solutions, where \(g=\gcd(m,2)\), by the multiplicative cyclicity of \(K^\times\). A nonzero solution exists exactly when the norm of \(\sigma(b)/b\) to \(\mathbb F_{q^g}\) equals one. For odd \(m\) this holds for every \(b\), yielding \(q\) possible \(A\). For even \(m\) it is equivalent to \(\operatorname{N}_{K/\mathbb F_{q^2}}(b)\in\mathbb F_q^\times\). The finite-field norm is onto \(\mathbb F_{q^2}^\times\), so exactly \((q-1)(Q-1)/(q^2-1)=(Q-1)/(q+1)\) choices of nonzero \(b\) satisfy it. Multiplying the solution counts by the free \(B,C\) and the free original coefficient \(c\) proves the spectrum and center statements.

**Commuting-pair count.** The \((Q-1)Q^2\) elements with \(a\ne0\) contribute \((Q-1)q^2Q^3\) ordered commuting pairs. For \(a=0\), define \(h(b)=\#\{A:b\sigma^2(A)=A\sigma(b)\}\). By reversing the order of summation, \(\sum_{b\in K}h(b)=Q+q(Q-1)\): \(A=0\) allows all \(Q\) values of \(b\), while every \(A\ne0\) imposes the linearized equation \(\sigma(b)=(\sigma^2(A)/A)b\), with exactly \(q\) solutions. (Indeed \(b=A\sigma(A)\) is a nonzero solution, and the solution ratios lie in \(\mathbb F_q\).) The free original \(c\) and partner \(B,C\) contribute a factor \(Q^3\), yielding the formula. Since \((1+x)(1+y)=(1+y)(1+x)\) exactly when \(xy=yx\), the same classification lifts to the algebra group \(1+J\): the maximal commuting sets already proved above are additive subalgebras, so their \(1+\)-images are precisely the maximal abelian subgroups.

## Verification
The included standalone `verify.py` uses explicit prime-field polynomial models of \(\mathbb F_4,\mathbb F_8,\mathbb F_9,\mathbb F_{16}\). It independently forms the Ore products, exhaustively measures all centralizers and ordered commuting pairs, constructs the proposed maximal commuting subalgebras, tests their cardinalities and projective incidence fiber sizes, and for the three smaller fields exhaustively enumerates maximal graph cliques. The numerical data are: \(Q=4\): 7 maximal cliques, 1408 ordered commuting pairs; \(Q=8\): 29 and 25600; \(Q=9\): 13 and 76545; \(Q=16\): 121 and 434176. Every test passes. Such finite enumerations validate small instances, not the unrestricted proof.

## Relationship to prior work
Ore skew polynomial rings and their coefficient-twisting multiplication are classical. Pumplün and Thompson's 2020 preprint *The norm of a skew polynomial* (arXiv:2006.10418, later *Algebras and Representation Theory*) works with skew polynomials and central quotient algebras, and studies norm/reducibility rather than maximal commuting subsets of the nilpotent quotient by \(t^4\). Cheraghpour, Ghosseiri, Jafari and Seyfpour (arXiv:2402.12619) compute commuting-graph invariants of upper triangular \(2\times2\) matrix rings; their noncentral-only graph decomposes into disjoint cliques over fields, and its theorems do not give the overlapping maximal-clique incidence law here. Nath, Sharma, Dutta and Shang (2021) study general noncommuting graphs and ring isoclinism; their public summary was inspected but their full text was not, so possible indirect implications remain a residual literature risk. The present formulas depend on the Frobenius twist, the quotient \(t^4\), and the projective power map \([a]\mapsto[a^{q+1}]\). No publication-priority certification is claimed.

## Limitations
This is an internal mathematical proof and self-review, not an independent audit. The theorem treats the radical \(J\) of exactly the fourth-order Frobenius-skew quotient, with \(m\ge2\), and not the full ring's commuting graph. The centralizer spectra for even extension degree distinguish cases by a field norm; smaller parameter coincidences of cardinalities are aggregated when making numerical tables. Source searches cannot establish global uniqueness; an unlocated general class-two or class-three algebra-group commutation theorem may imply part of the result.

## References
1. S. Pumplün and D. Thompson, *The norm of a skew polynomial*, arXiv:2006.10418, first public 2020-06-18; *Algebras and Representation Theory* **25** (2022), 869–887; doi:10.1007/s10468-021-10051-z.
2. H. Cheraghpour, M. N. Ghosseiri, M. Jafari and F. Seyfpour, *On Commuting graphs of triangular rings*, arXiv:2402.12619v1, first public 2024-02-20, especially Section 2, Theorem 2.11.
3. R. K. Nath, M. Sharma, P. Dutta and Y. Shang, *On r-Noncommuting Graph of Finite Rings*, *Axioms* **10** (2021), article 233; doi:10.3390/axioms10030233.
4. X. Caruso and J. Le Borgne, *A new faster algorithm for factoring skew polynomials over finite fields*, *Journal of Symbolic Computation* **79** (2017), 411–443; doi:10.1016/j.jsc.2016.02.016. Background on skew-polynomial quotients, not asserted as a priority comparison from full text.
