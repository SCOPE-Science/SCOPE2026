# The signed periodic-closing law for uniform words of a mixing Markov shift

## Finding

Let \(B\) be a finite primitive zero-one adjacency matrix of Perron root \(\lambda>1\). Choose \(W_n\) uniformly from its admissible length-\(n\) words. Let \(\eta(w)\) be the shortest least period of a periodic sequence beginning with \(w\), and set \(D_n=n-\eta(W_n)\).

The **signed** variable \(D_n\) converges in total variation at an exponential rate to \(D_B\), described below by two independent Perron boundary chains. The limit has a bounded negative part and an exponentially decreasing positive tail. Expectations of fixed polynomials in \(D_n\) converge exponentially. In particular the previously bounded mean correction and variance have actual limits: \(\mathbb E\eta(W_n)=n-\mathbb E D_B+o(1)\) and \(\operatorname{Var}\eta(W_n)\to\operatorname{Var}D_B\).

Negative mass need not vanish. For
\[
B=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix},
\]
the fraction of cylinders with \(\eta=n+1\) converges exponentially, and its limit lies in \([1/12,1/3]\).

## Assumptions and scope

An admissible word \(w_0\ldots w_{n-1}\) follows the directed edges \(B_{w_i,w_{i+1}}=1\). A cylinder prescribes these first \(n\) symbols of a one-sided sequence. The probability is uniform on the finite language, not the stationary Parry measure. A nonempty proper border of length \(k\) is equality of the prefix and suffix of that length, \(1\le k<n\). Write \(L(w)\) for the largest such length, or zero. For symbols \(j,i\), let \(d_B(j,i)\) be their shortest directed path length in **positive** edges; in particular \(d_B(i,i)\) is a shortest nonempty return. The result is for the canonical cylinder generator, not a supremum over generators or an assertion about general sofic or nonmixing shifts.

## Proof

### Exact closing and a uniform tail

A nonempty border of length \(k\) makes \(p=n-k\) a combinatorial period. The first \(p\) letters repeat to extend the word; the closing edge from position \(p-1\) to position \(0\) occurs inside the word because \(w_p=w_0\). Conversely a periodic extension of period \(p<n\) forces a border of length \(n-p\). If there is no border, the return path from the last symbol to the first must complete the prescribed \(n-1\) edges, and a shortest positive such path realizes the optimum, with no smaller least period possible. Hence
\[
n-\eta(w)=\begin{cases}L(w),&L(w)>0,\\1-d_B(w_{n-1},w_0),&L(w)=0.\end{cases}
\]
This includes a single-letter word and distinguishes a loop from a zero-length path. The directed return lengths have a finite uniform bound.

Write \(N_n=\mathbf1^TB^{n-1}\mathbf1\). Perron–Frobenius gives \(c\lambda^n\le N_n\le C\lambda^n\). The event of a border of length \(k\) is equivalent to a labeled closed walk of length \(p=n-k\) with a specified starting position, by repeating its first \(p\) symbols. Its exact count is \(\operatorname{tr}(B^{n-k})\), the individual shorter-period summand in [1]. It is also at most \(N_{n-k}\), since the initial block determines the word. Uniformly over \(n\), we obtain \(\Pr(L(W_n)\ge k)\le C_B\lambda^{-k}\) by summing the resulting geometric upper bounds. In particular overlapping borders cause no failure of this estimate. For a fixed \(k\), the trace ratio converges to \(\lambda^{1-k}\langle\ell,r\rangle/((\sum_i\ell_i)(\sum_i r_i))\), where \(\ell,r\) are positive left and right Perron vectors. The earlier summed trace formula therefore gives limiting expected border count \(\lambda\langle\ell,r\rangle/((\lambda-1)(\sum_i\ell_i)(\sum_i r_i))\). These are consequences of the trace counts and are not new contributions claimed here.

### Independent boundary law and quantitative truncation

For a forward infinite string \(U\) read from position zero, assign each admissible initial word \(u\) of length \(s\) probability
\[
\nu_+([u])=\frac{r_{u_{s-1}}}{\lambda^{s-1}\sum_a r_a}.
\]
Independently take a backward string \(V\), indexed with its last position at zero, with probability of a chronologically written terminal word \(v\) given by
\[
\nu_-([v])=\frac{\ell_{v_0}}{\lambda^{s-1}\sum_a\ell_a}.
\]
The eigenvector equations give consistency under adding one symbol at the free end of either block. A matching length is equality of the first \(k\) symbols of \(U\) and the last \(k\) of \(V\) in chronological order. If \(L_\infty\) is the largest matching length, with zero for no matches, define \(D_B=L_\infty\) when positive and \(D_B=1-d_B(V_0,U_0)\) otherwise.

