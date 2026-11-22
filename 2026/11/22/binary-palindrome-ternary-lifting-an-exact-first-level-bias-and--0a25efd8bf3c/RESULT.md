# Binary-palindrome ternary lifting: an exact first-level bias and unrestricted higher lifts

## Finding

For integers \(m\ge1\), let \(\mathcal B_{2m}\) be the set of positive integers whose canonical base-two expansion is a palindrome of exactly \(2m\) digits. Every member is divisible by three. For \(r\in\{0,1,2\}\), put
\[
H_m(r)=\#\{P\in\mathcal B_{2m}:P/3\equiv r\pmod3\},\qquad Z=\lfloor m/3\rfloor,\quad N=2^{m-1}.
\]
The **exact first-lift law** is
\[
\boxed{
(H_m(0),H_m(1),H_m(2))=
\begin{cases}
((N-2^Z)/3,(N+2^{Z+1})/3,(N-2^Z)/3),&m\equiv1\pmod3,\\
((N+2^Z)/3,(N-2^{Z+1})/3,(N+2^Z)/3),&m\equiv0,2\pmod3.
\end{cases}}
\]
The first and third counts are always equal, but their difference from the middle count has exact magnitude \(2^{\lfloor m/3\rfloor}\), with sign changing periodically with \(m\). All three first-lift classes occur for every \(m\ge4\), and the lower bound four is sharp.

**All-level lifting theorem.** For every \(k\ge2\), let
\[
M_k=(5\cdot3^{k-2}+3)/2.
\]
For **every** \(m\ge M_k\), the residue set of \(\mathcal B_{2m}\) modulo \(3^k\) is exactly the \(3^{k-1}\) classes divisible by three. Thus the closure of all even-digit binary palindromes in the three-adic integers is exactly \(3\mathbb Z_3\), of normalized Haar measure \(1/3\). Each such residue is realized at every sufficiently large even length, hence infinitely often. The stated sufficient bound \(M_k\) is sharp for \(k=2\), but not asserted optimal for larger \(k\).

## Assumptions and scope

The digits of an exactly \(2m\)-digit binary palindrome are \(\varepsilon_0,\ldots,\varepsilon_{m-1}\), counted from the outer (least significant) end, mirrored at the middle; \(\varepsilon_0=1\) and all other digits are arbitrary elements of \(\{0,1\}\). Writing
\[
P=\sum_{j=0}^{m-1}\varepsilon_j(2^j+2^{2m-1-j}),\qquad
w_{m,j}=\frac{2^j+2^{2m-1-j}}3,
\]
we have \(P/3=\sum_j\varepsilon_j w_{m,j}\in\mathbb Z\). The initial bit must be one, and leading zeros are never counted as different numbers. Every length, congruence and closure statement concerns these canonical integer palindromes, not palindromic strings with optional initial zeros.

## Proof

**1. Divisibility and the exact valuation of a digit coefficient.** Since \(2\equiv-1\pmod3\), the two exponents \(j\) and \(2m-1-j\) have opposite parity, so their powers sum to zero modulo three. Set \(d=2m-1-2j\), a positive odd integer. Then
\[
w_{m,j}=2^j(2^d+1)/3.
\]
The standard odd-exponent lifting-the-exponent identity gives \(\nu_3(2^d+1)=1+\nu_3(d)\), whence the exact and all-index formula
\[
\boxed{\nu_3(w_{m,j})=\nu_3(2m-1-2j).}
\]

**2. The exact first lift.** Expanding \(2=-1+3\) modulo nine in the two paired powers proves
\[
w_{m,j}\equiv(-1)^j(2m-1-2j)\pmod3.
\]
Among the free indices \(1\le j<m\), exactly \(Z=\lfloor m/3\rfloor\) give residue zero. Denoting the numbers with residue one and two by \(a\) and \(b\), a direct inspection of the periodic six-index pattern yields
\[
a-b=\begin{cases}0,&m\equiv1\pmod3,\\-1,&m\equiv2\pmod3,\\1,&m\equiv0\pmod3.\end{cases}
\]
Moreover \(w_{m,0}\equiv2m-1\pmod3\). For \(\omega=e^{2\pi i/3}\), the finite Fourier identity for independent binary choices is
\[
H_m(r)=\frac13\left(2^{m-1}+2\operatorname{Re}\left[\omega^{w_{m,0}-r}\prod_{j=1}^{m-1}(1+\omega^{w_{m,j}})\right]\right).
\]
Here \(1+\omega=e^{\pi i/3}\), \(1+\omega^2=e^{-\pi i/3}\), and \(1+\omega^0=2\), so the product is exactly \(2^Z e^{(a-b)\pi i/3}\). The three cases of \(m\pmod3\) give the displayed formula. For \(m=1,2,3\), the counts show a missing class, whereas for all \(m\ge4\) every count is positive. In fact \(H_m(1)-H_m(0)\) equals \(+2^Z\) for \(m\equiv1\pmod3\) and \(-2^Z\) otherwise; this proves the sharp discrepancy statement.

