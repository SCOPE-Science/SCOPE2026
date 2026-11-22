# Eventual first-site optimality of both Stein factors for dense hyper-negative-binomial laws

## Finding
Fix integers \(r\ge2\), \(c\ge1\), and nonnegative integer offsets \(\kappa_1,\ldots,\kappa_r\) with \(\kappa_r=0\). For \(0<w<1\), let \(N_w\) have the hyper-negative-binomial law
\[
 p_n=\frac{w^n}{Z_w}\prod_{i=1}^r\binom{n+\kappa_i+c-1}{n+\kappa_i},\qquad n\ge0.
\]
Let \(b(n)=\prod_i(n+\kappa_i+c)\) and \(d(n)=\prod_i(n+\kappa_i)\). For every subset \(A\subseteq\mathbb N_0\), let \(g_A(0)=0\) solve
\[
 w b(n)g_A(n+1)-d(n)g_A(n)=\mathbf1_A(n)-\Pr(N_w\in A).
\]
Define the *sharp indicator* factors
\[
 \Gamma_w=\sup_{A\subseteq\mathbb N_0}\sup_{n\ge1}|g_A(n)|,\qquad
 \Lambda_w=\sup_{A\subseteq\mathbb N_0}\sup_{n\ge0}|g_A(n+1)-g_A(n)|.
\]
**Theorem.** There exists \(w_0=w_0(r,c,\boldsymbol\kappa)<1\) such that for every \(w_0<w<1\),
\[
 \boxed{\Gamma_w=\Lambda_w=\frac{1-p_0}{w\prod_{i=1}^r(\kappa_i+c)}.}
\]
In particular, both have the sharp common limit
\[
 \lim_{w\uparrow1}\Gamma_w=\lim_{w\uparrow1}\Lambda_w
 =\left(\prod_{i=1}^r(\kappa_i+c)\right)^{-1}.
\]
The supremum in each factor is then attained at the first lattice step \(g_A(1)-g_A(0)\), for the singleton test event \(A=\{0\}\) or its complement.

## Assumptions and scope
All \(r,c,\boldsymbol\kappa\) are fixed while \(w\uparrow1\); the threshold \(w_0\) may depend on them. Neither varying offsets nor simultaneous growth of \(r\) or \(c\) is claimed. The result uses the birth–death normalization of the stated Stein equation and indicator tests, not Lipschitz tests. The product law is meaningful for the given offset constraints, and the model includes the degree-two case with \(c=1\). We do not assert the equality for every \(w\in(0,1)\).

## Proof
Write \(a_n=p_n/(p_0w^n)\). Then \(a_0=1\) and
\[
 a_n=\prod_{i=1}^r\prod_{h=1}^{c-1}\frac{n+\kappa_i+h}{\kappa_i+h},
 \qquad a_{n+1}d(n+1)=a_n b(n).
\]
Empty products equal one. Thus \(a_n\) is a nondecreasing positive polynomial of degree \(s=r(c-1)\), and \(p_n=a_nw^n/\sum_{j\ge0}a_jw^j\). Its normalizer diverges as \(w\uparrow1\), so every fixed mass \(p_n\) tends to zero.

**Step 1: a sharp comparison of partial weights.** Set \(S_m=\sum_{j=0}^m a_j\) and \(T_m=S_m/(a_m b(m))\). Each coefficient of the polynomial \(b(x)-d(x)\) is nonnegative and its constant coefficient is \(b(0)\) because \(d(0)=0\). In fact \(b(m)-d(m)>b(0)\) for integers \(m\ge1\), since \(r\ge2\) and all positive-degree coefficients in the product difference are positive. Consequently
\[
 b(m)\ge d(m)+b(0),\qquad S_m\le\frac{a_m b(m)}{b(0)}.
\]
The second inequality follows by induction: it is equality at zero; then
\(S_{m+1}\le a_{m+1}(d(m+1)+b(0))/b(0)\le a_{m+1}b(m+1)/b(0)\). The latter inequality is strict for \(m+1\ge1\). Since \(S_m\ge a_m\),
\[
 \frac1{b(m)}\le T_m\le\frac1{b(0)},\quad T_0=\frac1{b(0)},\quad T_m<T_0\quad(m\ge1).
\]
Also \(a_mb(m)\) strictly increases with \(m\).

**Step 2: fixed-site limits.** Write \(F_m=\sum_{j\le m}p_j\) and \(G_{m+1}=1-F_m\). Telescoping the Stein equation gives
\[
 g_A(m+1)=\frac{1}{w b(m)p_m}\sum_{j=0}^m p_j\bigl(\mathbf1_A(j)-\Pr(N_w\in A)\bigr).
\]
The sharp sitewise size factor is
\[
 \Gamma_m(w):=\sup_A|g_A(m+1)|=\frac{F_mG_{m+1}}{w b(m)p_m}\longrightarrow T_m
\]
for each fixed \(m\). At \(m=0\), \(\Gamma_0(w)=(1-p_0)/(wb(0))\).

