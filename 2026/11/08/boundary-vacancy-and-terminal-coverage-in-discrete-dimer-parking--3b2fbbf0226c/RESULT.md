# Boundary vacancy and terminal coverage in discrete dimer parking

## Finding

Fix an integer \(n\geq 2\). In the discrete Page--Rényi parking process on a line of \(n\) sites, independent uniform attempts park length-two dimers on adjacent vacant sites until no further dimer fits. Let \(V_n\) be the terminal indicator that the **first site is vacant**, and let \(M_n\) be the **number of occupied sites** (twice the number of successfully parked dimers). Set

\[
T_k(c)=\sum_{j=0}^{k}\frac{(-c)^j}{j!}\quad(k\geq0),\qquad T_{-1}(c)=0.
\]

The three finite-size moments have the exact formulas

\[
\begin{aligned}
e_n:=\mathbb E[V_n]&=T_{n-1}(1),\\
a_n:=\mathbb E[M_n]&=n\bigl(1-T_{n-1}(2)\bigr)-2T_{n-2}(2),\\
b_n:=\mathbb E[V_nM_n]&=\left(n-\tfrac12\right)\bigl(T_{n-1}(1)-T_{n-1}(3)\bigr)-3T_{n-2}(3).
\end{aligned}
\]

Consequently, the exact covariance is \(c_n=b_n-e_na_n\). Its complete sign classification is

\[
\boxed{c_n=0\ \text{for }n\in\{2,3,5\},\qquad c_n<0\ \text{for }n=4\text{ or }n\geq6.}
\]

Moreover its nonzero boundary--bulk thermodynamic limit is

\[
\boxed{\lim_{n\to\infty}c_n=-\frac{e^{-1}+e^{-3}}2\approx-0.20883325476965314.}
\]

The exceptional zero at \(n=5\) reflects deterministic terminal coverage: all outcomes then occupy four sites, whereas the covariance at \(n=4\) equals \(-4/9\).

## Assumptions and scope

There are exactly \(n-1\) initially available adjacent pairs. At each attempt a uniformly chosen pair is filled if and only if both sites are vacant. Attempts repeat indefinitely; the terminal packing is almost surely well-defined. Equivalently assign independent, atomless random priorities to all \(n-1\) pairs, scan pairs once in increasing priority order, and accept a pair if its sites remain vacant. The first successful pair divides the residual sites into independent left and right intervals. The result concerns finite uniform paths, with no periodic boundary, no desorption, no size-three cars, and no continuum intervals. For the recurrences below define \(a_0=a_1=0\), \(e_0=0,e_1=1\), and \(b_0=b_1=0\); the stated theorem itself begins at \(n=2\).

## Proof

Condition on the left endpoint of the first parked dimer. It is uniformly distributed over \(1,\ldots,n-1\). If its left residual segment has length \(j\), then the right segment has length \(n-2-j\), and the two residual parking processes are independent. For \(n\geq2\), this immediately gives

\[
\begin{aligned}
a_n&=2+\frac{2}{n-1}\sum_{j=0}^{n-2}a_j,\\
e_n&=\frac1{n-1}\sum_{j=1}^{n-2}e_j,\\
b_n&=\frac1{n-1}\sum_{j=1}^{n-2}\bigl(b_j+e_j(2+a_{n-2-j})\bigr).
\end{aligned}
\tag{1}
\]

The first equation uses reflection symmetry of both residual intervals. In the last two equations, the event that site one is vacant forces the first pair not to touch site one, so the left segment is nonempty. When the first site in the residual left segment remains vacant, its occupancy count is multiplied by the independent total occupation of the right segment plus the first dimer's two sites.

Write \(A(z)=\sum_{n\geq0}a_nz^n\), \(E(z)=\sum_{n\geq0}e_nz^n\), and \(B(z)=\sum_{n\geq0}b_nz^n\). Equation (1), with the stated initial conditions, yields identities of formal power series

\[
A(z)=\frac{z(1-e^{-2z})}{(1-z)^2},\qquad
E(z)=\frac{ze^{-z}}{1-z}.
\]

For the third recurrence, multiplying by \(z^n\) and summing gives

\[
zB'(z)-B(z)=\frac{z^2}{1-z}B(z)+\frac{2z^2}{1-z}E(z)+z^2E(z)A(z).
\]

The analogous equation for \(E\) cancels the homogeneous part and gives

\[
\left(\frac{B}{E}\right)'=\frac{2z}{1-z}+zA(z).
\]

The ratio has zero constant term, and integration gives

