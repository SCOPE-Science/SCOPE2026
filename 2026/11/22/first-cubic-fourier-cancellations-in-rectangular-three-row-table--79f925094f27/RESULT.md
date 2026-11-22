# First cubic Fourier cancellations in rectangular three-row tableau words

## Finding

Let \(\mathcal W_n\subseteq(\mathbb Z/3\mathbb Z)^{3n}\) be the set of words with exactly \(n\) copies of each symbol \(0,1,2\), such that every prefix has symbol multiplicities \(c_0\ge c_1\ge c_2\). These are the row-index words of standard Young tableaux of rectangular shape \((n,n,n)\). Write \(f_n=\mathbf1_{\mathcal W_n}\). On the full complex group algebra, define \(T_n h=f_n*h\), with unnormalized convolution. The exact ranks at the first four rectangular widths are

| \(n\) | \(|\mathcal W_n|\) | \(|G_n|\) | Fourier zeros | \(\operatorname{rank}T_n\) | smallest degree of a zero |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 27 | 0 | 27 | none |
| 2 | 5 | 729 | 0 | 729 | none |
| 3 | 42 | 19683 | 1134 | 18549 | 2 |
| 4 | 462 | 531441 | 3996 | 527445 | 3 |

In particular, **all Fourier characters supported on at most two coordinates survive at width four**, despite a nontrivial convolution kernel. There are exactly eight vanishing cubic characters. Using one-based coordinate positions and recording the three nonzero frequency entries in the corresponding order, these are

| support | nonzero entries |
|---|---|
| \(\{2,5,8\}\) | \((1,2,2)\), \((2,1,1)\) |
| \(\{2,5,9\}\) | \((1,2,2)\), \((2,1,1)\) |
| \(\{4,8,11\}\) | \((1,1,2)\), \((2,2,1)\) |
| \(\{5,8,11\}\) | \((1,1,2)\), \((2,2,1)\) |

For a witness on \(\{2,5,8\}\) with entries \((1,2,2)\), the 462 words give exactly 154 phase exponents in each of the three residue classes, so the character sum vanishes.

## Assumptions and scope

The ambient group is the **full** ternary product group \(G_n=(\mathbb Z/3\mathbb Z)^{3n}\), not the 462-point tableau set treated as a group. Characters are \(\chi_t(w)=\omega^{\sum_{j=1}^{3n}t_jw_j}\), with \(\omega=e^{2\pi i/3}\), so the Fourier coefficient is \(\widehat f_n(t)=\sum_{w\in\mathcal W_n}\chi_t(w)\). Degree means the number of nonzero frequency coordinates \(t_j\). The opposite Fourier sign convention conjugates every coefficient and leaves zeros unchanged. All ranks and nullities are over \(\mathbb C\). These are finite, exactly stated widths; no conclusion is asserted for \(n\ge5\).

## Proof

**1. Correct support.** In a standard tableau, record the row containing entry \(j\) as its \(j\)-th symbol. The row lengths give exactly \(n\) occurrences of each symbol, and the shape after inserting labels \(1,\ldots,j\) is a Young diagram precisely when each prefix has \(c_0\ge c_1\ge c_2\). The reverse construction fills the next available cell in the indicated row. Thus the two descriptions are bijective. The enumerator in `verify.py` extends every legal prefix by all three possible symbols and rejects precisely forbidden extensions. It exhausts the finite sets without duplicate words. The independent rectangular hook-length calculation gives support sizes \(1,5,42,462\).

**2. Exact Fourier factorization.** Every Fourier coefficient lies in \(\mathbb Z[\omega]\). Represent it uniquely as \(a+b\omega\), with \(a,b\in\mathbb Z\), using \(\omega^2=-1-\omega\). For a fixed coordinate, Fourier transformation of the three input values \((u,v,w)\) is exactly

\[
(u+v+w,\quad u+\omega v+\omega^2w,\quad u+\omega^2v+\omega w).
\]

Applying this identity successively at all \(3n\) coordinates computes every frequency in \(G_n\). Both the initialization and every butterfly are integral operations on the two coefficients \((a,b)\); no rounding or tolerance enters the result. A coefficient is zero **if and only if** both integral coordinates are zero, because \(1,\omega\) are linearly independent over \(\mathbb Q\).

**3. Exhaustive exact certificate.** The included standalone `verify.py` implements the preceding transform using the finite index \(\sum_j w_j3^{j-1}\) and enumerates all \(3^{3n}\) outputs. For widths 1–4 the zero totals are respectively \(0,0,1134,3996\). At width four the zero counts by frequency degree are

| degree | 0–2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| zeros | 0 | 8 | 62 | 204 | 456 | 776 | 870 | 796 | 680 | 144 | 0 |

The table sums to \(3996\). Since convolution is diagonalized by all characters of the finite abelian group, its rank is the number of nonzero Fourier coefficients, giving \(531441-3996=527445\). The degree-three list above is checked against a second, direct summation over all 462 words. This proves the claimed finite rank, the low-degree protection, and the exact eight-cubic classification.

## Verification

Run `python3 verify.py` from the directory containing that file. It requires Python's standard library only. The program independently checks every character of degrees 0 through 3 by direct residue-class summation, checks further nonlocal frequencies, verifies conjugate character symmetry at every frequency and the integer Parseval identity \(\sum_t|\widehat f_n(t)|^2=|G_n|\,|\mathcal W_n|\). At width four it checks every cubic frequency directly and confirms that exactly the eight displayed witnesses vanish. The fixed assertion totals and the precise verified output are explained in `VERIFICATION.md`.

The exhaustive certificate is a **finite proof for these four widths**; neither it nor a numerical experiment establishes a higher-width theorem.

## Relationship to prior work

Eu (2010) develops the row-index/Yamanouchi-word correspondence and enumeration through Motzkin paths for tableaux of height at most three. Kim (2011) treats generating functions for three-row skew tableaux using symmetric functions and Motzkin-number expressions. These provide a natural, established tableau family and counting tools, but do not state a character-by-character Fourier nullity or the exact ternary convolution rank at shape \((4,4,4)\). Other exact Fourier studies of tableau sampling at shape \((3,3,3)\) address restricted observation matrices on tableaux, which are not the convolution operators on the full ternary word group studied here. The absence of a matching result in the searched sources is not a proof of global priority.

## Limitations

Only the four stated widths are proven; the displayed character classes and all nullities are unnormalized and use the full ambient ternary group. No asymptotic claim, complete formula for larger rectangles, or independent validation is asserted. A sufficiently detailed earlier position-weighted tableau enumerator could imply the reported finite Fourier values without using Fourier terminology; that remains a priority risk.

## References

1. S.-P. Eu, *Skew-standard tableaux with three rows*, arXiv:1002.4060, first publicly posted 2010-02-22, https://arxiv.org/abs/1002.4060. See its definition of row-index words and the Motzkin-path bijection.
2. J. H. Kim, *On the enumeration of three-rowed standard Young tableaux of skew shape in terms of Motzkin numbers*, arXiv:1107.3873, first publicly posted 2011-07-20, https://arxiv.org/abs/1107.3873. See its introduction and symmetric-function enumerations.
3. The MSC2020 classification description of 43A25, *Fourier and Fourier-Stieltjes transforms on locally compact and other abelian groups*, https://mathscinet.ams.org/msc/msc2020.html?t=43A07.
