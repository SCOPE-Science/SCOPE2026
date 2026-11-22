# Uniform Lucas classification of higher integral cube-square ratios for odd progressions

## Finding
For integers \(n\ge2\) and positive odd \(a\), let
\[
S(n,a)=\sum_{i=0}^{n-1}(a+2i),\qquad C(n,a)=\sum_{i=0}^{n-1}(a+2i)^3.
\]
For any *fixed odd integer* \(k\ge5\), define the integral Lucas sequence
\[
U_0(k)=0,\quad U_1(k)=1,\quad U_{j+1}(k)=kU_j(k)-U_{j-1}(k)\quad(j\ge1).
\]
Then the complete set of pairs satisfying \(C(n,a)=kS(n,a)^2\) is
\[
\boxed{n=U_{3t+1}(k),\qquad a=(k-1)U_{3t+1}(k)-U_{3t}(k)+1,\quad t\ge1.}
\]
Every pair displayed is positive, has \(a\) odd, and gives the claimed multiplier. The least possible length and its unique starting term are
\[
\boxed{n_{\min}(k)=k^3-2k,\qquad a_{\min}(k)=k^4-k^3-3k^2+2k+2.}
\]
In particular the least length across all multipliers \(k\ge5\) is \(115\), at \((k,n,a)=(5,115,437)\). For each fixed \(k\ge5\), the count of distinct admissible lengths at most \(X\) is
\[
\frac{\log X}{3\log\!\left((k+\sqrt{k^2-4})/2\right)}+O_k(1).
\]
There are no integral even multipliers for a positive odd-term progression of length at least two. The multiplier \(3\) is a previously accessible boundary case; the novelty claim concerns the uniform classification for all odd \(k\ge5\).

## Assumptions and scope
All parameters \(n,a,k,t\) above are ordinary integers. The progression has *step exactly two*, *odd positive first term*, and length \(n\ge2\). The numerator is the sum of cubes, whereas the denominator is the *square of the sum of terms*, not an arbitrary perfect square. No statement is made about other common differences, zero or negative terms, or additional odd powers.

## Proof
**1. Ratio reduction.** Put \(x=a+n-1\). Then \(S=nx\). Expanding cubes (equivalently applying the general arithmetic-progression cubic identity) yields
\[
C=S\bigl(a(a+2n-2)+2n(n-1)\bigr)
 =nx\bigl(x^2+n^2-1\bigr).
\]
Hence
\[
\frac{C}{S^2}=\frac{x^2+n^2-1}{nx},\qquad x=a+n-1\ge n.
\]
If this quotient is an integer, then \(x\mid n^2-1\). When \(n\) is even, \(x\) is even, contradicting that \(n^2-1\) is odd. Thus \(n\) is odd. Then \(x\) is odd, the numerator and denominator of the quotient are odd, and the integer quotient \(k\) is odd. This also rules out every even multiplier.

**2. Norm-four equation and the positive branch.** Fix any odd \(k\ge5\), write \(D=k^2-4>0\). The condition \(C=kS^2\) is
\[
 x^2-knx+n^2-1=0
 \quad\Longleftrightarrow\quad u^2-Dn^2=4,\quad u=2x-kn.
\]
The discriminant has the two roots \(x=(kn\pm\sqrt{Dn^2+4})/2\). Since \(\sqrt{Dn^2+4}>(k-2)n\), the negative root is strictly below \(n\), contradicting \(x\ge n\). Thus \(u>0\) and only the plus root is admissible.

