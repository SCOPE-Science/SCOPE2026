# Optimal words of orientation-preserving two-state probabilistic automata

## Finding

Fix a finite alphabet \(\Sigma\) of size \(q\geq2\). A two-state probabilistic finite automaton has a row-stochastic transition matrix \(P_a\) for each letter \(a\in\Sigma\), an initial probability row vector, and a nonconstant Boolean final-state indicator. Call it *orientation-preserving* if \(\det P_a\geq0\) for every letter.

**Theorem.** A nonempty word \(w\in\Sigma^n\) is the unique most-probably accepted word of length \(n\) for some orientation-preserving two-state probabilistic automaton if and only if each letter of \(\Sigma\) occurs in at most one contiguous run of \(w\). Every word satisfying the condition has a witness with strictly positive transition determinants, rational transition probabilities, a deterministic initial state, and precisely one accepting state. For a word of length \(n\) with \(r\) runs, every transition probability in the supplied witness has denominator dividing \(r2^{2n+5}\), so its rational description has \(O(n+\log r)\) bits per entry.

Consequently the number of such words of length \(n\geq1\) is exactly
\[
N_q(n)=\sum_{r=1}^{\min(q,n)}\frac{q!}{(q-r)!}\binom{n-1}{r-1},
\]
and its ordinary generating function is
\[
\sum_{n\geq1}N_q(n)z^n
=\sum_{r=1}^{q}\frac{q!}{(q-r)!}\left(\frac{z}{1-z}\right)^r.
\]
For fixed \(q\), this is a polynomial-growth class, with \(N_q(n)\sim q n^{q-1}\). These statements classify this **restricted witness model**, not unrestricted two-state probabilistic automatic complexity.

## Assumptions and scope

Inputs are finite words read left to right. The probability of accepting \(w=a_1\cdots a_n\) is \(\pi P_{a_1}\cdots P_{a_n}\eta\), with \(\eta\in\{0,1\}^2\). A unique winner means strictly greater acceptance probability than every other word of exactly length \(n\) over the full alphabet \(\Sigma\). The assumptions \(q\geq2\) and \(n\geq1\) are essential to the enumerative statement and the exclusion of trivial one-state witnesses. A run is a maximal nonempty contiguous block of identical letters; a run-distinct word never revisits a letter after leaving its run.

Relabel states so that the accepting state is state one, and write \(x\in[0,1]\) for its probability. A transition acts as an affine map
\[
f_a(x)=\alpha_a x+\beta_a,\qquad
P_a=\begin{pmatrix}\alpha_a+\beta_a&1-\alpha_a-\beta_a\\\beta_a&1-\beta_a\end{pmatrix}.
\]
Stochasticity means \(0\leq\beta_a\leq1\) and \(0\leq\alpha_a+\beta_a\leq1\), while \(\det P_a=\alpha_a\). Thus orientation preservation means each \(f_a\) is nondecreasing.

## Proof

**Necessity.** Put \(G(x)=\max_{a\in\Sigma}f_a(x)\). Since the maps are nondecreasing, \(G\) is nondecreasing, and the maximum reachable acceptance probability among length-\(t\) words obeys
\[
x_0=\pi_1,\qquad x_t=G(x_{t-1}).
\]
The sequence \((x_t)\) is monotone: if \(x_1\geq x_0\), then \(x_{t+1}\geq x_t\) for all \(t\), and similarly when \(x_1\leq x_0\). In particular, the sequence never reverses direction.

If a length-\(n\) word is a unique winner, then at each step its chosen letter must be the unique maximizer of \(f_a(x_{t-1})\) over \(a\). Indeed, any tied letter could replace the chosen letter while keeping an optimal prefix, producing a different word with the same maximal probability at length \(t\). Such a tie cannot later be removed while preserving uniqueness: applying a common suffix to two probability-equal words gives equal probabilities. In addition, the winning word must use an optimal prefix at every length: replacing a nonoptimal prefix by an optimal one improves the terminal value if the remaining affine composition has positive slope, and if that composition has zero slope then all same-length prefixes tie at the end. Either outcome contradicts uniqueness. Thus each letter of the winning word is uniquely active on the upper envelope at the corresponding \(x_{t-1}\).

Suppose some letter \(a\) occurred in two separated runs with a different letter \(b\) between them. At three chronologically ordered orbit points, the affine difference \(f_a-f_b\) would have strictly positive, strictly negative, and strictly positive values. This is impossible for an affine function evaluated along a monotone sequence of real points. Hence a winning word is run-distinct.

**Sufficiency: explicit rational construction.** Write a run-distinct word as
\[
w=a_1^{m_1}a_2^{m_2}\cdots a_r^{m_r},\qquad
m_i\geq1,\quad r\leq q,
\]
with pairwise different \(a_i\), and let \(T_i=m_1+\cdots+m_i\) for \(1\leq i<r\). Use the baseline map \(f(x)=x/2+1/4\) with orbit from zero
\[
\xi_t=\frac{1-2^{-t}}2,\qquad t\geq0.
\]
Choose increasing thresholds \(c_i=(\xi_{T_i-1}+\xi_{T_i})/2\), and let
\[
\varepsilon=\frac{2^{-(n+4)}}r,
\qquad f_{a_i}(x)=\left(\frac12+(i-1)\varepsilon\right)x
+\frac14-\varepsilon\sum_{j<i}c_j.
\]
Assign every unused letter the map \(f_a(x)=x/2\). Each displayed map takes \([0,1]\) into itself, has positive slope, and therefore corresponds to an orientation-preserving stochastic transition matrix via the formula above. Indeed, all used slopes lie in \([1/2,17/32)\), while all their intercepts lie in \((7/32,1/4]\) and their slope-plus-intercept values lie below \(25/32\). Unused maps are strictly dominated by \(f_{a_1}\) on \([0,1]\).

