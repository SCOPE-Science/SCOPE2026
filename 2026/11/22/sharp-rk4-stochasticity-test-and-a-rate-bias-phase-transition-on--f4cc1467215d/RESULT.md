# Sharp RK4 stochasticity test and a rate-bias phase transition on directed three-cycles

## Finding

Consider the irreducible three-state one-way continuous-time Markov cycle with positive departure rates \(a,b,c\). For the unmodified classical four-stage, fourth-order Runge–Kutta end-step, **all nine entrywise nonnegativity constraints reduce exactly to just two explicitly computable scalar inequalities**, valid for every timestep and every positive rate triple. The two-jump transitions are strictly positive at every positive step; the possible obstructions are the direct transition between the two largest-rate states and the diagonal of a largest-rate state.

Write \(S=a+b+c\), \(T=ab+bc+ca\), and order the rates \(M\ge u\ge v>0\). Define
\[
F(h)=h-\frac{T h^3}{6}+\frac{STh^4}{24},\qquad
G(h)=\frac{h^2}{2}-\frac{Sh^3}{6}+\frac{(S^2-T)h^4}{24}.
\]
Then, for **every** \(h\ge0\), the RK4 step is row stochastic if and only if
\[
\boxed{F(h)-(M+u)G(h)\ge0,\qquad 1-MF(h)+M^2G(h)\ge0.}\tag{1}
\]
Here “row stochastic” means that the row sums are one and every entry is nonnegative. The two largest rates determine **which entries to test**, not the values of those entries: the coefficients \(F\) and \(G\) depend on all three rates through \(S\) and \(T\). The exact condition is independent of the cyclic ordering of the three departure rates. Formula (1) is a complete test for any specified step, not an assertion about numerical roundoff.

There is a sharp **mechanism-switching transition** on the natural two-equal-rate family \((a,b,c)=(\lambda,\lambda,\lambda r)\), \(\lambda>0\), \(0<r\le1\). Put \(z=\lambda h\) and
\[
E_r(z)=24-24z+12z^2-(4-r)z^3,
\]
\[
D_r(z)=24-24z+12z^2+4(r-1)z^3+(1-3r-r^2)z^4.
\]
Each \(E_r\) has a unique positive root \(e(r)\). The polynomial
\[
P(r)=8r^6+48r^5+93r^4-24r^3-84r^2+48r-8
\]
has exactly one root \(r_*\) in \((0,1)\), with
\[
r_*=0.542437577761975\ldots,\qquad e(r_*)=1.765840714010906\ldots.
\]
For \(r>r_*\), \(D_r\) has a unique positive zero \(d(r)\); the endpoint step is stochastic **exactly** on
\[
\boxed{0\le z\le H(r),\quad H(r)=
\begin{cases}
e(r),&0<r\le r_*,\\
d(r),&r_*\le r\le1.
\end{cases}}\tag{2}
\]
The two formulas agree at \(r_*\). Below \(r_*\) the direct transition between the two fast-rate states becomes negative first; above \(r_*\) a fast-state diagonal becomes negative first. At \(r=1\), the diagonal-root value recovers the published equal-rate cutoff \(1.4933773767\ldots\). There is no positivity recovery after the stated cutoff in this family.

## Assumptions and scope

The generator is the row matrix
\[
Q=\begin{pmatrix}-a&a&0\\0&-b&b\\c&0&-c\end{pmatrix},\qquad a,b,c>0.
\]
The completed RK4 matrix is \(R(h)=I+hQ+(hQ)^2/2+(hQ)^3/6+(hQ)^4/24\). State distributions multiply it from the left. All claims concern one completed step on a time-homogeneous linear system, not nonnegative intermediate RK stages. Rescaling all rates by \(\lambda\) rescales the admissible physical timestep inversely. Formula (1) holds without imposing \(a=b\) or any other relation; the complete sharp interval theorem (2) is specifically for the two-equal-rate family with the third rate no larger.

## Proof

**1. Three-state characteristic reduction.** Direct expansion gives \(Q(Q^2+SQ+TI)=0\). Consequently \(Q^3=-SQ^2-TQ\) and \(Q^4=(S^2-T)Q^2+STQ\). Substitution yields exactly \(R(h)=I+F(h)Q+G(h)Q^2\) with the coefficients displayed above.

