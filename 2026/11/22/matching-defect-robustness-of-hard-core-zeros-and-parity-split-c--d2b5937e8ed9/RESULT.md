# Matching-defect robustness of hard-core zeros and parity-split crown-edge scales

## Finding

Let \(G_{n,k}\) be the balanced complete bipartite graph with \(n\) vertices on each shore, from which precisely \(k\) pairwise vertex-disjoint cross-edges have been deleted. For each integer \(n\ge3\) and \(1\le k\le n\), its grand-canonical hard-core partition function is
\[
Z_{n,k}(z)=2(1+z)^n-1+kz^2.
\]
Every complex zero \(z\) of this polynomial lies **strictly in the open left half-plane** \(\operatorname{Re}z<0\). It has exactly two distinct negative real zeros when \(n\) is even, and exactly three when \(n\) is odd; for \(k=1\), one is precisely \(z=-1\), while the same parity census applies.

For the crown-graph case \(k=n\), write the two roots in \((-1,0)\) as \(-x_{n,1},-x_{n,2}\), ordered by \(0<x_{n,1}<x_{n,2}<1\). Then
\[
nx_{n,1}\longrightarrow\log2,\qquad \sqrt n\,x_{n,2}\longrightarrow1.
\]
If \(n\) is odd, the unique third real zero is \(-x_{n,3}\) with \(x_{n,3}>1\), and
\[
x_{n,3}=2+\frac{\log(2n)}{n}+o(n^{-1})
\quad\text{along odd }n\longrightarrow\infty.
\]
The complex fugacity zeros near the physical origin exhibit a lattice limit: for every fixed integer \(j\), there is a zero \(z_{n,j}\) (for all sufficiently large \(n\)) such that
\[
nz_{n,j}\longrightarrow-\log2+2\pi i j.
\]
The \(j=0\) zero is the first real zero above. These claims concern finite partition-function zeros and their continuation; no positive-real-fugacity phase transition is asserted.

## Assumptions and scope

A configuration is an independent vertex subset \(S\subseteq V(G_{n,k})\). The activity \(z\) is a formal complex fugacity, with physical hard-core probability proportional to \(z^{|S|}\) only when \(z>0\). Every retained edge excludes simultaneous occupation of its endpoints. All deleted edges are a matching; the claim does not extend to arbitrary \(k\) deleted edges that share endpoints. Graphs are finite, simple and labeled. The zero counts distinguish distinct roots, not multiplicities; \(n\ge3\) and \(1\le k\le n\) are mandatory.

## Proof

**1. Exact partition polynomial.** An independent set contained in either one shore contributes \(2(1+z)^n-1\), with the empty set counted once. An independent set meeting both shores can contain exactly one vertex from each: these two must be endpoints of one of the \(k\) deleted edges. No larger mixed independent set exists, because deleted edges share no endpoints and all other cross-edges are present. Hence the additional contribution is \(kz^2\). The formula for \(k=n\) agrees with the known crown-graph independence-polynomial table; the enumerator itself is not claimed as new.

**2. Strict complex half-plane bound.** If \(\operatorname{Re}z\ge0\), then \(|1+z|^2=1+2\operatorname{Re}z+|z|^2\ge1+|z|^2\). As \(n\ge3\), Bernoulli's inequality gives
\[
2|1+z|^n\ge2(1+|z|^2)^{n/2}\ge2+n|z|^2
\ge2+k|z|^2>1+k|z|^2\ge|kz^2-1|.
\]
Therefore \(Z_{n,k}(z)\ne0\) on the closed right half-plane, proving strict stability independently of any spectral calculation.

**3. Exactly two or three real zeros.** All real zeros are negative because \(Z_{n,k}(x)>0\) for \(x\ge0\). Write \(z=-x\), \(x>0\), and \(f(x)=2(1-x)^n+kx^2-1\). On \([0,1]\),
\[
f''(x)=2n(n-1)(1-x)^{n-2}+2k>0.
\]
We have \(f(0)=1\), \(f(1)=k-1\ge0\), and \(f(1/n)<0\). For \(n=3\), the last assertion follows from \(2(2/3)^3+3/9<1\); for \(n\ge4\), it follows from \(2(1-1/n)^n+k/n^2\le2/e+1/n\le2/e+1/4<1\). Strict convexity implies exactly two distinct zeros in \((0,1]\), with the second equal to \(1\) only when \(k=1\). For even \(n\), \(f(x)=2(x-1)^n+kx^2-1>0\) for \(x>1\), so there are no others. For odd \(n\) and \(x>1\),
\[
f'(x)=2kx-2n(x-1)^{n-1}.
\]
The quotient \((x-1)^{n-1}/x\) increases strictly from zero to infinity on \((1,\infty)\), since its logarithmic derivative is \((n-1)/(x-1)-1/x>0\). Thus \(f\) initially increases, reaches one maximum, and then decreases to \(-\infty\). Because \(f(1)=k-1\ge0\), it has exactly one zero strictly above \(1\). The claimed parity census follows.

