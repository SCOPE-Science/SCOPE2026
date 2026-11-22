# Three-vertex rigidity of consecutive-time stochastic ordering for signed-strength Markov walks

## Finding

**Theorem (sharp three-state consecutive-time rigidity).** Let \(D=\{(d,s)\in\mathbb R^2:d>0,\ |s|\le d\}\) and let \(F:D\to(0,\infty)\) be any positive function, with **no** regularity assumptions. For every finite connected simple signed weighted graph with at least two vertices, give each edge a nonzero real signed weight \(a_{ij}=a_{ji}\) and define the strength \(d_i=\sum_j|a_{ij}|\), signed strength \(s_i=\sum_j a_{ij}\), and Markov transition probabilities \(P_{ij}=|a_{ij}|/d_i\). Start the walk from \(\alpha_i=F(d_i,s_i)/\sum_jF(d_j,s_j)\).

The following are equivalent:

1. On every connected signed weighted graph with **exactly three vertices**, the score process satisfies \(s(X_0)\le_{\rm st}s(X_1)\le_{\rm st}s(X_2)\) (first-order stochastic order).
2. There exists a constant \(c>0\) such that \(F(d,s)=cd\) for every \((d,s)\in D\).
3. On every finite connected signed weighted graph, the laws of \(s(X_t)\) are identical at all integer times \(t\ge0\).

The three-vertex test size is sharp: on connected two-vertex graphs the score is the same at both vertices, for every signed edge weight, and every positive \(F\) passes the three-time score test.

In particular, universal monotonicity **between successive times** is much more restrictive than dominance of each later score over the initial score. The latter condition permits nonstationary positive rules \(F(d,s)=d g(s)\) for positive decreasing \(g\), as established by Louvaris and Trevezas.

## Assumptions and scope

The graph is finite, simple, undirected and connected, with no loops and with real nonzero edge marks. A missing edge has weight zero. Every vertex has positive magnitude strength. Stochastic order means \(U\le_{\rm st}V\) if \(\Pr(U\ge z)\le\Pr(V\ge z)\) for every real threshold \(z\). All initial weights \(F(d,s)\) are strictly positive; the theorem quantifies over **all** edge magnitudes and sign patterns. No continuity, differentiability, homogeneity, measurability, or boundedness of \(F\) is assumed. The theorem is about distributions of signed strengths, not necessarily the distribution of the entire Markov state.

## Proof

**Step 1: any signed three-vertex path forces additivity.** Fix arbitrary \(x,y\in\mathbb R\setminus\{0\}\). Consider a path with center \(o\) and leaves \(u,v\), whose incident signed edge weights are \(x,y\). Write

\[
A=F(|x|+|y|,x+y),\qquad B=F(|x|,x),\qquad C=F(|y|,y),
\]
\[
p=\Pr(X_0=o)=\frac{A}{A+B+C},\qquad q=\frac{|x|}{|x|+|y|}\in(0,1).
\]

The center-state probabilities at times zero, one, two are \(p,1-p,p\), while at times one and two the respective leaf probabilities are \((pq,p(1-q))\) and \(((1-p)q,(1-p)(1-q))\). If \(x,y>0\), the center has the unique greatest score \(x+y\), so monotonicity of that upper-tail event across all three times gives \(p\le1-p\le p\), hence \(p=1/2\). If \(x,y<0\), the center has the unique least score, so monotonicity of its lower-tail event gives \(p\ge1-p\ge p\), again \(p=1/2\).

If \(x>0>y\), the largest score is \(x\), at leaf \(u\), and the smallest score is \(y\), at leaf \(v\), because \(y<x+y<x\). Monotonicity from time one to time two gives \(pq\le(1-p)q\) for the top tail and \(p(1-q)\ge(1-p)(1-q)\) for the bottom tail. Because \(0<q<1\), these imply both \(p\le1/2\) and \(p\ge1/2\). The case \(y>0>x\) is identical after swapping the leaves. In every case \(p=1/2\), therefore

\[
F(|x|+|y|,x+y)=F(|x|,x)+F(|y|,y).\tag{1}
\]

**Step 2: positivity solves the functional equation without continuity.** For \(t>0\), set \(f_+(t)=F(t,t)\) and \(f_-(t)=F(t,-t)\). Equation (1) for two positive weights and two negative weights gives \(f_\pm(u+v)=f_\pm(u)+f_\pm(v)\) for \(u,v>0\). Since \(f_\pm\) are positive, each is strictly increasing. An additive monotone function on the positive real numbers is linear: rational approximation gives \(f_+(t)=c_+t\) and \(f_-(t)=c_-t\) with \(c_+,c_->0\). Applying (1) to \(x=(d+s)/2>0\) and \(y=-(d-s)/2<0\) gives, for \(|s|<d\),

