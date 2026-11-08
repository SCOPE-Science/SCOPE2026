# Complete three-factor language of infinite-alphabet \(k\)-Bonacci words

## Finding

Fix an integer \(k\geq 3\). Define the infinite-alphabet morphism \(\phi_k\) by
\[
\phi_k(ki+j)=
\begin{cases}
(ki)(ki+j+1),&0\le j\le k-2,\\
ki+k,&j=k-1,
\end{cases}
\]
where the right sides are words over \(\mathbb N\), not products of integers. Write \(W_n=\phi_k^n(0)\) and \(\mathbf W=\lim_{n\to\infty}W_n\). A triple \((a,b,c)\) denotes the contiguous factor with these three letters, and \(d\oplus(a,b,c)=(a+d,b+d,c+d)\).

For every integer \(j\ge1\), set
\[
t_k(j)=\begin{cases}
j-(j\bmod k),&j\not\equiv0\pmod k,\\
j-k+1,&j\equiv0\pmod k.
\end{cases}
\]
Define six explicit families of triples:
\[
\begin{aligned}
\mathcal A_0&=\{(0,1,0)\},\\
\mathcal A_1&=\{(1,0,j):2\le j\le k-1\},\\
\mathcal I_1&=\{(t_k(j),j,0):j\ge2\},\\
\mathcal I_2&=\{(j,0,1):j\ge2\},\\
\mathcal T_1&=\{(t_k(j),j,k):j\ge1\},\\
\mathcal T_2&=\{(j,k,k+1):j\ge2\}.
\end{aligned}
\]
Let \(\mathcal S_k\) be their union. Then **every length-three factor, and no other triple,** is given by
\[
\boxed{\operatorname{Fac}_3(\mathbf W)
=\bigcup_{h\ge0}\bigl(hk\oplus\mathcal S_k\bigr).}
\tag{1}
\]
The displayed union is a union of *sets*; different descriptions need not be disjoint. It is a complete explicit description of the length-three factor language for every \(k\ge3\).

There is also an exact finite-iterate description. Assign witness stages \(s\) to the six unshifted families: \((0,1,0)\) has stage \(2\); \((1,0,j)\) has stage \(j\); each of \((t_k(j),j,0)\) and \((j,0,1)\) has stage \(j+1\); and each terminal-boundary triple \((t_k(j),j,k)\) or \((j,k,k+1)\) has stage \(k+j-1\). If \(\mathcal P_k\) is the resulting collection of triple-stage pairs, then for every \(n\ge0\),
\[
\boxed{\operatorname{Fac}_3(W_n)
=\bigcup_{(B,s)\in\mathcal P_k}\ \bigcup_{\substack{h\ge0\\s+hk\le n}}\{hk\oplus B\}.}
\tag{2}
\]
The stages supply witnesses by the stated iterate; no claim that the displayed descriptions are unique is required. Formula (1) also admits a constant-number-of-cases membership test, by inspecting the residue of the last letter modulo \(k\); see the proof.

## Assumptions and scope

The alphabet consists of nonnegative integers. Every factor is contiguous; factors may overlap; the empty word is excluded. The formulas describe the set of distinct length-three words, not their occurrence multiplicities. The parameter \(k\) may be any integer at least three, and the iterate index \(n\) is any nonnegative integer. No finite-alphabet projection or identification of symbols modulo \(k\) is made.

## Proof

**1. Word decomposition and suffixes.** The established block decomposition for these words is
\[
W_0=0,\quad
W_n=W_{n-1}W_{n-2}\cdots W_0\,n\quad(1\le n<k),
\]
\[
W_n=W_{n-1}W_{n-2}\cdots W_{n-k+1}\,\bigl(k\oplus W_{n-k}\bigr)
\quad(n\ge k).
\tag{3}
\]
Each \(W_j\) is a prefix of \(W_{j+1}\). Each \(W_j\), for \(j\ge1\), begins with the two symbols \((0,1)\) and ends with the two symbols \((t_k(j),j)\). Indeed, the final symbol is \(j\). For \(1\le j<k\), the final two symbols are \((0,j)\); for \(j=k\), they are \((1,k)\). For \(j>k\), the last block of (3) has at least two letters, so its final two symbols are obtained by adding \(k\) to the final two symbols of \(W_{j-k}\). These cases establish the stated formula for \(t_k\) by induction.

**2. Initial iterates.** For \(2\le n<k\), the decomposition in (3) creates the terminal triple \((1,0,n)\) across \(W_1\mid W_0\mid n\), and \((0,1,0)\) across \(W_1\mid W_0\). For each ordinary internal boundary \(W_j\mid W_{j-1}\), where \(j\ge2\), exactly two length-three factors can cross that boundary: \((t_k(j),j,0)\) and \((j,0,1)\). They exist because the left and right blocks each have length at least two. No length-three factor can cross two of these ordinary boundaries, since the middle block would have length at least two. The only middle block of length one is the terminal \(W_0\), already handled. Consequently, all factors appearing before iterate \(k\) belong to \(\mathcal A_0\cup\mathcal A_1\cup\mathcal I_1\cup\mathcal I_2\), with the listed witness stages.

