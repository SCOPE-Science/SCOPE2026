# Exact LSD-first state complexity of translated Thue–Morse sequences

## Finding

Let \(t(n)=s_2(n)\bmod 2\), where \(s_2(n)\) is the number of ones in the binary expansion of a nonnegative integer. For every integer shift \(c\ge 0\), let \(S(c)\) be the minimum number of states of a complete deterministic finite automaton with output (DFAO) computing \(t(n+c)\) from the binary representation of \(n\) **least-significant-digit first**. The DFAO must work on every finite binary word, including the empty word and words with any number of trailing zero digits.

The four exceptional values are
\[
(S(0),S(1),S(2),S(3))=(2,3,5,6).
\]
For \(c\ge4\), put \(k=\lfloor\log_2 c\rfloor\), and for \(1\le j\le k-1\) put
\[
q_j=\left\lfloor\frac{c}{2^j}\right\rfloor,\qquad
r_j=c\bmod 2^j,\qquad
a_j=2-\mathbf{1}_{\{r_j=2^j-1\}},\qquad
b_j=\begin{cases}0&r_j=0,\\1&r_j=1,\\2&r_j\ge2.\end{cases}
\]
Then the **exact state complexity for every shift** is
\[
\boxed{S(c)=7+\sum_{j=1}^{k-1}\bigl(\mathbf{1}_{\{q_j\ge3\}}a_j+b_j\bigr).}
\]
In each complete dyadic block \(2^k\le c<2^{k+1}\), for every integer \(k\ge3\),
\[
\boxed{2k+3\le S(c)\le4k+1.}
\]
The minimum is attained **only** at \(c=2^k\). The maximum is attained **exactly** at
\[
\boxed{c\equiv2\pmod4,\qquad 3\cdot2^{k-1}\le c<2^{k+1},}
\]
which comprises \(2^{k-3}\) distinct shifts. These state counts also give the exact cardinalities of the binary \(2\)-kernels of the shifted sequences.

## Assumptions and scope

All integers \(n,c\) are nonnegative, every input is a finite word \(w=w_0\cdots w_{L-1}\in\{0,1\}^*\), and its least-significant-digit-first value is \(v(w)=\sum_{i=0}^{L-1}w_i2^i\). The required output on \(w\) is \(t(v(w)+c)\). A DFAO state has one binary output, both bit transitions are defined, and equivalent states must give equal outputs for **every** continuation. Leading-zero normalization is not imposed; appending zeros at the **end** of the least-significant-digit-first input leaves its integer value unchanged.

The first-public-date and primary reference used for the literature context is December 10, 2025, arXiv:2512.10017v1. That paper studies state complexity for linear subsequences and distinguishes the LSD-first and MSD-first regimes. The result proved here concerns only LSD-first shifts; it does not claim to solve an open question about MSD-first shifts.

## Proof

**1. An explicit automaton and its residuals.** Let the possible states be pairs \((d,e)\), where \(d\in\mathbb N\) and \(e\in\{0,1\}\). Begin at \((c,0)\) and, on reading a bit \(b\in\{0,1\}\), set
\[
\delta((d,e),b)=\left(\left\lfloor\frac{d+b}{2}\right\rfloor,\ e\oplus((d+b)\bmod2)\right),\qquad o(d,e)=e\oplus t(d).
\]
Here \(\oplus\) denotes binary exclusive OR. After reading a length-\(L\) prefix of value \(p\), direct induction gives
\[
(d,e)=\left(\left\lfloor\frac{c+p}{2^L}\right\rfloor,\ t((c+p)\bmod2^L)\right).
\]
For any continuation of numerical value \(x\), its output is the residual function
\[
R_{d,e}(x)=e\oplus t(x+d).
\]
Indeed, the lower \(L\) bits of \(c+p+2^Lx\) contribute \(e\), and its remaining binary digits contribute \(t(x+d)\).

**2. Every reachable pair represents a different state.** The binary Thue–Morse sequence is not ultimately periodic. For a self-contained proof, suppose that \(t(m+h)=t(m)\) for every sufficiently large \(m\) and some integer \(h>0\). If \(h\) is even, applying this to even arguments and using \(t(2m)=t(m)\) halves the period. Thus, after finitely many halvings, one gets an odd eventual period \(h=2r+1\). For all large \(m\), the identities \(t(2m)=t(m)\) and \(t(2m+1)=1-t(m)\) imply simultaneously \(t(m+r)=1-t(m)\) and \(t(m+r+1)=1-t(m)\). Hence adjacent terms would eventually be equal. But \(t(2^s)=1\) and \(t(2^s+1)=0\) for every \(s\ge1\), a contradiction.

