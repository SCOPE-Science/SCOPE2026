# Isotropy-induced darkening and exact sitewise capture on prime quantum tori

## Finding

Fix an odd prime \(p\), a positive loss rate \(\gamma\), and positive hopping strengths \(J_x,J_y\). On the \(p\)-by-\(p\) periodic square lattice with a single absorber at the origin, the exact eventual absorption probability of a particle initially at \((x,y)\) depends on whether the two directional hopping strengths coincide. All site coordinates below are interpreted modulo \(p\).

For equal strengths, the probability is
\[
 C_{\mathrm{iso}}(x,y)=\frac18\left[(1+\mathbf1_{x=0})(1+\mathbf1_{y=0})+(\mathbf1_{x=y}+\mathbf1_{x=-y})^2\right].
\]
It equals \(1\) at the absorber, \(1/4\) on the four lines \(x=0\), \(y=0\), \(x=y\), \(x=-y\) away from the absorber, and \(1/8\) elsewhere. For every *positive rational* unequal ratio \(J_x/J_y\), the exact probability instead is
\[
 C_{\mathrm{aniso}}(x,y)=\frac14(1+\mathbf1_{x=0})(1+\mathbf1_{y=0}).
\]
Thus it equals \(1\) at the absorber, \(1/2\) on either coordinate axis away from the origin, and \(1/4\) elsewhere. The anisotropic conclusion also holds for all positive real ratios outside the explicitly described finite resonance set below.

The dimensions of the two corresponding absorbing (bright) subspaces are respectively
\[
 R_{\mathrm{iso}}=\frac{(p+1)(p+3)}8,\qquad R_{\mathrm{aniso}}=\frac{(p+1)^2}4.
\]
An initially maximally mixed state therefore has eventual capture probability \(R/p^2\). Every sufficiently small *nonzero rational* anisotropic perturbation of the isotropic coupling changes the exact infinite-time sitewise law, while each finite-time transition amplitude remains continuous in the couplings.

## Assumptions and scope

The Hilbert space is \(\mathbb C^{(\mathbb Z/p\mathbb Z)^2}\), with site vectors \(|x,y\rangle\). Define the undirected cycle adjacency \(A_p|x\rangle=|x+1\rangle+|x-1\rangle\). The Hermitian tight-binding Hamiltonian and absorbing generator are
\[
 H=J_x(A_p\otimes I_p)+J_y(I_p\otimes A_p),\qquad K=H-i\gamma|0,0\rangle\langle0,0|.
\]
We define \(C(x,y)=1-\lim_{t\to\infty}\|e^{-itK}|x,y\rangle\|^2\). The limit exists; the theorem does not depend on the particular \(\gamma>0\).

Put \(h=(p-1)/2\) and \(c_r=2\cos(2\pi r/p)\) for \(0\le r\le h\). The finite exceptional set of positive coupling ratios is
\[
 \mathcal R_p=\left\{-\frac{c_s-c_v}{c_r-c_u}>0:\ 0\le r,u,s,v\le h,\ r\ne u,\ s\ne v\right\}.
\]
Every ratio outside \(\mathcal R_p\) has the anisotropic capture law. Moreover \(\mathcal R_p\cap\mathbb Q_{>0}=\{1\}\). In particular, all unequal positive rational ratios are covered, with no restriction on numerator or denominator.

## Proof

**1. Absorption equals spectral visibility.** Let \(P_\lambda\) denote the orthogonal spectral projection of \(H\) at an eigenvalue \(\lambda\), and write \(|o\rangle=|0,0\rangle\). Define
\[
 |b_\lambda\rangle=\frac{P_\lambda|o\rangle}{\sqrt{\langle o|P_\lambda|o\rangle}},\qquad Q=\sum_\lambda|b_\lambda\rangle\langle b_\lambda|,
\]
where summation is over eigenvalues with nonzero denominator. The direct sum of vectors in each eigenspace perpendicular to \(P_\lambda|o\rangle\) is a dark subspace \(\mathcal D\). The orthogonal complement \(\mathcal B\), the range of \(Q\), is invariant under both \(H\) and \(K\); \(\mathcal D\) is invariant as well, with no loss on \(\mathcal D\). If \(Kv=zv\) for a nonzero \(v\in\mathcal B\), taking imaginary parts of \(\langle v|Kv\rangle=z\|v\|^2\) gives \(\operatorname{Im}z=-\gamma|\langle o|v\rangle|^2/\|v\|^2\le0\). Equality would imply \(Kv=Hv=zv\) and \(v\in\mathcal D\), contradicting \(v\in\mathcal B\). Thus all eigenvalues of \(K|_{\mathcal B}\) have strictly negative imaginary parts, so \(e^{-itK}|_{\mathcal B}\to0\), including Jordan blocks. The surviving component is exactly the \(\mathcal D\)-projection. For any unit vector \(|\psi\rangle\), therefore, \(C(\psi)=\langle\psi|Q|\psi\rangle\). More generally, for any density matrix \(\rho\), the capture probability is \(\operatorname{tr}(Q\rho)\).

