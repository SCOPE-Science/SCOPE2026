# All-degree harmonic sampling on the \(E_6\) and \(E_7\) root lines

## Finding
For either root system \(E_d\), where \(d\in\{6,7\}\), let \(X_d\) contain exactly one unit-normalized representative of each antipodal root line. Thus \(|X_6|=36\) and \(|X_7|=63\). Let \(\mathcal H_\ell(S^{d-1})\) be the complex homogeneous spherical harmonics of exactly degree \(\ell\), with their probability-surface-measure \(L^2\) norm, and let \(E_\ell f=(f(x))_{x\in X_d}\). For **every** nonnegative integer \(\ell\), the ranks are

\[
\begin{array}{c|rrrrr|c}
 &\ell=0&1&2&3&4&\ell\ge5\\\hline
E_6&1&6&20&30&35&36\\
E_7&1&7&27&56&62&63
\end{array}
\]

In particular, degree five is the sharp permanent-surjectivity threshold for both exceptional root-line configurations. Degree three loses exactly \(d\) sampling directions despite the harmonic space being large enough to interpolate, and the degree-four attainable data are precisely the mean-zero hyperplane. The theorem also gives every Gram eigenvalue at every degree and the exact minimum-norm interpolation operator.

Write \(h_{d,\ell}=\binom{d+\ell-1}{\ell}-\binom{d+\ell-3}{\ell-2}\), with the second binomial term interpreted as zero for \(\ell<2\), and
\[
a_\ell=\frac{C_\ell^{((d-2)/2)}(1/2)}{C_\ell^{((d-2)/2)}(1)},\qquad
b_\ell=\frac{C_\ell^{((d-2)/2)}(0)}{C_\ell^{((d-2)/2)}(1)}.
\]
These numbers are rational for all integer \(\ell\). The **complete** eigenvalue multipliers of \(E_\ell E_\ell^*/h_{d,\ell}\) are:

* For odd \(\ell\), \(1+\kappa_d a_\ell\) with multiplicity \(d\), and \(1-2a_\ell\) with multiplicity \(|X_d|-d\), where \(\kappa_6=10\) and \(\kappa_7=16\).
* For even \(\ell\), \(1+k_da_\ell+(|X_d|-1-k_d)b_\ell\) with multiplicity one, \(1-b_\ell+r_d(a_\ell-b_\ell)\) with multiplicity \(u_d\), and \(1-b_\ell+s_d(a_\ell-b_\ell)\) with multiplicity \(v_d\), where \((k_d,r_d,s_d,u_d,v_d)=(20,2,-4,20,15)\) for \(d=6\) and \((32,4,-4,27,35)\) for \(d=7\).

The corresponding eigenspace projectors depend only on the finite root-line geometry, not the harmonic degree. Consequently the spectrum determines the complete attainable-data subspace and the unique minimum-\(L^2\)-norm interpolant for every degree, including all defective degrees.

## Assumptions and scope
Use standard simply-laced \(E_6\) and \(E_7\) roots, normalized to length one; changing signs or root-system coordinates only conjugates the sampling Gram by a diagonal sign matrix for odd degrees and does not change its spectrum or rank. Complex harmonics are used; no real-signal, positivity, noisy-observation, or higher-band union claim is made. The sampled data carry the usual unweighted counting norm; harmonics use probability-normalized spherical surface measure. At degree zero, set \(h_{d,0}=1\).

## Proof
**1. Exact root geometry.** Represent the 240 \(E_8\) roots at twice their usual coordinates by (i) all vectors having two entries \(\pm2\) and six zeros and (ii) all sign vectors \((\pm1,\ldots,\pm1)\) with an even number of minus signs. Their squared Euclidean length is eight. The vectors with final three coordinates equal form 72 roots of rank six; those with final two coordinates equal form 126 roots of rank seven. Select the lexicographically greater of \(v\) and \(-v\), giving \(N=36\) or \(63\) lines.

Let \(S_{ij}=\langle v_i,v_j\rangle/4\) for \(i\ne j\) and \(S_{ii}=0\), where these are the doubled integral vectors, and let \(A_{ij}=|S_{ij}|\). Every off-diagonal \(S_{ij}\) lies in \(\{-1,0,1\}\). Direct integer dot-product counting gives
\[
\begin{array}{c|c|c|c}
d&N& S^2-(\kappa_d-2)S-2\kappa_d I&A^2\\\hline
6&36&0&8I-2A+12J\\
7&63&0&16I+16J
\end{array}
\]
and \(A\mathbf1=k_d\mathbf1\), with \(k_6=20\), \(k_7=32\). Here \(J\) is the all-ones matrix. Both matrices are symmetric and have zero diagonal. Their minimal polynomial identities, trace, and constant eigenvector yield \(S\)-eigenvalues \(\kappa_d\) (multiplicity \(d\)) and \(-2\) (multiplicity \(N-d\)), and \(A\)-eigenvalues \(k_d\) (once), \(r_d\) (multiplicity \(u_d\)), and \(s_d\) (multiplicity \(v_d\)) with parameters specified above. All these finite identities are generated and verified independently by the supplied script; the definitions give a finite exact certificate rather than relying on a graph-table lookup.

**2. Harmonic kernels.** The spherical addition theorem with probability normalization gives
\[
G_\ell(i,j)=h_{d,\ell}\frac{C_\ell^{((d-2)/2)}(\langle x_i,x_j\rangle)}{C_\ell^{((d-2)/2)}(1)}.
\]
For odd \(\ell\), parity and \(C_\ell(0)=0\) give \(G_\ell/h_{d,\ell}=I+a_\ell S\). For even \(\ell\), \(G_\ell/h_{d,\ell}=I+a_\ell A+b_\ell(J-I-A)\). Diagonalizing the two finite symmetric matrices proves the spectral formulas. The exact rational Gegenbauer recurrence verifies the listed vanishing and positivity of all multipliers at degrees \(0\) through \(79\), including the rank table.

