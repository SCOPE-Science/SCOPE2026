# Weak-bond spectral splitting and metastable coverage on odd reversible-dimer rings

## Finding
Fix an odd integer \(N=2m+1\ge3\). On the cycle of \(N\) binary sites, each ordinary bond \((i,i+1)\), \(1\le i<N\), converts \(00\leftrightarrow11\) at rate one in each direction; the closing bond \((N,1)\) performs the same conversion at rate \(\varepsilon\ge0\). Start from the completely empty configuration. Every change is a simultaneous adsorption or desorption of two neighboring particles. Work in the invariant even-total-occupation class, and let \(\gamma_N(\varepsilon)\) be the positive spectral gap of its continuous-time generator for \(\varepsilon>0\).

**Theorem.** At fixed odd \(N\), as \(\varepsilon\downarrow0\), exactly \(m\) positive relaxation rates tend to zero. With their increasing order labeled by \(1\le j\le m\), they satisfy
\[
\lambda_{j,N}(\varepsilon)=\frac{4j(N-j)}{N(N-1)}\varepsilon+O_N(\varepsilon^2).
\]
In particular,
\[
\boxed{\gamma_N(\varepsilon)=\frac4N\varepsilon+O_N(\varepsilon^2).}
\]
The remaining positive relaxation rates have nonzero limits. This spectral splitting is governed exactly, to first order, by a binomial reversible birth-and-death chain with jumps of size two.

Let \(\theta_{N,\varepsilon}(t)=N^{-1}\mathbb E[\sum_{i=1}^N x_i(t)]\) be the mean fractional coverage. For every fixed \(s>0\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\theta_{N,\varepsilon}(s/\varepsilon)
=\frac12-\frac{e^{-4s/N}}{2N^2}.}
\]
Moreover, the stationary limits are singular at the missing bond:
\[
\lim_{t\to\infty}\theta_{N,0}(t)=\frac12-\frac1{2N^2},\qquad
\lim_{t\to\infty}\theta_{N,\varepsilon}(t)=\frac12\quad(\varepsilon>0).
\]
All these assertions concern the same symmetric pair-adsorption/desorption model and the same initially empty parity sector.

## Assumptions and scope
Sites are numbered \(1,\ldots,N\) with \(N\) odd and at least three. An allowed reaction flips both endpoints of a bond only when their occupancies are equal. Ordinary reaction rates in both directions equal one; the distinguished closing-bond reaction has rate \(\varepsilon\), in both directions. There is no single-particle hopping, no other interaction, and no external injection. All spectral statements refer to the finite generator restricted to original configurations with an even number of occupied sites. First take \(\varepsilon\downarrow0\) at fixed \(N\); no uniformity in growing \(N\) is claimed. The time-rescaled limit holds for each fixed strictly positive \(s\), not at \(s=0\).

## Proof

**1. Exclusion transformation and communicating sectors.** Set
\[
\eta_i=\begin{cases}x_i,&i\text{ odd},\\1-x_i,&i\text{ even}.\end{cases}
\qquad K=\sum_{i=1}^N\eta_i.
\]
For each ordinary bond, \(00\leftrightarrow11\) in the original occupancies is exactly \(01\leftrightarrow10\) in \(\eta\). Therefore, at \(\varepsilon=0\), the process is the unit-rate symmetric simple exclusion process on the *path* of \(N\) sites. Its state space at any fixed number \(K=k\) is connected: adjacent transpositions move an arbitrary \(k\)-subset to any other \(k\)-subset. This gives exactly one stationary vector, uniform on \(\binom Nk\) states, for each allowed \(k\).

The original even-occupation condition is equivalent to \(K\equiv m\pmod2\). At the closing bond both endpoints have odd indices, so its reaction in the new variables is \(00\leftrightarrow11\), changing \(K\) by \(\pm2\). For \(\varepsilon>0\), the fixed-\(K\) sectors communicate in succession: every allowed \(k\le N-2\) has configurations with both endpoints vacant, and every \(k\ge2\) has configurations with both endpoints filled. Thus the full even-original-occupation chain is irreducible. All transitions have symmetric reverse rates, so the equilibrium measure is uniform on its \(2^{N-1}\) states.

