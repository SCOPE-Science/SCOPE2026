# An eleven-rim onset and exact energy spectrum of Kawasaki weak minima on antiferromagnetic wheels

## Finding

For every odd integer \(n\ge3\), the complete energy-resolved enumeration of weak exchange-local minima of the antiferromagnetic Ising Hamiltonian on the wheel \(W_n=K_1\vee C_n\), restricted to zero total magnetization, is the explicit polynomial \(P_n(y)\) below. A weak local minimum is a configuration for which **no exchange of opposite spins across an existing graph edge strictly lowers energy**; zero-energy exchanges are permitted. Let \(q=(n+1)/2\). With \(P_n(y)=\sum_{a\ge0}N_{n,a}y^a\), \(N_{n,a}\) counts such configurations of energy \(E_0+4Ja\), where \(E_0=J(2-n)-K\):

\[
\begin{aligned}
P_{2q-1}(y)&=2(2q-1)\left(1+\sum_{t=2}^{\lfloor(q-2)/2\rfloor} A_{q,t}y^{t-1}\right),\\
A_{q,t}&=\sum_{s=1}^{\min(t,q-2t-1)}\frac1s
\binom{q-2t-1}{s-1}\binom{t-1}{s-1}
\binom{q-t-s-2}{q-2t-s-1}.
\end{aligned}
\]

An empty sum means zero; all binomial coefficients in displayed nonempty sums have nonnegative integer arguments. The coefficient of \(y^0\) is exactly \(2n\), the number of ground configurations. Non-ground weak minima exist **if and only if** \(n\ge11\). The first examples are \(P_9(y)=18\), \(P_{11}(y)=22(1+y)\), \(P_{13}(y)=26(1+3y)\), and \(P_{15}(y)=30(1+6y+y^2)\).

The count is independent of the strength and sign of the spoke coupling and of any uniform magnetic field. Moreover, the number \(B_n=P_n(1)\) is exponentially large in the sense that
\[
\liminf_{n\to\infty\atop n\ \mathrm{odd}}\frac1n\log B_n\ge\frac{\log2}{4}>0.
\]
No exact limit or sharp entropy constant is asserted.

## Assumptions and scope

The wheel has labeled rim vertices \(1,\dots,n\) with cyclic adjacency \(i\sim i+1\), and hub \(0\) adjacent to every rim vertex. Spins \(\sigma_i\in\{-1,+1\}\). Fix \(J>0\), any real \(K\) and any real field \(h\), with energy
\[
H(\sigma)=J\sum_{i=1}^n\sigma_i\sigma_{i+1}
 +K\sigma_0\sum_{i=1}^n\sigma_i-h\sum_{i=0}^n\sigma_i,
\qquad \sigma_{n+1}=\sigma_1.
\]
Work only in the sector \(\sum_{i=0}^n\sigma_i=0\), which exists because \(n\) is odd. Exchange moves swap the spins at the endpoints of **one existing wheel edge**; arbitrary nonadjacent swaps are not allowed. Only strict energy decreases are prohibited in the definition of weak local minimum. The count refers to labeled spin configurations, not rotations or spin-flip orbits.

## Proof

**1. Field and spoke cancellation.** At zero total magnetization \(M\), \(\sum_{i=1}^n\sigma_i=-\sigma_0\). Thus the spoke term is \(-K\), and the field term vanishes, before and after every allowed exchange. Energy ordering is entirely determined by the antiferromagnetic rim term \(J\sum_i\sigma_i\sigma_{i+1}\). Global spin reversal is a bijection between hub-sign sectors, so count hub spin \(+1\) and multiply by two.

**2. Exact forbidden words.** Write the cyclic rim spins as \(+\) and \(-\), with exactly \(q\) minuses and \(q-1\) pluses. Swapping opposite rim spins at \(i,i+1\) changes energy by
\[
\Delta H=2J\sigma_i(\sigma_{i+2}-\sigma_{i-1}).
\]
The move strictly decreases energy exactly on either cyclic four-letter word \(++--\) or \(--++\), with the swapped spins at the middle two positions. Swapping the positive hub with a negative rim spin \(\sigma_i=-1\) gives
\[
\Delta H=2J(\sigma_{i-1}+\sigma_{i+1}).
\]
It decreases energy exactly when the rim has the cyclic three-letter word \(---\) centered at \(i\). Hence weak minima with positive hub are **precisely** length-\(n\) cyclic binary words with one more minus than plus and avoiding \(---,++--,--++\). This argument is valid also for \(n=3\), for which the four-letter word test is interpreted cyclically.

**3. Run structure.** Since \(---\) is forbidden, each negative run has length one or two. Let \(k\) be the number of negative runs (equal to the number of positive runs), and let \(t\) be the number of length-two negative runs. The number of negative spins is \(q=k+t\). There are \(u=k-t=q-2t\) singleton negative runs. Write the lengths of the intervening positive runs as \(1+b_1,\dots,1+b_k\) with \(b_j\ge0\). Since there are \(q-1\) positive spins,
\[
\sum_{j=1}^k b_j=t-1.
\]
The two forbidden four-letter words say exactly that \(b_j>0\) is possible only if the two neighboring negative runs are **both singleton runs**.

