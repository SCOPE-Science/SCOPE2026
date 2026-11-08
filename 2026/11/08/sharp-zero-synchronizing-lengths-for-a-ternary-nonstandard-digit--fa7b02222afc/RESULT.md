# Sharp zero-synchronizing lengths for a ternary nonstandard digit family

## Finding

For every integer \(k\geq1\), the ternary complete-residue digit set
\[
D_k=\{0,1,3^{k+1}-1\}
\]
has a finite zero-carry automaton whose **minimum zero-synchronizing input length is exactly \(2k+1\)**. Moreover at least \((3^k+1)/2\) distinct words realize this minimum. This provides a sharp quantitative synchronization law for an infinite family of nonstandard digit systems.

## Assumptions and scope

Fix \(k\ge1\). Set
\[
B=3^{k+1},\quad M=(B-1)/2,\quad H=(3^k-1)/2,
\quad D=\{0,1,B-1\}.
\]
The residue representatives of \(D\) modulo \(3\) are \(d_0=0\), \(d_1=1\), and \(d_2=B-1\). For input \(a\in\{0,1,2\}\), define
\[
h_a(c)=\frac{a+c-d_{[a+c]_3}}3
\]
on the state set \(K=\{-M,-M+1,\ldots,0\}\), where brackets denote the least nonnegative residue. All these transitions preserve \(K\), because \(-M\le (a+c-d)/3\le0\) for \(c\in K\). A word \(a_0\cdots a_{\ell-1}\) is read with \(a_0\) the least significant digit and is *zero-synchronizing* when the composition \(h_{a_{\ell-1}}\circ\cdots\circ h_{a_0}\) sends every member of \(K\) to \(0\). Its minimum possible length is denoted \(\ell(D)\).

**Theorem.** \(\ell(D_k)=2k+1\). More precisely, let \(v\) range through the integers \(0\le v\le H\); write the ordinary base-\(3\) expansion of \(v\) in exactly \(k\) digits, least significant first, including leading zeros in the usual most-significant sense. Appending \(k+1\) consecutive input digits equal to \(1\) gives a zero-synchronizing word of minimum length. Consequently at least \(H+1=(3^k+1)/2\) minimum-length words exist. No assertion that this is the complete set of minimum words is needed.

## Proof

**Step 1: Interval criterion.** Define the finite representation set
\[
T_\ell=\left\{\sum_{j=0}^{\ell-1}\delta_j3^j:\delta_j\in D\right\}.
\]
This set has exactly \(3^\ell\) members, one in each residue class modulo \(3^\ell\), because \(D\) is a complete residue digit set. For an input word \(w=a_0\cdots a_{\ell-1}\), let \(A=\sum_{j<\ell}a_j3^j\). Iterating the carry equation gives, for each initial carry \(c\),
\[
A+c=\sum_{j<\ell}d_{[a_j+c_j]_3}3^j+3^\ell c_\ell.
\]
The digit sequence on the right is uniquely determined by the residue of \(A+c\) modulo successive powers of \(3\). Hence \(c_\ell=0\) exactly when \(A+c\in T_\ell\). Thus \(w\) is zero-synchronizing if and only if
\[
[A-M,A]\cap\mathbb Z\subseteq T_\ell. \tag{1}
\]
In particular the longest consecutive run of \(T_\ell\) must contain at least \(M+1\) members.

**Step 2: Every initial run has length at most two.** For \(1\le\ell\le k+1\), rewrite each digit \(B-1\) as \(B+(-1)\). Any represented element can then be written uniquely in the form
\[
 x=U+B V,\quad U=\sum_{j<\ell}e_j3^j,\quad
 V=\sum_{\substack{j<\ell\\e_j=-1}}3^j,
\qquad e_j\in\{-1,0,1\}.
\]
Here \(|U|\le(3^\ell-1)/2\) and \(V\) has only ordinary ternary digits \(0,1\). Suppose \(x,x+1\in T_\ell\). From \(1=(U'-U)+B(V'-V)\) and \(|U'-U|\le3^\ell-1\le B-1\), we must have \(V'=V\), except possibly when \(\ell=k+1\), \(U=M\), \(U'=-M\), and \(V'-V=1\). But in that exceptional extreme the all-\(+1\) digit string has \(V=0\), and the all-\(-1\) string has \(V'=M>1\), a contradiction. Thus \(V'=V\). Three consecutive represented integers would therefore have three consecutive values \(U,U+1,U+2\) and the same \(V\). Their least significant balanced ternary digits run through \(-1,0,1\) in some order; but \(V\bmod3\) is \(1\) for digit \(-1\) and \(0\) for the other two, a contradiction. Therefore the longest consecutive run length \(r(\ell)\) satisfies \(r(\ell)\le2\) for \(1\le\ell\le k+1\).

