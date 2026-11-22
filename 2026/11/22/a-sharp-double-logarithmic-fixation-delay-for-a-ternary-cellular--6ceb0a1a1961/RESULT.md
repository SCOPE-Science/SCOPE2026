# A sharp double-logarithmic fixation delay for a ternary cellular automaton

## Finding

Let \(X^{(0)}\) be independent uniform symbols from \(\{0,1,2\}\) on the cyclic ring \(\mathbb Z/n\mathbb Z\). Evolve synchronously by

\[
X_i^{(t+1)}=\begin{cases}
X_{i+1}^{(t)},&X_{i-1}^{(t)}=X_i^{(t)}>X_{i+1}^{(t)},\\
X_i^{(t)},&\text{otherwise}.
\end{cases}
\]

Define the first fixed-configuration time
\[
T_n=\min\{t\geq0:X^{(t+1)}=X^{(t)}\},\qquad
b_n=\log_3 n+\log_3(\log_3 n).
\]
For integers \(n\to\infty\),
\[
\boxed{T_n-b_n=O_{\mathbb P}(1),\qquad \mathbb E T_n=b_n+O(1).}
\]
Thus the finite-system relaxation clock has an additive second-order \(\log_3\log_3 n\) delay, even though local relaxation follows a polynomial-times-exponential law.

More explicitly, for integers \(t\geq1\) with \(n\geq2t+3\),
\[
\mathbb P(T_n>t)\leq \frac{n(t+15)}{81\,3^t}.
\]
For integers \(t\geq3\) with \(n\geq2(t+4)\),
\[
\mathbb P(T_n<t)\leq\frac{3^{t+4}}{n(t-1)}+\frac6n.
\]
These two finite-size inequalities imply the tight centered clock and expectation estimate.

## Assumptions and scope

All indices are read modulo the ring length; all sites update simultaneously. The initial law is the product of the uniform three-symbol measure. The conclusion concerns the *first time the entire finite ring becomes fixed*, not the evolution of an individual site or a fixed finite observation window. Constants in both asymptotic statements are absolute. The defining formula for \(b_n\) is used for \(n\geq3\); the result is asymptotic as the integer length grows.

The local rule is exactly the three-state lifted elementary Rule 140 introduced by Fukś and Midgley-Volpato, rather than ordinary two-state Rule 140. It agrees with their piecewise lift on each of the 27 possible neighborhood triples; the shorter form is obtained by observing that the only nonidentity change is the rightmost member of a descending constant pair. This identity is also checked exhaustively in the accompanying code.

## Proof

**1. Monotonicity and certain finite-time fixation.** Every local transition preserves its symbol or strictly decreases it. Therefore \(S_t=\sum_i X_i^{(t)}\) is a nonnegative integer, decreasing by at least one on every nonstationary update. Consequently every initial state becomes fixed after at most \(2n\) updates, so the stopping time is well defined.

**2. A one-site decrease identity.** Let \(\mu_t=\mathbb E X_0^{(t)}\) in the bi-infinite product initial law. Specializing the all-time density polynomials for lifted Rule 140 in Fukś–Midgley-Volpato, specifically their equations (19) and (24), to the uniform law gives, for integers \(t\geq1\),
\[
\mathbb P(X_0^{(t)}=1)=\frac{11}{36}+\frac{2t+7}{108\,3^t},\qquad
\mathbb P(X_0^{(t)}=2)=\frac29+\frac{1}{9\,3^t}.
\]
Hence
\[
\mu_t=\frac34+\frac{2t+31}{108\,3^t},\qquad
\mu_t-\mu_{t+1}=\frac{t+15}{81\,3^t}.
\]
This single-site density identity is a prior published result, not part of the new claim. For additional algebraic verification, the published preimage transfer at the uniform law has
\[
R=\begin{pmatrix}1/3&0&0&0\\1/3&1/3&0&0\\0&1/3&1&1/3\\0&0&0&1/3\end{pmatrix},\quad
Q=\frac1{27}\begin{pmatrix}1\\4\\5\\2\end{pmatrix},\quad
U=\frac1{27}\begin{pmatrix}9\\14\\27\\13\end{pmatrix}.
\]
The density of symbol \(1\) for \(t\geq3\) equals \(U^{\mathsf T}R^{t-3}Q\). The exact identity \((R-I)(R-I/3)^2=0\), with the three base values at times \(3,4,5\), verifies the displayed closed form at every later time. The symbol-\(2\) formula follows from the simpler published density polynomial (24). The packaged checker performs these rational-arithmetic certificates and small-time direct neighborhood enumeration.

For a ring with \(n\geq2t+3\), the initial causal window for a site at times \(t,t+1\) contains \(2t+3\) distinct independent symbols and has exactly the same law as on the bi-infinite lattice. A nonfixed state at time \(t\) must change at least one symbol in the next update. Since decreases are integer-valued and nonnegative, Markov's inequality and translation invariance yield
\[
\mathbb P(T_n>t)\leq\mathbb E(S_t-S_{t+1})
=n(\mu_t-\mu_{t+1})=\frac{n(t+15)}{81\,3^t}.
\]

