# Sharp binary one-deletion trigram-profile capacity and its first attainment length

## Finding
For a binary linear word \(w\) and a binary triple \(v\), let \(c_v(w)\) denote the number of **overlapping contiguous** occurrences of \(v\). The trigram profile is the ordered vector \(P_3(w)=(c_{000}(w),c_{001}(w),\ldots,c_{111}(w))\). For every \(n\ge1\), define the one-deletion *profile-ball size*
\[
B_3(w)=\left|\left\{P_3(w_1\cdots w_{i-1}w_{i+1}\cdots w_n):1\le i\le n\right\}\right|,
\qquad M_3(n)=\max_{w\in\{0,1\}^n}B_3(w).
\]
Equal profiles are counted once even if they arise from different deletion positions or descendant words. For all lengths, the exact sharp spectrum is

| \(n\) | \(M_3(n)\) |
|---|---|
| 1, 2, 3 | 1 |
| 4, 5 | 4 |
| 6, 7 | 6 |
| 8 | 7 |
| 9, 10 | 8 |
| 11 | 9 |
| 12, 13, 14 | 10 |
| 15 | 11 |
| 16, 17, 18 | 12 |
| 19 | 13 |
| every \(n\ge20\) | **14** |

In particular, **fourteen** is the universal maximum, and **twenty** is the sharp first input length that attains it. An explicit extremal word of every length \(20+t\), \(t\ge0\), is
\[
w_t=\mathtt{01}\,\mathtt{0}^{\,t+3}\,\mathtt{100101011011101}.
\]

## Assumptions and scope
Strings are indexed, noncyclic, and binary. Exactly one symbol is removed; deletions of the first and last symbols are included. All overlapping triples of the shortened word contribute with multiplicities. For words shorter than three, \(P_3\) is the eight-coordinate zero vector. No reversal or complementation identification is performed. The claimed function concerns distinct *profiles* of deletion descendants, not distinct descendants and not the number of attainable profiles globally.

## Proof
Let \(e_{abc}\) denote the standard unit vector for triple \(abc\), with coordinates indexed \(000,001,\ldots,111\). For each deletion at index \(i\), subtract the fixed original profile from the new profile and call the resulting vector \(\Delta_i\). Subtracting one common vector preserves all equalities and inequalities among output profiles.

**Interior upper bound.** When \(3\le i\le n-2\), write the five consecutive symbols centered at the deletion as \(a,b,x,c,d\). Exactly three old triples disappear and two new triples appear, so
\[
\Delta_i=e_{abc}+e_{bcd}-e_{abx}-e_{bxc}-e_{xcd}.
\]
The following exhaustive table groups all 32 five-bit neighborhoods into their ten **distinct** change vectors. The eight coordinates below are in the stated lexicographic order; the second column is a representative five-bit neighborhood and the third is the number of neighborhoods of this vector.

| Representative | Count | Eight-coordinate change vector |
|---|---:|---|
| `00000` | 8 | \((-1,0,0,0,0,0,0,0)\) |
| `00111` | 8 | \((0,0,0,0,0,0,0,-1)\) |
| `00110` | 4 | \((0,0,1,-1,0,0,-1,0)\) |
| `01001` | 4 | \((0,-1,0,0,-1,1,0,0)\) |
| `00101` | 2 | \((1,0,-1,0,0,-1,0,0)\) |
| `01011` | 2 | \((0,0,-1,0,0,-1,0,1)\) |
| `00100` | 1 | \((2,-1,-1,0,-1,0,0,0)\) |
| `01010` | 1 | \((0,0,-2,1,0,-1,1,0)\) |
| `10101` | 1 | \((0,1,-1,0,1,-2,0,0)\) |
| `11011` | 1 | \((0,0,0,-1,0,-1,-1,2)\) |

All counts sum to 32, and all ten vectors differ. At most four other vectors arise from deletion indices \(1,2,n-1,n\). The first two depend only on the initial four bits and the last two only on the final four bits. Hence \(B_3(w)\le10+4=14\) for all \(n\ge5\); for shorter words the bound is immediate.

**Infinite sharpness family.** Every \(w_t\) starts with `0100` and ends with `1101`. Its two left-boundary deletion changes are respectively \((0,0,-1,0,0,0,0,0)\) and \((1,0,-1,0,-1,0,0,0)\). The two right-boundary changes are respectively \((0,0,0,0,0,-1,-1,1)\) and \((0,0,0,0,0,-1,0,0)\). These four are pairwise distinct and absent from the ten-vector table. Every \(w_t\) also contains the ten five-bit neighborhoods
`01000`, `00100`, `01001`, `00101`, `01010`, `10101`, `01011`, `10110`, `11011`, `10111`,
which realize all ten table rows. The first two neighborhoods persist at the two ends of the enlarged initial zero run; all others remain inside the unchanged suffix. Thus \(B_3(w_t)=14\) for every integer \(t\ge0\).

