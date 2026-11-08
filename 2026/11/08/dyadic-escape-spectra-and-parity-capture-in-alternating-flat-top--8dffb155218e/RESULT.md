# Dyadic escape spectra and parity capture in alternating flat-top tent maps

## Finding

Consider alternating a height limiter with the full tent map on \([-1,1]\). For the complete natural dyadic family of limiter heights \(u_m=1-2^{-m}\), \(m\ge1\), the exceptional never-limited set has an exactly soluble finite-state entropy, Hausdorff dimension, and Lebesgue escape law. Writing \(k=\lfloor m/2\rfloor\), the surviving transition matrix has Perron root \(\lambda_m\), characterized by
\[
\begin{cases}
\lambda_m^k(4-\lambda_m)=2,&m=2k,\quad k\ge1,\\
\lambda_m^k(4-\lambda_m)=1,&m=2k+1,\quad k\ge0.
\end{cases}
\]
The root lies in \((3,4)\), except \(\lambda_1=3\). The survivor-set dimension and exponential escape rate per two-step return are exactly
\[
\dim_H X_m=\frac{\log\lambda_m}{\log4},\qquad
\gamma_m=\log\frac4{\lambda_m}.
\]
The entire finite-time first-hit distribution is a finite matrix formula given below. The exceptional set has zero Lebesgue measure. Every other point enters the limiter interval in finite time and then lands on one specific finite forward orbit. For odd \(m=2k+1\), that orbit is a superstable least-period-\(k+1\) cycle containing the origin; for even \(m=2k\), all such points land after finitely many further steps on the repelling fixed point \(-1\). The escape rate has the parity-uniform sharp expansion
\[
\gamma_m=p_m+(k+\tfrac12)p_m^2+O(k^2p_m^3),\qquad
p_m=2^{-m-1},\quad m\to\infty.
\]
The first-order term is the normalized limiter-interval length, while the second-order coefficient depends on the dyadic preperiod.

## Assumptions and scope

Put \(T(x)=1-2|x|\), \(C_u(x)=\min\{u,T(x)\}\), and \(F_m=T\circ C_{u_m}\), with \(u_m=1-2^{-m}\) and integer \(m\ge1\). Thus the first step of each two-step cycle is limited and the next step is the full tent map. Set \(H=T^2\), \(r_m=2^{-m-1}\), and \(I_m=(-r_m,r_m)\). Exactly,
\[
F_m(x)=\begin{cases}
-1+2^{1-m},&|x|<r_m,\\
H(x),&|x|\ge r_m.
\end{cases}
\]
Define \(\tau_m(x)=\min\{j\ge0:H^j(x)\in I_m\}\), with \(\tau_m(x)=\infty\) if there is no visit, and \(X_m=\{x:\tau_m(x)=\infty\}\). The first-hit law uses normalized Lebesgue probability \(\Pr(E)=\operatorname{Leb}(E)/2\) on \([-1,1]\). First-hit statements refer to the uncontrolled map \(H\) up to the first visit, which agrees with \(F_m\) before capture. No claim is made about arbitrary nondyadic limiter heights or nonperiodic limiting schedules.

## Proof

### Critical orbit and exact finite Markov partition

The four affine pieces of \(H\) on \([-1,-\tfrac12]\), \([-\tfrac12,0]\), \([0,\tfrac12]\), and \([\tfrac12,1]\) are, respectively,
\[
4x+3,\quad -4x-1,\quad 4x-1,\quad 3-4x.
\]
For \(m=2k\) include the endpoints \(-1,-\tfrac12,-r_m,0,r_m,\tfrac12,1\), and the additional orbit points \(-1+2/4^j\) for \(2\le j\le k\). For \(m=2k+1\) include the same base endpoints and \(-1+1/4^j\) for \(1\le j\le k\). These ordered endpoint sets are forward invariant under \(H\): each nontrivial negative point \(-1+c/4^j\) moves to \(-1+c/4^{j-1}\); the two hole boundaries map to the last such point (or directly to \(-\tfrac12\) in the even base case and to \(0\) in the odd base case); and \(H(0)=-1\), \(H(-\tfrac12)=H(\tfrac12)=1\), \(H(\pm1)=-1\).

Delete the two open Markov cells \((-r_m,0)\) and \((0,r_m)\). Order the remaining closed cells as consecutive negative cells \(L_0,\ldots,L_h\) followed by \(B=[-\tfrac12,-r_m]\), \(C=[r_m,\tfrac12]\), and \(D=[\tfrac12,1]\). Here \(h=k-1\) when \(m=2k\), and \(h=k\) when \(m=2k+1\). In every cell \(H\) is affine of absolute slope \(4\). Let \(A_m(i,j)=1\) precisely when the image of cell \(i\) covers cell \(j\), and zero otherwise. Images are unions of whole partition cells and the deleted hole cells, by the forward-invariant endpoint property.

The complete transition rules, where 'all' means every retained cell and 'noninitial' means all except \(L_0\), are as follows.

