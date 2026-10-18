# Exact Jaffard profile of the Tran–Nguyen realization domains
## Finding
Let \(k\) be a finite field and let \(3\le m\le n\). For the local domain \(D_{{m,n}}\) constructed by Tran and Nguyen, the ordinary dimensions are
\[
\dim D_{{m,n}}=m-2,\qquad
\dim D_{{m,n}}[X]=m,\qquad
\dim\operatorname{{Int}}(D_{{m,n}})=n.
\]
The corresponding valuative dimensions are exactly
\[
\dim_v D_{{m,n}}=n-1,\qquad
\dim_v D_{{m,n}}[X]=n,\qquad
\dim_v\operatorname{{Int}}(D_{{m,n}})=n.
\]
Hence the exact Jaffard defects are
\[
\dim_v D_{{m,n}}-\dim D_{{m,n}}=n-m+1
\]
and
\[
\dim_v D_{{m,n}}[X]-\dim D_{{m,n}}[X]=n-m.
\]
Thus \(D_{{m,n}}\) is never Jaffard, \(D_{{m,n}}[X]\) is Jaffard exactly when \(m=n\), and \(\operatorname{{Int}}(D_{{m,n}})\) is always Jaffard.

For the base family \(D_{{3,n}}\), write \(q=|k|\), \(F=X^q-X\), and let
\[
C_{{3,n}}=\{{c\in K:\text{{ there exists }}N\ge0\text{{ with }}cF^N\in\operatorname{{Int}}(D_{{3,n}})\}}\}
\]
be the weak coefficient transform introduced in the source. Then
\[
\dim C_{{3,n}}=\dim_v C_{{3,n}}=n-1.
\]
Moreover
\[
\operatorname{{Int}}(D_{{3,n}})[1/F]=C_{{3,n}}[X,1/F]
\]
has both Krull and valuative dimension \(n\). Thus the coefficient transform is a Jaffard core that realizes the full valuative dimension hidden behind the one-dimensional base domain.

## Assumptions and scope
Here \(\dim_v A\) denotes the valuative dimension, the supremum of the Krull dimensions of valuation overrings of the domain \(A\). A finite-dimensional domain is Jaffard exactly when its Krull and valuative dimensions coincide.

The statement concerns the explicit Tran–Nguyen realization domains for \(3\le m\le n\), obtained from their base domains by their suspension construction. It does not assert the same profile for every domain having the same pair \((\dim D[X],\dim\operatorname{{Int}}(D))\).

## Proof
Put \(K_{{m,n}}=\operatorname{{Frac}}(D_{{m,n}})\). For the base domain \(D_{{3,s}}\), the source constructs a quotient field \(\Omega_s\) algebraic over
\[
k(u_1,\ldots,u_{{s-2}},t),
\]
so
\[
\operatorname{{trdeg}}_k\Omega_s=s-1.
\]
The general domain \(D_{{m,n}}\) is obtained from the seed with \(s=n-m+3\) by exactly \(m-3\) suspensions, and each suspension replaces the quotient field by a one-variable rational function field. Therefore
\[
\operatorname{{trdeg}}_k K_{{m,n}}=(s-1)+(m-3)=n-1.
\]

The source records the general inequality
\[
\dim\operatorname{{Int}}(D)\le \dim_v D+1.
\]
Since \(\dim\operatorname{{Int}}(D_{{m,n}})=n\), this gives
\[
\dim_v D_{{m,n}}\ge n-1.
\]
For the reverse inequality, every valuation overring \(V\) of \(D_{{m,n}}\) contains \(k\) and has quotient field \(K_{{m,n}}\). The standard transcendence-degree bound, also used in the source, gives
\[
\dim V\le \operatorname{{trdeg}}_k K_{{m,n}}=n-1.
\]
Taking the supremum over valuation overrings proves
\[
\dim_v D_{{m,n}}=n-1.
\]
The standard polynomial identity for valuative dimension then yields
\[
\dim_v D_{{m,n}}[X]=\dim_v D_{{m,n}}+1=n.
\]

