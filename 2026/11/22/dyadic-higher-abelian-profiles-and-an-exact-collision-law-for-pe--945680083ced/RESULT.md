# Dyadic higher-Abelian profiles and an exact collision law for period-doubling factors

## Finding

Let \(\mu(0)=01\), \(\mu(1)=00\), and let \(p=\mu^\omega(0)\) be the infinite period-doubling word. For \(\ell\ge2\), write \(\mathcal P_p^{(\ell)}(n)\) for the number of distinct \(\ell\)-Abelian profiles of contiguous length-\(n\) factors of \(p\): the profiles give the number of overlapping occurrences of *every* binary word of length at most \(\ell\). Write \(P_p(m)\) for ordinary factor complexity, namely the number of distinct length-\(m\) factors of \(p\).

**General dyadic classification.** Put \(m=2(\ell-1)\), \(j=\lceil\log_2 m\rceil\). For all integers \(k\ge j+3\),
\[
\boxed{\mathcal P_p^{(\ell)}(2^k)=2P_p(2\ell-2).}
\]
In fact the profiles are in explicit bijection with pairs \((a,v)\), where \(a\in\{0,1\}\) and \(v\) is any length-\(m\) factor of \(p\). Set \(U_{k,a}=\mu^k(a)\), of length \(L=2^k\). The natural frequency of the profile labeled \((a,v)\), as the starting index of a factor ranges over nonnegative integers, exists and equals
\[
\boxed{\nu_{k,\ell}(a,v)=\frac{\pi_a}{L}\operatorname{occ}_{\rm cyc}(v,U_{k,a}),\qquad (\pi_0,\pi_1)=(2/3,1/3),}
\]
where \(\operatorname{occ}_{\rm cyc}\) counts starting positions in the circular word \(U_{k,a}\), with multiplicity.

**Explicit three-Abelian law.** For every integer \(k\ge4\), the length-\(2^k\) factors have exactly twelve three-Abelian profiles. Write \(L=2^k\), \(\delta=(-1)^k\), and partition their four-letter bridge contexts into \(A=\{0001,0010,0100,1000\}\) and \(B=\{0101,1010\}\). Their individual natural frequencies are given by the following table; each listed value occurs for every \(v\) in that row's context set.

| Block label | Context set | Number of profiles | Frequency of each profile |
|---|---|---:|---|
| \(a=0\) | \(A\) | 4 | \((L+2\delta)/(9L)\) |
| \(a=0\) | \(B\) | 2 | \((L-4\delta)/(9L)\) |
| \(a=1\) | \(A\) | 4 | \((L-4\delta)/(18L)\) |
| \(a=1\) | \(B\) | 2 | \((L+8\delta)/(18L)\) |

Consequently, for two independent length-\(L\) factors sampled from the stationary natural-frequency law, the probability that their complete three-Abelian profiles agree is exactly
\[
\boxed{\sum_{a,v}\nu_{k,3}(a,v)^2=\frac5{54}+\frac{32}{27\cdot4^k}.}
\]
This is a distributional statement about all factor *starts*, not a uniform distribution on distinct factors or distinct profiles.

## Assumptions and scope

All words are binary, occurrences are contiguous and may overlap, and positions start at zero. A factor's \(\ell\)-Abelian profile records exact counts of all subwords of lengths \(1,2,\ldots,\ell\). Finite circular occurrence counts are taken modulo the circular word length, whereas factor counts and natural frequencies in \(p\) use ordinary linear factors. The general classification requires \(\ell\ge2\) and \(k\ge\lceil\log_2(2\ell-2)\rceil+3\); its explicit \(\ell=3\) refinement holds already for \(k\ge4\). No assertion is made for smaller general thresholds, and the theorem does not assert a reconstruction-code capacity.

## Proof