If \(t=1\), every \(b_j=0\), giving one double-negative run among alternating singleton runs. There are \(n\) labeled words for the positive-hub sector, hence \(2n\) ground states. If \(t\ge2\), a positive excess exists, and consequently at least two neighboring negative singleton runs exist. Therefore \(u\ge2\), so \(t\le\lfloor(q-2)/2\rfloor\); the first possible \(t=2\) has \(q=6\), i.e. \(n=11\).

**4. Circular run enumeration.** For fixed \(t\ge2\), arrange the \(t\) double-negative runs (symbol \(D\)) and the \(u\) singleton-negative runs (symbol \(S\)) cyclically in a run-word of length \(k=t+u\). If the \(S\) symbols form exactly \(s\) circular blocks, there are exactly \(g=u-s\) gaps between adjacent singleton-negative runs where a positive run may be enlarged. The count of **indexed** circular run-words with exactly \(s\) such blocks is
\[
\frac{k}{s}\binom{u-1}{s-1}\binom{t-1}{s-1}.
\]
Indeed choose positive compositions of \(u\) and \(t\) into \(s\) alternating blocks, choose a run-word starting point among \(k\) positions, and divide by the \(s\) equivalent block starting points. Requiring \(g\ge1\) and \(s\le t\) yields \(1\le s\le\min(t,u-1)\). The number of nonnegative vectors \(b\) of sum \(t-1\) on those \(g\) gaps is
\[
\binom{t+g-2}{g-1}=\binom{q-t-s-2}{q-2t-s-1}.
\]
A labeled rim word with \(k\) negative-run starts is counted \(k\) times when one of its starts is distinguished, while the distinguished starting position can be any of the \(n\) labeled rim locations. Multiply the run-word count by \(n/k\) and then by two for hub-sign reversal. This gives the displayed exact \(P_n(y)\).

**5. Energy and exponential family.** There are \(t\) equal-spin bonds inside double-negative runs and \(t-1\) equal-spin bonds inside positive runs. Thus the number of equal rim bonds is \(2t-1\); the energy is \(J(4t-n-2)-K=E_0+4J(t-1)\), verifying every exponent of \(y\).

For the exponential bound take \(q\ge8\), \(t=\lfloor q/4\rfloor\), and \(u=q-2t\ge2t\). Fix the negative run-word consisting of \(t\) repetitions of \(DSS\), followed by \(u-2t\) additional \(S\) symbols. Choose the excess \(t-1\) positive spins freely among the \(t\) distinguished \(SS\) gaps. These choices give \(\binom{2t-2}{t-1}\) pairwise distinct labeled weak minima. Stirling's formula and \(t/n\to1/8\) give the asserted lower exponential rate \(\log2/4\). The onset and every coefficient were proved without extrapolation from finite samples.

## Verification

Run \(\texttt{python3 verify.py}\) in the directory containing the standalone verifier. It computes the polynomial by the displayed finite sum; independently enumerates all balanced labeled spin assignments for odd rim sizes \(3\) through \(15\), exchanging spins on actual graph edges and recomputing the full Hamiltonian; independently counts forbidden-word cyclic paths by dynamic programming for odd sizes \(3\) through \(47\); checks the local forbidden-word equivalence for sizes through \(11\); and checks initial coefficients and the sharp onset through size \(119\). The verifier prints \(\texttt{VERIFY_OK}\) on success. It uses only Python's standard library. These are finite corroborations; the proof of the all-size formula and exponential bound is the combinatorial argument above.

## Relationship to prior work

The foundational zero-temperature Kawasaki study of De Smedt–Godrèche–Luck, arXiv:cond-mat/0210477v1 (22 October 2002), derives blocked-state statistics for a **ferromagnetic chain** and uses an energy-resolved transfer matrix. Grynberg, arXiv:1009.4511v1 (23 September 2010), studies antiferromagnetic one-dimensional Kawasaki relaxation and spectral gaps on a **pure periodic chain**. Gómez Albarracín–Rosales–Grynberg, arXiv:1601.04375v1 (18 January 2016), treats chains with first- and second-neighbor couplings, including a proliferation analysis in Appendix A. All three establish or employ methodological context but neither the wheel hub exchanges nor the zero-magnetization wheel formula, threshold and energy spectrum follow from their stated chain results. Earlier wheel one-spin-flip stability results concern a different set of allowed moves; they do not imply exchange stability.

## Limitations

The result concerns **weak** local minima under single edge exchanges and **only** the balanced sector on odd-rim wheels. In particular, zero-energy moves may exist and the theorem does **not** assert dynamically absorbing states, Arrhenius barriers, fixation probabilities, relaxation rates, or the sharp asymptotic entropy. It does not address even-rim wheels or arbitrary nonlocal Kawasaki swaps. An unindexed equivalent enumeration could affect the historical novelty assessment; priority requires independent examination.

## References

- G. De Smedt, C. Godrèche, J. M. Luck, *Metastable states of the Ising chain with Kawasaki dynamics*, arXiv:cond-mat/0210477v1, 2002-10-22. https://arxiv.org/abs/cond-mat/0210477
- M. D. Grynberg, *Revisiting Kawasaki dynamics in one dimension*, arXiv:1009.4511v1, 2010-09-23. https://arxiv.org/abs/1009.4511
- F. A. Gómez Albarracín, H. D. Rosales, M. D. Grynberg, *Metastable and scaling regimes of a one-dimensional Kawasaki dynamics*, arXiv:1601.04375v1, 2016-01-18. https://arxiv.org/abs/1601.04375
