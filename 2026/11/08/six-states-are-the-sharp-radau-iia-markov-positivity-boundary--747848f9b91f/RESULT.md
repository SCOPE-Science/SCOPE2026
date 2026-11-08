# Six states are the sharp Radau IIA Markov positivity boundary

## Finding

Let \(Q\in\mathbb R^{n\times n}\) be any finite continuous-time Markov-chain generator in the **row convention**: \(q_{ij}\ge0\) when \(i\ne j\), and \(Q\mathbf1=0\). For \(h\ge0\), define the completed two-stage, third-order Radau IIA transition approximation
\[
\mathcal R_h(Q)=r(hQ),\qquad r(z)=\frac{6+2z}{z^2-4z+6}.
\]
Then the following are proved.

**Sharp minimum dimension.** If \(1\le n\le5\), every such \(Q\) admits \(\varepsilon_Q>0\) such that \(\mathcal R_h(Q)\) is entrywise nonnegative (and hence stochastic) for \(0\le h\le\varepsilon_Q\). The bound is sharp: a six-state unit-rate pure-birth generator has a negative entry for **every** sufficiently small positive \(h\). The property is local in \(h\) for each fixed \(Q\), and there is no assertion of a uniform \(\varepsilon\) over generators with unbounded rates.

**Exact six-state stochasticity set.** Let \(Q_*\) have \((Q_*)_{i,i}=-1\) and \((Q_*)_{i,i+1}=1\) for \(i=0,1,2,3,4\), all other entries zero; state \(5\) is absorbing. Let \(\alpha\) be the unique positive zero of
\[
P(h)=h^5+30h^4+180h^3+360h^2+180h-72.
\]
Then \(1/4<\alpha<13/50\), with \(\alpha\approx0.253946561637298\), and
\[
\boxed{\mathcal R_h(Q_*)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad h=0\ \text{or}\ \alpha\le h\le3.}
\]
For \(0<h<\alpha\) the transition from state \(0\) to state \(5\) is negative, and for \(h>3\) every transient diagonal is negative. For a common positive birth rate \(\lambda\), the same classification holds with \(h\) replaced by \(\lambda h\).

## Assumptions and scope

Only exact arithmetic and the **end-step** rational stability map are considered, not floating-point rounding, positivity of internal stages, general nonlinear problems, or other time integrators. There is no restriction of reversibility or graph connectivity on \(Q\). The rational map is defined for all \(h\ge0\): the zeros of \(z^2-4z+6\) are \(2\pm i\sqrt2\), strictly in the right half-plane, whereas CTMC-generator eigenvalues have nonpositive real part. Because \(r(0)=1\), all \(\mathcal R_h(Q)\) have row sums exactly one.

## Proof

**1. Positivity in at most five states.** Direct division of the defining rational function gives
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{36}-\frac{z^5}{108}+O(z^6).
\]
Write its Taylor coefficients as \(a_j\); thus \(a_j>0\) for \(0\le j\le4\), but \(a_5<0\). For distinct states \(i,j\), if no positive-rate directed walk connects them then \((Q^k)_{ij}=0\) for all integers \(k\ge0\), so \((r(hQ))_{ij}=0\). Otherwise let \(d\) be the length of a shortest such directed walk. It is simple, hence \(1\le d\le n-1\). All terms contributing to \((Q^k)_{ij}\) with \(k<d\) vanish; and \((Q^d)_{ij}>0\), since a length-\(d\) contributing product cannot contain a diagonal stay and all shortest positive-rate walks contribute positively. Therefore
\[
(r(hQ))_{ij}=a_d h^d(Q^d)_{ij}+O(h^{d+1})>0
\]
for all sufficiently small \(h>0\) if \(n\le5\). Diagonal entries are \(1+O(h)>0\). There are finitely many entries, so a common \(\varepsilon_Q\) exists. This does not claim a lower bound on \(\varepsilon_Q\) depending on dimension alone.

**2. Exact entries on the six-state chain.** Put \(D(h)=h^2+4h+6\). The transient \(5\times5\) block of \(-Q_*\) is \(I-N\), where \(N\) has ones on its superdiagonal and \(N^5=0\). Taylor's formula for a rational function of a Jordan block gives, for \(0\le i\le j\le4\),
\[
(\mathcal R_h(Q_*))_{i,j}=c_{j-i}(h),\qquad c_d(h)=\frac{(-h)^d}{d!}\left(\frac{\mathrm d}{\mathrm dh}\right)^d\left(\frac{6-2h}{D(h)}\right)
\quad(0\le d\le4).
\]
Elementary differentiation yields
\[
\begin{aligned}
c_0&=\frac{2(3-h)}D,\\
c_1&=\frac{2h(18+6h-h^2)}{D^2},\\
c_2&=\frac{2h^2(h+3)(18+12h-h^2)}{D^3},\\
c_3&=\frac{2h^3(108+216h+108h^2+12h^3-h^4)}{D^4},\\
c_4&=\frac{2h^4(108+540h+540h^2+180h^3+15h^4-h^5)}{D^5}.
\end{aligned}
\]
These are strictly positive for \(0<h<3\), and at \(h=3\) they are nonnegative (only \(c_0\) vanishes). For \(d=1,2\), the positive factors are evident on \((0,3]\). For \(d=3,4\), the only negative monomial combines respectively as \(h^3(12-h)>0\) and \(h^4(15-h)>0\) on that interval.

