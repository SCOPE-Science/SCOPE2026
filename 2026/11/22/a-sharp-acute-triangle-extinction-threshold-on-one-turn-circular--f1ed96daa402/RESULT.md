# A sharp acute-triangle extinction threshold on one-turn circular helices

## Finding

Let \(\gamma_c(t)=(\cos t,\sin t,ct)\), \(0\le t\le2\pi\), for \(c\ge0\). Define \(\mathcal P(c)\) as the probability that three independent uniform-arclength points on this entire one-turn helix form a strictly acute Euclidean triangle. Put
\[
G(t)=\cot(t/2)-\frac2t-\tan t, \quad \pi/2<t<\pi.
\]
There is exactly one root \(t_*\in(\pi/2,\pi)\) of \(G(t)=0\). Define
\[
m=-\cos t_*\left(\frac{\sin(t_*/2)}{t_*/2}\right)^2,
\qquad c_*=\sqrt m.
\]
Then **\(\mathcal P(c)>0\) if and only if \(0\le c<c_*\)**, and \(\mathcal P(c)=0\) for \(c\ge c_*\). Numerically \(t_*=2.670778089087041\) and \(c_*=0.687437444831901\). This is an exact pitch cutoff: the axial rise per turn is \(2\pi c_*\) when the helical radius is one.

The threshold is accompanied by a sharp positive-probability onset. Write
\[
d=\frac{1}{4\sin^2(t_*/2)}-\frac{1}{t_*^2}>0,
\qquad e=d+\frac{1}{2\cos^2t_*}>0,
\qquad C=\frac{3(\pi-t_*)}{\pi^2m\sqrt{de}}.
\]
Then
\[
\boxed{\mathcal P(c)=C(m-c^2)+o(m-c^2)\quad\text{as }c\uparrow c_*,}
\]
where \(C=0.989816440567424\ldots\). The event has an exact two-dimensional gap integral at every \(c\ge0\), given below, not just an asymptotic.

There is also an explicit limiting shape for rare acute triples. Sort their parameters as \(U_1<U_2<U_3\) and set \(A=U_2-U_1\), \(B=U_3-U_2\), \(\eta=m-c^2\). Conditional on acuteness as \(c\uparrow c_*\),
\[
\frac{(A-t_*,B-t_*)}{\sqrt\eta}
\quad\Longrightarrow\quad\operatorname{Unif}\left\{z\in\mathbb R^2:\frac12 z^{\mathsf T}Qz<1\right\},
\]
where \(Q\) is the positive-definite matrix with eigenvalues \(md\) on \((1,-1)/\sqrt2\) and \(me\) on \((1,1)/\sqrt2\). Jointly, \(U_1\) converges to an independent uniform variable on \([0,2\pi-2t_*]\). Endpoints of intervals have measure zero.

## Assumptions and scope

