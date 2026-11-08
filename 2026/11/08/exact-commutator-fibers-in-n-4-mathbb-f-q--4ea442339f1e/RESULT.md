# Exact commutator fibers in \(N_4(\mathbb F_q)\)

## Finding
Let \(k=\mathbb F_q\) be **any** finite field, including characteristic two, and let \(N=N_4(k)\) be the six-dimensional associative algebra of strictly upper-triangular \(4\times4\) matrices. For \(w\in N\), write
\[
F_q(w)=\#\{(X,Y)\in N^2:XY-YX=w\}.
\]
The linear commutator span is \(W=[N,N]_{\mathrm{span}}=\langle E_{13},E_{24},E_{14}\rangle_k\), and **the set of individual commutator values is exactly \(W\)**. Writing \(w=uE_{13}+vE_{24}+tE_{14}\), the complete fiber law is
\[
F_q(w)=\begin{cases}
q^8+2q^7(q^2-1),&u=v=t=0,\\
2q^7(q^2-1),&u=v=0,\ t\ne0,\\
q^7(q^2-1),&(u,v)\ne(0,0),\\
0,&w\notin W.
\end{cases}
\]
Thus the nonzero central commutators have **twice** the fiber cardinality of the noncentral commutators. In particular,
\[
\Pr_{X,Y\ \mathrm{uniform}}(XY=YX)=2q^{-3}+q^{-4}-2q^{-5}.
\]

## Assumptions and scope
The notation \(N_4(k)\) means matrices with all diagonal and lower-triangular entries zero, not the full triangular algebra or the unitriangular **group**. The commutator is the additive associative-algebra commutator, not a multiplicative group commutator. All pairs \((X,Y)\) are **ordered**, and elements are sampled uniformly when probabilities are stated. Every prime-power \(q\ge2\) is allowed. The displayed fibers are exact over nonprime fields as well, since only finite-field linear algebra is used.

Use coordinates
\[
X=aE_{12}+bE_{23}+cE_{34}+dE_{13}+eE_{24}+fE_{14},
\quad
Y=AE_{12}+BE_{23}+CE_{34}+DE_{13}+EE_{24}+FE_{14}.
\]
The six coordinates in either matrix vary independently over \(k\); the repeated capital letter \(E\) in the coefficient of \(E_{24}\) is a scalar, not a matrix unit.

## Proof
**1. Commutator coordinates and support.** Direct multiplication of matrix units gives
\[
XY-YX=(aB-bA)E_{13}+(bC-cB)E_{24}
 +(aE+dC-Ae-Dc)E_{14}.
\]
No other matrix coordinate can occur. Conversely, the brackets of \(E_{12},E_{23}\), of \(E_{23},E_{34}\), and of \(E_{12},E_{24}\) give the three respective basis vectors of \(W\). The center of \(N\) is exactly \(kE_{14}\): commuting a general \(X\) with \(E_{12}\), \(E_{23}\), and \(E_{34}\) successively forces \(b=e=0\), \(a=c=0\), and \(d=0\). It remains to count fibers and show every \(w\in W\) is an individual value.

**2. Projected fibers.** Fix prescribed \(u,v\in k\), and count sextuples \((a,b,c,A,B,C)\) satisfying
\[
aB-bA=u,\qquad bC-cB=v.
\]
If \((b,B)\ne(0,0)\), each equation is a nonzero linear functional on a disjoint pair of unknowns; hence each has exactly \(q\) solutions. The total contribution, for **each** prescribed \((u,v)\), is \((q^2-1)q^2\). If \((b,B)=(0,0)\), both left sides vanish and all four remaining variables are free. Hence the projected fiber count is
\[
H_q(u,v)=q^2(q^2-1)+q^4\mathbf 1_{(u,v)=(0,0)}.
\]
In particular \(H_q(0,0)=2q^4-q^2\), while \(H_q(u,v)=q^2(q^2-1)\) for each nonzero pair.

