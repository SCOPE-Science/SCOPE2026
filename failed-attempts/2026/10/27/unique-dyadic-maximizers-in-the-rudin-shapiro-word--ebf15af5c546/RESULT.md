# Unique dyadic maximizers in the Rudin–Shapiro word

## Finding

Let \(\sigma\) be the length-two substitution
\[
\sigma(a)=ab,\qquad \sigma(b)=ac,\qquad \sigma(c)=db,\qquad \sigma(d)=dc,
\]
and let \(\tau(a)=\tau(b)=1\), \(\tau(c)=\tau(d)=-1\). Write
\(\mathbf r=\tau(\sigma^\omega(a))\) for the resulting one-sided Rudin–Shapiro sign word.

For every integer \(k\ge2\), among all distinct factors of \(\mathbf r\) of length \(2^k\), exactly one factor word attains the largest possible sign-sum. Put
\[
j_k=\frac{2\cdot4^{\lfloor k/2\rfloor}+1}{3}.
\]
The maximizing factor is the suffix of \(\tau(\sigma^k(b))\) of length \(2^k-j_k\), followed by the prefix of \(\tau(\sigma^k(a))\) of length \(j_k\), when \(k\) is even. When \(k\) is odd, replace \(b\) in the suffix by \(c\). The adjacent block pair is therefore \(ba\) for even \(k\) and \(ca\) for odd \(k\).

The maximum sign-sum is
\[
M_k=
\begin{cases}
3\cdot2^{k/2}-2,&k\text{ even},\\
4\cdot2^{(k-1)/2}-2,&k\text{ odd}.
\end{cases}
\]
“Unique” means one distinct factor word, not one occurrence position; the same word may occur more than once.

## Assumptions and scope

Positions in the one-sided word are indexed from \(0\). A sign-sum is the ordinary sum of the entries in a factor, each entry being \(1\) or \(-1\). The claim concerns only lengths \(2^k\) with \(k\ge2\), for the specified four-letter substitution and coding. It does not assert uniqueness at arbitrary lengths or for generalized Rudin–Shapiro sequences.

## Proof

For \(x\in\{a,b,c,d\}\) and \(k\ge0\), set
\[
B_k(x)=\tau(\sigma^k(x)),\qquad L_k=2^k,\qquad
T_k(x)=\sum B_k(x).
\]
For \(0\le j\le L_k\), let \(P_k(x,j)\) be the sum of the first \(j\) signs of \(B_k(x)\). For an ordered pair \(xy\), define
\[
F_k(x,y;j)=T_k(x)-P_k(x,j)+P_k(y,j),
\]
the sign-sum of the suffix of \(B_k(x)\) beginning at offset \(j\), followed by the prefix of \(B_k(y)\) of length \(j\). Define
\[
G_k(x,y)=\max_{0\le j\le L_k}F_k(x,y;j),\qquad
J_k(x,y)=\{j:F_k(x,y;j)=G_k(x,y)\}.
\]

The length-two factors of \(\sigma^\omega(a)\) are exactly
\[
\mathcal P=\{ab,ac,ba,bd,ca,cd,db,dc\}.
\]
Indeed, the internal pairs of substitution images are \(ab,ac,db,dc\), and the boundary pairs are \(ba,bd,ca,cd\); all eight occur already in \(\sigma^4(a)=abacabdbabacdcac\). Every length-\(L_k\) factor lies within one substitution block or crosses one boundary between two length-\(L_k\) blocks. Consequently its sum is \(F_k(x,y;j)\) for some \(xy\in\mathcal P\) and some \(j\in[0,L_k]\), and conversely every such legal pair and offset gives a factor.

If \(\sigma(x)=uv\) and \(\sigma(y)=st\), splitting the two length-\(2L_k\) blocks into their halves gives
\[
T_{k+1}(x)=T_k(u)+T_k(v),
\]
\[
F_{k+1}(x,y;j)=T_k(v)+F_k(u,s;j)\quad(0\le j\le L_k),
\]
\[
F_{k+1}(x,y;L_k+j)=T_k(s)+F_k(v,t;j)\quad(0\le j\le L_k).
\]
Hence
\[
G_{k+1}(x,y)=
\max\!\left\{T_k(v)+G_k(u,s),\ T_k(s)+G_k(v,t)\right\}.
\]
The maximizing-offset sets \(J_{k+1}\) are obtained from the first or second child set exactly when that branch attains this maximum, adding \(L_k\) to offsets from the second branch.

