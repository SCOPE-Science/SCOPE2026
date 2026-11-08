# The seven-phase threshold for improved Barker-seven Fourier fourth moments

## Finding
For each integer \(2\le q\le7\), write \(\zeta_q=e^{2\pi i/q}\), and let
\[
P_x(z)=\sum_{j=0}^{6}\zeta_q^{x_j}z^j,\qquad x_j\in\mathbb Z/q\mathbb Z.
\]
With normalized Haar measure on the unit circle, put \(M_q(x)=\int_{\mathbb T}|P_x|^4\,dm\). Then the exact minimum over all \(q^7\) coefficient arrays, and the number of arrays attaining it, are

| \(q\) | Sharp minimum \(M_q\) | Normalized minimizers | All minimizers |
| --- | --- | ---: | ---: |
| 2 | \(55\) | 1 | 4 |
| 3 | \(57\) | 2 | 18 |
| 4 | \(55\) | 1 | 16 |
| 5 | \(86-13\sqrt5\) | 4 | 100 |
| 6 | \(55\) | 1 | 36 |
| 7 | \(87-52\cos(2\pi/7)\) | 2 | 98 |

Here normalized means \(x_0=x_1=0\). In particular, the smallest integer phase-alphabet size among \(q\ge2\) for which a length-seven polyphase sequence strictly improves the classical binary Barker-seven fourth moment \(55\) is \(q=7\). Its exact optimum integrated aperiodic sidelobe energy is
\[
\boxed{E_7=19-26\cos(2\pi/7)=2.7892651516729\ldots<3.}
\]
The two normalized seven-phase minimizers, and no others, have exponent vectors
\[
(0,0,2,2,6,1,5),\qquad(0,0,5,5,1,6,2).
\]
Every unrestricted optimizer arises uniquely from a normalized one by adding \(u+vj\pmod q\) to its \(j\)-th exponent, with \(u,v\in\mathbb Z/q\mathbb Z\).

## Assumptions and scope
All statements concern exactly seven consecutive Fourier frequencies \(0,1,\ldots,6\), all coefficients of unit modulus, and coefficients restricted to the \(q\)-th roots of unity for each listed \(q\). The phase alphabets are distinct sets rather than automatically nested: for example a fifth-root alphabet is not contained in a sixth-root alphabet. The exact minima are for the **continuous torus integral**, not a finite Fourier sampling grid. Define
\[
C_k(x)=\sum_{j=0}^{6-k}\zeta_q^{x_{j+k}-x_j},\quad
E_q(x)=\sum_{k=1}^{6}|C_k(x)|^2.
\]
The identity \(M_q(x)=49+2E_q(x)\) will follow from Fourier orthogonality. No claim about the unrestricted continuous-phase optimum is made.

## Proof
**Aperiodic Fourier identity.** Expanding \(|P_x(z)|^2\) produces constant coefficient \(7\), positive Fourier coefficients \(C_k\), and negative coefficients \(\overline{C_k}\). Parseval gives
\[
\int_{\mathbb T}|P_x|^4\,dm=7^2+2\sum_{k=1}^{6}|C_k|^2=49+2E_q(x).
\]

**Exact phase-gauge reduction.** The transformation
\[
x_j\mapsto x_j+u+vj\pmod q
\]
makes each \(C_k\) change only by \(\zeta_q^{vk}\), so \(E_q\) is invariant. Every array has a unique normalized representative: choose \(u=-x_0\), \(v=x_0-x_1\). Distinct pairs \((u,v)\) are distinct on the coefficient array, so each normalized representative accounts for exactly \(q^2\) arrays. Consequently enumerating the \(q^5\) possibilities \((x_2,\ldots,x_6)\) with \(x_0=x_1=0\) is exhaustive, not a random or truncated sample.

**Exact cyclotomic reduction.** For an integer vector \(x\), define its profile \(N_d(x)\), \(0\le d<q\), to be the count of ordered pairs of terms with difference \(d\pmod q\) in the six positive-lag autocorrelation squares:
\[
N_d(x)=\sum_{k=1}^{6}\#\{(j,\ell):0\le j,\ell\le6-k,\ 
(x_{j+k}-x_j)-(x_{\ell+k}-x_\ell)\equiv d\pmod q\}.
\]
Thus \(\sum_d N_d=1^2+\cdots+6^2=91\), \(N_d=N_{q-d}\), and
\[
E_q(x)=\sum_{d=0}^{q-1}N_d(x)\cos(2\pi d/q).
\]
The six optimal ordered profiles \((N_0,\ldots,N_{q-1})\), found by the complete integer enumeration below, are respectively
\[
\begin{array}{c|l}
q&\text{winning profile}\\\hline
2&(47,44)\\
3&(33,29,29)\\
4&(47,0,44,0)\\
5&(33,8,21,21,8)\\
6&(47,0,0,44,0,0)\\
7&(33,1,14,14,14,14,1).
\end{array}
\]
These profiles imply in order
\[
E_q^{\min}=3,\ 4,\ 3,\ \tfrac{37-13\sqrt5}{2},\ 3,\ 19-26\cos(2\pi/7).
\]

