# The universal half-power step for two-phase rank-one extragradient

## Finding

Consider simultaneous equal-step extragradient on two alternating real bilinear games, each with one scalar minimizing player and a two-dimensional maximizing player. Their row vectors \(u,v\in\mathbb R^2\) have unit length. Let \(P_h\) be the product of the two consecutive extragradient iteration matrices, with a common step \(h\geq0\), and define \(c=|\langle u,v\rangle|\in[0,1]\). For \(0\le h\le1\), put
\[
\delta=h^2(1-h^2),\qquad k=1-\delta.
\]
The **complete singular-value multiset** of the two-step map is
\[
\boxed{\quad\left\{
\frac{\sqrt{4k+\delta^2c^2}+\delta c}{2},\quad
\frac{\sqrt{4k+\delta^2c^2}-\delta c}{2},\quad k
\right\}.\quad}
\]
In particular, if \(0\le c<1\), the unique minimizer of the sharp one-period Euclidean error-amplification factor \(\|P_h\|_2\) over **all real \(h\ge0\)** is \(h=1/\sqrt2\), independently of the angle between the payoff rows, and
\[
\boxed{\quad \min_{h\ge0}\|P_h\|_2=\frac{\sqrt{48+c^2}+c}{8}<1.\quad}
\]
For parallel or antiparallel rows (\(c=1\)), \(\|P_h\|_2=1\) for all \(0\le h\le1\); the common neutral direction prevents any strict contraction. For orthogonal rows (\(c=0\)), the sharp factor is \(\sqrt3/2\). If the acute angle between the two row lines is \(\theta\downarrow0\), the optimal contraction defect has the sharp expansion
\[
1-\min_{h\ge0}\|P_h\|_2=\frac{\theta^2}{14}+O(\theta^4).
\]
This is a one-period worst-case operator-norm guarantee, **not** a claim that the displayed step minimizes the asymptotic Floquet spectral radius or computational runtime.

## Assumptions and scope

For every pair of unit row vectors \(u,v\in\mathbb R^2\), and every real step \(h\ge0\), use two successive evaluations of the same stage's payoff vector per extragradient update. A game with row \(w\in\{u,v\}\) has payoff \(f_w(x,y)=x\langle w,y\rangle\), where \(x\in\mathbb R\) and \(y\in\mathbb R^2\). The equal-step simultaneous update is
\[
\begin{aligned}
x_{1/2}&=x-h\langle w,y\rangle,&y_{1/2}&=y+hw x,\\
x^+&=x-h\langle w,y_{1/2}\rangle,&y^+&=y+hw x_{1/2}.
\end{aligned}
\]
Its linear iteration map on \(z=(x,y)\in\mathbb R^3\) is
\[
T_w(h)=\begin{pmatrix}
1-h^2&-hw^\top\\hw&I_2-h^2ww^\top
\end{pmatrix},\qquad P_h=T_v(h)T_u(h).
\]
All norms are Euclidean operator norms on \(\mathbb R^3\). There is no stochastic noise, unequal step size, adaptive rule, projection or regularization. The order of \(u,v\) does not affect the singular-value multiset.

## Proof

**1. Single-stage geometry.** Choose any unit \(n_w\perp w\) in \(\mathbb R^2\), and embed it as \(e_w=(0,n_w)\in\mathbb R^3\). The update \(T_w(h)\) fixes \(e_w\), while on the orthogonal plane spanned by \((1,0)\) and \((0,w)\), it is the real matrix
\[
\begin{pmatrix}1-h^2&-h\\h&1-h^2\end{pmatrix}.
\]
Its two singular values there are \(\sqrt{k}\) with \(k=(1-h^2)^2+h^2=1-h^2+h^4=1-\delta\). Consequently, for every real \(h\),
\[
T_w(h)^\top T_w(h)=T_w(h)T_w(h)^\top=kI_3+\delta e_we_w^\top,
\qquad T_w(h)e_w=e_w.
\]

**2. Two-stage rank-two calculation.** First suppose \(0<h<1\), so \(0<\delta\le1/4\). Set \(a=e_u\) and \(b=T_u(h)^\top e_v\). Their Gram quantities are
\[
\|a\|^2=1,\qquad
\|b\|^2=k+\delta c^2,\qquad
|\langle a,b\rangle|=c.
\]
The last identity follows from \(T_u(h)a=a\) and \(|\langle e_u,e_v\rangle|=|\langle u,v\rangle|\). Direct multiplication yields the rank-two update
\[
P_h^\top P_h=k^2I_3+k\delta aa^\top+\delta bb^\top.
\]
The two nonzero eigenvalues of its positive update are those of the Gram matrix of \(\sqrt{k\delta}\,a\) and \(\sqrt\delta\,b\), whose trace and determinant are respectively
\[
\delta(2k+\delta c^2),\qquad \delta^2k^2(1-c^2).
\]
Thus the three eigenvalues of \(P_h^\top P_h\) are
\[
 k^2,\qquad k+\tfrac12\delta^2c^2\pm
\tfrac12\delta c\sqrt{4k+\delta^2c^2}.
\]
The latter two are precisely the squares of
\[
\frac{\sqrt{4k+\delta^2c^2}\pm\delta c}{2}.
\]
These are the top and middle singular values: the rank-two update is positive semidefinite, so the remaining singular value is \(k\). This also covers \(c=0\) and \(c=1\) by continuity, and the endpoints \(h=0,1\) follow directly (all three singular values equal one).

