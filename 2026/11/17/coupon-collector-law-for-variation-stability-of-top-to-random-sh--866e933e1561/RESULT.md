# Coupon-collector law for variation stability of top-to-random shuffle averages

## Finding
For integers \(n\ge2\) and \(r\ge0\), let \(S_n\) average the \(n\) permutations of a real vector obtained by removing its first entry and reinserting that entry at a uniformly selected position. On the quotient of \(\mathbb R^n\) by constant vectors, use adjacent total variation
\[
V_n(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|.
\]
For the standard coupon-collector completion time \(T_N\) on \(N\) equally likely types, the *sharp* two-input coefficient is
\[
\boxed{\sup_{V_n(x-y)>0}\frac{V_n(S_n^r x-S_n^r y)}{V_n(x-y)}
=\left(\frac{n-1}{n}\right)^r\Pr\{T_{n-1}>r\}.}
\]
Here \(T_N\) counts draws including the first; \(T_1=1\). The identity holds at \(r=0\), with both sides equal to one. At \(r\ge1\) it has the finite exact formula
\[
\frac1{n^r}\sum_{j=1}^{n-1}(-1)^{j+1}\binom{n-1}{j}(n-1-j)^r.
\]
For each fixed \(n\ge3\), the same exact formula yields the sharp far-tail law \(C_{n,r}\sim(n-1)((n-2)/n)^r\) as \(r\to\infty\), dominated by the first inclusion-exclusion term. The maximum is always attained by a signal with its only jump between positions \(n-1\) and \(n\). For \(n\ge3\), the coefficient equals \(((n-1)/n)^r\) for \(1\le r\le n-2\), and its first strict deficit is
\[
C_{n,n-1}=\left(\frac{n-1}{n}\right)^{n-1}-\frac{(n-1)!}{n^{n-1}}.
\]
If \(N=n-1\) and \(r_n=\lfloor N(\log N+t)\rfloor\) with fixed \(t\in\mathbb R\), then
\[
\boxed{\lim_{n\to\infty} nC_{n,r_n}=e^{-t}\left(1-e^{-e^{-t}}\right).}
\]
In contrast, the adjoint positional average \(R_n=S_n^{\mathsf T}\), corresponding to removing a uniformly selected position and moving its entry to the front, has one-step sharp variation coefficient \(0\) for \(n=2\), \(1\) for \(n=3\), and \(2-2/n\) for all \(n\ge4\). Thus the inverse shuffles exhibit opposite one-step variation stability beginning at four positions.

## Assumptions and scope
Signals are real, entries represent positions in a single ordered deck, each insertion or removal position has equal probability, and different shuffle steps are independent. No periodic closing edge is included in \(V_n\). The adjective *variation* refers to differences of neighboring signal entries, not total variation distance between probability distributions on permutations. The induced coefficient is a norm on the quotient by constants; the input difference can be any nonconstant real signal. \(S_n^r\) is the expected positional permutation operator after \(r\) top-to-random moves.

## Proof
**1. Reduction to step signals.** Let \(D:\mathbb R^n\to\mathbb R^{n-1}\) be \((Dx)_i=x_{i+1}-x_i\), and let \(h^{(k)}_i=\mathbf1_{\{i>k\}}\) for \(1\le k<n\). Every signal is a constant plus \(\sum_{k=1}^{n-1}(Dx)_k h^{(k)}\), so for any constant-preserving linear map \(A\), \(\|A\|_{V\to V}=\max_k V_n(Ah^{(k)})\).

**2. Explicit gradient matrix.** Directly counting the \(n\) insertion positions gives
\[
(S_nx)_j=\frac{x_1+(n-j)x_{j+1}+(j-1)x_j}{n}\quad(1\le j<n),
\qquad(S_nx)_n=\frac{x_1+(n-1)x_n}{n}.
\]
Writing \(D S_n=B_n D\), the only nonzero entries of \(B_n\) are
\[
(B_n)_{j,j}=\frac{j-1}{n}\quad(1\le j<n),\qquad
(B_n)_{j-1,j}=\frac{n-j}{n}\quad(2\le j<n).
\]
This matrix is nonnegative. Its first column is zero; all other columns sum to \(q_n=(n-1)/n\). Therefore \(\|S_n^r\|_{V\to V}\) is the maximum column sum of \(B_n^r\).

**3. The last column is sharp.** Write \(B_n=q_nK_n\). Regard \(K_n\) as a substochastic transition kernel on states \(1,\ldots,n-1\), with state \(1\) killed at the next step. From state \(j\ge2\), it stays at \(j\) with probability \((j-1)/(n-1)\), and moves to \(j-1\) with probability \((n-j)/(n-1)\). The transitions admit a monotone coupling: draw a common uniform integer in \(\{1,\ldots,n-1\}\), stay from state \(j\) when that integer is at most \(j-1\), and otherwise move down one. A chain started at a larger state never lies below one started at a smaller state, with the cemetery state treated as zero. Consequently survival probabilities (column sums of powers of \(K_n\)) are greatest starting at \(n-1\). Since \(B_n\) is nonnegative, the last-jump signal attains the variation norm.

**4. Coupon collector identity.** Starting from state \(n-1\), the successive waiting times to move \(n-1\to n-2\to\cdots\to1\) are independent geometric random variables, supported on positive integers, with success probabilities \(1/(n-1),2/(n-1),\ldots,(n-2)/(n-1)\). Their sum \(H\) has the law of \(T_{n-1}-1\): the usual coupon collector has exactly these geometric stage times in reverse order after its first draw. A chain is alive after \(r\) transitions exactly when \(H\ge r\), i.e. \(T_{n-1}>r\). Multiplication by \(q_n^r\) proves the boxed formula, including \(n=2\) where every positive-step coefficient vanishes. Inclusion-exclusion gives the finite sum for \(r\ge1\). For \(r\le n-2\) the collector cannot have completed all \(n-1\) types after only \(r\) draws. At \(r=n-1\), completion occurs only when all draws have distinct types, with probability \((n-1)!/(n-1)^{n-1}\), giving the first deficit.

**5. Critical-window limit.** At \(r_n=\lfloor N(\log N+t)\rfloor\), let \(U_N\) be the number of coupon types not yet seen. For each fixed integer \(k\ge1\),
\[
\mathbb E[(U_N)_k]=(N)_k\left(1-\frac{k}{N}\right)^{r_n}\longrightarrow e^{-kt}.
\]
These are the factorial moments of a Poisson random variable of mean \(e^{-t}\), so \(\Pr\{U_N>0\}\to1-\exp(-e^{-t})\). Also \(n(N/n)^{r_n}\to e^{-t}\), proving the critical-window formula.

**6. Reverse shuffle.** Since each top-to-random insertion permutation is inverted by the matching move-to-front permutation, averaging shows \(R_n=S_n^{\mathsf T}\). For a single-jump input \(h^{(k)}\), the move-to-front output has first entry \((n-k)/n\), entries \(2,\ldots,k\) equal to zero, the entry at \(k+1\) equal to \(k/n\), and all subsequent entries equal to one (with empty ranges omitted). Its variation equals \(1\) at \(k=n-1\), equals \(2-k/n\) for \(2\le k\le n-2\), and equals \(2-3/n\) at \(k=1\) when \(n\ge3\); direct evaluation handles \(n=2\). The maximum is as claimed. These are attained by actual step inputs.

## Verification
The standalone `verify.py` uses exact rational arithmetic. It independently constructs each shuffle average from all insertion permutations, checks the transpose relation, raises each averaging matrix to powers through \(r=25\) for \(2\le n\le11\), computes its variation norm by step-input enumeration, and compares it with both a coupon-collector occupancy recursion and the inclusion-exclusion sum. It additionally checks the first-deficit identity and the reverse one-step formula. The infinite claims follow from the proof above, not these finite tests.

## Relationship to prior work
Classical work on top-to-random and random-to-top card shuffling establishes mixing laws and coupon-collector representations for the full permutation process. In particular, Diaconis, Fill and Pitman describe top-to-random distributions, while Jonasson studies random-to-top and discusses the classical coupon collector mixing time. The present object is instead the induced operator norm on the ordered-signal quotient equipped with adjacent variation. Its exact finite-time equality to a *coupon noncompletion probability*, the exceptional first-deficit horizon, the critical-window norm profile and the adjoint variation contrast do not follow directly from the previously inspected mixing-time statements without the new gradient-operator reduction. An inaccessible full-text historical source remains a priority risk.

## Limitations
No analogous exact formula is claimed for biased insertion positions, periodic variation, nonlinear signal filters, operator norms on full permutation-state distributions, or other finite-deck statistics. The previous literature's total-variation *mixing distance* must not be confused with adjacent-signal variation. Historical priority is not independently certified.

## References
- Johan Jonasson, *Biased random-to-top shuffling*, arXiv:math/0607124v1, July 5, 2006, https://arxiv.org/abs/math/0607124 (full text inspected, especially introduction and section 2).
- Persi Diaconis, James Allen Fill and Jim Pitman, *Analysis of Top To Random Shuffles*, Combinatorics, Probability and Computing 1 (1992), 135–155, https://doi.org/10.1017/S0963548300000158 (publisher abstract and bibliographic material inspected; full text not accessible in this run).
- David Aldous and Persi Diaconis, *Shuffling Cards and Stopping Times*, American Mathematical Monthly 93 (1986), 333–348, https://doi.org/10.2307/2323590 (historical contextual reference, not used as a proof source).
