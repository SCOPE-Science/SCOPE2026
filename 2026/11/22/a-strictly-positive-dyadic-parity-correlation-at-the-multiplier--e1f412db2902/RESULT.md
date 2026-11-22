# A strictly positive dyadic parity correlation at the multiplier \(7\)

## Finding

Let \(s_2(n)\) be the number of ones in the binary expansion of an integer \(n\geq0\), with \(s_2(0)=0\), and set \(\varepsilon(n)=(-1)^{s_2(n)}\). For every integer \(L\geq0\), define the signed multiplicative correlation
\[
C_L=\sum_{n=0}^{2^L-1}\varepsilon(n)\varepsilon(7n).
\]
Then
\[
C_0=1,\qquad C_1=C_2=C_3=2,\qquad
C_{L+4}=C_{L+1}+2C_L\quad(L\geq0).
\]
Consequently,
\[
\sum_{L\geq0}C_Lz^L
=\frac{1+2z+2z^2+z^3}{1-z^3-2z^4}
=\frac{1+z+z^2}{1-z+z^2-2z^3},
\]
and **\(C_L>0\) at every dyadic length**. In particular, the reduced denominator gives the shortest constant-coefficient linear recurrence over the rationals,
\[
C_{L+3}=C_{L+2}-C_{L+1}+2C_L\qquad(L\geq0).
\] Equivalently, among \(0\leq n<2^L\), the number for which \(s_2(n)\) and \(s_2(7n)\) have the same parity exceeds the number for which they have opposite parity by exactly \(C_L\).

## Assumptions and scope

The multiplier is precisely the fixed integer \(7\), the lower endpoint is \(0\), and the interval is the complete dyadic range \(0\leq n<2^L\). All statements are valid for every integer \(L\geq0\). This is a finite-block statement; it does not assert a nonzero limiting normalized correlation. Indeed, the recurrence shows that the unnormalized positive excess grows sublinearly in the block length.

## Proof

Read the binary digits \(b\in\{0,1\}\) of \(n\), starting with its least significant digit, while multiplying by \(7\). If the incoming carry is \(c\), the outgoing product digit is \(y=(7b+c)\bmod2\), and the next carry is \(c'=\lfloor(7b+c)/2\rfloor\). All carries belong to \(\{0,1,2,3,4,5,6\}\). As \(7\) is odd, \(b+y\equiv c\pmod2\), so the sign contributed by this digit transition is \((-1)^c\), independently of \(b\).

Index rows and columns by \(0,\ldots,6\). Let \(M_{c,c'}\) sum these signs over the two possible inputs \(b\). Its explicit value is
\[
M=\begin{pmatrix}
1&0&0&1&0&0&0\\
-1&0&0&0&-1&0&0\\
0&1&0&0&1&0&0\\
0&-1&0&0&0&-1&0\\
0&0&1&0&0&1&0\\
0&0&-1&0&0&0&-1\\
0&0&0&1&0&0&1
\end{pmatrix}.
\]
After the first \(L\) product bits, the remaining higher part is exactly the final carry \(c\). Its sign is \((-1)^{s_2(c)}\); hence the terminal column and initial row are
\[
v=(1,-1,-1,1,-1,1,1)^{\mathsf T},\qquad e_0=(1,0,0,0,0,0,0),
\]
and, for all \(L\geq0\),
\[
C_L=e_0M^Lv.\tag{1}
\]
The finitely checkable identity
\[
(M^4-M-2I)v=(0,0,4,0,-4,0,0)^{\mathsf T}\tag{2}
\]
reduces the general recurrence to one coordinate invariant. Write \(w_L=e_0M^L\), with components \(w_{L,j}\). For an arbitrary row \(w\), its product \(w'=wM\) has components
\[
(w_0-w_1,\ w_2-w_3,\ w_4-w_5,\ w_0+w_6,\ -w_1+w_2,\ -w_3+w_4,\ -w_5+w_6).
\]
Thus the two relations \(w_1=w_5\) and \(w_2=w_4\) are preserved by multiplication with \(M\). They hold for \(e_0\), so both hold for every \(w_L\). Multiplying (2) from the left by \(w_L\), and applying (1), gives
\[
C_{L+4}-C_{L+1}-2C_L=4(w_{L,2}-w_{L,4})=0.
\]
Directly from (1), \(C_0,C_1,C_2,C_3\) are \(1,2,2,2\). The generating function follows by multiplying the recurrence by powers of \(z\) and summing. All four initial values are positive and each subsequent term is a sum of positive earlier terms, proving strict positivity for every \(L\). The numerator \(1+z+z^2\) and reduced denominator \(1-z+z^2-2z^3\) are coprime, so the displayed third-order recurrence is of minimal possible rational constant-coefficient order. Every root \(\lambda\) of the fourth-order characteristic equation \(\lambda^4=\lambda+2\) has \(\lvert\lambda\rvert<2\) (otherwise \(\lvert\lambda\rvert^4\leq\lvert\lambda\rvert+2\) is impossible), proving the stated sublinear growth relative to \(2^L\).

## Verification

The standalone file `verify_correlation.py` builds \(M\) from the binary carry rule rather than taking it on trust, checks the vector identity (2), verifies the coordinate invariants through 40 transfers and the recurrence through the resulting first 41 terms, and independently enumerates all \(n<2^L\) for \(0\leq L\leq15\). The first fourteen values are
\[
1,2,2,2,4,6,6,8,14,18,20,30,46,56.
\]
Run `python3 verify_correlation.py`. The infinite proof depends on the explicitly displayed seven-state transition rule, exact vector identity (2) and preserved coordinate invariant, **not** on the finite enumeration.

## Relationship to prior work

Spiegelhofer's 2023 paper [1] treats the binary sum-of-digits parity along cubes and uses correlation estimates as part of an analytic approach; its Theorem 2.1 and Section 4.3 do not assert an exact finite-block formula for the simultaneous parity of \(n\) and \(7n\). The more general study of multiplicative properties of Thue–Morse in Mauduit's 2002 survey [2] is contextually relevant, but the complete paper was not accessible for a definitive comparison. Nearby published computations [3,4] concern the multiplier \(3\) and the family \(2^k+1\), respectively: neither result applies to the multiplier \(7\) as stated. The present seven-carry cancellation and strictly positive exact recurrence require a different parameter comparison, not a substitution in those claims.

## Limitations

No claim is made for arbitrary odd multipliers, for shifted intervals or for a nonzero limiting normalized correlation. Standard finite-automaton transfer methods imply that correlations of this type have rational generating functions, so the contribution is the **specific low-order recurrence and persistent sign at multiplier \(7\)**, not rationality alone. The possibility of an older equivalent formula in unexamined literature, including [2], remains a residual originality risk. 

## References

[1] L. Spiegelhofer, *Thue–Morse along the sequence of cubes*, arXiv:2308.09498v1, first posted August 18, 2023. https://arxiv.org/abs/2308.09498

[2] C. Mauduit, *Multiplicative properties of the Thue–Morse sequence*, Periodica Mathematica Hungarica 43 (2002), 137–153, DOI:10.1023/A:1015241900975. https://doi.org/10.1023/A:1015241900975

[3] *Exact oscillatory parity correlations at binary triples*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-oscillatory-parity-correlations-at-binary-triples--4ded471daa94

[4] *Exact dyadic multiplicative correlations for two-one binary multipliers*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-dyadic-multiplicative-correlations-for-two-one-binary-mult--50b8d332f4b5