If two residuals \(R_{d,e}\) and \(R_{d',e'}\) were identical with \(d\ne d'\), then the original Thue–Morse sequence would eventually repeat or complement itself after a positive translation \(h=|d-d'|\). In the latter case it would have eventual period \(2h\). Both are impossible. With \(d=d'\), different \(e\) clearly produce different residuals. Consequently this reachable-state automaton is already minimal, and it remains only to count its reachable pairs.

**3. Exact count in each digit layer.** Fix a prefix length \(L\ge1\), write \(M=2^L\), \(c=qM+r\) with \(0\le r<M\), and allow the prefix value \(p\) to run through every integer in \([0,M-1]\). The above state formula shows that the reachable states on this layer are exactly
\[
\{(q,t(y)):r\le y\le M-1\}\ \cup\
\{(q+1,t(y)):0\le y\le r-1\},
\]
where the second set is empty when \(r=0\). The final two entries of a length-\(M\) Thue–Morse block have opposite values, while its first two entries are \(t(0)=0\) and \(t(1)=1\). Therefore the first set has exactly \(2-\mathbf{1}_{\{r=M-1\}}\) states, and the second has exactly \(0,1,2\) states as \(r=0\), \(r=1\), or \(r\ge2\), respectively.

**4. The six universal low-quotient states.** For every \(c\ge4\), both values of \(e\) occur for each \(d\in\{0,1,2\}\). For \(d=0\), choose \(L\) large enough that \(2^L\ge c+2\) and use the distinct final two Thue–Morse values in \([c,2^L-1]\). For \(d=1\), use the second set on that same layer: its interval \([0,c-1]\) includes \(0\) and \(1\).

For \(d=2\), set \(k=\lfloor\log_2c\rfloor\ge2\) and \(M=2^{k-1}\). If \(2^k\le c<3M\), the layer \(L=k-1\) has quotient \(q=2\) and remainder \(r=c-2^k\). If \(r\le M-2\), its quotient-two states contain both outputs by the last-two-values argument. If \(r=M-1\) and \(M\ge4\), the layer \(L=k\) has quotient \(q=1\) and remainder \(M-1\ge2\), so its overflow states give both values at quotient two. The remaining exceptional case is \(k=2,c=5\): the two layers supply \((2,1)\) and \((2,0)\), respectively. If instead \(3M\le c<2^{k+1}\), the layer \(L=k\) has quotient \(q=1\) and remainder \(c-2^k\ge M\ge2\); its overflow states give both values at quotient two. Thus precisely six distinct low-quotient states always occur.

The initial state \((c,0)\) is a seventh state, distinct from all others since \(c\ge4\). Every positive-length prefix with length \(L\ge k\) has quotient at most two; hence all additional states must have \(d\ge3\) and arise at levels \(1\le j\le k-1\). At level \(j\), the quotient \(q_j\) contributes \(a_j\) states if \(q_j\ge3\), whereas the overflow quotient \(q_j+1\) contributes \(b_j\) states. These high quotients cannot coincide between adjacent or nonadjacent levels: \(q_j\ge2q_{j+1}\) and \(q_{j+1}+1<2q_{j+1}\) for \(q_{j+1}\ge2\). They are also below \(c\) and above two. Summing gives the displayed exact formula. Direct enumeration of the same reachable states gives the exceptional counts for \(c=0,1,2,3\).

**5. Sharp dyadic extrema.** Let \(k\ge3\). At \(j=1\), \(q_1\ge4\) and the layer contributes exactly two high-quotient states, whether \(c\) is odd or even. Every intermediate level \(2\le j\le k-2\) has \(q_j\ge4\) and contributes between two and four states. At the final level \(j=k-1\), the quotient is either two (contribution between zero and two) or three (contribution between two and four). Therefore
\[
7+2+2(k-3)=2k+3\le S(c)\le7+2+4(k-3)+4=4k+1.
\]
Equality on the left forces the final contribution to be zero, hence \(q_{k-1}=2\) and \(r_{k-1}=0\), which is precisely \(c=2^k\); this shift attains the lower bound at every intermediate level.

Equality on the right forces the final quotient to be three and every layer from \(j=2\) onward to contribute four. For \(j\ge2\), the condition for four is \(2\le r_j\le2^j-2\). At \(j=2\) this is exactly \(c\equiv2\pmod4\), and that congruence automatically enforces the required inequalities at all larger levels. The final quotient equals three exactly when \(c\ge3\cdot2^{k-1}\). These conditions describe all maximizing shifts, and the number of such shifts is exactly \(2^{k-3}\).

Finally, minimal LSD-first DFAO states correspond bijectively to subsequences \((t(2^L n+r+c))_{n\ge0}\), with \(L\ge0\) and \(0\le r<2^L\), since these are the residual functions of input prefixes. Thus the same formula counts the shifted binary \(2\)-kernel.

## Verification

A standalone Python standard-library verifier is included as `verify.py`, with recorded output in `verification_output.txt`. Run `python verify.py` in the directory containing the file. It constructs all reachable pairs directly, refines output-equivalence classes by an additional algorithm, and compares the exact formula with all shifts \(0\le c<4096\). It checks all binary inputs of length at most nine on 96 shifts (98,208 direct output evaluations), every dyadic extremizer in blocks \(3\le k\le11\) (4,088 shifts), and 300 fixed-seed random shifts having up to 100 bits. The recorded run concludes `VERIFY_OK`. These computations are finite cross-checks, not a substitute for the universal argument above.

As initial hand-checkable values, \((S(0),\ldots,S(15))=(2,3,5,6,7,8,9,9,9,10,11,11,11,12,13,12)\). At \(k=3\), the minimum is \(S(8)=9\) and the unique maximum is \(S(14)=13\); at \(k=10\), the bounds are 23 and 41.

## Relationship to prior work

Moradi, Rampersad and Shallit (arXiv:2512.10017, first posted 2025-12-10) establish general state-complexity frameworks and distinguish LSD-first arithmetic constructions from the more difficult MSD-first shifted Thue–Morse problem. Their general LSD-first bounds and constructions do not supply the all-shift exact cardinality or its sharp dyadic extremizers derived here. Their stated open problem about **MSD-first** Thue–Morse shifts is a different question and is not claimed solved here.

Zantema and Bosma (*Complexity of automatic sequences*, 2022, Section 7) introduce the reversed-input state-complexity framework, prove general tail-operation bounds, and explicitly calculate the LSD-first one-step Thue–Morse tail complexity as three states. This is the shift \(c=1\) case, not the exact function of all shifts or the dyadic extremal classification.

Moradi, Popoli, Shallit and Vukusic (arXiv:2603.18858, first posted 2026-03-19) obtain logarithmic shift complexity and an exact LSD-first formula for the **Fibonacci word in Zeckendorf representation**, rather than the binary Thue–Morse word. Charlier, Cisternino and Massuir (arXiv:1910.08543) give exact state complexities for the **multiplicative-and-remainder** sets \(m\mathcal T+r\), with \(0\le r<m\); this does not characterize the negative translates of the Thue–Morse set corresponding to \(t(n+c)\). OEIS A382296 explicitly counts **MSD-first** Thue–Morse shifted automata and has different values.

## Limitations

This is an exact result for base-two, LSD-first, complete DFAOs of additive nonnegative translates of the classical Thue–Morse sequence. It does not classify MSD-first minimal automata, shifts in other numeration systems, or arbitrary automatic sequences. The finite verifier cannot establish the infinite result on its own. Relevant accessible primary literature and indexed claims were compared, but unindexed or otherwise inaccessible previous work could still have established an equivalent formula; publication priority has not been independently certified.

## References

1. Delaram Moradi, Narad Rampersad and Jeffrey Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017, first posted 2025-12-10. https://arxiv.org/abs/2512.10017 and https://arxiv.org/html/2512.10017v5
2. Delaram Moradi, Pierre Popoli, Jeffrey Shallit and Ingrid Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858, first posted 2026-03-19. https://arxiv.org/html/2603.18858v1
3. Émilie Charlier, Célia Cisternino and Adeline Massuir, *Minimal automaton for multiplying and translating the Thue-Morse set*, arXiv:1910.08543, first posted 2019-10-18. https://arxiv.org/abs/1910.08543
4. Hans Zantema and Wieb Bosma, *Complexity of automatic sequences*, *Information and Computation* 288 (2022), 104710; available online 2021-02-10. https://doi.org/10.1016/j.ic.2021.104710 and https://www.math.ru.nl/~bosma/pubs/Zantema_Bosma_Complexity_of_Automatic_Sequences.pdf
5. OEIS Foundation, *A382296: Number of states in smallest DFAO computing a shifted Thue-Morse sequence, msd-first*. https://oeis.org/A382296