**Sharp first attainment and prethreshold values.** It remains to exclude a shorter word and establish the finite values in the table. This is a finite exhaustive proof using an explicitly specified finite-state recurrence, implemented in `verify_trigram_dp.py`. Let \(\varphi(u)\) be the interior change type of a five-bit word \(u\). For each initial four-bit word \(p\), a length-\(\ell\) state records \((s,T)\), where \(s\) is the final four bits and \(T\) is the set of \(\varphi\)-types of the length-five factors. Initialize with \((p,\varnothing)\) at \(\ell=4\); upon appending bit \(b\), update
\[
(s,T)\longmapsto\bigl(s_2s_3s_4b,\;T\cup\{\varphi(sb)\}\bigr).
\]
This recurrence enumerates **every** binary word up to equality of exactly those statistics relevant to \(B_3\); induction on \(\ell\) proves that no possible state is omitted. At each reachable state, \(B_3\) is the cardinality of \(T\) together with the two deletion-change vectors determined by \(p\) and two determined by \(s\). Keeping the exact sets, rather than only their sizes, is essential. Exhausting the sixteen possible \(p\), sixteen \(s\), and at most \(2^{10}\) type subsets through length 20 gives the displayed maxima, including \(M_3(19)=13\) and \(M_3(20)=14\). This is a fully finite certificate, not an extrapolation to infinity. The all-length argument follows separately from the universal upper bound and explicit family.

## Verification
`verify_trigram_dp.py` uses only Python's standard library, recomputes the 32 neighborhood changes directly from triple counts, performs the complete dynamic-state recurrence for every length four through twenty, and checks the displayed explicit family at lengths 20 through 44. Its saved output reports ten interior classes, upper bound fourteen, the finite maxima, and first attainment length twenty.

`independent_brute.cpp` uses a different procedure: for every binary word of each length one through nineteen it **literally deletes each symbol**, recounts all eight three-bit factors in every descendant, and maximizes the number of distinct output vectors. It does not invoke the ten-class construction. Compile with `g++ -O2 -std=c++17 independent_brute.cpp -o independent_brute` and execute `./independent_brute`. Its saved output confirms all finite maxima; it also checks the explicit infinite-family construction at lengths 20 through 30. The verification programs and text outputs are embedded alongside this manuscript. A finite check alone does not prove the infinite family; the preceding proof does.

## Relationship to prior work
Profile-vector reconstruction was formalized by Kiah, Puleo and Milenkovic, who analyze global profile counts, substitution errors, missing reads, and sequencing noise. Their statistic is the same overlapping \(k\)-gram count vector, but their results do not supply a one-*source-symbol*-deletion profile-ball maximum or its first attainment threshold. The earlier published binary dinucleotide-profile deletion work gives a **six-profile** maximum and first attainment length nine for **two**-grams, not this three-gram classification. Published binary three-gram spectrum enumeration counts *all realizable profiles across all words*, rather than the number of different profiles reachable from one word by one deletion, and its statements do not entail the present result. En Gad's September 2026 work develops deletion-code constructions using substring-count hashes, motivating the analysis of local changes. Its accessible abstracts do not state the bound fourteen or threshold twenty, but its full manuscript was not successfully inspected and remains a priority risk.

## Limitations
The result applies to full multiplicity-preserving **linear binary three-gram** profiles and exactly one source-symbol deletion. It does not determine the all-length distribution of profile-ball sizes, larger alphabets, other read lengths, insertion or multiple deletions, or code cardinalities. The shortest-length classification uses a small, exhaustive finite-state computation; no unchecked inference from limited numerical experiments is needed. The priority comparison is limited by incomplete access to one plausible 2026 full manuscript and by possible unindexed work. An independent scientific audit has not been performed.

## References
1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, first publicly posted 2026-09-16, arXiv:2609.19493v1, https://arxiv.org/abs/2609.19493.
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (2015), IEEE Trans. Inf. Theory 62 (2016), https://www3.ntu.edu.sg/home/hmkiah/docs/papers/DNASeqProfile.pdf.
3. *The complete one-deletion dinucleotide-profile ball distribution for binary words*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-complete-one-deletion-dinucleotide-profile-ball-distribution--294c530e44d7/RESULT.md.
4. *Exact enumeration of binary length-three substring multispectra*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-enumeration-of-binary-length-three-substring-multispectra--7044900c1ee8/RESULT.md.
