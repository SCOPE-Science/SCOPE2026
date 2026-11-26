# Exact state complexity of simultaneous binary value and digit-weight congruences

## Finding

For integers \(m,k\ge 1\) and residues \(0\le a<m\), \(0\le b<k\), let \(L_{m,k;a,b}\) be the language of all finite binary strings \(w\), including the empty string and strings with leading zeros, for which the base-two value \(\operatorname{val}_2(w)\) is congruent to \(a\pmod m\) and the number \(|w|_1\) of ones is congruent to \(b\pmod k\). Write \(m=2^t u\) with \(u\) odd and \(t\ge0\). Then the minimal **complete** DFA for every one of these languages has exactly

\[
\boxed{ku+t}
\]

states, independently of the chosen target residues. The quotient classes are given explicitly below. For completeness we also give a direct finite-state proof of the known density conclusion: for each fixed \(m,k,a,b\), the fraction of length-\(n\) binary strings belonging to \(L_{m,k;a,b}\) tends exponentially fast to \(1/(mk)\).

For example, the exact state counts at \((m,k)=(3,2),(6,2),(8,3),(12,2),(24,3),(30,4)\) are respectively \(6,7,6,8,12,61\), for **every** target pair. The count is not the product of the minimal state counts for the two separate conditions: shared binary input causes an exact two-adic collapse.

## Assumptions and scope

Words are read **most significant digit first** and may contain leading zeros. Define \(\operatorname{val}_2(\varepsilon)=0\) and \(|\varepsilon|_1=0\). Congruences with modulus one impose no restriction. A complete DFA includes a transition on each of the letters \(0,1\) at every state. These conventions matter: excluding empty words or leading zeros changes the language and may change its state complexity.

Use the complete \(mk\)-state residue DFA with states \((r,p)\in\mathbb Z/m\mathbb Z\times\mathbb Z/k\mathbb Z\), start state \((0,0)\), only accepting state \((a,b)\), and transitions

\[
(r,p)\xrightarrow{d}(2r+d\bmod m,\ p+d\bmod k),\qquad d\in\{0,1\}.
\]

Its reachable states are all \(mk\) pairs. The result identifies the exact right-language quotient of this DFA for every target pair.

## Proof

**1. Fixed-length simultaneous reachability.** For odd \(u>1\), let \(h\) be the multiplicative order of \(2\pmod u\), so \(h\ge2\). A word of length \(N\) has contributions \((2^j\bmod u,1)\) to its value modulo \(u\) and its one-count modulo \(k\) when its bit at exponent \(j\) is one. Positions of exponent congruent to \(0\) and \(1\pmod h\) contribute respectively \((1,1)\) and \((2,1)\). Their difference is \((1,0)\), so together they generate the whole finite abelian group \(\mathbb Z/u\mathbb Z\times\mathbb Z/k\mathbb Z\). Every element is a nonnegative combination of these two generators with each coefficient bounded by \(uk-1\): reduce integer coefficients modulo their finite orders. The length \(N=huk+1\) supplies at least \(uk\) bit positions of each kind. Hence **every** pair of residues is attained by some word of the same length \(N\). For \(u=1\), the same holds with \(N=k\), by selecting the required number of ones.

For \(m=2^t u\), prescribe any numerical residue \(c\pmod m\) and one-count residue \(d\pmod k\). Fix the last \(t\) bits to represent \(s=c\bmod 2^t\) (take \(s=0\) and an empty suffix when \(t=0\)). For \(u>1\), the preceding length-\(N\) word can be chosen to have value \(2^{-t}(c-s)\pmod u\) (using the inverse of \(2^t\) modulo odd \(u\)) and one-count \(d-|s|_1\pmod k\). For \(u=1\), the value condition on the preceding word is vacuous and only the one-count condition is prescribed. It follows that every pair \((c,d)\) is realized by a word of a common length \(N+t\), and by words of every greater length after adding leading zeros. In particular, every state of the residue DFA is reachable.

**2. All sufficiently long suffixes.** Starting in \((r,p)\), appending a length-\(j\) word \(z\) gives value \(2^j r+\operatorname{val}_2(z)\pmod m\) and one-count \(p+|z|_1\pmod k\). For every \(j\ge t\), acceptance therefore depends on the old state **only** through \((r\bmod u,p)\). Conversely, two states with different values of this pair can be distinguished by a sufficiently long suffix: choose a common suffix length at least \(t\) at which every numerical residue modulo \(m\) and one-count residue modulo \(k\) is representable, and choose its residues to make the first state accept. If the two old numerical residues differ modulo \(u\), invertibility of \(2^j\pmod u\) prevents acceptance from the second; if the numerical residues agree modulo \(u\) but the one-count residues differ, the latter condition prevents it. Thus long suffixes give exactly \(uk\) preliminary equivalence classes.

**3. Short suffixes add exactly \(t\) classes.** For \(0\le j<t\), a length-\(j\) suffix can reach numerical residue \(a\) only if it represents \(s_j=a\bmod2^j\), so there is exactly one *possible accepting suffix* of that length, namely the \(j\)-digit representation of \(s_j\) padded with leading zeros (\(s_0=\varepsilon\)). Its accepting predecessor set is

\[
E_j=\left\{(r,p):r\equiv\left\lfloor\frac a{2^j}\right\rfloor\pmod{m/2^j},\quad p\equiv b-|s_j|_1\pmod k\right\}.
\]