For the increment at site \(m\ge1\), put \(B_m=(wb(m)p_m)^{-1}\), \(C_m=B_mF_m-B_{m-1}F_{m-1}\). Its linear coefficient for \(\mathbf1_A(j)\) is
\[
 K_{m,j}=p_j\left(B_m\mathbf1_{j\le m}-B_{m-1}\mathbf1_{j\le m-1}-C_m\right),
 \qquad \sum_{j\ge0}K_{m,j}=0.
\]
Therefore the exact sitewise first-difference factor is the sum of the positive coefficients. At fixed \(m\), \(C_m\to T_m-T_{m-1}\). The coefficients for \(j<m\) tend to nonpositive numbers because \(a_mb(m)\) strictly increases; the one for \(j=m\) tends to \(1/b(m)\). The combined tail \(j>m\) has the single sign of \(-C_m\) and its total tends to \(-(T_m-T_{m-1})\). Hence
\[
 \lim_{w\uparrow1}\sup_A|g_A(m+1)-g_A(m)|
 =H_m:=\frac1{b(m)}+\max(0,T_{m-1}-T_m).
\]
For \(m=1\), \(H_1<T_0\): if \(T_1\ge T_0\) the result is immediate, while otherwise \(H_1=T_0+1/b(1)-T_1<T_0\), because \(S_1>a_1\). For \(m\ge2\), \(H_m\le T_{m-1}<T_0\). At site zero, the increment factor is exactly \((1-p_0)/(wb(0))\) and tends to \(T_0\).

**Step 3: uniform control of remote sites.** Put \(\varepsilon=1-w\), \(w\ge1/2\), and fix \(L>0\). For \(m\varepsilon\le L\), use monotonicity of \(a_n\), \(G\le1\), and \(w^{-m}\le e^{2m\varepsilon}\) to obtain
\[
 \Gamma_m(w)\le \frac{(m+1)w^{-m}}{wb(m)}
 \le 2e^{2L}(m+1)^{1-r}.
\]
For \(m\varepsilon>L\), the degree-\(s\) polynomial product yields \(a_{m+j}/a_m\le(1+j/m)^s\), so
\[
 \frac{G_{m+1}}{p_m}=\sum_{j\ge1}\frac{a_{m+j}}{a_m}w^j
 \le\sum_{j\ge1}(1+\varepsilon j/L)^s(1-\varepsilon)^j
 \le C_{s,L}/\varepsilon.
\]
The last estimate follows by bounding geometric power moments of orders at most \(s\). Thus \(\Gamma_m(w)\le C_{s,L}/(\varepsilon wb(m))\le 2C_{s,L}\varepsilon^{r-1}/L^r\). Combining the two regimes proves
\[
 \lim_{K\to\infty}\limsup_{w\uparrow1}\sup_{m\ge K}\Gamma_m(w)=0,
\]
and, by the triangle inequality for adjacent solutions,
\[
 \lim_{K\to\infty}\limsup_{w\uparrow1}\sup_{m\ge K}
 \sup_A|g_A(m+1)-g_A(m)|=0.
\]
As \(T_m<T_0\) and \(H_m<T_0\) for every fixed \(m\ge1\), the uniform tail bounds and finitely many strict comparisons imply that, for all \(w\) sufficiently close to one, every noninitial site has a strictly smaller factor than the initial site. The stated simultaneous **exact equality** and limits follow. \(\square\)

## Verification
The independent-of-parameters inequalities in Steps 1–3 constitute the all-index proof. A standalone exact-rational diagnostic script, `check.py`, checks rate balance, the strict limiting inequalities and exact finite-\(w\) indicator-site factors across 36 parameter families. Run with `python check.py`; the recorded execution passed 6,156 assertions. The finite calculations do not substitute for the uniform tail argument and do not certify a numerical value of \(w_0\).

## Relationship to prior work
DeSalvo (2026), Proposition 3.17, supplies the exact size-factor formula and bounds for the first-difference factor; its Open Problem 7 asks for dense-regime behavior. The present theorem identifies both limits **and an eventual exact common maximizer**, for every fixed row count, integer shape and offset vector with \(r\ge2\). Eichelsbacher (2026) studies Stein factors with affine birth rates, whereas these rates are degree-\(r\) products. The earlier special-case result for two equal rows and shape two provides the size factor in a restricted window, not the general simultaneous first-difference conclusion. Related general birth–death factor representations are used, not claimed as new.

## Limitations
The existence threshold \(w_0\) is not given by a closed formula. Offsets, row count and shape cannot drift with \(w\). The distinction from the ordinary one-row negative-binomial regime is structural: the proof needs \(r\ge2\) to make \((m+1)/b(m)\) uniformly vanish. Historical-priority completeness cannot be proved from literature search; independent verification is outstanding.

## References
1. S. DeSalvo, *Stein's method for negative binomial and hyper-negative-binomial laws, with applications*, arXiv:2611.00275v1 (2026-10-30), Proposition 3.17 and Open Problem 7. https://arxiv.org/html/2611.00275v1
2. P. Eichelsbacher, *Stein Solution Factors via Mills Ratios: Affine Birth Rates and Symmetric Potential Distributions*, arXiv:2609.25380 (2026-09-21). https://arxiv.org/abs/2609.25380
3. T. C. Brown and A. Xia, *Stein's method and birth-death processes*, Ann. Probab. 29 (2001), 1373–1403; background general factor theory.
