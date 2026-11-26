# First-attainment locations for dyadic extremal Rudin–Shapiro factors

## Finding
Let \(r(n)=(-1)^{e_{11}(n)}\), where \(e_{11}(n)\) counts overlapping occurrences of `11` in the ordinary binary expansion of \(n\ge0\), and let
\[
T_k(i)=\sum_{j=0}^{2^k-1}r(i+j)\qquad (i\ge0).
\]
For every integer \(k\ge2\), define the **first maximizing** and **first minimizing** factor starts
\[
I_k^+=\min\{i\ge0:T_k(i)=\max_{j\ge0}T_k(j)\},\qquad
I_k^-=\min\{i\ge0:T_k(i)=\min_{j\ge0}T_k(j)\}.
\]
Then the exact first-attainment positions are
\[
\boxed{\begin{aligned}
I_k^+&=\begin{cases}(5\cdot2^k+1)/3,&k\text{ even},\\(10\cdot2^k+1)/3,&k\text{ odd},\end{cases}\\
I_k^-&=\begin{cases}(35\cdot2^k+1)/3,&k\text{ even},\\(16\cdot2^k+1)/3,&k\text{ odd}.\end{cases}
\end{aligned}}
\]
The extremal values themselves are the previously studied Rudin–Shapiro Abelian-complexity specializations
\[
\max_{i\ge0} T_k(i)=-\min_{i\ge0}T_k(i)=H_k,
\qquad H_k=\begin{cases}3\cdot2^{k/2}-2,&k\text{ even},\\2^{(k+3)/2}-2,&k\text{ odd}.\end{cases}
\]
The **new assertion** is the first-attainment localization, not the extremal value \(H_k\). Equivalently, \(I_k^++2^k\) and \(I_k^-+2^k\) are the shortest observed prefix lengths in which a length-\(2^k\) factor realizes the respective global maximal or minimal signed sum. These are exact for every \(k\ge2\), not asymptotic estimates.

## Assumptions and scope
The word is one-sided, zero-indexed, and has values \(+1,-1\); windows are contiguous, indexed by starting position, and have exact length \(2^k\). The maxima/minima range over **all** \(i\ge0\). All displayed fractions for first starts are integers because \(2^k\equiv1\pmod3\) for even \(k\), and \(2^k\equiv2\pmod3\) for odd \(k\). The theorem is stated for \(k\ge2\); the length-two boundary case has additional extremizers and is deliberately not included.

## Proof
**1. Two canonical blocks.** Let \(P_k=(r(0),\ldots,r(2^k-1))\), and let \(Q_k\) be obtained from \(P_k\) by negating its second half; at \(k=0\), take \(P_0=Q_0=(1)\). Concatenation of binary digits and the definition of \(e_{11}\) give
\[
P_{k+1}=P_k Q_k,\qquad Q_{k+1}=P_k(-Q_k).
\]
For any \(m\ge0\), the signed block \((r(m2^k+j))_{0\le j<2^k}\) equals \(r(m)P_k\) if \(m\) is even, and \(r(m)Q_k\) if \(m\) is odd. Indeed, concatenating the binary expansion of \(m\) with the \(k\)-digit expansion of \(j\) creates exactly one possible extra `11` across the join, present precisely when \(m\) is odd and the leading digit of the padded \(j\) is one.

