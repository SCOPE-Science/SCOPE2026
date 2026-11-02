# Pseudo-Frobenius numbers of halved four-term arithmetic-progression semigroups

## Finding
For odd coprime integers \(a\ge5\) and \(d\ge1\), let
\[
S=\langle a,a+d,a+2d,a+3d\rangle,
\qquad T=S/2=\{n\in\mathbb N_0:2n\in S\}.
\]
Put \(x=(a+d)/2\), \(y=(a+3d)/2=3x-a\), and write \(a=3Q+R\), with \(R\in\{0,1,2\}\). The complete pseudo-Frobenius set is
\[
\operatorname{PF}(T)=
\begin{cases}
\{(Q-1)y+2x-a\},&R=0,\\
\{(Q-1)y+2x-a,\ Qy-a\},&R=1,\\
\{(Q-1)y+2x-a,\ Qy+x-a\},&R=2.
\end{cases}
\]
Consequently, \(T\) is symmetric if and only if \(3\mid a\). Its type is \(1\) in that case and \(2\) otherwise. Its Frobenius number is
\[
F(T)=
\begin{cases}
(Q-1)y+2x-a,&R=0,\\
\max\{(Q-1)y+2x,Qy\}-a,&R=1,\\
Qy+x-a,&R=2.
\end{cases}
\]
When \(R=1\), the maximizing branch is the first for \(d<a\) and the second for \(d>a\); equality is excluded by \(\gcd(a,d)=1\), since \(a\ge5\). These formulas are valid for every parameter pair in the stated domain, without a bounded search assumption.

## Assumptions and scope
All semigroups consist of nonnegative integers. The quotient \(S/2\) is defined by membership of twice an integer in \(S\). The pseudo-Frobenius set of a numerical semigroup \(T\) is \(\{f\notin T:f+(T\setminus\{0\})\subseteq T\}\). Its cardinality is the type, and the largest gap is \(F(T)\). The hypotheses require \(a,d\) both odd, positive, and coprime; \(a\ge5\) ensures that four displayed generators give a proper initial progression within the classical open-problem range. In particular, \(2\nmid a\), so standard quotient results requiring the denominator to divide the first generator do not apply.

## Proof
**1. Exact quotient generators.** The first and third generators of \(S\), namely \(a\) and \(a+2d\), are odd; the other two are even. In any even nonnegative combination of the four, the total number of odd generators is even. Pair the odd summands. Upon division by two, each pair contributes one of \(a\), \(a+d=2x\), or \(a+2d=x+y\), while each individual even summand contributes \(x\) or \(y\). Conversely, \(2a\), \(2x=a+d\), and \(2y=a+3d\) belong to \(S\). Therefore
\[
T=\langle a,x,y\rangle,\qquad 3x=a+y.
\]
Also \(\gcd(a,x)=1\), since \(a\) is odd and \(\gcd(a,d)=1\); hence \(T\) is cofinite.

**2. Complete Apéry set.** For any integer \(u\ge0\), write \(u=3q+r\) with \(0\le r\le2\) and set \(W(u)=qy+rx\). The relation \(3x=a+y\) allows every factorization in \(T\) to be rewritten
\[
n=\alpha a+W(u),\qquad \alpha,u\ge0.
\]
Indeed, replace every three copies of \(x\) by one \(a\) and one \(y\). Since \(y\equiv3x\pmod a\), we have \(W(u)\equiv ux\pmod a\). Because \(x\) is invertible modulo \(a\), the residue class of \(W(u)\) determines \(u\bmod a\).

We claim \(W(u+a)>W(u)\) for every \(u\ge0\). If \(a\ge7\), writing \(a=3Q+R\) gives \(Q\ge2\); increasing \(u\) by \(a\) increases its quotient on division by three by at least \(Q\), and decreases its remainder by at most two. Thus
\[
W(u+a)-W(u)\ge Qy-2x\ge2(y-x)=2d>0.
\]
For \(a=5\), the three remainder cases give increments \(y+2x\) or \(2y-x\), both positive because \(y>x>0\). Iteration shows that, for each fixed residue, the least possible normal-form value is obtained at the unique \(u\in\{0,\ldots,a-1\}\). Adding \(\alpha a\) cannot decrease it. Thus
\[
\operatorname{Ap}(T,a)=\{W(0),W(1),\ldots,W(a-1)\}
\]
with exactly one representative per residue class. The elements displayed are actual members of \(T\), so no unverified existence premise is used.