Each \(E_j\) is nonempty and lies inside a single long-suffix class. Process these sets in descending order \(j=t-1,t-2,\ldots,0\), refining the partition according to membership in each set. All elements of \(E_j\) have the same residues modulo \(m/2^j\) and modulo \(k\), so all have identical membership in every \(E_\ell\) with \(\ell>j\). Thus \(E_j\) can split **at most one** existing class. To see that a split really occurs, choose \((r,p)\in E_j\) and compare it with \((r+m/2^{j+1}\bmod m,p)\). The two lie in the same long-suffix class (the residue difference is a multiple of \(u\)), have identical membership in all \(E_\ell\) with \(\ell>j\), but only the first lies in \(E_j\). Hence each short suffix adds exactly one class, producing \(uk+t\) classes. Since these are exactly all right-language distinctions, the Myhill–Nerode theorem gives the claimed minimal complete-DFA size.

**4. Uniform long-word densities.** On \(\mathbb Z/u\mathbb Z\times\mathbb Z/k\mathbb Z\), the two letter maps \((r,p)\mapsto(2r,p)\) and \((r,p)\mapsto(2r+1,p+1)\) are permutations. Their average is therefore a doubly stochastic Markov transition matrix. Step 1 shows that a sufficiently high fixed power has every entry positive: from any start pair, every end pair can be reached in the common length. Hence the chain is primitive and converges exponentially fast to the uniform distribution. For \(n\ge t\), the last \(t\) bits are uniform and independent of the first \(n-t\), determining the residue modulo \(2^t\). The preceding block becomes uniform jointly in value modulo \(u\) and one-count modulo \(k\); the Chinese remainder theorem then gives asymptotic probability \(1/(2^tuk)=1/(mk)\) for each prescribed pair. This proves the density assertion.

## Verification

Run `python3 check_minimize.py`, `python3 check_quotient.py`, and `python3 check_density.py` in a directory containing these three files. The first program constructs every reachable residue state and independently refines the full complete DFA for \(180\) parameter pairs and \(1294\) chosen target-residue pairs. The second constructs the explicit residual-signature equivalence, checks its transition congruence and verifies its predicted number of classes for \(2610\) target-residue pairs. The third counts exact input words dynamically and checks the predicted asymptotic distribution for six modulus pairs. Their captured outputs are included separately. The infinite theorem is proved by the preceding arguments, not by these finite tests.

## Relationship to prior work

Binary-coded unary languages and their state complexity provide context in Geffert, Hlaváč and Královič (2026), who study two-way automata. For the one-way problem, Alexeev's divisibility theorem already gives \(u+t\) for \(k=1\), \(a=0\). Charlier, Cisternino and Massuir (2019) prove \(2u+t\) states in binary for \(m\mathcal T+a\), where \(\mathcal T\) is the set of nonnegative integers of even binary digit sum and \(0\le a<m\). In general this is not the simultaneous residue language: for instance \(6\in 3\mathbb Z\cap\mathcal T\) but \(6\notin3\mathcal T\). However, if \(m=2^t\), \(k=2\) and \(b=|a|_1\bmod 2\) (the parity of the binary weight of \(a\)), the language is exactly the binary representations of \(2^t\mathcal T+a\): the low \(t\) bits are those of \(a\), and the remaining bits must have even weight. That subcase, including \((a,b)=(0,0)\), is already covered. The state-complexity contribution here is the joint congruence quotient for arbitrary moduli and both arbitrary targets, beyond these special cases.

The uniform exponential density is a consequence of Gelfond's classical digit-sum theorem [6, 7], not a novelty claim. In radix two its coprimality condition on the digit-sum modulus is automatic. Each length-\(n\) word represents exactly one integer in \([0,2^n)\), so the power-saving error \(O(X^\lambda)\) for \(X\) integers, where \(\lambda<1\), becomes a frequency error \(O(2^{-n(1-\lambda)})\). If a modulus is one, one may use modulus two in its place and sum over the two residues. Section 4 supplies a direct argument using the same residue states as the state-complexity proof.

## Limitations

This statement assumes radix two, most-significant-digit-first reading, leading zeros allowed, and a single joint target pair. It does not determine complexities after forbidding leading zeros, changing radix, or accepting unions of target pairs. An equivalent state-complexity result or a stronger theorem outside the inspected sources remains possible.

## References

1. V. Geffert, V. Hlaváč and R. Královič, *Unary Versus Binary Two-Way Automata*, EPTCS 451 (2026), 1–16, first arXiv posting 2026-08-25, https://arxiv.org/abs/2608.24238 .
2. É. Charlier, C. Cisternino and A. Massuir, *State Complexity of the Multiples of the Thue-Morse Set*, EPTCS 305 (2019), 34–49, https://arxiv.org/abs/1909.07676 .
3. É. Charlier, C. Cisternino and A. Massuir, *Minimal automaton for multiplying and translating the Thue-Morse set*, arXiv:1910.08543 (2019), https://arxiv.org/abs/1910.08543 .
4. B. Alexeev, *Minimal DFA for testing divisibility*, Journal of Computer and System Sciences 69 (2004), 235–243, https://borisalexeev.com/papers/dfa.html .
5. É. Charlier, N. Rampersad, M. Rigo and L. Waxweiler, *State Complexity of Testing Divisibility*, arXiv:1008.1668 (2010), https://arxiv.org/abs/1008.1668 .
6. A. O. Gelfond, *Sur les nombres qui ont des propriétés additives et multiplicatives données*, Acta Arithmetica **13**, 259–265, https://doi.org/10.4064/aa-13-3-259-265 .
7. J. Morgenbesser, *General Gelfond problems for numeration systems* (2010), p. 135, equation (6.1), https://repositum.tuwien.at/handle/20.500.12708/10276 .
