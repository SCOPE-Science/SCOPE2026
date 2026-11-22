# Poisson cycle lengths and exponential periodic mass for products of uniform finite retractions

## Finding
Let \(F_n\) and \(G_n\) be independent and uniform among all idempotent functions on \([n]\), and let \(T_n=F_n\circ G_n\). Every common fixed point is a fixed point of \(T_n\). Let \(C_{n,r}\) count length-\(r\) directed cycles of \(T_n\) other than these common fixed points, and let \(S_n=\sum_{r\ge1}rC_{n,r}\) count the remaining periodic vertices.

The point process \(\Xi_n=\sum_{r\ge1}C_{n,r}\delta_{r/\log n}\) converges vaguely on \((0,\infty)\) to a Poisson random measure of intensity \(e^{-2t}\,dt/t\). Consequently, for every \(x>0\),
\[
\lim_{n\to\infty}\Pr\!\left(\max\{r:C_{n,r}>0\}/\log n\le x\right)
=\exp\!\left(-\int_x^\infty\frac{e^{-2t}}{t}\,dt\right),
\]
where an empty maximum is zero. Moreover,
\[
\frac{S_n}{\log n}\ \xrightarrow{\mathrm d}\ \operatorname{Exp}(2),
\]
with rate-two exponential law, and for any fixed \(s\), the vector \((C_{n,1},\ldots,C_{n,s})\) converges to independent Poisson variables with means \((1,1/2,\ldots,1/s)\).

There is a finite-size exact conditional factorial-moment identity. Write \(K=|\operatorname{Fix}(F_n)|\), \(L=|\operatorname{Fix}(G_n)|\), \(h=|\operatorname{Fix}(F_n)\cap\operatorname{Fix}(G_n)|\), and \(a=K-h\), \(b=L-h\). For any finitely supported collection of integers \(q_r\ge0\), with \(m=\sum_{r\ge1}rq_r\),
\[
\mathbb E\!\left[\prod_{r\ge1}(C_{n,r})_{q_r}\mid K,L,h\right]
=\frac{(a)_m(b)_m}{(KL)^m}\prod_{r\ge1}r^{-q_r}.
\]
Here \((z)_m=z(z-1)\cdots(z-m+1)\) is the falling factorial, \((z)_0=1\), and \((z)_m=0\) for integers \(m>z\).

## Assumptions and scope
An idempotent map is a function \(f:[n]\to[n]\) with \(f\circ f=f\). Its image equals its set of fixed points; conditional on a nonempty specified image, every element outside the image independently chooses one image point uniformly. Both maps are sampled independently from the **uniform distribution over all labeled idempotent functions**, not by first choosing their image sizes uniformly. Composition means \(T_n(x)=F_n(G_n(x))\). Every claim holds along all integers \(n\to\infty\); the finite identity holds for every \(n\ge1\), every feasible pair of image sizes and intersection size, and every finite family of nonnegative factorial-moment exponents. The limit concerns only noncommon cycles; the common fixed points are explicitly excluded. Point-process convergence is vague, thus on compact subintervals bounded away from zero.

## Proof
**1. Exact alternating-cycle representation.** Fix the two root sets \(R_F,R_G\), of sizes \(K,L\). Set \(A=R_F\setminus R_G\), \(B=R_G\setminus R_F\), and \(H=R_F\cap R_G\). The map \(T_n\) has its image in \(R_F\). Every vertex of \(H\) is fixed by both maps. If a noncommon vertex belongs to a nontrivial periodic orbit of \(T_n\), it must lie in \(A\); its image under \(G_n\) cannot lie in \(H\), since \(F_n\) fixes \(H\), so its intermediate image lies in \(B\). For a noncommon fixed point the same argument forces an alternating two-edge excursion \(A\to B\to A\). Thus length-\(r\) noncommon cycles correspond bijectively to directed alternating cycles through \(r\) distinct points of \(A\) and \(r\) distinct points of \(B\), with prescribed \(G_n\)-edges from \(A\) to \(B\) and prescribed \(F_n\)-edges from \(B\) to \(A\). Every such edge occurs independently with respective probabilities \(1/L\) and \(1/K\). Choosing and ordering \(m\) distinct points of each side in a prescribed collection of labeled cycles gives \((a)_m(b)_m\) possibilities; dividing by the \(r\) cyclic rotations of each size-\(r\) cycle gives \(\prod r^{-q_r}\). Multiplication by \((KL)^{-m}\) proves the stated factorial-moment identity. The result depends on root sets only through \(K,L,h\).