**4. Crown negative-zero scales.** Let \(k=n\). For fixed \(u>0\),
\[
f(u/n)=2(1-u/n)^n+u^2/n-1\longrightarrow2e^{-u}-1.
\]
Bracketing the smallest root around the unique zero \(u=\log2\) proves \(nx_{n,1}\to\log2\). For fixed \(c>0\),
\[
f(c/\sqrt n)=2(1-c/\sqrt n)^n+c^2-1\longrightarrow c^2-1,
\]
so bracketing the second root for \(c<1\) and \(c>1\) proves \(\sqrt n\,x_{n,2}\to1\). Along odd \(n\), for every fixed \(0<\delta<1\), \(f(2-\delta)>0\) and \(f(2+\delta)<0\) for sufficiently large \(n\), because exponential terms respectively decay and dominate the polynomial term. Thus \(x_{n,3}\to2\). At that root, the defining equation gives \(2(x_{n,3}-1)^n=nx_{n,3}^2-1\). Taking logarithms,
\[
n\log(x_{n,3}-1)=\log(nx_{n,3}^2-1)-\log2=\log(2n)+o(1).
\]
Exponentiation and \(\log(2n)/n\to0\) yield \(x_{n,3}=2+\log(2n)/n+o(n^{-1})\).

**5. Edge lattice of complex zeros.** The entire functions \(u\mapsto Z_{n,n}(u/n)\) converge locally uniformly on \(\mathbb C\) to \(2e^u-1\). The limit has isolated simple zeros \(-\log2+2\pi ij\) for \(j\in\mathbb Z\). Rouché's theorem on disjoint small circles around each fixed limit zero (or Hurwitz's theorem) provides exactly one nearby zero for sufficiently large \(n\) and proves its rescaled limit. These statements concern each fixed \(j\), not a uniform approximation to all \(n\) zeros.

## Verification

The standalone Python file `verify_hardcore_crown.py` checks the labeled independent-set generating polynomial by direct subset enumeration for \(3\le n\le7\) and all \(1\le k\le n\), exact Sturm real-root counts for \(3\le n\le14\), strict nonvanishing at sampled closed-right-half-plane points, and numerical instances of the crown-root asymptotics and complex edge lattice. Run `python verify_hardcore_crown.py` in an environment with SymPy and mpmath. A completed replay reported `CROWN_HARD_CORE_CHECKS_PASSED 156`. Finite checks are supplemental; the proof above is independent of enumeration.

## Relationship to prior work

The known exact crown independence polynomial \(2(1+z)^n+nz^2-1\) is tabulated by MathWorld, so that formula alone is not new. Brown and Cameron's 2018 treatment studies broad Hurwitz stability, including balanced complete multipartite graphs and vertex graph operations, but does not establish the uniform matching-edge-deletion stability or the parity-resolved real-zero and asymptotic classifications here. Chen, Ning and Tu's 2025 full text proves balanced complete bipartite stability and several unbalanced results, but its exact objects have **all** cross-edges and do not imply stability after matching deletion. Levit and Mandrescu's 2009 independence-polynomial preprint is background on the polynomial and evaluations at negative fugacity, not evidence for this all-zero result. These comparisons are not a proof of historical priority.

## Limitations

No theorem about arbitrary edge-deletion configurations, asymmetric shore sizes or nonuniform activities is asserted. The complex edge scaling is pointwise in each fixed integer mode. The complete half-plane result is qualitative, not a uniform spectral gap to the imaginary axis as \(n\to\infty\). The earlier crown enumerator is credited; independent expert review and historical-priority confirmation remain outstanding.

## References

- V. E. Levit and E. Mandrescu, *The independence polynomial of a graph at -1*, arXiv:0904.4819, first public preprint 2009-04-30. https://arxiv.org/abs/0904.4819
- J. I. Brown and B. Cameron, *On the Stability of Independence Polynomials*, first arXiv preprint 2018-02-07, subsequently Electron. J. Combin. 25(1), P1.46. https://arxiv.org/pdf/1802.02478
- G. Chen, B. Ning and J. Tu, *The stability of independence polynomials of complete bipartite graphs*, arXiv:2505.24381, posted 2025-05-30. https://arxiv.org/html/2505.24381
- E. W. Weisstein, *Independence Polynomial*, MathWorld, table entry for crown graphs. https://mathworld.wolfram.com/IndependencePolynomial.html
