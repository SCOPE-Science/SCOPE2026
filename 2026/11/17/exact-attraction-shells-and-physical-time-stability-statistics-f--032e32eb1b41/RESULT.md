# Exact attraction shells and physical-time stability statistics for an oscillatory sewed focus

## Finding
For each integer \(k\ge 2\), the sinusoidal sewed centre-focus considered below has countably many hyperbolic periodic orbits accumulating at the origin. In the section \(\{(-r,0):0<r<2/27\}\), every point other than a repelling periodic point is attracted to exactly one of the even-indexed cycles. Their complete basin intervals, normalized basin probabilities, physical periods, and Floquet multipliers are explicit. More sharply, when an initial section radius is uniformly distributed, the distribution of slow physical-time contraction is bounded away from zero for \(k=2\), but exhibits a power-law zero-rate tail for every \(k\ge3\).

Put \(r_n=2/n\) for integers \(n\ge27\), and let \(n\ge28\) be even. The stable cycle at \(r_n\) has exactly the section basin
\[
 B_n=(r_{n+1},r_{n-1}),\qquad |B_n|=\frac4{n^2-1},\qquad T_n=\frac8n,
\]
with return multiplier and physical-time Floquet exponent
\[
\mu_{n,k}=\frac{1-\pi(2/n)^{2k-3}}{1+\pi(2/n)^{2k-3}},\qquad
\Lambda_{n,k}=\frac n8\log\mu_{n,k}<0.
\]
If \(U\) is uniform on \((0,2/27)\) and \(N\) is the even index of its attracting cycle, then
\[
\mathbb P(N=n)=\frac{54}{n^2-1},\qquad
\mathbb P(N\ge K)=\frac{27}{K-1}\quad(K\ge28\text{ even}).
\]
When \(k=2\), every \(|\Lambda_{n,2}|>\pi/2\) and their infimum is \(\pi/2\). When \(k\ge3\), writing \(q=2k-4\) and \(A_k=\pi 2^{2k-5}\),
\[
 \mathbb P(0<|\Lambda_{N,k}|\le\varepsilon)
 \sim 27\left(\frac{\varepsilon}{A_k}\right)^{1/q}
 \quad(\varepsilon\downarrow0).
\]

## Assumptions and scope
Use the plane divided into the open upper and lower half-planes at \(y=0\). In the upper half-plane let
\[
\dot x=1,\qquad
\dot y=-2x+D_k(x),\qquad
D_k(x)=\frac{d}{dx}\left(x^{2k}\sin(2\pi/x)\right)\quad(x\ne0),
\]
with \(D_k(0)=0\). In the lower half-plane let \(\dot x=-1,\ \dot y=-2x\). Cross the switching line by ordinary forward-time sewing; near the origin the normal components have matching strict signs for \(x\ne0\), so the specified crossing flow is unambiguous. The origin is excluded from the section. The parameter \(k\) is an integer, \(k\ge2\), and every probabilistic statement uses one uniform initial radius on the stated one-dimensional section, not planar area or an invariant dynamical measure. The theorem is local in the prescribed interval and does not claim a global planar phase portrait.

## Proof
Set \(R=2/27\) and define on \([0,R]\)
\[
 H_k(r)=r^2-r^{2k}\sin(2\pi/r),\qquad
 G_k(r)=r^2+r^{2k}\sin(2\pi/r),
\]
where the oscillatory terms vanish at zero. Direct differentiation gives \(H_k'(r)=2r-D_k(r)\), \(G_k'(r)=2r+D_k(r)\) for \(r>0\). Uniformly for all integer \(k\ge2\) and \(0<|x|\le R\),
\[
 \frac{|D_k(x)|}{2|x|}\le k|x|^{2k-2}+\pi|x|^{2k-3}
 \le 2R^2+\pi R<1.
\]
The last comparison follows because the two displayed powers are largest at \(k=2\) for \(R<1\). Thus both \(H_k\) and \(G_k\) increase strictly from zero to \(R^2\): \(\sin(2\pi/R)=\sin(27\pi)=0\). Their ranges coincide, so \(P_k=H_k^{-1}\circ G_k\) is an increasing homeomorphism of \([0,R]\).

The upper trajectory from \((-r,0)\) has graph
\[
 y(x)=-x^2+x^{2k}\sin(2\pi/x)+G_k(r).
\]
Its derivative has the sign opposite to \(x\) off zero because \(|D_k(x)|<2|x|\). Therefore it crosses the upper half-plane in one arc until its unique next zero \(x=s>0\), determined by \(H_k(s)=G_k(r)\). The lower arc is \(y=x^2-s^2\), going from \((s,0)\) to \((-s,0)\). Consequently the exact full section return is \(P_k(r)=s\). It preserves \((0,R)\), and
\[
 \operatorname{sgn}(P_k(r)-r)=\operatorname{sgn}\sin(2\pi/r).
\]

