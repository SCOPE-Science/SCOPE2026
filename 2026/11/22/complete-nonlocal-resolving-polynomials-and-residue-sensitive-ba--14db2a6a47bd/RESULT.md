# Complete nonlocal resolving polynomials and residue-sensitive basis counts for wheels

## Finding

Let \(W_n=K_1\vee C_n\) be the simple labelled wheel with \(n\ge7\) rim vertices. Let \(N_n(z)\) count vertex subsets that distinguish every **nonadjacent** pair by ordinary graph distances, with weight \(z\) for each selected vertex. Define

\[
A=x+x^2,\quad B=x^3,\quad C=x^4+x^5,\quad D=1-zA-z^2AB.
\]

Then the complete nonlocal resolving polynomial is

\[
\boxed{N_n(z)=(1+z)n[x^n]\left(-\log D+\frac{z^2AC}{D}\right).}
\]

The coefficient operation is formal; in particular the answer is an integer polynomial for each \(n\). Every nonlocal metric basis avoids the hub, and the already-known minimum size is \(k_n=\lfloor 2n/5\rfloor\). The **number** \(b_n=[z^{k_n}]N_n(z)\) of labelled bases has the following explicit five-class formula, with \(n=5s+r\):

\[
\boxed{
 b_{5s+r}=\begin{cases}
 \dfrac{5(s+1)(s^4+9s^3+14s^2-24s+24)}{24},&r=0,\ s\ge2,\\[4pt]
 \dfrac{(5s+1)(s^2+s+2)}2,&r=1,\ s\ge2,\\[4pt]
 5s+2,&r=2,\ s\ge1,\\[4pt]
 \dfrac{s(5s+3)(s^2+6s+11)}6,&r=3,\ s\ge1,\\[4pt]
 s(5s+4),&r=4,\ s\ge1.
\end{cases}}
\]

For comparison, let \(R_n(z)\) count ordinary resolving sets of the *same* labelled wheel, which must distinguish all pairs. Their exact polynomial differs by one positive term:

\[
\boxed{N_n(z)-R_n(z)=(1+z)n[x^n]\frac{z^2Ax^5}{D}.}
\]

In particular, writing \(\rho\) for the unique positive root of \(1-x-x^2-x^4-x^5=0\),

\[
\boxed{\lim_{n\to\infty}\frac{N_n(1)}{R_n(1)}=1+\rho=1.551753477740\ldots.}
\]

Thus asymptotically \(\rho/(1+\rho)=0.355567740401\ldots\) of all nonlocal resolving subsets fail ordinary resolution. The nonlocal-basis count has markedly different residue-class growth: it is quintic along \(n\equiv0\pmod5\) but linear along \(n\equiv2\pmod5\).

## Assumptions and scope

The wheel is finite, simple, unweighted and undirected. Its rim is \(v_0,\ldots,v_{n-1}\) in cyclic order, and its hub is \(h\). All subsets are **labelled**, not identified under dihedral symmetries. A nonlocal resolving set \(S\) requires, for every nonadjacent distinct pair \(u,v\), some \(s\in S\) with \(d(u,s)\ne d(v,s)\). A metric basis is a set with minimum cardinality; no claim is made for wheels with fewer than seven rim vertices.

## Proof

**1. Reduction to cyclic signatures.** The hub is adjacent to every rim vertex, so every nonadjacent pair lies on the rim. The hub has equal distance one to both vertices of each such pair, so it never helps nonlocal resolution. For a selected rim set \(T\), any pair containing a selected vertex is distinguished by distance zero. For each unselected rim vertex \(u\), define its signature \(\sigma_T(u)=T\cap\{u-1,u+1\}\), with cyclic indices. The distances to selected rim vertices are one precisely at this signature and two otherwise. Consequently \(T\) is nonlocal resolving exactly when two nonadjacent unselected rim vertices never have the same signature.

