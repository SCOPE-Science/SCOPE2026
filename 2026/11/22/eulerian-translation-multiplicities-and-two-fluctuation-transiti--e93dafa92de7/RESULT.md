# Eulerian translation multiplicities and two fluctuation transitions for hypersimplices

## Finding
For integers \(n\ge2\), \(1\le k<n\), and \(t\ge1\), let
\[
\Delta_{n,k}=\{x\in[0,1]^n:\textstyle\sum_{i=1}^n x_i=k\},
\qquad P_{n,k,t}=t\Delta_{n,k}.
\]
Choose \(U\) according to Haar probability on the torus \(H/\Lambda\), with
\[
H=\{u\in\mathbb R^n:\textstyle\sum_i u_i=0\},\qquad
\Lambda=H\cap\mathbb Z^n,
\]
and count \(N_{n,k,t}(U)=\#((P_{n,k,t}+U)\cap\mathbb Z^n)\). This is well-defined on \(H/\Lambda\), since changing \(U\) by an integral vector simply relabels counted lattice points.

Write \(A(m,r)\) for the Eulerian number counting permutations of \(m\) elements with exactly \(r\) descents, and let
\[
C_{n,t}(s)=[z^s](1+z+\cdots+z^{t-1})^n,
\]
with \(C_{n,t}(s)=0\) outside \(0\le s\le n(t-1)\). For every nonnegative integer \(v\), the *exact full counting distribution* is
\[
\Pr(N_{n,k,t}=v)
=\frac1{(n-1)!}\sum_{j=1}^{n-1} A(n-1,j-1)
\mathbf1\{C_{n,t}(tk-j)=v\}.
\tag{1}
\]
Equivalently, \(N_{n,k,t}\overset{d}=C_{n,t}(tk-J_n)\) where
\(\Pr(J_n=j)=A(n-1,j-1)/(n-1)!\). In particular,
\[
\Pr(N_{n,k,t}>0)
=\frac1{(n-1)!}\sum_{j=1}^{n-1}A(n-1,j-1)
\mathbf1\{tk-n(t-1)\le j\le tk\},
\tag{2}
\]
and
\[
\mathbb E N_{n,k,t}
=\frac{t^{n-1}A(n-1,k-1)}{(n-1)!}.
\tag{3}
\]

For each fixed integer \(t\ge2\), suppose \(k_n/n\to\rho\in(0,1)\). The probability in (2) tends to one for
\(1/(2t)<\rho<1-1/(2t)\), and to zero for
\(0<\rho<1/(2t)\) or \(1-1/(2t)<\rho<1\). Its *exact Gaussian edge scales* are: for fixed real \(a\),
\[
\begin{aligned}
&k_n=\frac{n}{2t}+a\sqrt n+o(\sqrt n)
&&\Longrightarrow\ \Pr(N_{n,k_n,t}>0)\to\Phi(\sqrt{12}\,t a),\\
&k_n=n\bigl(1-\frac1{2t}\bigr)+a\sqrt n+o(\sqrt n)
&&\Longrightarrow\ \Pr(N_{n,k_n,t}>0)\to\Phi(-\sqrt{12}\,t a).
\end{aligned}\tag{4}
\]
Here \(\Phi\) denotes the standard normal distribution function. These rank windows are nondegenerate for every \(t\ge2\).

At \(t=2\) there is a *second, different fluctuation change*, inside the almost-sure occupancy region. Indeed \(C_{n,2}(s)=\binom ns\) and, whenever
\(k_n=n/2+a\sqrt n+o(\sqrt n)\),
\[
\log\max\{1,N_{n,k_n,2}\}-n\log2
+\frac12\log(\pi n/2)
\ \xrightarrow{\ d\ }\ -2\left(2a-\frac Z{\sqrt{12}}\right)^2,
\tag{5}
\]
where \(Z\) is standard normal. For \(a=0\) this is \(-\chi_1^2/6\); for nonzero \(a\) it is a scaled noncentral chi-square. By contrast, for any fixed \(\rho\in(1/4,3/4)\setminus\{1/2\}\), \(k_n=\lfloor\rho n\rfloor\), and \(\beta=2\rho-1/2\),
\[
\frac{\log\max\{1,N_{n,k_n,2}\}-n h(\beta)}{\sqrt n}
\xrightarrow{\ d\ }\mathcal N\left(0,\frac1{12}\log^2\frac{1-\beta}{\beta}\right),
\quad h(x)=-x\log x-(1-x)\log(1-x).
\tag{6}
\]
Thus translation occupancy has two Gaussian edge windows, whereas the logarithmic multiplicity has a chi-square central crossover and Gaussian off-center fluctuations.

## Assumptions and scope
All probabilities refer to intrinsic, *orientation-preserving translations inside the affine span*, not random rotations, random lattices, or full ambient \(\mathbb R^n\) translations. Coordinates of \(U\) are chosen modulo the root lattice \(\Lambda\), and \(n,k,t\) are integral as specified. Hyperplanes have sum \(kt\) after translation, so the intersection with \(\mathbb Z^n\) is meaningful. The use of \(\log\max\{1,N\}\) in (5)--(6) makes the expressions defined even on rare empty events. Bounds at exact finite \(n\) include all generic translates; the measure-zero set of translations with a coordinate integral does not affect the distribution. The transition (4) holds for fixed \(t\ge2\), not for \(t\) growing with \(n\).

## Proof
**Step 1 (Haar parameters and Eulerian law).** Identify \(H/\Lambda\) with \((\mathbb R/\mathbb Z)^{n-1}\) using its first \(n-1\) coordinates. For a Haar-uniform \(U\), the fractional parts \(f_i=\{-U_i\}\), \(1\le i<n\), are independent uniform \((0,1)\). Since \(\sum U_i=0\), the last fractional part is
\(f_n=\lceil\sum_{i<n}f_i\rceil-\sum_{i<n}f_i\), almost surely. Consequently
\(J_n=\sum_{i=1}^n f_i=\lceil\sum_{i<n}f_i\rceil\). The uniform-cube slice identity (equivalently the Irwin--Hall law or Laplace's Eulerian hypersimplex volume formula) gives
\[
\Pr(J_n=j)=\frac{A(n-1,j-1)}{(n-1)!},\qquad 1\le j<n.
\]
For \(n\ge3\), the usual Eulerian mean and variance give \(\mathbb E J_n=n/2\) and \(\mathrm{Var}(J_n)=n/12\); the latter also follows from the Irwin--Hall local distribution, and only its asymptotic is needed below.

**Step 2 (complete arithmetic count).** For each integral point \(z\in(P_{n,k,t}+U)\cap\mathbb Z^n\), the vector \(x=z-U\in P_{n,k,t}\) has coordinates \(x_i=q_i+f_i\) with \(q_i\in\{0,\ldots,t-1\}\), except on the null boundary set. Conversely every such \(n\)-tuple with \(\sum q_i=tk-J_n\) determines exactly one lattice point \(z\). Hence
\(N_{n,k,t}=C_{n,t}(tk-J_n)\) pointwise outside that null set, proving (1). Inclusion-exclusion yields the optional computable formula
\[
C_{n,t}(s)=\sum_{b=0}^{\lfloor s/t\rfloor}(-1)^b\binom nb
\binom{s-tb+n-1}{n-1},\quad 0\le s\le n(t-1).
\]
Each integer between zero and \(n(t-1)\) is a sum of \(n\) integers in \(\{0,\ldots,t-1\}\); therefore positivity is equivalent to the condition in (2). Finally, integrating the number of lattice points over a fundamental parallelepiped equals the intrinsic volume of the body divided by the root-lattice covolume, by disjoint tiling and Tonelli's theorem. The hypersimplex's normalized volume is \(A(n-1,k-1)/(n-1)!\), proving (3). The independent integer identity behind this step is directly checked in the accompanying program.

**Step 3 (outer occupancy windows).** Write \(S_{n-1}=\sum_{i=1}^{n-1}f_i\). By the usual central limit theorem,
\[
\frac{J_n-n/2}{\sqrt{n/12}}\ \xrightarrow{\ d\ }\ Z.
\]
Indeed \(J_n-S_{n-1}\in[0,1]\) while \(\mathbb E S_{n-1}=(n-1)/2\) and \(\mathrm{Var}(S_{n-1})=(n-1)/12\). Substitute \(J_n\) into the exact interval in (2). Away from the two threshold ratios, both interval endpoints lie a linear distance from \(n/2\); the weak law gives limits zero or one. At the lower boundary the lower endpoint is a linear distance *below* \(n/2\), and the upper endpoint is \(n/2+ta\sqrt n+o(\sqrt n)\). At the upper boundary the upper endpoint is a linear distance *above* \(n/2\), and the lower endpoint is \(n/2+ta\sqrt n+o(\sqrt n)\). The normal distribution has no atoms; this proves both limits in (4), including equality \(a=0\).

**Step 4 (central log-multiplicity crossover).** For \(t=2\), the coefficient in Step 2 is \(\binom n{2k-J_n}\) when the lower index belongs to \([0,n]\), otherwise zero. The CLT gives \(J_n=n/2+\sqrt{n/12}Z_n\), \(Z_n\Rightarrow Z\). Under the central scale for \(k_n\), the binomial lower index is
\[
2k_n-J_n=n/2+\sqrt n\left(2a-Z_n/\sqrt{12}\right)+o(\sqrt n).
\]
This lies in \((0,n)\) with probability tending to one. Uniform Stirling expansion for lower-index deviations \(O(\sqrt n)\), uniformly on bounded scaled intervals, states
\[
\log\binom n{n/2+y\sqrt n}
=n\log2-\frac12\log(\pi n/2)-2y^2+o(1).
\]
Tightness of \(Z_n\) and continuous mapping yield (5). For the off-center regime, the index equals \(n\beta-(J_n-n/2)+O(1)\); the entropy expansion \(\log\binom n{np}=nh(p)+O(\log n)\) and a first-order Taylor expansion yield
\[
\log N_{n,k_n,2}
=nh(\beta)-h'(\beta)(J_n-n/2)+o_{\Pr}(\sqrt n),
\]
where \(h'(\beta)=\log((1-\beta)/\beta)\). The CLT proves (6); the probability of an empty translate tends to zero, so replacing \(\log N\) by \(\log\max\{1,N\}\) does not change its distributional limit.

## Verification
Run `python3 checker.py` with Python 3 and no third-party packages. The checker verifies 225 exact all-dilation Eulerian-volume identities at \(2\le n\le10\), \(1\le k<n\), \(1\le t\le5\); directly enumerates bounded compositions for the smaller sizes; and checks 720 random intrinsic geometric translations by enumerating their integer points independently from the coefficient formula. It also compares the exact finite-size central logarithmic deficit moments at \(n=40,80,160,320\) to the derived \(-\chi_1^2/6\) limits. The finite computations are reproducibility checks, not proofs of the asymptotic statements.

## Relationship to prior work
The Eulerian volume identity is classical (Laplace; see Li's 2011 exposition), as is the generating-function coefficient for bounded compositions. The 2026 translation-count work of Freyer and Hofstätter studies deterministic translation functions, uniqueness, eigen-decompositions and general inequalities; it does not state the intrinsic hypersimplex Eulerian mixture, occupancy edge windows, or the chi-square central log-count transition. Higashitani--Murai--Yoshinaga (first posted 2023, published 2025) give general toric-arrangement algorithms for translated Ehrhart quasi-polynomials, but no dimension-varying probability limits for this hypersimplex model. Their general algorithms may, in principle, be applied separately at each dimension; the present explicit joint distribution and asymptotic transitions require additional derivation. This is a scoped comparison, not a claim of exhaustive historical priority.

## Limitations
Uniform translations are intrinsic to the affine span; full-dimensional ambient translations would almost surely have no lattice point at all. The local boundary and concentration results do not address nonintegral dilations, dependent random orientations, or general matroid base polytopes. The exact formulas do not assert that every distinct Eulerian slice yields a different numeric multiplicity. The log-multiplicity asymptotics require \(t=2\), and the edge-window theorem keeps \(t\) fixed. Historical literature may contain equivalent formulas under another translation/occupancy terminology; independently checking that possibility is outside the scope of the stated mathematical proof. No independent validation is claimed.

## References
- A. Freyer and G. C. Hofstätter, *Counting Lattice Points in Translations: Uniqueness and Existence Results*, arXiv:2610.26523 (first posted 19 October 2026), https://arxiv.org/html/2610.26523v2.
- A. Higashitani, S. Murai and M. Yoshinaga, *Ehrhart quasi-polynomials and parallel translations*, Combinatorial Theory 5 (2025), article 13; preprint arXiv:2307.08151, https://arxiv.org/abs/2307.08151.
- N. Li, *Ehrhart \(h^*\)-vectors of hypersimplices*, arXiv:1104.5292 (2011), https://arxiv.org/abs/1104.5292.
