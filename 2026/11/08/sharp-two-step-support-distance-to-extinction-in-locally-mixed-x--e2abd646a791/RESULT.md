# Sharp two-step support distance to extinction in locally mixed XOR automata

## Finding
Let \(n\ge 2\). On the periodic binary ring \(\mathbb Z/n\mathbb Z\), independently at each site and update, choose rule 60 with probability \(1-\lambda\) or rule 102 with probability \(\lambda\), where \(0<\lambda<1\). These rules send the triple \((a,b,c)\) to \(a\oplus b\) and \(b\oplus c\), respectively. Write \(\mathbf0\) for the zero configuration, and define the **positive-support extinction distance**
\[
d_n(x):=\min\{t\ge0:\mathbb P_x(X_t=\mathbf0)>0\}.
\]
An **isolated bit** in a circular word \(x\) is a position \(i\) where \(x_{i-1}=x_{i+1}\ne x_i\), with indices modulo \(n\). Then the complete support-distance classification is
\[
d_n(x)=\begin{cases}0,&x=\mathbf0,\\1,&x\ne\mathbf0\ \text{and }x\text{ has no isolated bit},\\2,&\text{otherwise}.\end{cases}
\]
In particular \(\max_x d_n(x)=2\) for every \(n\ge2\), and the bound is attained by a configuration with exactly one nonzero site.

Put \(\varphi=(1+\sqrt5)/2\) and \(\psi=(1-\sqrt5)/2\). The number of circular words with no isolated bit is exactly
\[
A_n=\varphi^n+\psi^n+2\cos(n\pi/3).
\]
Consequently, exactly \(1\), \(A_n-1\), and \(2^n-A_n\) configurations have support distance \(0\), \(1\), and \(2\), respectively; the fraction at distance two tends to one exponentially as \(n\to\infty\).

For \(r=\min\{\lambda,1-\lambda\}\) and the actual random hitting time \(\tau_0=\min\{t\ge0:X_t=\mathbf0\}\), we also have uniformly over all starting states
\[
\mathbb P_x(\tau_0\le2)\ge r^{2n},\qquad
\mathbb P_x(\tau_0>2k)\le(1-r^{2n})^k,\qquad
\mathbb E_x\tau_0\le 2r^{-2n}\quad(k\ge0).
\]
These explicit tail estimates apply to every mixing parameter strictly between zero and one. They are not asserted to be optimal probability bounds.

## Assumptions and scope
All states are binary and indexed cyclically; all sites update synchronously, and the individual rule selections are conditionally independent given the current configuration. The positive-support graph has an edge \(x\to y\) precisely when the one-step transition probability is positive. The statement concerns this finite-volume support graph and the associated finite-volume Markov chain; it does not assert extinction in the infinite-lattice model or any uniform-in-\(n\) relaxation rate. The endpoints \(\lambda=0,1\) are excluded.

## Proof
**1. Local support as the discrete derivative of a cyclic word.** Given \(x\), set \(b_i=x_{i-1}\oplus x_i\). The two possible updates at site \(i\) are exactly \(b_i\) (rule 60) and \(b_{i+1}\) (rule 102). Thus \(y\) is a permitted next configuration if and only if \(y_i=b_i\) whenever \(b_i=b_{i+1}\); when \(b_i\ne b_{i+1}\), either bit is permitted. Because \(0<\lambda<1\), every permitted joint output has positive probability.

**2. One-step extinction.** If \(x\) has an isolated bit at \(i\), the two outer neighbors agree and oppose the central bit. Both rules then force a \(1\) at \(i\), making \(\mathbf0\) inaccessible in one step. Conversely, if \(x\) has no isolated bit, at a site with equal outer neighbors all three inputs are equal, so the forced update is \(0\); at every other site the two possible updates are \(0\) and \(1\). Conditional independence therefore makes \(\mathbf0\) reachable in one step. This proves the exact one-step criterion.

**3. A globally admissible first step.** Every binary circular word \(b\) admits an output \(y\) obeying the constraints of Step 1 and having no isolated bit. If the cyclic word \(b\) has no adjacent equal entries, all its update positions are free; choose \(y=\mathbf0\). Otherwise partition \(b\) into its maximal constant cyclic runs. Keep each run of length at least two unchanged, and fill each intervening succession of singleton runs with the bit of the preceding run of length at least two (cyclically). In the degenerate constant-word case, simply put \(y=b\). Every forced position \(b_i=b_{i+1}\) lies inside a run of length at least two and is preserved. Every maximal constant run of the resulting \(y\) contains an unchanged run of length at least two and therefore has length at least two. Hence \(y\) has no isolated bit. By Step 2 it has a permitted transition to \(\mathbf0\), proving \(d_n(x)\le2\) for all \(x\). If \(x\) has a single \(1\), the update at that site is forced to be \(1\), so its distance is exactly two. This holds also for the two-site ring, where the two neighboring indices coincide.

