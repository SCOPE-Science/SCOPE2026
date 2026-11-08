# Sharp signed three-denomination postage ranges for all orders congruent to nine modulo twelve

## Finding

For an integer \(h\ge 1\), write \(hA\) for the set of sums of **exactly** \(h\) (not necessarily different) members of a set \(A\subset\mathbb Z\). Define \(n_h^{\flat}(2)\) to be the maximum \(T\) such that \([0,T]\subseteq hA\) for some three-element \(A\) with a negative member.

**Theorem.** For every integer \(t\ge0\), put \(b=2t+2\), \(h=6b-3=12t+9\), and \(A_b=\{-b,b,2b+1\}\). Then
\[
[0,9b^2-3]\subseteq hA_b,\qquad
n_h^{\flat}(2)=9b^2-3=\frac{h^2+6h+1}{4}-1.
\]
Thus the strict inequality against the classical three-denomination optimum is sharp for the infinite progression \(h\equiv9\pmod{12}\).

## Assumptions and scope

All parameters are integers; \(b\ge2\) is even, and \(t\) ranges over the nonnegative integers. Three denominations are distinct, at least one is negative, and representations use exactly \(h\) summands, including repetitions. No assertion is made about odd orders in other residue classes. The primary classification is additive number theory (MSC2020 11B13).

## Proof

**1. Universal strict upper bound for odd orders.** For arbitrary odd \(h=2m+1\ge3\), let \(N=m^2+4m+2=(h^2+6h+1)/4\). Suppose a set \(A=\{a,a+x,a+y\}\), where \(a<0\) and \(1\le x<y\), represented all of \([0,N]\). A sum has the form \(ha+sx+ry\), with \(s,r\ge0\) and \(s+r\le h\). Because \([0,h+1]\subseteq hA\), subtracting representations of zero and one gives \(\gcd(x,y)=1\). Moreover, among representations of \(h+2\) integers in \([0,h+1]\), two have the same coefficient \(s\in[0,h]\), so their positive difference is a nonzero multiple of \(y\); hence \(y\le h+1\).

Consider the residue class \(ha-x\pmod y\). Its unique representative \(u\in[0,y-1]\) and its last representative \(v\in[N-y+1,N]\) are both in \(hA\). For any such representation, coprimality implies \(s\equiv-1\pmod y\), so \(s\ge y-1\). Hence
\[
ha+(y-1)x\le u\le y-1,
\]
and
\[
N-y+1\le v\le ha+hy-(y-1)(y-x).
\]
Equivalently,
\[
N-hy+(y-1)(y-x-1)\le ha\le(y-1)(1-x).
\]
Subtracting yields \(0\le hy-(y-1)(y-2)-N=-(y-m-2)^2\). Thus \(y=m+2\) and both bounds coincide, giving
\[
ha=(m+1)(1-x).
\]
Since \(a<0\), we have \(2\le x<y\), hence \(1\le x-1\le m\). But \(2(m+1)=h+1\) implies \(h\mid(x-1)\), contradiction. Consequently \(n_h^{\flat}(2)\le N-1\) for all odd \(h\ge3\). This elementary derivation is included to make the upper bound independent of the verification script; it is also established in the cited 2026 primary source.

**2. Explicit coverage for \(h=6b-3\) with even \(b\).** Put \(x=2b\) and \(y=3b+1\). The proposed set is \(A_b=-b+\{0,x,y\}\). Because \(b\) is even,
\[
\gcd(x,y)=\gcd(2b,3b+1)=\gcd(2,b+1)=1.
\]
For each \(s\in[0,y-1]\), the numbers realized with exactly that coefficient of \(x\) form the arithmetic progression
\[
S_s, S_s+y,\ldots,E_s,\quad
S_s=-hb+sx,\qquad E_s=S_s+(h-s)y.
\]
There is an available progression for every residue modulo \(y\) because \(x\) is invertible modulo \(y\), and \(y-1=3b\le h\). Write \(s=3b-k\) with \(0\le k\le3b\), and let \(T=9b^2-3\). Direct calculation yields
\[
S_s=3b-2bk,\qquad E_s=T-3b+(b+1)k,\qquad T\equiv 3b-1\pmod{3b+1}.
\]
Let \(r_s\in[0,y-1]\) be the least nonnegative integer congruent to \(S_s\pmod y\). For \(k\ge2\), \(S_s\le-b<0\le r_s\); for \(k=0,1\), respectively \(S_s=r_s=3b\) and \(S_s=r_s=b\). Thus each progression starts no later than the first nonnegative integer of its residue.

For \(k\ge3\), \(E_s\ge T+3\), so its progression continues beyond the desired upper endpoint. For \(k=0,1,2\), the last integers not exceeding \(T\) in the respective residues \(r_s=3b,b,2b+1\) are
\[
T-3b,\quad T-2b+1,\quad T-b+2,
\]
which agree with \(E_s\) in those three cases. Hence every residue progression meets the full interval \([0,T]\) in its residue class. Their union covers every integer in \([0,T]\). Combining with Step 1 proves the theorem. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs the finite sumset in two independent ways for even \(b=2,4,\ldots,100\): directly enumerating choices of the three summand multiplicities, and by checking the residue-progression endpoint inequalities above. Each case verifies inclusion of \([0,9b^2-3]\), exclusion of the next integer from the exhibited construction, and coprimality. Run `python verify.py` to reproduce the checks. Finite testing does not establish the infinite theorem; Steps 1–2 do.

## Relationship to prior work

Van Doorn, Monticone, and Nathanson (arXiv:2610.19470, 14 October 2026) establish the exact classical optimum and the strict inequality \(n_h^{\flat}(2)<n_h(2)\) for all odd \(h\). Their Section 4 explicitly describes the exact odd-order values as open, and contains no construction proving equality with the one-unit deficit on the progression \(h\equiv9\pmod{12}\). The present proof supplies this missing lower construction; the upper inequality is an already-known premise, here reproduced directly. Nathanson (arXiv:2605.26425) provides the antecedent problems on structures of additive bases. The classical nonnegative optimum is due to Stöhr (1955), a different admissibility class.

## Limitations

Only orders \(h\equiv9\pmod{12}\) are resolved; the complete odd-order classification remains open. The explicit construction proves existence of an optimal signed basis, not uniqueness or a classification of all extremizers. Priority is assessed against the available full text and indexed material, not an exhaustive archive of every unpublished calculation. The numerical verification is supplementary.

## References

- W. van Doorn, P. Monticone, and M. B. Nathanson, *Positivity and negativity for h-bases for n*, arXiv:2610.19470v1 (14 October 2026), especially Sections 1, 2, and 4. https://arxiv.org/html/2610.19470v1
- M. B. Nathanson, *Problems in additive number theory, VII: The structure of additive h-bases for n*, arXiv:2605.26425 (2026). https://arxiv.org/abs/2605.26425
- A. Stöhr, *Gelöste und ungelöste Fragen über Basen der natürlichen Zahlenreihe*, J. Reine Angew. Math. 194 (1955), 40–65, 111–140.