Adjacent constructed lines satisfy
\[
f_{a_{i+1}}(x)-f_{a_i}(x)=\varepsilon(x-c_i).
\]
Since \(c_1<\cdots<c_{r-1}\), the upper envelope \(G\) uses \(f_{a_i}\) *uniquely* on the interval between \(c_{i-1}\) and \(c_i\), with the obvious unbounded endpoint intervals. To see this for nonadjacent lines, telescope the displayed difference; every summand then has the requisite strict sign.

Each used map differs from the baseline \(f\) by less than \(2r\varepsilon\) uniformly on \([0,1]\). Therefore, if \(y_0=0\), \(y_{t+1}=G(y_t)\), then
\[
|y_t-\xi_t|<4r\varepsilon=2^{-(n+2)}\qquad(t\geq1),
\]
by the contraction ratio \(1/2\) of \(f\). Every \(\xi_{t-1}\) for \(1\leq t\leq n\) is separated from every threshold by at least \(2^{-(n+1)}\): each threshold lies strictly between two consecutive baseline orbit positions at a run boundary, and its distance from either endpoint is \(2^{-(T_i+2)}\geq2^{-(n+1)}\). The perturbation cannot change which upper-envelope region contains each orbit point. Thus \(f_{a_i}\) is the *unique* maximizing transition on precisely the consecutive steps belonging to the run \(a_i^{m_i}\).

Finally, the chosen transitions are strictly increasing. Induction in \(t\) therefore shows that the unique maximizing path to \(y_t\) is exactly the length-\(t\) prefix of \(w\). Taking the initial distribution \((0,1)\), accepting indicator \((1,0)^T\), and the stochastic matrices associated to the constructed maps proves sufficiency. As \(c_i=1/2-3\cdot2^{-(T_i+2)}\) and \(T_i\leq n-1\), all thresholds have dyadic denominator dividing \(2^{n+1}\). The displayed rational formula therefore makes every transition entry have denominator dividing \(r2^{2n+5}\), proving the stated bit-size bound.

**Counting.** If a word has \(r\) runs with distinct letters, its ordered letters can be selected in \(q!/(q-r)!\) ways. The positive run lengths summing to \(n\) can be chosen in \(\binom{n-1}{r-1}\) ways. Summation yields the formula; summing the composition generating series \((z/(1-z))^r\) yields the rational generating function. The largest-degree term is the \(r=q\) term, of leading coefficient \(q\).

## Verification

The accompanying `checker.py` constructs all rational maps and their stochastic matrices using Python's exact `fractions.Fraction`. For alphabet sizes \(2,3\) and lengths \(1\) through \(5\), and alphabet size \(4\) and lengths \(1\) through \(4\), it checks every run-distinct word against **every** same-length competitor by exact rational arithmetic. It also checks the five-distinct-symbol example \(0011234\) over five letters, compares the affine iteration to direct matrix multiplication, and tests the necessity direction on a separate grid of positive-slope transition maps. The recorded output reports 374 successful exhaustive witness checks plus a grid sanity check.

This finite verification is independent corroboration of the concrete construction at these parameters; the arbitrary-alphabet theorem follows from the proof above rather than extrapolation.

## Relationship to prior work

Kenneth Gill introduced probabilistic automatic complexity and completely classified binary strings having unrestricted two-state witnesses, including alternating patterns that need not be run-distinct. His full paper's Section 4.4 treats extension of binary witnesses to larger alphabets but does not classify multi-letter words witnessed by orientation-preserving two-state transitions. Bjørn Kjos-Hanssen proved that three states suffice for every finite word and, in Section 5 of the 2026 paper, identified the general classification of two-state witnesses on alphabets of three or more letters as unresolved. The theorem here supplies an exact, proper subcase distinguished by nonnegative transition determinants; it does not resolve the unrestricted multi-letter problem.

## Limitations

If some transition determinants are negative, the letterwise affine maps may reverse order, so the monotone-envelope argument no longer applies; words with revisited letters can then be unique winners. The theorem makes no classification claim for those automata, higher-state PFAs, empty words, or the unary alphabet. Published binary classifications and arbitrary-alphabet three-state upper bounds are not claimed as new. Earlier unindexed work concerning monotone affine iterated systems may contain equivalent statements; no historical uniqueness is asserted. No independent audit has been performed.

## References

1. Kenneth Gill, *Probabilistic automatic complexity of finite strings*, arXiv:2402.13376 (first submitted 2024-02-20), especially Theorem 4.1, Proposition 4.10, and Section 4.4. Author-hosted full text: https://nowheredense.github.io/PFAcomplexity.pdf.
2. Bjørn Kjos-Hanssen, *Every string has probabilistic automatic complexity at most three*, arXiv:2607.26275v1 (first submitted 2026-07-28), especially Sections 1, 4, and 5. Full text: https://arxiv.org/html/2607.26275.