**2. Effective slow generator.** Denote by \(L_0\) the generator of the path exclusion dynamics and by \(V\) the unit-rate endpoint-pair-flip generator, so that \(L_\varepsilon=L_0+\varepsilon V\). Let \(P\) be the orthogonal projection, with respect to counting measure, onto functions constant on each fixed-\(K\) sector. The projected generator \(PVP\) acts on functions \(f(k)\), where \(k\in\{0,\ldots,N\}\) and \(k\equiv m\pmod2\), by
\[
(Bf)(k)=b_k[f(k+2)-f(k)]+d_k[f(k-2)-f(k)],
\]
with out-of-range terms omitted, where
\[
b_k=\frac{\binom{N-2}{k}}{\binom Nk}
=\frac{(N-k)(N-k-1)}{N(N-1)},\quad
d_k=\frac{\binom{N-2}{k-2}}{\binom Nk}
=\frac{k(k-1)}{N(N-1)}.
\]
Indeed, after a rapid equilibration in a fixed-\(k\) sector, the probabilities that the two endpoints are both vacant or both occupied are exactly \(b_k\) and \(d_k\). This also shows that \(B\) is reversible with mass proportional to \(\binom Nk\) on the allowed parity class.

**3. Exact effective spectrum.** Consider the auxiliary hypercube process that, at total rate one, chooses an unordered pair of different bit positions uniformly and flips both. When applied to functions of the number \(k\) of occupied bits, a mixed pair leaves \(k\) unchanged; the two other cases have precisely the rates \(b_k,d_k\) above. For any set \(S\) of \(j\) coordinates, the Walsh character \(\chi_S(\eta)=(-1)^{\sum_{i\in S}\eta_i}\) changes sign exactly when one chosen position belongs to \(S\) and the other does not. Such a pair is selected with probability \(2j(N-j)/(N(N-1))\). Hence this character has eigenvalue \(-4j(N-j)/(N(N-1))\).

Averaging these characters over all size-\(j\) sets \(S\) yields the nonzero Krawtchouk polynomial
\[
H_j(k)=\sum_{\ell=0}^j(-1)^\ell\binom{k}{\ell}\binom{N-k}{j-\ell},
\qquad BH_j=-\frac{4j(N-j)}{N(N-1)}H_j.
\]
On one parity class with \(N=2m+1\), the \(m+1\) distinct eigenvalues for \(j=0,\ldots,m\) exhaust the \(m+1\)-dimensional space of sector functions (each eigenfunction remains nonzero there, since the parity-restricted Krawtchouk basis is complete). In particular the smallest nonzero value is \(4/N\), at \(j=1\).

**4. Perturbative lifting.** The finite symmetric operator \(-L_0\) is nonnegative; its zero eigenspace consists exactly of the \(m+1\) sector-constant functions, while its remaining spectrum is strictly positive by sector irreducibility. Symmetric finite-dimensional degenerate perturbation theory applied to \(-L_0-\varepsilon V\) gives \(m+1\) eigenvalues converging to zero, with first derivatives equal to the eigenvalues of \(-PVP=-B\); all other eigenvalues remain bounded away from zero. Because the \(m+1\) first-order eigenvalues are distinct, each low eigenvalue has the displayed \(O_N(\varepsilon^2)\) expansion. Zero is an exact eigenvalue at every positive rate. This proves the full low spectral classification and the gap asymptotic.

**5. Slow coverage and singular equilibrium.** The standard finite-state averaging limit for \(L_0+\varepsilon V\), obtained equivalently by decomposing into the zero-spectral projection \(P\) and its gapped orthogonal complement, implies that at times \(t=s/\varepsilon\) with fixed \(s>0\), the conditional within-sector law becomes uniform and \(K\) evolves by \(B\), initialized at \(K=m\). Direct calculation gives
\[
B k=2(b_k-d_k)=-\frac4N\left(k-\frac N2\right).
\]
Consequently \(\mathbb E K(s)=N/2-(1/2)e^{-4s/N}\). Under uniform sampling conditional on \(K=k\), an odd site has expected original occupancy \(k/N\) and an even site \(1-k/N\). Thus the expected total original occupancy is \(m+k/N\), and its division by \(N\) yields the claimed slow-time coverage limit.

