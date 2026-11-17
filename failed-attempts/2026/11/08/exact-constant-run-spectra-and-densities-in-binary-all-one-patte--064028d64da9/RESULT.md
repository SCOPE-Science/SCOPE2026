# Exact constant-run spectra and densities in binary all-one-pattern parity words

## Finding

For each integer \(d\ge 2\), let \(f_d(n)\in\{0,1\}\) be the parity of the number of possibly overlapping occurrences of \(1^d\) in the ordinary binary expansion of \(n\ge0\). A *constant-letter run* is a maximal interval of successive indices carrying the same value of \(f_d\); the first run starts at index zero. This is distinct from a periodicity run of arbitrary period.

Set \(M=2^d\). The complete set of lengths of constant-letter runs is
\[
\mathcal L_d=\{2^j:0\le j\le d-2\}\ \cup\
\{M-2^j:1\le j\le d-1\}\ \cup\
\{M-1,M/2+1,M\}.
\]
In particular, the longest run has length exactly \(M\). For \(d=2\), the entries \(M-1\) and \(M/2+1\) coincide, but are counted as one distinct length.

For an integer \(\ell\ge1\), let \(C_d(\ell;N)\) be the number of starting positions \(i<N\) of maximal constant-letter runs of length \(\ell\). Every density
\[
\lambda_d(\ell)=\lim_{N\to\infty}\frac{C_d(\ell;N)}{N}
\]
exists, and is given by the following additive indicator formula (a repeated length receives the sum of all applicable contributions):
\[
\begin{aligned}
\lambda_d(\ell)={}&\left(\frac7{6M}-\frac2{3M^2}\right)[\ell=1]\\
&+\sum_{j=1}^{d-2}\frac{[\ell=2^j]}{M2^{j+1}}
+\sum_{j=1}^{d-1}\frac{[\ell=M-2^j]}{M2^{j+1}}\\
&+\frac{1+2/M}{6M}[\ell=M-1]
+\frac1{M^2}[\ell=M/2+1]
+\frac{2-2/M}{6M}[\ell=M].
\end{aligned}
\]
Here \([P]\) is one or zero according as \(P\) is true or false. Consequently, the total run-start density is
\[
\rho_d=\sum_{\ell\ge1}\lambda_d(\ell)
=\frac{8(M-1)}{3M^2},
\]
and the limiting relative frequency *among runs*, as opposed to per index, is \(\lambda_d(\ell)/\rho_d\). The sum of length-weighted start densities is one.

There is also an exact non-asymptotic rule for every transition position, hence for the complete run decomposition. For \(k\ge0\), in the open interval \((kM,(k+1)M)\), changes occur precisely at
\[
(k+1)M-2^j,\qquad 0\le j\le\min\{d-1,\nu_2(k+1)\}.
\]
At the boundary \(kM\), for \(k\ge1\), a change occurs precisely when
\[
[\nu_2(k)\text{ is even}]\ \mathbin{\oplus}\
[\nu_2(\operatorname{odd}(k)+1)\ge d]=1,
\]
where \(\operatorname{odd}(k)=k/2^{\nu_2(k)}\), and \(\oplus\) means exclusive or.

## Assumptions and scope

All integers \(d\ge2\) are covered, including the classical Rudin–Shapiro case \(d=2\). Binary representations of positive integers have no leading zeros; the expansion of zero is taken as \(0\). Counts of occurrences allow overlaps. Starting indices begin at zero. A run is maximal to both sides, except that the first run has only a right boundary. All density limits are natural densities over integer positions, not probabilities of independently sampled random words.

## Proof

**Transition lemma.** For an integer \(x\ge1\), put \(q=\nu_2(x)\), \(m=x/2^q\) (odd) and \(u=\nu_2(m+1)\). The transition indicator \(T_d(x)=[f_d(x-1)\ne f_d(x)]\) satisfies
\[
T_d(x)=\bigl((q-d+1)_+\bmod2\bigr)\ \mathbin{\oplus}\ [u\ge d],
\qquad t_+=\max\{t,0\}.
\]
Indeed, write \(m=2a+1\). The binary expansion of \(x-1=(m-1)2^q+(2^q-1)\) is the expansion of the even integer \(m-1\) followed by \(q\) ones. Because \(m-1\) ends in zero, this appends exactly \((q-d+1)_+\) occurrences of \(1^d\) without creating crossings. By contrast \(x=m2^q\) has the same number of occurrences as \(m\). Changing the final zero in \(m-1\) to a one creates one new \(1^d\) occurrence if and only if \(m\) ends with at least \(d\) ones, equivalently \(u\ge d\). Subtracting modulo two yields the formula, also when \(m=1\).