For even \(m\) and \(h\ge1\): \(L_0\to L_0,L_1\); \(L_j\to L_{j+1}\) for \(1\le j<h\); \(L_h\to B,C,D\); \(B,C\to\text{noninitial}\); \(D\to\text{all}\). When \(h=0\), \(L_0,D\to\text{all}\) and \(B,C\to B,C,D\).

For odd \(m\) and \(h\ge2\): \(L_0\to L_0,L_1\); \(L_j\to L_{j+1}\) for \(1\le j<h-1\); \(L_{h-1}\to L_h,B\); \(L_h\to C,D\); \(B,C\to\text{noninitial}\); \(D\to\text{all}\). When \(h=1\), replace the first rule by \(L_0\to L_0,L_1,B\), keeping \(L_1\to C,D\). When \(h=0\), \(L_0,D\to\text{all}\) and \(B,C\to C,D\). These rules follow by substituting each pair of endpoints in the four displayed affine pieces.

Every vertex reaches \(D\), and \(D\) reaches every vertex and has a self-loop. Thus \(A_m\) is irreducible and aperiodic (primitive). The graph-directed interval system formed by the inverse branches has mutually disjoint interiors and common contraction ratio \(1/4\).

### Eigenvalues and dimension

For even \(h\ge1\), a positive right Perron eigenvector has entries \(z_0,\ldots,z_h,b,b,d\). Put \(S=\sum_{j=0}^h z_j+2b+d\). The row rules give \(\lambda b=S-z_0\), \(\lambda d=S\), \(\lambda z_0=z_0+z_1\), \(\lambda z_j=z_{j+1}\) for \(1\le j<h\), and \(\lambda z_h=2b+d\). Therefore \(z_0=\lambda(d-b)\), \(z_j=\lambda^{j-1}(\lambda-1)z_0\) for \(1\le j\le h\), and \(S=\lambda^h z_0+2b+d\). Eliminating \(b,d,S\) yields \(\lambda^{h+1}(4-\lambda)=2\). For \(h=0\), the four-row equations directly yield \(\lambda(4-\lambda)=2\).

For odd \(h\ge2\), the same notation gives \(\lambda z_{h-1}=z_h+b\), \(\lambda z_h=b+d\), and \(\lambda z_j=z_{j+1}\) for \(1\le j<h-1\), along with the same \(B,C,D\) equations. Hence \(z_{h-1}=\lambda^{h-2}(\lambda-1)z_0\), \(z_h=\lambda^{h-1}(\lambda-1)z_0-b\), and \(S=\lambda^h z_0+b+d\). These identities reduce to \(\lambda^h(4-\lambda)=1\). The explicit \(h=1\) and \(h=0\) matrices give respectively \(\lambda(4-\lambda)=1\) and \(\lambda=3\).

For both parities, the polynomial has exactly one root in \((3,4)\), with the base case \(\lambda_1=3\): for \(k\ge1\), the function \(t^k(4-t)\) starts above the right-hand side at \(t=3\), can increase only up to its single interior maximum, and then decreases to zero at \(t=4\). The positive eigenvalue is consequently the Perron root. Laplace expansion along the successive singleton-transition rows, followed by the identical \(B,C\) rows, gives the quotient recurrence \(Q_{h+1}(t)=tQ_h(t)+c(1-t)\), where \(c=2\) in the even family and \(c=1\) in the odd family; the base quotients are \(Q_0(t)=t^2-4t+2\) and \(Q_0(t)=t-3\), respectively. This also gives the complete characteristic identities
\[
\det(tI-A_m)=\begin{cases}
t^2\bigl(t^{k+1}-4t^k+2\bigr),&m=2k,\\
t^3\bigl(t^{k+1}-4t^k+1\bigr),&m=2k+1.
\end{cases}
\]
(The determinant identities are not needed to identify the Perron root; they provide additional reproducible checks.) Standard graph-directed interval counting and the open set condition give \(\dim_H X_m=\log\lambda_m/\log4\). Countably many boundary itineraries do not alter the dimension.

### Exact finite-time distribution and escape asymptotics

Let \(\ell_j\) be the lengths of the retained cells, regarded as a column vector, and \(\mathbf1\) the all-ones column of compatible size. The inverse branch associated to each permitted transition scales length by exactly \(1/4\). Thus, for every integer \(n\ge1\),
\[
\Pr\{\tau_m\ge n\}
=\frac{\mathbf1^\mathsf{T} A_m^{n-1}\ell}{2\,4^{n-1}}.
\]
This formula counts every itinerary, not only asymptotic survivors; the endpoint set has zero Lebesgue measure. The graph is primitive, so Perron--Frobenius theory supplies a positive leading coefficient and \(\lim_{n\to\infty}-n^{-1}\log\Pr\{\tau_m\ge n\}=\log(4/\lambda_m)\). In particular, \(\Pr\{\tau_m=\infty\}=0\). For example \(m=1\) gives \(\Pr\{\tau_1\ge n\}=(3/4)^n\), and \(m=2\) gives \(\Pr\{\tau_2\ge1\}=7/8\), \(\Pr\{\tau_2\ge2\}=3/4\), and \(\Pr\{\tau_2\ge3\}=41/64\).

