# Exact least-significant-first state complexity of shifted binary digit-sum words

## Finding

Let \(s_2(n)\) be the number of ones in the binary expansion of the nonnegative integer \(n\). For every integer \(m\ge 2\), define the generalized Thue–Morse word \(t_m(n)=s_2(n)\bmod m\). For every shift \(c\ge0\), the exact size of the binary \(2\)-kernel of \(n\mapsto t_m(n+c)\), and hence the exact number of states in its minimal binary least-significant-digit-first deterministic finite automaton with output (DFAO), is the cardinality of the explicit finite set \(\mathcal Q_{m,c}\) below.

For \(c=0\), put \(\mathcal Q_{m,0}=\{(0,b):0\le b<m\}\). For \(c\ge1\), put \(L=1+\lfloor\log_2 c\rfloor\), and for each \(0\le e<L\), let
\[
q_e=\left\lfloor\frac c{2^e}\right\rfloor,\qquad
u_e=c\bmod2^e,\qquad
d_e=\min_{\nu_e\le z<2^e}s_2(z),\qquad
h_e=\max_{0\le z<\nu_e}s_2(z).
\]
The maximum of the empty set is understood here and below to be \(-1\). Set \(H(c)=\max_{0\le z<c}s_2(z)\). For any nonnegative integers \(a,j\), let \([a,j]_m\) indicate the state \((a,j\bmod m)\). Then
\[
\begin{aligned}
\mathcal Q_{m,c}={}&\{(0,b):0\le b<m\}
\cup\{[1,j]_m:0\le j\le H(c)\}\\
&\cup\bigcup_{e=0}^{L-1}\left(
\{[q_e,j]_m:d_e\le j\le e\}
\cup\{[q_e+1,j]_m:0\le j\le h_e\}
\right).
\end{aligned}
\]
Each union is a *set union*: identical states reached at different digit depths are counted once. In particular,
\[
\boxed{\operatorname{sc}_{\mathrm{LSD}}(t_m(\cdot+c))=|\mathcal Q_{m,c}|.}
\]

For the natural family of power-of-two shifts, this specializes to the closed formula, for every \(m\ge2\) and \(k\ge0\),
\[
\boxed{\operatorname{sc}_{\mathrm{LSD}}(t_m(\cdot+2^k))
=m+\sum_{j=1}^{k+1}\min(m,j).}
\]
Thus the usual binary Thue–Morse word (\(m=2\)) shifted by \(2^k\) requires exactly \(2k+3\) states, whereas when \(m\ge k+1\) the answer is \(m+(k+1)(k+2)/2\).

## Assumptions and scope

Integers \(c,n,e,k\) are nonnegative and the output modulus satisfies \(m\ge2\). An LSD-first input word \(w=d_0d_1\cdots d_{e-1}\) represents \(\sum_{i=0}^{e-1}d_i2^i\). Arbitrary trailing zero digits must preserve output, and the empty word represents zero. State complexity is the minimum number of reachable states in a *complete* DFAO satisfying this requirement on every finite binary input. The binary \(2\)-kernel consists of all sequences \(n\mapsto t_m(2^en+r+c)\) with \(e\ge0\) and \(0\le r<2^e\).

The maxima and minima in the formula can be evaluated from the \(e\) low bits of \(c\); no exponential interval scan is needed. Specifically for \(0\le t<2^e\), define \(d(t,e)=\min_{t\le z<2^e}s_2(z)\) and \(h(t,e)=\max_{0\le z<t}s_2(z)\), with \(h(0,e)=-1\). If \(t_i\in\{0,1\}\) is its bit in position \(i\), then
\[
\begin{aligned}
d(t,e)&=\min\left(s_2(t),\ \min_{0\le i<e,\ t_i=0}\big(s_2(\lfloor t/2^{i+1}\rfloor)+1\big)\right),\\
h(t,e)&=\max_{0\le i<e,\ t_i=1}\big(s_2(\lfloor t/2^{i+1}\rfloor)+i\big).
\end{aligned}
\]
Empty inner minima are omitted. The displayed state family is consequently computable by polynomially many operations on the binary digits of \(c\), plus generation of the \(m\) output phases.

