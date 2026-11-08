# Hypercube dimension barriers and a sharp three-cube threshold for Gauss–Legendre heat steps

## Finding

For the unit-edge-rate graph heat equation on the Boolean \(d\)-cube \(Q_d\), let \(L_d=dI-A_d\) be its positive combinatorial Laplacian, and let \(T_{s,d}(h)\) be the \(s\)-stage Gauss–Legendre collocation end-step applied to \(u'=-L_du\), where \(s,d\) are positive integers and \(h\ge0\).

**Theorem (dimension and parity barrier).** For all \(s,d,h\), \(T_{s,d}(h)\mathbf1=\mathbf1\), and all its eigenvalues have modulus at most one (strictly less than one on nonconstant modes at \(h>0\)). For every even \(s\), the eigenvalues are positive at finite \(h\), but if \(d\ge3\), every entry joining adjacent cube vertices is strictly negative for all sufficiently large \(h\). For every odd \(s\) and every \(d\ge2\), the diagonal entries are strictly negative for all sufficiently large \(h\). In dimension one, all stages preserve entrywise nonnegativity at every \(h\ge0\). For the two-stage method, unconditional nonnegativity holds exactly when \(d\le2\).

On the first failing cube \(Q_3\), the two-stage method has the **sharp complete** step-size interval

\[
T_{2,3}(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad 0\le h\le\rho,
\]

where \(\rho\) is the unique positive root of
\[
p(h)=h^4-6h^3-20h^2-18h-6,
\qquad 8.583763463<\rho<8.583763464.
\]

For \(h>\rho\), precisely the entries between adjacent vertices turn negative; the diagonal and distance-two and distance-three entries stay strictly positive. Thus the method retains mass, symmetry, and positive scalar eigenvalues after losing entrywise positivity.

## Assumptions and scope

Vertices are \(\{0,1\}^d\); two vertices are adjacent exactly when they differ in one coordinate. Edge-flip rates are one, so the eigenvalues of \(L_d\) are \(2j\), \(j=0,\ldots,d\). The numerical transition is the exact rational matrix functional calculus for the \(s\)-stage Gauss–Legendre end-step, not a stage-by-stage positivity claim. Numerical step size \(h\) is measured in inverse unit edge rate; multiplying every edge rate by \(c>0\) replaces \(h\) by \(ch\). The theorem covers every positive integer \(s,d\). Entrywise nonnegativity means all matrix coefficients are nonnegative, and the vector \(\mathbf1\) denotes constants.

## Proof

**1. Rational stability function and scalar spectral sign.** Gauss–Legendre collocation has diagonal Padé stability function
\[
R_s(z)=\frac{P_s(z)}{P_s(-z)},\qquad
P_s(z)=\sum_{k=0}^{s}\frac{s!(2s-k)!}{(2s)!\,k!(s-k)!}z^k.
\]
Its integral representation is
\[
P_s(z)=\frac1{(2s)!}\int_0^{\infty}e^{-t}t^s(t+z)^s\,dt,
\]
obtained by binomial expansion and factorial integration. For every \(x>0\), \(P_s(x)>|P_s(-x)|\), because \(|t-x|<t+x\) for positive \(t,x\) inside the integral. Consequently \(|R_s(-x)|<1\). If \(s\) is even, the same integral makes \(P_s(-x)>0\) and therefore \(0<R_s(-x)<1\). Also \(R_s(0)=1\). Since \(L_d\) is real symmetric, the asserted row sums and spectral bounds follow.

**2. Walsh diagonalization.** For a displacement of Hamming distance \(r\), Walsh characters give the scalar entry
\[
T_{s,d}^{(r)}(h)=2^{-d}\sum_{j=0}^{d}K_j^{(d)}(r)R_s(-2jh),
\quad
K_j^{(d)}(r)=\sum_{a=0}^{j}(-1)^a\binom ra\binom{d-r}{j-a},
\]
with impossible binomial coefficients interpreted as zero. In particular \(\sum_{j=0}^dK_j^{(d)}(r)=2^d\mathbf1_{r=0}\). The first-neighbour coefficients are
\[
K_j^{(d)}(1)=\binom{d-1}{j}-\binom{d-1}{j-1}.
\]
All entries at equal Hamming distance coincide, so these \(d+1\) expressions constitute a complete entrywise characterization.

**3. Large-step parity.** The leading two coefficients of \(P_s\) satisfy \(a_{s,s-1}/a_{s,s}=s(s+1)\). For odd \(s\), \(R_s(-x)\to-1\) as \(x\to\infty\), while the zero eigenmode stays at one. Therefore
\[
T_{s,d}(h)\longrightarrow 2^{1-d}\mathbf1\mathbf1^{\mathsf T}-I,
\qquad s\text{ odd},
\]
whose diagonal \(2^{1-d}-1\) is negative for \(d\ge2\).

For even \(s\), the same coefficient ratio yields
\[
R_s(-x)=1-\frac{2s(s+1)}x+O_s(x^{-2}).
\]
Thus for adjacent cube vertices
\[
T_{s,d}^{(1)}(h)=-\frac{s(s+1)}{2^dh}S_d+O_{s,d}(h^{-2}),
\qquad
S_d=\sum_{j=1}^d\frac{\binom{d-1}{j}-\binom{d-1}{j-1}}j.
\]
The generating polynomial \((1-t)(1+t)^{d-1}\) gives
\[
S_d=\int_0^1\frac{(1-t)(1+t)^{d-1}-1}{t}\,dt,
\qquad
S_{d+1}-S_d=\int_0^1(1-t)(1+t)^{d-1}\,dt>0.
\]
Direct evaluation gives \(S_3=1/6\). Hence \(S_d>0\) for all \(d\ge3\) and the displayed leading adjacent coefficient is strictly negative for sufficiently large \(h\).

**4. The low-dimensional boundary.** For \(Q_1\), the two entries are \((1+R_s(-2h))/2\) and \((1-R_s(-2h))/2\), strictly positive for \(h>0\). For \(Q_2\) with \(s=2\), set
\[
D_2(h)=(h^2+3h+3)(4h^2+6h+3)>0.
\]
The respective distance-zero, one, and two entries are
\[
\frac{4h^4+3h^3+6h^2+9h+9}{D_2(h)},\qquad
\frac{3h}{4h^2+6h+3},\qquad
\frac{9h^2(h+1)}{D_2(h)}.
\]
These are all nonnegative for \(h\ge0\). Part 3 establishes failure for every \(d\ge3\), proving the two-stage if-and-only-if statement.

**5. Exact sharp boundary on \(Q_3\).** For \(s=2\), the stability scalar is
\[
R_2(-x)=\frac{1-x/2+x^2/12}{1+x/2+x^2/12}.
\]
For \(r=0,1,2,3\), the corresponding \(T_{2,3}^{(r)}(h)\) has common positive denominator
\[
D_3(h)=2(h^2+3h+3)(3h^2+3h+1)(4h^2+6h+3),
\]
and the following numerators in order:
\[
\begin{aligned}
N_0(h)&=24h^6+45h^5+44h^4+36h^3+66h^2+54h+18,\\
N_1(h)&=-3h(h^4-6h^3-20h^2-18h-6),\\
N_2(h)&=3h^2(7h^3+18h^2+18h+6),\\
N_3(h)&=3h^3(11h^2+18h+6).
\end{aligned}
\]
The denominator and \(N_0,N_2,N_3\) are strictly positive for \(h>0\). The quartic \(p\) has exactly one positive root by Descartes' rule of signs (one sign change), continuity, and its negative value at zero and positive leading term. An exact rational evaluation gives \(p(8583763463/10^9)<0<p(8583763464/10^9)\), so its unique positive root is \(\rho\) in the claimed interval. Since \(N_1=-3hp\), this completes the classification, including the endpoint \(h=0\), where \(T=I\).

## Verification

The companion standalone standard-library Python program `verify_hypercube.py` implements exact rational stability functions, Walsh/Krawtchouk weights, independent direct \(8\times8\) rational matrix multiplication, numerator polynomial identity checks, root-bracketing tests, mass-preservation identities, and sampled large-step sign tests. It prints `VERIFY_OK checks=1080` on a successful execution. The source of the universal statement is the algebraic and analytic argument above; finite checks provide reproducibility and error detection, not proof for all dimensions, stages, or step sizes.

## Relationship to prior work

Blanes, Iserles, and Macnamara establish the general need for positivity-preserving integrators on graph-Laplacian systems and discuss limitations of ordinary high-order Runge–Kutta approaches. Banjai and Ferrari give the relevant Gauss-method Padé stability representation in a different, convolution-quadrature context. Zappavigna, Colaneri, Kirkland, and Shorten exhibit Markov-positivity failures for Padé methods on other generators, including an eight-state one-way chain; their construction is not the reversible-cube classification or the sharp \(Q_3\) interval proved here.

Previously reported exact positivity classifications for Gauss steps on cycles, strongly regular graphs, and complete multipartite graphs cover \(Q_1\) and \(Q_2\), but not the non-strongly-regular, non-multipartite \(Q_d\) for \(d\ge3\). The new content is the universal even-stage edge-sign obstruction on Boolean cubes and the exact all-steps first-failure threshold on \(Q_3\). A database or title search cannot by itself certify novelty; specialist duplication remains possible.

## Limitations

The positive-step interval is completely classified only for the two-stage method on the three-cube; a sharp threshold for every higher-dimensional cube or every number of stages is not claimed. Eventual negativity does not assert monotonicity of all entries across intermediate steps. Positivity refers to the final one-step matrix, not intermediate Runge–Kutta stages or floating-point implementations. The fixed-edge-rate normalization must be rescaled for other heat generators. Literature overlap remains subject to independent specialist review.

## References

- S. Blanes, A. Iserles, S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242 (first posted February 16, 2021), https://arxiv.org/abs/2102.08242 .
- L. Banjai, M. Ferrari, *Runge-Kutta convolution quadrature based on Gauss methods*, arXiv:2212.07170 (first posted December 14, 2022), https://arxiv.org/abs/2212.07170 .
- A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially negative results for matrix functions preserving positivity*, preprint publicly available at https://mural.maynoothuniversity.ie/id/eprint/3761/ (2012).