**3. Exact optimization.** For fixed \(c\in[0,1]\) and \(0\le\delta\le1/4\), write
\[
F_c(\delta)=\frac{\sqrt{4(1-\delta)+\delta^2c^2}+\delta c}{2}.
\]
For \(c<1\), its derivative has the sign of
\[
c-\frac{2-\delta c^2}{\sqrt{4(1-\delta)+\delta^2c^2}},
\]
which is strictly negative because both compared quantities are nonnegative and
\[
(2-\delta c^2)^2-c^2\bigl(4(1-\delta)+\delta^2c^2\bigr)
=4(1-c^2)>0.
\]
Hence \(\|P_h\|_2=F_c(\delta)\) is uniquely minimized at the largest possible \(\delta=1/4\), occurring exactly at \(h=1/\sqrt2\), and substitution yields the stated closed form. For \(c=1\), the formula reduces identically to one on this step interval. If \(h>1\), then \(k>1\), so every single-stage matrix has minimum singular value one. Thus the minimum singular value of their product is at least one and \(\|P_h\|_2\ge1\). Therefore no \(h>1\) improves on the interior minimum when \(c<1\). At \(h=0,1\), the norm is also one. Strictness, uniqueness and the parallel boundary follow.

**4. Angular asymptotic and sharpness.** For acute \(\theta\in[0,\pi/2]\), put \(c=\cos\theta\). The derivative at \(c=1\) of \((\sqrt{48+c^2}+c)/8\) equals \(1/7\); since \(1-\cos\theta=\theta^2/2+O(\theta^4)\), the angular defect follows. Every operator-norm bound is attained by a right singular vector of the finite matrix \(P_h\); no generic-state averaging is used.

## Verification

Run `python verify.py` with the dependencies in `requirements.txt`. The checker establishes an exact symbolic characteristic-polynomial identity modulo \(c^2+s^2-1\), the strict derivative certificate, rational specialization identities and additional numerical singular-value comparisons. The recorded output is in `verification_output.txt`. These computations independently stress-test the algebra but the infinite-dimensional quantifiers and all real steps are settled by the proof, not by finite tests.

## Relationship to prior work

Feng, Fu, Hu, Li, Panageas, Peng and Wang (arXiv:2310.02604v1, 2023) prove exponential convergence for general periodic bilinear extragradient and use normality of each stage in Appendix B. Their periodic-game theorem provides a qualitative convergence rate through Floquet multipliers; it does not state the present exact **one-period singular spectrum**, angular formula or universal operator-norm-optimal step on the two-row family. Zhang and Yu (arXiv:1908.05699, initially 2019) analyze stability and optimal asymptotic rates for fixed bilinear payoff matrices; Azizian, Mitliagkas, Lacoste-Julien and Gidel (arXiv:1906.05945, initially 2019) treat another fixed-game spectral setting. Neither fixed-payoff analysis immediately implies the noncommuting period product's singular spectrum. The underlying Gram-rank reduction is classical, and any earlier specialist product-of-contractions formula equivalent to this application is a precedence risk. The theorem does not claim discovery of extragradient, the normality identity, or convergence of arbitrary periodic games.

## Limitations

Only unit row payoffs, dimension \(1\times2\), equal extragradient steps, and two-stage time variation are proved. The model is deterministic and unconstrained. The sharp objective is worst-case Euclidean error **after one full period**; the asymptotic spectral-radius-optimal step may differ. When the payoff row space has higher codimension, untouched coordinates can keep the full operator norm equal to one. No general nonlinear-game, nonunit-row, noisy-oracle, runtime or optimal-control policy claim is made. A specialized earlier theorem on noncommuting products of scaled rotations could already imply the angular formula; independent precedence review remains important.

## References

1. Y. Feng, H. Fu, Q. Hu, P. Li, I. Panageas, B. Peng, and X. Wang, *On the Last-iterate Convergence in Time-varying Zero-sum Games: Extra Gradient Succeeds where Optimism Fails*, arXiv:2310.02604v1, first posted 2023-10-04. https://arxiv.org/abs/2310.02604
2. G. Zhang and Y. Yu, *Convergence of Gradient Methods on Bilinear Zero-Sum Games*, arXiv:1908.05699v4 (originally 2019-08-15), ICLR 2020. https://arxiv.org/html/1908.05699v4
3. W. Azizian, I. Mitliagkas, S. Lacoste-Julien, and G. Gidel, *A Tight and Unified Analysis of Gradient-Based Methods for a Whole Spectrum of Games*, arXiv:1906.05945v5 (originally 2019-06-13), AISTATS 2020. https://arxiv.org/html/1906.05945v5