**3. Protected long-lasting two-run words.** Fix an integer \(t\geq3\). At any ring position choose a word
\[
W_{a,b}=0\,2^a1^b\,0,\qquad
 a\geq2,\quad b\geq2,\quad a+b=t+2.
\]
Here exponent notation means a consecutive run of the specified symbol. Both endpoint zeros remain zero forever, regardless of the exterior configuration, so the interior evolves independently. For exactly \(a-1\) steps the right edge of the block of twos erodes into ones while the right edge of the block of ones erodes into zeros; the ones-block retains length \(b\). Once a single two remains, the ones-block shortens for exactly \(b-1\) more steps. Thus at least one symbol still changes at the transition into time \(t\), proving \(T_n\geq a+b-2=t\) whenever this protected word is initially present. The words are true witnesses for *global* nonfixation, not merely for delayed local density.

There are \(t-1\) allowed ordered run-length splits. Let \(L=t+4\) and let \(Z\) count their occurrences at all \(n\) ring starts, with the split determined by the word. Each full word has probability \(3^{-L}\), hence
\[
\mathbb EZ=\frac{n(t-1)}{3^{t+4}}.
\]
Assume \(n\geq2L\). Two distinct candidate starts with interiors overlapping cannot both match, because each motif has zeros only at its endpoints; the only nonnegative overlap covariance arises when the last zero of one occurrence is the first zero of another. For each of the two such cyclic displacements, at most \((t-1)^2\) split pairs are compatible, each with probability \(3^{-2L+1}\). Therefore
\[
\operatorname{Var}Z\leq\mathbb EZ+2n(t-1)^2\,3^{-2L+1},
\qquad
\mathbb P(Z=0)\leq\frac{\operatorname{Var}Z}{(\mathbb EZ)^2}
\leq\frac{3^{t+4}}{n(t-1)}+\frac6n.
\]
As \(Z>0\) forces \(T_n\geq t\), this proves the claimed lower-tail inequality.

**4. Tight centering and expectation.** Put \(\ell_n=\log_3 n\) and \(b_n=\ell_n+\log_3\ell_n\). At \(t=\lceil b_n+K\rceil\), the upper bound is \(O(3^{-K})\) uniformly for fixed nonnegative \(K\) as \(n\to\infty\). At \(t=\lfloor b_n-K\rfloor\), the lower bound is also \(O(3^{-K})\). Both positions are \(O(\log n)\), so all causal-cone and motif-size restrictions apply for large enough \(n\). It follows that \(T_n-b_n\) is tight.

For the mean, sum the two one-sided tail estimates. Above \(b_n\), the displayed exponential upper bound has a uniformly summable tail. At the end of the valid cone range, near \(n/2\), its exponentially small probability times the deterministic \(2n\) horizon remains negligible. Below \(b_n\), use the geometric lower bound down to \(\ell_n/2\); for all earlier times, monotonicity and the single bound at \(\lfloor\ell_n/2\rfloor\) give an \(O(\ell_n/\sqrt n)\) remainder. Thus the expected absolute centered deviation is bounded, proving \(\mathbb ET_n=b_n+O(1)\).

## Verification

Run `python VERIFY.py` from this directory; only the Python standard library is needed. It checks the 27 local neighborhood cases against the original lifted definition; proves the exact rational transfer-matrix annihilator and the three base values used in the all-time density identity; exhaustively enumerates the one-site mean decrease through four updates; checks 64 protected two-run witnesses; and compares two implementations over every three-symbol ring configuration for lengths \(3\) through \(10\). This is computational corroboration of the explicitly stated proof, not a substitute for its all-length argument.

## Relationship to prior work

Fukś and Midgley-Volpato publicly presented the three-symbol lifted Rule 140 and its degenerate-polynomial-exponential local density phenomenon in June 2015, subsequently publishing their preprint on 22 June 2015. Its finite-state-machine density expressions are used verbatim as an input to step 2, and are not claimed as new. The cited work studies one-site density and its convergence on the infinite lattice; the present conclusion is a *whole-ring first-fixation clock* with a second-order \(\log\log\) correction and a mean estimate. The additional protected-word second-moment argument provides the matching lower bound. The earlier binary-rule density analysis concerns a different alphabet and lacks this two-run double-logarithmic mechanism. Nearby finite-ring transient results for other majority and elementary rules are neither equivalent nor stronger for this particular update rule.

## Limitations

The theorem assumes uniform independent three-state initial conditions and synchronous cyclic updating; it makes no claim for nonuniform Bernoulli parameters, open boundaries, or noisy/asynchronous updates. It establishes bounded centered fluctuations but does not identify a limiting lattice extreme-value law or its oscillatory subsequences. The proof uses the published all-depth preimage-language description of the lifted automaton; the algebraic transfer certificate and exhaustive finite experiments check important consequences but do not independently recreate that entire infinite-language construction. Definitive priority beyond the inspected literature is not asserted.

## References

1. H. Fukś and J. Midgley-Volpato, *Degenerate hyperbolicity in cellular automata*, public AUTOMATA 2015 presentation dated 8 June 2015: https://math.utu.fi/automata2015/wp-content/uploads/sites/5/2015/06/HenrykFuks-Automata2015.pdf
2. H. Fukś and J. Midgley-Volpato, *An example of degenerate hyperbolicity in a cellular automaton with 3 states*, arXiv:1506.06649 (first public preprint 22 June 2015), especially equations (11), (19), (24): https://arxiv.org/pdf/1506.06649
3. H. Fukś and J. M. Gómez Soto, *Exponential convergence to equilibrium in cellular automata asymptotically emulating identity*, arXiv:1306.1189 (first preprint 2013), binary-rule comparison: https://arxiv.org/pdf/1306.1189