**1. Substitution blocks and their weights.** Both \(U_{k,0}\) and \(U_{k,1}\) have length \(L=2^k\). For every \(k\ge1\) they have a common prefix of length \(L-1\), and their last bits are opposite. This follows by induction from the common first symbol in \(\mu(0)=01\) and \(\mu(1)=00\). The binary substitution matrix gives the one-counts
\[
 |U_{k,0}|_1=(L-(-1)^k)/3,\quad |U_{k,1}|_1=(L+2(-1)^k)/3.
\]
They differ by one. The primitive substitution has letter frequencies \(\pi_0=2/3\) and \(\pi_1=1/3\).

**2. Exact rotation decomposition.** The factor of length \(L\) starting at \(qL+r\), where \(0\le r<L\), consists of the suffix of the \(q\)-th substituted block \(U_{k,p_q}\) and an \(r\)-letter prefix of the next block. For \(r<L\), this prefix is independent of the next block's letter, so this factor is exactly the rotation \(\rho_r(U_{k,p_q})\). Thus *every* length-\(L\) factor is one of the rotations of the two blocks. Conversely every such rotation actually occurs, because both letters occur in the fixed point. Their different one-counts prevent any cross-block equality of \(\ell\)-Abelian profiles.

**3. The bridge lemma.** Let \(w\) be a circular binary word of length \(L\) and \(h=\ell-1\), with \(L\ge2h\). To a cut \(r\) assign the length-\(2h\) circular bridge \(v_r\) formed by the last \(h\) letters before the cut followed by the first \(h\) letters after it. Two rotations \(\rho_r(w),\rho_s(w)\) are \(\ell\)-Abelian equivalent if and only if \(v_r=v_s\).

For the forward implication, linear occurrence counts of \((h+1)\)-grams determine the initial and terminal \(h\)-letter words: for any \(h\)-gram \(u\), its occurrence count minus the sum of occurrence counts of all \((h+1)\)-grams \(cu\) is exactly the indicator that \(u\) is the initial \(h\)-gram; subtraction of counts of \(uc\) instead identifies the terminal \(h\)-gram. Both rotations therefore have equal prefixes and suffixes of length \(h\), and hence equal bridges. For the reverse implication, every circular occurrence count of a word of length at most \(\ell\) is invariant under rotation. Its corresponding *linear* count is the circular count minus the contributions straddling the chosen cut. Each straddling contribution depends only on the last \(\ell-1\) symbols before the cut and the first \(\ell-1\) after it, namely the bridge. Equal bridges imply equal linear occurrence counts at all lengths up to \(\ell\).

**4. Stabilization of bridge contexts.** Fix \(m=2h\), \(j=\lceil\log_2 m\rceil\), so \(m\le2^j\). Decompose \(p\) into aligned length-\(2^j\) blocks. Every length-\(m\) factor meets at most two consecutive blocks. Because the first \(2^j-1\) positions of both block types agree, it is a circular factor of \(U_{j,a}\) for the letter \(a\) of the first block. Conversely all circular length-\(m\) factors of \(U_{j,0}\) or \(U_{j,1}\) occur linearly in \(p\): the pairs of adjacent block types \(00\) and \(10\) both occur in \(p\), and any wraparound tail uses at most \(m-1\le2^j-1\) letters, which the two substituted blocks share. Hence
\[
 \mathcal F_m(p)=\mathcal F_m^{\rm cyc}(U_{j,0})\cup\mathcal F_m^{\rm cyc}(U_{j,1}).
\]
For \(k-j\ge3\), each \(\mu^{k-j}(a)\) contains both length-two factors \(00\) and \(10\): this is visible in \(\mu^3(0)=01000101\) and \(\mu^3(1)=01000100\), and is preserved under further iteration. Expanding these pairs by \(\mu^j\) shows that the *single* word \(U_{k,a}\) contains all the circular length-\(m\) factors of both \(U_{j,0}\) and \(U_{j,1}\). Conversely every circular length-\(m\) factor of \(U_{k,a}\) is a linear factor of \(p\), by the same common-prefix argument using a pair \(a0\) occurring in \(p\). Therefore, for each \(a=0,1\),
\[
 \mathcal F_m^{\rm cyc}(U_{k,a})=\mathcal F_m(p).
\]
The bridge lemma and the distinct block weights prove the general formula and labeling.