\[
F(d,s)=c_+\frac{d+s}{2}+c_-\frac{d-s}{2}=cd+bs,
\]

where \(c=(c_++c_-)/2>0\) and \(b=(c_+-c_-)/2\) satisfy \(|b|<c\). The same formula holds on \(s=\pm d\) by definition of \(f_\pm\). This is the entire function domain \(D\).

**Step 3: the signed triangle forces the slope in score to vanish.** Take the three-vertex triangle with weights \(a_{12}=a_{23}=1\), \(a_{13}=-1\). All three strengths are \(d_i=2\), and the score vector is \((0,2,0)\). The magnitude-weighted walk chooses either other vertex with probability \(1/2\). Since \(F(d,s)=cd+bs\), the probability of the unique high-score vertex \(2\) at time zero is

\[
p_0=\frac{c+b}{3c+b};\qquad
p_1=\frac{c}{3c+b};\qquad
p_2=\frac{2c+b}{2(3c+b)}.
\]

The two required inequalities for this single upper-tail event are

\[
p_1-p_0=-\frac b{3c+b}\ge0,\qquad
p_2-p_1=\frac b{2(3c+b)}\ge0.
\]

The denominator is positive because \(|b|<c\). Thus \(b=0\) and \(F(d,s)=cd\). This completes \((1)\Rightarrow(2)\).

**Step 4: stationarity and minimality.** For \(F(d,s)=cd\), the initial law is \(\pi_i=d_i/\sum_jd_j\). Detailed balance holds because \(\pi_iP_{ij}=|a_{ij}|/\sum_kd_k=\pi_jP_{ji}\). Therefore \(\pi P=\pi\), yielding \((2)\Rightarrow(3)\). Identical laws trivially imply the three-time stochastic order, proving \((3)\Rightarrow(1)\). A connected graph on two vertices consists of one edge of weight \(x\ne0\); both vertex scores equal \(x\), so \(s(X_t)=x\) at every time under *every* initial distribution. Two vertices cannot enforce any restriction on \(F\), whereas three suffice.

## Verification

Run \(`python3 checker.py`\) with the Python 3 standard library. It performs 1,315 exact-rational checks on three-vertex paths with 100 nonzero signed integer edge pairs and four distinct linear rule parameters, and on the signed triangle with five parameter choices. It verifies the complete two-step Markov law, path-center identity, stationary special case, and triangle temporal inequalities. These finite checks are **not** a substitute for the universal analytical proof, which covers all real edge weights and arbitrary positive functions.

## Relationship to prior work

Louvaris and Trevezas (2026, arXiv:2611.17118v1), Theorem 1 and Corollary 1, classify universal one-time improvement and stochastic domination \(s(X_0)\le_{\rm st}s(X_k)\) for each fixed \(k\); they explicitly note on page 4 that Theorem 1(iv) does *not* assert monotonicity between consecutive times. Those admissible functions include nonconstant decreasing score tilts; our requirement forces the unique stationary sampling class, using only three-state tests. In particular their sharp five-vertex threshold concerns the weaker initial-versus-later condition, not the present sharp three-state rigidity. The earlier multistep friendship-paradox literature studies degree bias and steps on different random-walk/graph models, not arbitrary positive local signed-strength sampling rules with the universal consecutive-time condition. Stationarity of magnitude-strength bias is standard and is fully credited as the sufficiency half, not claimed as new.

## Limitations

The result is a finite-state exact characterization, not a mixing-time theorem, and requires universal quantification over **signed** edge weights; unsigned-only tests are not asserted sufficient. It restricts the starting law to a common positive local rule \(F(d,s)\); arbitrary graph-dependent global starting laws are outside scope. A broader published time-monotonicity characterization might imply this theorem; available primary sources and published claim records were compared, but human historical-priority validation remains outstanding.

## References

1. M. Louvaris and S. Trevezas, *Universal sampling rules for the signed friendship paradox*, arXiv:2611.17118v1 (first public 2026-11-12), https://arxiv.org/abs/2611.17118 . Especially Theorem 1 and discussion following Corollary 1.
2. K. S. Berenhaut and C. M. Zhang, *Disparity-persistence and the multistep friendship paradox*, Probability in the Engineering and Informational Sciences 38 (2024), 290–298, https://doi.org/10.1017/S026996482300013X .
3. K. S. Berenhaut and C. M. Zhang, *The degree-wise effect of a second step for a random walk on a graph*, Journal of Applied Probability 55 (2018), 1203–1210, https://doi.org/10.1017/jpr.2018.79 .
