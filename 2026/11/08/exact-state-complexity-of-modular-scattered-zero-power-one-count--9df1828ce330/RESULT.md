# Exact state complexity of modular scattered zero-power–one counts

## Finding
For integers \(d\ge 1\), \(m\ge 2\), and \(0\le r<m\), let \(L_{d,m,r}\) be the language of binary words \(w\) for which the number \(\binom{w}{0^d1}\) of scattered occurrences of \(d\) zeros followed by one \(1\) is congruent to \(r\) modulo \(m\). Then the state complexity of a **complete deterministic finite automaton** for \(L_{d,m,r}\) is exactly
\[
\boxed{\operatorname{sc}(L_{d,m,r})=m\prod_{p^a\parallel m}p^{a+\lfloor\log_p d\rfloor}.}
\]
The prime-power product is over the distinct primes dividing \(m\). It is independent of \(r\). A minimal automaton is given explicitly below, with a matching Myhill–Nerode lower bound.

## Assumptions and scope
A scattered occurrence of a pattern \(v\) in \(w\) is a strictly increasing selection of letter positions of \(w\) spelling \(v\); occurrences are counted with multiplicity. \(0^d1\) means \(d\) repetitions of \(0\) followed by a single \(1\), with \(d\ge1\). The alphabet is exactly \(\{0,1\}\), words are finite including the empty word, and the automaton is deterministic and complete, with no end marker. Residues and counts are computed in \(\mathbb Z/m\mathbb Z\). The asserted state count is the number of reachable, pairwise distinguishable states, not merely an upper bound for a counting automaton.

Define
\[
P_d(m)=\prod_{p^a\parallel m}p^{a+\lfloor\log_p d\rfloor},\qquad f(z)=\binom zd\pmod m\quad(z\ge0).
\]
Binomial coefficients are zero for \(0\le z<d\). The claim concerns all indicated integer parameters; it does not assert a minimal automaton for arbitrary other patterns.

## Proof

**1. Exact period of the binomial sequence.** First we prove that the least positive period of \(f\), as a sequence indexed by all nonnegative integers, is \(P=P_d(m)\). Fix a positive integer \(T\). Vandermonde's identity gives
\[
\binom{n+T}{d}-\binom nd=\sum_{j=1}^{d}\binom Tj\binom n{d-j}\quad(n\ge0).
\]
The functions \(n\mapsto\binom nk\), for \(0\le k\le d-1\), are linearly independent over \(\mathbb Z/m\mathbb Z\) as functions of nonnegative \(n\): evaluating successively at \(n=0,1,\ldots,d-1\) gives a unit lower-triangular coefficient matrix. Hence \(T\) is a period if and only if
\[
\binom Tj\equiv0\pmod m\qquad(1\le j\le d).
\]
For each prime-power \(p^a\) dividing \(m\), set \(h=\lfloor\log_p d\rfloor\) and \(e=\nu_p(T)\). If \(e\ge a+h\), use \(\binom Tj=(T/j)\binom{T-1}{j-1}\) to see that \(\nu_p(\binom Tj)\ge e-\nu_p(j)\ge a\) whenever \(1\le j\le d\). Conversely, if \(e\le h\), then \(j=p^e\le d\) and Lucas's congruence shows \(\binom{T}{p^e}\not\equiv0\pmod p\), contradicting periodicity. If \(h<e<a+h\), set \(j=p^h\). Since the lowest \(h\) base-\(p\) digits of \(T-1\) equal \(p-1\), Lucas's congruence yields \(\binom{T-1}{p^h-1}\not\equiv0\pmod p\). Therefore \(\nu_p(\binom T{p^h})=e-h<a\). Thus periodicity modulo \(p^a\) is equivalent to \(p^{a+h}\mid T\); the prime-power conditions jointly establish exactly \(P\).

**2. Explicit complete reachable DFA.** Use states \((z,c)\in\mathbb Z/P\mathbb Z\times\mathbb Z/m\mathbb Z\), starting state \((0,0)\), accepting states with \(c=r\), and transitions
\[
(z,c)\xrightarrow{0}(z+1,c),\qquad
(z,c)\xrightarrow{1}(z,c+f(z)).
\]
The exact period established in step 1 makes the second transition well-defined modulo \(P\). After any word \(w\), its state satisfies \(z\equiv |w|_0\pmod P\) and \(c\equiv\binom w{0^d1}\pmod m\), by adding \(\binom{|w|_0}{d}\) when a \(1\) arrives. Every state is reachable: for any target \(z\pmod P\), choose an integer \(Z\ge d\) with \(Z\equiv z\pmod P\). For each target residue \(c\), the word \(0^d1^c0^{Z-d}\) contains \(Z\) zeros and exactly \(c\) occurrences of the target pattern, since each of the first \(c\) ones has exactly \(d\) preceding zeros. This proves the upper bound \(mP\) and accessibility.

