# Three-transition immunity and a sharp five-state positivity threshold for the second-order Padé Markov step

## Finding

Consider the second-order, L-stable rational map
\[
f(z)=\frac{1}{1-z+z^2/2},\qquad R_h(Q)=f(hQ)=(I-hQ+\tfrac12h^2Q^2)^{-1}.
\]
The following results hold in exact arithmetic for the row-generator convention of a finite continuous-time Markov chain.

**Three-transition immunity.** If the directed graph of positive off-diagonal rates of \(Q\) is acyclic and has no directed path longer than three edges, then \(R_h(Q)\) is entrywise nonnegative and row-stochastic for **every** \(h\ge0\), regardless of graph size or positive transition rates.

**Sharp small-step state count.** For every finite Markov generator on at most four states, including those with cycles, there exists \(\varepsilon_Q>0\) such that \(R_h(Q)\) is entrywise nonnegative and row-stochastic for \(0\le h\le\varepsilon_Q\). Five states are necessary and sufficient for a fixed generator to have a negative entry at every sufficiently small positive step.

**Exact five-state witness.** Let \(Q_*\) be the unit-rate pure-birth generator on states \(1,2,3,4,5\), with states \(1\) through \(4\) advancing at rate one and state \(5\) absorbing. Explicitly,
\[
Q_*=\begin{pmatrix}
-1&1&0&0&0\\
0&-1&1&0&0\\
0&0&-1&1&0\\
0&0&0&-1&1\\
0&0&0&0&0
\end{pmatrix}.
\]
The only entry of \(R_h(Q_*)\) that can be negative is
\[
\boxed{(R_h(Q_*))_{1,5}
=\frac{h^4\bigl(h^4+8h^3+12h^2-4\bigr)}{(h^2+2h+2)^4}.}
\]
Let \(h_*\) denote the unique positive zero of \(h^4+8h^3+12h^2-4\), numerically \(h_*=0.496605762665489\ldots\). The *complete* step-size set for which the witness defines a stochastic transition matrix is
\[
\boxed{R_h(Q_*)\ge0\ \Longleftrightarrow\ h=0\ \text{or}\ h\ge h_*.}
\]
In particular, this rational approximation has a negative transition probability for every \(0<h<h_*\) although its exact Markov semigroup is nonnegative for all \(h\ge0\).

## Assumptions and scope

A finite row-generator \(Q\in\mathbb R^{n\times n}\) satisfies \(Q_{ij}\ge0\) for \(i\ne j\) and \(Q\mathbf1=0\). Its directed graph has an edge \(i\to j\) precisely when \(i\ne j\) and \(Q_{ij}>0\). The length of a directed path counts edges, and the longest-path restriction is on *all* directed paths, not just shortest paths. The first assertion assumes this graph is acyclic. The second small-step assertion has no acyclicity assumption and is local for each fixed generator, not a single uniform time-step bound independent of rates. The witness uses unit rates; common rate \(\lambda>0\) changes the dimensionless variable to \(h\lambda\). All inequalities are entrywise.

The rational matrix function is well-defined for every \(h\ge0\), since every eigenvalue of a Markov generator has nonpositive real part and the zeros of \(1-z+z^2/2\) are \(1\pm i\). As \(Q\mathbf1=0\) and \(f(0)=1\), one has \(R_h(Q)\mathbf1=\mathbf1\) for every \(Q,h\). Hence the question is nonnegativity, not conservation.

## Proof

**1. Pathwise formula for acyclic generators.** Order vertices topologically, so \(Q\) is upper triangular with diagonal entries \(d_i\le0\) and off-diagonal rates \(q_{ij}\ge0\). For distinct vertices \(i\ne j\), the upper-triangular matrix-function formula gives
\[
(R_h(Q))_{ij}=\sum_{i=i_0\to i_1\to\cdots\to i_k=j}
 h^k\left(\prod_{a=0}^{k-1}q_{i_a i_{a+1}}\right)
 f[h d_{i_0},\ldots,h d_{i_k}],
\]
where brackets denote the divided difference of order \(k\), extended continuously to repeated diagonal nodes. This identity follows, for example, by expanding the resolvent around the triangular diagonal and collecting the products corresponding to directed paths. The diagonal entries are \(f(hd_i)>0\).

