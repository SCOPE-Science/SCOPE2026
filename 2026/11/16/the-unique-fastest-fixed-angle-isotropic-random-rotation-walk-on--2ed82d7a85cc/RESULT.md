# The unique fastest fixed-angle isotropic random rotation walk on \(\mathrm{SO}(3)\)

## Finding

Let \(P_\theta\) be the Markov convolution operator on normalized Haar \(L^2(\mathrm{SO}(3))\) obtained by rotating through a **fixed** angle \(\theta\in[0,\pi]\) about an independently uniform random unoriented axis at each step. Write \(\Pi f=\int_{\mathrm{SO}(3)}f\,dg\). Among all such fixed-angle one-step laws, the exact sharp nonconstant \(L^2\)-operator contraction is

\[
\min_{0\leq\theta\leq\pi}\|P_\theta-\Pi\|_{2\to2}
=\rho_*:=\frac{\sqrt[3]{35}-2}{9}
=0.141229590020954\ldots .
\]

There is exactly one minimizing angle,

\[
\theta_*=\arccos\!\left(-\frac{1+\sqrt[3]{35}}6\right)
=2.362917121238644\ldots\ \text{radians}
=135.385178386177\ldots^\circ.
\]

At this angle, the only extremal nonconstant Fourier sectors are spins \(\ell=1\) and \(\ell=3\), with eigenvalues respectively \(-\rho_*\) and \(+\rho_*\); their regular-representation multiplicities are \(9\) and \(49\). All other nonconstant spin sectors have strictly smaller eigenvalue modulus. Consequently, for each integer \(k\ge1\),

\[
\min_{0\leq\theta\leq\pi}\|P_\theta^{\,k}-\Pi\|_{2\to2}=\rho_*^k,
\]

and the same unique angle is optimal for every fixed iteration count \(k\).

## Assumptions and scope

The group is the compact rotation group \(G=\mathrm{SO}(3)\), with normalized Haar measure. The one-step probability is the conjugacy-class law \(\mu_\theta\), i.e. the pushforward of Haar measure by \(g\mapsto gR_\theta g^{-1}\), where \(R_\theta\) is a rotation through \(\theta\) around a fixed axis. Define \(P_\theta f(x)=\int f(h^{-1}x)\,d\mu_\theta(h)\). The angle is fixed for every step; the axes are independently Haar-uniform. We optimize the operator norm on the mean-zero space, not total variation from a point mass and not the larger class of mixtures of angles or anisotropic step laws.

The irreducible representations of \(G\) are indexed by integers \(\ell\ge0\), with dimension \(2\ell+1\). Conjugation invariance and Schur's lemma yield the real Fourier scalar

\[
\lambda_\ell(\theta)
=\frac{\chi_\ell(\theta)}{2\ell+1}
=\frac{\sin((\ell+\tfrac12)\theta)}{(2\ell+1)\sin(\theta/2)}
=\frac{1+2\sum_{j=1}^{\ell}\cos(j\theta)}{2\ell+1},
\]

with its continuous limit at \(\theta=0\). The trivial sector \(\ell=0\) has eigenvalue one and is removed by \(\Pi\). Peter–Weyl therefore gives \(\|P_\theta-\Pi\|=\sup_{\ell\ge1}|\lambda_\ell(\theta)|\).

## Proof

**Step 1: three controlling Fourier polynomials.** Set \(c=\cos\theta\in[-1,1]\). The first three nonconstant scalars are

\[
L_1(c)=\frac{1+2c}{3},\qquad
L_2(c)=\frac{4c^2+2c-1}{5},\qquad
L_3(c)=\frac{8c^3+4c^2-4c-1}{7}.
\]

Their first/third balance equation is

\[
L_1(c)+L_3(c)=\frac{2}{21}(12c^3+6c^2+c+2)
=\frac{(6c+1)^3+35}{189}.
\]

It has exactly one real solution \(c_*=-(1+\sqrt[3]{35})/6\), which satisfies \(-5/7<c_*<-7/10\). At that point, \(L_1(c_*)=-\rho_*\) and \(L_3(c_*)=+\rho_*\), with \(\rho_*=(\sqrt[3]{35}-2)/9\). Direct rational bracketing implies

\[
\frac2{15}<\rho_*<\frac17,\qquad
\left|L_2(c_*)\right|\le\frac{11}{125}<\frac2{15}.
\]

**Step 2: the remaining infinitely many sectors are strictly smaller at balance.** For all \(\ell\ge4\), the character formula and \(c_*<-7/10\) imply

\[
|\lambda_\ell(\theta_*)|
\le\frac{1}{(2\ell+1)\sin(\theta_*/2)}
\le\frac{1}{9\sqrt{17/20}}<\frac2{15}<\rho_*.
\]