**3. Distinguishability of all states.** Suppose two states \((z,c)\) and \((z',c')\) accept exactly the same continuation words. For \(t=0,\ldots,P-1\), set \(u_t=f(z+t)\), \(v_t=f(z'+t)\), where indices are interpreted modulo \(P\). Any suffix
\[
1^{k_0}0\,1^{k_1}0\,\cdots\,0\,1^{k_{P-1}},\qquad k_0,\ldots,k_{P-1}\ge0,
\]
adds \(\sum_tk_tu_t\) and \(\sum_tk_tv_t\) to the respective count coordinates. Therefore the attainable pairs of count increments form the subgroup
\[
H=\langle(u_t,v_t):0\le t<P\rangle\le(\mathbb Z/m\mathbb Z)^2.
\]
Both coordinate projections from \(H\) are surjective: among the \(P\) consecutive arguments of either \(f\) there is one congruent to \(d\pmod P\), where the value of \(f\) is \(\binom dd=1\pmod m\).

For all \((u,v)\in H\), equivalence of the two states says
\[
(c+u=r)\iff(c'+v=r)\quad\text{in }\mathbb Z/m\mathbb Z.
\]
The first projection is surjective, so some pair in \(H\) has \(u=r-c\). For that first coordinate every pair must have \(v=r-c'\). Consequently the first projection has trivial kernel (otherwise its fiber would contain different second coordinates). Together with surjectivity of both projections, \(H\) is the graph of an additive automorphism of the cyclic group \(\mathbb Z/m\mathbb Z\); there is a unit \(a\pmod m\) such that \(v=au\) for every \((u,v)\in H\). In particular,
\[
f(z'+t)=a f(z+t)\pmod m\quad\text{for all }t\ge0,
\]
because the relation holds for a complete residue period and \(f\) is periodic. Taking the \(d\)-th forward difference in \(t\) gives \(1=a\), since \(\Delta^d\binom{t+z}{d}=1\) as an exact integer identity. Hence \(f(z'+t)=f(z+t)\) for every \(t\ge0\). The least-period assertion of step 1 then forces \(z'=z\pmod P\). Finally every attainable increment is diagonal, and its first projection is surjective; the acceptance predicates for all diagonal increments agree only if \(c'=c\pmod m\). Thus no two distinct states have the same right language. By the Myhill–Nerode theorem, the DFA has exactly the minimum possible number \(mP\) of states. \(\square\)

## Verification
The standalone Python 3 standard-library `checker.py` recomputes \(P_d(m)\), independently minimizes the explicitly constructed DFA through partition refinement for bounded parameters, checks reachable state witnesses, and compares the automaton's output to direct scattered-subsequence counting on binary words of length at most \(12\). A successful run reports:

```text
VERIFIED period_cases=117 minimized_cases=243 reachable_states=2849 direct_word_checks=163820
```
These are finite checks only. The all-parameter proof rests on the period lemma, reachability construction, and subgroup/Myhill–Nerode argument above, not on the enumerations.

## Relationship to prior work
Glenn Bruda (arXiv:2607.02578; first public 2026-06-30) treats enumeration of binary words with an **exact** prescribed scattered-subsequence frequency and obtains eventual polynomiality for patterns with at least two runs. Those frequency enumerations do not imply the minimal number of DFA states recognizing a **modular** frequency condition. Alazemi and Černý (2011) develop weighted trie automata and generalized Parikh matrices that represent scattered-subword counts; this provides an algebraic construction related to the present counting transition, but an exact all-parameter minimal-state result is not supplied by the available abstract/preview, and the complete article could not be inspected. Colbourn, Dougherty, Lidbetter and Shallit (arXiv:1804.11175) study languages comparing **contiguous** subword occurrences, which use a different occurrence notion. Renard, Rigo and Whiteland (arXiv:2402.05657) develop deformed binomial coefficients of words, another counting framework rather than the present modular right-congruence index. The distinctive claims here are the sharp prime-power period and the proof of exact Myhill–Nerode minimality for all \(d,m,r\).

## Limitations
The theorem is restricted to one binary scattered pattern \(0^d1\) and one modular equality residue; it does not give a general formula for arbitrary patterns or multiple simultaneous modular constraints. The 2011 trie-automaton article was accessible only in bibliographic/abstract form during the literature comparison. Historical priority therefore retains uncertainty: no independent priority certification is asserted. Finite tests do not constitute proof beyond their checked ranges, and no independent mathematical validation has been performed.

## References
- G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578, first posted 2026-06-30, https://arxiv.org/abs/2607.02578.
- H. M. K. Alazemi and A. Černý, *Counting subwords using a trie automaton*, International Journal of Foundations of Computer Science **22** (2011), 1457–1469, https://doi.org/10.1142/S0129054111008817.
- C. J. Colbourn, R. E. Dougherty, T. F. Lidbetter and J. Shallit, *Counting Subwords and Regular Languages*, arXiv:1804.11175, https://arxiv.org/abs/1804.11175.
- A. Renard, M. Rigo and M. Whiteland, *q-Parikh Matrices and q-deformed binomial coefficients of words*, arXiv:2402.05657, https://arxiv.org/abs/2402.05657.