Since \(\mathcal R_h(Q_*)\mathbf1=\mathbf1\), the absorbing-column probability in row \(i\) is \(b_{5-i}(h)=1-\sum_{d=0}^{4-i}c_d(h)\). Direct rational simplification gives
\[
\begin{aligned}
b_1&=\frac{h(h+6)}D,\\
b_2&=\frac{h^2(h^2+12h+18)}{D^2},\\
b_3&=\frac{h^3(h^3+18h^2+54h+36)}{D^3},\\
b_4&=\frac{h^4(h^4+24h^3+108h^2+144h+36)}{D^4},\\
b_5&=\frac{h^5P(h)}{D^5}.
\end{aligned}
\]
Thus \(b_1,b_2,b_3,b_4>0\) for all \(h>0\). The only possible obstruction for \(0<h\le3\) is \(b_5\).

**3. Exact boundaries.** \(P(0)=-72\), and
\[
P'(h)=5h^4+120h^3+540h^2+720h+180>0\qquad(h>0).
\]
Moreover \(P(1/4)=-1607/1024<0\) and \(P(13/50)=761862793/312500000>0\); consequently \(P\) has exactly one positive root \(\alpha\) in that rational interval. For \(0<h<\alpha\), the entry \((\mathcal R_h(Q_*))_{0,5}=b_5(h)<0\). For \(\alpha\le h\le3\), all transient-block entries and absorbing-column entries are nonnegative; the absorbing state contributes only the unit diagonal. If \(h>3\), then \(c_0(h)=2(3-h)/D(h)<0\). At \(h=0\) the map is the identity. This proves both the complete stochasticity set and the sharp six-state obstruction.

## Verification

The accompanying dependency-free `artifacts/verify_radau_markov.py` independently computes \((6I+2hQ_*)(6I-4hQ_*+h^2Q_*^2)^{-1}\) using exact fractions. Its extracted execution checked 504 entry equalities across 14 rational timesteps, 14 exact row sums, the first six Maclaurin coefficients, root-bracketing signs, and four sign witnesses; output: `VERIFY_OK`. These finite tests corroborate explicit identities, but the universal five-state result and exact interval are established by the algebraic arguments above, not extrapolation from tests.

## Relationship to prior work

Brugnano, Iavernaro and Magherini (first public arXiv version, 2013-02-05) study Radau IIA collocation and its implementations, without a CTMC dimension cutoff. Zappavigna, Colaneri, Kirkland and Shorten (public repository deposit 2012-06-19) demonstrate loss of positivity under **diagonal** Padé approximations for positive Metzler systems, including a nilpotent shift and a Hurwitz perturbation; their paper does not impose row-sum-zero conservation on the witness or evaluate the subdiagonal \([1/2]\) Radau map. Lóczi and Ketcheson (2013) study absolute-monotonicity radii of rational stability functions; a zero universal radius does not determine the smallest conservative finite-state dimension or the exact re-entrant stochasticity interval. Bonaventura and Della Rocca (2015) analyze positivity for TR-BDF2 rather than the Radau IIA map.

A published result on the fourth-order two-stage Gauss–Legendre \([2/2]\) Padé map establishes a **different**, eight-state minimal conservative dimension and an explicit stochasticity window. It supplies an important methodological analogue but does not imply the present six-state \([1/2]\) numerical values or window. The present calculation uses the first wrong-signed Taylor coefficient at degree five instead of the vanishing degree-six coefficient and wrong-signed degree-seven term of \([2/2]\).

## Limitations

No claim of a uniform positivity radius for all generators with fixed dimension, nor of unconditional positivity on six-state chains, nor of a result for arbitrary \(n>6\) or nonlinear systems. The present finding is about **end-step** stochasticity, not stagewise preservation. Publication-priority uncertainty remains for unindexed literature on subdiagonal Padé methods and conservative Markov generators; the inspected sources do not provide exhaustive coverage of all past mathematical work. It does not claim an independent audit.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra Appl. 436 (2012), 3425–3442. Lawful open preprint: https://mural.maynoothuniversity.ie/id/eprint/3761/ (public deposit 2012-06-19); https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf.
2. L. Brugnano, F. Iavernaro, C. Magherini, *Efficient implementation of Radau collocation methods*, arXiv:1302.1037 (2013-02-05). https://arxiv.org/abs/1302.1037.
3. L. Lóczi, D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651 (2013-03-26); LMS J. Comput. Math. 17 (2014), 159–205. https://arxiv.org/abs/1303.6651.
4. L. Bonaventura, A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303 (2015-10-14). https://arxiv.org/abs/1510.04303.
5. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, public mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
