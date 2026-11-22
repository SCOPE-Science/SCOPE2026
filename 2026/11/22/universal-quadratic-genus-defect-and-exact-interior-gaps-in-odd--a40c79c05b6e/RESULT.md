# Universal quadratic genus defect and exact interior gaps in odd consecutive coin triples

## Finding

For each odd integer \(a=2m+1\ge5\), let \(d_a(n)\) count ordered-coordinate nonnegative integer solutions of
\[
a x+(a+1)y+(a+2)z=n,
\]
and let \(G_p(a)=\{n\in\mathbb Z_{\ge0}:d_a(n)\le p\}\). The entire second parameter phase above the classical small-threshold range has a uniform exact gap-set formula.

For every integer \(1\le t\le m+2\), put \(p=m+t\), \(L_t=a(a+t)\), and \(J_t=\lfloor(t-1)/3\rfloor\). For \(1\le h\le J_t\), define the *interior nongap interval*
\[
I_{t,h}(a)=\bigl\{a(a+t-h)+r:\ 2h\le r\le 2(t-2h-1)\bigr\}.
\]
These intervals are pairwise disjoint and lie strictly below \(L_t\). The complete generalized gap set is
\[
\boxed{G_{m+t}(a)=\{0,1,\ldots,L_t-1\}\setminus\bigcup_{h=1}^{J_t}I_{t,h}(a).}
\]
In particular, the generalized gap count (the \(p\)-genus, including zero) is
\[
\boxed{N_{m+t}(a)=|G_{m+t}(a)|=a(a+t)-\left\lfloor\frac{(t-2)^2}{3}\right\rfloor.}
\]
The already-known generalized Frobenius number on this parameter range is \(g_{m+t}(a)=a(a+t)-1\). Thus the exact *genus–Frobenius deficit*
\[
\boxed{g_{m+t}(a)+1-N_{m+t}(a)=\left\lfloor\frac{(t-2)^2}{3}\right\rfloor}
\]
is **independent of the odd denomination parameter** even though both invariants grow quadratically in \(a\). It first becomes positive at \(t=4\), where \(I_{4,1}(a)=\{a(a+3)+2\}\), creating precisely one internal nongap between two gap intervals. At \(t=5\) the defect is three; for large \(t\), up to the stated parameter boundary, it grows quadratically. The new result is the exact gap-set topology and genus law, not the already established Frobenius endpoint.

## Assumptions and scope

The first denomination \(a\) is an odd integer at least five. The threshold runs through the complete second Frobenius phase \(p=m+1,\ldots,a+1\), equivalently \(1\le t\le m+2\). We count \(n=0\) as having one representation and include it in each \(G_p(a)\) at these levels. All finite intervals use integer endpoints. The case \(a=3\), even first denominations, larger \(p\), and nonconsecutive progressions are outside scope.

## Proof

Every integer \(n\ge0\) has a unique expression \(n=aq+r\), with \(q\ge0\), \(0\le r<a\). In a representation let \(c=x+y+z\). Since \(n=ac+y+2z\), there is a unique \(j\ge0\) such that \(c=q-j\) and \(y+2z=r+ja\). For given \(j\), the number of solutions is exactly
\[
B(q,r,j)=\max\!\left(0,\left\lfloor\frac{r+ja}{2}\right\rfloor-\max(0,r+ja-(q-j))+1\right).
\]
The corresponding \(x\) is uniquely determined, and \(d_a(aq+r)=\sum_{j=0}^{q}B(q,r,j)\). This elementary coin-count identity is not claimed as new.

Set \(a=2m+1\) and \(q=a+s\) with \(0\le s\le m+2\). For all \(j\ge3\) the inequality \(r+ja\ge3a>2(a+s-3)\ge2(q-j)\) makes \(B(q,r,j)=0\). For \(j=0,1,2\), the elementary floor computations yield
\[
\begin{aligned}
B(a+s,r,0)&=\lfloor r/2\rfloor+1,\\
B(a+s,r,1)&=m+\lfloor(r+1)/2\rfloor+1-\max(0,r-s+1),\\
B(a+s,r,2)&=\max(0,s-1-\lceil r/2\rceil).
\end{aligned}
\]
The expression on the second line is nonnegative: if \(r\ge s-1\) it equals \(m+s-\lfloor r/2\rfloor\ge s\ge0\), while if \(r<s-1\) it is plainly positive. Thus there is no omitted outer truncation.

Summing and simplifying gives the universal *tent-height identity*
\[
\boxed{d_a(a(a+s)+r)=m+s+1+E_s(r),\qquad E_s(r)=[s-1-\lceil r/2\rceil]_+-[s-1-r]_+,}
\]
where \([v]_+=\max(v,0)\). In particular \(E_s(r)\ge0\), and it is exactly \(\lfloor r/2\rfloor\) if \(0\le r\le s-1\), and \(\max(0,s-1-\lceil r/2\rceil)\) if \(r\ge s-1\). This is a complete exact formula for every claimed \(s,r,a\), including the boundary \(s=0\).

