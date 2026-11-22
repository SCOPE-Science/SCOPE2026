# Balanced kinetic defects minimize fluctuation without changing drift in periodic biased transport

## Finding

Consider a continuous-time, nearest-neighbor random walk on the infinite integer lattice with a repeating period of \(n\ge4\) sites. Fix \(p>q>0\) and two distinct positive holding-time parameters \(\tau_0\ne\tau_1\). Every site has mean holding time \(\tau_0/(p+q)\), except for exactly \(k\) sites in each period, which have mean holding time \(\tau_1/(p+q)\), where \(2\le k\le n-2\). From a site of type \(i\), the walker moves one unit right at rate \(p/\tau_i\) or left at rate \(q/\tau_i\).

Let \(X_t\) denote the lifted lattice position, \(V=\lim_{t\to\infty}\mathbb E[X_t]/t\) and \(\sigma^2=\lim_{t\to\infty}\operatorname{Var}(X_t)/t\), and put \(S=(n-k)\tau_0+k\tau_1\). Then every choice of the \(k\) exceptional sites has the **same velocity**
\[
V=\frac{n(p-q)}{S}.
\]
However, the asymptotic variance rate is **strictly smallest** exactly for cyclically balanced exceptional sites, and **strictly largest** exactly when the \(k\) sites are consecutive (up to translation). Here cyclic balance means: for every \(1\le m<k\), the numbers of physical lattice edges spanning any \(m\) successive gaps between exceptional sites differ by at most one. In particular, a minimizing placement is
\[
A_{\min}=\left\{\left\lfloor\frac{jn}{k}\right\rfloor:0\le j<k\right\},
\]
whereas a maximizing placement is \(A_{\max}=\{0,1,\ldots,k-1\}\). The location dependence vanishes entirely in the unbiased case \(p=q>0\) and in the totally directed case \(p>0,q=0\).

More precisely, write \(r=q/p\), \(u=\tau_1-\tau_0\), and for any exceptional-site set \(A\subset\{0,\ldots,n-1\}\) define
\[
\mathcal E_r(A)=\sum_{\{a,b\}\subset A}\left(r^{(b-a)\bmod n}+r^{(a-b)\bmod n}\right).
\]
For any two such sets \(A,B\),
\[
\boxed{\sigma^2(A)-\sigma^2(B)
=\frac{2(p+q)(p-q)^2n^2u^2}{S^3p^2(1-r^n)(1-r^2)}
\left[\mathcal E_r(A)-\mathcal E_r(B)\right].}
\]
Every coefficient outside the square bracket is strictly positive under the standing hypotheses.

## Assumptions and scope

The lattice is infinite; the rates repeat modulo the integer \(n\). Position is **unwrapped** and both right and left jumps contribute respectively \(+1\) and \(-1\) to displacement, including across a period boundary. All waiting times are exponential and independent given the current state, and the exceptional-site *multiset* of rates is fixed while only the positions change. The claim concerns long-time mean velocity and centered variance per unit time, not mixing rates on the finite residue ring or finite-time distributions. The standard diffusion constant is \(D=\sigma^2/2\).

## Proof

**Stationary measure and corrector.** On residues modulo \(n\), the invariant probability is \(\pi_i=\tau_i/S\), since the rightward and leftward probability fluxes on every edge are respectively \(p/S\) and \(q/S\). Hence the mean velocity is \(V=n(p-q)/S\). The finite irreducible residue process admits a unique (up to addition of a constant) corrector \(h\) solving
\[
(Qh)_i=V-\frac{p-q}{\tau_i},\qquad
(Qh)_i=\frac{p(h_{i+1}-h_i)+q(h_{i-1}-h_i)}{\tau_i}.
\]
Let \(d_i=h_{i+1}-h_i\). Then \(\sum_i d_i=0\) and
\[
pd_i-qd_{i-1}=(p-q)\left(\frac{n\tau_i}{S}-1\right).
\]
The compensated process \(X_t+h_{X_t\bmod n}-Vt\) is a martingale with bounded corrector. Its predictable quadratic variation in the stationary residue law gives
\[
\sigma^2=\frac1S\sum_i\left[p(1+d_i)^2+q(1+d_{i-1})^2\right]
=\frac{p+q}{S}\left(n+\sum_i d_i^2\right).
\]
The finite-state ergodic theorem and boundedness of the corrector establish existence and identification of the limit for every initial residue.

**Geometric response kernel.** Put \(r=q/p\in(0,1)\). Solving the preceding periodic first-order recurrence yields
\[
d_i=\frac{(p-q)n}{Sp(1-r^n)}
\sum_{j=0}^{n-1}r^j\left(\tau_{i-j}-\frac Sn\right).
\]
Since \(\tau_i=\tau_0+u\mathbf1_{\{i\in A\}}\), only the squared norm of the cyclic convolution of \(\mathbf1_A\) with the geometric sequence matters. For distinct residues separated by forward distance \(s\in\{1,\ldots,n-1\}\), direct summation gives
\[
\sum_{j=0}^{n-1}r^j r^{(j-s)\bmod n}
=\frac{1-r^n}{1-r^2}\left(r^s+r^{n-s}\right).
\]
Diagonal terms and mean-subtraction terms depend only on \(n,k,\tau_0,\tau_1\), not positions. Expanding the remaining cross terms proves the displayed pair-energy difference formula.

