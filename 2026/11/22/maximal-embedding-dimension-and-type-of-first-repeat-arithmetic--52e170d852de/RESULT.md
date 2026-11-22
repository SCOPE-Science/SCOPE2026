# Maximal embedding dimension and type of first-repeat arithmetic-progression semigroups

## Finding

For coprime integers \(a\ge3\) and \(d\ge1\), put \(u=a\), \(v=a+d\), and \(w=a+2d\). Let \(r(n)\) count solutions \((x,y,z)\in\mathbb N_0^3\) of \(ux+vy+wz=n\), with distinct triples counted separately. Define
\[
S_0=\langle u,v,w\rangle,\qquad S=\{0\}\cup\{n\ge1:r(n)\ge2\},\qquad m=2v.
\]
Then \(S\) is a numerical semigroup of multiplicity \(m\), embedding dimension \(m\), and pseudo-Frobenius type \(m-1\). In particular, its embedding dimension and type attain their respective general upper bounds at every admissible parameter.

More precisely, writing \(a=2q\) or \(a=2q+1\), respectively,
\[
\begin{aligned}
a=2q:&\quad S\setminus\{0\}=(m+S_0)\cup(B+S_0),\quad B=qw=(q+d)u,\\
a=2q+1:&\quad S\setminus\{0\}=(m+S_0)\cup(B+S_0)\cup(C+S_0),\\
&\qquad B=v+qw=(q+d+1)u,\qquad C=(q+1)w=(q+d)u+v.
\end{aligned}
\]

## Assumptions and scope

All assertions hold for integers \(a\ge3\), \(d\ge1\) and \(\gcd(a,d)=1\), with no assumption about \(d<a\). The count is of *distinct nonnegative coefficient triples*, not just factorization lengths. The zero element is adjoined explicitly because it has one empty representation. For a numerical semigroup, the *multiplicity* is its smallest positive element, the *embedding dimension* the number of minimal positive additive generators, and a *pseudo-Frobenius number* is an integer \(h\notin S\) for which \(h+s\in S\) for all positive \(s\in S\). The type is their number.

## Proof

**1. Representation ideal.** The relation \(u+w=2v=m\) gives two distinct representations of \(m\). The displayed identities for \(B\) and \(C\) likewise give two distinct representations. Adding any fixed element of \(S_0\) to the two representations proves that each displayed translate lies in \(S\setminus\{0\}\).

Conversely, take two distinct factorizations of \(n\). If either uses two or more \(v\)-coins, its value lies in \(m+S_0\); hence suppose both have \(v\)-coin counts zero or one. If those counts agree, the two factorizations express the same number using only \(u,w\) after cancelling the common \(v\). When \(a=2q\), \(\gcd(u,w)=2\), and two different such factorizations differ by at least \(q\) copies of \(w\) (since \(u/\gcd(u,w)=q\)). Thus one uses at least \(q\) copies of \(w\), putting \(n\) in \(B+S_0\). When \(a=2q+1\), \(\gcd(u,w)=1\), so one uses at least \(a\) copies of \(w\). Since \(aw=B+(q+d)u\), again \(n\in B+S_0\).

If the two factorizations use different counts of \(v\), choose labels so the first has zero \(v\)-coins and the second has one. Reducing modulo \(u=a\) and cancelling the invertible \(d\) gives \(2(z_0-z_1)\equiv1\pmod a\). For even \(a\) this is impossible. For odd \(a=2q+1\), every integer solution satisfies \(z_0-z_1\ge q+1\) or \(z_0-z_1\le-q\). In the first case the zero-\(v\) factorization contains \(q+1\) copies of \(w\), so \(n\in C+S_0\); in the second the one-\(v\) factorization contains \(q\) copies of \(w\) and one of \(v\), so \(n\in B+S_0\). This proves both exact unions.

Because \(\gcd(u,v,w)=1\), \(S_0\) is cofinite, and the union contains the cofinite ideal \(m+S_0\). It is closed under addition because adding to any member with at least two factorizations preserves two distinct factorizations; adjoining zero therefore gives a numerical semigroup. Each \(B,C\) strictly exceeds \(m\), so the union makes \(m\) its least positive element.

**2. The sum-minus-multiplicity property.** We prove
\[
\forall x,y\in S\setminus\{0\}:\quad x+y-m\in S.\tag{1}
\]
By the exact unions, write \(x=h_i+s\) and \(y=h_j+t\) for \(s,t\in S_0\) and \(h_i,h_j\) among \(m,B\), or among \(m,B,C\). It suffices to verify \(h_i+h_j-m\in S\). Cases involving \(m\) are immediate. If \(a=2q\), \(q\ge2\), then
\[
2B-2m=(q-2)w+(q+d-2)u\in S_0,
\]
so \(2B-m=m+(2B-2m)\in S\).

