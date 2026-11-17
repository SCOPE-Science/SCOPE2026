# Singleton cyclic binary trigram spectra: a run rigidity theorem and a rational census

## Finding

For a nonempty binary circular word \(w\) of length \(n\), let \(C_{abc}(w)\), for \(a,b,c\in\{0,1\}\), count cyclic occurrences of the labeled length-three block \(abc\). Indices are read modulo \(n\), even when \(n<3\). Two circular words are identified only under rotation, never under reversal or bit complementation. Call the eight-component vector \(\mathbf C_3(w)=(C_{000},\ldots,C_{111})\) a *singleton spectrum* if exactly one circular word has that vector.

**Structural theorem.** Monochromatic circular words and words having exactly one run of each bit have singleton spectra. Every other nonmonochromatic circular word has a unique run representation, up to cyclic permutation of its \(r\ge2\) paired runs,
\[
[0^{a_1}1^{b_1}\cdots0^{a_r}1^{b_r}],\qquad a_i,b_i\ge1.
\]
For a vector \((a_1,\ldots,a_r)\), define the following mutually exclusive types:

- **U (uniform):** all entries are \(1\), or all entries are \(2\).
- **D (one distinguished run):** exactly one entry is at least \(2\) and all others are \(1\); or, when \(r\ge3\), exactly one entry is \(1\) and all others are \(2\); or exactly one entry is \(3\) and all others are \(2\).
- **X:** every remaining vector.

Then \(\mathbf C_3(w)\) is singleton **if and only if** its two run-length vectors have type \((\mathrm U,\mathrm U)\), \((\mathrm U,\mathrm D)\), or \((\mathrm D,\mathrm U)\). In particular, two distinguished run-length vectors, however individually simple, give at least two nonrotational reconstructions.

**Exact census.** Let \(s_n\) count singleton spectra of length \(n\), with \(n\ge1\). Put
\[
U_r(z)=z^r+z^{2r},\qquad
D_r(z)=\frac{z^{r+1}}{1-z}+z^{2r+1}+\mathbf1_{\{r\ge3\}}z^{2r-1}\qquad (r\ge2).
\]
Then the ordinary generating function is
\[
\begin{aligned}
S(z)=\sum_{n\ge1}s_nz^n
&=\frac{2z}{1-z}+\frac{z^2}{(1-z)^2}
+\sum_{r\ge2}\left(U_r(z)^2+2U_r(z)D_r(z)\right)\\
&=\frac{P(z)}{(1-z^3)(1-z^4)},
\end{aligned}
\]
where
\[
\begin{aligned}
P(z)={}&2z+3z^2+4z^3+4z^4+3z^5+5z^6+6z^7+7z^8+5z^9\\
&{}-z^{11}-4z^{12}-2z^{14}.
\end{aligned}
\]
The sequence begins, for \(n=1,2,\ldots,19\),
\[
2,3,4,6,8,12,16,19,22,24,28,29,34,34,38,41,44,44,50.
\]
In particular, \(s_n=\frac83n+O(1)\), with a bounded ultimately periodic fluctuation of period dividing \(12\). All statements are exact for every indicated length, including periodic circular words.

## Assumptions and scope

The alphabet is the two labeled symbols \(0\) and \(1\). Every circular occurrence starting at any position contributes separately to the trigram frequency, irrespective of repeated phases. A *run* is a maximal cyclic constant block, so a nonmonochromatic binary circle has equally many zero-runs and one-runs. The tuple of paired lengths is unique up to simultaneous cyclic shift of the pairs. All uniqueness statements are relative to **all** binary circles of the same length, not to a restricted codebook and not to edge-distinguishable Euler tours.

## Proof

**1. The spectrum fixes independent run statistics.** For a nonmonochromatic word with \(r\) zero-runs of lengths \(a_i\) and \(r\) one-runs of lengths \(b_i\), direct inspection at run boundaries yields
\[
\begin{array}{lll}
C_{101}=\#\{i:a_i=1\},& C_{001}=C_{100}=\#\{i:a_i\ge2\},&C_{000}=\sum_i(a_i-2)_+,\\
C_{010}=\#\{i:b_i=1\},& C_{011}=C_{110}=\#\{i:b_i\ge2\},&C_{111}=\sum_i(b_i-2)_+.
\end{array}
\]
Here \((t)_+=\max(t,0)\). Thus \(r=C_{101}+C_{001}=C_{010}+C_{011}\). For each symbol the spectrum fixes separately \(r\), the number \(s\) of singleton runs, and the total excess \(T=\sum_i(a_i-2)_+\) or its one-run analogue. It fixes **no pairing or cyclic ordering** of the two run-length vectors. Conversely, any two such length vectors with these statistics, interleaved in alternating order, have the same full eight-component trigram spectrum.