**4. Exact census.** Build the four-state overlap graph with vertex order \(00,01,10,11\), allowing precisely the six triples \(000,001,011,100,110,111\). Its adjacency matrix is
\[
B=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
The number \(A_n\) of labeled cyclic words without isolated bits equals \(\operatorname{tr}(B^n)\) (including \(n=2\)). Direct determinant expansion gives \(\det(tI-B)=(t^2-t-1)(t^2-t+1)\). Its eigenvalues are \(\varphi,\psi,e^{i\pi/3},e^{-i\pi/3}\), yielding the displayed exact formula. Since \(\varphi<2\), we have \(A_n/2^n\to0\) exponentially.

**5. Uniform positive probability and tail.** Each freely selectable bit in the constructed two-step path is chosen with conditional probability at least \(r=\min\{\lambda,1-\lambda\}\); a forced bit has probability one. There are at most \(2n\) free selections over the two updates, so \(\mathbb P_x(X_2=\mathbf0)\ge r^{2n}\). The zero state is absorbing. Applying the Markov property in blocks of two gives the stated geometric tail, and summing the tail over integer times gives \(\mathbb E_x\tau_0\le2r^{-2n}\). No infinite-volume conclusion follows because this uniform bound decays with \(n\).

## Verification
The dependency-free script `verify.py` exhaustively checks the explicit run-smoothing witness for every starting configuration and \(2\le n\le15\) (65,532 states), independently brute-forces the existence of a one-step admissible successor for every state with \(2\le n\le9\) (1,020 states), verifies all one-step distance counts against the closed form through \(n=15\), and checks 252 exact two-step absorption probabilities at \(\lambda=1/3\) on \(2\le n\le7\). The scripted finite checks corroborate, but do not replace, Steps 1--5.

## Relationship to prior work
Cirillo, Vliem, Schuricht and Spitoni (2026), Theorem 1, show a positive-probability path to extinction in **four** steps at the balanced parameter on rings with at least five sites, and Theorem 2 deduces eventual finite-volume absorption. Their Lemma 3 supplies the one-step cleaning observation used here. The new mathematical statement is the **exact two-step support distance**, including an explicit cyclic run-smoothing argument, and the complete distance census. The extension of positive-support statements to other interior mixing probabilities follows from the common support of the local kernels and is not presented as a separate discovery.

Bayraktar et al. (2024) study synchronization for a different class of probabilistic cellular automata whose local transition probabilities depend linearly on neighborhood empirical distributions through a transition matrix. Endo (2026) examines extinction times for deterministic additive and related cellular automata rather than this sitewise independent mixture. These contexts do not supply the exact support-distance classification above.

## Limitations
The result is restricted to finite periodic binary rings, the locally and independently selected XOR rules 60 and 102, and interior mixing probabilities. The probability lower bound is deliberately coarse. In particular, finite-volume almost-sure extinction for any interior parameter is compatible with long metastability and nonzero-density regimes in the thermodynamic limit. The result is not a classification of all probabilistic cellular automata. Historical priority and any generalization to other local rules require further investigation; no independent audit has been performed.

## References
- E. N. M. Cirillo, J. L. Vliem, D. Schuricht and C. Spitoni, *Inefficiency of the block approximation in diploid Probabilistic Cellular Automata*, arXiv:2602.13839v1 (first public: 2026-02-14), Section IV, Theorems 1--2 and Lemma 3, https://arxiv.org/html/2602.13839.
- E. Bayraktar, F. Lu, M. Maggioni, R. Wu and S. Yang, *Probabilistic cellular automata with local transition matrices: synchronization, ergodicity, and inference*, arXiv:2405.02928 (2024), https://arxiv.org/abs/2405.02928.
- K. Endo, *Extinction dynamics in cellular automata: extensions of additive systems and nonlinear constructions*, JSIAM Letters 18 (2026), 29--32, DOI 10.14495/jsiaml.18.29, https://doi.org/10.14495/jsiaml.18.29.
