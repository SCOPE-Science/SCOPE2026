# Arbitrarily large topological entropy with almost-sure superattracting endpoint cycles in a resonant sine map

## Finding

For every odd integer \(m\ge3\), let \(k=\pi m/2\) and consider the analytic interval map
\[
f_m:[-1,1]\longrightarrow[-1,1],\qquad f_m(x)=\sin(kx).
\]
Then \(h_{\mathrm{top}}(f_m)=\log m\), while almost every initial state converges to a superattracting endpoint orbit. More precisely:

1. When \(m\equiv1\pmod4\), both \(-1\) and \(1\) are superattracting fixed points. Their two physical measures are \(\delta_{-1}\) and \(\delta_1\), with basins of normalized Lebesgue measure \(1/2\) each.
2. When \(m\equiv3\pmod4\), the endpoints form one superattracting period-two orbit. The only physical measure is \((\delta_{-1}+\delta_1)/2\), with full normalized Lebesgue basin.
3. The exceptional noncaptured set \(E_m\), defined below, has zero Lebesgue measure, is uniformly expanding with explicit expansion \(\sqrt{2-k^{-2}}>1\) per step, and supports the remaining repelling dynamics. In both cases the derivative Lyapunov exponent is \(-\infty\) for almost every initial state.

The divergence \(h_{\mathrm{top}}(f_m)=\log m\to\infty\) coexists with purely atomic physical statistics and superattracting convergence. This is an exact resonant parameter family within the published single-sine map, not an assertion about generic frequency or phase.

## Assumptions and scope