**2. Concentration of the random root sizes.** A uniform idempotent map has exactly \(k\) fixed points with weight \(w_n(k)=\binom nk k^{n-k}\), for \(1\le k\le n\). Directly,
\[
\frac{w_n(k+1)}{w_n(k)}=\frac{n-k}{k(k+1)}\left(1+\frac1k\right)^{n-k-1}.
\]
This ratio decreases in \(k\). If \(k\sim c n/\log n\), for fixed \(c>0\), its logarithm equals \((1/c-1)\log n+O(\log\log n)\). For every fixed \(\epsilon\in(0,1)\), the ratio is therefore at least \(n^{\delta}\) below \((1-\epsilon)n/\log n\), and at most \(n^{-\delta}\) above \((1+\epsilon)n/\log n\), for some \(\delta>0\) and all sufficiently large \(n\). Comparing each tail to a geometric series and to an interior weight proves \(K\log n/n\to1\) in probability; the same holds for \(L\).

Conditional on \(K,L\), the root sets are independent uniform subsets, so \(h\) is hypergeometric with mean \(KL/n\) and variance at most \(KL/n\). As \(KL/n\sim n/(\log n)^2\to\infty\), Chebyshev's inequality gives \(h/(KL/n)\to1\) in probability. Consequently,
\[
q_n:=\frac{ab}{KL}=\left(1-\frac hK\right)\left(1-\frac hL\right),
\quad -\log(q_n)\log n\ \xrightarrow{\Pr}\ 2,
\quad \min(a,b)\xrightarrow{\Pr}\infty.
\]
All logarithms in this step are evaluated on the event \(a,b>0\), whose probability tends to one.

**3. Poisson spectrum on the logarithmic cycle scale.** From the conditional identity,
\[
\mathbb E[C_{n,r}\mid K,L,h]=\frac1r\frac{(a)_r(b)_r}{(KL)^r}\le\frac{q_n^r}{r}.
\]
For \(r=O(\log n)\) and any fixed number of jointly marked cycles, the falling-factorial correction satisfies
\[
\frac{(a)_m(b)_m}{(ab)^m}=1+O\!\left(\frac{m^2}{\min(a,b)}\right)=1+o_{\Pr}(1)
\]
uniformly for \(m=O(\log n)\). Thus the conditional mixed factorial moments of cycle counts in disjoint compact length windows \(I_i\subset(0,\infty)\) are asymptotic to those of independent Poisson variables with conditional means \(\sum_{r/\log n\in I_i}q_n^r/r\). Riemann sums and the root estimate imply the means converge in probability to \(\lambda_i=\int_{I_i}e^{-2t}\,dt/t\). On the event that the root sizes and overlap satisfy their concentration estimates, these conditional mixed factorial moments converge to the independent Poisson mixed factorial moments; the conditional laws therefore converge by the multivariate factorial-moment criterion. Because the event has probability tending to one and bounded test functions are dominated, mixing the conditional laws does not require control of moments on the exceptional root-size event. The standard locally finite point-process criterion gives the claimed vague convergence. For every fixed \(r\), the same identity with fixed exponents has limit \(\prod r^{-q_r}\), proving independent Poisson limits for the finite short-cycle vector.

**4. The largest cycle and periodic mass.** For any \(M>0\), conditional Markov's inequality and the first-moment bound give
\[
\Pr(\exists r>M\log n:C_{n,r}>0\mid K,L,h)
\le\sum_{r>M\log n}\frac{q_n^r}{r}.
\]
On any event where \(q_n\le\exp[-(2-\eta)/\log n]\), the right side is bounded asymptotically by \(\int_M^\infty e^{-(2-\eta)t}\,dt/t\). Its limit tends to zero as \(M\to\infty\), while the event has probability tending to one for every \(\eta>0\). This proves the largest-cycle formula.

