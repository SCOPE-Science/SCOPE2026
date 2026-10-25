# All strict subcritical Campanato–Morrey embeddings without upper regularity

## Finding
Let \(X=[0,1]\) have its Euclidean metric and the finite Borel measure
\[
 d\mu(t)=\log(e/t)\,dt\qquad(0<t\le1).
\]
The measure is doubling (with doubling constant at most \(8\)) and lower \(1\)-regular, but is not upper \(1\)-regular. Nevertheless, **for every** \(1\le p<\infty\) and **every** \(0\le\lambda<1\), the radius-normalized Campanato-to-Morrey inclusion
\[
 L_C^{p,\lambda}(X,\mu)\hookrightarrow L_M^{p,\lambda}(X,\mu)
\]
is continuous. At the critical exponent \(\lambda=1\), the inclusion fails even for the constant function \(1\). This gives a negative answer to Question 2 of Górka–Stępień [1], including when the measure is assumed doubling and lower \(1\)-regular.

## Assumptions and scope
For \(x\in X\) and \(r>0\), write \(B(x,r)=X\cap(x-r,x+r)\), with endpoint conventions immaterial to \(\mu\). For an integrable \(f\), write \(f_B=\mu(B)^{-1}\int_B f\,d\mu\). In the precise radius-normalized conventions of [1],
\[
 [f]_{C^{p,\lambda}}=
 \sup_{x\in X,r>0}r^{-\lambda/p}
 \left(\int_{B(x,r)}|f-f_{B(x,r)}|^p\,d\mu\right)^{1/p},
\]
\[
 \|f\|_{L_C^{p,\lambda}}=\|f\|_{L^p(\mu)}+[f]_{C^{p,\lambda}},\qquad
 \|f\|_{L_M^{p,\lambda}}=
 \sup_{x\in X,r>0}r^{-\lambda/p}
 \left(\int_{B(x,r)}|f|^p\,d\mu\right)^{1/p}.
\]
Here \(f\in L_C^{p,\lambda}\) is understood to belong to \(L^p(X,\mu)\). Constants of the inclusion may depend on \(p\) and \(\lambda\); uniformity as \(\lambda\uparrow1\) is not claimed. The theorem is about these global spaces on this specified measured interval, not about arbitrary measures or local definitions with different normalizations.

## Proof
**1. Exact mass formula and uniform ball estimates.** Define \(F(0)=0\) and \(F(t)=2t-t\log t\) for \(0<t\le1\). Then \(\mu([a,b])=F(b)-F(a)\), and \(\mu(X)=2\). Fix \(0<r\le1\), and put \(a=\max(0,x-r)\), \(b=\min(1,x+r)\), \(\ell=b-a\), and \(L_r=\log(e/b)\). Since \(r\le\ell\le2r\), \(L_r\ge1\), and
\[
 \mu(B(x,r))=\ell L_r+\int_a^b\log(b/t)\,dt,
\]
while
\[
 0\le\int_a^b\log(b/t)\,dt
 =\ell+a\log(a/b)\le\ell
\]
(the expression at \(a=0\) is interpreted by continuity), we obtain
\[
 rL_r\le\mu(B(x,r))\le4rL_r. \tag{1}
\]
For \(0<r\le R\le1\), the corresponding right endpoints obey \(b_R/b_r\le R/r\). Thus \(L_r\le L_R+\log(R/r)\), where \(L_R\ge1\), and (1) gives the **uniform reverse growth bound**
\[
 \frac{\mu(B(x,R))}{\mu(B(x,r))}
 \ge\frac{R/r}{4(1+\log(R/r))}. \tag{2}
\]
Also \(b_r\ge r\), so \(\mu(B(x,r))\le4r\log(e/r)\). Consequently, for every \(0\le\lambda<1\),
\[
 \mu(B(x,r))\le A_\lambda r^\lambda\quad(r>0),
 \qquad A_\lambda=\frac{4e^{-\lambda}}{1-\lambda}. \tag{3}
\]
Indeed, maximize \(e^{-(1-\lambda)s}(1+s)\) over \(s\ge0\); the case \(r\ge1\) follows from \(\mu(X)=2\) and \(A_\lambda\ge4\).

