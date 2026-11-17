# Packet-count universality and seven-card onset of variation amplification in inverse riffle averaging

## Finding
Fix an integer \(a\ge2\) and probabilities \(p_1,\ldots,p_a>0\) summing to one. Give the \(n\) original positions independent labels with these probabilities, stable-sort the positions by label, and average the resulting permutation action on real signals. Denote the linear averaging operator by \(T_{n,p}\). On the nonperiodic path use
\[
V_n(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|,
\qquad
C_n(p)=\sup_{V_n(h)>0}\frac{V_n(T_{n,p}h)}{V_n(h)}.
\]
Then, for every \(n\ge2\),
\[
C_n(p)\le2a-1,\qquad \boxed{\lim_{n\to\infty}C_n(p)=2a-1}.
\]
More quantitatively, if \(p_*:=\min_j p_j\) and \(n\ge16/p_*\), then
\[
(2a-1)\left(1-12a\exp\!\left(-\frac{np_*^2}{32}\right)\right)
\le C_n(p)\le 2a-1.
\]
The lower bound is allowed to be vacuous at modest sizes; it proves exponentially fast convergence for every fixed strictly positive packet law. Every finite-dimensional coefficient is attained by a prefix step, and hence by a finite pair of inputs.

The uniform two-packet law \(p=(1/2,1/2)\) has the following exact values:

| \(n\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) | \(7\) |
|---|---|---|---|---|---|---|
| \(C_n(p)\) | \(1/2\) | \(1/2\) | \(5/8\) | \(11/16\) | \(29/32\) | \(67/64\) |

Thus **seven sites are the first size at which the expected inverse fair two-packet riffle amplifies adjacent variation**.

Successive independent inverse shuffles satisfy \(T_{n,p}^{\,r}=T_{n,p^{\otimes r}}\), where the latter has \(a^r\) ordered packet labels with product probabilities. Consequently, for each fixed integer \(r\ge1\),
\[
\lim_{n\to\infty}\|T_{n,p}^{\,r}\|_{V}=2a^r-1,
\]
whereas for each fixed \(n\) the same variation operator norm tends to zero as \(r\to\infty\). In particular the limits in deck size and number of shuffles do not commute. Here \(\|\cdot\|_V\) is the induced operator norm on the quotient of real signals by constants, not total-variation distance between probability distributions.

## Assumptions and scope
The deck is an ordered path with \(n\) sites, and data are real-valued. Label assignments to distinct sites are independent. Each packet preserves the order of its original members, and packets are concatenated in label order. The strict positivity assumption is essential for the asserted packet-count limit; zero-probability labels should be omitted and the count replaced by the number of positive packets. The seminorm is unweighted, adjacent, and nonperiodic. The operator is the **expectation of the inverse shuffle**, not the expectation of the physical forward riffle permutation. The separate exact finite-size onset statement concerns only the unbiased two-packet law.

## Proof
**1. Reduction to one jump.** Let \(e^{(k)}_i=\mathbf1_{\{i\le k\}}\), for \(1\le k<n\). Since every inverse shuffle preserves constants, so does \(T_{n,p}\). Every real signal has the identity
\[
h=h_n\mathbf1+\sum_{k=1}^{n-1}(h_k-h_{k+1})e^{(k)},
\qquad V_n(h)=\sum_{k=1}^{n-1}|h_k-h_{k+1}|.
\]
The triangle inequality, together with testing each step, proves the **exact** formula
\[
\boxed{C_n(p)=\max_{1\le k<n}V_n(T_{n,p}e^{(k)})}.
\]
This also proves finite attainment and reduces the nonlinear-looking extremal problem to an explicit linear-operator computation.

**2. Sharp universal packet bound.** For a fixed label assignment and any prefix step, the sorted output is a concatenation
\[
1^{U_1}0^{W_1}\,1^{U_2}0^{W_2}\cdots1^{U_a}0^{W_a},
\]
where \(U_c\) and \(W_c\) are the numbers of original prefix and suffix sites assigned to packet \(c\), respectively. Empty blocks are permitted. There are at most \(a\) downward jumps and \(a-1\) upward jumps. Thus every realized binary output has variation at most \(2a-1\). Variation is convex, so taking expectations gives \(V_n(T_{n,p}e^{(k)})\le2a-1\). Step 1 yields the stated uniform upper bound.

**3. Uniformly separated alternating probes.** Set \(k=\lfloor n/2\rfloor\), \(p_* = \min_c p_c\), and \(s_c=\sum_{j\le c}p_j\), with \(s_0=0\). For \(n\ge16/p_*\), choose the strictly ordered integer probe positions
\[
u_c=\left\lfloor n(s_{c-1}+p_c/4)\right\rfloor,
\qquad
v_c=\left\lfloor n(s_{c-1}+3p_c/4)\right\rfloor,
\quad 1\le c\le a.
\]
For each random assignment let \(L_c\) count all labels below \(c\), let \(B_c\) count all labels below \(c\) plus labels equal to \(c\) among the first \(k\) sites, and let \(R_c\) count all labels at most \(c\). The ones segment of packet \(c\) occupies the integer interval \((L_c,B_c]\), and its zeros segment occupies \((B_c,R_c]\). Their three expectations are respectively \(ns_{c-1}\), \(ns_{c-1}+kp_c\), and \(ns_c\). Each count is a sum of \(n\) independent variables taking values in \(\{0,1\}\), including possible constants. Hoeffding's inequality therefore gives, with \(\delta=np_*/8\),
\[
\Pr\{|Z-\mathbb EZ|\ge\delta\}
\le2\exp\!\left(-\frac{np_*^2}{32}\right)
\quad\text{for each }Z\in\{L_c,B_c,R_c\}.
\]
With probability at least \(1-\varepsilon_n\), where \(\varepsilon_n=6a\exp(-np_*^2/32)\), **all** these counts are within \(\delta\) of their means. By the quarter-packet margins, the floor rounding error of at most one, and \(n\ge16/p_*\), on this event \(L_c<u_c\le B_c<v_c\le R_c\) for every packet. The realized step therefore equals one at every \(u_c\) and zero at every \(v_c\). For its expected image \(y=T_{n,p}e^{(k)}\), we have \(y_{u_c}\ge1-\varepsilon_n\) and \(y_{v_c}\le\varepsilon_n\). Taking variation along the ordered subsequence \(u_1,v_1,\ldots,u_a,v_a\) gives
\[
V_n(y)\ge(2a-1)(1-2\varepsilon_n).
\]
This proves the quantitative lower bound, and together with step 2 proves the sharp, packet-bias-independent limit.

**4. Exact unbiased small-deck threshold.** For two equally probable labels let \(X\) be the number of the first \(k\) sites placed in the first packet and \(Y\) the number of the last \(n-k\) sites so placed. Then \(X\sim\mathrm{Bin}(k,1/2)\) and \(Y\sim\mathrm{Bin}(n-k,1/2)\) are independent, and the sorted step is \(1^X0^Y1^{k-X}0^{n-k-Y}\). Hence its mean at position \(i\) is the exact rational number
\[
y_i^{(n,k)}=2^{-n}\sum_{x=0}^{k}\sum_{z=0}^{n-k}
\binom{k}{x}\binom{n-k}{z}
\left(\mathbf1_{\{i\le x\}}+\mathbf1_{\{x+z<i\le z+k\}}\right).
\]
The two indicators are disjoint. Evaluating \(\sum_{i=1}^{n-1}|y_{i+1}^{(n,k)}-y_i^{(n,k)}|\) for all \(1\le k<n\), and taking the largest value, gives the table in the Finding section. The full exact per-cut values, which expose the finite enumeration rather than just its maxima, are:

| \(n\) | Values as \(k\) runs from \(1\) to \(n-1\) |
|---|---|
| \(2\) | \(1/2\) |
| \(3\) | \(1/2,\ 1/2\) |
| \(4\) | \(1/2,\ 5/8,\ 1/2\) |
| \(5\) | \(5/8,\ 11/16,\ 11/16,\ 5/8\) |
| \(6\) | \(21/32,\ 27/32,\ 29/32,\ 27/32,\ 21/32\) |
| \(7\) | \(23/32,\ 31/32,\ 67/64,\ 67/64,\ 31/32,\ 23/32\) |

All entries are reproduced by the standalone exact-rational checker, independently cross-checked against enumeration of every two-label assignment. There is no numerical extrapolation in this finite calculation.

**5. Repeated-shuffle separation of limits.** The inverse shuffle product rule follows by concatenating independent label digits in lexicographic order; \(r\) repetitions produce the same permutation law as one inverse shuffle into \(a^r\) packets with product probabilities. Applying step 3 for fixed \(r\) yields \(\lim_{n\to\infty}\|T_{n,p}^{\,r}\|_V=2a^r-1\). Conversely, with \(n\) fixed, any pair of original sites has the same compound label with probability \((\sum_c p_c^2)^r\). A union bound makes the probability of any collision at most \(\binom n2(\sum_c p_c^2)^r\), which tends to zero because \(a\ge2\) and every \(p_c>0\). Conditional on all labels being distinct, their relative order is uniform; consequently the conditional expectation of every step is constant. On the collision event any binary step image has variation at most \(n-1\). The step-norm formula now gives
\[
\|T_{n,p}^{\,r}\|_V\le(n-1)\binom n2\left(\sum_c p_c^2\right)^r\xrightarrow[r\to\infty]{}0.
\]
Hence the two limits do not commute, despite fixed-deck convergence to uniform averaging.

## Verification
Run `python check.py` with Python 3; it uses only standard-library integers and exact rational fractions. It independently enumerates all label assignments and checks the binomial expression and all exact finite coefficients through nine sites, verifies the packet-run upper bound in small two- and three-packet cases, verifies the inverse shuffle product matrix identity through five sites, and checks a nonuniform packet law. Its final printed line is `ALL_INVERSE_RIFFLE_VARIATION_CERTIFICATES_PASS`. These computations verify only stated finite cases. Steps 1–3 and 5, including the limit over every deck size, are analytical proofs, not empirical extrapolations.

## Relationship to prior work
Bayer and Diaconis introduced the inverse-riffle description and studied convergence in **total-variation distance between permutation laws**. Fulman developed biased packet laws and their convolution rule; those formulations and that rule are used here, not claimed as original. Assaf, Diaconis and Soundararajan give exact one-card transition matrices and their spectra, which in principle permit numerical evaluation of finite signal operators. Their statistical-distance and spectral statements do not provide the asserted sharp adjacent-signal-variation limit or seven-site onset. The present variation seminorm concerns changes between neighboring **signal coordinates**, not probability total variation. Earlier studies of transfer operators acting on continuous \(BV\) spaces concern different state maps and do not directly imply the finite inverse-shuffle variation theorem.

## Limitations
The sharp asymptotic is for each **fixed** packet count and fixed positive packet-probability vector as deck size grows; the displayed convergence rate is not uniform as the minimum packet probability vanishes or the packet count grows with the deck. Finite exact values are classified only for the unbiased two-packet case through seven sites (with additional diagnostics through nine sites), not for arbitrary probability vectors or arbitrary finite deck sizes. No assertion is made about the expected **forward** riffle operator. The comparison does not exclude an unindexed historical equivalent or uninspected theorem on an equivalent transfer operator. Independent mathematical audit has not been performed.

## References
1. J. Fulman, *The Combinatorics of Biased Riffle Shuffles*, arXiv:math/9712240, first publicly posted 1997-12-09; see Section 1, the inverse description and the convolution proposition. https://arxiv.org/abs/math/9712240
2. D. Bayer and P. Diaconis, *Trailing the Dovetail Shuffle to Its Lair*, Stanford technical report dated August 1989, later *Annals of Applied Probability* **2** (1992), 294–313; see inverse shuffles, group-algebra structure and permutation-law mixing. https://statistics.stanford.edu/technical-reports/trailing-dovetail-shuffle-its-lair
3. S. Assaf, P. Diaconis and K. Soundararajan, *Riffle Shuffles of a Deck with Repeated Cards*, arXiv:0905.4698, first posted 2009-05-28; especially the single-card transition-matrix section. https://arxiv.org/abs/0905.4698
4. S. P. Lalley, *Riffle Shuffles and Their Associated Dynamical Systems*, *Journal of Theoretical Probability* **12** (1999), 903–932. https://doi.org/10.1023/A:1021636902356
5. A. Berechet, *Perron–Frobenius Operators Acting on BV(I) as Contractors*, *Ergodic Theory and Dynamical Systems* **21** (2001), 1609–1624. https://doi.org/10.1017/S0143385701001778