Because
\[
D_{{m,n}}[X]\subseteq\operatorname{{Int}}(D_{{m,n}})\subseteq K_{{m,n}}[X],
\]
the quotient field of \(\operatorname{{Int}}(D_{{m,n}})\) is \(K_{{m,n}}(X)\), of transcendence degree \(n\) over \(k\). Its ordinary dimension is already \(n\). Every valuation overring has dimension at most that transcendence degree, while valuative dimension is at least ordinary dimension, so
\[
\dim_v\operatorname{{Int}}(D_{{m,n}})=n.
\]
The stated Jaffard conclusions and defects now follow by subtracting the ordinary dimensions given in the source.

For \(D_{{3,n}}\), the weak coefficient transform \(C_{{3,n}}\) contains \(D_{{3,n}}\) and lies in its quotient field \(\Omega_n\); hence
\[
\operatorname{{Frac}}(C_{{3,n}})=\Omega_n
\]
and its quotient field has transcendence degree \(n-1\). The source constructs a strict prime chain of length \(n-1\) in \(C_{{3,n}}\), giving the lower bound \(\dim C_{{3,n}}\ge n-1\). The transcendence-degree bound gives the reverse inequality, so
\[
\dim C_{{3,n}}=n-1.
\]
Applying the same bound to every valuation overring shows
\[
\dim_v C_{{3,n}}=n-1,
\]
so \(C_{{3,n}}\) is Jaffard.

Finally, the source proves
\[
\operatorname{{Int}}(D_{{3,n}})[1/F]=C_{{3,n}}[X,1/F]
\]
and exhibits a prime chain of length \(n\) in this localization. Since \(C_{{3,n}}\) is Jaffard of dimension \(n-1\), its polynomial ring has dimension \(n\), and localization cannot increase dimension. Hence the displayed localization has Krull dimension exactly \(n\). Its valuative dimension is at most that of \(C_{{3,n}}[X]\), namely \(n\), and at least its Krull dimension, so it too is Jaffard of dimension \(n\).

## Verification
The argument is symbolic and dimension-theoretic; no finite experiment is used as a substitute for proof. The checks were replayed directly against the source construction: the base quotient field has transcendence degree \(s-1\); each suspension adds one transcendence variable; the source gives \(\dim\operatorname{{Int}}(D_{{m,n}})=n\); and the weak coefficient transform carries a prime chain of length \(n-1\), while its localized polynomial ring carries a chain of length \(n\). These facts force all upper and lower bounds above to meet.

The proof does not compute individual valuation overrings or classify their value groups. It only determines their maximal possible rank through the quotient-field transcendence degree and the matching lower bound forced by the integer-valued polynomial ring.

## Relationship to prior work
Tran and Nguyen prove the ordinary dimension profile of \(D_{{m,n}}\), and for the base construction they explicitly note that \(D_{{3,n}}\) is not Jaffard. They also introduce the weak coefficient transform and construct the long prime chains used above. Their statements do not give the exact valuative dimension of the realization domains, the exact Jaffard defects, the Jaffard criterion for their polynomial rings, or the equality \(\dim C_{{3,n}}=\dim_v C_{{3,n}}=n-1\).

General dimension theory supplies relations between valuative dimension, polynomial rings, and rings of integer-valued polynomials. Those relations alone do not determine the present numerical profile until they are combined with the specific quotient fields, ordinary dimensions, and coefficient-transform chains in this construction.

## Limitations
The theorem applies to the explicit realization domains of the cited construction and, for the coefficient-transform statement, to its base family. It does not classify the valuation overrings themselves, nor does it show that every domain realizing the same ordinary dimension pair has the same valuative dimension. The originality comparison is strongest against the motivating preprint, the published-finding index, and the checked own-ledger claims; older dimension-theory literature could contain an equivalent consequence stated in a more abstract pullback language.

## References
1. Viet-Hoang Tran and Tan M. Nguyen, *On the Krull dimensions of rings of integer-valued polynomials and polynomial rings*, arXiv:2610.00115v1, 9 September 2026.
