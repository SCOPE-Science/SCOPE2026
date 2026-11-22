# Reentrant distant-leaf correlations on hard-core helm graphs

## Finding
For each even integer \(n\ge6\), the hard-core occupation covariance of two pendant vertices at rim separation three on the \(n\)-helm changes sign at least twice as common activity \(z\) increases: it is positive near zero, negative at \(z=1\), and positive at sufficiently high activity. There is a sequence of high-activity sign crossings at
\[
z_n\sim \frac{3\sqrt5-5}{10}\left(\frac{1+\sqrt5}{2}\right)^n
\]
as even \(n\to\infty\). No uniqueness of crossings is asserted.

## Assumptions and scope
For an even integer \(n\ge6\), the helm graph \(H_n\) has rim vertices \(r_0,\ldots,r_{n-1}\), edges \(r_ir_{i+1}\) (indices modulo \(n\)), a hub joined to each rim vertex, and leaves \(\ell_i\) adjacent only to \(r_i\). Each independent set \(I\) has Gibbs weight \(z^{|I|}\), for real \(z>0\). The variables \(L_i\) indicate leaf occupation. The claim concerns \(K_n(z)=\mathbb E_z(L_0L_3)-\mathbb E_z(L_0)\mathbb E_z(L_3)\). These are distinct graph vertices, at the first rim separation for which a nonadjacent odd-distance anticorrelation can compete with hub fluctuations.

For \(k\ge0\), define the path independence polynomial
\[
P_k(t)=\sum_{j=0}^{\lfloor(k+1)/2\rfloor}\binom{k-j+1}{j}t^j.
\]
Define the cycle independence polynomial
\[
A_n(t)=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n}{n-j}\binom{n-j}{j}t^j,
\]
where the \(j=0\) term is one. Set \(t=z/(1+z)\), \(W_1=tP_{n-3}(t)\) and \(W_2=t^2P_{n-6}(t)\).

## Proof
Condition on the occupation of the hub and of the rim. Summing all compatible leaf occupations gives \((1+z)^n\) times \(A_n(t)\) when the hub is empty, and \(z(1+z)^n\) when it is occupied. Thus \(Z_{H_n}(z)=(1+z)^n[A_n(t)+z]\). The conditional occupation probability of a leaf whose rim site is vacant is \(p=z/(1+z)\). If a rim site is occupied the corresponding leaf is forced empty. Hence the two leaf indicators are conditionally independent given hub/rim, and
\[
\boxed{K_n(z)=p^2\frac{[A_n(t)+z]W_2-W_1^2}{[A_n(t)+z]^2}.}\tag{1}
\]
Here \(W_1\) is the rim weight forcing one specified rim vertex occupied, obtained by deleting that vertex and its two neighbors; \(W_2\) forces rim vertices separated by three occupied, leaving a path of length \(n-6\). All formulae also apply at \(n=6\) with \(P_0=1\).

At small activity, \(A_n(t)=1+nt+O(t^2)\), \(W_1=t[1+(n-3)t+O(t^2)]\), \(W_2=t^2[1+(n-6)t+O(t^2)]\), and \(z=t+O(t^2)\). Therefore the numerator in (1) is \(t^3+O(t^4)>0\) at sufficiently small positive activity. At large activity \(t\to1\), and the same numerator is \(zP_{n-6}(1)+O(1)>0\), because \(P_{n-6}(1)>0\).

