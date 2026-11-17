# Sharp uniform Parry mixing in all-orientation high-entropy interval maps

## Finding
For every integer \(n\ge3\) and every orientation word \(\varepsilon\in\{+1,-1\}^{n}\), the canonical affine interval map of Oliveira [1, Theorem 7.1] has a primitive \(n\)-state Markov adjacency matrix \(M_\varepsilon\). Every non-Perron eigenvalue lies in the closed unit disk. Consequently the Parry chain of its unique measure of maximal entropy has asymptotic mixing rate
\[
\eta_\varepsilon=\frac{\max\{|\xi|:\xi\in\operatorname{spec}(M_\varepsilon),\ \xi\ne\lambda_\varepsilon\}}{\lambda_\varepsilon}\le\frac1{\lambda_\varepsilon}\le\frac1{n-1}.
\]
This is sharp in its dependence on the number of branches: for the word containing \(n-1\) increasing signs followed by one decreasing sign,
\[
\lambda_\varepsilon=\frac{n-1+\sqrt{(n-1)(n+3)}}2,\qquad
\eta_\varepsilon=\frac{n-1}{\lambda_\varepsilon^2},\qquad
\lim_{n\to\infty}n\eta_\varepsilon=1.
\]
Thus exponentially many distinct mixed-orientation Markov realizations have a **uniform, sharp inverse-branch-number maximal-entropy relaxation scale**, despite the different orientation words.

## Assumptions and scope
Fix \(n\ge3\) and \(\varepsilon=(\varepsilon_0,\dots,\varepsilon_{n-1})\in\{+1,-1\}^n\). Use exactly the affine branches and equal subinterval partition from [1, Theorem 7.1]; arbitrary maps with the same orientation word are not covered. Put
\[
A=\#\{1\le j<n:\varepsilon_{j-1}=-1,\ \varepsilon_j=+1\},\qquad
B=\#\{1\le j<n:\varepsilon_{j-1}=+1,\ \varepsilon_j=-1\},\quad\kappa=A+B.
\]
The published construction gives \(M=J-u e_0^{\mathsf T}-v e_{n-1}^{\mathsf T}\), where \(J\) is all ones; the disjoint indicator vectors \(u,v\) mark those respective orientation switches. Set \(a_*=1\) if the last switch is from minus to plus and \(b_*=1\) if it is from plus to minus; otherwise the corresponding indicator is zero. They cannot both equal one. \(\lambda=\rho(M)\) is the Perron eigenvalue. The Parry chain is \(P_{ij}=M_{ij}r_j/(\lambda r_i)\), for a strictly positive right Perron vector \(r\). Its mixing rate means the spectral-root rate of \(P^m-\mathbf1\pi^{\mathsf T}\) as \(m\to\infty\), with any matrix norm; the statement is asymptotic in time for fixed \(n\), not a uniform finite-time total-variation estimate.

## Proof
Every row of \(M\) has at least \(n-1\) ones and every column has at least two ones (for an outer column, at most \(\lceil(n-1)/2\rceil\) orientation changes of its type can occur). Any row support of size at least \(n-1\) intersects every column's support of size at least two, so \(M^2\) is strictly positive. Hence the chain is primitive and \(n-1\le\lambda\le n\) by row-sum bounds.

Oliveira [1, Theorem 7.2, equation (7.2)] proves that all nonzero eigenvalues of \(M\) are among the roots of
\[
Q(z)=z^3-(n-b_*)z^2+(\kappa-nb_*)z+(Ab_*-Ba_*).
\]
All remaining eigenvalues are zero. We now bound the two remaining roots, counting multiplicity.

**No terminal switch.** If \(a_*=b_*=0\), then \(Q(z)=z(z^2-nz+\kappa)\). The smaller quadratic root is nonnegative and equals \(\kappa/\lambda\le(n-1)/\lambda\le1\); the third root is zero.

**Terminal minus-to-plus switch.** If \(a_*=1,b_*=0\), the two roots after \(\lambda\) have real sum \(n-\lambda\in[0,1]\) and nonnegative product \(B/\lambda\le1\). If they are real, both are nonnegative and individually at most one; if nonreal, their common modulus is \(\sqrt{B/\lambda}\le1\).

**Terminal plus-to-minus switch.** If \(a_*=0,b_*=1\), then
\[
Q(-1)=-B\le0,\qquad Q(0)=A\ge0,\qquad Q(1)=\kappa+A-2(n-1)\le0.
\]
Since the Perron root satisfies \(\lambda\ge n-1>1\) and is simple, the cubic has a root in \([-1,0]\) and one in \([0,1]\), with the remaining root equal to \(\lambda\). This also handles vanishing \(A\) or \(B\) by continuity or the endpoint zero. These cases exhaust the orientations and establish the unit-disk bound.

Diagonal similarity \(P=(1/\lambda)D^{-1}MD\) with \(D=\operatorname{diag}(r)\) transfers the eigenvalues and, by Perron-Frobenius and the spectral-radius formula, yields the stated asymptotic rate. For \(\varepsilon=(+1,\ldots,+1,-1)\) there is only the final plus-to-minus switch: \(A=0,B=1\) and \(M=J-e_{n-1}e_{n-1}^{\mathsf T}\). Its nonzero eigenvalues are the roots of \(z^2-(n-1)z-(n-1)\). Their product is \(-(n-1)\); dividing the negative root's modulus by the positive one gives \(\eta=(n-1)/\lambda^2\). As \(\lambda/n\to1\), the sharp limit follows.

## Verification
The standalone Python checker `verify.py` constructs all \(2^n\) orientation words for each \(3\le n\le12\), generates their adjacency matrices and evaluates the published cubic. It tests primitivity, all nonleading eigenvalue moduli at most one, and the sharp-example formula. These finite checks support the algebra but are not substituted for the proof for arbitrary \(n\). Execute `python verify.py` with Python 3 and NumPy.

## Relationship to prior work
The canonical affine Markov matrices, their cubic characteristic polynomials and high-entropy bounds are due to Oliveira [1]. These inputs are not claimed as new. The new conclusion is the uniform **all-orientation subleading-spectrum inclusion**, its Parry-measure rate bound, and the asymptotically sharp realizing orientation family. Coles and Pavlov [2] give general primitive-matrix mixing estimates, but their general irreducibility/chainability inequalities do not already assert this specialized unit-disk spectrum. Earlier exact results for the Lebesgue-invariant, switching-indicator process in a terminal-agreeing subfamily concern another measure and do not imply the Parry full-chain spectral bound. Optimally tuned symmetric Markov kernels on incomplete graphs likewise address a different optimization problem and do not cover these forced (possibly asymmetric) Parry kernels.

## Limitations
The theorem applies to the *canonical* equal-branch affine Markov realizations in [1], not to arbitrary piecewise monotone maps. It bounds the asymptotic spectral mixing rate of the Parry Markov measure; it does not establish uniform-in-\(n\) prefactors for total variation, a physical/Lebesgue correlation bound, or mixing rates for nonlinear perturbations. Historical spectral-graph literature not indexed by targeted searches may contain equivalent specializations. Independent external mathematical validation has not been performed.

## References
[1] Henrique M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1, first public 2026-11-02, Theorems 7.1–7.2 and equation (7.2). https://arxiv.org/html/2611.03287v1

[2] Solly Coles and Ronnie Pavlov, *Spectral gaps and mixing rates of primitive matrices*, arXiv:2611.10951v1, first public 2026-11-07. https://arxiv.org/html/2611.10951v1
