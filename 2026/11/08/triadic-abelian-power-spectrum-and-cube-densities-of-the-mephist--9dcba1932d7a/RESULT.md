# Triadic Abelian-power spectrum and cube densities of the Mephisto Waltz word

## Finding

Let \(w=001001110001\cdots\) be the binary Mephisto Waltz word, the fixed point beginning in \(0\) of the morphism \(0\mapsto001\), \(1\mapsto110\). For each integer \(k\ge0\), **the largest exponent of an Abelian power whose consecutive blocks all have length \(3^k\) is exactly three**. Thus triadic-period Abelian cubes occur, but triadic-period Abelian fourth powers do not.

There is also an exact characterization and frequency formula for *every* Abelian cube of this block length. Write
\[
  i=q3^k+r,\qquad q\ge0,\quad 0\le r<3^k,
\]
and put \(s(n)=(-1)^{d_2(n)}\), where \(d_2(n)\) counts ternary digits equal to \(2\), and
\[
  P_k(r)=\sum_{j=0}^{r-1}s(j),\qquad P_k(0)=0.
\]
Three consecutive length-\(3^k\) blocks starting at \(i\) have identical Parikh vectors if and only if **exactly one** of the following mutually exclusive statements holds:
\[
\begin{split}
&P_k(r)=0\quad\text{and}\quad s(q)=s(q+1)=s(q+2),\\
&P_k(r)=1\quad\text{and}\quad s(q+1)=s(q+2)=s(q+3).
\end{split}
\]
(The two alternatives are in fact disjoint, because \(P_k(r)\) has one value.) Their set of starting positions has a natural density
\[
  \boxed{\displaystyle
  \delta_k=\frac{C_k}{6\cdot3^k},\qquad
  C_k=\#\{0\le r<3^k:P_k(r)\in\{0,1\}\}.}
\]
The numbers \(C_k\) are exactly computable by the finite-state integer recurrence in the proof; for \(k=0,\ldots,8\), they are
\[
  1,\ 2,\ 5,\ 13,\ 35,\ 96,\ 267,\ 750,\ 2123.
\]
This restriction is genuinely *scale-selective*: four Abelian-equivalent blocks of length seven do occur, starting at index \(37\), namely
`0100111 0110110 0011101 1000111`.

## Assumptions and scope

Indices are zero-based, and factors are contiguous. A binary *Abelian \(e\)-power of block length* \(L\ge1\) consists of \(e\) consecutive length-\(L\) factors with equal Parikh vectors. For equal-length binary blocks this is equivalent to equality of their \(\pm1\)-valued sums, using \(0\leftrightarrow+1\) and \(1\leftrightarrow-1\). No assertion is made about avoidance for general nontriadic block lengths. The density is the limit as \(N\to\infty\) of the number of admissible starting positions \(0\le i<N\), divided by \(N\).

## Proof

**1. Digit-product and block identity.** The substitution shows
\[
  s(3n)=s(3n+1)=s(n),\qquad s(3n+2)=-s(n).
\]
Consequently \(s(3^kq+j)=s(q)s(j)\) whenever \(0\le j<3^k\); and the signed sum of a complete substituted block of length \(3^k\) equals \(1\), since each substitution replaces a sign \(a\) by \((a,a,-a)\). Thus
\[
  \sum_{j=0}^{3^k-1}s(j)=1.
\]
The signed sum of the length-\(3^k\) block at \(q3^k+r\) is therefore
\[
  B_k(q,r)=s(q)[1-P_k(r)]+s(q+1)P_k(r).
\]
This accounts for the suffix of the block labeled \(q\) and the prefix of the block labeled \(q+1\), including \(r=0\).

**2. An integer-affine rigidity lemma.** Fix an integer \(p\) and define \(H_p(a,b)=(1-p)a+pb\) on \(\{-1,1\}^2\). The four possible outputs are \(1,-1,1-2p,-1+2p\). If \(p\notin\{0,1\}\), all four are distinct (the only further potential collision would require \(p=1/2\)). Hence equality of consecutive values \(H_p(s(j),s(j+1))\) forces their ordered sign pairs to coincide, which forces all involved signs to be constant. If \(p=0\), equality of \(e\) consecutive values requires a constant run of \(e\) signs beginning at \(j\); if \(p=1\), a constant run of \(e\) signs beginning at \(j+1\).

**3. The longest constant run has length three.** Each substituted length-three block has sign pattern \((a,a,-a)\), so the two entries at indices \(3n+1\) and \(3n+2\) differ; any interval of four consecutive indices contains such a pair. Thus no run has length four. On the other hand, \(s(5)=s(6)=s(7)=-1\), giving a three-letter run.

Combining steps 1–3, equal signed sums of four consecutive length-\(3^k\) blocks are impossible, while the three aligned blocks starting at \(5\cdot3^k\) all have signed sum \(-1\). The same rigidity argument for three consecutive blocks gives precisely the two conditions stated in the finding: for \(p\notin\{0,1\}\), equal values would force an impossible four-letter constant run.

**4. Existence and density of triple runs.** Define \(t(n)=1\) when \(s(n)\ne s(n+1)\), and \(t(n)=0\) otherwise. The substitution implies
\[
  t(3n)=0,\quad t(3n+1)=1,\quad t(3n+2)=1-t(n).
\]
If \(T(N)=\sum_{n=0}^{N-1}t(n)\), then \(T(3N)=2N-T(N)\). For a general \(N=3m+r\) with \(0\le r<3\), the last \(r\) summands are bounded, so
\[
  T(N)-N/2=-[T(m)-m/2]+O(1).
\]
Iteration gives \(T(N)=N/2+O(\log(N+2))\). A constant triple of signs can start only at an index \(3n+2\), and it occurs there exactly when \(t(n)=1\). Thus the natural density of starting indices of constant sign triples is \(1/6\). Shifting those indices by one does not change their density. Each of the \(C_k\) admissible residues \(r\) contributes density \(1/(6\cdot3^k)\) to Abelian-cube starts, giving the formula for \(\delta_k\).

**5. Exact recurrence for the density numerator.** Define, for \(u\in\mathbb Z\) and \(\epsilon\in\{-1,1\}\),
\[
 A_k(u,\epsilon)=\#\{0\le j<3^k:P_k(j)=u,\ s(j)=\epsilon\}.
\]
The initial state is \(A_0(0,+1)=1\), with all other entries zero. The three digit cases give
\[
 \boxed{A_{k+1}(u,\epsilon)=A_k(u,\epsilon)
       +A_k(u-\epsilon,\epsilon)
       +A_k(u+2\epsilon,-\epsilon).}
\]
Indeed the prefix sums at \(3j,3j+1,3j+2\) are respectively \(P_k(j),P_k(j)+s(j),P_k(j)+2s(j)\), with corresponding signs \(s(j),s(j),-s(j)\). Consequently
\[
  C_k=\sum_{\epsilon\in\{-1,1\}}\left(A_k(0,\epsilon)+A_k(1,\epsilon)\right).
\]
This is an exact finite recurrence with at most linearly many reachable sum coordinates at each fixed \(k\), not an extrapolation from a finite prefix.

**6. Nontriadic contrast.** The four displayed length-seven blocks beginning at index \(37\) are direct factors of the fixed point and each contains exactly four ones. Hence they form an Abelian fourth power. This shows that the triadic nonexistence assertion cannot be promoted to an all-period prohibition.

## Verification

Run `python3 verify.py` from this directory. The standalone, standard-library-only checker independently constructs the signed word from ternary digits, checks the substitution identity, compares the formula for all block offsets for \(k=0,\ldots,8\) and \(q=0,\ldots,49\), checks the cube classifier and the nonexistence of fourth powers on these instances, and verifies the recurrence and the nontriadic witness. Its successful output is

`VERIFY_OK checks= 3121982 density_numerators= [1, 2, 5, 13, 35, 96, 267, 750, 2123] nontriadic_witness=(start=37,length=7,blocks=4)`

The finite diagnostics are not used as proof of any universal quantifier; the infinite result follows from the preceding digit, affine, and transition identities.

## Relationship to prior work

Meleshko, Ochem, Shallit and Shan (2022, arXiv:2207.10171, Section 4.1) analyze pseudoperiods of the same Mephisto Waltz word and identify its three-shift pseudoperiodicity. Pseudoperiods compare individual symbols at prescribed forward shifts, rather than Parikh vectors of adjacent length-\(3^k\) blocks, so those results do not imply the present cube spectrum or density formula. Allouche and Shallit's classical ordinary fourth-power-freeness concerns identical adjacent blocks; Abelian equivalence is strictly weaker, as the explicit length-seven Abelian fourth power illustrates. Currie, Mol, Rampersad and Shallit (2021, arXiv:2111.07857) construct **different** binary morphic words that avoid all Abelian fourth powers; their construction does not cover the present word. Chen and Wen (2018, arXiv:1809.06554) count Abelian equivalence classes of factors of a different generalized Thue–Morse family, not consecutive equal-Parikh runs in this word.

## Limitations

This result classifies Abelian cubes and excludes higher Abelian powers **only for block lengths that are powers of three**. The source-comparison search cannot establish universal novelty against unpublished or unindexed literature. The finite verifier is a diagnostic, not an independent audit or a substitute for proof. No exact closed elementary form or limiting asymptotic is asserted for the recursively computable numerator \(C_k\).

## References

- J. Meleshko, P. Ochem, J. Shallit, S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171 (first public version 2022-07-20), Section 4.1. https://arxiv.org/abs/2207.10171
- J. D. Currie, L. Mol, N. Rampersad, J. Shallit, *Extending Dekking's Construction of an Infinite Binary Word Avoiding Abelian 4-Powers*, arXiv:2111.07857 (2021-11-15). https://arxiv.org/abs/2111.07857
- J. Chen and Z.-X. Wen, *On the Abelian Complexity of Generalized Thue–Morse Sequences*, arXiv:1809.06554 (2018-09-18). https://arxiv.org/abs/1809.06554
- J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), Exercise 1.9.16.
