# Field-resonant weak minima and parity-alternating complexity on complete tripartite Ising networks

## Finding

For every integer \(n\ge 1\), uniform antiferromagnetic coupling \(J>0\), and real longitudinal field \(h\), place Ising spins \(\sigma_v\in\{-1,+1\}\) on the labeled complete tripartite graph \(K_{n,n,n}\). Let \(N_n(t)\) count configurations for which **no single-spin flip decreases the Hamiltonian**, with \(t=|h|/J\). A zero-energy flip is allowed under this definition. Then the **complete field-dependent classification** is

\[
N_n(t)=\begin{cases}
6(2^n-1)+\mathbf1_{2\mid n}\binom n{n/2}^{\!3},&t=0,\\
3+3\binom nk^2+\mathbf1_{2\mid(n+k)}\binom n{(n+k)/2}^{\!3},&t=2k,\quad 1\le k\le n-1,\\
3,&0<t<2n,\quad t\notin\{2,4,\ldots,2n-2\},\\
3\cdot2^n-2,&t=2n,\\
1,&t>2n.
\end{cases}
\]

Here indicator-weighted binomial terms are included only when their lower index is an integer. The first, second, and fourth rows are exact isolated field values, not intervals. The number of **strict** single-spin local minima (all single flips increase the energy) is zero at \(t=0\) and \(t=2n\), exactly three for \(0<t<2n\), and exactly one for \(t>2n\).

For each fixed integer \(k\ge1\), along \(n>k\) with \(n\equiv k\pmod2\),
\[
\frac{\log N_n(2k)}{3n}\longrightarrow\log2;
\]
whereas along \(n\not\equiv k\pmod2\) the limit is zero. At \(t=0\), these limits are respectively \(\log2\) for even \(n\) and \((\log2)/3\) for odd \(n\). Thus the normalized configurational complexity has sharp, parity-sensitive spikes at isolated resonant fields. Every nonground weak minimum in this classification has a two-spin-flip escape sequence whose first step costs zero energy and whose second step strictly decreases the energy.

## Assumptions and scope

The three independent vertex parts, \(A,B,C\), each have exactly \(n\) **labeled** spins; every pair in different parts is connected and no pair in one part is connected. The Hamiltonian is

\[
H(\sigma)=J\sum_{uv\in E(K_{n,n,n})}\sigma_u\sigma_v-h\sum_v\sigma_v.
\]

The classification counts single-spin weak local minima, not trapping/absorbing states of stochastic zero-temperature Glauber dynamics (which may make zero-energy moves), not strict positive-barrier metastability, and not finite-temperature equilibrium phases. Degeneracies are counts of labeled spin configurations. Magnetic fields are unscaled real values; there is no implicit Curie-Weiss rescaling of \(J\) by \(n\). By the global spin-flip symmetry, the count depends only on \(t=|h|/J\).

## Proof

**1. Local stability rule.** Work with \(h\ge0\), since flipping all spins replaces \(h\) by \(-h\). Let \(a,b,c\in\{0,\ldots,n\}\) count the positive spins in the respective parts, and write their magnetizations as \(A=2a-n\), \(B=2b-n\), \(C=2c-n\). The energy divided by \(J\) is

\[
E=A B+A C+B C-t(A+B+C).
\]

Flipping a spin \(s\in\{-1,+1\}\) in part \(A\) changes the energy by \(2Js[t-(B+C)]\). Hence, if part \(A\) is all positive, stability requires \(t\ge B+C\); if it is all negative, stability requires \(t\le B+C\); if it is mixed, **both signs are present** and stability requires equality \(t=B+C\). Analogous rules hold for the other two parts. For strict stability all applicable inequalities are strict, and a mixed part is impossible.

**2. Uniform configurations.** Among the eight triples of monochromatic parts, at \(t=0\) precisely the six nonconstant triples are weakly stable. For \(0<t<2n\), precisely the three configurations with two positive parts and one negative part are weakly (indeed strictly) stable. At \(t=2n\), those three and the all-positive configuration are weakly stable. For \(t>2n\), only the all-positive configuration remains, strictly stable. This also shows that strict local minima number zero at both boundary fields and three in the open interval.

**3. Exactly one mixed part.** Suppose part \(A\) is mixed, while parts \(B,C\) are uniform. The equality \(t=B+C\) implies \(t\in\{-2n,0,2n\}\). For \(t=0\), parts \(B,C\) must be opposite, and every one of the \(2^n\) configurations of \(A\) is allowed. The six choices (free part, sign of an opposite pair) jointly describe the ground-state family, counting each of the six nonconstant monochromatic configurations twice. Thus they contribute \(6\cdot2^n-6\) distinct states, including states with no mixed part. At \(t=2n\), parts \(B,C\) must both be positive, and all \(2^n\) choices for \(A\) are allowed. The three free-part families overlap only at the all-positive configuration; their union has \(3\cdot2^n-2\) elements. No one-mixed states occur at an interior positive field.

**4. Exactly two mixed parts.** Suppose \(A\) and \(B\) are mixed and \(C\) is uniform. Their stability equalities give \(A=B=t-C\). In the open interval \(0<t<2n\), \(C=-n\) would imply \(A=B=t+n>n\), impossible. Thus \(C=n\), \(A=B=t-n\), and both mixed parts have exactly \(k=t/2\) positive spins. Such configurations exist precisely at \(t=2k\), integer \(1\le k\le n-1\). The positive uniform part's stability inequality is \(t\ge A+B=2t-2n\), automatically satisfied. Choosing which part is uniform yields \(3\binom nk^2\) distinct configurations.