**2. Two-jump signs and a reduction from nine constraints to two.** For \(h>0\),
\[
G(h)=\frac{h^2}{24}\bigl[12-4Sh+(S^2-T)h^2\bigr]>0.
\]
Indeed \(S^2-T>0\), and the bracket has discriminant \(16(3T-2S^2)=-16[2(a^2+b^2+c^2)+T]<0\). In a cyclic row of departure rate \(x\), let the next state's rate be \(y\). The row entries are
\[
R_{i,i}=1-xF+x^2G,\quad R_{i,i+1}=x[F-(x+y)G],\quad R_{i,i+2}=xyG,
\]
where indices are modulo three. Thus all two-jump entries are strictly positive. Since the adjacent unordered rate pairs are \((M,u)\), \((u,v)\), \((v,M)\), and \(G>0\), all direct entries are nonnegative if and only if \(F-(M+u)G\ge0\). Under that inequality, for any other rate \(x\le M\),
\[
(1-xF+x^2G)-(1-MF+M^2G)=(M-x)[F-(M+x)G]\ge0.
\]
Hence the smallest diagonal is the largest-rate diagonal. At \(h=0\), \(R(0)=I\) and (1) remains true. The row-sum identity follows from \(Q\mathbf1=0\). This proves the full equivalence (1), also showing that permuting rates does not alter entrywise stochasticity.

**3. Unique direct-edge cutoff in the symmetric-rate subfamily.** Put \(a=b=1\), \(c=r\) by scaling. Algebra gives \(24[F(z)-2G(z)]/z=E_r(z)\) for \(z>0\), and \(24[1-F(z)+G(z)]=D_r(z)\). Now
\[
E_r'(z)=-24+24z-3(4-r)z^2<0
\]
for all real \(z\), because its discriminant is \(576-288(4-r)<0\) for \(0<r\le1\). Since \(E_r(0)=24\) and its leading coefficient is negative, \(E_r\) has exactly one positive root \(e(r)\), with \(e(0)=1.5960716379\ldots\) and \(e(1)=2\). Moreover \(\partial E_r/\partial r=z^3>0\) at positive \(z\), so \(e(r)\) is strictly increasing.