Write \(g_1,\ldots,g_k\) for the cyclic lengths of zero-runs between consecutive selected rim vertices, where \(k=|T|\). The empty signature occurs at internal zero-run vertices whose two cyclic neighbors are unselected. A run of length five creates two nonadjacent such vertices; a run of length four creates exactly two, which are adjacent. Two different runs of length at least three create a nonadjacent pair with empty signatures. A repeated nonempty signature can only be a singleton \(\{w\}\), shared by the two neighbors of a selected vertex \(w\); this occurs exactly when the zero-runs immediately before and after \(w\) both have length at least two. These facts give the following necessary and sufficient cyclic-gap conditions:

\[
0\le g_i\le4,\qquad
\#\{i:g_i\ge3\}\le1,\qquad
g_i\ge2\Longrightarrow g_{i-1},g_{i+1}\le1.
\]

Conversely, these three conditions rule out every repeated signature for a nonadjacent pair. At \(n\ge7\), they also force at least two selected rim vertices.

**2. Cyclic enumeration.** Small gaps \(0,1\) have rim-length weight \(A=x+x^2\); gaps of length two have weight \(B=x^3\); a possible *single* exceptional gap of length three or four has weight \(C=x^4+x^5\). No two gaps of length at least two may be adjacent in cyclic gap order. Thus the two-state weighted transition matrix is

\[
M=z\begin{pmatrix}A&B+uC\\A&0\end{pmatrix},
\qquad \det(I-M)=1-zA-z^2A(B+uC).
\]

The variable \(u\) counts exceptional gaps. The weighted trace of \(M^k\) counts indexed cyclic words of \(k\) gaps, and a word with \(k\) selected rim vertices and total rim length \(n\) specifies exactly \(n/k\) labelled subsets (choose the first selected vertex, then forget which of the \(k\) selected vertices was first). Hence the desired rim polynomial is

\[
n[x^n]([u^0]+[u^1])\sum_{k\ge1}\frac1k\operatorname{tr}(M^k).
\]

The formal identity \(\sum_{k\ge1}\operatorname{tr}(M^k)/k=-\log\det(I-M)\) gives \(-\log D+z^2AC/D\) after extracting the coefficients of \(u^0\) and \(u^1\). The hub is entirely optional, giving the factor \(1+z\).

**3. Explicit coefficient and basis count.** If \(k\) rim vertices are selected and \(j\) gaps have length two, the no-exception contribution is

\[
n\sum_{j=0}^{\lfloor k/2\rfloor}\frac{1}{k-j}\binom{k-j}{j}\binom{k-j}{n-k-2j}.
\]

If one exceptional gap has length \(e\in\{3,4\}\), put it in one of \(k\) indexed positions. The \(j\) two-gaps occupy nonadjacent positions outside its two forced-small neighbors; there are \(\binom{k-j-2}{j}\) choices. The remaining small gaps give the contribution

\[
n\sum_{e=3}^4\sum_{j\ge0}
\binom{k-j-2}{j}\binom{k-j-1}{n-k-e-2j}.
\]

Binomial coefficients with out-of-range lower arguments are zero, including terms where the upper argument is negative. These two expressions add to \([z^k]F_n(z)\), where \(F_n(z)=N_n(z)/(1+z)\) counts rim-only choices. At the minimum size \(k=k_n\), the optional hub does not contribute because there are no successful rim sets of size \(k_n-1\). The minimum \(k=\lfloor2n/5\rfloor\) is the known nonlocal wheel dimension of Klavžar and Kuziak. Substitution \(n=5s+r\) and \(k=\lfloor2n/5\rfloor\) yields the displayed five formulas: in the exceptional sum, writing \(j=s-t\), only \(1\le t\le2a+e-r-1\) can contribute, where \(a=0\) for \(r\in\{0,1,2\}\) and \(a=1\) otherwise. Each term becomes

\[
(5s+r)\binom{s+a+t-2}{a+2t-2}\binom{s+a+t-1}{2a+e-r-t-1}.
\]

There is a no-exception contribution of five only when \(r=0\). The remaining sums have at most three terms, and direct binomial simplification gives the five displayed polynomial expressions, valid for every stated \(s\). This proves them without polynomial interpolation or finite-case extrapolation.