**5. Three mixed parts.** The equations \(t=B+C=A+C=A+B\) imply \(A=B=C=t/2\). For \(t=0\) this requires even \(n\), with exactly \(\binom n{n/2}^3\) states. For \(t=2k\) in the interior it requires \(n\equiv k\pmod2\), with exactly \(\binom n{(n+k)/2}^3\) states. In both cases every single flip has zero energy cost. These families are disjoint from the preceding cases. The five enumerated regimes are exhaustive and yield the stated count.

**6. Strict minima and relation to ground energy.** A mixed part can never be strictly stable. The uniform-state inequalities in step 2 therefore give the strict count. For \(0<t<2n\), the three two-positive-one-negative uniform states are precisely the global ground states, with energy \(-Jn^2-hn\). To verify this, observe that the energy in the three part magnetizations is affine in each one separately; its global minimum over the cube \([-n,n]^3\) is attained at a monochromatic triple. For this open field interval, the only minimizing corners are the three two-positive-one-negative triples, and no two are joined by a cube edge on which the energy is constant. At \(t=0\) the ground states form the six free-part/opposite-part families, and at \(t=2n\) they form the three all-positive-pair/free-part families. These assertions also follow by identifying the minimum-energy cube edges using the same affine argument.

The additional weakly stable states at \(t=0\) or an interior resonant field have at least two mixed parts; they are not ground states. Choose one such mixed part and flip any of its spins. That flip has zero cost. In another mixed part, a spin with the *opposite sign to the original flipped spin* exists. Because the first flip changes its neighboring magnetization by minus twice the original sign, flipping this opposite-sign spin next changes the energy by \(-4J\). Thus every nonground weak local minimum admits a zero-cost move followed by a strictly downhill move; there is no claim it is absorbing under tie-accepting dynamics.

**7. Parity-alternating complexity.** For fixed \(k\ge1\) with \(n\equiv k\pmod2\), the three-mixed term dominates, and Stirling's formula gives

\[
\binom n{(n+k)/2}^{\!3}\sim 2^{3n}\left(\frac{2}{\pi n}\right)^{3/2}.
\]

On the opposite parity, the three-mixed term vanishes and \(N_n(2k)=3+3\binom nk^2\sim3n^{2k}/(k!)^2\), giving zero normalized logarithmic growth. For \(t=0\), the same central-binomial estimate applies on even \(n\), while on odd \(n\) one has \(N_n(0)=6(2^n-1)\). This proves the asserted limits.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently evaluates the exact stability predicates over all part magnetizations for \(1\le n\le17\) and half-integer field grids covering all critical fields, checks the strict-minimum formula, and brute-force enumerates all \(2^{3n}\) labeled spin assignments for \(n\le5\). For nonground weak minima in the brute-force range it verifies the existence of a two-step downhill path starting with a zero-cost flip. Run `python3 verify.py` from the extracted package directory; the expected output contains `PASS: 2902 independent group and full-spin assertions`.

These finite computations serve as independently implementable checks; they are not used as proofs for arbitrary \(n\) or real \(h\). Steps 1–7 give the general proof.

## Relationship to prior work

Waclaw and Burda (2008), *Counting metastable states of Ising spin glasses on arbitrary graphs*, investigate the complexity of local minima for **Gaussian random couplings**, primarily on random regular graphs and lattices. Their field-theory calculation does not state this finite, uniformly antiferromagnetic complete-tripartite formula, nor the field-resonant parity split. Pagnani, Parisi and Ratiéville (2002), *Metastable configurations on the Bethe lattice*, study finite-connectivity locally tree-like random graphs using cavity methods, including the standard weak-stability convention; the graph family and results differ. Spirin, Krapivsky and Redner (2001), *Freezing in Ising Ferromagnets*, examine Glauber kinetics of **ferromagnets** on spatial lattices and distinguish zero-energy fluctuations, but give no complete-tripartite antiferromagnet enumeration. These works provide physical motivation and terminology, not this classification. Complete-rook Ising ground-state and circular-ladder weak-stability results on different graph geometries likewise do not imply these tripartite formulas.

## Limitations

The theorem assumes exactly three equal-size parts, uniform positive coupling, labeled spins, and single-spin flips. It does not classify unequal complete-tripartite graphs, multiple-spin local minima, lifetimes, metastable stochastic absorbing sets, Gibbs states at nonzero temperature, or a thermodynamic phase transition. The normalized logarithmic counts are combinatorial complexities for this unscaled dense-graph family. The accessible primary-literature comparisons do not establish a priority guarantee over every unindexed historical source.

## References

1. B. Waclaw and Z. Burda, "Counting metastable states of Ising spin glasses on arbitrary graphs," arXiv:0801.1224v1 (first public 2008-01-08), *Physical Review E* **77**, 041114 (2008). https://arxiv.org/html/0801.1224v1
2. A. Pagnani, G. Parisi and M. Ratiéville, "Metastable configurations on the Bethe lattice," arXiv:cond-mat/0210305 (first public 2002-10-14), *Physical Review E* **67**, 026116 (2003). https://arxiv.org/abs/cond-mat/0210305
3. V. Spirin, P. L. Krapivsky and S. Redner, "Freezing in Ising Ferromagnets," arXiv:cond-mat/0105037 (first public 2001-05-02). https://arxiv.org/abs/cond-mat/0105037