**2. Prime cyclotomic independence.** Set \(\zeta=e^{2\pi i/p}\). The Bloch characters \(p^{-1}\zeta^{kx+\ell y}\) diagonalize \(H\) and have energies \(J_x(\zeta^k+\zeta^{-k})+J_y(\zeta^\ell+\zeta^{-\ell})\). The involution \(k\mapsto-k\) gives labels \(0\le r\le h\), with multiplicities \(d_0=1\), \(d_r=2\) for positive \(r\).

Here is the needed cyclotomic lemma, including its exceptional relation. If rational coefficients \(a_r\) satisfy
\[
 \sum_{r=0}^{h}a_r(\zeta^r+\zeta^{-r})=0,
\]
then \((a_0,a_1,\ldots,a_h)\) is a rational multiple of \((1,2,\ldots,2)\). To prove it, rewrite the sum as a polynomial in \(\zeta\) of degree at most \(p-1\): its coefficient at exponent zero is \(2a_0\), and at exponents \(r\), \(p-r\) it is \(a_r\). The minimal polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) therefore forces \(2a_0=a_1=\cdots=a_h\). If, additionally, \(\sum_r a_r=0\), then the common multiplier is zero because \(1+2h=p\ne0\).

Let \(\alpha=J_x/J_y\). For \(\alpha=A/B\in\mathbb Q_{>0}\) in lowest terms, energy equality between labels \((r,s)\) and \((u,v)\) yields
\[
 A(c_r-c_u)+B(c_s-c_v)=0.
\]
The coefficient vector has sum zero, so the lemma makes it identically zero. Thus \(A(e_r-e_u)+B(e_s-e_v)=0\) as a formal coefficient-vector equality. If \(A\ne B\), positivity and comparison of nonzero entries imply \(r=u\) and \(s=v\). If \(A=B\), the only additional possibility is the exchanged pair \((u,v)=(s,r)\). Here \(e_r\) means the standard coordinate unit vector for label \(r\). For arbitrary positive real ratios outside \(\mathcal R_p\), the defining ratio criterion directly excludes every equality of two different ordered labels. In the rational case it also shows \(\mathcal R_p\cap\mathbb Q_{>0}=\{1\}\): any collision between distinct ordered labels occurs only by exchanging them at ratio one.

**3. Exact mode projections.** Let \(S_0=\{0\}\) and \(S_r=\{r,p-r\}\) for \(r>0\). Set
\[
 a_r(t)=\sum_{k\in S_r}\zeta^{kt},\qquad z_r(t)=\frac{a_r(t)}{\sqrt{d_r}},\qquad \mathcal K(a,b)=\sum_{r=0}^h z_r(a)z_r(b).
\]
All \(a_r(t)\) are real because each positive-frequency term is paired with its conjugate. Discrete character orthogonality gives
\[
 \mathcal K(a,b)=\frac12\sum_{k\bmod p}(\zeta^{k(a-b)}+\zeta^{k(a+b)})=\frac p2(\mathbf1_{a=b}+\mathbf1_{a=-b}).
\]
In an eigenspace spanned by \(m\) Bloch modes \((k,\ell)\), the spectral weight at the detector is \(m/p^2\) and the matrix coefficient \(\langle x,y|P_\lambda|o\rangle\) is \(p^{-2}\sum\zeta^{kx+\ell y}\). Hence that eigenspace contributes
\[
 \frac{1}{p^2m}\left|\sum_{(k,\ell)\text{ in the block}}\zeta^{kx+\ell y}\right|^2
\]
to \(C(x,y)\).

