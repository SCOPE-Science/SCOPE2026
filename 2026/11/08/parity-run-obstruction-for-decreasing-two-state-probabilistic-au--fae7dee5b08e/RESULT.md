# Parity-run obstruction for decreasing two-state probabilistic automata over arbitrary finite alphabets

## Finding
Let \(q\ge3\), let \(\Sigma\) have \(q\) symbols, and let \(n\ge1\). Consider the class of two-state probabilistic finite automata (PFAs) whose every letter-transition matrix has strictly negative determinant. If such an automaton strictly prefers one length-\(n\) word \(w\) to every other length-\(n\) word, then the odd-indexed subsequence \(w_1w_3\cdots\) and the even-indexed subsequence \(w_2w_4\cdots\) each have *nonrecurrent runs*: no letter occupies two separated constant runs.

Consequently, the total number \(R_q(n)\) of words realizable as strict unique maximizers by this class obeys
\[
R_q(n)\le T_q(\lceil n/2\rceil)T_q(\lfloor n/2\rfloor),\qquad
T_q(0)=1,\qquad
T_q(m)=\sum_{r=1}^{\min(q,m)}(q)_r\binom{m-1}{r-1}\quad(m\ge1),
\]
where \((q)_r=q!/(q-r)!\). Thus, for every fixed \(q\ge3\), \(R_q(n)=O_q(n^{2q-2})\), whereas the full word space has size \(q^n\). The upper bound is not asserted to be sharp.

## Assumptions and scope
A two-state PFA has an initial distribution, one row-stochastic \(2\times2\) matrix \(P_a\) for each input letter \(a\), and an indicator vector of accepting states. Its acceptance probability for a word is the probability of ending in an accepting state. A *strict unique maximizer* at length \(n\) has strictly larger acceptance probability than each other length-\(n\) word. Determinants are required to be strictly negative for **every** letter. Accepting all or no states cannot yield a strict unique maximizer for \(q\ge3\); interchange the two state labels if needed to make state 1 the only accepting state.

Write
\[
P_a=\begin{pmatrix}u_a&1-u_a\\v_a&1-v_a\end{pmatrix},\quad
f_a(x)=v_a+(u_a-v_a)x,
\]
where \(x\in[0,1]\) is the probability of state 1 before the letter. Since \(\det P_a=u_a-v_a<0\), every map \(f_a\) is strictly decreasing. All statements quantify over all transition probabilities and all initial distributions satisfying these constraints.

## Proof
**Extremal envelope recurrence.** For each integer \(t\ge0\), let \(M_t\) and \(m_t\) be the largest and smallest probabilities of state 1 reached after an arbitrary length-\(t\) input. Both equal the initial state-1 probability at \(t=0\). Put \(U(x)=\max_{a\in\Sigma} f_a(x)\), \(L(x)=\min_{a\in\Sigma} f_a(x)\). As each \(f_a\) is strictly decreasing, both \(U\) and \(L\) are decreasing, and
\[
M_{t+1}=U(m_t),\qquad m_{t+1}=L(M_t).
\]
It follows that \(M_{t+2}=(U\circ L)(M_t)\) and \(m_{t+2}=(L\circ U)(m_t)\). Both two-step maps are nondecreasing. For any nondecreasing self-map \(F\) of an interval, its iterates from any starting point form a monotone sequence: if \(F(x)\ge x\), every later iterate is at least the preceding one; otherwise all are at most the preceding one. Consequently each parity subsequence \((M_{2j+e})_j\) and \((m_{2j+e})_j\), \(e\in\{0,1\}\), is monotone (the direction may differ).

**Strict optimality constrains every prefix.** Fix the unique maximizing word \(w=w_1\cdots w_n\). Consider its prefix of length \(t\), with \(0\le t\le n\), and hold the remaining suffix fixed. Because that suffix is a composition of \(n-t\) strictly decreasing maps, its value is strictly increasing in the prefix probability if \(n-t\) is even, and strictly decreasing otherwise. If the prefix failed to attain the unique appropriate extremum among all length-\(t\) prefixes, replacing it would create a different word of length \(n\) with acceptance at least as large. Thus the prefix probability is the *unique* \(M_t\) if \(n-t\) is even and the *unique* \(m_t\) otherwise, in the sense that no other prefix word attains that extremal value.