Writing \(p_m=2^{-m-1}\), \(\delta_m=1-\lambda_m/4\), the two parity polynomial identities both become \(\delta_m(1-\delta_m)^k=p_m\). Since \(kp_m\to0\), the root near zero satisfies \(\delta_m=p_m+kp_m^2+O(k^2p_m^3)\). Expanding \(-\log(1-\delta_m)\) proves the stated second-order escape law.

### What follows after first capture

For odd \(m=2k+1\), \(F_m(0)=-1+1/4^k\); the next \(k\) applications of \(F_m=H\) outside \(I_m\) follow the negative endpoint orbit and return to \(0\). All the intermediate points lie outside \(I_m\), hence \(0\) lies on a primitive period-\(k+1\) orbit. Its derivative product is zero because one step crosses the constant plateau. Every state that enters \(I_m\) is mapped onto this cycle after the first limited step.

For even \(m=2k\), the plateau maps to \(-1+2/4^k\). The subsequent \(k-1\) steps follow the negative endpoint orbit to \(-\tfrac12\), and the next two steps reach \(1\) and \(-1\); specifically \(F_m^{k+2}(x)=-1\) whenever \(x\in I_m\). The point \(-1\) is fixed with one-sided derivative \(4\), and hence repelling in the usual local stability sense despite the full-measure finite-capture basin. This does not assert Lyapunov attraction of \(-1\). In both parities, the exceptional set of points never hitting the plateau is exactly \(X_m\).

## Verification

The accompanying standalone `verify_markov.py` uses exact fractions to reconstruct every Markov endpoint and adjacency relation for \(1\le m\le22\), checks the stated characteristic polynomials by integer matrix traces, and checks the post-capture orbits. A second, independent direct-cylinder grid enumeration of all branch cylinders for \(1\le m\le6\) and \(1\le n\le4\) reproduces the matrix first-hit lengths in 24 comparisons. The program reports `DYADIC_ALTERNATING_TENT_EXACT_MARKOV_AND_CHARPOLY_OK` and `DIRECT_GRID_CYLINDER_LENGTHS_OK`. Finite checking supplements, but does not replace, the indexed proof above.

## Relationship to prior work

Silva's 2023 construction introduces the flat-top tent family and non-autonomous iteration patterns, and develops classifications of attracting sets; those definitions and the broad attractor mechanism are prior work. The explicit *dyadic all-parameter* survivor matrices, their two parity-dependent Perron polynomials, complete first-hit laws, and sharp logarithmic escape expansion are the asserted additions. General Markov-hole pressure/dimension machinery and small-hole escape asymptotics predate this result, particularly the work of Życzkowski--Bollt, Georgiou--Dettmann--Altmann and Dettmann. The 1998 gap-tent construction removes a central interval at every one-step tent iterate, while the present alternating system removes an interval at every second iterate and has a four-branch return. Those general methods do not themselves supply the two explicit dyadic polynomial families in these coordinates. Silva and Silva's 2025 follow-up focuses on kneading invariants and period-incrementing attractors; its complete text was not available for a full overlap comparison.

## Limitations

The theorem assumes exact real arithmetic and the indicated convention at plateau endpoints; endpoints are negligible for Lebesgue survival and Hausdorff dimension. The result is specific to the fixed alternating pattern and dyadic heights, and does not give the general entropy-versus-height staircase. The named 2025 follow-up could not be inspected beyond its front matter and abstract, and unindexed explicit tables may exist. No independent mathematical audit is claimed.

## References

1. L. Silva, *Attractors in Pattern Iterations of Flat Top Tent Maps*, Mathematics **11** (2023), 2677, doi:10.3390/math11122677; first publicly available 2023-06-13.
2. O. Georgiou, C. P. Dettmann, and E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, Chaos **22** (2012), 043115, doi:10.1063/1.4766723; preprint arXiv:1207.7000.
3. C. P. Dettmann, *Open circle maps: small hole asymptotics*, Nonlinearity **26** (2013), 307–317, doi:10.1088/0951-7715/26/1/307; preprint arXiv:1112.5390.
4. P. Glendinning and N. Sidorov, *The doubling map with asymmetrical holes*, Ergodic Theory and Dynamical Systems **35** (2015); arXiv:1302.2486.
5. L. Silva and T. M. Silva, *Milnor attractors and period incrementing on pattern iterations of flat top tent maps*, Topological Methods in Nonlinear Analysis **65** (2025), 79–97, doi:10.12775/TMNA.2024.023.
6. K. Życzkowski and E. M. Bollt, *On the entropy devil’s staircase in a family of gap-tent maps*, arXiv:chao-dyn/9807013 (1998).
