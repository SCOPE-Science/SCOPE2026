# A limiting hitting-time law for the Fibonacci rank map on five-smooth integers

## Finding

Write \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). The **Fibonacci order-of-appearance map** is
\[
z(n)=\min\{j\ge1:n\mid F_j\},\qquad n\ge1.
\]
Define its first fixed-point hitting time by
\[
H(n)=\min\{k\ge0:z^{k+1}(n)=z^k(n)\}.
\]
A positive integer is **five-smooth** if all its prime factors belong to \(\{2,3,5\}\); this includes \(1\).

**Theorem (exact smooth-core dynamics and a limiting law).** Let \(a,b,c\ge0\) be integers. Then \(H(2^a3^b5^c)=h(a,b)\), independently of \(c\), where
\[
h(a,b)=\begin{cases}
0 &(a,b)=(0,0),\\
3 &a=0,\ b=1,\\
b-1 &a=0,\ b\ge2,\\
4 &(a,b)=(1,0),\\
2 &b=0,\ a\in\{2,3\},\\
\lceil(a-2)/2\rceil &b=0,\ a\ge4,\\
\max\{\lceil(a-2)/2\rceil,b-1,\mathbf{1}_{a=1}\} &a,b\ge1.
\end{cases}
\]
The eventual fixed point is \(5^c\) if \(a=b=0\), and \(12\cdot5^c\) otherwise.

For \(X>1\), choose \(N_X\) uniformly from the five-smooth positive integers not exceeding \(X\). Put
\[
A=2\log2,\qquad B=\log3,\qquad x_+=\max\{x,0\}.
\]
Uniformly for all real \(t\ge0\),
\[
\mathbb P\!\left(\frac{H(N_X)}{\log X}\le t\right)
=G(t)+O\!\left(\frac1{\log X}\right),
\quad G(t)=1-(1-At)_+^3-(1-Bt)_+^3+(1-(A+B)t)_+^3.
\]
Consequently the normalized hitting time has a continuous, nondegenerate compactly supported limit distribution, whose support is exactly
\[
[0,1/B]=[0,1/\log3],
\]
and
\[
\mathbb E H(N_X)=\left(\frac1{4A}+\frac1{4B}-\frac1{4(A+B)}\right)\log X+O(1).
\]
The coefficient is approximately \(0.3072892856723686\).

## Assumptions and scope

The ranks \(z(n)\) are defined for all positive integers, but the exact time formula and probability law here **only** concern integers with prime support contained in \(\{2,3,5\}\). They are not claims about uniformly random integers in \([1,X]\). All logarithms are natural; the probability measure on the finite five-smooth set is uniform, not logarithmically weighted. The error constants are absolute, and the displayed uniform bound is intended as \(X\to\infty\).

## Proof

**1. Exact exponent dynamics.** The classical Fibonacci rank identities (recalled in the reference preprint, Lemmas 2.2–2.3) are
\[
\begin{aligned}
&z(1)=1,\ z(2)=3,\ z(4)=6,\quad z(2^a)=3\cdot 2^{a-2}\quad(a\ge3),\\
&z(3^b)=4\cdot3^{b-1}\quad(b\ge1),\qquad z(5^c)=5^c\quad(c\ge0),\\
&z(uv)=\operatorname{lcm}(z(u),z(v))\quad\text{when }\gcd(u,v)=1.
\end{aligned}
\]
These identities give \(z(2^a3^b5^c)=2^{a'}3^{b'}5^c\), with
\[
\begin{gathered}
 u(0)=u(1)=0,\quad u(2)=1,\quad u(a)=a-2\ (a\ge3),\\
 a'=\max\{u(a),2\mathbf1_{b>0}\},\qquad
 b'=\max\{\mathbf1_{a>0},b-1,0\}.
\end{gathered}
\]
The exponent \(c\) is preserved exactly, and the only fixed exponent pairs are \((0,0)\) and \((2,1)\). In the latter case the fixed integer is \(12\cdot5^c\).

**2. First hitting times, including exceptional boundaries.** The quadrant \(a\ge2,b\ge1\) is invariant, with the decoupled transition
\[
(a,b)\longmapsto(\max\{a-2,2\},\max\{b-1,1\}).
\]
The exact number of steps to \((2,1)\) from this quadrant is
\[
\max\{\lceil(a-2)/2\rceil,b-1\}.
\]
When \(a=1,b\ge1\), one preliminary step enters that quadrant at \((2,\max\{b-1,1\})\), giving \(\max\{1,b-1\}\) steps overall. When \(a=0,b\ge2\), the first step reaches \((2,b-1)\), giving \(b-1\) steps in total; \((0,1)\) follows the three-step path \((0,1)\to(2,0)\to(1,1)\to(2,1)\). The three small cases \((1,0),(2,0),(3,0)\) require respectively \(4,2,2\) steps. For \(a\ge4,b=0\) one step enters \((a-2,1)\), and the total is \(\lceil(a-2)/2\rceil\). Thus all stated cases are exhaustive, and
\[
\left|h(a,b)-\max\{a/2,b\}\right|\le4
\]
for every \(a,b\ge0\).

