# Exact minimal modular subsequence counters for every binary two-run pattern

## Finding
For any integers \(a,b\ge1\) and \(m\ge2\), let \(N_{a,b}(w)\) be the number of **positional scattered** occurrences of the word \(0^a1^b\) in a finite word \(w\in\{0,1\}^*\). An occurrence is a strictly increasing selection of \(a+b\) input positions spelling this pattern; different selections are counted separately. Consider complete deterministic Moore machines that, after reading \(w\), output \(N_{a,b}(w)\bmod m\). Their minimum possible state count is exactly
\[
\boxed{\operatorname{sc}(a,b;m)=m^b\prod_{p^e\parallel m}p^{e+\lfloor\log_p a\rfloor}.}
\]
Here the product is over prime powers exactly dividing \(m\). Every state of the explicit machine below is reachable and distinguishable. Equivalently, each terminal-one extension multiplies the exact state count by \(m\), while the initial zero-run length produces prime-power staircases. For example, for \(m=2\), the count is \(2^{b+\lceil\log_2(a+1)\rceil}\). The statement is valid for all positive \(a,b\), including the previously considered cases \(b=1\) and \((a,b)=(2,2)\); its all-parameter extension to unrestricted \(b\) is the subject of the finding.

## Assumptions and scope
Only the input alphabet \(\{0,1\}\), left-to-right deterministic complete machines, and the full residue-valued output map are considered. The empty input is allowed and has output zero. The claimed minimal number concerns a Moore output machine, **not** the minimum DFA recognizing an individual residue class, although at modulus two the same number is also minimal for each of the two residue-class Boolean languages. No claim is made about composite-modulus Boolean languages or about patterns with more than two runs. All binomial coefficients below are ordinary integers before reduction modulo \(m\), with \(\binom{r}{j}=0\) if \(j>r\).

## Proof
Let \(k=a+b\), \(R=\mathbb Z/m\mathbb Z\), and write \(c_j(w)\) for the residue of the count of scattered copies of the length-\(j\) prefix of \(0^a1^b\), with \(c_0=1\). When a letter matching the \(j\)-th pattern letter is appended, the standard terminal-position decomposition gives \(c_j'=c_j+c_{j-1}\), simultaneously using the old vector on the right. Otherwise \(c_j'=c_j\). This yields a complete deterministic counting machine.

**1. A sharp zero-count period.** Write
\[
P=P_a(m)=\prod_{p^e\parallel m}p^{e+\lfloor\log_p a\rfloor}.
\]
We prove that the binomial vector \((\binom{r}{1},\ldots,\binom{r}{a})\bmod m\) has least positive period exactly \(P\), and that its value identifies \(r\bmod P\). For an integer \(T>0\), Vandermonde's identity and a unit-lower-triangular evaluation at \(r=0,\ldots,a-1\) show that \(\binom{r+T}{a}\equiv\binom r a\pmod m\) for every \(r\ge0\) if and only if
\[
\binom{T}{j}\equiv0\pmod m\qquad(1\le j\le a).
\]
The same criterion is necessary and sufficient for periodicity of the whole binomial vector. Fix \(p^e\parallel m\), put \(h=\lfloor\log_p a\rfloor\), and write \(v=\nu_p(T)\). If \(v\ge e+h\), then \(\binom Tj=(T/j)\binom{T-1}{j-1}\) shows \(\nu_p(\binom Tj)\ge v-\nu_p(j)\ge e\) for all \(j\le a\). Conversely, if \(v\le h\), choose \(j=p^v\); Lucas's congruence gives \(\binom Tj\not\equiv0\pmod p\). If \(h<v<e+h\), choose \(j=p^h\); the lower \(h\) base-\(p\) digits of \(T-1\) are all \(p-1\), giving \(\nu_p(\binom T{p^h})=v-h<e\). Hence the criterion holds exactly when \(p^{e+h}\mid T\) for each \(p^e\parallel m\), establishing the least period \(P\).

To prove injectivity at different residues, suppose the full binomial vectors at nonnegative \(r<s\) are equal. Put \(T=s-r\). Vandermonde's identity, inducting on \(j=1,\ldots,a\), gives \(\binom Tj\equiv0\pmod m\): all terms of lower positive index have already vanished, while the coefficient of \(\binom Tj\) equals one. Therefore \(P\mid T\). Thus the \(P\) zero-count phases have distinct binomial vectors.

**2. A compressed complete machine.** Store \(r=|w|_0\bmod P\) and the polynomial
\[
Y(X)=\sum_{j=1}^b c_{a+j}(w)X^j\quad\text{in}\quad X R[X]/(X^{b+1}).
\]
Let \(B(r)=\binom r a\bmod m\). The transitions are
\[
0:(r,Y)\mapsto(r+1,Y),\qquad
1:(r,Y)\mapsto\bigl(r,(1+X)Y+B(r)X\bigr),
\]
where \(r\) is interpreted modulo \(P\), and the output is the coefficient of \(X^b\). The preceding period proof makes the update well defined. The initial state is \((0,0)\). This machine has \(P m^b\) formal states, giving the upper bound.