Write \(D(x)=x^2+2x+2\). Direct differentiation yields, for every \(x\ge0\),
\[
\begin{aligned}
f(-x)&=\frac2{D(x)},\\
f'(-x)&=\frac{4(x+1)}{D(x)^2},\\
f''(-x)&=\frac{4(3x^2+6x+2)}{D(x)^3},\\
f'''(-x)&=\frac{48x(x+1)(x+2)}{D(x)^4}.
\end{aligned}
\]
These four functions are nonnegative. By the Hermite--Genocchi formula, each divided difference of order at most three at nonpositive real nodes is a positive-simplex average of the corresponding derivative, hence is nonnegative. If no directed path exceeds three transitions, every summand in the displayed pathwise formula is nonnegative, for *every* \(h\ge0\). The row-sum identity proved above completes the first assertion.

**2. No arbitrarily-small sign loss on four or fewer states.** The origin expansion is
\[
f(z)=1+z+\tfrac12z^2+0\,z^3-\tfrac14z^4+O(z^5).
\]
Fix distinct states \(i,j\) connected by a directed path, and let \(\ell\) be the length of a shortest path. In an \(n\)-state graph, \(\ell\le n-1\). Every \(Q^k\) with \(k<\ell\) has a zero \((i,j)\) entry, while \((Q^\ell)_{ij}>0\): in a shortest-length walk, every factor must be an off-diagonal transition. For \(\ell=1,2\), the leading term of \((R_h(Q))_{ij}\) is strictly positive, because the first two nonconstant Taylor coefficients are positive.

Only \(\ell=3\) needs care when \(n\le4\). Here the cubic Taylor coefficient vanishes. Every length-four nonzero product contributing to \((Q^4)_{ij}\) must contain exactly three off-diagonal rates and one diagonal factor: four off-diagonal steps would repeat a vertex in a four-state graph, giving a cycle whose deletion produces a path shorter than three. The three-transition shortest path exists and all its transient vertices have strictly negative diagonal entries, so \((Q^4)_{ij}<0\). Consequently,
\[
(R_h(Q))_{ij}=-\tfrac14h^4(Q^4)_{ij}+O(h^5)>0
\]
for all sufficiently small positive \(h\). If no directed path connects \(i,j\), the entry is identically zero for every \(h\). Diagonal entries approach one. Taking the minimum of finitely many valid neighborhoods proves the local assertion for all \(n\le4\).

**3. Exact five-state classification.** The transient block of \(Q_*\) is the Jordan matrix \(-I+N\) with four superdiagonal ones. Every transient-to-transient \((i,j)\) entry of \(R_h(Q_*)\), with \(k=j-i\) transitions, is
\[
\frac{h^k}{k!}f^{(k)}(-h),\qquad 0\le k\le3,
\]
which is nonnegative by the derivatives above. The absorbing-column entry in a row with \(m\) transient states left is
\[
B_m(h)=1-\sum_{k=0}^{m-1}\frac{h^k}{k!}f^{(k)}(-h).
\]
Algebra gives the *complete* four expressions
\[
\begin{aligned}
B_1(h)&=\frac{h(h+2)}{D(h)},\\
B_2(h)&=\frac{h^2(h^2+4h+2)}{D(h)^2},\\
B_3(h)&=\frac{h^4(h^2+6h+6)}{D(h)^3},\\
B_4(h)&=\frac{h^4(h^4+8h^3+12h^2-4)}{D(h)^4}.
\end{aligned}
\]
Only \(B_4\) can be negative. Set \(P(h)=h^4+8h^3+12h^2-4\). Then \(P(0)=-4\), \(P(h)\to+\infty\) as \(h\to\infty\), and \(P'(h)=4h(h^2+6h+6)>0\) for \(h>0\). Thus \(P\) has exactly one positive root, and its sign yields the asserted stochasticity set. As \(B_4(h)=-h^4/4+O(h^5)\), five states realize arbitrarily-small loss, completing the sharp minimum-state claim.

## Verification

The attached `verify.py` uses symbolic rational arithmetic to reconstruct all four derivatives, the Jordan-block entries, the absorbing-column factorizations, conservation of the five-state map, the derivative and location of the unique threshold, and the first negative Taylor coefficient. It also performs 192 supplementary rational-matrix tests on acyclic layer graphs (three or fewer transitions). Its actual result on the supplied source is `VERIFY_OK exact_formula+derivative+root+small_graph_trials 192`. The infinite family and the dimension-minimality statement follow from the proof above; the finite tests are not offered as substitutes for that proof.

## Relationship to prior work

Itkin and Kazbek (2026) introduce this particular Padé \((0,2)\) factor for eventually positive Fokker--Planck discretizations. Their Theorem 6 proves a large-step positivity window for their generator class, and their Remark 4 recognizes that Metzler generators need not give unconditional nonnegativity. They do not state the path-depth sufficient condition, the dimension-four local protection, or the five-state exact stochasticity threshold established here. Their context motivates why one should distinguish small-step positivity from large-step positivity.

Zappavigna, Colaneri, Kirkland and Shorten (2012) study positivity loss and sufficient conditions for **diagonal** Padé discretizations of positive linear systems, with examples not imposing the conservative Markov row-sum constraint. The published 2026 note *Eight-state barrier for Markov positivity of the [2/2] Padé map* provides an analogous minimal-state and exact-window analysis, but for the different fourth-order diagonal Padé function. Its coefficients, minimal dimension eight, and bounded positivity interval do not imply this subdiagonal \([0/2]\) map's graph-depth theorem or five-state threshold. Classical positive-rational-approximation barriers explain why no order-two method preserves positivity over *all* Markov generators; they do not specify this transition-depth classification or exact witness window.

## Limitations

Acyclicity and maximum path length three are **sufficient**, not necessary, conditions for all-step nonnegativity. The local small-step result for arbitrary generators of dimension at most four need not hold at large steps. The exact threshold belongs to the specific unit-rate pure-birth witness; it is not a bound applying to all five-state chains, all rate choices, or general Fokker--Planck matrices. This concerns the exact one-step matrix function, not nonlinear internal stages, global simulation accuracy or rounding errors. Mathematical priority may be affected by unindexed classical matrix-function or positive-systems results; the literature comparison is not an exhaustive proof of novelty.

## References

1. A. Itkin and R. Kazbek, *Diagonal Frog meets ADI: trading matrix exponentials for rational maps in the Fokker--Planck equation*, arXiv:2608.22703v1, first public 24 August 2026. https://arxiv.org/abs/2608.22703
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially negative news about positive systems*, Linear Algebra and its Applications **436** (2012), 3425--3442. https://doi.org/10.1016/j.laa.2011.12.021 ; open preprint https://mural.maynoothuniversity.ie/id/eprint/3761/
3. *Eight-state barrier for Markov positivity of the [2/2] Padé map* (2026), publicly available mathematical note. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
4. C. Bolley and M. Crouzeix, *Conservation de la positivité lors de la discrétisation des problèmes d'évolution paraboliques*, RAIRO Analyse Numérique **12** (1978), 237--245.
