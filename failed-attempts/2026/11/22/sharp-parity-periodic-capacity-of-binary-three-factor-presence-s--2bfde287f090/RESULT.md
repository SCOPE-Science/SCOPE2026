# Sharp parity-periodic capacity of binary three-factor presence spectra

## Finding
For a binary word \(w=w_1\cdots w_n\) of length \(n\ge3\), let \(F_3(w)\) be the **set** of distinct contiguous length-three factors of \(w\), with neither positions nor multiplicities retained. Let
\[
R_n=\bigl|\{F_3(w):w\in\{0,1\}^n\}\bigr|.
\]
Then
\[
(R_3,R_4,R_5,R_6,R_7,R_8,R_9)=(8,15,27,48,72,94,100),
\]
and, for every integer \(n\ge10\),
\[
\boxed{R_n=102+(-1)^n
=\begin{cases}103,&n\text{ even},\\101,&n\text{ odd}.
\end{cases}}
\]
More strongly, the **sets of attainable factor-presence profiles** stabilize separately on even and odd lengths. The even-length profile collection (from length \(10\)) has precisely two members absent at every odd length \(n\ge11\):
\[
\{001,010,011,101\},\qquad \{010,100,101,110\}.
\]
These two profiles already occur at every even length \(n\ge6\). The other \(101\) eventual profiles occur at every length \(n\ge11\). The exact maximal size of a binary length-\(n\) codebook whose members are distinguished solely by presence/absence queries for the eight possible contiguous triples is \(R_n\).

## Assumptions and scope
Words are linear, not circular. A factor must occupy three consecutive positions; the empty set never occurs at \(n\ge3\). A binary three-factor profile records exactly which of the eight possible triples occur at least once, and does **not** retain their counts, order of occurrence, or the endpoint bits. All source words have known common length. The theorem covers every \(n\ge3\) and claims no analogue for larger alphabets, different factor lengths, or noisy readouts.

## Proof
**1. Exact finite-state recurrence.** Encode each two-bit suffix by \(s\in\{0,1,2,3\}\) and the factor-presence set by an eight-bit mask \(m\in\{0,\ldots,255\}\), whose bit \(e\) denotes the triple with binary value \(e\). Let \(E_n\) be the set of all attainable ordered pairs \((s,m)\) from length-\(n\) words. At length two,
\[
E_2=\{(0,0),(1,0),(2,0),(3,0)\}.
\]
For \(n\ge2\), a word with final suffix \(s\) can be extended by a bit \(b\in\{0,1\}\). This creates exactly one new triple of index \(e=2s+b\), leaves previous triples present, and changes the last-two-bit state to \(e\bmod4\). Consequently the **exact set recurrence** is
\[
E_{n+1}=\bigcup_{(s,m)\in E_n}\bigcup_{b\in\{0,1\}}
\{((2s+b)\bmod4,\ m\mathbin{\mathrm{OR}}2^{2s+b})\}.
\]
Every word has one length-\(n\) prefix and one appended bit, and every transition corresponds to a word; hence this recurrence has no spurious or omitted profiles. Let \(P(E)=\{m:(s,m)\in E\}\). Then \(R_n=|P(E_n)|\).

**2. A finite, independently reproducible certificate.** Applying this recurrence over a universe of at most \(4\cdot256=1024\) states gives the initial values listed in the Finding. The complete finite computation establishes the exact set equality
\[
E_{11}=E_{17},\qquad |E_{11}|=196,
\]
and the support sizes
\[
(|P(E_{11})|,\ldots,|P(E_{16})|)=(101,103,101,103,101,103).
\]
Since the state-set update is a single deterministic map \(T\), equality \(E_{11}=E_{17}\) implies by induction
\[
E_{11+j}=E_{17+j}\quad\text{for every integer }j\ge0.
\]
Thus the six computed consecutive lengths cover **every** later length. Their counts alternate by parity, establishing the all-length formula; this is a finite-state induction, not an extrapolation from sample values. The packaged standard-library `verify.py` reconstructs all these sets, checks the equality of the full sets of pairs rather than merely matching cardinalities, and independently enumerates the actual binary words at lengths \(3\) through \(15\). The state computation also verifies \(P(E_{10})=P(E_{12})\), the three odd-length profile collections at lengths \(11,13,15\) are equal, the three even-length collections at \(12,14,16\) are equal, and
\[
P(E_{10})\setminus P(E_{11})=\{46,116\}.
\]
Both masks decode to the two indicated factor sets.

