# Sharp precision-sign transition for fractional circular Matérn samples

## Finding
Let \(s>1/2\), \(\kappa>0\), and let \(x_1,\ldots,x_n\) be arbitrary pairwise distinct points of the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with \(n\ge2\). Define the circular Matérn Fourier kernel and its finite covariance and precision matrices by
\[
K_{s,\kappa}(\theta)=\sum_{m\in\mathbb Z}(\kappa^2+m^2)^{-s}e^{im\theta},\qquad
\Sigma_{ij}=K_{s,\kappa}(x_i-x_j),\qquad Q=\Sigma^{-1}.
\]
Then the following sharp trichotomy holds.

**Nonlocal attractive phase.** If \(1/2<s<1\), every off-diagonal entry is **strictly negative**, \(Q_{ij}<0\) for all \(i\ne j\), for *every* choice of sites and \(\kappa\). The Gaussian vector of sampled field values has a complete positive-partial-correlation graph.

**Local endpoint.** At \(s=1\), arrange the sites in circular order \(x_1<\cdots<x_n<x_1+2\pi\) and write \(\ell_i=x_{i+1}-x_i>0\) (periodic indices). For \(i\ne j\),
\[
Q_{ij}=-\frac{\kappa}{2\pi}\sum_{\substack{a:\ \{a,a+1\}=\{i,j\}}}\frac{1}{\sinh(\kappa\ell_a)}.
\]
Thus the only nonzero off-diagonal entries correspond to neighboring sites on the cycle (two arcs contribute when \(n=2\)).

**Failure above the endpoint.** For every \(s>1\), the four sites \(0,\pi/2,\pi,3\pi/2\) admit a sufficiently small \(\kappa>0\) with \(Q_{1,3}>0\), and in fact
\[
\lim_{\kappa\downarrow0}Q_{1,3}
=\frac{2^{2s-1}-2}{16(1-2^{-2s})\zeta(2s)}>0.
\]
Consequently, the property that **all off-diagonal precision entries are nonpositive for every finite site set and every \(\kappa>0\)** holds **if and only if** \(1/2<s\le1\). The threshold \(s=1\) is sharp and the strict/non-strict sparsity distinction is also sharp.

## Assumptions and scope
The Fourier series uses Haar probability measure \(d\mu=d\theta/(2\pi)\) and Fourier coefficients \(\widehat f_m=\int f(\theta)e^{-im\theta}d\mu(\theta)\). All data and interpolation functions in the sign proof are real. The covariance is the point-evaluation kernel of \(H^s(\mathbb T)\) equipped with
\[
E_s(f)=\sum_{m\in\mathbb Z}(\kappa^2+m^2)^s|\widehat f_m|^2.
\]
Since \(s>1/2\), evaluation is bounded and the displayed covariance series converges absolutely. Every coefficient is positive, so \(\Sigma\) is strictly positive definite: for nonzero \(c\), \(c^*\Sigma c=\sum_m(\kappa^2+m^2)^{-s}|\sum_jc_je^{imx_j}|^2>0\); zero of all Fourier moments would force a finite signed measure to vanish. A Gaussian field with this covariance exists. Positive Gaussian partial correlation has sign \(-\operatorname{sgn}Q_{ij}\), and zeros in \(Q\) characterize conditional independence for the sampled Gaussian vector.

## Proof
**1. Variational trace identity.** For any real interpolation values \(v\in\mathbb R^n\), the unique minimizer of \(E_s(f)\) subject to \(f(x_i)=v_i\) lies in the span of the kernel sections. This follows directly from orthogonal projection onto the representer span in the Fourier Hilbert space. Its coefficients are \(\Sigma^{-1}v\), and its minimum squared norm is exactly
\[
\min_{f(x_i)=v_i}E_s(f)=v^{\mathsf T}Qv. \tag{1}
\]
This applies at every stated \(s>1/2\).

