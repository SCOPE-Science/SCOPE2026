# Phase-independent window spectra and exact factor recurrences for prime-base valuation words

## Finding

Let \(p\ge 3\) be prime and \(q\ge2\). Write \(\nu_p\) for the ordinary \(p\)-adic valuation of a positive integer, and form the infinite word
\[
 u_i=\nu_p(i+1)\pmod q\qquad(i\ge0)
\]
over \(\{0,1,\ldots,q-1\}\). Let \(P(n)\) count all distinct contiguous length-\(n\) factors of \(u\). At each block length \(n\ge1\) and each phase \(0\le r<n\), let
\[
 \mathcal W_{n,r}=\{u_{r+jn}u_{r+jn+1}\cdots u_{r+(j+1)n-1}:j\ge0\}.
\]
Put \(n=p^k m\), with \(k=\nu_p(n)\) and \(p\nmid m\). **For every phase \(r\)**, there is an explicit bijection between the full length-\(m\) factor set and \(\mathcal W_{n,r}\); in particular,
\[
 |\mathcal W_{n,r}|=P(m).
\]
Thus the ordinary nonoverlapping-window complexity (phase zero) depends only on the \(p\)-free part of the length, and the count is *independent of the window phase*.

For evaluation of this window spectrum, the ordinary factor count on the right can be computed by the following exact finite radix recurrence, with \(n=pt+s\) and \(0\le s<p\) in the last line. This recurrence is a specialization of Sell's simple Toeplitz factor-complexity theorem; a short direct derivation is included for completeness.
\[
 P(n)=\begin{cases}
 1+n(q-1),&1\le n\le p,\\
 1+(n-p)+n(q-1),&p<n<2p,\\
 (p-s)P(t)+sP(t+1),&n\ge2p.
 \end{cases}
\]
In particular \(|\mathcal W_{p^k,r}|=q\) for every \(k\ge0\), even though \(P(p^k)\ge p^k+1\). At lengths coprime to \(p\), all \(P(n)\) factors occur in *every* phase. The new claim is the explicit all-phase window bijection in prime bases \(p\ge3\). Neither the ordinary factor counts nor the dyadic case are claimed as new.

## Assumptions and scope

Indices and block starts are zero-based; a factor is contiguous and its distinct value, not its occurrence count, is recorded. The phase \(r\) is an integer in \(\{0,\ldots,n-1\}\). The alphabet is a cyclic residue alphabet, not a real-valued valuation sequence. The prime condition is used at the coprimality step \(\gcd(m,p)=1\). Nothing is asserted about analogous all-length identities for composite bases. The ordinary factor count includes factors starting at every nonnegative integer.

## Proof

**1. Prime-adic repetitions.** Fix a source factor \(v=u_a\cdots u_{a+L-1}\). Choose \(h\) with \(p^h>a+L\). For every \(j\in\{0,\ldots,L-1\}\) and \(t\ge0\), the positive integers \(a+j+1\) and \(a+j+1+t p^h\) have the same \(p\)-adic valuation, which is smaller than \(h\). Hence \(v\) occurs at all positions \(a+t p^h\). If \(m\) is coprime to \(p\), these positions traverse every residue modulo \(m\), and do so infinitely often. Consequently **each finite factor occurs at starts of every residue modulo every integer coprime to \(p\)**.

**2. The one-variable block morphism.** Define the length-\(p\) morphism \(\phi(a)=0^{p-1}(a+1\bmod q)\). The valuation identity \(u_{pj+i}=0\) for \(0\le i<p-1\), and \(u_{pj+p-1}=u_j+1\bmod q\), proves \(u=\phi(u)\). Inductively, for every \(k\ge1\) there is a *fixed* word \(H_k\) of length \(p^k-1\) such that
\[
 \phi^k(a)=H_k\,(a+k\bmod q)
\]
for every letter \(a\). Thus each source letter is recovered from the final position of its image block, and every other position of the block is independent of that letter.

**3. Exact phase bijections.** Let \(b=p^k\), \(n=bm\), \(p\nmid m\), and \(0\le r<n\). Write \(r=bj_0+t\) with \(0\le t<b\). Any window starting at \(r+hn\) begins at offset \(t\) inside the block \(\phi^k(u_{j_0+hm})\). For \(t=0\), it is exactly \(\phi^k(u_j\cdots u_{j+m-1})\). For \(t>0\), it equals
\[
 \operatorname{suf}_{b-t}(\phi^k(u_j))\,\phi^k(u_{j+1}\cdots u_{j+m-1})\,\operatorname{pref}_t(H_k).
\]
The last letter of each of these first \(m\) source blocks survives in its own designated location, so either displayed map from a length-\(m\) source factor to its window is **injective**. Both maps use only those \(m\) source letters. Conversely every source factor occurs at a start \(j\equiv j_0\pmod m\) by Step 1, so every such mapped word occurs among the selected windows. This proves a bijection for every \(n,r\), including \(k=0\) (where \(b=1\) and \(t=0\)).

**4. Exact factor recurrence.** Every nonzero letter of \(u\) lies at a position congruent to \(p-1\pmod p\), and the word \(u\) never has two adjacent copies of the letter \(q-1\). A factor of length \(n=pt+s\) beginning at a fixed source-block offset \(e\in\{0,\ldots,p-1\}\) contains exactly \(t\) variable last-block positions for \(p-s\) of the offsets and exactly \(t+1\) such positions for the other \(s\). These values are the corresponding consecutive source letters, shifted by \(+1\pmod q\). Hence the number of factors at each fixed phase is respectively \(P(t)\) or \(P(t+1)\), when those lengths are positive.