**3. Unrestricted positivity.** For \(\lambda>0\), the normalized Gegenbauer polynomial admits the probability-integral representation
\[
\frac{C_\ell^\lambda(t)}{C_\ell^\lambda(1)}=
\frac{\Gamma(\lambda+1/2)}{\sqrt\pi\,\Gamma(\lambda)}
\int_{-1}^{1}\bigl(t+i\sqrt{1-t^2}\,u\bigr)^\ell (1-u^2)^{\lambda-1}\,du.
\]
Taking absolute values, using \(1-z\le e^{-z}\), changing variables \(u=\cos\theta\), and applying \(\sin\theta\ge2\theta/\pi\) on \([0,\pi/2]\), yields, for \(|t|<1\) and \(\ell\ge1\),
\[
\left|\frac{C_\ell^\lambda(t)}{C_\ell^\lambda(1)}\right|
\le\frac{\Gamma(\lambda+1/2)}{\sqrt\pi}
\left(\frac{\pi^2}{2\ell(1-t^2)}\right)^\lambda.
\]
For \(\ell\ge80\), \(\pi^2<10\), and \(\lambda=2\) or \(5/2\), these give rational upper estimates:
\[
\begin{array}{c|cc}
d&|a_\ell|&|b_\ell|\\\hline
6&\le 100/(3\ell^2)&\le75/(4\ell^2)\\
7&\le800/(9\ell^2)&\le50/\ell^2
\end{array}
\]
(the last row uses \(2/\sqrt\pi<2\) and the fact that powers \(5/2\) are at most powers \(2\) when the base is below one). Thus the even-degree strict diagonal-dominance row-sum bounds are \(11375/(12\ell^2)<1\) for \(d=6\) and \(39100/(9\ell^2)<1\) for \(d=7\). In odd degrees the deviations of the two signed-adjacency multipliers from one are bounded by at most \(1000/(3\ell^2)<1\) and \(12800/(9\ell^2)<1\), respectively. Hence every eigenvalue is strictly positive for every \(\ell\ge80\). Together with the finite exact calculation, this proves full interpolation at every degree at least five.

**4. Exact images and minimal norm.** Define \(P_0=J/N\), \(P_r=(A-s_dI-(k_d-s_d)P_0)/(r_d-s_d)\), \(P_s=I-P_0-P_r\), and \(Q_+=(S+2I)/(\kappa_d+2)\), \(Q_-=I-Q_+\). In even degrees the data image is the sum of \(P_0,P_r,P_s\) eigenspaces having positive multipliers; in odd degrees it is the analogous sum of \(Q_+,Q_-\). If \(T\) denotes \(E_\ell E_\ell^*\) and \(y\) belongs to its range, \(f_*=E_\ell^*T^+y\) is the unique minimum-norm interpolant, with \(\|f_*\|_2^2=y^*T^+y\). The pseudoinverse is obtained by reciprocating the nonzero listed eigenvalues on the corresponding explicit projectors. For \(\ell=4\) this reduces to \(\mathbf1^*y=0\); for \(\ell=3\) the missing data space is the \(d\)-dimensional range of \(Q_+\).

## Verification
Run `python check_exceptional_pair.py` with Python 3 and SymPy. The program generates the actual root-line coordinates, verifies all integer matrix identities and their trace-based eigenvalue multiplicities, checks all exact rational spectral signs for degrees 0–79, and verifies the strict analytic cutoff inequalities. It prints `ALL_CHECKS_OK 172`. These finitely many computations do not independently prove an infinite theorem; the displayed Gegenbauer integral estimate supplies the high-degree proof. The Gram diagonalization follows algebraically from the displayed matrix identities.

## Relationship to prior work
Delsarte–Goethals–Seidel (1977) established spherical-code/design and zonal-Gegenbauer methods. Bussemaker–Cvetković–Seidel (1976) studied graphs associated with exceptional roots; their graph-related work is directly pertinent to the known finite spectral ingredients, not claimed here as new. Cohn–Kumar (arXiv posted July 19, 2006) developed spherical-energy theory involving classical exceptional configurations. The contribution assessed here is the all-degree **individual harmonic evaluation** rank cutoff, the complementary cubic defect, and the complete sampling/reconstruction statements on both \(E_6\) and \(E_7\) line configurations. The known methods and graph spectra are necessary mathematical predecessors; they are not independently reproduced as new contributions.

## Limitations
The full 1976 root-graph memorandum was identified but not read because its download endpoint was inaccessible and institutional retrieval was unavailable; it remains a concrete originality risk. The 1977 primary spherical-code article likewise was not reviewed in full. Older general association-scheme treatments could implicitly contain an equivalent complete rank cutoff. Results are self-reviewed only, not independently certified or peer reviewed. No claim is made about other point orbits, weighted samples, or joint degree bands. The 1976 historical report has a verified publication year (and a June cover-month in its indexed snippet), but no exact public release day verified; the first-public-date metadata uses the first precisely day-verified archival lead source rather than fabricating a day in 1976.

## References
1. H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, arXiv:math/0607446, first posted 2006-07-19. https://arxiv.org/abs/math/0607446
2. F. C. Bussemaker, D. M. Cvetković and J. J. Seidel, *Graphs related to exceptional root systems*, Eindhoven University of Technology memorandum 7609, 1976. https://research.tue.nl/en/publications/graphs-related-to-exceptional-root-systems-3/
3. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, doi:10.1007/BF03187604.
4. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, Journal of Approximation Theory 195 (2015), 1–18, doi:10.1016/j.jat.2014.06.010.
