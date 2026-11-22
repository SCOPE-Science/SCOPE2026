# Sharp Schatten boundary eigenarcs for beta-weighted Bergman harmonic-Toeplitz dynamics

## Finding

For every beta-weighted analytic Bergman disk space with \(\beta>-1\) and every Schatten exponent \(1\le p<\infty\), the diagonal Schatten operators form an invariant space for Panja's unital completely positive harmonic-Toeplitz map. Its restriction \(B_{\beta,p}\) has an exactly determined point spectrum, including a sharp phase transition on the spectral boundary. Set
\[
a=\frac1{\beta+2},\quad c=\frac{\beta+1}{\beta+2},\quad \kappa=\beta+1,\quad \mu=\frac{\lambda-c}{a}.
\]
Then
\[
\boxed{\sigma_p(B_{\beta,p})=\{\lambda:|\mu|<1\}\ \cup\ \{\lambda:|\mu|=1,\ p\kappa(1-\operatorname{Re}\mu)>1\}\ \cup\ \{c-a\kappa/(j+1):j\in\mathbb N_0,\ j<\beta\}.}
\]
Here the subscript \(p\) on \(\sigma_p\) denotes point spectrum, whereas \(p\) in \(B_{\beta,p}\) is the Schatten exponent. The full spectrum and Fredholm essential spectrum are
\[
\sigma(B_{\beta,p})=\{\lambda:|\lambda-c|\le a\}\cup\{c-a\kappa/(j+1):0\le j<\beta\},
\quad\sigma_{\mathrm{ess}}^{\mathrm{Fred}}(B_{\beta,p})=\{\lambda:|\lambda-c|=a\}.
\]
At any boundary value satisfying \(p\kappa(1-\operatorname{Re}\mu)=1\), the uniquely determined formal eigenvector belongs to weak \(\ell^p\) but not to the diagonal Schatten class \(\ell^p\); its entries have exact order \(n^{-1/p}\). Thus a nonempty boundary eigenarc occurs **if and only if** \(p(\beta+1)>1/2\); it is entirely absent at the threshold. When the arc exists, its two endpoints are excluded, and the fixed-point value \(\lambda=1\) is always excluded. Every eigenvalue has one-dimensional geometric eigenspace; the isolated eigenvalues exterior to the disk are algebraically simple. The Fredholm index is \(+1\) inside the disk and zero outside.

## Assumptions and scope