For \(n\ge2p\), each factor captures at least two consecutive source letters. At least one is not \(q-1\), so the factor has a nonzero letter. All of its nonzero letters share the unique residue \(p-1-e\pmod p\), allowing us to recover the starting phase \(e\). Phase classes are therefore disjoint, giving the last line of the recurrence. For \(1\le n\le p\), at most one nonzero letter occurs in a factor. Each of the \(n\) possible sites and each of the \(q-1\) nonzero letters occurs, as does the all-zero factor, giving \(1+n(q-1)\). For \(n=p+s\), \(1\le s<p\), the \(p-s\) phases exposing one source letter each contribute \(q-1\) nonzero factors plus one *shared* all-zero factor; the remaining \(s\) phases expose two source letters and contribute \(P(2)=2q-1\) nonzero factors each. Hence
\[
 P(p+s)=1+(p-s)(q-1)+s(2q-1)=1+s+(p+s)(q-1).
\]
This completes the recurrence and the theorem.

**5. Contrasting scales.** At \(n=p^k\), \(m=1\) and the phase-window count is exactly \(P(1)=q\). For \(\gcd(n,p)=1\) it equals \(P(n)\). The word is aperiodic: for any proposed positive period \(d\), choose \(h>\nu_p(d)\) and vary \(h\pmod q\). Then \(u_{p^h-1}=h\bmod q\), whereas \(u_{p^h-1+d}=\nu_p(d)\bmod q\), contradicting periodicity. By the Morse–Hedlund bound \(P(n)\ge n+1\), the window counts are unbounded along lengths coprime to \(p\), but equal \(q\) at all powers of \(p\).

## Verification

Two independent standalone Python programs accompany this result. `verify_templates.py` enumerates all possible length-\(n\) factors using residues modulo the least power of \(p\) exceeding \(n\), with one freely variable high-valuation position, and compares with the radix recurrence. This is a mathematically exhaustive finite oracle for each sampled length, not a finite-prefix guess: the Chinese remainder theorem and arbitrary valuations at the unique exceptional position establish exhaustiveness. It matched 525 cases over \(p\in\{2,3,5,7\}\), \(q\in\{2,3,4\}\), with parameter-dependent ranges of \(n\). `verify_windows.py` independently enumerates every phase's possible length-\(n\) words from compatible residue classes, rather than relying on finite observed prefixes, and matched all 13,542 checked phase cases. The proof above supplies the all-parameter certificate; the programs check finite cases and implementation consistency.

## Relationship to prior work

Cassaigne and Kaboré, *On modulo-recurrence and window complexity in infinite words* (arXiv:2606.13744v1, June 11, 2026), establish a window-complexity/ordinary-complexity identity for the **Thue–Morse** word based on removing the dyadic valuation of the window length. The prime-base words here instead have a fixed-letter prefix in each substitution block; the result treats every phase, all prime bases \(p\ge3\), all residue-alphabet sizes, and supplies an independent exact factor recurrence.

Bognini and Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences* (arXiv:2511.20881v1, November 25, 2025), analyze the **base-two** generalized period-doubling morphism and kernel/gap factorizations. The distinct record *Complete factor and aligned-window complexity of generalized period-doubling words* states the all-length ordinary count and the aligned-window law for \(p=2\), \(q\ge2\). Its windows start only at multiples of their length. It does not state the all-phase result for the higher prime bases, and no relative publication order is asserted here.

Sell's *Combinatorics of One-Dimensional Simple Toeplitz Subshifts*, Proposition 3.7 and Theorem 3.9, supplies the ordinary factor counts for this family. In his coding take level letters \(a_j=j\bmod q\), periods \(n_j=p\) and hole offsets \(r_j=p-1\). The hole set at level \(j\) is \(-1+p^{j+1}\mathbb Z\); its one-sided word is the valuation word above. Filling the single two-sided limit hole at \(-1\) by any letter does not change the factor language: every finite block through that hole is repeated at sufficiently high positive prime powers with the matching valuation residue. All tail alphabets have size \(q\). Thus the ordinary complexity is \(1+(q-1)L\) up to \(p\), and for \(B=p^j\), \(j\ge1\), and \(B<L\le pB\), it is \((q-1)L+B+\min(0,L-2B+B/p)\). This gives \(P(pt)=pP(t)\) when \(t\ge2\); above \(2p\) its breakpoints are multiples of \(p\), so linear interpolation between adjacent multiples gives the displayed recurrence. This prior formula counts all translates together, not the factors observed at starts restricted modulo their own length. The phase-window bijection here requires the separate coprime repetition and shifted-slice arguments in Steps 1–3.

## Limitations

This does not establish the full analogous identity for composite substitution lengths. It counts distinct factor words, not multiplicities or frequencies. The claim of originality is a comparison with inspected literature and retrieved mathematical indices, not a guarantee of priority over unindexed manuscripts. The quoted exhaustive programs check only the stated finite parameters; the infinite theorem depends on the written proof.

## References

1. J. Cassaigne and I. Kaboré, *On modulo-recurrence and window complexity in infinite words*, arXiv:2606.13744v1 (first publicly posted 2026-06-11), https://arxiv.org/html/2606.13744v1.
2. K. E. Bognini and H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881v1 (first publicly posted 2025-11-25), https://arxiv.org/html/2511.20881v1.
3. M. Morse and G. A. Hedlund, *Symbolic Dynamics II: Sturmian Trajectories*, Amer. J. Math. 62 (1940), 1–42 (factor-complexity aperiodicity bound).
4. D. Sell, *Combinatorics of One-Dimensional Simple Toeplitz Subshifts*, arXiv:1801.08778v2, https://arxiv.org/pdf/1801.08778v2, Proposition 3.7 and Theorem 3.9.
5. *Complete factor and aligned-window complexity of generalized period-doubling words*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-complete-factor-and-aligned-window-complexity-of-generalized-per--b359a69047d4.