Starting with \(T_0=(1,1,-1,-1)\) and \(G_0(x,y)=\max(\tau(x),\tau(y))\), direct use of this recurrence gives the following matrices, with rows and columns in order \(a,b,c,d\). For even \(k\ge2\), put \(t=2^{k/2}\); then
\[
T_k=(t,t,-t,-t),\qquad
G_k=
\begin{pmatrix}
t&t&t&t\\
3t-2&t&t&t\\
t&t&-t&-t\\
3t-2&t&t-2&-t
\end{pmatrix}.
\]
For odd \(k\ge3\), put \(t=2^{(k+1)/2}\); then
\[
T_k=(t,0,0,-t),\qquad
G_k=
\begin{pmatrix}
t&t&t&t\\
t&0&0&0\\
2t-2&2t-2&0&0\\
t&t-2&0&-t
\end{pmatrix}.
\]
The \(k=2\) and \(k=3\) matrices follow directly from the recurrence. Substituting the even matrix into the recurrence gives the odd matrix with parameter \(2t\); substituting the odd matrix gives the even matrix with the same parameter \(t\). This proves the displayed formulas by induction.

Now restrict to legal pairs in \(\mathcal P\). For even \(k\), the unique largest entry among these pairs is \(G_k(b,a)=3t-2\). For odd \(k\ge3\), the largest legal entry is uniquely \(G_k(c,a)=2t-2\); the other entry \(G_k(c,b)\) has the same value in the full matrix but \(cb\notin\mathcal P\). Thus the maximizing legal block pair is uniquely \(ba\) for even \(k\), and \(ca\) for odd \(k\), and the maximum values are \(M_k\) as stated.

It remains to locate the maximizing offset. The recurrence for \(J_k\), together with the displayed \(G_k\) matrices, gives the following strict-branch relations: for even \(k\ge2\),
\[
J_{k+1}(c,a)=J_{k+1}(c,b)=J_k(d,a),
\]
and for odd \(k\ge3\),
\[
J_{k+1}(b,a)=J_{k+1}(d,a)=2^k+J_k(c,b).
\]
A direct base calculation gives \(J_2(b,a)=J_2(d,a)=\{3\}\). Therefore the relevant maximizing offset is unique, with \(j_2=3\), \(j_{k+1}=j_k\) for even \(k\), and \(j_{k+1}=2^k+j_k\) for odd \(k\). Solving this recurrence yields
\[
j_k=\frac{2\cdot4^{\lfloor k/2\rfloor}+1}{3},
\]
which completes the proof.

## Verification

The accompanying `verification.py` implements the exact \(T,G,J\) recurrences and checks the displayed matrices, the unique legal maximizing pair, and the offset formula for \(2\le k\le20\). This is a finite consistency check only; the all-\(k\) conclusion follows from the induction in the proof, not from finite enumeration.

## Relationship to prior work

The known abelian-complexity literature determines the maximum sign-sum as a function of length and constructs factors attaining it. The result here refines that information at dyadic lengths by proving uniqueness of the distinct maximizing factor word and giving its exact substitution-block boundary offset. Work on general factor properties of automatic words and finite string-attractor data for this sequence studies different invariants and does not imply this uniqueness statement.

## Limitations

The theorem is specific to the stated substitution and coding, and only treats dyadic lengths \(2^k\) with \(k\ge2\). It does not classify all occurrences of the maximizing word, all maximizers at non-dyadic lengths, or analogous extremizers for other automatic sequences. The recurrence script checks finitely many levels; it is not an infinite proof. The full text of one older extremal-property paper was inaccessible in this run, so that source remains a literature risk rather than evidence of coverage.

## References

1. J.-P. Allouche and M. Mendès France, “On an extremal property of the Rudin–Shapiro sequence,” *Mathematika* 32 (1985), 33–38. DOI: 10.1112/S0025579300010822.
2. X. Lü, J. Chen, Z. Wen, and W. Wu, “On the abelian complexity of the Rudin–Shapiro sequence,” arXiv:1606.06935 (first public version 2016-06-22); *Journal of Mathematical Analysis and Applications* 451 (2017), 822–838.
3. L. Schaeffer and J. Shallit, “Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences,” arXiv:1508.02074 (first public version 2015-08-09); *Electronic Journal of Combinatorics* 23(1) (2016), P1.25.
4. X. Lü and P. Han, “A Note on the Abelian Complexity of the Rudin–Shapiro Sequence,” *Mathematics* 10(2) (2022), 221.
