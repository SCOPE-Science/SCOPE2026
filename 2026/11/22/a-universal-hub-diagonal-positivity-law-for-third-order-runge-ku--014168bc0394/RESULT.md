# A universal hub-diagonal positivity law for third-order Runge–Kutta on weighted stars

## Finding
Let a finite star have a center indexed \(0\), \(m\ge2\) leaves indexed \(1,\ldots,m\), and strictly positive spoke conductances \(a_1,\ldots,a_m\). Its symmetric continuous-time Markov generator \(Q\) has \(Q_{0i}=Q_{i0}=a_i\), \(Q_{00}=-S\), \(Q_{ii}=-a_i\), other entries zero, where \(S=\sum_i a_i\). Set \(T_2=\sum_i a_i^2\) and \(T_3=\sum_i a_i^3\). For the classical third-order three-stage Runge–Kutta stability polynomial,
\[
P(h)=I+hQ+\frac{h^2}{2}Q^2+\frac{h^3}{6}Q^3,
\]
define the center-diagonal cubic
\[
C(h)=1-Sh+\frac{S^2+T_2}{2}h^2-\frac{S^3+2ST_2+T_3}{6}h^3.
\]
**Theorem.** The cubic \(C\) has exactly one positive root \(H\), and \(P(h)\) is entrywise nonnegative **if and only if** \(0\le h\le H\). At \(h=H\), the center diagonal vanishes, while every other entry is strictly positive. No later nonnegative interval exists. Put \(t=SH\). If \(\alpha\) is the positive root of \(1-t+t^2-2t^3/3\) and \(\beta\) the positive root of \(1-t+t^2/2-t^3/6\), then
\[
1<\alpha=1.2563726633\ldots <t<\beta=1.5960716380\ldots.
\]
Both constants are sharp over the class of all finite weighted stars: \(t\to\alpha\) as one positive conductance takes asymptotically all weight, and \(t\to\beta\) along unweighted stars with increasing numbers of leaves. In particular the exact permissible completed step always exceeds the forward-Euler/SSP sufficient limit \(1/S\) by a factor greater than \(\alpha\).

## Assumptions and scope
All weights are finite and strictly positive. There are at least two leaves; zero conductances and arbitrary nonstar graphs are excluded. The statement concerns the **completed** three-stage third-order polynomial, not positivity of intermediate stage vectors, exact semigroup positivity, or a uniform guarantee for all Markov generators of prescribed exit rate. Every row sum of \(P(h)\) is one for all real \(h\), because \(Q\mathbf 1=0\); nonnegative entries therefore imply stochasticity.

## Proof
Write \(x=a_i\), \(S=\sum_k a_k\) and \(T_j=\sum_k a_k^j\). Exact multiplication gives, for every leaf \(i\) and distinct leaves \(i,j\),
\[
\begin{aligned}
P_{00}(h)&=C(h),\\
P_{ii}(h)&=1-xh+x^2h^2-\frac{x^2(S+3x)}6h^3=:L_i(h),\\
P_{0i}(h)&=P_{i0}(h)=xh\left[1-\frac{S+x}{2}h+\frac{S^2+T_2+Sx+x^2}{6}h^2\right],\\
P_{ij}(h)&=\frac{a_i a_j h^2}{6}\left[3-(S+a_i+a_j)h\right].
\end{aligned}
\]