**5. Exact natural frequencies.** At any fixed offset \(r\) within aligned length-\(L\) blocks, the type \(a\) of the block appears with natural frequency \(\pi_a\). Each type-
\(a\) block contributes one factor start of each of its \(L\) offsets. The proportion of all factor starts bearing bridge \(v\) and type \(a\) is therefore \(\pi_a\operatorname{occ}_{\rm cyc}(v,U_{k,a})/L\). The bridge lemma makes this the frequency of the corresponding \(\ell\)-Abelian profile.

**6. Three-Abelian frequencies and collision.** The period-doubling word has no \(11\) and no \(0000\); since each even index contains zero, every circular zero gap between consecutive ones in \(U_{k,a}\) has length one or three. For \(k\ge4\), both lengths occur. Each three-zero gap contributes exactly once to *each* of the four contexts in \(A\); each one-zero gap contributes exactly once to *each* of the two contexts in \(B\). Let \(B_a\) and \(C_a\) denote the numbers of these gaps. Then \(4B_a+2C_a=L\) and \(B_a+C_a=|U_{k,a}|_1\), giving
\[
 B_0=(L+2\delta)/6,\ C_0=(L-4\delta)/6,\quad B_1=(L-4\delta)/6,\ C_1=(L+8\delta)/6.
\]
The six possible bridge contexts exhaust the period-doubling length-four language. Substitution into Step 5 produces the twelve displayed frequencies. Summing the squares of the four occurrences of each \(A\)-frequency and two of each \(B\)-frequency gives \(5/54+32/(27L^2)\), as asserted.

## Verification

Two standalone Python standard-library programs are provided. `verification/check_general.py` independently compares the full overlapping \(\ell\)-Abelian signatures, the circular bridge partitions, and the length-\(m\) ordinary factor sets for \(\ell=2,3,4,5,6\) and the tested pairs \((\ell,k)=(2,4),(2,5),(3,5),(3,6),(4,6),(4,7),(5,6),(5,7),(6,7),(6,8)\). It prints `GENERAL_OK` on success. `verification/check_direct.py` enumerates every rotation for \(k=4,5,6,7,8,9\), computes all overlapping counts through length three, checks each of the twelve context multiplicities, and verifies the exact rational collision probabilities, printing `DIRECT_OK`. The programs check finite instances independently of the symbolic all-length proof; they are not substituted for that proof.

## Relationship to prior work

Cassaigne, Fici, Sciortino and Zamboni describe the cyclic complexity of the period-doubling word; their Proposition 17 gives two *fully represented cyclic-conjugacy classes* at dyadic lengths. That count neither states the classification of all \(\ell\)-Abelian profiles nor gives their natural frequencies. Parreau, Rigo, Rowland and Vandomme establish regularity methods for binary two-Abelian complexity, including period doubling; these do not supply the present higher-order dyadic bridge spectrum or the exact nonuniform three-Abelian collision law. The bridge-count and frequency formula provides information not implied by the bare complexity/count of cyclic classes.

## Limitations

The all-order formula is proved only at the specified sufficient dyadic threshold, which is not claimed to be sharp. The explicit three-Abelian twelve-profile result starts one scale earlier. The collision probability is with respect to natural factor-start frequencies, not uniformly selected distinct factors. The result has undergone only the included mathematical reconstruction and finite checks; no independent audit has been performed. A complete priority claim against all unindexed historical literature is not made.

## References

- J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first public version 2014-02-24, https://arxiv.org/pdf/1402.5843.
- P. Parreau, M. Rigo, E. Rowland and E. Vandomme, *A new approach to the 2-regularity of the ℓ-Abelian Complexity of 2-Automatic Sequences*, arXiv:1405.3532, first public version 2014-05-14, https://arxiv.org/pdf/1405.3532.
