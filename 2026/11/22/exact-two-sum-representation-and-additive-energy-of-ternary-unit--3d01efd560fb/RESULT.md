# Exact two-sum representation and additive energy of ternary-unit Catalan indices

## Finding
Let \(C_n=(n+1)^{-1}\binom{2n}{n}\) be the classical Catalan numbers and, for each integer \(r\ge1\), let
\[
A_r=\{n\in\{0,\ldots,3^r-1\}:3\nmid C_n\}.
\]
For \(m=r-1\), define \(w_m(u)=2^{N_1(u)}\), where \(N_1(u)\) counts digits equal to one in the length-\(m\) ternary expansion of \(u\in\mathbb Z/3^m\mathbb Z\). In the expressions below, \(u+1\) is reduced modulo \(3^m\) (including when \(m=0\)). The number of **ordered** two-summand representations of \(t\) modulo \(3^r\) is
\[
R_r(t)=\#\{(a,b)\in A_r^2:a+b\equiv t\pmod{3^r}\}.
\]
For every \(0\le u<3^m\), the complete representation function is
\[
\begin{aligned}
R_r(3u)&=3w_m(u),\\
R_r(3u+1)&=2w_m(u)+w_m(u+1),\\
R_r(3u+2)&=w_m(u)+2w_m(u+1).
\end{aligned}
\]
The following consequences hold at **every** depth \(r\ge1\):

- \(|A_r|=3\cdot2^{r-1}\); every target residue is represented.
- The least representation count is \(3\), attained at exactly \(2^{r-1}+2\) target residues.
- The largest representation count is \(3\cdot2^{r-1}\). For \(r\ge2\), its unique maximizing target is \(t=3(3^{r-1}-1)/2\); for \(r=1\), all three targets have value \(3\).
- The ordered modular additive energy satisfies the exact identity
\[
E_r=\#\{(a,b,c,d)\in A_r^4:a+b\equiv c+d\pmod{3^r}\}
=\frac{127\cdot6^{r-1}+8}{5}.
\]

There is also a complete probabilistic interpretation. The compatible uniform laws on \(A_r\) define a probability measure \(\mu\) on \(\mathbb Z_3\). Its self-convolution \(\nu=\mu*\mu\) is non-atomic, has **all of** \(\mathbb Z_3\) as its topological support, but is singular with respect to normalized Haar measure. With the standard cylinder-based correlation-dimension convention,
\[
D_2(\nu)=\lim_{r\to\infty}
\frac{-\log\sum_{t\bmod3^r}\nu(t+3^r\mathbb Z_3)^2}{r\log3}
=\log_3(8/3)<1.
\]

## Assumptions and scope
All congruences are in the finite ring \(\mathbb Z/3^r\mathbb Z\); all digits are ordinary base-three digits; summands are ordered, and zero is an allowed index. These statements concern **indices at which the Catalan number is a unit modulo three**, not residues of Catalan values themselves. No assertion of natural density for those indices or of absolute continuity of their convolution is made.

The starting digit characterization is the established theorem of Deutsch and Sagan: \(3\nmid C_n\) precisely when all ternary digits of \(n+1\), except the lowest digit, are zero or one. Their result is used as an input, not presented as new.

## Proof
**1. The index digit set.** Write \(m=r-1\), and define
\[
K_m=\left\{\sum_{j=0}^{m-1}\epsilon_j3^j:\epsilon_j\in\{0,1\}\right\}\subset\mathbb Z/3^m\mathbb Z.
\]
The Deutsch–Sagan condition on \(n+1\) gives an equality of residue sets
\[
A_r=3K_m+\{-1,0,1\}\pmod{3^r}.
\]
The three displayed translates have disjoint residue classes modulo three, so each index has exactly one such description and \(|A_r|=3\cdot2^m\). In particular, \(K_0=\{0\}\) and all formulas also cover \(r=1\).

**2. The full representation function.** A pair of elements of \(K_m\) adds digitwise without carries: its sum at digit \(j\) is zero, one, or two, with respectively one, two, or one choices of the ordered digit pair. Hence the number of ordered pairs summing to \(u\pmod{3^m}\) is \(w_m(u)=2^{N_1(u)}\). The ordered convolution of the uniform three-element offset set \(\{-1,0,1\}\), before normalization, has coefficients \((1,2,3,2,1)\) at offsets \((-2,-1,0,1,2)\). For a target \(3u\), only offset zero applies, with coefficient three. For \(3u+1\), offsets one and minus two apply, with coefficients two and one; minus two shifts the upper index to \(u+1\). For \(3u+2\), offsets two and minus one apply, with coefficients one and two. This proves all three formulas, including wraparound modulo \(3^m\).

**3. Exact extrema.** Each weight lies between one and \(2^m\), with the maximum weight attained only at \(u=(3^m-1)/2\), whose length-\(m\) digits are all one. Thus \(R_r(3u)\le3\cdot2^m\), with the stated unique maximizing target for \(m\ge1\). Since \(u\) and \(u+1\) cannot both have all digits one when \(m\ge1\), each of \(R_r(3u+1)\) and \(R_r(3u+2)\) is strictly less than \(3\cdot2^m\). The minimum of each displayed formula is at least three. The values \(R_r(3u)=3\) occur exactly when the digits of \(u\) lie in \(\{0,2\}\), giving \(2^m\) choices. The other two classes each attain three exactly when \(w_m(u)=w_m(u+1)=1\). For \(m\ge1\) this forces \(u=3^m-1\): a ternary word with no ones whose successor also has no ones must consist entirely of twos. For \(m=0\), the unique empty word gives the same one-per-class count. Therefore exactly \(2^m+2\) targets attain the minimum. Positivity proves full two-sum coverage.