**3. Later iterates.** For \(n\ge k\), use the second decomposition (3). Every length-three factor wholly contained within a block is inherited from a smaller iterate, or is the letterwise \(k\)-shift of a factor in \(W_{n-k}\). At any internal boundary \(W_j\mid W_{j-1}\), where \(n-k+2\le j\le n-1\), the suffix/prefix information in Step 1 gives precisely the two crossing triples
\[
(t_k(j),j,0),\qquad(j,0,1).
\]
At the final boundary \(W_{n-k+1}\mid(k\oplus W_{n-k})\), write \(j=n-k+1\). There is always the crossing triple \((t_k(j),j,k)\), and, if \(j\ge2\), also \((j,k,k+1)\). When \(j=1\), the shifted right block has one letter, and there is no second triple. Every nonempty block before the final one has length at least two; therefore a length-three factor cannot cross two block boundaries. This exhausts all possibilities, proving by induction that every factor of every \(W_n\) belongs to the right side of (1).

**4. Every listed triple actually occurs.** The word \((0,1,0)\) appears in \(W_2\). Each \((1,0,j)\), \(2\le j<k\), appears in \(W_j\). Both internal-boundary triples indexed by \(j\ge2\) appear in \(W_{j+1}\), using the early decomposition when \(j+1<k\), and the later decomposition otherwise. The terminal-boundary triple \((t_k(j),j,k)\) occurs in \(W_{k+j-1}\), as does \((j,k,k+1)\) for \(j\ge2\). Finally, (3) exhibits \(k\oplus W_m\) as a terminal block of \(W_{m+k}\) for every \(m\ge0\). Iteration gives a copy of \(hk\oplus W_m\) inside \(W_{m+hk}\), so every nonnegative \(k\)-shift of a listed factor occurs at or before its witness stage plus \(hk\). As the \(W_n\) are nested prefixes, this proves both the reverse inclusion of (1) and the exact stage formula (2).

**5. Effective membership.** Given a proposed triple \((x,y,z)\), write \(z=qk+r\), \(0\le r<k\). If \(2\le r<k\), only the \(\mathcal A_1\) family is possible: test \((x,y)=(qk+1,qk)\). If \(r=0\), test the \(qk\)-shift of \(\mathcal A_0\cup\mathcal I_1\), and, if \(q\ge1\), the \((q-1)k\)-shift of \(\mathcal T_1\). If \(r=1\), test the \(qk\)-shift of \(\mathcal I_2\), and, if \(q\ge1\), the \((q-1)k\)-shift of \(\mathcal T_2\). Each test is a direct comparison involving \(t_k(j)\) and one arithmetic divisibility/remainder operation. This proves constant-case decidability, independently of the sizes of the letters.

## Verification

The standalone file `verify_triples.py` constructs each finite iterate in two independent ways: directly by applying the morphism to every letter, and by using the block decomposition (3). It compares the actual set of all length-three factors of every tested iterate against the stage-restricted right side of (2). Separately, it checks the residue-based membership algorithm against every triple over a bounded alphabet, using a sufficiently long iterate to include all triples whose witness stages meet the tested bound. Reproducing the recorded run with Python 3 requires only the standard library:

```text
python3 verify_triples.py
```

The reproducible run tested \(k=3,4,5,6,7,8\), a total of 88 iterate languages (with maximum iterate indices 17, 15, 14, 13, 12, and 11 respectively), 2,512 actual factor-set instances across those iterates, and 4,131 membership decisions for all bounded triples. All tests passed. These finite checks support, but do not substitute for, the proof for every \(k\) and \(n\).

## Relationship to prior work

Ghareghani, Mohammad-Noori and Sharifani (2020) introduced the underlying infinite-alphabet words and proved their block decomposition, last-letter and suffix facts and a length-two factor classification. Ghareghani, Golafshan, Mohammad-Noori and Sharifani (2026) enumerated digit and length-two factor occurrences and explicitly posed the classification of length-three and longer factors as Problem 1(i). Formula (1) gives that next length-three language completely; formula (2) also supplies a stage-resolved finite-iterate description. The known suffix and length-two results are prerequisites, not claimed as new.

A separately posted 2026 proof attempt concerning the rationality of occurrence generating functions for factors of arbitrary length addresses a different assertion, about the number of occurrences across iterates rather than which length-three factors exist. Neither the current theorem nor its finite-stage description follows as a *stated* classification from that posted assertion. The present finding makes no claim to a length-three occurrence generating function.

## Limitations

No multiplicities, rational occurrence generating functions for triples, or classifications for lengths four and higher are established. The six families may overlap, so they are not a partition. The result depends on the specified infinite-alphabet morphism, not on arbitrary morphisms with similar block lengths. Published or publicly posted equivalent classifications not identified in the inspected sources remain a historical-priority risk; there has been no independent mathematical validation.

## References

1. N. Ghareghani, M. Golafshan, M. Mohammad-Noori and P. Sharifani, *Enumeration of Factor Occurrences in \(k\)-Bonacci Words over an Infinite Alphabet*, arXiv:2604.01488, first submitted 2026-04-01, especially Sections 2, 5 and Problem 1(i) in Section 6. https://arxiv.org/abs/2604.01488
2. N. Ghareghani, M. Mohammad-Noori and P. Sharifani, *Some Properties of the \(k\)-Bonacci Words on Infinite Alphabet*, Electronic Journal of Combinatorics 27(3) (2020), P3.59, especially Lemmas 4 and 6, Definition 12, Lemma 13 and Theorem 16. https://doi.org/10.37236/9406
3. *Rationality conjecture for factor-occurrence generating functions in \(k\)-Bonacci words*, MathDB public problem record and posted proof attempt, accessed 2026-11-02. https://mathdb.com/p/373998/rationality-conjecture-for-factor-occurrence-generating-func