For \(S_n/\log n\), truncate to cycles with \(\epsilon\log n\le r\le M\log n\), where the Poisson-process convergence applies. The expected scaled mass from shorter cycles, conditionally on every pair of root sets, is at most \(\epsilon+1/\log n\). The expected scaled mass above \(M\log n\), on the preceding high-probability event, is bounded by \((\log n)^{-1}\sum_{r>M\log n}e^{-(2-\eta)r/\log n}\), which tends to \(e^{-(2-\eta)M}/(2-\eta)\). Markov's inequality followed by \(\epsilon\downarrow0\), \(M\uparrow\infty\) proves convergence to the sum of points of the limiting process. Its Laplace transform is
\[
\exp\!\left(\int_0^\infty\frac{e^{-st}-1}{t}e^{-2t}\,dt\right)
=\frac{2}{2+s},\qquad s\ge0,
\]
using the elementary Frullani integral. This identifies the rate-two exponential law.

## Verification
A standalone standard-library Python verifier exhaustively enumerates all idempotent maps through \(n=5\), all \(40{,}207\) ordered pairs across those sizes, and compares their directly extracted noncommon cycles against the exact conditional factorial-moment formula in every feasible root-size/intersection stratum. Seven moment tests are evaluated in every stratum, including cross-length mixed moments. The package checker reports \(40{,}837\) exact assertions. These computations test the finite identity, not the infinite-dimensional limit, which follows from the proof above. Run `python3 verification/check_cycles.py`.

## Relationship to prior work
The count \(\sum_{k=1}^n\binom nk k^{n-k}\) of labeled idempotent maps, also called retractions, is classical and is not claimed as new. Hansen and Jaworski (2000) study unrestricted independent bipartite random mappings, proving Poisson–Dirichlet limits for normalized connected-component sizes. Their unrestricted model has no shared fixed-point roots that absorb alternating paths; it does not supply the above logarithmic killed-cycle point process or the finite conditional moment law. Brown and Higgins (1988) study uniformly sampled unrestricted transformations and their iterates rather than the product of two uniformly sampled retractions. Dalal and Schmutz (2002) study compositions of unrestricted random functions. Lugo (2009) and Kammoun–Maïda (2019) analyze products of random permutations, including involutions; permutation products have no absorbing root sets and do not imply the present killed-cycle result. The new claim is specific to the random idempotent composition and the associated absorbing overlap geometry, not a rephrasing of the classic bipartite component or general random-mapping limit.

## Limitations
The result does not describe the distribution of nonperiodic transient branches of \(T_n\), nor the number of common-root fixed points, whose scale is much larger than that of the additional periodic mass. Vague convergence alone does not assert convergence of the total point-process count, which diverges near zero. The novelty assessment is qualified by possible general killed-bipartite-mapping theorems not identified in the consulted literature. There has been no independent mathematical audit or external certification.

## References
1. Jennie Hansen and Jerzy Jaworski, *Large components of bipartite random mappings*, Random Structures & Algorithms 17 (2000), 317–342. First online 2000-11-03. https://doi.org/10.1002/1098-2418(200010/12)17:3/4%3C317::AID-RSA7%3E3.0.CO;2-7
2. William F. Brown and P. M. Higgins, *Finite full transformation semigroups as collections of random functions*, Glasgow Mathematical Journal 30 (1988), 203–211. https://doi.org/10.1017/S0017089500007230
3. Robert Dalal and Eric Schmutz, *Compositions of random functions on a finite set*, Electronic Journal of Combinatorics 9 (2002), R26. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1r26
4. Michael Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604 (2009). https://arxiv.org/abs/0911.3604
5. Mohamed Slim Kammoun and Mylène Maïda, *A product of invariant random permutations has the same small cycle structure as uniform*, arXiv:1910.04031 (2019). https://arxiv.org/abs/1910.04031
6. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), chapters on labeled mappings and idempotents. https://ac.cs.princeton.edu/home/AC.pdf
