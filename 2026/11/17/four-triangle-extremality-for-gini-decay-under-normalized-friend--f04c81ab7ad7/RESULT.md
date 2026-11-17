# Four-triangle extremality for Gini decay under normalized friendship-graph heat

## Finding

Let \(F_m\) be the simple unweighted friendship graph consisting of \(m\ge1\) triangles joined at exactly one hub. Let \(A\) and \(D\) be its adjacency and degree matrices, and let \(H_t=\exp(t(D^{-1}A-I))\), for real \(t\ge0\). On real vertex signals use the complete-pair Gini seminorm
\[
G_m(f)=\sum_{\{u,v\}\subset V(F_m)}|f(u)-f(v)|.
\]
For every \(m\ge1\) and every \(t\ge0\), its exact induced quotient seminorm is
\[
\boxed{\|H_t\|_{G_m\to G_m}=e^{-3t/2}+\frac{2(m^2-1)}{m(2m-1)}(e^{-t/2}-e^{-3t/2}).}
\]
For \(m=1\), this is \(e^{-3t/2}\); for \(m=2\), it is \(e^{-t/2}\). For every \(m\ge2\), the constant is attained by the binary signal supported on both peripheral vertices of a single triangle. At \(t>0\), exactly four triangles maximize this norm among **all** finite friendship graphs:
\[
\boxed{\sup_{m\ge1}\|H_t\|_{G_m\to G_m}=\frac{15}{14}e^{-t/2}-\frac1{14}e^{-3t/2},\quad\text{uniquely at }m=4.}
\]
Every such semigroup is strictly Gini-contracting for positive time, although the sharp quotient norm exceeds the slow spectral decay factor \(e^{-t/2}\) when \(m\ge3\). The largest relative excess, at four triangles, increases toward \(1/14\) as \(t\to\infty\).

## Assumptions and scope

The graph is undirected and unweighted, with one hub \(o\), and pairs \((u_j,v_j)\) for \(1\le j\le m\); each pair plus the hub forms a triangle and different pairs have no connecting edges. Consequently \(\deg(o)=2m\), and every peripheral vertex has degree two. The semigroup acts on the finite-dimensional real vector space \(\mathbb R^{2m+1}\); the seminorm vanishes precisely on constants. There are no boundary, large-graph, or regularity assumptions. Supremums defining the operator norm range over all nonconstant real input signals.

## Proof

**1. Spectral decomposition of the normalized generator.** Write \(s_j=(f(u_j)+f(v_j))/2\), and \(\bar s=m^{-1}\sum_j s_j\). Define a projection \(P_m\) by \((P_mf)(o)=0\) and \((P_mf)(u_j)=(P_mf)(v_j)=s_j-\bar s\). Let \(C_m\) denote the constant-valued projection with value \((f(o)+2\bar s)/3\), and put \(R_m=I-C_m-P_m\). Direct substitution into \(Q=D^{-1}A-I\) gives
\[
Q C_m=0,\qquad QP_m=-\tfrac12P_m,\qquad QR_m=-\tfrac32R_m.
\]
The operators \(C_m,P_m,R_m\) are complementary projections. Thus, with \(a=e^{-t/2}\) and \(b=e^{-3t/2}\),
\[
H_t=C_m+aP_m+bR_m=C_m+b(I-C_m)+(a-b)P_m.
\]
Since constants disappear in \(G_m\), it follows that
\[
G_m(H_tf)=G_m\bigl(bf+(a-b)P_mf\bigr).
\]

**2. Exact Gini norm of the pair-mean projection.** We claim
\[
\boxed{\|P_m\|_{G_m\to G_m}=c_m:=\frac{2(m^2-1)}{m(2m-1)}.}
\]
The formula gives \(c_1=0\), correctly, because the sole pair mean equals the overall peripheral mean. For a constant-annihilating linear map \(T\), the Gini seminorm ratio is maximized among characteristic functions of nonempty proper vertex subsets: order the distinct levels of a real input, express it as a constant plus a positive linear combination of nested indicator functions, and apply the triangle inequality to \(G_m(Tf)\) and the identity \(G_m(f)=\sum\text{(level gap)}\,G_m(\text{indicator})\).

Every indicator is equivalent, up to taking its complement, to one whose hub value is zero. Label a peripheral pair *full*, *split*, or *empty* according as it has two, one, or zero selected vertices. If there are \(r\) full, \(q\) split and \(m-r-q\) empty pairs, independently replace each split pair by a full pair or an empty pair, each with probability \(1/2\). The resulting random indicator \(X\) satisfies \(\mathbb E X=f\). For its complete-pair variation, all cross-pair contributions and hub-pair contributions retain their expectations, while the within-pair contribution of each originally split pair drops from one to zero. Therefore \(\mathbb E G_m(X)=G_m(f)-q\). Jensen's inequality and linearity imply
\[
G_m(P_m f)\le\mathbb E G_m(P_m X)\le c\,\mathbb E G_m(X)\le c G_m(f)
\]
whenever the bound \(G_m(P_m X)\le cG_m(X)\) holds for all indicators built from entirely full or empty pairs. Consequently it suffices to test such cuts.