At a nonresonant ratio each spectral block is a single ordered label \((r,s)\), with \(m=d_rd_s\). Consequently
\[
 C_{\mathrm{aniso}}(x,y)=\frac1{p^2}\sum_{r,s}\frac{a_r(x)^2a_s(y)^2}{d_rd_s}=\frac{\mathcal K(x,x)\mathcal K(y,y)}{p^2}.
\]
At the isotropic ratio \(1\), diagonal blocks \(r=s\) retain multiplicity \(d_r^2\), while off-diagonal blocks \(r<s\) merge two ordered labels, acquiring multiplicity \(2d_rd_s\). The block sums are respectively \(a_r(x)a_r(y)\) and \(a_r(x)a_s(y)+a_s(x)a_r(y)\). Using the identity
\[
 \frac12\sum_{r<s}\big(z_r(x)z_s(y)+z_s(x)z_r(y)\big)^2+\sum_r z_r(x)^2z_r(y)^2=\frac12\big[\mathcal K(x,x)\mathcal K(y,y)+\mathcal K(x,y)^2\big],
\]
we obtain
\[
 C_{\mathrm{iso}}(x,y)=\frac{\mathcal K(x,x)\mathcal K(y,y)+\mathcal K(x,y)^2}{2p^2}.
\]
Substituting the displayed explicit formula for \(\mathcal K\) proves both sitewise capture laws. Because every Bloch mode has nonzero detector amplitude and there is one bright direction per distinct energy, the bright ranks are the numbers of ordered and unordered pairs of \(h+1\) labels: \((h+1)^2=(p+1)^2/4\) and \((h+1)(h+2)/2=(p+1)(p+3)/8\). The maximally mixed case follows by taking \(\operatorname{tr}(Q)/p^2\).

## Verification

The self-contained numerical reproduction script is `verification/verify_prime_torus.py`; install dependencies listed in `verification/requirements.txt`, then run `python verification/verify_prime_torus.py` from the package root. The actual packaged program was run and reported: `VERIFY_OK prime_sizes=5 rational_coupling_pairs=4 exact_spectrum_groups=20 Fourier_site_checks=1492 direct_loss_models=4`. It checks odd primes \(p=3,5,7,11,13\), rational strength pairs \((1,1),(2,1),(3,2),(4,7)\), the Fourier projector formula against the closed sitewise answer, and direct lossy matrix propagation for the smaller prime lattices. For Fourier spectral grouping, the script uses integer coefficient vectors modulo \(\Phi_p\), avoiding floating-eigenvalue grouping errors; exponential propagation uses floating-point arithmetic. These tests are finite corroboration and not proofs of the general formulas or all-time limit, which follow analytically above.

## Relationship to prior work

Agliari, Mülken and Blumen (2009) study continuous-time quantum walks and trapping with non-Hermitian losses, including ring systems, but do not give this prime two-dimensional sitewise formula. Mülken and Blumen (2011) derive the coherent two-dimensional torus dispersion and separately describe absorbing-trap dynamics; their treatment does not evaluate the anisotropy-dependent capture projector. Anishchenko, Blumen and Mülken (2013) analyze nonperiodic two-dimensional lattices with randomly selected nearest-neighbor bonds and absorbers on an entire terminal boundary, not an odd-prime periodic torus with one point absorber. Godsil (2011) provides the average-mixing projector formula; time-averaged coherent transition probabilities are distinct from loss capture because capture contributions are divided by the detector's spectral weight. Marquezino, Portugal and Abal (2010) study coined discrete-time walks on periodic grids, not the present continuous-time single-sink Hamiltonian. Thus the toroidal Fourier machinery and the trapping principle are antecedents, whereas the evaluated two-dimensional prime-order sitewise dichotomy and finite-resonance description are the specific claim assessed here.

## Limitations

The results require an odd prime side length, nearest-neighbor periodic hopping, one absorbing site, and perfectly homogeneous hopping within each direction. They establish eventual absorption, not uniform absorption times or numerical stability near resonance. Additional exceptional *irrational* ratios belonging to \(\mathcal R_p\) are excluded from the anisotropic closed form; their sitewise profiles are not classified here. Mathematical correctness does not by itself establish publication novelty: specialized absorbing-torus studies not found in the literature checks could provide equivalent or stronger coverage. Finite computation is not a substitute for the cyclotomic and spectral arguments.

## References

- E. Agliari, O. Mülken, A. Blumen, "Continuous-Time Quantum Walks and Trapping" (2009), arXiv:0903.3288, https://arxiv.org/abs/0903.3288 .
- O. Mülken, A. Blumen, "Continuous-Time Quantum Walks: Models for Coherent Transport on Complex Networks" (2011), arXiv:1101.2572, https://arxiv.org/abs/1101.2572 .
- A. Anishchenko, A. Blumen, O. Mülken, "Geometrical aspects of quantum walks on random two-dimensional structures" (2013), arXiv:1309.2827, https://arxiv.org/abs/1309.2827 .
- C. Godsil, "Average Mixing of Continuous Quantum Walks" (2011), arXiv:1103.2578, https://arxiv.org/abs/1103.2578 .
- R. Marquezino, R. Portugal, G. Abal, "Mixing Times in Quantum Walks on Two-Dimensional Grids" (2010), arXiv:1006.4625, https://arxiv.org/abs/1006.4625 .