\[
\frac{B(z)}{E(z)}=
\frac{1-e^{-2z}}{1-z}-z-\frac12+\frac{e^{-2z}}2.
\tag{2}
\]

Expanding the two exponentials and extracting coefficients from the rational factors in (2) proves all three displayed moment formulas, for every integer \(n\geq2\).

To prove the sign for *all* lengths rather than merely check initial terms, denote \(L=-(e^{-1}+e^{-3})/2\). The alternating Taylor remainder bound

\[
|T_k(c)-e^{-c}|\leq\frac{c^{k+1}}{(k+1)!}
\quad(c\in\{1,2,3\},\ k\geq0)
\]

and \(0\leq a_n\leq n\) applied to the moment formulas imply

\[
|c_n-L|\leq R_n:=\frac{(n-\tfrac12)(1+3^n)+3n3^{n-1}+n+2n2^n}{n!}.
\tag{3}
\]

Every positive summand defining \(R_n\) is strictly decreasing in \(n\) for \(n\geq11\), by taking consecutive-term ratios. Thus

\[
R_n\leq R_{11}=\frac{275267}{2851200}<\frac16
\quad\text{for all }n\geq11.
\]

Since \(e<3\), one has \(-L=(e^{-1}+e^{-3})/2>1/6\); hence \(c_n<0\) for every \(n\geq11\). Exact rational substitution for \(2\leq n\leq10\) gives zeros precisely at \(2,3,5\) and strictly negative values otherwise. In particular, for \(n=4,6,7,8,9,10\), these values are respectively

\[
-\frac49,\quad-\frac{77}{225},\quad-\frac{91}{648},\quad
-\frac{1751}{7350},\quad-\frac{25651}{129600},\quad-\frac{13656971}{64297800}.
\]

Finally, \(T_k(c)\to e^{-c}\), with factorially decaying errors, in the closed-form moments. The terms linear in \(n\) cancel in \(b_n-e_na_n\), leaving exactly \(L\), as asserted.

## Verification

The accompanying standard-library script `verify_parking.py` independently implements the recurrences and closed forms using arbitrary-precision rational arithmetic, exhaustively scans every \((n-1)!\) pair-priority ordering for each \(2\leq n\leq9\), and verifies finite formulas and their signs for \(2\leq n\leq100\). The extraction replay passed 523 exact assertions. The proof of the infinite sign classification is the analytic remainder inequality (3), not a finite enumeration; the script also checks \(R_{11}<1/6\).

Reproduce with `python3 verify_parking.py` in the same directory. No external packages, network access, or random seeds are required.

## Relationship to prior work

Gerin's *The Page--Rényi parking process* (arXiv:1411.8002; 2015 journal version) explicitly studies the same dimer model, provides first-dimer decomposition for total occupancy, proves asymptotic density, bounds correlations in the infinite process, and computes an example of a short-range pair correlation. It does not state the finite mixed moment between a distinguished boundary-vacancy indicator and total occupation, its exceptional lengths, or its nonzero limiting covariance. Shneer--van de Ven's *Per-site occupancy in the discrete parking problem* derives one-point site occupancy probabilities and expected jamming density but not this mixed moment. Both sources establish the relevance of finite boundary effects without furnishing the stated boundary--global dependence classification. Formula (1) requires a new mixed-moment marking in addition to their marginals. The result may nevertheless be implicitly derivable from more general historical multivariate treatments; no absolute historical-priority assertion is made.

## Limitations

The theorem concerns only ordinary length-two Page parking on a finite path and only one specified terminal boundary/global covariance. No monotonicity of its magnitude in \(n\) is claimed (indeed the values oscillate). The result does not give the full two-point correlation kernel or fluctuations for other car lengths. Published literature was not exhaustively searched; historical generalizations might imply some or all of the formula. No independent audit has been performed.

## References

1. L. Gerin, *The Page--Rényi parking process*, arXiv:1411.8002, first publicly posted 28 November 2014; *Electronic Journal of Combinatorics* 22(4) (2015), P4.4, https://doi.org/10.37236/5150 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i4p4/pdf/ .
2. S. Shneer and P. M. van de Ven, *Per-site occupancy in the discrete parking problem*, preprint dated 29 August 2016, https://ir.cwi.nl/pub/25286/parking5.pdf .
3. P. J. Flory, *Intramolecular reaction between neighboring substituents of vinyl polymers*, *Journal of the American Chemical Society* 61 (1939), 1518--1521 (historical model reference as cited in Gerin).
4. E. S. Page, *The distribution of vacancies on a line*, *Journal of the Royal Statistical Society, Series B* 21 (1959), 364--374 (historical model reference as cited in Gerin).
