# A single intra-part adsorption channel creates an imbalance-driven jamming transition

## Finding

Let \(a\ge2\), \(b\ge1\), and \(\lambda>0\). Start from the complete bipartite graph \(K_{a,b}\) with parts \(A,B\), designate two vertices \(x,y\in A\), and add one edge \(xy\). Dimers deposit irreversibly on edges with both endpoints vacant: every cross-part edge has rate \(1\), and the added edge has rate \(\lambda\). All clocks are independent Poisson processes. Once occupied, a vertex cannot be used again.

Write \(P_{a,b}(\lambda)\) for the probability that the added edge is eventually occupied, \(N=\min(a,b)\), and, for \(0\le k\le N\),
\[
f_k=\frac{(a-k)(a-k-1)}{a(a-1)},\quad
h_k=(a-k)(b-k),\quad
L_0=1,\quad L_k=\prod_{j=0}^{k-1}\frac{h_j}{h_j+\lambda}.
\]
Here \(h_N=0\), and \(f_k=0\) when fewer than two vertices remain in \(A\). The exact all-size law is
\[
\boxed{P_{a,b}(\lambda)=\sum_{k=0}^{N-1}f_kL_k\frac{\lambda}{h_k+\lambda}+f_NL_N.}
\tag{1}
\]
In particular, this is a rational function of \(\lambda\) for every pair of positive integers \(a,b\). It also admits the direct finite product form
\[
P_{a,b}(\lambda)=\sum_{k=0}^{\min(a-2,b)}\frac{\lambda}{(a-k)(b-k)+\lambda}\prod_{j=0}^{k-1}\frac{(a-j-2)(b-j)}{(a-j)(b-j)+\lambda}.
\tag{2}
\]
When \(b\le a-2\), the last term in (2) has denominator \(\lambda\) and represents deposition after every cross-part edge is blocked.

If \(X\) denotes the total number of dimers at jamming, then, **pathwise**, \(X=N\) if \(xy\) is never used and \(X=1+\min(a-2,b)\) otherwise. Consequently,
\[
\boxed{\mathbb E[X]=\min(a,b)+\Delta_{a,b}P_{a,b}(\lambda),\quad
\Delta_{a,b}=\begin{cases}-1,&a\le b,\\0,&a=b+1,\\+1,&a\ge b+2.\end{cases}}
\tag{3}
\]
Thus adding an admissible edge *strictly reduces* expected terminal dimer count whenever \(a\le b\), increases it for \(a\ge b+2\), and leaves it unchanged for \(a=b+1\). The event probability is strictly between zero and one at all finite \(a,b,\lambda\).

The weak added-channel limit is discontinuous at zero rate precisely when the unmodified bipartite adsorption leaves at least two \(A\)-vertices:
\[
\boxed{\lim_{\lambda\downarrow0}P_{a,b}(\lambda)=\frac{(a-b)(a-b-1)}{a(a-1)}\mathbf1_{\{a-b\ge2\}}.}
\tag{4}
\]
The discontinuity means the \(\lambda=0\) model has probability zero, whereas every positive rate eventually fills the added edge if its two endpoints survive cross-part deposition.

For fixed \(\lambda>0\), the thermodynamic dependence on the relative population \(b/a\) is sharp. If \(a\to\infty\) and \(b/a\to\rho\in(0,1)\), then
\[
P_{a,b}(\lambda)\longrightarrow (1-\rho)^2.
\tag{5}
\]
If instead \(b/a\to\rho>1\), then
\[
\boxed{aP_{a,b}(\lambda)\longrightarrow\lambda\left[1-(\rho-1)\log\frac{\rho}{\rho-1}\right].}
\tag{6}
\]
Exactly on the balanced line \(a=b\), \(aP_{a,a}(\lambda)\to\lambda\). The sharp critical window joining these regimes has width \(\sqrt a\): if \((a-b)/\sqrt a\to c\in\mathbb R\), then
\[
\boxed{aP_{a,b}(\lambda)\longrightarrow\lambda+(\max\{c,0\})^2.}
\tag{7}
\]
Equations (1)--(7), including the exact finite jamming-count response, are the single combined finding.