Use normalized area measure on \(\mathbb D\) and the normalized beta radial density \(w_\beta(z)=(\beta+1)(1-|z|^2)^\beta\), \(\beta>-1\). Its moments are \(\omega_j=\Gamma(\beta+2)\Gamma(j+1)/\Gamma(j+\beta+2)\). In the orthonormal monomial basis \(e_j=z^j/\sqrt{\omega_j}\), Panja's map is
\[
\Psi_\beta(X)=\omega_1\left[S'^*XS'+\sum_{j\ge1}(\delta_{j-1}-\delta_j)Q_jXQ_j\right],\quad\delta_j=\frac{\omega_j}{\omega_{j+1}},
\]
where \(S'=M_z(M_z^*M_z)^{-1}\) and \(Q_j\) projects onto the monomial tail beginning at degree \(j\). For each real \(1\le p<\infty\), let \(\mathcal D_p=\{\operatorname{diag}(x_j):(x_j)\in\ell^p(\mathbb N_0)\}\subset\mathcal S_p\), with Schatten norm \(\|\operatorname{diag}(x)\|_{\mathcal S_p}=\|x\|_p\). This diagonal space, not necessarily the whole Schatten ideal, is the domain for the claimed spectral classification. The Fredholm essential spectrum means the failure-of-Fredholmness set, not the index-zero Weyl essential spectrum.

## Proof

**Restriction and boundedness.** Since \(\omega_1=1/(\beta+2)\) and \(\delta_j=(j+\beta+2)/(j+1)\), calculating the diagonal entries of the Kraus formula yields
\[
(B_{\beta,p}x)_j=b_jx_j+r_jx_{j+1},\qquad
r_j=\frac{j+\beta+2}{(\beta+2)(j+1)}=a\left(1+\frac\kappa{j+1}\right),\quad
b_j=1-r_j= c-\frac{a\kappa}{j+1}.
\]
The sequences \((r_j),(b_j)\) are bounded, so this operator preserves \(\ell^p\) and is bounded for every finite \(p\) (the diagonal multiplier and backward shift are bounded). Since \(r_j-a\to0\), it is a compact perturbation of \(cI+aL\), where \((Lx)_j=x_{j+1}\) on \(\ell^p\). For \(|\mu|<1\), \(L-\mu I\) is surjective with one-dimensional kernel using its forward-shift right inverse and a Neumann series; for \(|\mu|>1\) it is invertible by a Neumann series. On \(|\mu|=1\), long smooth finite-support approximate eigenvectors show failure of Fredholmness. Thus compact-perturbation invariance gives the asserted Fredholm circle and its indices.

**Exact eigenvector product.** For \(\lambda=c+a\mu\), the eigenvector recurrence is
\[
 x_{j+1}=\frac{\mu(j+1)+\kappa}{j+1+\kappa}\,x_j,\qquad
 x_n=x_0\prod_{j=1}^{n}\frac{\mu j+\kappa}{j+\kappa}.
\]
The solution is one-dimensional whenever it exists, since every superdiagonal coefficient is nonzero. For \(\mu\ne0\) and no terminating numerator factor, the gamma-product identity gives
\[
 x_n=x_0\mu^n\frac{\Gamma(\kappa+1)}{\Gamma(1+\kappa/\mu)}
 \frac{\Gamma(n+1+\kappa/\mu)}{\Gamma(n+1+\kappa)}.
\]
For \(|\mu|<1\), the factors have asymptotic modulus less than one, so the sequence is exponentially summable in every \(\ell^p\), including \(\mu=0\). For \(|\mu|>1\), a nonzero \(\ell^p\) solution must terminate. The terminating parameters are \(\mu=-\kappa/j\) for integers \(j\ge1\), corresponding to \(\lambda=b_{j-1}=c-a\kappa/j\). Such an eigenvalue lies exterior to the disk precisely when \(j<\kappa\), equivalently \(j-1<\beta\).

**Sharp unit-circle summability.** For \(|\mu|=1\), no terminating factor, the gamma ratio asymptotic implies a positive constant \(C(\mu,\kappa,x_0)\) with
\[
 |x_n|\sim C\,n^{-\kappa(1-\operatorname{Re}\mu)}.
\]
Thus \(x\in\ell^p\) if and only if \(p\kappa(1-\operatorname{Re}\mu)>1\). At equality the sequence is asymptotic in modulus to \(Cn^{-1/p}\), hence belongs to weak \(\ell^p\) and not \(\ell^p\). The only possible terminating unit-circle parameter is \(\mu=-1\), requiring \(\kappa\in\mathbb N\); this always lies in the stated strict arc, since \(p\kappa(1-(-1))=2p\kappa>1\). The smallest possible real part of a unit complex number is \(-1\), so the strict arc exists exactly when \(2p\kappa>1\). At \(\mu=1\), the exact recurrence gives \(x_{j+1}=x_j\), excluding any nonzero \(\ell^p\) eigenvector.

**Exterior and full spectrum.** Every exterior \(\lambda\) is Fredholm with index zero. If it is not one of the terminating values, the recurrence makes its kernel zero; Fredholmness forces invertibility. The exterior terminating eigenvalues are therefore the only spectral outliers, and the whole closed disk is spectral because its boundary is Fredholm-essential and its interior consists of eigenvalues. Each exterior eigenvalue has a one-dimensional eigenspace. To exclude generalized eigenvectors, the homogeneous recurrence above the terminal index has ratio tending to \(\mu\), with \(|\mu|>1\); a generalized eigenvector in \(\ell^p\) must have zero tail, contradicting its inhomogeneous equation at the last nonzero coordinate of the eigenvector. Thus exterior eigenvalues are algebraically simple. There are exactly \(\max\{0,\lceil\beta\rceil\}\) of them.

## Verification

The standalone `CHECK.py` verifies rational beta coefficients, exact finite-support eigenvector recurrences and outlier inequalities, plus exact finite approximations to the boundary power exponents for several \(p\). These finite diagnostics do not prove asymptotic gamma ratios, spectral Fredholm assertions or the full parameter classification. The proof explicitly handles beta near \(-1\), the birth threshold \(2p(\beta+1)=1\), integer-beta terminating products, \(\mu=0\), \(\mu=-1\), and \(\mu=1\).

## Relationship to prior work

Panja (2026) constructs the unital completely positive map and identifies its bounded-operator fixed points, but does not classify its diagonal Schatten point spectra. A prior analysis of the diagonal bounded-sequence algebra identifies a full spectral disk and a finite moment-doubling outlier set; that established disk/outlier identification is **not claimed as new**. Another published finding gives a boundary eigenarc on the Hilbert–Schmidt ideal for the **ordinary** Bergman weight, corresponding to the single parameter pair \(p=2\), \(\beta=0\); that case is likewise **not claimed as new**. The additional claim here is the **complete two-parameter Schatten-diagonal boundary arc**, including the sharp onset at \(2p(\beta+1)=1\) and the exact weak-Schatten critical boundary. These conclusions do not follow as stated from a single bounded-diagonal or Hilbert–Schmidt special case. Weighted-shift recurrences and gamma asymptotics are classical tools, not new theorems.

## Limitations

Only the invariant diagonal \(\mathcal S_p\) subspace is classified; no spectrum of the entire noncommutative Schatten ideal is claimed. Full spectral disks and beta outlier counts overlap existing bounded-diagonal analysis and are included only to contextualize the new boundary result. The weak-\(\ell^p\) endpoint is a statement about the formal recurrence vector, not membership in \(\mathcal S_p\). A general result on gamma-weighted backward shifts might subsume part of the two-parameter computation, so broader bibliographic priority remains a risk. No independent mathematical audit has been performed.

## References

1. S. Panja, *Toeplitz operators with bounded harmonic symbols on weighted Bergman spaces are the fixed points of a normal unital completely positive map*, arXiv:2611.09731v1 (first public 2026-11-06). https://arxiv.org/html/2611.09731v1
2. *A boundary eigenarc for the Hilbert–Schmidt spectrum of a Bergman completely positive map*, public 2026 mathematical finding (special case of the present boundary argument for ordinary Bergman space).
3. S. R. El-Shabrawy, *Spectra and fine spectra of certain lower triangular double-band matrices as operators on c0*, Journal of Inequalities and Applications (2014), article 241. https://doi.org/10.1186/1029-242X-2014-241
4. N. Durna and R. Kılıç, *On the spectrum of the upper triangular double band matrix U(a0,a1,a2;b0,b1,b2) over the sequence c*, Commun. Fac. Sci. Univ. Ank. 71 (2022), 554–565. https://doi.org/10.31801/cfsuasmas.977593
