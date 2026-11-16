# Two-to-one short-root profiles and dyadic Fourier recovery in type \(C\)

## Finding
Let \(\Phi_n^+\) be the positive roots of the crystallographic root system of type \(C_n\), for \(n\geq1\), ordered by the positive-simple-root order. Let \(\mathcal I_n\) be **all lower order ideals** of \(\Phi_n^+\), and let \(\Phi_{n,s}^+=\{e_i-e_j,e_i+e_j:1\leq i<j\leq n\}\) be its \(n(n-1)\) short positive roots. Restrict each ideal to its short-root incidence vector \(v(I)\in G_n=\mathbb F_2^{n(n-1)}\), and define the counting kernel \(f_n(x)=\#\{I\in\mathcal I_n:v(I)=x\}\). Thus this is a **multiplicity-weighted** kernel, not the indicator of all full-root ideals nor the indicator of short antichains alone.

**Uniform-fibre theorem.** Every occurring short-root profile has exactly **two** extensions to a full ideal, for every \(n\geq1\). Consequently, \(f_n\) takes only the values \(0,2\), with exactly \(\binom{2n-1}{n-1}\) nonzero values.

**Infinite Fourier consequence.** If \(n\) is a power of two, every unnormalized Walsh multiplier
\[
W_n(k)=\sum_{I\in\mathcal I_n}(-1)^{\langle k,v(I)\rangle},\qquad k\in G_n,
\]
is congruent to \(2\pmod4\) and hence nonzero. Counting convolution by \(f_n\) is therefore invertible on the real or complex \(\ell^2(G_n)\), with inverse Hilbert-space norm at most \(1/2\).

**First exact nonmonotone spectral census.** At ranks \(n=2,3,4,5\), respectively, the numbers of zero multipliers are \(0,18,0,126056\); the respective convolution ranks are \(4,46,4096,922520\), and the least nonzero multiplier magnitudes are \(2,4,2,4\). Rank \(6\) is singular, as exhibited by a signed sum of \(462-462=0\). Thus, among ranks \(2\) through \(6\), precisely ranks \(2\) and \(4\) are invertible; the return to full invertibility at rank \(4\) is followed by renewed singularity. No full rank-six zero count is claimed.

## Assumptions and scope
Take simple roots \(\alpha_i=e_i-e_{i+1}\) for \(1\leq i<n\) and \(\alpha_n=2e_n\). For two positive roots \(\beta,\gamma\), define \(\beta\leq\gamma\) if each coordinate of \(\gamma-\beta\) in the simple-root basis is nonnegative. The positive roots are precisely \(e_i-e_j,e_i+e_j\) for \(i<j\), together with the long roots \(2e_i\). The zero ideal and full ideal are included. All Walsh sums and convolution operators use **unnormalized convolution** and integer-valued characters \((-1)^{\langle k,x\rangle}\), with no probability normalization. Frequencies are ordered by increasing short-root coordinate vectors, first by coefficient sum and then lexicographically, as in the checkers.

## Proof
**1. The long-short spine.** Write \(L_i=2e_i\), \(1\leq i\leq n\), and \(S_i=e_i+e_{i+1}\), \(1\leq i<n\). Direct subtraction of simple-root coordinates gives the strict chain
\[
L_1>S_1>L_2>S_2>\cdots>S_{n-1}>L_n.
\]
For any short positive root \(\beta\), coordinate comparison gives two further precise equivalences:
\[
\beta\leq L_i\ \Longleftrightarrow\ \beta\leq S_i\quad(i<n),
\qquad
L_i\leq\beta\ \Longleftrightarrow\ S_{i-1}\leq\beta\quad(i>1).
\]
Indeed for \(\beta=e_a-e_b\) the final simple-root coefficient is zero, so this root cannot dominate any \(L_i\); it lies below \(L_i\) exactly when \(a\geq i\), in which case it lies below \(S_i\). For \(\beta=e_a+e_b\), the root lies below \(L_i\) exactly when \(a\geq i\), equivalently below \(S_i\). It dominates \(L_i\) exactly when \(b\leq i\), equivalently it dominates \(S_{i-1}\). These observations include all short roots, and the endpoint cases are vacuous where a spine short root does not exist.

**2. Exactly two lifts.** Fix any occurring short-root profile \(J=I\cap\Phi_{n,s}^+\). Its intersection with the short spine consists of the lowest \(t\) members \(S_{n-t},\ldots,S_{n-1}\), for some \(0\leq t\leq n-1\). Their inclusion forces \(L_{n-t+1},\ldots,L_n\); exclusion of the other spine shorts forbids \(L_1,\ldots,L_{n-t-1}\). The remaining long root \(L_{n-t}\) is optional. The equivalences in step 1 show that either choice respects every comparison with every **other** short root: including it requires no short root outside \(J\), and excluding it is not contradicted by any short root in \(J\). Every full ideal extending \(J\) must make one of these two choices, so the fibre has size exactly two. This argument also works for \(n=1\), when the unique long root is optional.

**3. Counting and infinite Fourier nonvanishing.** The established type-\(C_n\) root-ideal count is \(\#\mathcal I_n=\binom{2n}{n}\) (equivalently the type-\(C\) Coxeter-Catalan count). Step 2 gives precisely \(\binom{2n-1}{n-1}\) short profiles. Hence
\[
W_n(k)=2\sum_{x:\,f_n(x)=2}(-1)^{\langle k,x\rangle}.
\]
By Legendre's formula the exponent of \(2\) in \(\binom{2n}{n}\) equals the number of ones in the binary expansion of \(n\). Thus \(\binom{2n-1}{n-1}\) is odd exactly when \(n\) is a power of two. In that case the displayed signed sum contains an odd number of signs, hence is odd: \(W_n(k)\equiv2\pmod4\) for every frequency. Walsh diagonalization of convolution gives invertibility and the inverse-norm bound. This does not claim the converse for every non-power-of-two rank.

**4. Exact first spectral losses.** For each \(n=2,3,4,5\) a finite exhaustive computation produces all \(\binom{2n}{n}\) ideals in two independent ways: by repeatedly adjoining an admissible root and by taking down-closures of all antichains. Their short profiles are compressed into a vector of length \(2^{n(n-1)}\), and an integer Walsh-Hadamard transform computes all signed multipliers. The independent C++ verifier instead directly sums all \(\binom{2n}{n}\) signs for each frequency. Both reproduce the following data:

| Rank \(n\) | Full ideals | Distinct short profiles | Frequencies | Zero multipliers | Convolution rank | Minimum nonzero \(|W_n|\) |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 6 | 3 | 4 | 0 | 4 | 2 |
| 3 | 20 | 10 | 64 | 18 | 46 | 4 |
| 4 | 70 | 35 | 4096 | 0 | 4096 | 2 |
| 5 | 252 | 126 | 1048576 | 126056 | 922520 | 4 |

In rank \(4\), all twelve short-root marginal ideal counts are even (listed in `C4_MARGINALS.tsv`). Together with \(70\equiv2\pmod4\) this provides a second, calculation-light proof that **every** rank-four multiplier is \(2\pmod4\). The frequency with short-coordinate bitmask \(33\) attains \(W_4(33)=2\), so the inverse norm is exactly \(1/2\). At rank \(3\), bitmask \(4\) gives \(10-10=0\); at rank \(5\), bitmask \(514\) gives \(126-126=0\). At rank \(6\), without enumerating its \(2^{30}\) frequencies, bitmask \(524545=2^0+2^8+2^{19}\) gives \(462-462=0\) across all \(924\) ideals. Every bitmask here uses the explicit root ordering in the supplied checkers.

## Verification
Run `python3 short_root_fourier_check.py`; it independently reconstructs the ideals by two exhaustive methods, verifies exact root counts and fibre multiplicity, checks the complete Walsh spectra through rank five, applies Parseval, verifies the rank-six witness, and tests the uniform two-to-one assertion through rank eight. Run `c++ -O3 -std=c++17 short_root_direct_check.cpp -o verify` followed by `./verify` for a separate exact **direct character sum** of every rank-two-through-five Fourier coefficient. Neither checker uses floating point, stored spectrum data, an external package, or a probabilistic test. The infinite result is established by steps 1–3, not extrapolated from the checks.

## Relationship to prior work
Panyushev's 2003 theory explicitly studies short antichains, short-root ideals and the type-\(C\) shifted Ferrers model and establishes the corresponding Catalan enumerations. The present kernel instead pushes **all** root ideals forward under restriction to short-root membership and counts their multiplicities. The two-to-one extension statement and its binary Fourier consequence are not among the statements inspected in that work. Armstrong–Stump–Thomas (2011) gives type-\(C\) nonnesting/noncrossing bijections and cyclic sieving, not additive binary short-profile Fourier nullities. Abe–Barakat–Cuntz–Hoge–Terao (2013) proves freeness and exponent formulas for ideal subarrangements, not these character sums. General Walsh-transform algorithms can calculate the listed small-rank numbers, but the evaluated classification and uniform-fibre argument require additional analysis.

## Limitations
Invertibility is proved for every power-of-two rank, but no converse is established for arbitrary other ranks. The complete zero-multiplier and minimum-nonzero-multiplier census is established only for ranks two through five; rank six has only an explicit zero witness. The infinite result concerns multiplicity-weighted **short-root profiles of all ideals**, not the entire positive-root incidence family nor a uniform probability distribution on distinct profiles. External independent mathematical review and exhaustive historical-priority certification have not been performed.

## References
1. D. I. Panyushev, *Short antichains in root systems, semi-Catalan arrangements, and B-stable subspaces*, first submitted 2003-04-24, https://arxiv.org/abs/math/0304380. Especially sections 1, 4, and 7 on short roots, root ideals, and shifted Ferrers diagrams.
2. D. Armstrong, C. Stump, H. Thomas, *A uniform bijection between nonnesting and noncrossing partitions*, first submitted 2011-01-06, https://arxiv.org/abs/1101.1277.
3. T. Abe, M. Barakat, M. Cuntz, T. Hoge, H. Terao, *The freeness of ideal subarrangements of Weyl arrangements*, first submitted 2013-04-30, https://arxiv.org/abs/1304.8033.