**3. Uniform lattice-simplex count.** Write \(L=\log X\), and \(\alpha=\log2\), \(\beta=\log3\), \(\gamma=\log5\). The five-smooth integers up to \(X\) correspond one-to-one to the integer points
\[
(a,b,c)\in\mathbb Z_{\ge0}^3,\qquad \alpha a+\beta b+\gamma c\le L.
\]
The standard unit-cube comparison for a three-dimensional orthant simplex gives, uniformly for \(y\ge0\),
\[
Q(y)=\#\{(a,b,c)\ge0:\alpha a+\beta b+\gamma c\le y\}
=\frac{y^3}{6\alpha\beta\gamma}+O((y+1)^2).
\]
In particular \(Q(L)=L^3/(6\alpha\beta\gamma)+O(L^2)\).

For \(t\ge0\), let \(K=\lfloor2tL\rfloor\) and \(J=\lfloor tL\rfloor\). The count satisfying both \(a\le K\) and \(b\le J\) is exactly, by inclusion–exclusion,
\[
Q(L)-Q(L-\alpha(K+1))-Q(L-\beta(J+1))
+Q(L-\alpha(K+1)-\beta(J+1)),
\]
where \(Q(y)=0\) for \(y<0\). In the displayed asymptotic one may replace each shifted budget by \(L(1-2\alpha t)\), \(L(1-\beta t)\), or \(L(1-(2\alpha+\beta)t)\), respectively, at a uniform error \(O((L+1)^2)\). The estimates are valid even when a shifted budget changes sign, by using the positive part.

By the bound in Step 2, the conditions \(h(a,b)\le tL\) and \(a\le2tL,b\le tL\) differ only inside bounded-width strips near \(a=2tL\) or \(b=tL\). Each strip contains at most \(O((L+1)^2)\) eligible lattice points, uniformly in \(t\). Therefore the cumulative count is
\[
\#\{n\le X:n\text{ five-smooth}, H(n)\le tL\}
=\frac{L^3}{6\alpha\beta\gamma}G(t)+O((L+1)^2)
\]
uniformly in \(t\ge0\). Dividing by \(Q(L)\) proves the asserted uniform distributional estimate.

**4. Support and mean.** Since \(1/B>1/A\), both negative terms and the final positive term in \(G\) vanish for \(t\ge1/B\), while \(G(t)<1\) for every smaller nonnegative \(t\); the density is positive on the interior. Also \(H(n)/L\) is bounded uniformly for \(n\le X\) by \(\max\{1/(2\alpha),1/\beta\}+O(1/L)\). Integrating the uniformly controlled survival functions gives
\[
\frac{\mathbb E H(N_X)}L
=\int_0^\infty(1-G(t))\,dt+O(1/L).
\]
For \(q>0\), \(\int_0^\infty(1-qt)_+^3\,dt=1/(4q)\); the mean formula follows.

## Verification

The accompanying standalone program `verify.py` (Python standard library only) checks the exact exponent recurrence against the closed hitting-time formula for ten thousand exponent pairs; computes ranks directly from the Fibonacci recurrence modulo every integer \(2^a3^b5^c\) with \(0\le a\le7\), \(0\le b\le5\), \(0\le c\le3\); checks the final fixed point as well as the first hitting time in all 192 cases; and compares finite five-smooth empirical distributions and means against the limiting formulas at four explicit logarithmic cutoffs. It also verifies the finite lattice inclusion-exclusion identity. These computations corroborate finite cases only; the all-exponent and asymptotic statements follow from Steps 1–4 rather than from enumeration.

## Relationship to prior work

FitzGibbons, Miller, and Verga (initially public 2023-09-25, arXiv:2309.14501) prove general convergence to fixed points, give exact orders for pure powers of two (their Lemma 4.2), and establish the lcm identity for iterates (their Lemma 5.1). Their article contains the rank identities and fixed-point characterization used above. The present theorem does **not** claim those inputs as novel: it adds the exact boundary-sensitive two-variable hitting-time classification and the uniform statistical limit, including a quantitative error and a mean coefficient, for the naturally invariant five-smooth core. Their results do not themselves give a smooth-number sampling measure or this cumulative distribution.

Luca and Tron (arXiv:1410.2489) study the global counting function of *self-Fibonacci divisors* and recall rank divisibility facts; self-divisibility is not first-passage time, and their counting theorem does not imply the statistical law here. Trojovská (2020) excludes nontrivial periodic points of the rank map; her Table 2 enumerates finite orbit lengths among all integers up to \(50{,}000\), not a first-passage limit under uniform sampling of five-smooth integers.

## Limitations

The law concerns **uniformly sampled five-smooth integers**, a zero-density subset of the positive integers; no assertion is made for general integers. The error term establishes convergence and its rate but does not establish a best possible oscillatory secondary term. The paper's source identities are cited rather than reproved from first principles. The 2025 journal version has a fourth listed author and was retrievable in abstract form; the accessible 2023 preprint was the full text used for the detailed theorem comparison. Additional unindexed work could contain the same statistical calculation, so priority beyond the inspected literature remains subject to independent assessment.

## References

1. M. FitzGibbons, S. J. Miller, A. Verga, *Dynamics of the Fibonacci Order of Appearance Map* (first public 2023-09-25), https://arxiv.org/abs/2309.14501. See Sections 2, 4, 5 and the appendix. A later journal version (2025) also lists M. Javaheri: https://doi.org/10.1080/00150517.2025.2515497.
2. F. Luca and E. Tron, *The Distribution of Self-Fibonacci Divisors* (2014), https://arxiv.org/abs/1410.2489; especially Lemma 1.3 and Theorem 1.2.
3. E. Trojovská, *On Periodic Points of the Order of Appearance in the Fibonacci Sequence*, Mathematics 8 (2020), 773, https://doi.org/10.3390/math8050773.
