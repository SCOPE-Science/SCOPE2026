# Complete one-insertion sphere spectrum of ternary short-tandem-irreducible words

## Finding

Let \(\mathcal I_n\) consist of the words \(w=w_1\cdots w_n\in\{0,1,2\}^n\) with no contiguous factor of either form \(aa\) or \(abab\). Here a factor \(abab\) may have \(a\ne b\); equal adjacent symbols are already excluded. Define \(d(w)\) to be the number of *distinct* words in \(\mathcal I_{n+1}\) obtainable from \(w\) by inserting one symbol at one of the \(n+1\) gaps. For every \(n\ge3\), put \(m=n-1\) and \(A_{n,j}=\#\{w\in\mathcal I_n:d(w)=j\}\). Define

\[
B(z,u)=\frac{z}{1-zu},\qquad
I(z,u)=z^2+z^3u^2+\frac{z^4u^2}{1-zu}.
\]

The complete bivariate insertion-sphere spectrum is the rational formal-power-series identity

\[
\boxed{\sum_{n\ge3}\sum_{j\ge0}A_{n,j}z^{n-1}u^j=6u^4\left(\frac{z^2u^2}{1-zu}+\frac{B(z,u)^2}{1-I(z,u)}\right).}
\]

The complete degree support is

\[
\{j:A_{n,j}>0\}=\begin{cases}
\{4\}\cup\{6,7,\ldots,m+2\}\cup\{m+4\},&m\text{ even},\\
\{5,6,\ldots,m+2\}\cup\{m+4\},&m\text{ odd}.
\end{cases}
\]

Ranges with reversed bounds are empty. In particular the next-to-largest value \(n+2=m+3\) never occurs, and if \(n\) is odd then the value five is also missing. The smallest degree is four if \(n\) is odd (exactly six words) and five if \(n\) is even (exactly twelve words); the largest is \(n+3\) (exactly six words). Those six maximizers have all successive alphabet differences equal, so are the six words obtained by choosing a starting symbol and one of the two period-three directions.

## Assumptions and scope

All words are linear and labeled, not cyclic or identified under relabeling. The alphabet is exactly \(\mathbb Z/3\mathbb Z\). The prohibited tandem squares have half-length one or two only; longer squares are allowed. Each insertion must leave the resulting word in the same avoidance language. The count is of distinct destination strings, not of edit scripts. The theorem applies to every integer \(n\ge3\), with no asymptotic or computational cutoff.

## Proof

Write \(s_i=w_{i+1}-w_i\pmod3\) and encode its nonzero value as \(+\) for one and \(-\) for two. The lack of \(aa\) is exactly the condition that every difference is \(\pm\). The absence of \(abab\) is exactly the absence of alternating sign triples \(+-+\) and \(-+-\): such a triple is equivalent to \(w_i=w_{i+2}\) and \(w_{i+1}=w_{i+3}\). Consequently each of the two sign types determines exactly three words (one for each initial letter), and in every valid sign string each internal sign-run has length at least two; its initial and terminal runs may have length one.

Let the run lengths of a valid sign string of length \(m\) be \(\ell_1,\ldots,\ell_r\). Inserting a symbol between two original letters whose difference is \(s_i\) must use the unique third alphabet symbol; in sign notation this replaces \(s_i\) by \((-s_i,-s_i)\). A new alternating triple can therefore arise only immediately before or after this doubled pair. The replacement is forbidden exactly if the selected sign is second in a noninitial run or penultimate in a nonterminal run. For a run internal to the sign string, the two forbidden positions are distinct except when its length is three, in which case they coincide. If the run is initial, it has one forbidden internal replacement when its length is at least two; otherwise the left-end insertion loses exactly one of its two symbol choices. The terminal run similarly contributes exactly one forbidden possibility at the right. Each internal run contributes two forbidden positions, except a length-three internal run contributes one.

There are \(m\) candidate internal insertions (one per original difference) and four candidate end insertions (two at each end). If \(r=1\), all \(m+4\) choices are permitted. If \(r\ge2\), let \(t_3\) count internal runs of length three. Then exactly \(2+2(r-2)-t_3\) candidates are forbidden, hence

\[
\boxed{d(w)=\begin{cases}m+4,&r=1,\\m+6-2r+t_3,&r\ge2.\end{cases}}
\]

Different permitted insertions produce different output words: if two deletions at distinct positions in a putative output yielded the same source, all characters between these positions would have to coincide, giving adjacent equal symbols, impossible for an output in \(\mathcal I_{n+1}\). Thus the counted choices equal the sphere cardinality.

For \(r\ge2\), the two boundary runs have lengths at least one. Their contributions to \(d(w)-4\) are respectively \(\ell_1-1\) and \(\ell_r-1\). Every internal run has length \(L\ge2\) and contributes \(L-2+\mathbf1_{\{L=3\}}\). Consequently the generating series for each boundary run is \(B(z,u)\) and that for each internal run is \(I(z,u)\). Summing over zero or more internal runs gives \(B^2/(1-I)\); one-run sign strings contribute \(z^2u^2/(1-zu)\). Each run-length composition has two possible initial signs and three initial letters. Including the baseline degree four proves the displayed generating function.

For the support, put \(e=d(w)-4\). Among words with at least two runs, every degree has \(e=\ell_1-1+\ell_r-1+\sum_{k=2}^{r-1}(\ell_k-2+\mathbf1_{\{\ell_k=3\}})\). An interior run has length at least two, so a zero excess requires both boundary lengths to be one and all interior lengths to be two. This is possible if and only if \(m\) is even and gives exactly two sign choices times three initial-letter choices, or six words. Excess one requires exactly one boundary run to have length two, again with all interior lengths two; it is possible only for odd \(m\), and gives twelve words. Therefore the sharp minima have the claimed parity and multiplicities.

For all other degrees, take all interior runs of length two and allocate any excess to the first boundary run. This realizes \(e=m-2r+2\), for every \(r\ge2\) satisfying the length constraints: all even \(e\) from zero to \(m-2\) when \(m\) is even, and all odd \(e\) from one to \(m-2\) when \(m\) is odd. To realize the opposite parity, use exactly one internal run of length three, all others of length two, and allocate remaining excess to the first boundary run. This realizes \(e=m-2r+3\), with \(r\ge3\), giving all odd \(e\) from three through \(m-3\) when \(m\) is even, and all even \(e\) from two through \(m-3\) when \(m\) is odd. No other non-one-run degrees exceed \(m+2\) because every word with at least two runs loses at least two of the \(m+4\) insertion choices. One-run sign strings produce degree \(m+4\), with exactly six words. This proves the support, maximum, gap, and all stated extremal counts.

## Verification

The accompanying standalone file `verify_insertion.py` computes the degree spectrum in three separate ways: constructing actual eligible inserted output words, counting via binary sign runs, and expanding the proved run-composition generating function. All three agree, including every support value and extremal multiplicity, for all lengths \(3\le n\le12\). Direct finite verification checks examples and the implementation; the all-length conclusions follow from the preceding proof, not extrapolation.

For instance the coefficient lists are \((A_{5,4},A_{5,6},A_{5,8})=(6,18,6)\) and \((A_{6,5},A_{6,6},A_{6,7},A_{6,9})=(12,6,24,6)\).

## Relationship to prior work

Chee, Chrisnata, Kiah, and Nguyen (2018) derived the ordinary length enumerator and finite-state encoding for tandem-irreducible words, including this length-one-and-two avoidance language. Their total-language recurrence is the sum over all sphere sizes, not the insertion-degree distribution. Tang, Wang, Lou, Gabrys, and Farnoud (2022) consider irreducible root-based edit and tandem-duplication correction, using confusability bounds rather than this precise constrained one-insertion sphere. Mol and Rampersad (2020) and Dębski, Grytczuk, and Pawlik (2022) investigate insertion extension/extremality for words avoiding *all* square lengths; their claims neither quantify the truncated-square insertion degree nor give this rational two-variable enumerator. The complete spectrum here is not a corollary of those statements. Searches of published mathematical records for the same constrained insertion and run-spectrum invariants identified nearby but non-equivalent insertion-covering and profile-ball results.

## Limitations

This theorem covers only ternary words and tandem squares of half-length one or two. It does not count general edit balls or arbitrary tandem-duplication descendants, and does not solve optimal codebook packing/covering. Identical all-length spectra under a different encoding or earlier unindexed literature remain a possible historical-priority risk; no independent validation has been performed.

## References

1. Y. M. Chee, J. Chrisnata, H. M. Kiah, T. T. Nguyen, *Efficient Encoding/Decoding of Irreducible Words for Codes Correcting Tandem Duplications*, ISIT 2018, arXiv:1801.02310v1 (first public 2018-01-08), https://arxiv.org/abs/1801.02310.
2. L. Mol, N. Rampersad, *Lengths of extremal square-free ternary words*, arXiv:2001.11763v1 (first public 2020-01-31), https://arxiv.org/abs/2001.11763.
3. Y. Tang, S. Wang, H. Lou, R. Gabrys, F. Farnoud, *Low-redundancy codes for correcting multiple short-duplication and edit errors*, arXiv:2208.02330v1 (first public 2022-08-03), https://arxiv.org/abs/2208.02330.
4. M. Dębski, J. Grytczuk, B. Pawlik, *Extensions and reductions of square-free words*, arXiv:2209.08507v1 (first public 2022-09-18), https://arxiv.org/abs/2209.08507.