## Proof

**Residual identity.** For \(a\ge0\) and \(b\in\mathbb Z/m\mathbb Z\), write \(F_{a,b}(n)=s_2(n+a)+b\bmod m\). After a finite LSD-first input of length \(e\) representing \(r\), the residual function of the shifted digit-sum word is
\[
n\longmapsto t_m(2^e n+r+c)=F_{a,b}(n),
\quad a=\left\lfloor\frac{r+c}{2^e}\right\rfloor,
\quad b=s_2((r+c)\bmod2^e)\bmod m.
\]
This follows by splitting the binary expansion of \(2^e n+r+c\) at position \(e\): there are no carries across the split once its Euclidean quotient and remainder have been taken. For \(e=0\), the state is \((c,0)\).

**All distinct parameters give distinct residual functions.** If \(a=a'\) but \(b\ne b'\), the two residual functions differ for every \(n\). If \(a<a'\), put \(\Delta=a'-a>0\), choose any sufficiently large integer \(h\), and take \(n=2^h-a'\ge0\). Then
\[
s_2(n+a')=1,\qquad s_2(n+a)=s_2(2^h-\Delta)=h-s_2(\Delta-1).
\]
The difference of the digit sums changes by exactly one as \(h\) increases by one, so cannot be constant modulo \(m\ge2\). No fixed choice of phases \(b,b'\) makes \(F_{a,b}=F_{a',b'}\). By symmetry, all unequal pairs are distinguishable. Thus counting distinct reachable pairs is simultaneously counting distinct kernel sequences and minimizing the DFAO.

**Reachability at bounded depth.** Fix \(e\ge0\), write \(c=q2^e+t\) where \(0\le t<2^e\), and vary \(r\) through \([0,2^e)\). If \(0\le r<2^e-t\), the residual quotient is \(q\) and remainder \(t+r\) ranges over \([t,2^e)\). Otherwise the quotient is \(q+1\) and the remainder ranges over \([0,t)\). For fixed \(t\), the set of binary digit sums in the first interval is exactly the full integer interval \([d(t,e),e]\): from a minimum-weight integer \(z\ge t\), change any of its zero bits to one, one at a time, retaining the inequality \(z\ge t\) and raising the weight by one to \(e\). Likewise, sums on \([0,t)\) are precisely \([0,h(t,e)]\): start at a maximum-weight integer and change one bits to zero, remaining below \(t\) throughout. This proves the two finite-depth state families in the theorem.

For \(0\le e<L\), these are exactly the families involving \(q_e,d_e,h_e\). For all \(e\ge L\), we have \(q=0\) and \(t=c\). The states with quotient one are exactly \([1,j]_m\) for \(0\le j\le H(c)\). The states with quotient zero collectively realize **every** phase \((0,b)\): choose any sufficiently large \(j\equiv b\pmod m\) and then an \(e\) so large that \(2^j-1\ge c\) and \(j\le e\). The remainder \(z=2^j-1\) lies in \([c,2^e)\) and has digit sum \(j\). This proves that the displayed set \(\mathcal Q_{m,c}\) comprises all and only reachable pairs, with all phases of quotient zero accounted for. If \(c=0\), every residual quotient is zero and every phase is reached, giving exactly \(m\) states.

**Minimal automaton.** On the reachable pairs take initial state \((c,0)\), transition and output
\[
\delta((a,b),d)=\left(\left\lfloor\frac{a+d}{2}\right\rfloor,\ b+(a+d\bmod2)\pmod m\right),\quad
\tau(a,b)=s_2(a)+b\pmod m,
\quad d\in\{0,1\}.
\]
The residual identity proves correctness on all words, and \(\tau(\delta((a,b),0))=\tau(a,b)\) follows from \(s_2(a)=s_2(\lfloor a/2\rfloor)+(a\bmod2)\). Thus zero padding is respected, and minimality follows from distinguishability above.

**The power-of-two specialization.** If \(c=2^k\), the depths \(0\le e\le k\) have \(t=0\), quotient \(2^{k-e}\), and all digit-sum phases \(0,1,\ldots,e\) modulo \(m\). These \(k+1\) quotients are distinct. At greater depths, quotient zero supplies all \(m\) phases and quotient one supplies only phases already present at \(e=k\). Hence the total count is \(m+\sum_{e=0}^{k}\min(m,e+1)\), as asserted.

**Bit formulas for interval extrema.** If \(z<t\), let \(i\) be the highest differing bit: at that bit \(t_i=1\), the upper digits agree with \(t\), and the largest possible weight below is obtained by putting ones in all \(i\) lower positions, giving \(s_2(\lfloor t/2^{i+1}\rfloor)+i\). If \(z\ge t\), either \(z=t\) or its highest differing bit has \(t_i=0\); the least weight above is attained by putting a one at that position and zeros below, giving \(s_2(\lfloor t/2^{i+1}\rfloor)+1\). Taking extrema proves the digit formulas.

## Verification

Run `python3 check.py` with Python 3.10 or later. The checker independently constructs the entire reachable pair automaton via breadth-first search; applies Moore partition refinement without assuming irredundancy; compares the resulting minimized state count with the set formula for 903 shift/modulus pairs; independently enumerates all bit-interval weights for 2,047 cases; checks 96 power-of-two specialization cases; and checks 30,600 directly calculated residuals at eleven further arguments each. The observed result was four PASS lines, with no assertion failures. These finite checks corroborate, but do not replace, the infinite argument above.

## Relationship to prior work

Moradi, Rampersad and Shallit (arXiv:2512.10017v1, December 10, 2025) study automaton complexity for linear subsequences and shifted Thue–Morse sequences. Their Theorem 20 gives an upper bound linear in the shift for a most-significant-digit-first construction; their discussion of least-significant-digit-first input cites generic kernel and addition constructions. Neither inspected result gives this exact LSD-first state count for all shifts and all output moduli. Zantema and Bosma (2022) give generic bounds for automatic sequence shifts and a three-state example for the binary Thue–Morse word shifted by one, which agrees with the specialization here but does not imply the full classification. Moradi, Popoli, Shallit and Vukusic (arXiv:2603.18858v1, March 19, 2026) examine shifts of the Fibonacci word in Zeckendorf numeration, a different sequence and numeral system. Charlier, Cisternino and Massuir (2021) characterize minimal automata recognizing integer sets of the form \(u\mathcal T+r\), where \(\mathcal T\) is the even-binary-digit-sum set, rather than the precomposition \(n\mapsto t_m(n+c)\); that result is not an equivalent shift statement.

## Limitations

This is an exact result for **binary LSD-first** DFAOs computing binary digit sums modulo \(m\ge2\), with arbitrary redundant zero padding. It makes no claim for most-significant-digit-first state complexity, nonbinary numeration, arbitrary automatic sequences or affine slopes other than one. Comparisons of prior literature reduce but cannot eliminate the possibility of an earlier unindexed exact equivalence. Independent mathematical validation has not been performed.

## References

1. D. Moradi, N. Rampersad and J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017v1 (December 10, 2025), https://arxiv.org/html/2512.10017v1.
2. H. Zantema and W. Bosma, *Complexity of Automatic Sequences*, Information and Computation 288 (2022), article 104710, https://doi.org/10.1016/j.ic.2021.104710.
3. D. Moradi, P. Popoli, J. Shallit and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858v1 (March 19, 2026), https://arxiv.org/html/2603.18858v1.
4. É. Charlier, C. Cisternino and A. Massuir, *Minimal Automaton for Multiplying and Translating the Thue-Morse Set*, Electronic Journal of Combinatorics 28(3) (2021), P3.12, https://doi.org/10.37236/9068.