**3. The top coordinate.** For fixed sextuple from the preceding step, the scalar \(t\) equals the linear form
\[
(d,e,D,E)\longmapsto C d-Ae-cD+aE.
\]
It is a nonzero functional unless \(a=c=A=C=0\). For a nonzero functional each prescribed \(t\) has \(q^3\) solutions among the four middle-layer variables. The two central coordinates \(f,F\) are arbitrary, yielding \(q^5\) extensions per prescribed \(t\). In the exceptional case \(a=c=A=C=0\), there are precisely \(q^2\) choices of \((b,B)\), both projected coordinates are zero, and \(t\) must be zero. Each exceptional choice admits \(q^6\) choices of the remaining coordinates; the exceptional contribution to \(F_q(0)\) is therefore \(q^8\). Subtracting the \(q^2\) exceptional projected sextuples from \(H_q(0,0)\), the nonexceptional contribution is \((2q^4-2q^2)q^5=2q^7(q^2-1)\). For \((u,v)\ne(0,0)\), no exception is possible and the contribution is \(q^2(q^2-1)q^5=q^7(q^2-1)\). This gives every displayed fiber count. Since all three in-span expressions are positive for \(q\ge2\), every element of \(W\) is attained.

**4. Normalization and independent centralizer check.** The three support strata contain respectively \(1\), \(q-1\), and \(q(q^2-1)\) values. Thus the total pair mass is
\[
\bigl[q^8+2q^7(q^2-1)\bigr]+(q-1)2q^7(q^2-1)+q(q^2-1)q^7(q^2-1)=q^{12}=|N|^2.
\]
Independently, the linear map \(Y\mapsto[X,Y]\) has rank only \(0,1,2,3\). The respective numbers of \(X\in N\) are
\[
q,\quad q^3-q,\quad q^3(q^2+q-2),\quad q^3(q-1)(q^2-1).
\]
For example, its three potentially nonzero coordinate rows, in columns \((A,B,C,D,E,F)\), are \((-b,a,0,0,0,0)\), \((0,-c,b,0,0,0)\), and \((-e,0,d,-c,a,0)\); elementary row reduction gives those four classes. Summing \(q^{6-\mathrm{rank}}\) over \(X\) independently recovers the zero fiber \(q^8+2q^9-2q^7\).

## Verification
The standalone `verify.cpp` exhaustively forms both products of actual \(4\times4\) matrices, counts each commutator output, and compares every fiber with the theorem for \(q=2,3,4\) (the order-four field uses the irreducible relation \(z^2+z+1=0\)). It tests respectively \(4096\), \(531441\), and \(16777216\) ordered pairs. An independent `verify_independent.py` counts projected fibers and centralizer ranks over the prime fields of orders \(2,3,5\). Both terminate with `VERIFY_OK`. Instructions and numeric outputs appear in `VERIFICATION.md`. These finite calculations corroborate but do not replace the universal argument.

## Relationship to prior work
Jordan Bounds, *Power commuting and centralizing maps on the ring of strictly upper triangular matrices* (arXiv:2301.03422, first public version 9 January 2023), classifies linear maps satisfying a commuting or centralizing **functional identity** on these matrix rings. Its results do not count ordered pairs with a specified commutator value; its field assumption is characteristic zero in the inspected full text.

Kaur–Sharma–Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices* (arXiv:2006.01493, 2 June 2020), determines conjugacy branching and commuting probabilities in unitriangular **groups** of relevant sizes in odd characteristic. The group \(I+N\) has exactly the same **commuting-pair** condition as the algebra \(N\), so its results can imply the present zero fiber for odd \(q\), and that zero-fiber consequence is **not claimed as separately novel**. Their branching results do not state the current full nonzero **additive algebra-commutator** fiber law, and the multiplicative commutator is a different word map.

Fulman–Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields* (arXiv:1611.05499, 16 November 2016), counts commuting pairs in full matrix and classical Lie algebras and their nilpotent elements; it does not determine fixed nonzero commutator fibers in the strictly triangular subalgebra. The present contribution is the exact simultaneous classification of **all** nonzero commutator fibers in the first three-step strictly triangular algebra, uniform in finite-field characteristic.

## Limitations
The formula is specific to \(4\times4\) strictly upper-triangular matrices; no universal claim for higher sizes, other nilpotent algebras, or arbitrary coefficient rings is made. Part of the zero-fiber count follows from existing commuting-probability work. The search and source comparisons do not constitute independent certification of publication priority; unlocated exact formulas or stronger structural results may exist. The theorem is supported by a complete proof and small-field finite checks, but no independent mathematical audit has been performed.

## References
1. J. Bounds, *Power commuting and centralizing maps on the ring of strictly upper triangular matrices*, arXiv:2301.03422, first posted 2023-01-09; inspected HTML v3 (2025), https://arxiv.org/abs/2301.03422 .
2. D. Kaur, U. B. Sharma, A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493, first posted 2020-06-02, https://arxiv.org/abs/2006.01493 .
3. J. Fulman, R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499, first posted 2016-11-16, https://arxiv.org/abs/1611.05499 .