**2. Exact prefix extrema and their earliest starts.** Write \(L=2^k\), \(p_k=\sum P_k\), \(q_k=\sum Q_k\), and let \(a_k(t),b_k(t)\) be their prefix sums over \(0\le j<t\), for \(0\le t\le L\). Set \(U_k=\max_t a_k(t)\), \(V_k=\max_t b_k(t)\). Directly from the recursions,
\[
\begin{aligned}
p_{k+1}&=p_k+q_k,&q_{k+1}&=p_k-q_k,\\
U_{k+1}&=\max\{U_k,p_k+V_k\},&V_{k+1}&=\max\{U_k,p_k\}.
\end{aligned}
\]
All prefix sums of both words are nonnegative: at \(k=0\) this is immediate; for the next stage, the second half of \(P_{k+1}\) has prefix sums \(p_k+b_k(t)\), and the second half of \(Q_{k+1}\) has prefix sums \(p_k-b_k(t)\). The latter remain nonnegative because \(V_k\le p_k\), as confirmed inductively by the following closed forms. For each \(h\ge0\), induction yields
\[
\begin{array}{c|cccc}
 &p_k&q_k&U_k&V_k\\\hline
k=2h&2^h&2^h&2^{h+1}-1&2^h\\
k=2h+1&2^{h+1}&0&2^{h+1}&2^{h+1}-1
\end{array}
\]
Let \(u_k\) and \(v_k\) denote the **least** prefix indices attaining \(U_k\) and \(V_k\), respectively. The new maximum of \(P_{k+1}\) is achieved strictly in its second half, while the first maximum of \(Q_{k+1}\) is achieved in its first half (even when a second-half tie exists). Therefore
\[
u_0=v_0=1,\qquad u_{k+1}=2^k+v_k,\qquad v_{k+1}=u_k.
\]
Solving these exact recurrences gives
\[
u_{2h}=(2^{2h+1}+1)/3,\qquad u_{2h+1}=(2^{2h+2}+2)/3.
\]

**3. Exact bounds for all length-\(L\) windows.** A length-\(L\) window beginning at \(mL+t\), with \(0\le t<L\), consists of the suffix after \(t\) symbols of block \(m\) and the prefix of length \(t\) of block \(m+1\). Since consecutive block types alternate between \(P_k\) and \(Q_k\), its absolute sum cannot exceed the larger of
\[
A_k=\max_{0\le t<L}\bigl(\lvert p_k-a_k(t)\rvert+\lvert b_k(t)\rvert\bigr),\qquad
B_k=\max_{0\le t<L}\bigl(\lvert q_k-b_k(t)\rvert+\lvert a_k(t)\rvert\bigr).
\]
These expressions allow **independent signs** on consecutive blocks, hence are valid upper bounds even where particular signs are not attainable.

Write \(c_k(t)=a_k(t)+b_k(t)\) and \(d_k(t)=a_k(t)-b_k(t)\). From the concatenation formula,
\[
(c_k(t),d_k(t))=\begin{cases}(2a_{k-1}(t),0),&0\le t\le L/2,\\(2p_{k-1},2b_{k-1}(t-L/2)),&L/2\le t\le L.
\end{cases}
\]
Consequently \(0\le c_k(t)\le2U_{k-1}\) and \(0\le d_k(t)\le2V_{k-1}\). Also \(0\le a_k(t)\le U_k\) and \(0\le b_k(t)\le V_k\).

If \(k=2h\ge2\), put \(s=2^h\). Then \(p_k=q_k=s\), \(U_k=2s-1\), \(V_k=s\), \(\max c_k=2s\), \(\max d_k=2s-2\). For \(A_k\), when \(a_k(t)\le s\) its summand is \(s-d_k(t)\le s\); otherwise it is \(c_k(t)-s\le s\). Thus \(A_k\le s\). For \(B_k\), since \(b_k(t)\le q_k=s\), the summand is \(s+d_k(t)\), so \(B_k=3s-2\). This exceeds \(s\). It can be positive only for consecutive signed blocks \((+Q_k,+P_k)\) with \(d_k(t)=2s-2\), and negative only for \((-Q_k,-P_k)\) at the same earliest offset.

If \(k=2h+1\ge3\), put \(s=2^{h+1}\). Then \(p_k=s\), \(q_k=0\), \(U_k=s\), \(\max c_k=2s-2\), and \(\max d_k=s\). Here \(A_k\le s\) because \(a_k(t)\le s\), so its summand equals \(s-d_k(t)\). But \(B_k=\max c_k=2s-2>s\), with the positive extreme attainable only for \((-Q_k,+P_k)\), and the negative extreme only for \((+Q_k,-P_k)\), at offsets maximizing \(c_k\). This proves the stated global extremal sums once the indicated block signs are exhibited.