**2. Strict lattice inequality for \(1/2<s<1\).** Put \(A=\kappa^2-\partial_\theta^2\) and \(c_s=s/\Gamma(1-s)>0\). The spectral identity \(\lambda^s=c_s\int_0^\infty(1-e^{-t\lambda})t^{-1-s}\,dt\), combined with \(e^{-tA}=e^{-\kappa^2t}e^{t\partial_\theta^2}\), yields the exact nonlocal energy
\[
E_s(f)=\kappa^{2s}\|f\|_{L^2(\mu)}^2
+\iint_{\mathbb T^2}J_{s,\kappa}(\theta-\phi)
\bigl(f(\theta)-f(\phi)\bigr)^2\,d\mu(\theta)d\mu(\phi),\tag{2}
\]
where for distinct \(\theta,\phi\)
\[
J_{s,\kappa}(\theta-\phi)
=\frac{s}{2\Gamma(1-s)}\int_0^\infty t^{-1-s}e^{-\kappa^2t}p_t(\theta-\phi)\,dt>0,\qquad
p_t(\delta)=\sqrt{\frac\pi t}\sum_{k\in\mathbb Z}e^{-(\delta-2\pi k)^2/(4t)}.
\]
The heat kernel is strictly positive for each \(t>0\). The formula is first obtained for trigonometric polynomials; monotone convergence of nonnegative spectral and jump integrals extends it to the entire form domain. The mass term in (2) is obtained by separating \(1-e^{-t\kappa^2}\) and using the Markov heat kernel's unit mass.

For real \(u,v\in H^s\), set \(w=\min(u,v)\), \(z=\max(u,v)\), and \(d=u-v\). Pointwise \(w^2+z^2=u^2+v^2\). A direct two-point expansion gives
\[
(u_\theta-u_\phi)^2+(v_\theta-v_\phi)^2
-(w_\theta-w_\phi)^2-(z_\theta-z_\phi)^2
=|d_\theta d_\phi|-d_\theta d_\phi\ge0.\tag{3}
\]
In particular \(w,z\in H^s\) by (2), and integration proves
\[
E_s(u)+E_s(v)\ge E_s(w)+E_s(z),\tag{4}
\]
with **strict inequality** whenever \(d\) takes both strictly positive and strictly negative values on nonempty open sets. Indeed the strictly positive heat-derived jump kernel integrates (3) to a strictly positive number over the Cartesian product of those sets, which may be chosen separated from the diagonal.

Now take \(u\) and \(v\) to be the minimal-energy interpolants of the distinct standard basis vectors \(e_i\) and \(e_j\). They are continuous, with \((u-v)(x_i)=1\), \((u-v)(x_j)=-1\); therefore (4) is strict. At all sampling sites, \(w\) has interpolation data \(0\) and \(z\) has data \(e_i+e_j\). Their energies bound from below the corresponding minimal energies in (1), giving
\[
Q_{ii}+Q_{jj}=E_s(u)+E_s(v)>E_s(w)+E_s(z)
\ge (e_i+e_j)^{\mathsf T}Q(e_i+e_j)
=Q_{ii}+Q_{jj}+2Q_{ij}.
\]
Thus \(Q_{ij}<0\) for every distinct pair, regardless of arc spacing or sample count.