**All transition positions.** If \(q<d\), the first term of the lemma vanishes, so a transition occurs exactly when \(m\equiv-1\pmod{2^d}\). Expressing \(x=(k+1)M-2^q\) gives \(m=(k+1)2^{d-q}-1\), hence the condition is exactly \(\nu_2(k+1)\ge q\). This proves the displayed interior cluster formula. If \(x=kM\), then \(q=d+\nu_2(k)\) and \(m=\operatorname{odd}(k)\), giving precisely the boundary exclusive-or condition. There are no other transition positions. Each open block contains \((k+1)M-1\), so no infinite run exists. The first transition is at \(M-1\).

**Run lengths.** Write \(a_k=\min\{d-1,\nu_2(k+1)\}\). Interior transitions in block \(k\) are, in increasing order, \((k+1)M-2^{a_k},\ldots,(k+1)M-1\). Their successive spacings are \(2^{a_k-1},\ldots,2,1\). Every gap crossing from the last interior transition \(kM-1\) of block \(k-1\) to the next cluster is classified by the possible boundary change at \(kM\):

- For odd \(k\), put \(j=\nu_2(k+1)\ge1\). If \(j<d\), the boundary is a change, and the two successive gaps are \(1\) and \(M-2^j\). If \(j\ge d\), there is no boundary change, and the sole gap is \(M/2+1\).
- For even \(k\ge2\), the next cluster begins at \((k+1)M-1\). If the boundary is a change, the gaps are \(1\) and \(M-1\); otherwise the gap is \(M\).

Together with the initial run of length \(M-1\), these cases yield exactly \(\mathcal L_d\). Each displayed case occurs infinitely often by elementary congruence classes; the frequency computation below also proves positivity.

**Run frequencies.** We count complete run gaps per block and divide by \(M\). For any positive integer \(a\), the natural density of indices \(k\) with \(\nu_2(k+1)=j\) is \(2^{-j-1}\), and the density with \(\nu_2(k+1)\ge j\) is \(2^{-j}\). Consequently internal cluster gaps \(2^j\), \(0\le j\le d-2\), occur at density \(2^{-j-1}\) per block. For odd \(k\), the case \(\nu_2(k+1)=j\in\{1,\ldots,d-1\}\) has density \(2^{-j-1}\), and \(\nu_2(k+1)\ge d\) has density \(1/M\).

For even \(k\), put \(v=\nu_2(k)\ge1\) and \(a=\operatorname{odd}(k)\). The density of \(v\ge1\) odd is \(1/3\), and the density of \(v\ge2\) even is \(1/6\). Conditional on either valuation parity, the odd part \(a\) is equidistributed among odd residue classes modulo \(M\), so \([\nu_2(a+1)\ge d]\) has probability \(2/M\). Thus the density among all \(k\) of even boundary changes is
\[
E_d=\frac16(1-2/M)+\frac13(2/M)=\frac{1+2/M}{6},
\]
and of even boundary nonchanges is \(1/2-E_d=(2-2/M)/6\). These probabilities are ordinary natural densities, obtained from finite congruence classes plus convergent geometric tails.

The contributions are now: internal gaps of length \(2^j\) at rate \(1/2^{j+1}\) per block; odd-boundary cases of length \(M-2^j\) at rate \(1/2^{j+1}\); a length-one gap at every odd boundary with \(j<d\) and every changing even boundary; the exceptional \(M/2+1\) gap at odd boundaries with \(j\ge d\); and \(M-1\) or \(M\) at even boundaries according to the boundary indicator. Dividing by \(M\), then adding equal-length contributions, gives the stated formula. In particular the length-one rate per block is \(1/2+(1/2-1/M)+E_d=7/6-2/(3M)\). Summing all gap rates gives \(8(M-1)/(3M^2)\), and their length-weighted sum is one. Since only finitely many lengths occur and all relevant valuation events have natural densities, these block calculations also establish the claimed limits for arbitrary \(N\), not only dyadic cutoffs. This proves the theorem.

