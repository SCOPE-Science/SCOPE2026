# Quartic count of binary three-fragment composition observations

## Finding
For each integer \(n\geq 1\) and each binary word \(w=w_1\cdots w_n\), define \(C_{\leq 3}(w)\) to be the multiset of the compositions (numbers of zeros and ones) of **all contiguous linear factors** of lengths \(1\), \(2\), and \(3\) that do not exceed \(n\). Factors are counted with their multiplicities; the order of bits within a factor and the location of a factor are not observed. Let \(R_3(n)\) be the number of distinct such multisets as \(w\) ranges over \(\{0,1\}^n\).

The complete generating function is
\[
\boxed{\sum_{n\geq1}R_3(n)z^n=\frac{z(2-5z+6z^2-4z^3+4z^4-z^5+2z^6-3z^7+2z^8)}{(1-z)^4(1-z^4)}.}
\]
Equivalently, \(R_3(1)=2\), and for every integer \(n\geq2\),
\[
\boxed{R_3(n)=\frac{3n^4-16n^3+114n^2-272n+c_{n\bmod4}}{96}},
\qquad(c_0,c_1,c_2,c_3)=(480,555,456,555).
\]
The initial values are \(2,3,6,10,20,35,62,101,160,241,354,502\) for lengths \(1\) through \(12\). In particular \(R_3(n)\sim n^4/32\). Since one can select one representative from each observation class, \(R_3(n)\) is also the exact maximum size of a zero-error, length-\(n\) code for this observation channel.

## Assumptions and scope
The alphabet is labeled and binary, words are linear and not cyclic, substring multiplicities are retained, and all compositions from each available length \(1\) through \(3\) are observed without errors. For a word \(w\), write \(c_{k,j}(w)\) for the number of length-\(k\) factors containing exactly \(j\) ones, where \(k\in\{1,2,3\}\) and \(k\leq n\). The observed multiset is equivalently the family of these counts. The word length \(n\) is fixed.

For the structural proof, a *run* is a maximal nonempty block of equal symbols. Put \(a\) and \(b\) for the numbers of zeros and ones, \(p\) and \(q\) for the counts of zero-runs and one-runs, and \(e_0,e_1\) for the counts of runs of length exactly one of each symbol. The two constant words are handled separately. For a nonconstant word, \(p,q\geq1\) and \(|p-q|\leq1\).

## Proof
**Step 1: recover four run parameters.** Every zero-run of length \(L\) contributes \(L-1\) copies of \(00\); consequently \(c_{2,0}=a-p\). Similarly \(c_{2,2}=b-q\). A zero-run contributes \(\max\{L-2,0\}=L-2+\mathbf1_{\{L=1\}}\) copies of \(000\), whence \(c_{3,0}=a-2p+e_0\); similarly \(c_{3,3}=b-2q+e_1\). Thus the observation uniquely determines \((b,p,q,e_0,e_1)\) whenever the word is nonconstant. Only \(c_{3,1}\), the number of length-three factors with exactly one one, remains to distinguish different endpoint arrangements.

**Step 2: count possible boundary corrections.** Let \(h_0\) be the number of boundary zero-runs of length at least two, and \(t_1\) the number of boundary singleton one-runs. (For a nonconstant word the first and last runs are distinct.) Every long zero-run contributes two factors of type \(001\) or \(100\), except a boundary long zero-run contributes only one; every internal singleton one-run contributes one factor \(010\). Hence the exact identity
\[
c_{3,1}=2(p-e_0)-h_0+e_1-t_1.
\]
When \(p=q=m\geq1\), one boundary run is zero and the other one. The singleton status of the boundary zero-run is free precisely when \(0<e_0<m\), and similarly for the boundary one-run. Because the correction depends on their difference, the number of distinct attainable values of \(c_{3,1}\) is
\[
1+\mathbf1_{\{0<e_0<m\}}+\mathbf1_{\{0<e_1<m\}}.
\]
When \(p=q+1\geq2\), both boundary runs are zero. If exactly \(t\) of these are singleton runs, then \(0\leq t\leq2\), \(t\leq e_0\), and \(2-t\leq p-e_0\). The number of admissible integers \(t\), whose corrections are all distinct, is
\[
b(p,e_0)=1+\mathbf1_{\{1\leq e_0\leq p-2\}}+\mathbf1_{\{2\leq e_0\leq p-1\}}.
\]
The case \(q=p+1\geq2\) is the symbol-swapped analogue, with multiplier \(b(q,e_1)\). These boundary choices are all realizable: assign the prescribed singleton/long status to the boundary runs and permute the remaining run types in the interior. No further constraint couples the zero-run and one-run length allocations.