**3. Explicit uniform lifting to every power of three.** Fix \(k\ge2\) and \(m\ge M_k\). For each \(\ell=0,1,\ldots,k-2\), select the two free indices
\[
j_{\ell,1}=\frac{2m-1-3^\ell}{2},\qquad
j_{\ell,5}=\frac{2m-1-5\cdot3^\ell}{2}.
\]
The bound on \(m\) guarantees that all these indices lie in \(\{1,\ldots,m-1\}\). They are integers because both distances are odd, and they are pairwise distinct because the positive integers \(3^\ell\) and \(5\cdot3^\ell\) are distinct across all \(\ell\). The valuation formula gives
\[
\nu_3(w_{m,j_{\ell,1}})=\nu_3(w_{m,j_{\ell,5}})=\ell.
\]
Inductively prescribe any target residue \(t\pmod{3^{k-1}}\) for the quotient \(P/3\). Initially fix \(\varepsilon_0=1\), and set all unused bits to zero. At level \(\ell\), previously fixed bits have established the correct residue modulo \(3^\ell\). Each of the two new free coefficients is \(3^\ell\) times a unit modulo three. The four choices of the corresponding two bits have normalized new contributions \(\{0,u,v,u+v\}\pmod3\), where \(u,v\in\{1,2\}\), and this set is **all three residues**. Thus one choice corrects the next ternary digit without altering lower digits. Repeat through \(\ell=k-2\) to obtain \(P/3\equiv t\pmod{3^{k-1}}\), or equivalently \(P\equiv3t\pmod{3^k}\). No other residue is possible by step 1. Because the construction works at every \(m\ge M_k\), each admissible residue has infinitely many distinct palindromic representatives. The modular image at all depths establishes the closure identity and its normalized Haar measure.

## Verification

The standalone Python 3 file `verify.py` reproduces the canonical-palindrome digit coefficients and checks the exact first-lift histogram independently by enumerating all \(131071\) palindromes of lengths \(2,4,\ldots,34\), comparing the counts against the closed formulas. It also checks the coefficient congruence and valuation for \(2850\) pairs of \((m,j)\), and builds explicit greedy binary-digit witnesses for **every** normalized target residue at levels \(k=2,\ldots,7\), with the respective guaranteed half-lengths \(4,9,24,69,204,609\) (\(1092\) target witnesses). Execute `python verify.py` from the directory containing this file. These finite checks corroborate, but do not replace, the infinite proof above.

## Relationship to prior work

Even-length base-\(b\) palindromes are classically divisible by \(b+1\); this is not presented as new. Harminc and Soták [1] show that general base-\(b\) palindrome representations occur infinitely often in eligible arithmetic progressions, without an exact-length, all-even-length, all-residue spectrum or a first-lift frequency law. Tuxanidy and Panario [2] prove equidistribution results for palindromes in restricted coprimality settings, excluding the divisibility-by-three direction of the present even-binary problem. Onphaeng et al. [3] prove exact formulas for selected arithmetic progressions when \(b\equiv0\) or \(1\pmod q\); here \(b=2\) and \(q=3^k\), so these hypotheses do not hold when \(k\ge1\). The earlier exact count for odd-length palindromes with \(q\mid b+1\) [4] includes the base-two modulus-three case and the classical even-length zero congruence, but not lifting modulo \(9,27,\ldots\), nor the exact modulo-nine imbalance. None of these sources is claimed to be an independent confirmation of this theorem.

## Limitations

The upper bound \(M_k\) is a constructive sufficient length, not a minimal length classification except at the first lift \(k=2\). The theorem does not give exact nontrivial frequencies at powers \(3^k\) for \(k\ge3\), uniform mixing rates there, or results for arbitrary numeral bases or prime powers other than three. Earlier general existence theorems may admit unrecorded even-length refinements, and implicit instances in unsurveyed digit-automata literature remain possible. The proof and finite checker have not undergone independent scientific audit.

## References

[1] M. Harminc and R. Soták, *Palindromic Numbers in Arithmetic Progressions*, Fibonacci Quarterly **36** (1998), 259–262, DOI 10.1080/00150517.1998.12428937; https://www.academia.edu/18838282/PALINDROMIC_NUMBERS_IN_ARITHMETIC_PROGRESSIONS.

[2] A. Tuxanidy and D. Panario, *Infinitude of Palindromic Almost-Prime Numbers*, arXiv:2307.16637v1 (first posted 2023-07-31); https://arxiv.org/abs/2307.16637.

[3] K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap, and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences **27** (2024), Article 24.4.8; https://cs.uwaterloo.ca/journals/JIS/VOL27/Phunphayap/phun7.html.

[4] *Exact residue counts for palindromes modulo divisors of the base plus one*, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-residue-counts-for-palindromes-modulo-divisors-of-the-base--bab47a6477c9.