**2. Subcritical embedding via nested-ball averages.** Fix \(1\le p<\infty\) and \(0\le\lambda<1\). Let \(0<r<1\), set \(B_j=B(x,2^jr)\), and let \(n\ge1\) be least such that \(2^nr\ge1\). Then \(B_n=X\) up to a null set. By Hölder's inequality and the Campanato definition,
\[
 |f_{B_j}-f_{B_{j+1}}|
 \le\frac{(2^{j+1}r)^{\lambda/p}}{\mu(B_j)^{1/p}}[f]_{C^{p,\lambda}}
 \qquad(0\le j<n). \tag{4}
\]
Applying (2) to the pair of radii \(r\) and \(2^jr<1\) gives
\[
 \frac{\mu(B_0)}{\mu(B_j)}\le
 4(1+j\log2)2^{-j}\qquad(0\le j<n).
\]
Telescoping (4) and using the convergent sum
\[
 S_{p,\lambda}=\sum_{j=0}^{\infty}
 (1+j\log2)^{1/p}2^{-j(1-\lambda)/p}<\infty
\]
therefore yields
\[
 \left(\frac{\mu(B_0)}{r^\lambda}\right)^{1/p}|f_{B_0}-f_X|
 \le4^{1/p}2^{\lambda/p}S_{p,\lambda}[f]_{C^{p,\lambda}}. \tag{5}
\]
Since \(|f_X|\le2^{-1/p}\|f\|_{L^p(\mu)}\), (3) and (5), followed by Minkowski's inequality on \(B_0\), show
\[
 \|f\|_{L_M^{p,\lambda}}
 \le\left(\frac{A_\lambda}{2}\right)^{1/p}\|f\|_{L^p(\mu)}
 +\left(1+4^{1/p}2^{\lambda/p}S_{p,\lambda}\right)[f]_{C^{p,\lambda}}. \tag{6}
\]
For \(r\ge1\), the Morrey expression is at most \(\|f\|_{L^p(\mu)}\), also covered by (6). Thus (6) proves continuous inclusion for each exponent strictly below \(1\). For \(\lambda=0\), the equality \(L_M^{p,0}=L^p(X,\mu)\) offers an independent immediate check.

**3. Measure regularity and the sharp endpoint.** The density obeys \(\log(e/t)\ge1\). Hence \(\mu(B(x,r))\ge r\) for \(0<r\le1\), while for \(1<r<3\) one has \(\mu(B(x,r))=2\ge(2/3)r\), proving lower \(1\)-regularity. By (1), for \(0<r\le1/2\),
\[
 \frac{\mu(B(x,2r))}{\mu(B(x,r))}\le8,
\]
and for larger \(r\) the ratio is at most \(4\), proving doubling. However,
\[
 \frac{\mu(B(0,r))}{r}=2-\log r\longrightarrow\infty
 \qquad(r\downarrow0),
\]
so upper \(1\)-regularity fails. The constant \(f\equiv1\) has finite Campanato norm \(2^{1/p}\), yet has infinite Morrey norm when \(\lambda=1\), establishing the exact critical boundary.

## Verification
The proof is symbolic and requires no infinite-search or numerical extrapolation. The primitive \(F\), the integral estimate in (1), the mass ratio (2), and the geometric-logarithmic convergence of \(S_{p,\lambda}\) are the critical independently checkable steps. A separate deterministic finite-sample script `checks/weight_sanity.py` reproduces the exact ball mass formula and numerically samples (2) and doubling; its finite tests are illustrative and are **not** used to establish either embedding or the endpoint failure.

## Relationship to prior work
Górka–Stępień [1], Theorem 3.2(1), proves the same subcritical inclusion when the measure is Ahlfors \(Q\)-regular; Theorem 3.2(2) proves that a single \(\lambda\)-inclusion forces **upper \(\lambda\)-regularity**, and Question 2 asks whether having all \(\lambda<Q\) inclusions forces upper \(Q\)-regularity. The measure here is upper \(\lambda\)-regular for each strict exponent by (3), but not upper \(1\)-regular, while (6) verifies all the inclusions. Thus neither direction in that theorem implies this example. Stempak–Tao [2] studies generalized local Morrey and Campanato spaces on quasimetric measure spaces, but the reviewed global-space discussion does not state this specific radius-normalized all-subcritical obstruction; those wider frameworks remain a possible route to an implicit reformulation.

## Limitations
This is a counterexample to an endpoint inference, not a classification of metric measures. The constants in (6) depend on \(p\) and \(\lambda\) and diverge in the displayed bound as \(\lambda\uparrow1\); no uniform endpoint estimate is asserted. The log-singular measure remains finite, nonatomic, doubling, lower \(1\)-regular and Borel regular. The novelty assessment is literature-relative and does not constitute an independent exhaustive review.

## References
[1] P. Górka and Z. Stępień, *Optimal Embeddings of Campanato and Morrey Spaces*, arXiv:2610.04622v1 (first public 2026-10-03), especially Section 2.2, Theorem 3.2 and Question 2. https://arxiv.org/pdf/2610.04622

[2] K. Stempak and X. Tao, *Local Morrey and Campanato Spaces on Quasimetric Measure Spaces*, Journal of Function Spaces 2014, Article ID 172486, especially Section 3. https://doi.org/10.1155/2014/172486
