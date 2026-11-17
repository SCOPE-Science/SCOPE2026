# A paired-truncation rank law and uniform limiting spectrum for characteristic-two square-zero derivations

## Finding
Let \(q=2^e\) with \(e\ge1\), let \(A_N=\mathbb F_q[x]/(x^N)\), and write \(W_N=\operatorname{Der}_{\mathbb F_q}(A_N)\). For an integer \(m\ge1\), define \(S_{N,r}(q)=\#\{D\in W_N:D^2=0,\ \operatorname{rank}_{\mathbb F_q}(D)=r\}\). The **rank enumerators coincide at successive even and odd truncation lengths**:
\[
\sum_{r\ge0}S_{2m,r}(q)z^r=\sum_{r\ge0}S_{2m+1,r}(q)z^r=P_{m,q}(z),
\]
where
\[
\begin{aligned}
P_{m,q}(z)={}&1+(q-1)\sum_{r=1}^{m}q^{r-1}z^r\\
&+\sum_{b=1}^{\lfloor m/2\rfloor}(q-1)q^{b-1}
\left[q^{b-1}z^b+(q-1)\sum_{r=b}^{m-b}q^{r-1}z^r\right].
\end{aligned}
\]
Thus the number of square-zero derivations at either length is exactly
\[
P_{m,q}(1)=q^m+\lfloor m/2\rfloor(q-1)q^{m-1}.
\]
For fixed \(q\), if \(D_m\) is uniform on the square-zero derivations of \(A_{2m}\) **or** \(A_{2m+1}\), then
\[
\frac{\operatorname{rank}(D_m)}{m}\ \Longrightarrow\ \operatorname{Uniform}[1/2,1]
\qquad(m\to\infty).
\]
In particular, the limiting law is independent of the even field order \(q\). Among square-zero derivations on \(A_{2m}\), exactly \((q-1)q^{m-1}\) have zero homology \(\ker D/\operatorname{im}D\). At length \(2m+1\), exactly the same number have one-dimensional homology (the minimum possible dimension).

## Assumptions and scope
All derivations are \(\mathbb F_q\)-linear, and \(D^2=0\) means zero *composite linear operator* on the full truncated algebra, not merely preservation of square-zero algebra elements. The characteristic is exactly two; the field may be any finite extension of \(\mathbb F_2\). The algebra is unital and consists of residue classes modulo \(x^N\). The rank counts are for actual operators, not classes under algebra automorphisms. The limit holds with \(q\) fixed and \(m\) tending to infinity.

## Proof
Every derivation of \(\mathbb F_q[x]/(x^N)\) is uniquely \(D_f=f(x)\partial_x\), where \(f(x)\) is an arbitrary class modulo \(x^N\) if \(N\) is even, and is divisible by \(x\) if \(N\) is odd. Indeed, differentiating the relation gives \(N x^{N-1}f(x)=0\). In characteristic two, the composite \(D_f^2\) is again a derivation, so it vanishes exactly when \(D_f^2(x)=f f'=0\) in \(A_N\).

Set \(t=x^2\), and put \(R_m=\mathbb F_q[t]/(t^m)\). Every coefficient at even length has the unique form \(f=E(t)+xO(t)\) with \(E,O\in R_m\). Every admissible coefficient at odd length has the form \(\widetilde f=tE(t)+xO(t)\) with the **same** parameter pair \((E,O)\in R_m^2\). The derivative of either coefficient is \(O(t)\). Separating its product with the coefficient into even and odd powers gives, at both lengths, precisely
\[
E(t)O(t)=0\pmod{t^m},\qquad O(t)^2=0\pmod{t^m}.
\]
Consequently \((E,O)\mapsto(tE,O)\) induces a coefficient-wise bijection between square-zero derivations on the two truncations. It also preserves rank: both derivations kill all even powers of \(x\), and send the odd-power basis \(x,x^3,\ldots,x^{2m-1}\) to \(x^{2k}f\) or \(x^{2k}\widetilde f\). Under the decomposition into even and odd powers, the latter column is obtained from the former by shifting the even component up by one \(t\)-power and leaving the odd component unchanged. This shift is injective on the even component, hence preserves all linear dependencies among the columns.

We count these pairs with rank. If \(O=0\), the zero \(E\) has rank zero. A nonzero \(E\) of \(t\)-adic order \(a\in\{0,\ldots,m-1\}\) has rank \(m-a\) and there are \((q-1)q^{m-a-1}\) such elements. This produces the first line of \(P_{m,q}\).

If \(O\ne0\), write \(j=\operatorname{ord}_t(O)\). Since \(R_m\) is a chain ring, \(O^2=0\) is equivalent to \(j\ge\lceil m/2\rceil\). Put \(b=m-j\), so \(1\le b\le\lfloor m/2\rfloor\). There are \((q-1)q^{b-1}\) admissible \(O\)'s of this order, and the equation \(EO=0\) is equivalent to \(E\in t^bR_m\), giving \(q^{m-b}\) possibilities. If \(a=\operatorname{ord}_t(E)\le j\), the rank is \(m-a\); if \(a>j\), including \(E=0\), the rank is \(m-j=b\). For each \(r\in\{b,\ldots,m-b\}\), there are \((q-1)q^{r-1}\) elements \(E\) with \(a=m-r\); a further \(q^{b-1}\) elements with \(a>j\) also have rank \(b\). Multiplying by the \(O\)-count and summing over \(b\) proves the displayed rank polynomial. Each \(b\)-stratum has total size \((q-1)q^{m-1}\), proving the total count.

For the limit, set \(h=\lfloor m/2\rfloor\). The probability of \(O=0\) among square-zero derivations is \(q/[q+h(q-1)]\), tending to zero. Conditional on \(O\ne0\), the stratum index \(B\) is **uniform** on \(\{1,\ldots,h\}\). Conditional on \(B=b\), choose \(E\) uniformly in \(t^bR_m\) and define
\[
T=\min\{\operatorname{ord}_t(E)-b,\ m-2b\},
\]
with \(\operatorname{ord}_t(0)=+\infty\). The rank formula above is \(\operatorname{rank}(D)=m-b-T\), and \(\Pr(T\ge k\mid B=b)=q^{-k}\) for integers \(1\le k\le m-2b\). Therefore \(\mathbb E(T\mid B=b)\le1/(q-1)\) uniformly. Since \(B/m\) converges to the uniform law on \([0,1/2]\), and \(T/m\) converges in probability to zero, the normalized rank converges to \(\operatorname{Uniform}[1/2,1]\). The exceptional \(O=0\) proportion vanishes and does not affect the limit.

For any square-zero linear map on an \(N\)-dimensional space, \(\dim\ker D/\operatorname{im}D=N-2\operatorname{rank}D\). Hence homology is zero at even length, or minimal of dimension one at odd length, exactly when the rank is \(m\). This rank occurs only when \(O=0\) and \(E\) is a unit in \(R_m\), giving \((q-1)q^{m-1}\) such operators.

## Verification
The accompanying `verify.py` constructs every admissible coefficient over \(\mathbb F_2\) and \(\mathbb F_4\) in explicitly bounded small truncations, computes the derived linear maps by polynomial multiplication, independently tests \(D^2=0\), and obtains ranks by finite-field row reduction. It compares each complete rank histogram with the closed formula. Tested lengths are \(N=2,3,4,5,6,7,8,9\) over \(\mathbb F_2\) and \(N=2,3,4,5,6\) over \(\mathbb F_4\). The verifier ends with `VERIFY_OK` when all checks succeed. Finite checks are auxiliary; the proof above establishes the complete infinite family and the weak limit.

## Relationship to prior work
Modular Witt Lie algebras are the restricted Lie algebras of derivations of truncated polynomial rings; their restriction operation is operator composition. Evans–Fuchs (2001) give the restriction map for the special truncation \(\mathbb F[x]/(x^p)\); in characteristic two that is only length two, whereas the present statement concerns arbitrarily long truncations and a rank spectrum. Yao–Zhao (2020) treat **2-local maps on Jacobson–Witt Lie algebras**, including a characteristic-two non-simple example, rather than elements \(D\) satisfying \(D^{[2]}=0\). Chen (2019) studies nilpotent varieties, but the Zassenhaus analysis assumes characteristic greater than three; Chang–Yao (2021) study tensor-product representations for characteristic greater than three. None of these inspected results gives the rank-preserving paired-truncation correspondence or its uniform limiting spectrum. These comparisons do not establish global publication priority.

## Limitations
Only one-variable truncated polynomial algebras over finite fields of characteristic two are covered. The bijection between successive lengths is a rank-preserving bijection of operators, not asserted to preserve composition, brackets, conjugacy, or algebra automorphisms. The limiting law requires fixed \(q\); no joint limit with growing field size is claimed. A broader yet unidentified restricted-Lie nilpotent-cone or differential-classification theorem could subsume the result. No external or independent mathematical audit is asserted.

## References
- Y. Yao and K. Zhao, *2-local derivations on the Jacobson–Witt algebras in prime characteristic*, arXiv:2007.07746 (first posted 2020-07-15), especially Theorem 3.19 and Example 3.20.
- C. Chen, *Nilpotent varieties of some finite dimensional restricted Lie algebras*, arXiv:1910.00954 (2019), abstract and Chapter 4 (characteristic restrictions).
- H. Chang and Y.-F. Yao, *Tensor products of the defining representations over the Witt algebra in positive characteristic*, arXiv:2108.06657 (2021), introduction, Section 2 and Corollary 4.8.
- T. J. Evans and D. Fuchs, *On the restricted Lie algebra structure for the Witt Lie algebra in finite characteristic*, arXiv:math/0111271 (2001), Theorem 1.