## Verification

The accompanying standalone script \(\texttt{run\_spectrum\_verifier.py}\) reconstructs the sequence by the digit recurrence, independently constructs transitions from the exact valuation rule, and compares every boundary before \(2^{18}\), for each \(d\in\{2,3,4,5,6,7,8\}\). It also compares the observed length spectrum and finite-count discrepancies with the rational-density formula. The verifier is finite diagnostic evidence and is not substituted for any infinite argument in the proof.

For illustration, when \(d=3\), the support is \(\{1,2,4,5,6,7,8\}\), the run-start density is \(7/24\), and the largest run is eight. When \(d=2\), the support is \(\{1,2,3,4\}\), with start-density \(1/2\).

## Relationship to prior work

The pattern words \(f_d\) and their square-indexed subsequences are studied by Sun and Winterhof (2019). Their maximum-order-complexity results do not determine consecutive equal-symbol run lengths or their densities. Sobolewski (first public 2022) gives a general upper bound for monochromatic arithmetic progressions in binary pattern words. Taking progression step one in his Theorem 1.7 implies the upper bound \(2^d\) on the length of constant runs in \(f_d\); that upper bound is **not** presented as a novel standalone result here. What is added is the precise transition-position description, the full run-length spectrum, proof of sharpness simultaneously for all \(d\), and the rational densities for every permitted length.

Jugé and Marcovici (2022; extended 2024) analyze correlations of block-additive automatic sequences with primary MSC 68R15. Their correlation classifications and algorithms do not provide this run-length-frequency law. Marcovici, Stoll, and Tahay (2020) treat order-two discrete correlations of rank-two generalized Rudin–Shapiro words, a different statistic and, for \(d>2\), a different rank. Allouche and Bousquet-Mélou (1994) study paperfolding-derived generalized Rudin–Shapiro factor languages and powers, not this all-ones-pattern run distribution.

## Limitations

The result concerns *constant-letter* runs only, not maximal repetitions of arbitrary periods. It does not give separate frequencies for zero-runs versus one-runs, and does not classify all finite factors. Published-literature indexing may omit an equivalent source; the cited comparisons support a best-knowledge originality judgment rather than absolute novelty certification. Independent external audit has not been performed. The computational tests cover only finite dyadic prefixes; infinite correctness rests on the explicit proof above.

## References

1. V. Jugé and I. Marcovici, “Finding automatic sequences with few correlations,” *Pure Mathematics and Applications* 30(1) (2022), 75–81, DOI: https://doi.org/10.2478/puma-2022-0012 (public 2022-06-18; first-listed MSC 68R15). Extended treatment: *RAIRO Theoretical Informatics and Applications* 58 (2024), article 10, DOI: https://doi.org/10.1051/ita/2024008.
2. B. Sobolewski, “On monochromatic arithmetic progressions in binary words associated with pattern sequences,” arXiv:2204.05287 (first posted 2022-04-11), in particular Theorem 1.7: https://arxiv.org/abs/2204.05287.
3. Z. Sun and A. Winterhof, “On the maximum order complexity of subsequences of the Thue-Morse and Rudin-Shapiro sequence along squares,” arXiv:1910.13763 (first posted 2019-10-30): https://arxiv.org/abs/1910.13763.
4. I. Marcovici, T. Stoll and P.-A. Tahay, “Discrete correlations of order 2 of generalised Rudin–Shapiro sequences: a combinatorial approach,” arXiv:2006.13162 (first posted 2020-06-23): https://arxiv.org/abs/2006.13162.
5. J.-P. Allouche and M. Bousquet-Mélou, “Facteurs des suites de Rudin-Shapiro généralisées,” *Bulletin of the Belgian Mathematical Society* 1 (1994), 145–164: https://www.emis.de/journals/BBMS/Bulletin/bul942/ALLBOU.PDF.