For a union of \(r\) full pairs, where \(1\le r\le m\), write \(h=m-r\). Direct counting of pair-pair differences and hub-pair differences gives
\[
G_m(f)=2r(2h+1),\qquad G_m(P_mf)=4rh(1+1/m).
\]
Their ratio is \(2h(m+1)/(m(2h+1))\), strictly increasing in the integer \(h\). Its maximum for \(m\ge2\) occurs at \(h=m-1\), namely exactly one full pair, and equals \(c_m\). For \(m=1\), \(P_1=0\). This proves the projection-norm formula, including attainment.

**3. Exact semigroup norm and extremizers.** Since \(0<b\le a\le1\), the decomposition gives
\[
G_m(H_tf)\le b G_m(f)+(a-b)G_m(P_mf)\le[b+(a-b)c_m]G_m(f).
\]
For a single-full-pair indicator, every nonzero input pairwise difference has the same sign as the corresponding difference after applying \(P_m\); the other differences originate from \(P_m\) alone. Hence equality holds in the first triangle inequality and in the sharp projection estimate, giving the displayed norm for \(m\ge2\). For \(m=1\), \(P_1=0\) and \(H_t\) acts as \(bI\) modulo constants, so the norm is exactly \(b\). At \(t=0\) every case has norm one.

**4. Unique four-triangle maximizer and strict decay.** For \(m\ge2\), put \(d_m=c_m-1=(m-2)/(m(2m-1))\). Its forward difference is
\[
d_{m+1}-d_m=-\frac{2(m^2-3m-1)}{m(m+1)(2m-1)(2m+1)}.
\]
It is positive from \(m=2\) to \(m=4\), then negative thereafter. Thus \(d_m\) has its unique maximum \(d_4=1/14\). Since \(a>b\) for positive time, the entire semigroup norm is uniquely maximized at \(m=4\); \(m=1\) has norm \(b<a\). Also, for \(m\ge2\),
\[
1-\|H_t\|_{G_m\to G_m}=(1-a)[1-d_m a(1+a)]>0 \quad(t>0),
\]
because \(0\le d_m\le1/14\) and \(0<a<1\). The \(m=1\) case is immediate from \(b<1\). The ratio at four triangles to the slow factor is \(1+(1-e^{-t})/14\), giving the stated limiting excess.

## Verification

`verify.py` uses only the Python standard library and exact rational arithmetic. It checks the three projection identities against the explicit normalized generator in eight graph sizes, exhausts all full/split/empty-pair binary-cut **orbits** through eight triangles, checks exact sharp pair witnesses, tests 1,920 additional signed signals, and checks the four-triangle coefficient. Run `python verify.py` from the directory containing this file. These finite checks supplement, and are not substitutes for, the proof for arbitrary \(m\) and real \(t\).

## Relationship to prior work

Estrada, *When local and global clustering of networks diverge* (public repository copy deposited October 9, 2015), studies windmill graphs and gives adjacency and **combinatorial**, not degree-normalized, Laplacian spectra, along with clustering, epidemic and synchronization analyses. This establishes pertinent graph structure and spectral context, not an operator norm for complete-pair Gini variation. Sandryhaila and Moura, *Discrete Signal Processing on Graphs: Frequency Analysis* (first public arXiv version July 1, 2013), define graph variation via an adjacency-shift residual, rather than the unweighted complete-pair Gini seminorm used here. Earlier related studies of normalized heat, graph-edge variation, Wasserstein contraction and Gini-type dispersion do not supply the present pair-mean projection norm or its all-size four-triangle maximizer. Known spectral-decomposition techniques are used, and are not claimed as new.

## Limitations

The result concerns finite friendship graphs with all triangles unweighted, uniform counting-based Gini variation across **all vertex pairs**, and continuous-time random-walk-normalized heat. It does not give corresponding norms for graph-edge variation, arbitrary clique windmills, nonuniform vertex weights, directed graphs, discrete-time powers, or other metrics. Bibliographic searches and inspection of relevant primary material do not establish absolute historical priority; an unindexed equivalent calculation may exist.

## References

1. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis*, arXiv:1307.0468, initial public submission July 1, 2013. https://arxiv.org/abs/1307.0468
2. E. Estrada, *When Local and Global Clustering of Networks Diverge*, Linear Algebra and its Applications **488** (2016), 249–263; publicly deposited author manuscript October 9, 2015. https://strathprints.strath.ac.uk/id/eprint/54532
3. K. C. Das, A. D. Güngör, and S. B. Bozkurt, *On the Normalized Laplacian Eigenvalues of Graphs*, Ars Combinatoria **118** (2015), 143–154. https://combinatorialpress.com/ars-articles/volume-118-ars-articles/on-the-normalized-laplacian-eigenvalues-of-graphs/