**3. Structural reason for the two parity exceptions.** For the profile \(\{001,010,011,101\}\), the directed two-bit-suffix graph has a forced entry edge \(00\to01\) labeled `001`, a forced exit \(01\to11\) labeled `011`, and exactly the two internal transitions \(01\to10\to01\) labeled `010`, `101`. A walk using all four edges must enter once, traverse the internal two-cycle a positive number of times, and exit once. It therefore has \(2+2t\) edges for some integer \(t\ge1\), hence yields precisely even word lengths \(4+2t\ge6\). The second profile \(\{010,100,101,110\}\) is the bitwise-complement image and obeys the same condition. The finite-state certificate proves that these are the **only** persistent parity exceptions; the graph argument independently explains why they cannot be realized at odd lengths.

**4. Capacity interpretation and sharp onset.** Words sharing the same profile are indistinguishable under the eight binary three-factor membership tests. At most one word from each profile can be placed in a zero-error codebook, while selecting one representative of each attainable profile reaches this bound. Therefore the optimal codebook size is precisely \(R_n\). The values \(R_8=94\), \(R_9=100\), \(R_{10}=103\), and \(R_{11}=101\) establish the sharp eventual parity-stabilization onset.

## Verification
Run `python3 verify.py` under Python 3 with only the standard library. The verifier prints the initial counts, checks \(E_{11}=E_{17}\) as exact finite sets of suffix/profile pairs, compares the two eventual profile collections, checks the two exceptional bitmasks, and separately performs exhaustive direct word enumeration for every length from \(3\) through \(15\). Its passing output is:

```
CERTIFIED: R(3..11)=8,15,27,48,72,94,100,103,101
CERTIFIED: from n=10, 103 even and 101 odd support spectra
CERTIFIED: E(11)=E(17), 196 ordered (state,mask) pairs
CERTIFIED: only-even support bitmasks 46 (0x2e) and 116 (0x74)
CERTIFIED: independent exhaustive direct words n=3..15
```

## Relationship to prior work
Bernardini and coauthors (2022) formalize equality of length-\(k\) **sets** of factors and derive shortest-realization/listing algorithms through de Bruijn graph walks. This establishes the natural reconstruction model but does not state the exact all-length number of realizable linear binary length-three factor sets or their parity split. A previously published binary-three-factor result (2026) studies **the largest inverse-fiber population** of precisely this observation and develops the same finite suffix/mask transition method; it even provides finite-length profile-population tables through length \(50\). The present all-length claim is **not** an additional finite table or the earlier modal-fiber statement: it is the exact eventual **support-codebook capacity**, with equality of full state sets yielding an infinite-length period theorem and identifying the two exceptional support profiles. Those earlier computations supply substantial partial coverage and make priority qualification necessary; nothing here claims novelty for the elementary dynamic recurrence itself. Multiplicity-preserving three-gram multispectra and circular factor spectra use different observation operators and have different capacity questions.

## Limitations
The concrete numerical classification of the finite state universe uses a reproducible exhaustive computer calculation, while the infinite-length extension is a mathematical induction from the verified exact equality of finite state sets. The calculation has only \(1024\) possible states and is not an unrestricted word enumeration. The claim concerns output profiles, not their preimage populations; no noise model, larger fixed factor length, or source-distribution bound is addressed. Closely related published finite tables imply many of the small-length values, and it remains possible that another published algorithmic corollary or unindexed paper already states the eventual parity-periodic count. Independent validation has not been performed.

## References
1. G. Bernardini, A. Conte, E. Gabory, R. Grossi, G. Loukides, S. P. Pissis, G. Punzi and M. Sweering, *On Strings Having the Same Length-\(k\) Substrings*, Combinatorial Pattern Matching (CPM), 2022, DOI: 10.4230/LIPIcs.CPM.2022.16, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2022.16 (first verified public record 2022-06-01: https://ir.cwi.nl/pub/31869).
2. *The sharp full-support threshold for binary three-factor spectra*, publicly indexed mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-sharp-full-support-threshold-for-binary-three-factor-spectra--e450d182bc9b .
3. *Exact finite-length capacity of the linear binary three-gram spectrum*, publicly indexed mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-finite-length-capacity-of-the-linear-binary-three-gram-spe--bcc1ebef8280 .