The complete nonzero fixed set on \((0,R]\) is \(\{r_n=2/n:n\ge27\}\). At a fixed point, differentiating the inverse relation yields
\[
 P_k'(r_n)=\frac{1-(-1)^n\pi r_n^{2k-3}}
 {1+(-1)^n\pi r_n^{2k-3}}.
\]
The denominator is positive under the uniform derivative bound. Thus even \(n\) are attracting and odd \(n\) repelling. The sign of the displacement between consecutive fixed points points toward the even-indexed member; monotonicity of \(P_k\) and bounded monotone convergence prove the complete basin \((r_{n+1},r_{n-1})\) for each even \(n\ge28\). The only other section initial conditions are the odd fixed points and the right endpoint (excluded). An upper traversal of a fixed cycle takes \(2r_n\) because \(\dot x=1\), and its lower traversal takes the same amount because \(\dot x=-1\); hence \(T_n=4r_n=8/n\).

The basin width telescopes exactly:
\[
 |B_n|=\frac2{n-1}-\frac2{n+1},\qquad
 \sum_{\substack{n\ge K\\n\,\mathrm{even}}}|B_n|=\frac2{K-1}.
\]
Since the section length is \(R=2/27\), these give the probabilities and show that every nonexceptional radius is accounted for. Writing \(z_{n,k}=\pi(2/n)^{2k-3}\in(0,1)\) gives
\[
 |\Lambda_{n,k}|=\frac n4\operatorname{arctanh}(z_{n,k}).
\]
For \(k=2\), \(z_{n,2}=2\pi/n\), so the strict inequality \(\operatorname{arctanh}(z)>z\) gives \(|\Lambda_{n,2}|>\pi/2\), with convergence to \(\pi/2\) as \(n\to\infty\). For \(k\ge3\), the power series \(\operatorname{arctanh}z=z+O(z^3)\) gives \(|\Lambda_{n,k}|\sim A_kn^{-q}\), where \(q=2k-4\). The rate is eventually strictly decreasing because the positive function \(r^{-1}\operatorname{arctanh}(\pi r^{2k-3})\) increases with \(r\) for small \(r\) when \(k\ge3\), as its leading power is \(r^{2k-4}\). Hence the rate threshold selects all sufficiently large even \(n\), with cutoff \(n\sim(A_k/\varepsilon)^{1/q}\). Apply the exact probability tail \(27/(K-1)\) at the nearest even cutoff to obtain the stated constant and exponent.

## Verification
The accompanying standalone `checker.py` reproduces exact rational basin-width and tail telescoping identities, checks the inverse return map numerically on sample intervals for several values of \(k\), and compares computed multipliers and limiting rates with the formulas. It returns `SEWED_FOCUS_BASIN_RATE_CHECK_OK`. These finite diagnostics are not substitutes for the all-\(k\), all-\(n\) analytical inequalities and the exact telescoping proof above.

## Relationship to prior work
Glendinning, Hogan, Homer, Jeffrey and Szalai (2023), Section 4, equations (17)–(19) and Theorem 4, introduce this sewed centre-focus construction with odd oscillatory forcing, including the \(\sin(2\pi/x)\) example, infinitely many isolated cycles, and their alternating stability. Those properties are prior work, **not** claimed as new here. The contribution is the explicit full local return map on a common invariant section, all attraction-basin intervals and their exact probability law, and especially the physical-time rate dichotomy and sharp almost-neutral rate distribution. Classical Filippov local classification and related border-collision examples do not supply these particular quantitative conclusions.

## Limitations
Only \(0<r<2/27\) and integer \(k\ge2\) are treated; trajectories on the origin and global behavior outside the section are not classified. The attracting indices are not chosen uniformly but by a uniform *radius*, and the derived distribution is not a natural invariant planar probability. The degree of smoothness at \(x=0\) is finite and depends on \(k\). This work has not received an independent mathematical audit. Publication priority against unindexed equivalent calculations remains uncertain.

## References
1. P. Glendinning, S. J. Hogan, M. Homer, M. R. Jeffrey and R. Szalai, *Uncountably Many Cases of Filippov’s Sewed Focus*, Journal of Nonlinear Science **33**, article 52 (2023), DOI: 10.1007/s00332-023-09910-4; public May 5, 2023; freely readable preprint arXiv:2306.09743v1, Section 4.
2. A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer, 1988 (classical definitions and sewing context, as cited in reference 1).
3. D. J. W. Simpson, *Unfolding codimension-two subsumed homoclinic connections in two-dimensional piecewise-linear maps*, 2014, arXiv:1312.2651 (related but distinct border-collision mechanism; not used in the proof).