**2. Single-symbol rotation lemma.** Fix \(r\ge2\), \(0\le s\le r\) and \(T\ge0\). Let \(m=r-s\). If \(m=0\), realizability forces \(T=0\) and the only vector is all ones. If \(m>0\), the number \(M_r(s,T)\) of ordered length vectors with the prescribed statistics is
\[
M_r(s,T)=\binom rs\binom{T+m-1}{m-1},
\]
because we select the singleton positions and distribute \(T\) excess units among \(m\) runs of baseline length \(2\). As an integer, this is either \(1\), \(r\), or greater than \(r\). Its value is \(1\) exactly for the two U cases, and is \(r\) exactly for the D cases in the theorem. To check exhaustiveness: if \(s=0\), \(T=0,1,\ge2\) give respectively \(1,r,>r\); if \(s=r\), there is only the all-one vector; if \(0<s<r\), the binomial \(\binom rs\) exceeds \(r\) whenever \(2\le s\le r-2\). For \(s=r-1\), the count is \(r\) for every \(T\). For \(s=1<r-1\), the count is \(r\) only for \(T=0\), and is larger when \(T>0\). The case \(r=2,s=1\) is covered by \(s=r-1\). In every D case, the \(r\) vectors are precisely the rotations of one vector having a single distinguished coordinate.

**3. Coupled necklaces.** Let \(M_0,M_1\) be the independently available ordered zero-run and one-run vectors. Their Cartesian product parametrizes all run-pair tuples with the fixed spectrum. The cyclic group of order \(r\) rotates both length vectors simultaneously; its orbits are precisely the distinct binary circular words with that spectrum. Every orbit has size at most \(r\). If either factor has more than \(r\) vectors, or both have \(r\), the product has more than \(r\) elements and hence has at least two orbits. If both factors are U, the product is a singleton. If one is U and the other D, all \(r\) tuples are related by the common rotation. This proves the stated necessary and sufficient classification for \(r\ge2\). For \(r=1\) the unique word is \([0^a1^b]\) for the given run totals; monochromatic words are likewise unique.

**4. Counting.** The \(2\) monochromatic words at each length and the \(n-1\) possible choices \(a,b\ge1\), \(a+b=n\), contribute \(2z/(1-z)+z^2/(1-z)^2\). For fixed \(r\ge2\), U profiles have run-total generating polynomial \(U_r\). The three disjoint D classes have totals \(r-1+h\) for \(h\ge2\), \(2r-1\) when \(r\ge3\), and \(2r+1\), respectively; hence \(D_r\) as given. Since a singleton consists of U/U, U/D, or D/U, its contribution is \(U_r^2+2U_rD_r\). Geometric-series summation gives the displayed rational function. Multiplying the resulting expression by \((1-z^3)(1-z^4)\) produces the explicitly written \(P(z)\). Because \(P(1)=32\), the only double pole of \(S\) on the unit circle is at \(z=1\), with coefficient \(32/(3\cdot4)=8/3\); all other poles on that circle are simple roots of unity of orders dividing \(3\) or \(4\). Therefore \(s_n=(8/3)n+O(1)\), with bounded eventual period dividing \(12\).

## Verification

Execute `python3 verify.py` using only the Python standard library. It enumerates all \(2^{20}-2=1{,}048{,}574\) nonempty binary linear words of lengths \(1\) through \(19\), filters them into \(58{,}833\) rotation classes, constructs each trigram profile directly from cyclic indices, and independently checks the singleton status against the run-rigidity criterion for every class. It also compares the spectrum census with the generating-function coefficient formula at all those lengths and verifies the rational-coefficient recurrence through degree \(120\). The resulting terminal line is `PASS: 1048574 linear binary words examined, 58833 necklaces; n=1..19 classification and counts, 120 rational coefficients; exact formal rational identity.` The finite checks corroborate, but do not replace, the preceding infinite proof.

## Relationship to prior work

Ota and Manada (first publicly available September 5, 2023) give a general binary circular reconstruction condition and an automaton procedure employing minimal absent factors, assuming an aperiodic input of the stated length. Their framework addresses whether reconstruction succeeds, but its examined main theorems do not give this run-vector U/D/X classification, a singleton three-spectrum census, or the exact rational generating function; the present result also explicitly includes periodic words. Acosta and Tomescu (2022) give a linear-time uniqueness test for **edge-distinguishable** Eulerian circuits, for which parallel edges already destroy Euler-circuit uniqueness; a repeated trigram edge here is indistinguishable from another occurrence of the same trigram, so this is a different quotient. Gabrys and Milenkovic (2018) construct high-rate codebooks for reconstruction from linear substring multispectra with read length growing with block length, not the unrestricted cyclic length-three singleton enumeration. All these relationships concern precise implications, not merely differences in title or notation.

## Limitations

The classification and count are for binary **cyclic** labeled three-gram frequencies, not linear spectra, higher alphabets, longer windows, composition-only or noisy observations. It counts singleton spectra, not all spectra (a distinct invariant). A literature search and primary-text comparisons do not prove historical priority; an equivalent formula in unindexed or differently formulated literature remains a risk. No independent scientific audit is represented by this result.

## References

1. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548, first submitted 2018-04-12. https://arxiv.org/html/1804.04548v2
2. N. O. Acosta and A. I. Tomescu, *Simplicity in Eulerian Circuits: Uniqueness and Safety*, arXiv:2208.08522, first submitted 2022-08-17. https://arxiv.org/abs/2208.08522
3. T. Ota and A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, first public advance posting 2023-09-05, journal version *IEICE Transactions* E107.A (2024), 409–416, DOI:10.1587/transfun.2023TAP0015. https://www.jstage.jst.go.jp/article/transfun/E107.A/3/E107.A_2023TAP0015/_pdf/-char/en