The helix has unit radius, one full turn (including both parameter endpoints), nonnegative axial slope \(c\), and the ambient Euclidean metric in \(\mathbb R^3\). The constant speed \(\|\gamma_c'(t)\|=\sqrt{1+c^2}\) makes uniform parameter sampling exactly uniform in Euclidean arclength; the three samples are independent. A triangle is strictly acute only if all three Euclidean interior angles are strictly below \(\pi/2\). Collinear or repeated points do not count, but occur with probability zero. Scaling the radius to \(R>0\) changes the dimensionless slope to axial coefficient divided by \(R\); the statement is invariant under common Euclidean dilation.

## Proof

**1. An exact three-angle representation.** Sort the three parameters \(u<v<w\), and put \(a=v-u\), \(b=w-v\), \(s=a+b\), so \(a,b>0\) and \(s<2\pi\). Direct scalar products at the first, middle and last vertices are respectively
\[
\begin{aligned}
F_1(a,b;c)&=1-\cos a-\cos s+\cos b+c^2as,\\
F_2(a,b;c)&=1-\cos a-\cos b+\cos s-c^2ab,\\
F_3(a,b;c)&=1-\cos b-\cos s+\cos a+c^2bs.
\end{aligned}
\]
Each angle is acute exactly when its corresponding scalar product is strictly positive. The order-statistic density of \((u,a,b)\) is \(6/(2\pi)^3\) on \(0<u<2\pi-a-b\). Hence, without approximation,
\[
\mathcal P(c)=\frac{6}{(2\pi)^3}
\int_{a>0,b>0,a+b<2\pi}
(2\pi-a-b)\mathbf 1_{\{F_1,F_2,F_3>0\}}\,da\,db.
\]

**2. A global maximum controls existence.** Using \(1-\cos a-\cos b+\cos(a+b)=-4\sin(a/2)\sin(b/2)\cos((a+b)/2)\), the middle-vertex condition is
\[
F_2=ab[H(a,b)-c^2],\qquad
H(a,b)=-\cos((a+b)/2)\frac{\sin(a/2)}{a/2}\frac{\sin(b/2)}{b/2}.
\]
Because the sinc factors are positive in the allowed range, \(H\le0\) for \(a+b\le\pi\). For \(\pi<a+b<2\pi\), fix the sum \(s=a+b\). The function \(x\mapsto\log(\sin x/x)\) is strictly concave on \((0,\pi)\), since its second derivative is \(x^{-2}-\csc^2 x<0\). Thus \(H\) at fixed \(s\) is uniquely maximized at \(a=b=s/2\). Set \(a=b=t\). On \((\pi/2,\pi)\), its restriction is
\[
 h(t)=-\cos t\bigl(\sin(t/2)/(t/2)\bigr)^2.
\]
The derivative of \(\log h\) is \(G(t)\), which decreases strictly because
\[
G'(t)=-\tfrac12\csc^2(t/2)+2/t^2-\sec^2t<0
\quad (\pi/2<t<\pi).
\]
Indeed, \(2/t^2<1\le\sec^2t\). Furthermore \(G(t)\to+\infty\) at the left endpoint and \(G(\pi)=-2/\pi<0\). Consequently \(h\) has exactly one maximizer \(t_*\); the unique global maximum of \(H\) is \(m=H(t_*,t_*)>0\). If \(c^2\ge m\), then \(F_2\le0\) at every possible triangle, so no strictly acute triangle exists.

Conversely, when \(c^2<m\), choose \(a=b=t_*\). Then \(F_2=t_*^2(m-c^2)>0\); at this configuration \(F_1=F_3=1-\cos(2t_*)+2c^2t_*^2>0\). The inequalities persist on an open parameter neighborhood, with a nonempty interval of admissible \(u\), since \(2t_*<2\pi\). Thus the acute probability is strictly positive for every \(c<c_*\), completing the threshold classification.

**3. The nondegenerate summit and probability coefficient.** Let \(\Phi=\log H\) in a neighborhood of the maximizer. Its Hessian at \((t_*,t_*)\) has diagonal \(-\tfrac14\sec^2t_*-d\) and off-diagonal \(-\tfrac14\sec^2t_*\). Because the first derivative vanishes, \(-D^2H(t_*,t_*)=Q=-mD^2\Phi\). Thus \(Q\) has eigenvalues \(md\) and \(me\), both positive. With \(z=(a-t_*,b-t_*)\),
\[
H(a,b)=m-\frac12z^{\mathsf T}Qz+O(\|z\|^3).
\]
The global uniqueness and compactness of the feasible closure, together with the strict bound away from the unique maximizer, imply that \(\{H>m-\eta\}\) lies inside an \(O(\sqrt\eta)\) neighborhood. (At the boundary \(a=0\) or \(b=0\), the continuous extension is strictly below \(m\), by strict fixed-sum concavity.) There \(F_1,F_3\) are uniformly positive, so near criticality the only condition is \(H>c^2=m-\eta\).

Set \(z=\sqrt\eta\,y\). By the Taylor expansion and dominated convergence, the rescaled admissible gap region converges in area and distribution to \(E=\{y:\tfrac12 y^{\mathsf T}Qy<1\}\), whose area is \(2\pi/\sqrt{\det Q}\). The integration weight converges uniformly to \(2\pi-2t_*\). The exact order-statistic integral therefore gives
\[
\lim_{\eta\downarrow0}\frac{\mathcal P(\sqrt{m-\eta})}{\eta}
=\frac{6}{(2\pi)^3}(2\pi-2t_*)\frac{2\pi}{\sqrt{\det Q}}
=\frac{3(\pi-t_*)}{\pi^2m\sqrt{de}}=C.
\]
The same density convergence, including the originally uniform \(u\)-coordinate over \([0,2\pi-a-b]\), proves the conditional limiting shape and asymptotic independence asserted above. No finite numerical experiment is used to justify this limit.

## Verification

Run `python checks/verify_helix_acute.py` from the extracted package root. It uses only Python's standard library. Checks include high-precision-by-bisection evaluation of the unique critical root, a direct Cartesian-vector replay of all three angle identities for 60,000 seeded triples, a supplementary finite two-dimensional maximum grid, direct quadrature of the original three-angle indicator near the threshold, and confirmation of the leading coefficient. Its expected success marker is `HELIX_ONE_TURN_ACUTENESS_CHECKS_OK`.

The analytic proof, rather than finite grids, establishes the global maximizer, strict threshold, and continuous limit. Computed approximations are provided only for reproducibility and error detection.

## Relationship to prior work

Goriely, Neukirch and Hausrath (2012) study which spatial point configurations lie on a circular helix and give a radius–pitch parametrization, but do not bound acuteness of three points on a **prescribed one-turn helix**. Dogan (2015, arXiv:1508.05439) characterizes helices through geometry of developable surfaces and does not treat inscribed Euclidean triangle angles or their probability. Hall's classical ball-sampling problem concerns uniform **interior** points of a ball, not uniform arclength samples on a helical curve. Related recent results on circular, elliptic and spherical random triangles involve different supports or intrinsic angles, and neither their statements nor a direct specialization imply the axial-pitch cutoff here.

## Limitations

The sharp constant and its onset concern exactly one full turn and independent arclength-uniform samples. Different turn intervals or other space curves can have different thresholds. The theorem does not claim a global monotonicity formula for \(\mathcal P(c)\), a closed elementary form for its full integral, or a universal result for arbitrary helices. The existing mathematical literature cannot be exhaustively certified by indexing searches; historical priority remains open to independent examination. The research package has not received independent mathematical audit.

## References

1. A. Goriely, S. Neukirch and A. Hausrath, *Helices through 3 or 4 points?*, Note di Matematica 32 (2012), 87–103, DOI: [10.1285/i15900932v32n1p87](https://doi.org/10.1285/i15900932v32n1p87); lawful full text: https://www.lmm.jussieu.fr/~neukirch/articles/2012_helices-3-4-points.pdf.
2. F. Dogan, *On characteristic curves of developable surfaces in Euclidean 3-space*, first arXiv public version dated 2015-08-22, https://arxiv.org/abs/1508.05439 (primary MSC 53A04).
3. G. R. Hall, *Acute triangles in the n-ball*, Journal of Applied Probability 19 (1982), 712–715, https://doi.org/10.2307/3213533, related sampling convention, not a helix theorem.