**4. First block pairs and first offsets.** Every odd-numbered length-\(L\) block is \(r(m)Q_k\), followed by \(r(m+1)P_k\). The successive pairs \((r(m),r(m+1))\) for odd \(m=1,3,5,7,9,11\) are respectively
\[
(+,+),\quad(-,+),\quad(+,-),\quad(+,+),\quad(+,+),\quad(-,-).
\]
Therefore the first eligible block-pair indices are \(m=1\) for positive and \(m=11\) for negative extremes at even \(k\), and \(m=3\) for positive and \(m=5\) for negative extremes at odd \(k\ge3\). Even-numbered block pairs cannot attain these extremes because their absolute sums are at most \(A_k<H_k\). All earlier odd pairs have the wrong signs, and the inequalities above show they cannot tie the extreme.

For even \(k\ge2\), the first offset maximizing \(d_k\) lies in the second half, and equals
\[
t_k^{\mathrm{even}}=L/2+v_{k-1}=L/2+u_{k-2}=(2L+1)/3.
\]
For odd \(k\ge3\), the first offset maximizing \(c_k\) lies in the first half, because \(U_{k-1}>p_{k-1}\), and equals
\[
t_k^{\mathrm{odd}}=u_{k-1}=(L+1)/3.
\]
Substituting these offsets into the four first eligible starts \(mL+t\) proves all the displayed formulas for \(I_k^+\) and \(I_k^-\). No smaller start can achieve the corresponding extremum, which completes the proof.

## Verification
The included `verify.py` independently builds the Rudin–Shapiro sequence directly by counting adjacent `11` bits and checks all length-\(2^k\) window sums up to and including the first minimizing location, for \(2\le k\le16\). It also reconstructs the two canonical blocks and verifies their full prefix extrema and least maximizing prefix indices through \(k=16\), all using exact integers. Run `python3 verify.py`; the printed PASS indicates that all finite assertions checked by the program agree with the theorem. These finite tests support, but do not replace, the four-step infinite proof above.

## Relationship to prior work
Lü, Chen, Wen and Wu (2016/2017) determined the Rudin–Shapiro Abelian-complexity function, its recurrence and the symmetry between extreme factor sums. Lü and Han (2022) studied its growth order and distribution of complexity values. Hence the displayed formula for \(H_k\) is **not claimed as a new result**; the new datum is the **smallest factor starting position** attaining each extreme at all dyadic lengths. The earlier complexity function depends only on the attainable Parikh vectors and does not determine which prefix first contains an extremal vector. In particular, the distinction between first positive and negative witnesses requires analyzing the actual neighboring signed blocks and first prefix-maximizing offsets, not merely the numerical maximum. An unindexed first-occurrence result is a residual bibliographic possibility.

## Limitations
The theorem treats the classical signed Rudin–Shapiro sequence and dyadic factor lengths only. It does not classify every maximizing occurrence, non-dyadic lengths or factor frequencies. The first-location result is a direct, self-contained mathematical proof with finite checks, not an independent audit. Results on extremal **values** predate the present localization calculation. A potentially equivalent location formula hidden in unindexed literature has not been excluded.

## References
1. X. Lü, J. Chen, Z. Wen and W. Wu, *On the abelian complexity of the Rudin-Shapiro sequence*, arXiv:1606.06935 (first public 2016-06-22); Journal of Mathematical Analysis and Applications 451 (2017), 822–838. https://arxiv.org/abs/1606.06935
2. X. Lü and P. Han, *A Note on the Abelian Complexity of the Rudin-Shapiro Sequence*, Mathematics 10(2), 221 (first public 2022-01-12). https://doi.org/10.3390/math10020221