It remains to show strict negativity at \(z=1\). For \(n=6,8\), direct substitution into the exact polynomial expressions gives, respectively,
\[
[A_n(t)+z]W_2-W_1^2\big|_{z=1}= -\frac1{64},\qquad-\frac1{256}.
\]
For even \(n\ge10\) put \(\alpha=(1+\sqrt{1+4t})/2\), \(\beta=(1-\sqrt{1+4t})/2\), and \(u=-\beta/\alpha\in(0,1)\). The two-eigenvalue transfer formula gives \(A_n(t)=\alpha^n(1+u^n)\). Let \(\rho=W_1/A_n\), \(B=W_2/A_n\), and \(q=z/(A_n+z)\). Exact path transfer identities yield
\[
\rho=\frac{u+u^n}{(1+u)(1+u^n)},\quad
\frac B{\rho^2}=\frac{(1-u^2)(1+u^n)(1-u^{n-4})}{(1+u^{n-1})^2}=:C_n(u).
\tag{2}
\]
Since \(0<u<1\), we have \(C_n(u)<1-u^2\). By (1), the sign of \(K_n\) equals the sign of \(C_n(u)-(1-q)\). At \(z=1\), \(t=1/2\), \(u=2-\sqrt3>1/4\) and \(\alpha=(1+\sqrt3)/2>4/3\). For every even \(n\ge10\),
\[
q=\frac1{1+\alpha^n(1+u^n)}<\frac1{1+(4/3)^{10}}<\frac1{16}<u^2<1-C_n(u).
\]
Thus \(K_n(1)<0\) for every even \(n\ge6\). Continuity and the two positive endpoint signs give distinct positive roots below and above one.

For the exponential-scale statement, let \(\varphi=(1+\sqrt5)/2\), \(u_*=(3-\sqrt5)/2\), and fix any constant \(c>0\). Along even \(n\to\infty\), put \(z=c\varphi^n\). Then \(t\to1\), \(\alpha(t)^n/\varphi^n\to1\), \(u\to u_*\), and \(u^n\to0\). Thus \(A_n(t)/\varphi^n\to1\), \(q\to c/(c+1)\), \(C_n(u)\to1-u_*^2\). Hence the eventual sign is the sign of \(c/(c+1)-u_*^2\), which changes at \(c_*=u_*^2/(1-u_*^2)=(3\sqrt5-5)/10\). Applying the intermediate-value theorem between \((c_*\pm\varepsilon)\varphi^n\) for every sufficiently small \(\varepsilon>0\), then choosing one crossing for each even \(n\), proves existence of \(z_n/\varphi^n\to c_*\). This does not establish uniqueness of that crossing.

## Verification
The standalone script `verify.py` independently enumerates all independent rim configurations and integrates pendant occupations, without using transfer eigenvalues; it compares the resulting exact rational covariance against (1). It also verifies the transfer ratio (2) numerically and the proved sign examples. Run `python3 verify.py`. The packaged run reported `NEW_HELM_CHECKS_PASSED 76`. The finite comparisons supplement, but do not replace, the all-size inequalities above.

## Relationship to prior work
Scott and Sokal (first preprint 2003-09-15) establish the general hard-core lattice-gas and independent-set framework, not a helm-graph distance-three reentrant covariance. The known helm independence polynomial listed by Weisstein encodes the unmarked partition function and is acknowledged, not claimed here. The new observable requires two marked leaf occupations; the known univariate formula alone does not state their sign-reentrant law or the exponential scale of a return crossing. General finite-state transfer techniques are also established prior methods.

## Limitations
The proof only covers even rim lengths at least six, a specific pair of pendant sites, uniform positive fugacity, and exact finite-volume equilibrium. It establishes at least two positive crossing activities but neither exactly two nor uniqueness of the exponentially scaled crossing. It makes no thermodynamic phase-transition or independent historical-priority claim. Literature priority beyond the examined sources remains uncertain; the result has not received independent scientific validation.

## References
- A. D. Scott and A. D. Sokal, *The Repulsive Lattice Gas, the Independent-Set Polynomial, and the Lovász Local Lemma*, 2003 preprint, https://arxiv.org/abs/cond-mat/0309352 ; journal version 2005.
- E. W. Weisstein, *Helm Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/HelmGraph.html ; includes the known univariate independence polynomial.
- E. W. Weisstein, *Independence Polynomial*, Wolfram MathWorld, https://mathworld.wolfram.com/IndependencePolynomial.html .