The source's single-sine map is \(f(x)=A\sin(\omega_1(x-\varphi))\). Fix \(A=1\), \(\varphi=0\), and \(\omega_1=\pi m/2\) for odd integers \(m\ge3\). Initial states are arbitrary in the closed forward-invariant interval \(I=[-1,1]\). A physical measure is an invariant probability whose empirical-measure basin has positive Lebesgue measure. Define
\[
\delta=k^{-2},\quad U_m=\{x\in I:|x|>1-\delta\},\quad E_m=\bigcap_{j\ge0}f_m^{-j}(I\setminus U_m).
\]
A derivative Lyapunov exponent means \(\lim_{n\to\infty}n^{-1}\log |(f_m^n)'(x)|\), in the extended real line. Exact capture points at critical preimages have exponent \(-\infty\) by definition.

## Proof

**Exact entropy.** The \(m-1\) interior critical points are \((2j+1)/m\) for the appropriate consecutive integers \(j\); together with \(\pm1\) they partition \(I\) into \(m\) monotonic laps. Every lap is mapped exactly onto \(I\), and its endpoint images alternate between \(-1\) and \(1\). Induction on full inverse branches gives exactly \(m^n\) monotonic laps of \(f_m^n\): each old lap is mapped onto \(I\) and splits into \(m\) new full laps. The Misiurewicz–Szlenk lap-growth characterization for continuous piecewise monotone interval maps therefore gives \(h_{\mathrm{top}}(f_m)=\lim_{n\to\infty}n^{-1}\log(m^n)=\log m\).

**Endpoint capture.** Since \(k=\pi m/2\) is an odd multiple of \(\pi/2\), \(f_m(1)=(-1)^{(m-1)/2}\) and \(f_m(-1)=-f_m(1)\); both derivatives vanish at both endpoints. If \(x\) has endpoint distance \(d=1-|x|<\delta\), then \(|f_m(x)|=|\cos(kd)|\), and, since \(kd<k\delta=1/k<\pi/2\),
\[
0\le d'=1-|f_m(x)|=1-\cos(kd)\le\tfrac12 k^2 d^2.
\]
Thus \(U_m\) is forward invariant. With \(e=(k^2/2)d\), successive captured distances satisfy \(e_{j+1}\le e_j^2\) and initially \(e_0<1/2\). Consequently after \(j\) captured steps,
\[
d_j\le(2/k^2)2^{-2^j},
\]
which proves convergence at least doubly exponentially to the parity-determined endpoint orbit. Also \(|f_m'(x_j)|=k|\sin(kd_j)|\le k^2d_j\), so the time-average logarithmic derivative tends to \(-\infty\).

**Explicit complementary expansion.** For \(x\in E_m\), both \(x\) and \(f_m(x)\) lie outside \(U_m\). Using \(\cos^2(kx)=1-\sin^2(kx)\),
\[
|f_m'(x)|^2=k^2(1-f_m(x)^2)\ge k^2\{1-(1-k^{-2})^2\}=2-k^{-2}>1.
\]
Iteration yields \(|(f_m^n)'(x)|\ge(2-k^{-2})^{n/2}\) everywhere on \(E_m\). The set is compact and forward invariant. It contains no interval, because every nondegenerate interval contained in \(E_m\) would have iterated length exceeding \(|I|=2\) by uniform expansion, noting that derivative signs do not change within the interval since critical points map immediately into \(U_m\).

**Null exceptional set.** Apply the standard one-dimensional bounded-distortion lemma: for a \(C^2\) interval map, any compact forward-invariant uniformly expanding set that avoids critical points and has no interval has Lebesgue measure zero. For clarity, its usual proof uses bounded distortion on pullbacks of uniformly sized neighborhoods around iterates of a Lebesgue density point: positive measure would force a whole neighborhood inside the invariant expanding set, contradicting empty interior. In the present case \(f_m\) is analytic, \(E_m\) avoids all critical points, and the preceding uniform expansion and no-interval properties verify the lemma's hypotheses. Thus \(\operatorname{Leb}(E_m)=0\).

**Physical measures.** Every \(x\notin E_m\) eventually enters \(U_m\), after which the established estimate gives endpoint convergence. For \(m\equiv3\pmod4\), the empirical averages tend to the unique uniform measure on the two-cycle. For \(m\equiv1\pmod4\), each initial point selects one endpoint. Since \(f_m\) is odd, reflection exchanges the two basins while preserving Lebesgue measure. Their union has full measure, so each basin has normalized measure \(1/2\). No other invariant probability has a positive-measure empirical basin because almost every initial point already has one of those atomic limits.

## Verification

The accompanying standalone `VERIFY.py` checks the exact critical-point count, the alternating images of lap endpoints, endpoint parity, the trapping inequality, and the explicit derivative expansion bound for the frequencies \(m\in\{3,5,7,9,13,21\}\). It also performs finite sample capture checks without treating samples as a proof. It passes 2,807 assertions/checks in a deterministic Python run. The infinite entropy, full-measure and exponent claims depend on the analytic argument above, not on finite testing.

## Relationship to prior work

Ali Ali, Sriram, Natiq, Ahmadi, Rajagopal and Jafari introduce the map \(f(x)=A\sin(\omega_1(x-\varphi))\) and report numerical parameter-dependent stability, bifurcations and chaotic behavior. Their published analysis does not state the present odd-integer resonance family, its global physical-basin classification or its entropy–physical-exponent divergence. The entropy calculation uses the classical lap-growth theorem; the null exceptional-set conclusion uses standard expanding-set bounded distortion. Neither general tool is asserted new. Prior published work on full-branch, postcritically finite and expanding interval dynamics establishes the conceptual setting; the precise formula and parity-indexed global classification for this source's parameterized sine map is the proposed contribution. Related published constructions with entropy–physical-statistics separation concern different recurrence equations.

## Limitations

The conclusion is restricted to exactly resonant odd-integer frequencies and phase zero, and makes no claim of robustness under parameter perturbation. The exceptional set can support nonphysical invariant measures. The phrase “only physical measures” does not mean “only invariant measures.” A standard bounded-distortion lemma is used explicitly rather than reproduced from first principles. No claims are made about digital rounding, cryptographic use or hardware behavior. An independent mathematical audit has not yet been performed. Literature searches cannot exclude unindexed equivalent prior results.

## References

- A. M. Ali Ali, S. Sriram, H. Natiq, A. Ahmadi, K. Rajagopal and S. Jafari, *A novel multi-stable sinusoidal chaotic map with spectacular behaviors*, Communications in Theoretical Physics 75 (2023), 115001. DOI: https://doi.org/10.1088/1572-9494/acf307. Publisher records “Published” 2023-11-01.
- M. Misiurewicz and W. Szlenk, *Entropy of piecewise monotone mappings*, Studia Mathematica 67 (1980), 45–63. Classical lap-growth theorem.
- W. de Melo and S. van Strien, *One-Dimensional Dynamics*, Springer, 1993. Standard interval-map distortion and hyperbolic-set methods.
- M. Demers, *Markov Extensions for Dynamical Systems with Holes: An Application to Expanding Maps of the Interval*, 2004, https://arxiv.org/abs/math/0404255. Context for interval systems with holes, not the same conclusion.
