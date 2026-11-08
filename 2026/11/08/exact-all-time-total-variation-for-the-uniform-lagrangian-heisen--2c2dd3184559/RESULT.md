# Exact all-time total variation for the uniform-Lagrangian Heisenberg walk

## Finding
Let \(q\) be any odd prime power, \(m\ge1\), and \(Q=q^m\). In the finite Heisenberg group \(H\) associated with a nondegenerate alternating form on \(\mathbb F_q^{2m}\), choose a Lagrangian subspace uniformly, then sample one of its vectors uniformly as a zero-central-coordinate group increment. Let \(\mu\) denote this increment distribution and \(U\) uniform measure on \(H\). For **every** integer \(t\ge1\),
\[
\boxed{\|\mu^{*t}-U\|_{\mathrm{TV}}=\frac{q-1}{q}\left(\frac{2}{Q+1}\right)^{t-1}.}
\]
In particular, the one-step distance is \((q-1)/q\), while the two-step distance is exactly \(2(q-1)/(q(Q+1))\). Thus for any sequence of odd prime powers and positive dimensions with \(Q\to\infty\), the one-step distance remains at least \(2/3\), whereas the two-step distance tends to zero. The full probability mass function at every positive time and the complete regular-representation convolution spectrum are also explicit below.

## Assumptions and scope
Fix \(q\) odd, \(m\ge1\), and \(V=\mathbb F_q^m\oplus\mathbb F_q^m\). Write \(v=(x,y)\), \(w=(x',y')\), and \(\omega(v,w)=x\cdot y'-y\cdot x'\). The Heisenberg group is \(H=V\times\mathbb F_q\) with
\[
(v,z)(w,s)=(v+w,z+s+\tfrac12\omega(v,w)),\qquad |H|=qQ^2.
\]
The inverse of \((v,z)\) is \((-v,-z)\). A Lagrangian is a dimension-\(m\) totally isotropic \(\mathbb F_q\)-linear subspace \(L\le V\); \(H_L=\{(v,0):v\in L\}\) is a subgroup. At each independent step, choose \(L\) uniformly among all Lagrangians and then choose \(v\) uniformly in \(L\), producing \((v,0)\). There is no additional central increment. All total-variation distances are \(\tfrac12\) of the unnormalized \(\ell^1\) distance between probabilities. The result is for odd characteristic; characteristic two is not covered by this group-law normalization.

For \(t\ge1\), set \(a_t=(Q+1)^{-t}\) and \(b_t=(2/(Q+1))^t\). For every \((v,z)\in H\), the complete distribution is
\[
\boxed{\mu^{*t}(v,z)=\frac1{qQ^2}\left[1+a_t\bigl(Q^2\mathbf1_{v=0}-1\bigr)
+\frac{Qb_t}{2}\bigl(Q\mathbf1_{v=0}+1\bigr)\bigl(q\mathbf1_{z=0}-1\bigr)\right].}
\]
The full right-convolution spectrum, with algebraic multiplicities in \(\mathbb C[H]\), is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1&1\\
(Q+1)^{-1}&Q^2-1\\
2(Q+1)^{-1}&(q-1)Q(Q+1)/2\\
0&(q-1)Q(Q-1)/2
\end{array}
\]
and for all \(t\ge1\) the exact chi-square divergence is
\[
\chi^2(\mu^{*t}\Vert U)
=\frac{Q^2-1}{(Q+1)^{2t}}
+\frac{(q-1)Q(Q+1)}2\left(\frac{2}{Q+1}\right)^{2t}.
\]
The expression at \(t=0\) is instead \(qQ^2-1\), as the zero eigenspace contributes at time zero.

## Proof
**1. The uniform-Lagrangian measure.** The symplectic group acts transitively on nonzero vectors and permutes Lagrangians. Double counting pairs \((L,v)\) with \(v\in L\setminus\{0\}\) gives \(\Pr_L(v\in L)=(Q-1)/(Q^2-1)=1/(Q+1)\) for each nonzero \(v\). Thus
\[
\mu(0,0)=Q^{-1},\quad
\mu(v,0)=[Q(Q+1)]^{-1}\ (v\ne0),\quad
\mu(v,z)=0\ (z\ne0).
\]
If \(\nu\) is uniform measure on the zero-central-coordinate slice \(\{(v,0):v\in V\}\), this is precisely \(\mu=(Q+1)^{-1}\delta_e+Q(Q+1)^{-1}\nu\). The slice need not be a subgroup.

**2. Nonabelian Fourier blocks.** The irreducible complex representations of \(H\) comprise \(Q^2\) one-dimensional characters factoring through \(V\), plus one \(Q\)-dimensional Schrödinger representation \(\pi_\psi\) for each of the \(q-1\) nontrivial additive characters \(\psi\) of \(\mathbb F_q\). This exhausts all irreducibles since \(Q^2+(q-1)Q^2=|H|\). For a nontrivial one-dimensional character, the slice-uniform part has zero Fourier transform, hence \(\widehat\mu=(Q+1)^{-1}\); the trivial character gives \(1\).

For each nontrivial central character, realize \(\pi_\psi\) on \(\mathbb C^{\mathbb F_q^m}\) by
\[
[\pi_\psi(x,y,z)f](r)=\psi\!\left(z+y\cdot(r+x/2)\right)f(r+x).
\]
Orthogonality of additive characters yields \(\sum_{v\in V}\pi_\psi(v,0)=Q R\), where \([Rf](r)=f(-r)\) is parity. Since \(Q\) is odd, \(R\) has eigenspace dimensions \((Q+1)/2\) and \((Q-1)/2\), for eigenvalues \(+1\) and \(-1\). Hence
\[
\widehat\mu(\pi_\psi)=(I+R)/(Q+1)
=\frac2{Q+1}P_+,
\qquad P_+=(I+R)/2.
\]
Each Fourier eigenvalue in a \(Q\)-dimensional irreducible block occurs \(Q\) times in the regular representation. This proves all claimed spectral multiplicities. Standard finite-group Plancherel gives the chi-square identity, with the indicated \(t\ge1\) condition.