**Exhaustive rational certificate and equality cases.** The complete checker `check_psk7.py` uses only Python standard-library integer and rational arithmetic. It enumerates every normalized exponent tuple, forms all exact integer profiles, and compares each nonwinner profile against the winning one by *disjoint rigorous rational enclosures* for the relevant cosines. Thus it does not rely on floating-point rounding or a discrete approximation to the circle integral. The implemented enclosure derives rational bounds for \(\pi\) from Machin's identity
\[
\pi=16\arctan(1/5)-4\arctan(1/239)
\]
using alternating-series bounds, and then encloses each cosine using 21 rational Taylor terms with remainder at most \((44/7)^{42}/42!\). All cosine enclosures are outward rounded to multiples of \(10^{-15}\). For each listed \(q\) the checker verifies that every nonwinner energy lower bound strictly exceeds the winner energy upper bound. The smallest such *nonwinner* lower bounds for \(q=2,\ldots,7\) are, respectively, greater than \(6.9999\), \(6.9999\), \(6.9999\), \(5.1458\), \(3.9999\), and \(3.6618\), while the winner upper bounds are below \(3.0001\), \(4.0001\), \(3.0001\), \(3.9656\), \(3.0001\), and \(2.7893\). Hence the minimizers are precisely the arrays with the winning profile; the checker counts them exhaustively.

Their normalized exponent lists are: for \(q=2\), \((0,0,0,1,1,0,1)\); for \(q=3\), \((0,0,1,1,0,1,0)\) and its negation; for \(q=4\), \((0,0,0,2,2,0,2)\); for \(q=5\), \((0,0,1,1,4,0,3)\), \((0,0,2,2,0,2,0)\), \((0,0,3,3,0,3,0)\), \((0,0,4,4,1,0,2)\); for \(q=6\), \((0,0,0,3,3,0,3)\); and for \(q=7\), the two vectors stated in the finding. Multiplying their numbers \(1,2,1,4,1,2\) by \(q^2\) proves all counts in the table.

Finally \((37-13\sqrt5)/2>3\), and the checker rigorously proves \(19-26\cos(2\pi/7)<3\), giving the sharp smallest-alphabet transition. The exact fourth-moment values follow from the initial Parseval identity.

## Verification
Run `python3 check_psk7.py` with Python 3 and no dependencies. It checks exactly \(32+243+1024+3125+7776+16807=29007\) gauge-normalized arrays and 29007 integer correlation profiles. Its final line is `SEVEN_PSK_EXACT_ENUMERATION_PASS`. Each winner is verified by its computed autocorrelation profile; all nonwinners are excluded by certified rational separation. The algorithm relies on the finite integer phase alphabets, so the completeness inference applies only to those sets. An independent mathematical audit has not been performed.

## Relationship to prior work
The 2022 study of Syms and Noorwali exhaustively treats several short-polyphase alphabets in its search for low **peak sidelobes and cross-correlation code families**. Its objective is not a classification of the single-sequence **total squared aperiodic autocorrelation** over every alphabet through seven, and it does not examine the seven-phase alphabet. Raei and coauthors (first public 2021) explicitly formulate both discrete-phase and continuous-phase integrated sidelobe minimization but provide numerical optimization algorithms rather than the exact seven-tap, alphabet-specific minima and equality counts. Borwein and Ferguson (2005) study the same integrated aperiodic energy over continuous phases; their length-seven numerical table estimates a smaller *unrestricted* value, and hence does not furnish a sharp finite-seven-phase result. Published small-length analytical studies of five- and six-tap polyphase polynomials establish exact minima for different lengths; the nine-frequency two-dimensional square is a different Fourier support. Neither these results nor the motivating papers imply the theorem here.

## Limitations
The theorem does not determine the optimal moment for arbitrary unimodular phases, for \(q\ge8\), or for other lengths. In particular, the seven-phase minimum is **not** asserted to be optimal among all continuous phases. The finite-exhaustive certificate is reproducible from rational arithmetic; its exhaustiveness depends on the exact gauge reduction and on checking all \(q^5\) tuples. The mathematical value is the sharp first phase-resolution transition for the fixed natural seven-tap aperture, not an asymptotic claim. A specialized unindexed tabulation of exactly these small phase alphabets remains a bibliographic priority risk.

## References
1. R. R. A. Syms and A. Noorwali, “Polyphase codes for multiplexed acoustic signalling and sensing on pipes,” *Smart Materials and Structures* 31 (2022), 095033. First public 2022-08-02. DOI `10.1088/1361-665X/ac8385`.
2. E. Raei, M. Alaee-Kerahroodi, P. Babu, M. R. B. Shankar, “Design of MIMO Radar Waveforms based on \(\ell_p\)-Norm Criteria,” arXiv `2104.03303v1`, first public 2021-04-07.
3. P. Borwein and R. Ferguson, “Polyphase sequences with low autocorrelation,” *IEEE Transactions on Information Theory* 51 (2005), 1564–1567. DOI `10.1109/TIT.2004.842778`.
4. “Exact continuous-phase merit optimum at length five,” mathematical report (2026), published repository `published-finding corpus/2026`, record `afb1037d2af7`.
5. “Exact length-six polyphase base-energy minimum,” mathematical report (2026), published repository `published-finding corpus/2026`, record `b03150b9996c`.
6. “Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture,” mathematical report (2026), published repository `published-finding corpus/2026`, record `f31c28437f0d`.
