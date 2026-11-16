# Four-colour wheel convolution: universal Fourier support and a six-rim group-law distinction

## Finding
Let \(m\ge3\), let \(W_m=K_1\vee C_m\) have one labelled hub and \(m\) cyclically labelled rim vertices, and let \(H\) be either \(C_4=\mathbb Z/4\mathbb Z\) or \(V_4=(\mathbb Z/2\mathbb Z)^2\). Encode proper vertex colourings as a subset \(A_{m,H}\subset H^{m+1}\). With unnormalized additive Fourier coefficients
\[
\widehat{1_A}(\xi)=\sum_{c\in A_{m,H}}\prod_{v}\chi_{\xi_v}(c_v),
\]
all nonbalanced frequencies, those with \(\sum_v\xi_v\ne0\), vanish. **Every balanced coefficient is a nonzero real integer divisible by eight but not sixteen**. Thus the counting-convolution operator on \(H^{m+1}\) has rank exactly \(4^m\) and nullity exactly \(3\cdot4^m\). Its largest multiplier modulus is \(4(2^m+2(-1)^m)\), its smallest positive multiplier modulus is exactly \(8\), and its sharp positive-spectrum condition number is
\[
\kappa_m=2^{m-1}+(-1)^m.
\]
Despite these common rank and stability invariants, the complete absolute Fourier spectra of \(C_4\) and \(V_4\) agree for \(m=3,4,5\), and first differ at \(m=6\). At six rim vertices, their squared *reduced* coefficient magnitudes \(|\widehat{1_A}/4|^2\) have the following exhaustive multiplicities (one balanced frequency for each reduced rim frequency):

| Squared reduced magnitude | \(C_4\) | \(V_4\) |
|---:|---:|---:|
| 4 | 1664 | 1632 |
| 36 | 1107 | 1203 |
| 100 | 891 | 795 |
| 196 | 262 | 294 |
| 324 | 45 | 45 |
| 484 | 108 | 108 |
| 676 | 18 | 18 |
| 4356 | 1 | 1 |

Each column sums to \(4096=4^6\). Frequencies unbalanced with the hub coordinate vanish and do not enter the table.

## Assumptions and scope
The group is one of the two abelian groups of order four, with its ordinary full character group. Rim positions are labelled, and all proper colourings of the fixed wheel graph are counted once. No probability normalization is used in Fourier coefficients or convolution; changing to uniform probability convolution scales all positive multiplier magnitudes equally and leaves rank and condition number unchanged. The graph definition uses \(m\) rim vertices rather than a convention in which the wheel subscript denotes total vertices. The exact six-rim comparison is a finite computation with an exhaustive exact-arithmetic certificate, whereas the support and conditioning formula hold for every \(m\ge3\).

## Proof
Write the hub colour as \(h\) and the rim colours as \(h+y_1,\ldots,h+y_m\), where \(y_i\) ranges over the three nonzero elements of \(H\) and adjacent cyclically indexed \(y_i\)'s are unequal. Summing the common hub translation gives
\[
\widehat{1_A}(\xi)=4\,\mathbf1_{\{\sum_v\xi_v=0\}}F_H(k_1,\ldots,k_m),\qquad
F_H(k)=\sum_{\substack{y_i\in H\setminus\{0\}\\y_i\ne y_{i+1}}}\prod_i\chi_{k_i}(y_i).
\]
The number of labelled proper rim assignments is \(N_m=\operatorname{tr}(J_3-I_3)^m=2^m+2(-1)^m\). The natural action of all six permutations of the three nonzero colour labels on such assignments is free: every proper rim assignment uses at least two different colours. Hence there are \(N_m/6\) orbits, an odd number because \(N_m\equiv6\pmod{12}\) for \(m\ge3\).

We prove that the signed character sum over each six-element orbit is a real integer congruent to \(2\pmod4\). For \(V_4\), each character takes values \(\pm1\). Across the six permutations, each original colour is sent to each target colour exactly twice. The product of all six character weights is therefore \(+1\). Thus the number of negative weights is even, so the sum of the six signs equals \(6-2t\equiv2\pmod4\).

For \(C_4\), index the three nonzero colours as \(1,2,3\) and write \(\chi_k(y)=i^{ky}\). Group all position frequencies originally carrying a given colour, giving three exponents \(a,b,c\in\mathbb Z/4\mathbb Z\). The orbit sum is \(\sum_{\pi\in S_3}i^{a\pi(1)+b\pi(2)+c\pi(3)}\). Pair permutations in which two original groups, of exponent \(a,b\), are sent respectively to target colours \(1,3\) in opposite orders, while the remaining group is sent to colour \(2\). This pair contributes
\[
(-1)^c i^{a+3b}\bigl(1+(-1)^{a+b}\bigr).
\]
It vanishes when \(a+b\) is odd, and otherwise equals \(+2\) or \(-2\), since \(a+3b\) is even. Of the three choices of the group sent to colour \(2\), an odd number have the other two exponents of the same parity: three when all parities agree, and one otherwise. Consequently every orbit sum is real and congruent to \(2\pmod4\). Summing the odd number of orbits gives \(F_H(k)\equiv2\pmod4\), proving all balanced multipliers are nonzero and have absolute value at least eight. Exactly \(4^m\) balanced frequencies exist, proving the rank and nullity.