Combining this with Step 1 proves \(\|P_{\theta_*}-\Pi\|=\rho_*\), and that only spins one and three attain the norm.

**Step 3: global sharpness and uniqueness.** Let \(b=-3/5\) and \(d=(-1+3\rho_*)/2\). The bounds in Step 1 imply \(-3/10<d<-2/7<-1/4\). Divide the entire interval \([-1,1]\) into four parts:

- For \(-1\le c<c_*\), the increasing function \(L_1(c)\) obeys \(L_1(c)<-\rho_*\).
- For \(c_*<c\le b\), the cubic \(L_3(c)\) has one interior maximum and no interior minimum: its derivative is \((24c^2+8c-4)/7\), with the only critical point in this interval equal to \((-1-\sqrt7)/6\). Thus its minimum over \([c_*,b]\) is at an endpoint. The endpoint values are \(L_3(c_*)=\rho_*\) and \(L_3(b)=139/875>1/7>\rho_*\), proving \(L_3(c)>\rho_*\) for \(c>c_*\) in this range.
- For \(b\le c\le d\), the derivative \(L_2'(c)=(8c+2)/5\) is negative, because \(d<-1/4\). Thus \(L_2(c)\le L_2(b)=-19/125<-1/7<-\rho_*\).
- For \(d<c\le1\), \(L_1(c)>L_1(d)=\rho_*\).

Every \(c\ne c_*\) therefore has at least one spin \(\ell\in\{1,2,3\}\) with \(|L_\ell(c)|>\rho_*\). At \(c=c_*\) the supremum is exactly \(\rho_*\), establishing both global optimality and uniqueness. The estimates include \(c=\pm1\) and hence the angular endpoints. The final power assertion follows from selfadjoint diagonalization: \(\|P_\theta^k-\Pi\|=\big(\sup_{\ell\ge1}|\lambda_\ell(\theta)|\big)^k\).

## Verification

The included standalone `VERIFY.py` uses only the Python standard library. It checks the exact rational bracket values for the balance polynomial, the two comparison endpoints, the high-spin tail inequality, agreement of character and polynomial formulae at 300 sample points, and the lower bound across 2,001 angle grid values and 150 spin levels, along with 1,997 higher-spin checks at the optimizer. One execution reported **4,305 passing assertions**, with \(c_*\approx-0.7118443850314317\), \(\theta_*\approx2.362917121238644\), and \(\rho_*\approx0.1412295900209544\). These finite checks supplement, but do not substitute for, the all-angle, infinite-spin argument above.

## Relationship to prior work

Rosenthal (1994) defines the same fixed-angle conjugacy-class rotation walk on \(\mathrm{SO}(N)\) and develops the irreducible-character framework, but his stated results concern high-dimensional total-variation cutoff bounds, especially \(\theta=\pi\), not the exact three-dimensional mean-zero operator-norm minimax. Hough and Jiang (2012) examine all fixed angles in the uniform-plane walk and characterize high-dimensional mixing asymptotics; their Theorems 1.1–1.3 address the large-\(N\) regime, not the present all-spin optimization at \(N=3\). Al-Dayel and Deshmukh (2023) give Fourier-character expansions for continuous-time Brownian rotations and a geometric overlap observable, not this discrete fixed-angle optimal design. Here the new statement is specifically the **unique best fixed angle**, its closed radical value, and the exact two-sector extremality across all nontrivial representations.

## Limitations

The result compares only **single-angle conjugation-invariant** probability measures. It does not optimize among arbitrary mixtures of angles (Haar measure itself would trivialize an unconstrained one-step mixing problem), does not assert optimality for finite-axis discrete designs, and does not equate the \(L^2\) operator contraction rate with the total-variation distance from a Dirac initial state. Although the character formulae are classical and the argument is elementary once those are known, older literature may contain an equivalent minimax observation not identified in the sources checked. The statement has not undergone independent verification.

## References

1. Jeffrey S. Rosenthal, *Random Rotations: Characters and Random Walks on SO(N)*, Annals of Probability **22** (1994), 398–423. Author-hosted full text: https://probability.ca/jeff/ftpdir/rots.pdf ; DOI: https://doi.org/10.1214/aop/1176988864.
2. Bob Hough and Yunjiang Jiang, *Cut-off phenomenon in the uniform plane Kac walk*, first arXiv posting 2012-11-09, https://arxiv.org/abs/1211.2031.
3. Ibrahim Al-Dayel and Sharief Deshmukh, *The Heat Equation on Submanifolds in Lie Groups and Random Motions on Spheres*, Mathematics **11** (2023), 1958, first published 2023-04-20, https://doi.org/10.3390/math11081958.