**4. Unique meeting parameter.** Eliminating \(z\) from the simultaneous equations \(E_r(z)=D_r(z)=0\) gives the exact resultant
\[
\operatorname{Res}_z(E_r,D_r)=-41472P(r).
\]
To show \(P\) has exactly one root on \((0,1)\), express \(P(z/2)\) in the degree-six Bernstein basis on \([0,1]\). Its coefficients in increasing order are
\[
-8,\ -4,\ -7/5,\ -7/20,\ -49/80,\ -21/16,\ -9/16,
\]
so \(P<0\) throughout \([0,1/2]\). Similarly, the degree-five Bernstein coefficients of \(P'((1+z)/2)\) are
\[
9,\ 132/5,\ 1329/20,\ 1413/10,\ 1338/5,\ 468,
\]
so \(P'>0\) on \([1/2,1]\). Since \(P(1)=81>0\), it has precisely one root \(r_*\in(1/2,1)\).

The continuous function \(D_r(e(r))\) is positive at \(r=0\), because \(D_0(z)=24\sum_{j=0}^4(-z)^j/j!>0\) for \(z>0\) by the alternating exponential Taylor remainder. At \(r=1\), it equals \(D_1(2)=-24<0\). Thus it must vanish for some \(r\in(0,1)\). Every such point zeros the resultant; the uniqueness of the root of \(P\) forces this point to be exactly \(r_*\), and hence also proves the asserted strict signs on either side.

**5. Proving the entire interval classification.** For \(r\in[1/2,1]\), \(D_r'(z)<0\) at every \(z\ge0\). For \(0<z\le1\), this follows from
\[
D_r'(z)/24=-1+z-\frac{1-r}{2}z^2+\frac{1-3r-r^2}{6}z^3<0.
\]
For \(z\ge1\), the last expression is decreasing in \(r\ge1/2\), because its derivative with respect to \(r\) equals \(z^2[3-(3+2r)z]/6<0\). At \(r=1/2\) it equals \(-(z-2)^2/4-z^3/8<0\). Thus \(D_{r_*}\) is strictly decreasing and has its unique zero at \(e(r_*)\). For \(r\ge r_*\), \(D_r\) is also strictly decreasing, and since \(D_r(e(r))\le0\), its unique positive zero \(d(r)\) occurs at or before \(e(r)\).

For \(0<r<r_*\), the polynomial \(D_r(z)\) is strictly concave in \(r\) for any fixed \(z>0\), because \(\partial^2D_r/\partial r^2=-2z^4\). Thus for \(0\le z\le e(r)\le e(r_*)\),
\[
D_r(z)\ge(1-r/r_*)D_0(z)+(r/r_*)D_{r_*}(z)>0.
\]
Here \(D_0(z)>0\) for every \(z\ge0\), while \(D_{r_*}(z)\ge0\) up to \(e(r_*)\). For \(z>e(r)\), \(E_r(z)<0\) and hence a direct edge is negative. In the other regime \(r\ge r_*\), the fast-state diagonal is negative for \(z>d(r)\). These facts establish all endpoints, absence of reentry and the two obstruction mechanisms in (2).

## Verification

A self-contained SymPy-based Python verifier is supplied as `verify.py`. It independently constructs \(Q\) and the four matrix powers with exact rational arithmetic for \(6^3\) distinct positive rate triples and eight steps each (1,728 cases), and checks the rank-two reduction, exact row sums, every individual entry and equivalence (1). It also checks 30 supplementary cases of the two-equal-rate family, the exact resultant, both Bernstein coefficient certificates, and the numerical bracket for the unique crossover root. Run `python3 verify.py` with Python 3 and SymPy installed. The recorded output is in `verify_output.txt`. The computations are finite cross-checks; universal quantifiers follow from the polynomial proof above.

## Relationship to prior work

Nüßlein, Ranocha and Ketcheson (2020, arXiv:2005.06268) study modifying Runge–Kutta weights to enforce positivity, whereas (1)–(2) concern the *unmodified* classical RK4 end-step. Blanes, Iserles and Macnamara (first public preprint 2021-02-16; arXiv:2102.08242) develop positivity-preserving methods for graph-Laplacian ODEs but do not give this rate-bias phase classification. Horváth, Song and Terlaky (2014) provide general polynomial-root methods to obtain valid invariant-set step bounds, rather than the exact two-test reduction, the nonreentrant rate-one-parameter classification, or the algebraic mechanism switch.

The indexed statements in references 4 and 5 classify (i) the equal-rate directed three-cycle RK4 cutoff, and (ii) heterogeneous directed one-way cycles with at least five vertices. Those stated scopes do not include the unequal-rate three-cycle: in three states, three or four forward jumps can wrap around the cycle, unlike in cycles with at least five vertices. The known equal-rate answer is recovered at \(r=1\) and is not claimed as new. No blanket novelty or historical-priority guarantee is asserted.

## Limitations

The exact full-rate formula is a pair of polynomial inequalities; the explicit interval and algebraic phase change are established only when the two largest rates are equal. This is a final-step entrywise positivity result, not positivity of internal RK stages, and not a guarantee about nonlinear or time-dependent problems. It does not imply every nonnegative step forms an accurate approximation.

## References

1. S. Nüßlein, H. Ranocha and D. I. Ketcheson, *Positivity-Preserving Adaptive Runge–Kutta Methods*, arXiv:2005.06268, first posted 2020-05-13. https://arxiv.org/abs/2005.06268
2. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242, first posted 2021-02-16; ESAIM: M2AN 56 (2022), 1843–1870. https://arxiv.org/abs/2102.08242
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755, 2014. https://arxiv.org/abs/1406.6755
4. *Sharp cycle-length positivity frontiers for fourth-order Runge–Kutta*, published mathematical research record, 2026-11-02. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-cycle-length-positivity-frontiers-for-fourth-order-runge-k--6cbc274839ff
5. *Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain*, published mathematical research record, 2026-11-08. https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-rk4-positivity-on-heterogeneous-directed-cycles-and-a-shar--36d0a038ee0c