**4. Exact ordinary/nonlocal separation.** Adjacent unselected rim vertices have identical distance signatures only if both have empty signatures, because they cannot share a selected rim neighbor when \(n\ge7\). This happens precisely inside a zero-run of length at least four. Among nonlocal resolving sets, at most one zero-run of length four is possible. Moreover, when no gap has length four, the gap conditions imply \(k\ge3\) for \(n\ge7\); a rim set of three or more selected vertices always distinguishes the hub from every rim vertex, since a rim vertex has only two rim neighbors. Thus ordinary resolution is equivalent to the same gap conditions with no length-four gap. Replacing \(C=x^4+x^5\) by \(x^4\) gives \(R_n(z)\) and subtracting yields the claimed exact positive correction.

**5. Asymptotics.** At \(z=1\), set \(D_1(x)=1-x-x^2-x^4-x^5\). Its positive root \(\rho\in(0,1)\) is simple, and it is the unique root of minimum modulus: equality in the triangle inequality at \(|x|=\rho\) would require the positive \(x\) and \(x^2\) terms to have the same positive phase. The logarithmic contribution has coefficients of order \(\rho^{-n}\), whereas the one-exception contribution has coefficients asymptotic to \(c\,n\rho^{-n}\), with \(c>0\). For nonlocal resolution its numerator is \(A(x)(x^4+x^5)\); for ordinary resolution it is \(A(x)x^4\). Their values at the common simple pole have ratio \(1+\rho\). The optional-hub factor two cancels, proving the limit.

## Verification

`verify_nonlocal_wheel.py` uses graph distances directly, independently of the gap proof. For each \(7\le n\le16\), it exhausts all \(2^n\) rim masks, testing both possible hub choices for nonlocal and ordinary resolution, then compares both gap criteria, the full nonlocal polynomial, and the basis formulas. This is a total of 130,944 rim masks. Separately, it compares exact binomial coefficients against coefficients extracted by an integer polynomial recurrence from \(1/D\) through rim size 220, including absence of smaller sets. Running `python3 verify_nonlocal_wheel.py` outputs `VERIFY_OK`. Finite tests corroborate the symbolic proof; they are not a proof for unbounded \(n\).

## Relationship to prior work

Klavžar and Kuziak (arXiv:2211.10614, 19 November 2022), Theorem 4.1, already establish \(\dim_{n\ell}(W_n)=\lfloor2n/5\rfloor\); their Lemmas 4.2--4.3 provide essentially the same gap-feasibility conditions. These are explicit prior art, not claimed as discoveries here. Sooryanarayana, Suma and Chandrakala (2021), Theorem 7.11, characterize ordinary wheel resolving sets by related gap obstructions. The published research record *Exact resolving-set and metric-basis enumerators of wheel graphs* (2026) goes further and gives the complete **ordinary** resolving polynomial and metric-basis counts. It does not claim the nonlocal all-size polynomial, the five nonlocal basis multiplicities, or the exact nonlocal-only correction and limiting ratio. The new enumerations solve distinct questions rather than merely restating either minimum dimension.

## Limitations

The scope is \(n\ge7\), simple unweighted wheels, and labelled vertex subsets. The feasibility gap conditions and the minimum number of landmarks are known; novelty concerns explicit nonlocal enumeration, basis multiplicities and comparison to ordinary resolution. The asymptotic is for all resolving sets, not for basis counts. No classification of dihedral orbits is given. Priority checking cannot rule out obscure, unindexed or inaccessible equivalent counts. Independent validation has not been performed.

## References

1. S. Klavžar and D. Kuziak, *Nonlocal metric dimension of graphs*, arXiv:2211.10614 (first public version 2022-11-19), esp. Section 4, Lemmas 4.2--4.3 and Theorem 4.1. https://arxiv.org/html/2211.10614 .
2. B. Sooryanarayana, Suma A. S., C. S. B. Chandrakala, *Certain Varieties of Resolving Sets of A Graph*, J. Indones. Math. Soc. 27 (2021), 103--114, Theorem 7.11. https://doi.org/10.22342/jims.27.1.881.103-114 .
3. *Exact resolving-set and metric-basis enumerators of wheel graphs* (2026), available published record and full result: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-resolving-set-and-metric-basis-enumerators-of-wheel-graphs--2bd8596e7c59 .