**Step 3: count symbol totals without overcounting.** For a fixed number \(r\geq1\) of runs of one symbol, of which \(e\) are singletons, the generating function for its attainable total number of letters is
\[
T_{r,e}(z)=\begin{cases}z^r,&e=r,\\z^{2r-e}/(1-z),&0\leq e<r.\end{cases}
\]
Indeed, when all runs are singletons the total length is forced, and otherwise any excess can be added to one long run. Every attainable symbol total contributes one observation, not the number of its run-length compositions. Different totals \(b\), run counts \(p,q\), singleton counts \(e_0,e_1\), and values of \(c_{3,1}\) give different observations by Step 1. Therefore ordinary multiplication of the two symbol-total generating functions is justified.

Define
\[
A_m(z)=\sum_{e=0}^{m}T_{m,e}(z),\qquad F_m(z)=\sum_{e=1}^{m-1}T_{m,e}(z),\qquad H_m(z)=\sum_{e=0}^{m}b(m,e)T_{m,e}(z)\quad(m\geq2).
\]
The constant words contribute \(2z/(1-z)\). Balanced run counts contribute \(A_m^2+2A_mF_m\); either imbalanced orientation contributes \(H_{m+1}A_m\). Consequently the exact formal generating-function identity is
\[
\sum_{n\geq1}R_3(n)z^n=\frac{2z}{1-z}+\sum_{m\geq1}\bigl(A_m(z)^2+2A_m(z)F_m(z)+2H_{m+1}(z)A_m(z)\bigr).
\]

**Step 4: sum geometric series.** Direct summation of the run-length contributions gives
\[
\begin{aligned}
A_m&=z^m+\frac{z^{m+1}-z^{2m+1}}{(1-z)^2},\\
F_m&=\frac{z^{m+1}-z^{2m}}{(1-z)^2},\\
H_{m+1}&=z^{m+1}+\frac{(2+z)z^{m+2}-(1+z)z^{2m+1}-z^{2m+3}}{(1-z)^2}.
\end{aligned}
\]
Substituting and summing the resulting terms in \(z^{2m}\), \(z^{3m}\), and \(z^{4m}\) for \(m\geq1\) yields, after cancellation, exactly the displayed rational function with denominator \((1-z)^4(1-z^4)\). Partial fractions (or expansion separately in the four residue classes modulo four) give the displayed quartic formula, with \(n=1\) separately equal to two. This proves all assertions for every positive integer \(n\).

## Verification
The standalone `direct_check.py` forms the literal multiplicity vectors of every contiguous substring composition for every binary word through length \(17\), and compares each distinct-vector count with the theorem. It prints `DIRECT_OK` after enumerating \(262142\) words in total. The independent `structural_check.py` counts possible run-parameter observations without enumerating words for all lengths through \(42\), checks the rational generating function's integral coefficient recurrence against the quartic formula through length \(80\), and prints `STRUCTURAL_OK`. Neither finite verification substitutes for the all-length run argument above.

Run both programs with a standard Python 3 interpreter from the directory containing the files:

```sh
python3 direct_check.py
python3 structural_check.py
```

## Relationship to prior work
Acharya, Das, Milenkovic, Orlitsky, and Pan study reconstruction from compositions of **all** substring lengths. Their full-multiset equivalence and polynomial-factorization analysis address a strictly richer observation; they do not furnish the fixed-three-length quotient enumerator here. Ye and Elishco introduce precisely the length-limited model \(C_{\leq r}\). Section VIII of their paper gives a code construction, especially for read length growing with blocklength, and their conclusion asks for constant-\(r\) capacity results; the exact value at \(r=3\) is not supplied there. Two published mathematical records establish exact binary read-length-two enumerations, which do not determine the three-length quartic enumerator: three-letter windows additionally record singleton interior runs and the boundary corrections of Step 2.

This result is therefore a natural first higher-order exact image-size calculation for the length-limited model rather than an instance of the full-spectrum reconstruction theorem or the read-length-two formulas. Independent priority verification against unindexed or unpublished work is still necessary.

## Limitations
The theorem treats binary **linear** words and exact noiseless compositions from lengths at most three. It does not give class-size distributions, a polynomial-time ranking algorithm for representative codewords, exact capacities for higher read lengths or alphabets, or bounds for noisy or cyclic observations. The claim of originality is best-knowledge, not a guarantee of historical priority. The scientific verification described here is not an independent external audit.

## References
1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439v1 (first public 2014-03-10); SIAM J. Discrete Math. 29(3), 1340–1371 (2015), DOI:10.1137/140962486, https://arxiv.org/abs/1403.2439.
2. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963v1 (2022), Section VIII, https://arxiv.org/abs/2208.14963.
3. *Exact binary \(r=2\) length-limited composition reconstruction*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-r-2-length-limited-composition-reconstruction--a98561a7f27e.
4. *Exact binary two-multispectrum code size and singleton classification*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71.
