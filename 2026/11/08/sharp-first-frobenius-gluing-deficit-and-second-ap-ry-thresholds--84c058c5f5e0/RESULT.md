# Sharp first-Frobenius gluing deficit and second-Apéry thresholds for a lacunary triple

## Finding

For every pair of integers \(q\ge 3\) and \(k\ge 2\), set \(a=qk\) and consider
\[
S=\langle qk,qk+1,q(k+1)\rangle.
\]
Let \(R(n)\) be the number of ordered nonnegative **coefficient triples** \((x,y,z)\) satisfying
\[
qkx+(qk+1)y+q(k+1)z=n.
\]
(The order of the three generators is fixed; permutations of coefficients are not additionally counted.) For \(p=0,1\), let \(g_p=\max\{n\in\mathbb N_0:R(n)\le p\}\) and \(n_p=\#\{n\in\mathbb N_0:R(n)\le p\}\). Put \(\delta=\min(q-1,k+1)\). Then
\[
\boxed{g_0=a(k+q-2)-1,\qquad
 g_1=a(k+q-2+\delta)-1,}
\]
and
\[
\boxed{n_0=\frac{a(k+q-2)}2,\qquad
 n_1=\frac{a(k+q-2)}2+q(k+1)+q(k-1)\delta.}
\]
The exact first-Frobenius gluing-bound deficit is
\[
\boxed{a(2k+q-1)-1-g_1=a\max\{k+2-q,0\}.}
\]
Hence the known gluing bound is attained if and only if \(q\ge k+2\), and otherwise has positive deficit \(a(k+2-q)\). The qualitative equality/strictness dichotomy is already implied by the gluing equality criterion in [1]; the new contribution is the exact positive deficit, a complete residuewise two-representation threshold, and the first generalized genus. For instance, \(q=3,k=4\) yields \(S=\langle12,13,15\rangle\), \(g_1=83\), \(n_1=63\), and an upper-bound deficit of \(36\); the correction grows without bound at fixed \(q=3\) as \(k\to\infty\).

## Assumptions and scope

All counts refer to nonnegative integers, and the three generators are distinct and minimal when \(q\ge3\), \(k\ge2\). Their greatest common divisor is one because the first two are consecutive. The exceptional cases \(q=1,2\) are **not** part of the statement: for \(q=2\) the generators form an arithmetic progression, the subject of [2]. The first generalized Frobenius number here uses the convention \(R(n)\le1\), including unrepresented integers; since \(g_1>g_0\), the maximum agrees with the positive-representation-only convention \(0<R(n)\le1\) in [1].

For each residue \(0\le r<a\), write uniquely
\[
r=qu+v,\qquad 0\le u<k,\quad0\le v<q.
\]
The exact first and second representation thresholds in residue \(r\pmod a\) are
\[
\boxed{W_0(r)=r+a(u+v),\qquad
W_1(r)=r+a(u+v+\Delta_u),}
\]
where
\[
\Delta_u=\begin{cases}k+1,&u=0,\\\min(q-1,k+1),&1\le u<k.\end{cases}
\]
More precisely, \(W_p(r)\) is the least nonnegative member of the residue class having more than \(p\) coefficient-triple representations. Every smaller nonnegative member of that class has at most \(p\) representations, while every member at least \(W_p(r)\) in that class has more than \(p\) representations.

## Proof

**Exact denumerant parametrization.** Fix \(r=qu+v\) as above and \(N\ge0\). Write \(n=r+aN\). In a representation \(n=ax+(a+1)y+(a+q)z\), reduction modulo \(a\) gives \(y+qz=r+ja\) for a unique \(j\ge0\). Consequently \(y=v+qh\) and \(z=u+jk-h\) for a unique integer \(h\) satisfying \(0\le h\le u+jk\). Substituting into the full equation yields
\[
x=N-u-v-j(k+1)-(q-1)h.
\]
Every \((j,h)\in\mathbb N_0^2\) obeying
\[
0\le h\le u+jk,\qquad j(k+1)+(q-1)h\le N-u-v
\]
determines a unique nonnegative coefficient triple, and conversely. Thus
\[
\boxed{R(r+aN)=\#\{(j,h)\in\mathbb N_0^2:
0\le h\le u+jk,\ j(k+1)+(q-1)h\le N-u-v\}.}
\]
This equality is exact for every residue and every nonnegative \(N\); it is not an approximation.

**Residue thresholds.** The lowest-cost choice \((j,h)=(0,0)\) first becomes permissible at \(N=u+v\). Every other allowed pair has cost at least \(k+1\) when \(u=0\), because then \(h>0\) forces \(j\ge1\); the pair \((1,0)\) attains this cost. When \(u\ge1\), the two candidates \((0,1)\) and \((1,0)\) are permissible and have costs \(q-1\) and \(k+1\), respectively. All other nonzero pairs have cost at least their minimum. Hence the second factorization first occurs at \(N=u+v+\Delta_u\). Because representations persist under adding another \(a\) (increase \(x\) by one), these first thresholds hold for the entire residue class.

**Maxima.** Since \(r\in[0,a-1]\), the formal predecessor of the first element having more than \(p\) representations is \(W_p(r)-a\); if it is negative, that residue class has no nonnegative member with at most \(p\) representations. The largest such nonnegative integer over **all** residue classes is the maximum of these formal predecessors. For \(p=0\), maximize \(r+a(u+v-1)\): both \(r\) and \(u+v\) are increasing in \(u,v\), so the unique maximizer is \(u=k-1,v=q-1\), with \(r=a-1\). This gives \(g_0=a(k+q-2)-1\).