**Step 3: The lower bound on word length.** Among every three consecutive integers, one is congruent to \(1\pmod3\). Every \(x\in T_\ell\) with that residue must have lowest nonstandard digit \(1\), so \((x-1)/3\in T_{\ell-1}\). The \(1\bmod3\) members of an interval of \(L\) consecutive represented integers yield at least \(\lfloor L/3\rfloor\) consecutive members of \(T_{\ell-1}\). Therefore
\[
r(\ell)\le 3r(\ell-1)+2. \tag{2}
\]
Starting from \(r(k+1)\le2\), at most \(k-1\) applications give \(r(2k)\le3^k-1\). Since \(M+1=(3^{k+1}+1)/2>3^k-1\), criterion (1) excludes synchronization at length \(2k\). Moreover \(T_j\subseteq T_{2k}\) for \(j<2k\), by padding with high zero digits, so the same exclusion holds for all shorter lengths. Thus \(\ell(D)\ge2k+1\).

**Step 4: Construction at the lower bound.** Put \(A=3^kM\). The identities
\[
A=BH+3^k,\qquad A-M=BH-H,\qquad A+H=BH+M \tag{3}
\]
follow from the definitions. We will show
\[
[BH-H,BH+M]\cap\mathbb Z\subseteq T_{2k+1}. \tag{4}
\]
For any \(t\in[-H,M]\cap\mathbb Z\), write its unique balanced ternary expansion \(t=\sum_{j=0}^{k}e_j3^j\), where \(e_j\in\{-1,0,1\}\). The top digit cannot be \(-1\), since that would give \(t\le-3^k+H=-H-1\). Define \(V=\sum_{0\le j<k:e_j=-1}3^j\). In the low \(k+1\) places replace every digit \(-1\) by \(B-1\), leaving \(0,1\) unchanged. Those choices contribute \(t+BV\). Now \(H=\sum_{j=0}^{k-1}3^j\), and since the ternary digits of \(V\) all lie in \(\{0,1\}\), those of \(H-V\) also lie in \(\{0,1\}\). Fill the high places \(k+1,\ldots,2k\) with the ordinary digits of \(H-V\). Their contribution is \(B(H-V)\), giving \(BH+t\). This proves (4).

For each \(0\le v\le H\), choose the input whose first \(k\) digits represent \(v\) and whose next \(k+1\) digits are all \(1\). Its integer value equals \(A+v\); by (3) and (4), \([A+v-M,A+v]\cap\mathbb Z\) lies in \(T_{2k+1}\). Criterion (1) makes it zero-synchronizing. There are \(H+1=(3^k+1)/2\) such different inputs. Combined with the lower bound, this completes the proof. \(\square\)

## Verification

The accompanying standalone `verify.py` calculates represented-digit sets and their maximal consecutive intervals, verifies exact absence of shorter zero-synchronizing words for \(1\le k\le4\), enumerates all shortest words there, and independently applies the carry maps to constructed witnesses through \(k=8\). In particular, the computed minimum lengths for the four exhaustive cases are \(3,5,7,9\). These calculations are finite corroboration only; Steps 1–4 are a uniform proof for all positive integers \(k\).

Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Cruz, Loquias, and Thuswaldner study addition transducers and attractors for complete-residue matrix digit systems (arXiv:2507.06158v1, 8 July 2025, primary MSC 11A63). Their actual results address two-dimensional expanding rational matrices with fixed collinear digits and do not yield a sharp zero-reset length for the present scalar ternary family. Zhou's subsequent paper (arXiv:2611.07446v1, first posted 5 November 2026) proves a general qualitative zero-synchronization criterion for complete-residue digit systems and explicitly raises quantitative length bounds in Section 6.3. The present theorem supplies an exact sharp infinite-family answer, not a new proof of that general qualitative criterion. Other known slow-reset automata studies have different transition maps and do not imply this digit-arithmetic calculation.

## Limitations

The theorem concerns the specified scalar base-\(3\) digit family; it is not a general uniform upper bound for all complete-residue digit sets. We prove a lower bound on the number of shortest words, not an exhaustive count for every \(k\). The work has not undergone independent mathematical audit; the accompanying tests cannot substitute for the universal symbolic proof. Earlier unindexed equivalent results remain a literature-priority risk.

## References

1. A. G. R. Cruz, M. J. C. Loquias, J. M. Thuswaldner, *Addition Automata and Attractors of Digit Systems Corresponding to Expanding Rational Matrices*, arXiv:2507.06158v1, 2025-07-08, https://arxiv.org/html/2507.06158v1.
2. N. H. Zhou, *Periodic counting, carry synchronization, and primes in nonstandard numeration systems*, arXiv:2611.07446v1, 2026-11-05, https://arxiv.org/html/2611.07446v1, especially Sections 4 and 6.3.
3. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003 (background on numeration automata).