If \(a=2q+1\) and \(q\ge2\), the three remaining base checks are
\[
\begin{aligned}
2B-2m&=(d+1)u+(2q-3)v,\\
B+C-2m&=du+(2q-2)v,\\
2C-2m&=(d-1)u+(2q-1)v.
\end{aligned}
\]
All coefficients are nonnegative; adding \(m\) places every base difference in \(S\). For the sole boundary case \(a=3\), \(q=1\), instead \(2B-m=C\in S\), while \(B+C-2m=du\in S_0\) and \(2C-2m=(d-1)u+v\in S_0\). This establishes (1) in every case.

**3. Embedding dimension and type.** The Apéry set \(\operatorname{Ap}(S,m)=\{s\in S:s-m\notin S\}\) has exactly \(m\) elements, one for each residue class modulo \(m\), including zero. Any two positive elements of \(S\) have sum outside the nonzero Apéry set, by (1). Conversely, any decomposable positive element cannot lie in the nonzero Apéry set, again by (1). Hence the \(m-1\) nonzero Apéry elements are precisely the minimal generators other than \(m\), giving \(e(S)=m\).

For each nonzero Apéry element \(h\), the integer \(h-m\) lies outside \(S\), and (1) gives \((h-m)+s\in S\) for every positive \(s\in S\). Therefore all \(m-1\) nonzero Apéry elements yield distinct pseudo-Frobenius numbers. Conversely, every pseudo-Frobenius number \(f\) satisfies \(f+m\in\operatorname{Ap}(S,m)\setminus\{0\}\), so there are no others. Thus the type equals \(m-1\).

## Verification

`VERIFY.py` performs an independently coded dynamic-programming count of every three-coin factorization, compares the exact ideal unions at every index within explicit finite ranges, and independently enumerates the minimal generators and pseudo-Frobenius numbers for the tested parameters. It covers all coprime pairs with \(3\le a\le20\) and \(1\le d\le8\), including both parity cases and \(a=3\). Execute `python3 VERIFY.py`. These bounded checks corroborate, but do not establish, the universal claims; Steps 1–3 are the infinite proof.

## Relationship to prior work

Komatsu and Ying (2022, 2023) determine the \(p\)-Frobenius numbers and related Apéry/genus invariants for the same triple of arithmetic-progression generators; the case \(p=1\) motivates the first-repeat semigroup studied here. Their formulas do not supply the present full ideal decomposition, maximal embedding dimension, or complete pseudo-Frobenius type. Their subsequent work develops general \(p\)-semigroup theory and the definition of \(p\)-embedding dimension but does not establish the present two-parameter theorem. Komatsu (2024) studies \(p\)-almost symmetry and \(p\)-Arf notions, rather than the present all-parameter classification. Chapman and coauthors (2010) treat factorizations *of the same length*, a strictly narrower subset than factorizations merely distinct; in an arithmetic triple the former are generated by the length-preserving relation \(u+w=2v\). The new result also accounts for the unequal-length coincidence ideals \(B+S_0\) and, for odd \(a\), \(C+S_0\). Standard maximal-embedding-dimension bounds are known, but they alone do not imply that these first-repeat semigroups attain equality.

## Limitations

The theorem treats only the first-repeat threshold (at least two representations), not all higher denumerant thresholds or non-arithmetic generator triples. No independent external audit or historical-priority certificate has been performed. The literature comparison is limited to the cited and searched sources; an unrecognized equivalent in a general semigroup result remains possible.

## References

1. T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first posted 27 June 2022), https://arxiv.org/abs/2206.13052.
2. T. Komatsu and H. Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties*, arXiv:2207.08962 (2022), https://arxiv.org/abs/2207.08962.
3. T. Komatsu, *\(p\)-numerical semigroups with \(p\)-symmetric properties, II*, arXiv:2409.02394 (2024), https://arxiv.org/abs/2409.02394.
4. S. T. Chapman, P. A. García-Sánchez, D. Llena, A. Marshall and J. C. Rosales, *Elements in a Numerical Semigroup with Factorizations of the Same Length*, Canadian Mathematical Bulletin, DOI:10.4153/CMB-2010-068-3 (2010), https://doi.org/10.4153/CMB-2010-068-3.
5. T. Bogart, C. O'Neill and K. Woods, *When Is a Numerical Semigroup a Quotient?*, Bulletin of the Australian Mathematical Society, published online 10 February 2023, https://doi.org/10.1017/S0004972723000035.