## Assumptions and scope

The process starts with all vertices free. Its clocks are continuous-time exponential attempts: successful attempts occupy both endpoints, and later unsuccessful attempts have no effect. Rate \(\lambda\) is a fixed real positive number, independent of the system size in the large-size limits. The graph is labeled, but symmetry makes the identity of \(x,y\) irrelevant. All logarithms are natural. The limit in (7) permits either sign of \(c\). The singular statement (4) takes \(\lambda\downarrow0\) after each finite process reaches its jammed state; it does not exchange limits with physical time.

## Proof

**The independent-defect-clock coupling.** Run the pure \(K_{a,b}\) process using only its rate-one cross-edge clocks, and independently run a first exponential alarm \(\tau\) of rate \(\lambda\) for \(xy\). The added edge deposits in the full model if and only if both \(x,y\) are unmatched in the pure process at \(\tau\). This coupling is exact: before that alarm the processes coincide; after it the event is already decided. The pure process has \(k\) cross dimers for an exponentially distributed holding time of rate \(h_k=(a-k)(b-k)\), and reaches \(N\) dimers almost surely. Conditional on \(k\) cross dimers, the remaining \(a-k\) vertices in \(A\) form a uniformly random subset, independently of the holding times. Hence the survival probability for both marked vertices is \(f_k\). The chance the independent alarm first rings during stage \(k<N\) is \(L_k\lambda/(h_k+\lambda)\); its chance to outlast all \(N\) stages is \(L_N\). Summing establishes (1). Alternatively, while both marked vertices remain free, a cross dimer avoiding them has rate \((a-k-2)(b-k)\); comparing this to total rate \(h_k+\lambda\) gives (2).

**Terminal count and weak-link discontinuity.** On \(K_{a,b}\), every available cross edge remains available until one part is exhausted, so precisely \(N\) dimers deposit. If \(xy\) deposits after \(k\) cross dimers, the remaining cross graph is \(K_{a-k-2,b-k}\), and exactly \(\min(a-k-2,b-k)\) further dimers deposit. Thus the final number is \(1+\min(a-2,b)\), independently of \(k\). Subtraction gives (3), including the strict inequalities since the added edge has a positive chance to deposit and also a positive chance to be blocked. Letting \(\lambda\downarrow0\) in (1), all preterminal summands vanish and \(L_N\to1\), giving (4).

**Macroscopic imbalance.** For any \(k<N\), put \(r=a-k\) and \(d=b-a\); then
\[
\frac{f_k}{h_k+\lambda}=\frac{r(r-1)}{a(a-1)[r(r+d)+\lambda]}.
\tag{8}
\]
If \(\rho<1\), let \(s=a-b\sim(1-\rho)a\). Since
\[
0\le -\log L_b\le\lambda\sum_{j=1}^{b}\frac{1}{j(s+j)}\le\frac{\lambda H_b}{s}=o(1),
\]
the terminal term \(f_bL_b\to(1-\rho)^2\). Dropping \(L_k\le1\) and \(\lambda\) from the denominator bounds the nonterminal sum by
\[
\frac{\lambda}{a(a-1)}\sum_{j=1}^{b}\frac{s+j-1}{j}
=\frac{\lambda[b+(s-1)H_b]}{a(a-1)}=O(\log a/a),
\]
proving (5). If \(\rho>1\), put \(d=b-a\sim(\rho-1)a\). Here \(f_N=0\) and \(-\log L_N\le\lambda H_a/d=o(1)\), uniformly controlling the holding-time factors. Formula (8) becomes a Riemann sum, proving (6) by evaluation of \(\int_0^1 t/(t+\rho-1)\,dt\).