For disjoint word ends of length \(s\), the probability of the pair \((u,v)\) is \((B^{n-2s+1})_{u_{s-1},v_0}/N_n\). The normalized Perron limit of the bridge matrix is the strictly positive matrix \(r\ell^T/\langle\ell,r\rangle\); its error is exponential in the bridge length. Since there are only finitely many matrix indices and the Perron entries are bounded away from zero for fixed \(B\), this is a **uniform relative** error versus the independent boundary pair probabilities. The normalization \(N_n\) has relative error exponentially small in \(n\) as well. Thus the sum over all admissible pairs is bounded in total variation by \(O_B(\theta^{n-2s})\) for some \(\theta<1\), even when the block length grows. For each fixed \(k\) the limiting boundary-match event therefore has the finite-word border limit as its probability; their geometric tail sum gives \(\Pr(L_\infty\ge k)=O_B(\lambda^{-k})\). In particular the maximum is finite almost surely.

Truncate the tests to lengths at most \(s=\lfloor n/3\rfloor\) for \(n\ge3\), using the same return rule if no test matches. The limit and finite-word laws each differ from their own truncation with probability \(O_B(\lambda^{-s})\). The two truncated laws differ in total variation at most by the boundary-pair bound. This proves the exponential total variation statement. To compare any fixed polynomial expectations, restrict first to the fixed bounded negative range and positive values at most \(s\), where total variation times \(O((1+s)^d)\) controls a degree-\(d\) polynomial. The discarded part for either law is bounded by a polynomial times a geometric tail by the estimates just proved. Absorbing polynomial factors into a slightly slower exponential establishes the moment statements.

### A directed closing penalty

The displayed matrix has Perron root two, and both Perron vectors may be taken all ones. Under independent boundaries the first and last symbols are independent uniform symbols. Exactly when the terminal symbol is one directed advance past the initial symbol (modulo three), the shortest positive return takes two steps. This endpoint event has probability \(1/3\); the desired event additionally requires no border. A length-one match cannot occur on that endpoint event. The sum of limiting match probabilities over lengths at least two is \(\sum_{k\ge2}1/(3\cdot2^{k-1})=1/3\). The length-two match of a constant block is disjoint from the endpoint event; its boundary probability is \(3(1/6)^2=1/12\). Subtract it from the union bound for the excluded matches. What remains is at most \(1/3-1/12\), leaving probability at least \(1/12\) and at most \(1/3\) for the closing penalty. The signed total variation law gives exponential convergence of this event's finite-word frequency.

## Relationship to prior work

The earlier finite-state closure theorem [1, Finding and proof] already treats uniform admissible words on a larger class of irreducible graphs. It gives entropy-rate tail bounds for the nonnegative truncated deficit, exponential-moment thresholds, \(\mathbb E\eta=n+O(1)\), bounded variance and the stated trace sum for the expected count of shorter periods. In the primitive setting Perron–Frobenius gives the border incidences and their expected sum from those counts; the canonical normalized mean and variance limits also follow from these bounds and language growth. The refinement here is the full signed *distributional* limit and its exponential convergence, with the directed negative mass witness. Expected border counts alone do not encode overlaps of simultaneous proper borders or their interaction with the two endpoints.

Pannipitiya [2, Proposition 2.27 and §4.2] gives a deterministic closure upper bound for mixing finite-type shifts and canonical full-shift statistics. Holub–Shallit [3, §§2–3] prove exponential longest-border probability convergence for the unrestricted uniform alphabet; that case is not a new law here. The golden-mean analyses [4, 5] count unbordered admissible words, which in that shift for \(n\ge2\) are exactly the words with \(\eta=n\); their more specific enumerations are neither claimed here nor evidence for the negative atom on a different directed matrix.

## Verification and limitations

The finite package checker `check.py` illustrates the closing dichotomy and border counts on two small matrices, not the infinite limit. Exponential convergence and the directed lower bound follow from the bridge, tail and union-bound arguments. The analysis does not provide an elementary mass formula for general \(B\), and the bibliographic comparison does not rule out unindexed prior Markov-language work.

## References

1. *Entropy-sharp periodic cylinder closure and parity-oscillating subsequences*, Resultary record 22e18f2d92a1 (2026-11-17), https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-entropy-sharp-periodic-cylinder-closure-and-parity-oscillating-s--22e18f2d92a1 .
2. D. N. Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, https://arxiv.org/abs/2611.13416v1 .
3. Š. Holub and J. Shallit, *Periods and Borders of Random Words*, https://arxiv.org/abs/1509.05240v1 .
4. Golden-mean periodic cylinders, Resultary record ce7ef1cd5963 (2026-11-22), https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-golden-mean-periodic-cylinders-a-mahler-law-and-a-sharp-parity-s--ce7ef1cd5963 .
5. Weight-refined border-free spectrum for Fibonacci-admissible words, Resultary record 491b08dec094 (2026-11-22), https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-weight-refined-border-free-spectrum-for-fibonacci-admissible-b--491b08dec094 .