At each position \(t\ge1\), if \(n-t\) is even, \(w_t\) must be the unique index maximizing \(f_a(m_{t-1})\); if \(n-t\) is odd, it must be the unique index minimizing \(f_a(M_{t-1})\). If two letters tied at that input, exchanging the final letter of the length-\(t\) prefix would contradict unique optimality of \(w\).

**Monotone choice and nonrecurrent runs.** For a given letter \(a\), the strict winner region \(\{x:f_a(x)>f_b(x)\text{ for all }b\ne a\}\) is an interval, possibly empty, because every pairwise comparison of affine maps defines an open half-interval. The strict loser region \(\{x:f_a(x)<f_b(x)\text{ for all }b\ne a\}\) is likewise an interval. Restrict positions \(t\) to one parity. The same winner/loser envelope is used at all of them, and its input is a monotone sequence of the form \((m_{t-1})\) or \((M_{t-1})\) over one parity. A letter cannot be uniquely chosen, then a different letter, then the first letter again along a monotone path: the first letter's strict preference interval would contain the intermediate input. Thus each letter appears in only one constant run in each of the two parity subsequences.

**Counting.** A nonempty length-\(m\) word with no repeated letter-runs has \(r\) runs for some \(1\le r\le\min(q,m)\). Choose the \(r\) distinct run labels in \((q)_r\) ways and the positive run lengths in \(\binom{m-1}{r-1}\) ways. Summing yields \(T_q(m)\), with the unique empty word contributing \(T_q(0)=1\). Interleaving the independently chosen odd and even subsequences is bijective, so the number of words satisfying the necessary condition is their product. Since \(T_q(m)\) is a polynomial of degree at most \(q-1\) for fixed \(q\), the displayed polynomial bound follows; dividing by \(q^n\) gives exponential sparsity. \(\square\)

## Verification
The included standalone `checker.py` uses exact rational arithmetic and enumerates all words for the test alphabet sizes \(q=2,3,4\) and lengths up to \(8\) (through \(7\) for \(q=4\)). It verifies the parity-run counting formula and, for 460 independent deterministic pseudorandom choices of strictly decreasing rational transition maps, checks dynamic-program extrema against brute-force word enumeration and verifies the necessary parity-run restriction for every uniquely attaining maximizer or minimizer. These finite tests are not a substitute for the universal proof above. Reproduce with `python3 checker.py`; the expected line starts with `VERIFY_OK`.

## Relationship to prior work
Gill's *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376, Section 4, proves a stronger complete two-state classification **over binary alphabets** and establishes the affine iterated-function representation (Section 4.1). The present result concerns every alphabet size at least three and singles out the natural all-negative-determinant transition class; it does **not** assert a complete classification for arbitrary two-state PFAs with mixed determinant signs. Kjos-Hanssen's *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275 (first submitted 28 July 2026), gives a universal three-state upper bound for every finite alphabet, but does not furnish the above parity-split obstruction or counting bound for two states in the inspected paper. A separate known all-nonnegative-determinant classification concerns increasing maps, whereas this proof exploits alternating extrema and decreasing maps.

## Limitations
This is a necessity theorem and an upper bound, not a sufficient condition for realizability or a sharp enumeration. The result excludes PFAs mixing positive and negative determinants, as well as zero-determinant letter transitions. It does not determine the full ternary or larger-alphabet probabilistic automatic complexity function, and independent mathematical verification and definitive priority confirmation have not been performed. The exponent in the upper bound is not claimed optimal.

## References
1. K. Gill, *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376, https://arxiv.org/abs/2402.13376 (Section 4, affine IFS and binary two-state classification).
2. B. Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275, https://arxiv.org/abs/2607.26275 (first public version 2026-07-28).