**3. Every formal state is reachable.** Fix an arbitrary zero-count phase \(r_0\). Appending \(0^t1 0^{P-t}\) returns that phase and acts on \(Y\) by
\[
F_{B(r_0+t)}(Y)=(1+X)Y+B(r_0+t)X.
\]
As \(t\) ranges over one full period, it includes a phase of value \(B(0)=0\) and a phase of value \(B(a)=1\). Consequently words returning to \(r_0\) realize both maps \(F_0(Y)=(1+X)Y\) and \(F_1(Y)=(1+X)Y+X\). They are bijections of the finite set \(X R[X]/(X^{b+1})\), so their inverses also are realized by positive powers of the corresponding words. Their composition \(F_1F_0^{-1}\) is translation by \(X\). Conjugating by \(F_0^j\) realizes translation by \(X(1+X)^j\), for \(0\le j<b\). These \(b\) vectors are a basis of the free \(R\)-module \(X R[X]/(X^{b+1})\), because their coefficient matrix relative to \(X,X^2,\ldots,X^b\) is triangular with diagonal entries one. Arbitrary repeated translations therefore reach every \(Y\) at the fixed phase. Starting at \((0,0)\), this gives all \(m^b\) polynomials at phase zero, then appending \(0^r\) reaches all \(P\) phases. Thus all \(Pm^b\) states are reachable.

**4. No two states are equivalent.** Every distinct stored state has a distinct complete prefix-counter vector \((c_1,\ldots,c_k)\): the phase is recovered from the first \(a\) coordinates by Step 1, and \(Y\) gives the rest. For two differing vectors, let \(j\ge1\) be their highest differing coordinate. Append the length-\(k-j\) suffix of the target pattern following position \(j\). Under the simultaneous recurrence of Step 1, the difference in final count is exactly the previous difference at coordinate \(j\): lower differing coordinates cannot advance enough positions, and higher coordinates already agree. This nonzero difference holds modulo any \(m\), and distinguishes the two Moore outputs. By deterministic right-output equivalence, the machine is minimal. Combining Steps 2--4 proves the stated formula.

At \(m=2\), the final outputs are Boolean, so the same distinguishing suffix separates membership in either fixed residue-class language, giving the additional binary-DFA observation. \(\square\)

## Verification
`checker_modular.py` uses direct integer-binomial recurrences, an independent full-orbit search and finite distinguishing-suffix signatures. It checks \(201\) nontrivial parameter triples, totaling \(93{,}596\) distinct reachable modular states, plus \(4{,}236\) candidate-period tests and \(49{,}056\) direct modular checks against positional embeddings. `checker_bitwise.py` independently uses packed parity counter states, exhaustive words and an independent suffix-output signature. It checks \(54\) parameter pairs, \(13{,}196\) reachable states and \(24{,}042\) literal words. Both programs require only Python 3 and the standard library; run `python3 checker_modular.py` and `python3 checker_bitwise.py` in a directory containing them. Recorded outputs are included. These finite checks corroborate but do not replace the proof for unbounded parameters.

## Relationship to prior work
The 2011 trie-automaton construction of Alazemi and Černý counts arbitrary scattered subwords, and Fazekas and Huang's 2024 generalized Parikh-matrix paper gives homomorphic occurrence representations. Those general counting constructions do not themselves establish minimal deterministic residue-output state counts. The 2026 paper of Fazekas, Huang and Mercaş investigates binary Parikh-matrix universality and probabilities within classes, rather than the exact modular right-output orbit here. Chistikov, Piórkowski, Rino and van der Merwe (2026) examine finite-field-weighted automata and XNFA algorithmic complexity, but not these pattern-specific exact Moore-state formulas.

Two closest earlier exact statements already establish (i) the modular Boolean-DFA complexity for \(0^a1\) for every \(a,m\), and (ii) the modular Moore complexity for \(0011\) for every \(m\). Their formulas agree exactly with the corresponding specializations above: \(mP_a(m)\) and \(m^3\gcd(m,2)\), respectively. They do **not** state the full family with unrestricted terminal-one length \(b\), nor do those isolated state counts imply its affine-module reachability argument. These special cases are acknowledged as known, not claimed as independent new discoveries. The contribution is the single all-parameter two-run classification, including its exact multiplicative dependence on \(b\).

## Limitations
The result is a Moore-machine state count for the entire modular output function; it does not establish the minimum Boolean-DFA state count for a prescribed residue when \(m>2\), does not treat patterns with more than two runs, and does not assert minimum sizes for nondeterministic or other automata models. The 2026 motivating paper and the 2011 trie-automaton paper were not available in complete text in the source access routes used; their abstracts/metadata were compared, and full published equivalence cannot be categorically excluded. No independent mathematical audit or historical-priority certification has been performed.

## References
1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first publicly submitted 2026-10-05), https://arxiv.org/abs/2610.06717.
2. D. Chistikov, R. Piórkowski, N. Rino, B. van der Merwe, *Algorithms and fine-grained complexity for nondeterministic and symmetric difference automata*, arXiv:2607.00742 (first publicly submitted 2026-07-01), https://arxiv.org/abs/2607.00742.
3. S. Z. Fazekas, X. Huang, *Generalized Parikh Matrices For Tracking Subsequence Occurrences*, arXiv:2407.04462 (2024), https://arxiv.org/html/2407.04462v1.
4. H. M. K. Alazemi, A. Černý, *Counting subwords using a trie automaton*, International Journal of Foundations of Computer Science **22** (2011), 1457--1469, https://doi.org/10.1142/S0129054111008817.
5. *Exact state complexity of modular scattered zero-power–one counts*, public mathematical record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-state-complexity-of-modular-scattered-zero-power-one-count--9df1828ce330.
6. *Exact Moore-state complexity of modular scattered 0011 counts*, public mathematical record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-moore-state-complexity-of-modular-scattered-0011-counts--f0fa64081c4c.