**3. Exhaustive positive Pell descent.** If \(u,n>0\) satisfy \(u^2-Dn^2=4\), then \(u\equiv kn\pmod2\), as follows by reduction modulo four. Define
\[
 u'=\frac{ku-Dn}{2},\qquad n'=\frac{kn-u}{2}.
\]
These are integers, satisfy \(u'^2-Dn'^2=4\), and have \(u'>0\). For \(n\ge2\), the inequalities
\[
 (k-2)n<u<kn
\]
follow respectively from \(D>(k-2)^2\) and \(4<4n^2\). Therefore \(0<n'<n\). Repeated descent ends at \(n=1\), for which \(u=k\). Reversing the descent proves that *every* positive solution is generated from \((u_1,n_1)=(k,1)\) by
\[
 n_{j+1}=\frac{u_j+kn_j}{2},\qquad u_{j+1}=\frac{ku_j+Dn_j}{2}.
\]
Its \(n_j\) satisfy \(n_0=0,n_1=1,n_{j+1}=kn_j-n_{j-1}\), hence \(n_j=U_j(k)\); similarly \(u_j=kU_j(k)-2U_{j-1}(k)\). From the plus root,
\[
 a=x-n+1=\frac{(k-2)n_j+u_j}{2}+1
 =(k-1)U_j(k)-U_{j-1}(k)+1.
\]
Conversely each such pair satisfies the norm equation and the original cubic-sum identity. The expression for \(a\) is positive because \(U_j>U_{j-1}\ge0\) for \(k\ge5\) and \(j\ge1\).

**4. Exact parity filter.** Since \(k\) is odd, \(k-1\) is even, so the displayed \(a\) is odd exactly when \(U_{j-1}(k)\) is even. Modulo two, the Lucas recurrence becomes \(U_{j+1}\equiv U_j+U_{j-1}\pmod2\). Starting with \((U_0,U_1)\equiv(0,1)\), its parity sequence is \(0,1,1,0,1,1,\ldots\), and \(U_r\) is even iff \(3\mid r\). Thus \(j\equiv1\pmod3\). The case \(j=1\) yields \(n=1\) and is excluded; hence exactly \(j=3t+1\) for \(t\ge1\).

**5. Least length, uniqueness, and sparsity.** For \(k\ge5\), the positive sequence \(U_j(k)\) is strictly increasing. The least allowed index is \(j=4\), where \(U_3(k)=k^2-1\) and \(U_4(k)=k^3-2k\). Substitution gives the stated \(a_{\min}(k)\). This length is strictly increasing in \(k\ge5\), so the overall first occurrence is \((k,n,a)=(5,115,437)\). The characteristic roots of the recurrence are \(\alpha=(k+\sqrt{k^2-4})/2>1\) and \(\alpha^{-1}\), and
\[
 U_j(k)=\frac{\alpha^j-\alpha^{-j}}{\sqrt{k^2-4}}.
\]
Taking \(j=3t+1\) gives the displayed logarithmic counting asymptotic and zero natural density among lengths.

## Verification
A standalone Python 3 script, `verify.py`, checks 3,440 literal cube-sum comparisons against the polynomial reduction; exhausts 149,000 bounded odd-progression pairs \(2\le n<300\), \(1\le a<1000\), and compares every qualifying multiplier at least five with the recurrence; checks 28 independently generated larger Lucas pairs, including direct sums for the least-length cases; and independently tests the even-length parity obstruction. The script uses integer arithmetic only. Its finite tests are *not* used to prove exhaustion for unbounded \(n,a,k\); the descent above supplies that proof.

## Relationship to prior work
Aassila's 2026 paper provides the general cubic arithmetic-progression identity and proves divisibility results for odd-power sums. Its abstract also identifies the exact Nicomachus equality \(C=S^2\), not the higher-multiplier classification here. The full paper could not be materially inspected, so possible implicit coverage remains a priority risk.

Kim and Stolarsky (2024), Sections 2 and 7, establish Pell families arising from repeated consecutive blocks and an extended sequence that includes a *step-two* progression. In particular, their Proposition 9 identifies a Fibonacci case with discriminant \(5n^2+4\), which covers a related multiplier-three boundary through a variable shift. The present claim *excludes multiplier three* and concerns the entire odd family \(k\ge5\), whose norm-four equations have varying coefficients \(k^2-4\), a universal three-step parity selection, and sharp first-length formulas. The paper's inspected equations do not imply these all-\(k\) assertions as stated. Barbeau and Seraj (2013) investigate \(C=S^2\) for general integer collections, not multiplier \(k\ge5\) for odd arithmetic progressions.

## Limitations
This is an elementary classification, not an independence certificate or a claim of a paper-sized contribution. It does not address higher odd powers, steps other than two, or sums over sequences with repeated terms. The source novelty comparison is best-knowledge rather than exhaustive; the full Aassila article and Aguilar's 2026 thesis were not accessible for full-text comparison. An independent audit has not been performed.

## References
- M. Aassila, *When does the sum of an arithmetic progression divide its odd power sums?*, Annals of Communications in Mathematics **9** (2026), article 6; public November 18, 2026. https://www.technoskypub.com/journals/when-does-the-sum-of-an-arithmetic-progression-divide-its-odd-power-sums/ ; DOI: https://doi.org/10.62072/acm.2026.09053 .
- S.-H. Kim and K. B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences **27** (2024), Article 24.6.3, especially Sections 2 and 7. https://cs.uwaterloo.ca/journals/JIS/VOL27/Kim/kim8.pdf .
- E. J. Barbeau and S. Seraj, *Sum of Cubes is Square of Sum*, arXiv:1306.5257 (2013). https://arxiv.org/pdf/1306.5257 .
- J. M. Aguilar, *When a Sum of Cubes Equals the Square of the Sum*, M.A. thesis (2026), abstract. https://scholarworks.lib.csusb.edu/etd/2396/ .
