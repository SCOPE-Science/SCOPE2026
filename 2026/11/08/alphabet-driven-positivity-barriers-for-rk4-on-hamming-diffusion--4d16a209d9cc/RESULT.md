# Alphabet-driven positivity barriers for RK4 on Hamming diffusion networks

## Finding

Let \(H(d,q)\) be the Cartesian product of \(d\) copies of the complete graph \(K_q\), where \(d\ge3\) and \(q\ge3\) are integers. Let \(L\) denote its unweighted combinatorial Laplacian. The classical fourth-order Runge--Kutta diffusion matrix is
\[
P_{d,q}(h)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Write \(\Delta=d(q-1)\), \(p=q-2\), and \(H=2\Delta-3p>0\), and define \(h_3=2/H\).

**Exact positivity classification.** The set of all \(h\ge0\) for which \(P_{d,q}(h)\) is entrywise nonnegative is the single closed interval \([0,h_*]\), where:

* If \(d\ge4\), then \(h_*=h_3\), for every \(q\ge3\).
* If \(d=3\) and \(3\le q\le12\), then \(h_*=h_3=2/(3q)\).
* If \(d=3\) and \(q\ge13\), then \(h_*=h_3\theta_q\), where \(\theta_q\) is the unique root in \((0,1)\) of
\[
(1-t)^3+\frac{4(q+1)}{3q}t(1-t)^2+
\frac{29q^2+24q+12}{27q^2}t^2(1-t)+
\frac{64-5q}{81q}t^3=0.
\]

The obstruction is an entry at Hamming distance three except in the \(d=3,q\ge13\) regime, where an adjacent-vertex entry becomes negative first. Thus exactly \(q=13\) is the first alphabet size that switches the controlling distance, and no such switch occurs in four or more coordinate dimensions. At \(q=12\), \(h_*=1/18\); at \(q=13\), \(h_*=0.0512396000478449\ldots<2/39\).

Every \(P_{d,q}(h)\) is row-stochastic in the algebraic sense (all row sums equal one), but outside the stated interval it is not a nonnegative Markov matrix. The RK4 *spectral stability* interval is strictly larger: its endpoint is \(\alpha/(dq)\), where \(\alpha>0\) solves \(\alpha^3-4\alpha^2+12\alpha-24=0\) (numerically \(\alpha=2.785293563\ldots\)). Since \(dq\,h_*\le2<\alpha\), stability alone never ensures positivity on these networks.

## Assumptions and scope

Coordinates are words in \(\{0,\ldots,q-1\}^d\); two words are adjacent when they differ in exactly one coordinate. Every edge has weight one. The standard linear heat equation is \(u'(t)=-Lu(t)\), and positivity means \(P_{d,q}(h)v\ge0\) for **every** nonnegative initial vector \(v\). The theorem applies to all integers \(d\ge3,q\ge3\) and every real \(h\ge0\), with no prime-power restriction on \(q\). It asserts endpoint, not intermediate-stage, positivity. It excludes \(d=1,2\), weighted edges, other RK methods and non-Cartesian graphs.

## Proof

**1. Exact distance-shell entries.** For fixed vertices at Hamming distance \(k\), the entry \((P_{d,q}(h))_{uv}\) depends only on \(k\). Set \(a_k^{(0)}=\mathbf1_{k=0}\) and use the elementary adjacency-walk recursion
\[
a_k^{(j+1)}=k a_{k-1}^{(j)}+k(q-2)a_k^{(j)}+(d-k)(q-1)a_{k+1}^{(j)},
\]
with out-of-range coefficients zero. This follows by listing a neighbor according to whether a differing coordinate is repaired, changed to a third symbol, or a matching coordinate is altered. Since \(L=\Delta I-A\), the recursion calculates \(L^j\) for every \(0\le j\le4\) exactly. Define
\[
\begin{aligned}
A_3&=q^2-3q+3+3(d-1)(q-1),\\
A_4&=(q-2)(q^2-2q+2)+10(d-1)(q-2)(q-1),\\
B_4&=6(q-2)^2+8(q^2-3q+3)+12(d-2)(q-1).
\end{aligned}
\]
For \(k=1,2,3,4\) the resulting entries are, respectively,
\[
\begin{aligned}
P_1(h)&=h f_1(h),\\
f_1(h)&=1+(-\Delta+p/2)h+
(\Delta^2/2-\Delta p/2+A_3/6)h^2\\
&\quad+(-\Delta^3/6+\Delta^2p/4-\Delta A_3/6+A_4/24)h^3,\\
P_2(h)&=h^2f_2(h),\\
f_2(h)&=1-(\Delta-p)h+(\Delta^2/2-\Delta p+B_4/24)h^2,\\
P_3(h)&=h^3(1-h/h_3),\qquad P_4(h)=h^4.
\end{aligned}
\]
Entries at distance greater than four vanish. In every case \(d\ge3\), distance-three pairs exist, so \(P_3(h)<0\) for \(h>h_3\). This proves the universal upper bound \(h_*\le h_3\).

**2. Diagonal positivity.** The Laplacian is symmetric positive semidefinite. For every \(z\ge0\), the even Taylor polynomial \(r_4(-z)=1-z+z^2/2-z^3/6+z^4/24\) is strictly positive: Taylor's theorem gives \(r_4(-z)=e^{-z}+e^{-\xi}z^5/120\) for some \(\xi\in[0,z]\). Consequently \(P_{d,q}(h)\) is positive definite for all \(h\ge0\), and hence every diagonal entry is positive. Thus it remains to analyze \(f_1,f_2\) on \([0,h_3]\).

**3. Exact Bernstein positivity certificate.** Put \(t=h/h_3\in[0,1]\). For a polynomial \(f(t)\) of degree \(r\), write \(f(t)=\sum_{j=0}^r {r\choose j}b_j t^j(1-t)^{r-j}\). Nonnegative Bernstein coefficients imply nonnegativity on the full interval.

For \(d=3\), the degree-three Bernstein coefficients of \(f_1(h_3t)\) are
\[
1,\quad \frac{4(q+1)}{9q},\quad
\frac{29q^2+24q+12}{81q^2},\quad
\frac{64-5q}{81q}.
\]
The degree-two Bernstein coefficients of \(f_2(h_3t)\) are
\[
1,\quad\frac{q+1}{3q},\quad\frac{16}{27}.
\]
For \(3\le q\le12\) all are positive. For \(q\ge13\) exactly the last coefficient of \(f_1\) is negative, so \(f_1(0)>0\) and \(f_1(h_3)<0\). There is *exactly one* root in \((0,h_3)\): with \(w=t/(1-t)>0\), the equation becomes a cubic with coefficients \(b_0,3b_1,3b_2,b_3\) in ascending powers of \(w\), which has precisely one sign change and hence exactly one positive root by Descartes' rule (existence follows from the endpoint signs). Up to that root all other shell entries are nonnegative, and beyond it until \(h_3\), \(P_1<0\).

For \(d\ge4\), put \(u=q-2\ge1\), \(v=d-4\ge0\), and \(H=(2v+5)u+2v+8\). The four Bernstein coefficients for \(f_1(h_3t)\) are \(1\),
\[
\frac{4(uv+2u+v+4)}{3H},
\]
\[
\frac{18u^2v^2+78u^2v+89u^2+36uv^2+228uv+332u+18v^2+150v+308}{9H^2},
\]
and \(C(u,v)/(3H^3)\), where
\[
\begin{aligned}
C(u,v)={}&u^3(8v^3+48v^2+90v+45)\\
&+u^2(24v^3+192v^2+466v+332)\\
&+u(24v^3+240v^2+760v+740)\\
&+8v^3+96v^2+384v+512.
\end{aligned}
\]
All are strictly positive. The degree-two Bernstein coefficients for \(f_2(h_3t)\) are \(1\), \((uv+2u+v+4)/H\), and
\[
\frac{2(3u^2v^2+15u^2v+20u^2+6uv^2+42uv+68u+3v^2+27v+56)}{3H^2},
\]
again strictly positive. These identities follow by substituting \(h=2t/H\) into the explicit \(f_1,f_2\) and expressing each power-basis polynomial in the Bernstein basis; each is an exact polynomial identity. Therefore all shells are nonnegative for \(0\le h\le h_3\), proving the \(d\ge4\) cases.

Combining all cases gives precisely the claimed single closed interval. No finite-enumeration argument is used to infer any infinite-parameter claim.

**4. Strict gap to spectral stability.** The Laplacian eigenvalues of \(H(d,q)\) are \(jq\), \(0\le j\le d\), by Cartesian-product diagonalization of \(L(K_q)\). Along the negative real axis the RK4 stability polynomial stays in \([-1,1]\) exactly for \(0\le z\le\alpha\); in fact \(r_4(-z)>0\) and \(r_4(-z)\le1\) ends at the stated cubic root. Thus spectral stability holds if and only if \(h\le\alpha/(dq)\). Finally
\[
\frac{dq}{\Delta-\tfrac32(q-2)}\le2
\]
for \(d\ge3,q\ge3\), since \((d-3)(q-2)\ge0\); equality occurs at \(d=3\). Thus \(dq h_*\le dq h_3\le2<\alpha\).

## Verification

Run the included, standard-library-only `verify.py` with Python 3. It independently implements Hamming adjacency-walk recurrences, computes the RK4 polynomial without the Bernstein formulas, checks the exact shell identities and all Bernstein-coefficient identities across \(d=3,\ldots,24\) and several alphabets through \(q=100\), and compares the radial entries to a direct sparse-matrix computation on small graphs. The recorded test returned `VERIFY_OK 6556 exact coefficient/shell/Bernstein checks`. These are reproducibility checks and finite corroboration of the stated symbolic identities; they are not substituted for the all-parameter algebraic proof above.

## Relationship to prior work

Gottlieb--Shu--Tadmor (2001) develop strong-stability-preserving (SSP) time discretization theory and establish important restrictions for higher-order methods; that paper does not provide a \(q\)-ary Hamming-graph endpoint-positivity horizon. Horváth (2005) studies sharp positivity thresholds for general classes of initial-value problems and invariant cones; the inspected complete 16-page text treats no Hamming-graph shell or \(q=13\) switch. Lóczi--Ketcheson (2013) study absolute-monotonicity radii of rational functions, not this fixed graph family. The result is a **graph-specific endpoint positivity** statement and neither asserts universal SSP monotonicity nor contradicts the general theory. Related exact RK4 calculations on regular bipartite networks concern \(q=2\), and triangular graphs concern a different association scheme; neither establishes the nonbinary dimension/alphabet phase diagram here.

## Limitations

No independent mathematical audit or publication-priority certification is claimed. The asserted novelty is conditioned on the inspected literature and research-record comparisons; an unindexed specialist exact formula could still exist. The proof assumes simple unweighted Hamming graphs and the classical RK4 end-step; it does not address intermediate-stage positivity, nonuniform coordinate rates, variable timesteps, nonlinear positivity, or error control. The standalone finite checker confirms identities for selected parameter values but is not a formal symbolic proof checker; the displayed algebraic coefficients are the proof certificate.

## References

1. S. Gottlieb, C.-W. Shu, and E. Tadmor, "Strong stability-preserving high-order time discretization methods," *SIAM Review* 43 (2001), 89--112, electronically published 2001-02-02. DOI: https://doi.org/10.1137/S003614450036757X . Lawful full text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download .
2. Z. Horváth, "On the positivity step size threshold of Runge--Kutta methods," *Applied Numerical Mathematics* 53 (2005), 341--356, available online 2004-10-27. DOI: https://doi.org/10.1016/j.apnum.2004.08.026 .
3. L. Lóczi and D. I. Ketcheson, "Rational functions with maximal radius of absolute monotonicity," preprint posted 2013-03-26, https://arxiv.org/abs/1303.6651 .