For \(p=1\), when \(u\ge1\), \(\Delta_u=\delta\) is constant, and the maximum again occurs at \((k-1,q-1)\), yielding \(a(k+q-2+\delta)-1\). When \(u=0\), the maximum occurs at \(v=q-1\) and is \(a(k+q-1)+q-1\). Since \(\delta\ge2\) and \(a=qk>q\), the former strictly exceeds the latter: the difference is at least \(a-q>0\). Thus the displayed formula for \(g_1\) holds, and its maximizing integer has exactly one representation (the second threshold is one \(a\)-step above it).

**Counting small-representation integers.** In residue class \(r\), precisely \((W_p(r)-r)/a\) nonnegative members have at most \(p\) representations; there are no later such members by persistence. Summing for \(p=0\),
\[
n_0=\sum_{u=0}^{k-1}\sum_{v=0}^{q-1}(u+v)
=\frac{qk(k-1)}2+\frac{kq(q-1)}2
=\frac{a(k+q-2)}2.
\]
For \(p=1\), add \(\sum_{u,v}\Delta_u=q(k+1)+q(k-1)\delta\), proving the genus formula.

**Exact gluing comparison.** Put \(T=\langle k,k+1\rangle\), \(d=q\), and \(\gamma=qk+1\). Then \(\gamma=(q-1)k+(k+1)\in T\), \(\gcd(d,\gamma)=1\), and \(S=\langle dT,\gamma\rangle\). For the two-generator semigroup \(T\), the known first generalized Frobenius number is \(2k^2-1\). Proposition 5.2 of [1] therefore gives
\[
g_1\le q(2k^2-1)+(q-1)(qk+1)=a(2k+q-1)-1.
\]
Subtracting the proved closed expression for \(g_1\) gives \(a(k+1-\delta)=a\max\{k+2-q,0\}\). Theorem 5.3 of [1] already describes equality by factorization containment, so the threshold for equality is not asserted as a new general theorem. For completeness, the unique factorization of \(2k^2-1\) in \(T\) is \((k,k-1)\), and factorizations of \(\gamma\) are \((q-1-(k+1)t,1+kt)\) when the entries are nonnegative. Only \(t=0\) can be coordinatewise bounded by \((k,k-1)\), giving an obstruction exactly when \(q\le k+1\), in agreement with the exact deficit.

## Verification

The included `verify_cpp.cpp` is an independent capped-denumerant dynamic program: after fixing \(q,k\), it enumerates all representation counts through \(g_1+a\) using the ordinary unbounded-coin recurrence, capping at two because only the distinctions \(0,1,\ge2\) matter. It checks both generalized Frobenius maxima, both genera, and every first/second residue threshold against direct counts for \(3\le q\le36\), \(2\le k\le36\). It uses the symbolic formulas only as expectations, not for constructing the count table. A second implementation `verify_brute.py` enumerates coefficient triples directly for \(3\le q\le17\), \(2\le k\le17\) and checks critical boundaries.

Compile and run with `g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp && ./verify_cpp`; independently run `python3 verify_brute.py`. The recorded outputs are in `VERIFY_OUTPUT.txt`. The proof above is responsible for the infinite claim; finite checks only test implementation and boundaries.

## Relationship to prior work

García Barroso, García-García, Santana Sánchez and Vigneron-Tenorio [1] introduce a general affine-semigroup first-Frobenius framework. Their Section 5, Proposition 5.2 supplies the gluing **upper bound** specialized above, and Theorem 5.3 already determines when equality holds by containment among factorizations. These results do not provide the **size** of the deficit in the strict regime, the residuewise complete two-representation thresholds, or the first generalized genus for the present lacunary triple. The positive deficit is therefore the focus, rather than the known existence of strict inequality. Komatsu and Ying [2] classify generalized Frobenius invariants for three generators in an arithmetic progression, which is not the present \(q\ge3\) family. A later study [3] gives ordinary (zero-representation) Frobenius formulas in lacunary triples under different conditions, not this complete first-representation spectrum.

## Limitations

Only the first two thresholds, first generalized genus, and corresponding Frobenius numbers are classified; no formula is asserted for all higher \(p\). The result is restricted to integers \(q\ge3,k\ge2\). Independent verification by a human or separate institution has not been performed. A logically equivalent formula could exist in literature not indexed by the searches inspected; originality is qualified by those source-access limits.

## References

[1] E. R. García Barroso, J. I. García-García, L. J. Santana Sánchez and A. Vigneron-Tenorio, *On p-Frobenius of Affine Semigroups*, arXiv:2311.06050 (first public 2023-11-10), Mediterranean Journal of Mathematics 21 (2024), article 90, DOI: 10.1007/s00009-024-02625-0. Preprint: https://arxiv.org/abs/2311.06050 ; full open-access article: https://link.springer.com/article/10.1007/s00009-024-02625-0 .

[2] T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first public 2022-06-27), https://arxiv.org/abs/2206.13052 .

[3] I. O. Bado, *Explicit Frobenius Numbers for a Lacunary Three-Generated Family of Numerical Semigroups* (2026), full text visible at https://www.researchgate.net/publication/404721302_Explicit_Frobenius_Numbers_for_a_Lacunary_Three-Generated_Family_of_Numerical_Semigroups .