At the zero frequency \(F_H(0)=N_m\); the triangle inequality shows that \(4N_m\) is the largest multiplier modulus. To attain the lower bound, put distinct nonzero frequency elements \(a=2\) and \(b=1\) at the first and third rim vertices, all other rim frequencies zero, and the unique balancing frequency at the hub. For both groups, \(a,b,a+b\) are nonzero, and \(\sum_{y\ne0}\chi_c(y)=-1\) for each of those three characters. The three-by-three adjacency matrix \(K=J_3-I_3\) has \(K^r_{uu}=(2^r+2(-1)^r)/3\) and \(K^r_{uv}=(2^r-(-1)^r)/3\) for \(u\ne v\). Counting rim walks with the first and third colours equal or different yields
\[
F_H(a,0,b,0,\ldots,0)=-2(-1)^m.
\]
Thus the minimum positive multiplier is exactly eight and the stated sharp condition number follows.

Finally, equality of the two complete magnitude distributions at \(m=3,4,5\), and the displayed strict difference at \(m=6\), follow from the self-contained exhaustive integer algorithms in `check_fourier.py` and `check_transfer.cpp`. For every \(m\le6\), the first enumerates each proper rim assignment and performs an exact tensor character transform; the second independently computes each coefficient via a three-state transfer trace over Gaussian integers. Both inspect all \(4^m\) rim frequencies for each group and compare their full squared-magnitude histograms. This gives a genuine exhaustive proof of the finite first-divergence assertion; no extrapolation from finite experiments is used for the all-length support theorem.

## Verification
Run `python check_fourier.py` (Python 3 with NumPy), and compile and run `check_transfer.cpp` with `c++ -std=c++17 -O2 check_transfer.cpp -o check_transfer && ./check_transfer`. The independent approaches agree at all examined sizes, with their first histogram difference at six rim vertices; the first program checks through eight and the second through nine rim vertices. The all-length residue and sharp witness formulas are proved above without finite extrapolation.

## Relationship to prior work
Goodall (2007) develops finite-abelian Fourier methods for graphical partition functions, flows and Potts-model colourings. The classical chromatic-polynomial calculation gives the wheel colouring count but not the full characterwise nonvanishing, exact minimum multiplier, or cyclic-versus-Klein six-rim magnitude comparison. A previously published general congruence for proper Klein-four colourings already implies the \(V_4\) wheel *rank* conclusion; that rank special case is not claimed as new. The present additional conclusions concern cyclic four-colour Fourier support, exact sharp stability for both groups, and the first group-law separation of full magnitude spectra under wheel constraints. Previously computed four-colour surjection spectra concern unconstrained onto words rather than cycle-adjacency-constrained wheel colourings; they do not imply the six-rim table here.

## Limitations
All-length character nonvanishing and the sharp conditioning formula are proved only for the two four-element abelian groups and this wheel family. The complete magnitude distributions are tabulated at the first separating size, not classified for all rim lengths. The numerical comparison is rigorous because it exhausts an explicitly finite set using integer arithmetic; no statement about larger rim lengths' detailed spectral multiplicities follows from the table. Historical priority cannot be proved from bounded literature and record searches; equivalent unindexed computations remain possible. No independent audit has been performed.

## References
1. A. Goodall, “Fourier Analysis on Finite Abelian Groups: Some Graphical Applications,” in *Combinatorics, Complexity, and Chance*, pp. 103–129, published 18 January 2007. DOI: https://doi.org/10.1093/acprof:oso/9780198571278.003.0007 . Author-uploaded readable full text: https://www.researchgate.net/publication/266250848_Fourier_Analysis_on_Finite_Abelian_Groups_Some_Graphical_Applications .
2. E. W. Weisstein, “Wheel Graph,” *MathWorld*, https://mathworld.wolfram.com/WheelGraph.html (classical wheel definition and chromatic polynomial; consulted as background).
3. Earlier general Klein-four Fourier congruence for proper graph colourings, mathematical record ID `562fe56e-a7e5-4204-9a43-cfc1bb680dc8`; related cycle Fourier result ID `ace1142c-1563-47a6-931e-01252955ad6c`; related four-colour surjection comparison ID `fb5f5c63-18d9-4e61-982c-6ae1668e90d5` (overlap comparators, not evidence of independent validation).