**3. Local endpoint \(s=1\).** Parseval turns (1) into the minimum of \(\frac1{2\pi}\int_0^{2\pi}(|f'|^2+\kappa^2|f|^2)d\theta\). On each sampling arc of length \(\ell\), the minimizer solves \(-f''+\kappa^2f=0\) with prescribed endpoint values \(a,b\). Integrating by parts gives its exact energy
\[
\frac{\kappa}{2\pi\sinh(\kappa\ell)}\bigl[(a^2+b^2)\cosh(\kappa\ell)-2ab\bigr].\tag{5}
\]
Add (5) over the arcs. Comparing the coefficient of \(2v_iv_j\) with \(v^{\mathsf T}Qv\) gives the stated entry formula: adjacent pairs contribute strictly negative entries, while nonadjacent pairs give exactly zero.

**4. Sharp four-site obstruction for \(s>1\).** For the equispaced four sites, let
\[
S_r(\kappa)=\sum_{m\equiv r\ ({\rm mod}\ 4)}(\kappa^2+m^2)^{-s},\qquad r=0,1,2,3.
\]
Diagonalization of the circulant covariance by the four-point DFT gives eigenvalues \(4S_r\), with \(S_1=S_3\). Fourier inversion of their reciprocals gives
\[
Q_{1,3}=\frac1{16}\bigl[S_0^{-1}+S_2^{-1}-2S_1^{-1}\bigr].\tag{6}
\]
As \(\kappa\downarrow0\), \(S_0^{-1}\to0\), while for \(O_s=(1-2^{-2s})\zeta(2s)>0\),
\[
S_1\longrightarrow O_s,\qquad S_2\longrightarrow 2^{1-2s}O_s.
\]
Equation (6) yields the displayed positive limiting constant for every \(s>1\), because \(2^{2s-1}>2\). Continuity in positive \(\kappa\) then gives an actual finite-parameter violation. This supplies the converse for *every* \(s>1\), not only selected integer orders.

## Verification
Run `python3 verify_fractional_circle.py` with `mpmath>=1.3`. The included `verification_output.txt` is the program's actual output. It executes 125 standalone high-precision assertions: seven four-site limiting-sign/constant checks and exact irregular-grid local-precision comparisons for four sizes and two positive masses. In particular it checks signs below and above the threshold and the exact four-point positive obstruction. Computational evidence is finite and is not used to prove any universal quantifier; all such quantifiers are resolved by (1)–(6).

## Relationship to prior work
Huang and Li (first circulated January 30, 2022) defined the same Fourier-spectral circular Matérn model and proved the order-one equally spaced CAR identification, then analyzed an order-two CAR approximation. Their Sections 2–3 and appendices do not give the sign classification for every fractional exponent and **irregular** point sets, nor the sharp four-site converse. Antil and Saibaba (first circulated May 9, 2022) studied fractional Whittle–Matérn covariance powers and their numerical realization, rather than the inverse finite-sample sign boundary. Classical positivity-preserving-semigroup and Dirichlet-form theory underlies the strict lattice argument; the general Markovian mechanism itself is *not* claimed to be new. The distinguishing result is the two-sided sharp exponent classification together with the exact local endpoint and explicit universal four-site obstruction.

## Limitations
The statement concerns the one-dimensional *periodic Fourier-spectral* Matérn kernel, noiseless point samples, positive \(\kappa\), and the admissible continuous-point range \(s>1/2\). It does not assert any analogous result on higher-dimensional manifolds, under nonzero independent observation noise, or for Euclidean intrinsic/geodesic-distance kernels. The four-site positive entry is guaranteed for sufficiently small \(\kappa\), not for all \(\kappa\). Earlier broad trace-form or total-positivity literature may contain an equivalent characterization, so historical priority remains provisional pending an independent comprehensive review. No independent mathematical audit has been performed.

## References
1. C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856, first public January 30, 2022. https://arxiv.org/abs/2201.12856
2. H. Antil and A. K. Saibaba, *Efficient Algorithms for Bayesian Inverse Problems with Whittle–Matérn Priors*, arXiv:2205.04417, first public May 9, 2022. https://arxiv.org/abs/2205.04417
3. N. Jacob and R. L. Schilling, *Fractional Derivatives, Non-Symmetric and Time-Dependent Dirichlet Forms and the Drift Form*, Z. Anal. Anwend. 19 (2000), 801–830, DOI:10.4171/ZAA/981 (general subordination/form background). https://ems.press/journals/zaa/articles/11010