Appending one coin of value \(a\) injects every representation of \(n\) into a representation of \(n+a\), so \(d_a(n+a)\ge d_a(n)\). For each \(t\) in scope, the band \(q=a+t\) has \(d_a(qa+r)\ge m+t+1\) at all residues \(r\), so all \(n\ge L_t\) have more than \(m+t\) representations. For \(q<a\), compare to \(q=a\) at the same residue to see \(d_a(qa+r)\le m+1\le m+t\). Within the remaining bands \(q=a+s\), \(0\le s<t\), the nongaps at level \(p=m+t\) are exactly the residues with
\[
E_s(r)\ge t-s.
\]
Writing \(h=t-s\ge1\), the tent-height expression proves the exact equivalence
\[
E_s(r)\ge h\quad\Longleftrightarrow\quad 2h\le r\le2(s-1-h).
\]
There are solutions only when \(3h\le t-1\), i.e. \(1\le h\le J_t\). For each such \(h\), set \(s=t-h\): the corresponding nongaps are precisely \(I_{t,h}(a)\). Their right endpoint residue is at most \(2t-6\le2m-2<a\), so no interval is truncated at the residue boundary. Different \(h\) correspond to different quotient bands, so all intervals are disjoint. Conversely, no other nongap exists below \(L_t\). This proves the complete gap-set formula.

The number of integers in \(I_{t,h}(a)\) is \(2t-6h-1\). Summing over \(h=1,\ldots,J_t\) yields the count of interior nongaps:
\[
\sum_{h=1}^{J_t}(2t-6h-1)=J_t(2t-3J_t-4)=\left\lfloor\frac{(t-2)^2}{3}\right\rfloor.
\]
The final equality follows by writing \(t-1=3J_t+u\), \(u\in\{0,1,2\}\), and checking the three residues. The rightmost residue \(r=a-1\) of the preceding band \(s=t-1\) has \(E_s(r)=0\), so the last gap is indeed \(L_t-1\). Subtracting the interior nongap count from \(L_t\) proves the genus and deficit formulas. \(\square\)

## Verification

The standalone Python script `check_gap_profile.py` uses an unrestricted-coin dynamic program, an independently implemented number-of-coins sum, and direct enumeration of triples for small instances. It tests the tent-height identity for every band \(0\le s\le m+2\), every residue, every odd \(a\) from 5 through 121, and tests the complete gap-set predicates and deficit for **every** \(1\le t\le m+2\), including the full tail after the claimed maximal gap. The completed checker passed 160,598 band comparisons, 22,154,736 gap predicates and 1,351 direct triple coefficients. These finite checks corroborate the result; the proof above establishes its infinite parameter range. Run `python3 check_gap_profile.py` with Python 3 standard library.

## Relationship to prior work

Komatsu and Ying [1] developed the generalized Frobenius and Apéry theory of three-term arithmetic progressions for \(0\le p\le\lfloor a/2\rfloor\). The second phase here begins just above that bound. A later exact three-phase theorem for *consecutive* denominations [2] determines the maximal gaps \(g_p\) through \(p=2a\), and its proof also gives a generic exact denumerant sum. Neither source states the full interior nongap intervals, the closed universal quadratic genus defect, or the universal quadratic defect in the odd second phase. This work does not claim a new formula for the maximal gap or for the generic denumerant itself. Subwattanachai's general three-variable Frobenius theorem [3] requires additional divisibility not satisfied by the odd consecutive triple. Previously stated results at the first odd post-boundary threshold and for the even parity branch do not determine the complete odd-parameter second-phase genus law.

## Limitations

The result is limited to the entire second generalized Frobenius phase for odd consecutive denominations; it does not address the third phase, even first denominations or arbitrary progression steps. The proof uses and specializes a known exact denumerant identity; this creates a priority risk that the quadratic genus law may be an implicit corollary in literature not found in the comparisons. No independent mathematical audit has been performed.

## References

[1] T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052, first submitted 27 June 2022; *Symmetry* 15 (2023), 1328. https://arxiv.org/abs/2206.13052

[2] *Three exact phases of generalized Frobenius numbers for three consecutive denominations* (2026), publicly available research note, identifier 6dc430dbb315; Frobenius theorem and elementary denumerant summation.

[3] K. Subwattanachai, *Generalized Frobenius Number of Three Variables*, arXiv:2309.09149, first submitted 17 September 2023, Theorem 1. https://arxiv.org/abs/2309.09149