When \(\varepsilon=0\), \(K=m\) forever, and the unique stationary law in that sector has coverage \((m+m/N)/N=1/2-1/(2N^2)\). For any \(\varepsilon>0\), the unique stationary law is uniform on even-original-occupation configurations; every single-site marginal is one half for \(N\ge3\). Its coverage is therefore exactly \(1/2\). The two limiting procedures are inequivalent.

## Verification
Run `python3 CHECK.py` in the same directory. The standalone checker performs exact rational and combinatorial comparisons on odd ring lengths \(N=3,5,7,9,11\), including all fixed-charge sectors, endpoint transition probabilities, communicating classes, the Krawtchouk eigenvalue equation, and both coverage plateaux. Optional NumPy checks compare the low spectrum of the *actual full finite generator* at small positive \(\varepsilon\) with its predicted first-order slopes. These are finite checks only; the proof of the all-length and small-rate asymptotic statements is analytic above.

## Relationship to prior work
Mercado *et al.* (2022 preprint, 2023 journal publication) analyze finite reversible dimer adsorption/desorption rings with uniform bonds, identify odd/even sector counts, and derive stationary coverage and correlations. The present work instead marks a distinguished *weak closing bond of an odd cycle* and determines the complete leading slow spectral splitting and resulting two-time-scale coverage. The invariant alternating-sublattice charge and the fixed-sector counting are known background, not proposed as new. Crampe *et al.* (2016) study a different dissipative exclusion process with bulk hopping and pair reactions plus reservoirs; their open-chain Bethe-equation spectrum does not directly supply the weak-endpoint-pair-flip spectrum. Mobilia (2002) analyzes a homogeneous periodic diffusion-pair-reaction process on even lattices. Chen and Stinchcombe (1994) investigate a bond defect in a **different model with single-particle diffusion**; only their abstract was accessible here, so implicit spectral overlap cannot be excluded.

## Limitations
The statement is restricted to symmetric unit adsorption/desorption rates on the ordinary bonds and a symmetric weak closing-bond rate. The perturbation is analyzed for fixed odd finite \(N\), not uniformly as \(N\to\infty\), and the complete finite-positive-\(\varepsilon\) spectrum is not asserted. The coverage scaling requires strictly positive rescaled time. The full text of Chen–Stinchcombe (1994) was not available for comparison and remains a publication-priority risk. The finite checker is corroboration, not an infinite-dimensional or all-parameter certificate. No independent scientific validation has been performed.

## References
- E. Mercado, H. T. Jung, C. Kim, A. L. Garcia, A. J. Nonaka and J. B. Bell, *Surface Coverage Dynamics for Reversible Dissociative Adsorption on Finite Linear Lattices*, arXiv:2212.12286 (first submitted 2022-12-23), J. Chem. Phys. **159**, 144107 (2023). https://arxiv.org/abs/2212.12286
- N. Crampé, E. Ragoucy, V. Rittenberg and M. Vanicat, *Integrable dissipative exclusion process: Correlation functions and physical properties*, arXiv:1603.06796 (2016). https://arxiv.org/abs/1603.06796
- M. Mobilia, *Exact multipoint and multitime correlation functions of a one-dimensional model of adsorption and evaporation of dimers*, arXiv:cond-mat/0204148 (2002). https://arxiv.org/abs/cond-mat/0204148
- N.-N. Chen and R. B. Stinchcombe, *Stochastic dynamics of diffusive deposition-evaporation processes in the presence of defects*, Phys. Rev. E **49**, 2784–2789 (1994), https://doi.org/10.1103/PhysRevE.49.2784