**Sharp minimum.** Enumerate exceptional sites cyclically and let \(g_1,\ldots,g_k\) be their positive integer gaps, summing to \(n\). Define \(f(x)=r^x+r^{n-x}\) on \([0,n]\). This function is strictly convex because \(f''(x)=(\log r)^2f(x)>0\). For \(m=1,\ldots,k-1\), let \(G_{i,m}=g_i+\cdots+g_{i+m-1}\) with cyclic indices. Then
\[
\mathcal E_r(A)=\frac12\sum_{m=1}^{k-1}\sum_{i=1}^{k}f(G_{i,m}),
\qquad \sum_{i=1}^kG_{i,m}=mn.
\]
For a strictly convex function evaluated on integers of fixed sum, this inner sum is minimized precisely when its arguments differ by at most one (if two differ by two or more, shifting one unit from the larger to the smaller strictly lowers the sum). The set \(A_{\min}\) above achieves this balancing simultaneously for every \(m\), because every \(m\)-step span of equally distributed floor positions is either \(\lfloor mn/k\rfloor\) or \(\lceil mn/k\rceil\). Thus it attains every separate lower bound. Conversely, equality for the total sum requires the stated cyclic-balance condition for **all** \(m\); that is the full minimizing classification.

**Sharp maximum.** The same expression is strictly convex as a function of the real gap vector \(g\) on the simplex \(g_i\ge1\), \(\sum g_i=n\): already the \(m=1\) term \(\sum_i f(g_i)\) is strictly convex. Every vector that is not an extreme point is a nontrivial convex combination of two different allowed vectors, and therefore cannot attain the maximum. The extreme points have one gap \(n-k+1\) and every other gap \(1\), which is exactly a contiguous block of exceptional sites. Rotational symmetry makes their energies identical, so these and only these are the maximizers.

**Degenerate bias limits.** If \(p=q\), the local mean drift is zero and a constant corrector gives \(\sigma^2=n(p+q)/S\). If \(q=0\), direct substitution into the recurrence gives \(\sigma^2=p n^2(\sum_i\tau_i^2)/S^3\). Both depend on the multiset of holding times but not their spatial order.

## Verification

Execute `python3 checks/check_transport.py` from the package root. The program uses exact rational arithmetic and two separately expressed methods for variance (periodic generator linear systems and geometric convolution). It checks 297 generator/convolution combinations, exhaustively tests 4,070 small-period placement/equality cases, and verifies a six-site example: for \(n=6\), \((p,q)=(3,1)\), \((\tau_0,\tau_1)=(1,2)\), and two exceptional sites at separation \(1,2,3\), the exact variance rates are respectively \(1161/364\), \(18225/5824\), and \(81/26\). Finite checks complement, but do not replace, the arbitrary-period proof above.

## Relationship to prior work

Bernard Derrida's 1983 periodic hopping model supplies general formulas for velocity and diffusion at arbitrary nearest-neighbor rates; Zbigniew Koza's 1999 preprint supplies another general method for arbitrary periodic transport. Those general transport methods and their implications for **computability** are established prior work, not new. The present contribution is an explicit sharp **spatial arrangement/extremal theorem** for two-level waiting-time defects, including a complete equality criterion and the separation of drift from fluctuation optimization. Those conclusions are derived by an additional positive geometric-kernel identity and cyclic convex rearrangement rather than merely evaluating a generic rate formula. We do not claim priority for general diffusivity formulas or for convexity itself.

## Limitations

The theorem needs constant directional ratio across sites, nearest-neighbor jumps, period \(n\), two positive waiting-time levels, and fixed occupancy count. It is not an optimality theorem for general site-dependent biases, correlated waiting times, dynamically changing defects, or higher displacement cumulants. Historical-priority review is limited to the cited foundational methods and targeted searches; an earlier equivalent arrangement theorem could exist. Independent scientific validation has not been performed.

## References

- B. Derrida, *Velocity and diffusion constant of a periodic one-dimensional hopping model*, Journal of Statistical Physics **31** (1983), 433–450. https://www.lps.ens.fr/~derrida/PAPIERS/1983/jsp1983-vitesse.pdf
- Z. Koza, *General technique of calculating drift velocity and diffusion coefficient in arbitrary periodic systems*, arXiv:cond-mat/9909204 (first public preprint 1999-09-14); Journal of Physics A **32** (1999), 7637–7651. https://arxiv.org/abs/cond-mat/9909204