**The square-root window.** Suppose \((a-b)/\sqrt a\to c\), and separate (1) into the nonterminal sum \(S\) and terminal term \(T=f_NL_N\). On the bulk indices with \(r=a-k\ge\varepsilon a\), for any fixed \(\varepsilon>0\), the factors \(L_k\to1\) uniformly, \(d/a\to0\), and each summand in (8) is \((1+o(1))/[a(a-1)]\). Therefore \(\liminf aS\ge\lambda(1-\varepsilon)\). If \(b\ge a\), the full sum satisfies \(S\le\lambda/(a-1)\). If \(b<a\), writing \(s=a-b=O(\sqrt a)\), the full sum satisfies
\[
S\le\frac{\lambda}{a(a-1)}\sum_{j=1}^{b}\frac{s+j-1}{j}
\le\frac{\lambda[b+sH_b]}{a(a-1)};
\]
thus \(\limsup aS\le\lambda\), because \(sH_b=o(a)\). Let \(\varepsilon\downarrow0\), obtaining \(aS\to\lambda\). For \(c\le0\), \(aT\to0\) because \(f_N=0\) or \(f_N=o(1/a)\). For \(c>0\), \(s\sim c\sqrt a\) and \(-\log L_b\le\lambda H_b/s\to0\), so \(aT=a f_bL_b\to c^2\). This proves (7); choosing \(c=0\) includes the exactly balanced line.

## Verification

The standalone file `verify_defect.py` independently enumerates all residual vertex-subset states, branches on every currently available edge with its actual rate, and computes the added-edge event probability as an exact rational number. It compared the result with formula (2) for \(2\le a\le6\), \(1\le b\le6\), and four rational rates, totaling 120 independent parameter comparisons and 13,564 memoized states. All agreed. The file `verify_asymptotic.py` evaluates the finite product recurrence numerically for size up to 16,000 to stress-test (5)--(7), without treating those finite checks as an infinite proof. Both files run using Python 3's standard library only:

```sh
python3 verify_defect.py
python3 verify_asymptotic.py
```

Sample exact probabilities: \(P_{2,2}(1)=1/5\), \(P_{3,1}(1)=1/2\), and \(P_{4,6}(1)=13/150\). Proof of the infinite statements is analytical, not experimental.

## Relationship to prior work

The standard dimer RSA model and its relation to greedy matchings are classical. Cadilhe, Araújo and Privman's review (first public arXiv release 15 November 2006) documents lattice adsorption, jammed states and patterned substrates; its primary full text concerns Euclidean lattices and Bethe-lattice patterning, not the present two-population complete bipartite graph with an intra-part defect. Pippenger's 1989 paper considers graph adsorption including edge dimers, but available bibliographic text emphasizes regular high-girth and sparse-cycle graphs, not this exact defect family. Dyer and Frieze's 1991 randomized greedy-matching work concerns general performance and sparse graph bounds, not this exact event law. Arnosti (2021 first online) analyzes random-edge greedy matching on bipartite random graphs, whose edge set is still bipartite; the single added intra-part edge breaks that hypothesis. These methods motivate the model but do not by the inspected statements imply the exact asymmetric defect probability, the three-valued jamming response, or the \(\sqrt a\) crossover.

## Limitations

Historical originality is provisional: unavailable full text of Pippenger (1989) and Dyer--Frieze (1991), and possible unindexed equivalent formulations of randomized matching with one nonbipartite edge, remain priority risks. The result treats one distinguished defect edge and fixed positive cross-edge rate, not several defects, arbitrary spatial heterogeneity, or finite-time coverage trajectories. The two critical limits concern eventual jamming; none asserts finite-time robustness to an arbitrarily small defect rate. No independent external audit is represented.

## References

1. A. Cadilhe, N. A. M. Araújo, and V. Privman, *Random Sequential Adsorption: From Continuum to Lattice and Pre-Patterned Substrates*, arXiv:cond-mat/0611413, first public 2006-11-15, https://arxiv.org/abs/cond-mat/0611413.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. **2** (1989), 393--401, https://doi.org/10.1137/0402034.
3. M. Dyer and A. Frieze, *Randomized Greedy Matching*, Random Structures & Algorithms **2** (1991), 29--45, https://doi.org/10.1002/rsa.3240020104.
4. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems **12** (2022), 133--150; first online 2021-11-02, https://doi.org/10.1287/stsy.2021.0082.