**4. Closed additive energy.** Let \(H_m=\sum_uw_m(u)^2\), and \(P_m=\sum_uw_m(u)w_m(u+1)\), summing over \(\mathbb Z/3^m\mathbb Z\). Independent digit choices yield \(H_m=(1+4+1)^m=6^m\). Splitting \(u\) according to its lowest ternary digit shows
\[
P_0=1,\qquad P_m=4\cdot6^{m-1}+P_{m-1}\quad(m\ge1).
\]
Indeed, low digits zero and one each contribute \(2H_{m-1}\) in the successor product, while low digit two contributes \(P_{m-1}\) from the carry into the higher digits. Consequently \(P_m=(4\cdot6^m+1)/5\). Squaring the three representation formulas and summing over \(u\) gives
\[
E_r=19H_m+8P_m
=19\cdot6^m+\frac{8(4\cdot6^m+1)}5
=\frac{127\cdot6^m+8}{5}.
\]
All steps are exact integer identities, so the energy formula holds at all depths without extrapolation.

**5. Support, singularity, and correlation dimension.** Every admissible prefix lifts to precisely two admissible prefixes one digit longer, making the uniform measures compatible. Let \(X\in\mathbb Z_3\) have independent uniform digits in \(\{0,1\}\), and let \(S\) be independent and uniform on \(\{-1,0,1\}\). The resulting measure is the law of \(S+3X\); hence \(\nu\) is the law of \(S_1+S_2+3(X_1+X_2)\) for independent copies. The digits of \(X_1+X_2\) are independent (there are no carries) and have probabilities \((1/4,1/2,1/4)\) for digits zero, one and two. Almost surely their digit-one frequency is \(1/2\), whereas Haar-almost every ternary integer has digit-one frequency \(1/3\). Thus the law of \(X_1+X_2\) is Haar-singular, and its finite translates and multiplication by three remain Haar-null; \(\nu\) is singular. Each digit possibility has positive probability and offsets cover all classes modulo three, so \(\nu\) has full support. Nonatomicity follows because the product of the largest digit-cylinder probabilities tends to zero. Finally,
\[
\sum_{t\bmod3^r}\nu(t+3^r\mathbb Z_3)^2
=\frac{E_r}{|A_r|^4}
=\frac{127\cdot6^{r-1}+8}{405\cdot16^{r-1}},
\]
whose leading exponential ratio is \(3/8\), giving \(D_2=\log_3(8/3)\).

## Verification
The accompanying standalone Python checker directly evaluates Catalan numbers for all indices below \(3^r\) at \(1\le r\le6\), and independently builds the full residue representation histogram by double enumeration for \(1\le r\le8\). It checks every target against the exact digit formulas, all extrema and energies, and the cyclic adjacent-weight identity through \(m=8\). The observed energies for \(r=1,\ldots,8\) are \(27,154,916,5488,32920,197512,1185064,7110376\). Finite computations serve only as reproducibility checks; the preceding proof establishes every depth and the singularity statement.

To reproduce, execute \(\texttt{python3 check_catalan_energy.py}\) with a standard Python 3 installation; no external packages or data files are required.

## Relationship to prior work
Deutsch and Sagan (2004), Theorem 5.2, determine the exact modulo-three Catalan digit support, which is the foundational input here, but do not compute its modular two-sum representation function, exact additive energy, or the induced self-convolution. Krattenthaler and Müller (2013), §12, give generating-function congruences for Catalan *values* modulo higher powers of three, not for pair sums of indices in their modulo-three unit support. Burns (2016), Theorems 6–7, treats the natural density of the same unit-support index set, not its additive distribution. The present result is a further additive analysis of the established digit set, not a new modulo-three Catalan congruence.

## Limitations
Originality is subject to the possibility that an earlier general theorem on ternary digit convolutions or automatic-set representation functions implicitly contains the exact formulas. The comparison found no explicit equivalent in the inspected primary papers, but absence from searches is not a proof of historical priority. No optimal first-occurrence bound for a fixed integer sum outside the finite cyclic setting is claimed. Independent mathematical audit has not been performed.

## References
1. Emeric Deutsch and Bruce E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326 (first public version July 19, 2004), Theorem 5.2. https://arxiv.org/pdf/math/0407326
2. Christian Krattenthaler and Thomas W. Müller, *A method for determining the mod-\(3^k\) behaviour of recursive sequences*, arXiv:1308.2856 (first public version August 13, 2013), §12 and Theorems 37–39. https://arxiv.org/pdf/1308.2856
3. Rob Burns, *Asymptotic density of Catalan numbers modulo 3 and powers of 2*, arXiv:1611.03705 (first public version November 11, 2016), Theorems 6–7. https://arxiv.org/pdf/1611.03705