**3. Exact point probabilities.** Fourier inversion on the one-dimensional characters gives \(a_t(Q^2\mathbf1_{v=0}-1)/(qQ^2)\) beyond uniform probability. For a nontrivial central character, \(\operatorname{tr}\pi_\psi(v,z)^{-1}=Q\psi(-z)\mathbf1_{v=0}\) and \(\operatorname{tr}(R\pi_\psi(v,z)^{-1})=\psi(-z)\); the second trace is obtained by evaluating the unique fixed coordinate \(r\) satisfying \(2r+x=0\). Therefore \(\operatorname{tr}(P_+\pi_\psi(v,z)^{-1})=(Q\mathbf1_{v=0}+1)\psi(-z)/2\). Summing over the \(q-1\) nontrivial \(\psi\) yields \(q\mathbf1_{z=0}-1\). Substitution into finite-group Fourier inversion gives exactly the displayed point-mass formula for every \(t\ge1\).

**4. The exact total variation.** Subtract \(1/(qQ^2)\) from that point-mass formula. Its sign is strictly positive when \(z=0\), and strictly negative when \(z\ne0\), for all \(t\ge1\): indeed, at \(v\ne0,z=0\) the scaled numerator is \(a_t[-1+Q2^{t-1}(q-1)]>0\); at \(v=0,z\ne0\) it is \(a_t(Q+1)[(Q-1)-Q2^{t-1}]<0\); the other two signs are immediate. Thus total variation is exactly the total deficiency over the \(z\ne0\) states. For each nonzero \(z\), summing the \(a_t\)-contribution over all \(v\) gives zero, while summing \((Q\mathbf1_{v=0}+1)\) gives \(Q(Q+1)\). Hence
\[
\|\mu^{*t}-U\|_{\mathrm{TV}}
=\frac{q-1}{qQ^2}\cdot\frac{Qb_t}{2}\cdot Q(Q+1)
=\frac{q-1}{q}\left(\frac{2}{Q+1}\right)^{t-1}.
\]
This also proves sharp convergence for every odd prime power and all dimensions, not merely an asymptotic estimate.

## Verification
A standalone standard-library checker, `CHECK.py`, enumerates independent group-convolution probabilities through four steps for \((q,m)=(3,1),(5,1),(7,1),(3,2),(9,1)\). The \(q=9\) test uses explicit arithmetic in \(\mathbb F_3[\theta]/(\theta^2+1)\). It compares *every point mass* with the closed formula using exact fractions, checks total variation and chi-square identities, and additionally compares prime-field Schrödinger Fourier matrices with \((I+R)/(Q+1)\) to numerical tolerance \(10^{-11}\). A successful run prints `LAGRANGIAN_HEISENBERG_EXACT_CHECKS_PASS`. Finite checks are corroborative; the proof above handles all odd prime powers and all positive dimensions.

## Relationship to prior work
The classical finite Heisenberg representation theory and finite-group Fourier inversion are essential. Gross's 2006 discrete Wigner analysis explicitly identifies the parity phase-point operator, which covers a central ingredient in the Fourier-block computation, not a new discovery here. Bump–Diaconis–Hicks–Miclo–Widom (first public 2015) analyze sparse coordinate-generator walks requiring quadratic-in-modulus mixing; Diaconis–Hough (first public 2015) study local central limit behavior of unipotent-group walks. The present walk samples a **uniform random Lagrangian** and hence a dense zero-central slice; its all-time pointwise law and exact geometric total-variation identity concern a different transition measure. Its exact two-step mixing is not an implication of the sparse-generator mixing result alone. Miclo’s later work on strong stationary times for finite Heisenberg walks likewise uses a four-coordinate-generator measure, not this dense sampling. The classic parity identity plus the uniform-Lagrangian counting identity makes the Fourier computation short, so historical-priority risk concerns possible earlier explicit uses of these ingredients for this exact measure.

## Limitations
Odd characteristic is necessary for the displayed half-symplectic-coordinate model and the parity eigenspace formula as written. Nothing is asserted about characteristic two, nonuniform Lagrangian sampling, fixed rather than random coordinate Lagrangians, or other distances. The formula is an exact theorem within the stated model; any priority claim is bounded by the literature inspected, and no independent mathematical audit has been performed.

## References
- D. Gross, *Hudson's Theorem for finite-dimensional quantum systems*, arXiv:quant-ph/0602001, initially public 2006-02-01. Relevant material: Weyl operators and the parity phase-point identity, Theorem 6(5).
- D. Bump, P. Diaconis, A. Hicks, L. Miclo, H. Widom, *An Exercise (?) in Fourier Analysis on the Heisenberg Group*, arXiv:1502.04160, initially public 2015-02-14. Relevant material: sparse generating measure, Theorem 1, and Section 3.
- P. Diaconis, R. Hough, *Random walk on unipotent matrix groups*, arXiv:1512.06304, initially public 2015-12-20. Relevant material: its introduction and local limit framework for different walks.
- L. Miclo, *Strong stationary times for finite Heisenberg walks*, author-hosted preprint available at https://perso.math.univ-toulouse.fr/miclo/files/2020/11/Heisenberg.pdf; relevant material: the sparse lazy step law in Section 1 and Theorems 1–4.