**3. All pseudo-Frobenius elements.** Standard Apéry maximality says that \(W(u)-a\) is pseudo-Frobenius exactly when \(W(u)+x\) and \(W(u)+y\) fail to be Apéry representatives; addition of \(a\) is automatic. For \(u<a-1\), if \(u\equiv0,1\pmod3\), then \(W(u)+x=W(u+1)\), still Apéry. If \(u\equiv2\pmod3\), then \(W(u)+x=W(u+1)+a\), not Apéry. At \(u=a-1\), addition of \(x\) likewise exceeds the smaller same-residue element because \(W(u+a)>W(u)\). Therefore the \(x\)-condition is exactly
\[
u\equiv2\pmod3\quad\text{or}\quad u=a-1.
\]
Similarly \(W(u)+y=W(u+3)\). It is still Apéry when \(u+3<a\), and is not Apéry when \(u+3\ge a\), by the strict increase of \(W\) under addition of \(a\). Thus the \(y\)-condition is precisely \(u\ge a-3\). Their intersection is \(\{a-1\}\) when \(a\equiv0\pmod3\), \(\{a-2,a-1\}\) when \(a\equiv1\pmod3\), and \(\{a-3,a-1\}\) when \(a\equiv2\pmod3\). Inserting these indices into \(W(3q+r)=qy+rx\) yields exactly the three cases for \(\operatorname{PF}(T)\).

**4. Frobenius number and symmetry.** The maximum pseudo-Frobenius number is the Frobenius number. For \(a\equiv2\pmod3\), the second displayed value exceeds the first by \(y-x=d>0\). For \(a\equiv1\pmod3\), the second minus the first is \(y-2x=(d-a)/2\). This establishes the claimed branch and the formula for \(F(T)\). A numerical semigroup is symmetric exactly when it has one pseudo-Frobenius element; the computed sets therefore prove the stated symmetry and type classification.

## Verification
The standalone executable `verify.py` uses Dijkstra shortest paths on residue graphs with independent generating sets for \(S\) and \(T\). It checks that the quotient membership rule \(2n\in S\iff n\in T\) matches, compares the entire computed Apéry set against \(W(u)\), and obtains pseudo-Frobenius elements independently from the computed residue minima. The recorded run passed for 1,550 coprime odd parameter pairs with \(5\le a<100\), \(1\le d<80\), and 2,697,707 explicit quotient-membership comparisons. Reproduce with `python3 verify.py`. These are finite corroborations; the unrestricted mathematical justification is the proof above.

## Relationship to prior work
Adeniran, Butler, Defant, Gao, Harris, Hettle, Liang, Nam, and Volk (2018/2019) explicitly posed the computation of Frobenius numbers and genera for quotients of \(\langle a,a+d,\ldots,a+kd\rangle\) when \(3\le k\le a-2\); their derived formulas focus on restricted denominator regimes and shorter/full progressions. Liu (2023) treated the divisor-of-\(a\) subproblem and explicitly stated this restriction. The family here is the natural first four-term progression with denominator \(2\nmid a\), and the contribution is an exact pseudo-Frobenius classification and symmetry criterion together with the Frobenius formula.

General Apéry and three-generator semigroup theory provides methods for determining each example; no claim is made that Apéry maximality itself is new. Lee and Nam (2024) describe genus calculations for quotients of arithmetic-progressions; genus is not claimed as a new result here. Their complete 23-page article could not be inspected in this investigation, so implicit overlapping coverage is a residual literature risk. Liu (2026) studies a different greedy-coefficient family under an explicit \(p\mid a\) assumption. The classification above is not a direct specialization of the inspected statements requiring \(p\mid a\).

## Limitations
The theorem does not treat even \(a\), even \(d\), noncoprime parameters, longer progressions, or quotient denominators other than two. Its value is a complete formula for the stated nondivisor family, not a proof of the entire general quotient open problem. An unindexed earlier explicit classification or an implicit specialization of a general three-generated numerical-semigroup theorem remains possible. No independent mathematical audit has been performed.

## References
1. A. Adeniran, S. Butler, C. Defant, Y. Gao, P. E. Harris, C. Hettle, Q. Liang, H. Nam, A. Volk, *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360 (first posted 2018-09-25), Semigroup Forum 98 (2019), 690–700.
2. F. Liu, *On quotients of numerical semigroups for almost arithmetic progressions*, arXiv:2312.06096 (first posted 2023-12-11).
3. K. Lee, H. Nam, *The genus of a quotient of several types of numerical semigroups*, International Journal of Number Theory 20 (2024), 1809–1831, DOI:10.1142/S1793042124500891.
4. F. Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415 (2026).