**1. Unique center crossing.** We have \(C(0)=1\), \(C(h)\to-\infty\) as \(h\to+\infty\), and
\[
C'(h)=-S+(S^2+T_2)h-\frac{S^3+2ST_2+T_3}{2}h^2.
\]
The discriminant of the quadratic in the derivative is
\[
(S^2+T_2)^2-2S(S^3+2ST_2+T_3)
=-S^4-2S^2T_2+T_2^2-2ST_3<0,
\]
using \(0<T_2\le S^2\). Its leading coefficient and value at zero are negative, hence \(C'(h)<0\) for all real \(h\). There is one positive root \(H\), and \(C(h)<0\) for all \(h>H\).

**2. Center-to-leaf entries are always positive.** For \(h>0\) the bracket in \(P_{0i}\) is a quadratic with positive leading coefficient and discriminant
\[
\frac{(S+x)^2}{4}-\frac{2}{3}(S^2+T_2+Sx+x^2)
=-\frac{5S^2+2Sx+5x^2+8T_2}{12}<0.
\]
Therefore \(P_{0i}=P_{i0}>0\) for all positive \(h\).

**3. Every leaf diagonal strictly dominates the center diagonal.** Fix \(i\) and write \(B=\sum_{k\ne i}a_k>0\), \(U_2=\sum_{k\ne i}a_k^2\), \(U_3=\sum_{k\ne i}a_k^3\), and \(x=a_i\). Expansion yields
\[
L_i(h)-C(h)=\frac h6\left[6B-3(B(S+x)+U_2)h+A h^2\right],
\]
where
\[
A=B^3+3B^2x+2BU_2+4Bx^2+2U_2x+U_3>0.
\]
Put \(r=x/B\), \(z=U_2/B^2\), \(v=U_3/B^3\), so \(r>0\), \(0<z\le1\), \(v>0\). The negative of the bracket's quadratic discriminant equals
\[
24BA-9(B(S+x)+U_2)^2
=3B^4\left[5+12r+10z+20r^2+4rz-3z^2+8v\right]>0.
\]
Indeed \(10z-3z^2>0\) for \(0<z\le1\). With positive leading coefficient and strictly negative discriminant, the bracket is positive for all real \(h\). Hence \(L_i(h)>C(h)\) whenever \(h>0\), including at \(h=H\).

**4. Every leaf-to-leaf entry remains positive through the center crossing.** Fix distinct leaves with weights \(x,y>0\). Set \(B=\sum_{k\notin\{i,j\}}a_k\ge0\), \(U_2=\sum_{k\notin\{i,j\}}a_k^2\), \(U_3=\sum_{k\notin\{i,j\}}a_k^3\), and \(T=S+x+y=2x+2y+B\). At the leaf-to-leaf cutoff \(h_0=3/T\), direct expansion gives
\[
\begin{aligned}
-2T^3 C(h_0)={}&8x^3+8y^3-3x^2y-3xy^2\\
&+B(15x^2+12xy+15y^2)+9B^2(x+y)+4B^3+9BU_2+9U_3.
\end{aligned}
\]
The first four terms sum to \((x+y)[8(x+y)^2-27xy]>0\), since \(xy\le(x+y)^2/4\). All remaining terms are nonnegative. Therefore \(C(h_0)<0\), so \(H<h_0\). Thus \(P_{ij}(h)>0\) throughout \(0<h\le H\).

Combining the four steps proves every entry of \(P(h)\) is nonnegative for \(0\le h\le H\), with only the center diagonal zero at the positive endpoint. For \(h>H\), its center diagonal is negative, proving necessity, maximality and nonreentry.

**5. Sharp comparison with the forward-Euler threshold.** Normalize \(p_i=a_i/S\), \(r_2=\sum_i p_i^2\), \(r_3=\sum_i p_i^3\), and \(t=Sh\). Then
\[
C(t/S)=1-t+\frac{1+r_2}{2}t^2-\frac{1+2r_2+r_3}{6}t^3
=R(-t)+\frac{t^2}{6}[(3-2t)r_2-tr_3],
\]
with \(R(-t)=1-t+t^2/2-t^3/6\). At \(t=\beta>3/2\), the bracket is negative, so \(SH<\beta\). The one-spoke limiting cubic is \(C_1(t)=1-t+t^2-2t^3/3\). At its positive zero \(\alpha\in(1,3/2)\), because \(r_3\le r_2<1\),
\[
C(\alpha/S)-C_1(\alpha)
=\frac{\alpha^2}{6}[(3-2\alpha)(r_2-1)+\alpha(1-r_3)]
\ge\frac{\alpha^2}{2}(\alpha-1)(1-r_2)>0.
\]
Thus \(SH>\alpha\). Letting one weight dominate gives \(r_2,r_3\to1\) and the lower sharp limit, whereas equal weights on \(m\) leaves give \(r_2=1/m\), \(r_3=1/m^2\), yielding the upper sharp limit as \(m\to\infty\).

## Verification
`verify.py` is a standalone Python 3 script using exact rational arithmetic. It constructs \(Q\), multiplies it to obtain \(Q^2,Q^3\), reconstructs every matrix entry independently, and compares them to the displayed identities. The script also checks row sums, all center-to-leaf entry signs at positive rational test steps, and the strict leaf-versus-center diagonal inequality on many weighted stars. It passed 346,283 exact entry/row assertion groups. This finite testing does not establish the infinite-parameter assertions: Steps 1–5 give the proof.

Reproduce from this directory with `python verify.py`. The decimal constants can be independently obtained by solving the two displayed scalar cubics; the theorem is stated using their exact algebraic definitions, not their decimal approximations.

## Relationship to prior work
Gottlieb, Shu and Tadmor (2001), in their full paper, establish a general SSP/forward-Euler sufficient step-size principle; their conditions do not give the necessary-and-sufficient fixed-generator threshold for arbitrary heterogeneous weighted stars. Horváth (2005), inspected in its 16-page full text, treats positivity thresholds over classes of IVPs and invariant cones; that is distinct from the explicit all-initial-data threshold \(H\) for each fixed weighted-star generator, along with the identity of the first failing matrix entry and the sharp normalized interval. Related archived analyses of different implicit or fourth-order schemes on stars and of Taylor schemes on **unweighted** multipartite graphs were searched and compared; no inspected statement yields the arbitrary-positive-weight degree-three criterion. In particular, one cannot transfer a fourth-order or a rational stability function's entrywise-sign frontier to the cubic stability polynomial without further argument.

## Limitations
This result concerns symmetric, nonnegatively weighted stars and the third-order Taylor/RK completed endpoint only. It neither asserts stagewise positivity for steps above the Euler limit nor extends to directed stars, other graphs or modified/adaptive RK coefficients. An index and literature search cannot certify global priority; potentially unindexed equivalent historical formulas remain a risk, especially in the broad fixed-matrix positivity literature. Full text of some related archived repository records was unavailable, so comparisons to those records rely on their published claim summaries, not imagined full-text inspections. A separate independent audit has not been performed.

## References
1. Sigal Gottlieb, Chi-Wang Shu and Eitan Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112, doi:10.1137/S003614450036757X; published electronically 2001-02-02. Author-hosted full text: https://math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. Zoltán Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, doi:10.1016/j.apnum.2004.08.026; first available online 2004-10-27.
3. Relevant published comparative records include *An exact one-edge positivity horizon for fourth-order Runge–Kutta on bidirected stars* (2026-10-25), and *Parity law for Taylor heat positivity on complete multipartite graphs* (2026-11-08). Both concern different stability-polynomial/order or graph-weight hypotheses and have been compared at the claim level only.
