# Separate aggregate and peak cooling thresholds for two unequally heated cells

## Finding

Let two cells exchange heat symmetrically at rate \(k>0\), have baseline proportional heat loss \(a>0\), and receive unequal **positive** fixed inputs \(H_1>H_2>0\). For budget \(B>0\), add local proportional cooling rates \(u_1=B-y,\ u_2=y\), with \(0\le y\le B\). The stationary excess temperatures satisfy
\[
(a+B-y+k)T_1-kT_2=H_1,\qquad -kT_1+(a+y+k)T_2=H_2.
\]
Put \(h=H_2/H_1\in(0,1)\) and define
\[
\begin{aligned}
b_h&=k+h(2a+3k),\\
B_{\rm a}&=\frac{2(1-h)a(a+2k)}{b_h+\sqrt{b_h^2+4h(1-h)a(a+2k)}},\\
B_{\rm p}&=\frac{(1-h)a}{h}.
\end{aligned}
\]
The unique minimizer \(y_{\rm a}\) of \(T_1+T_2\) and the unique minimizer \(y_{\rm p}\) of \(\max(T_1,T_2)\) obey **\(0<B_{\rm a}<B_{\rm p}\)** and the following phase diagram:

| Budget | Aggregate minimizer | Peak minimizer |
|---|---|---|
| \(0<B\le B_{\rm a}\) | \(y_{\rm a}=0\) | \(y_{\rm p}=0\) |
| \(B_{\rm a}<B\le B_{\rm p}\) | \(0<y_{\rm a}< B/2\) | \(y_{\rm p}=0\) |
| \(B>B_{\rm p}\) | \(y_{\rm p}<y_{\rm a}<B/2\) | \(y_{\rm p}=(hB-(1-h)a)/(1+h)\), which equalizes the temperatures |

Thus the objectives disagree at every budget above \(B_{\rm a}\), including above the budget at which both cells receive peak-optimal cooling. Below or at \(B_{\rm a}\) the shared optimum cools only the higher-source cell. With \(q=H_1-H_2\), \(C=H_1(a+2k)+H_2(a+B+2k)\), \(D_0=a(a+B)+k(2a+B)\), and \(R=CB-qD_0\), the positive aggregate optimizer is
\[
y_{\rm a}=\frac{R}{C+\sqrt{C^2+qR}}\quad (B>B_{\rm a}).
\]

## Proof

The stationary matrix \(M(y)\) in the two displayed equations has positive diagonal entries and determinant \(D=D_0+By-y^2>0\) on the closed budget interval. Its inverse has positive entries, so the solution is unique and both temperatures are positive. Direct inversion gives
\[
T_1=\frac{(a+y+k)H_1+kH_2}{D},\qquad
T_2=\frac{kH_1+(a+B-y+k)H_2}{D}.
\]

**Aggregate objective.** Writing \(E=T_1+T_2=(C+qy)/D\) gives
\[
D^2E'(y)=Q(y)=qy^2+2Cy+qD_0-CB.
\]
This is strictly increasing on \([0,B]\), and \(Q(B/2)=qD(B/2)>0\). At \(y=0\),
\[
\frac{Q(0)}{H_1}=(1-h)a(a+2k)-b_h B-hB^2.
\]
The right side strictly decreases from positive to negative and vanishes only at the stated \(B_{\rm a}\). At the threshold, the derivative vanishes at the boundary only, so the boundary minimum is still unique. For \(B>B_{\rm a}\), the unique minimum is the positive root of \(Q(y)=0\) and lies strictly below \(B/2\); rationalizing that root gives the displayed expression.

**Peak objective.** Differentiating \(MT=(H_1,H_2)^{\mathsf T}\) with respect to \(y\) gives \(T'=M^{-1}(T_1,-T_2)^{\mathsf T}\). If \(T_1\ge T_2\), then
\[
T_1'=\frac{(a+y+k)T_1-kT_2}{D}\ge\frac{(a+y)T_1}{D}>0.
\]
If \(T_2\ge T_1\), then
\[
T_2'=\frac{kT_1-(a+B-y+k)T_2}{D}\le-\frac{(a+B-y)T_2}{D}<0.
\]
The sign of \(T_1-T_2\) is the sign of \(H_1[(1-h)a+(1+h)y-hB]\). For \(B\le B_{\rm p}\), the maximum is \(T_1\), strictly increasing in \(y\), so the peak optimizer is uniquely \(0\). For \(B>B_{\rm p}\), the equality point \(y_e=(hB-(1-h)a)/(1+h)\) is positive and is strictly less than \(B/2\). The peak strictly decreases up to \(y_e\) and increases thereafter, so \(y_{\rm p}=y_e\).

**Ordering of the thresholds and optimizers.** At an equal-temperature point with common value \(\tau>0\), the two heat balances give \(q=\tau(B-2y_e)\). The derivative formula above yields
\[
E'(y_e)=\frac{\tau(2y_e-B)}{D}=-\frac{q}{D}<0.
\]
At \(B=B_{\rm p}\) this applies to \(y_e=0\), so \(Q(0)<0\) there and \(B_{\rm a}<B_{\rm p}\). Above \(B_{\rm p}\) the strict inequality at \(y_e\) and the unique zero of \(Q\) yield \(y_{\rm a}>y_e=y_{\rm p}\). Between the thresholds one has \(y_{\rm p}=0<y_{\rm a}\). This proves the full diagram and includes both equality budgets.

## Exact example and scope

For \(a=k=H_1=1,\ H_2=1/4\), one has \(B_{\rm a}=(\sqrt{117}-9)/2\) and \(B_{\rm p}=3\). At \(B=2\) peak optimality gives \(y=0\); moving to \(y=1/5\) improves the sum from \(17/28\) to \(55/92\) but raises the peak from \(9/28\) to \(245/736\). At \(B=4\) the peak minimizer equalizes the temperatures at \(y=1/5\), while the aggregate optimum allocates still more to the lower-source cell. See `VERIFICATION.md` for exact finite checks; the proof covers all real parameters of the stated type.

The model is a steady two-cell abstraction with symmetric exchange, identical background loss, equal control costs, a fixed total of proportional cooling rates, and a sum of equally weighted excess temperatures. This is not a calibrated urban-cooling prediction. No claim covers added constraints, unequal weights or time-dependent controls. The source-free case is outside the finding: *A sharp source-to-remote filtration transition in a two-zone pollutant model* (record cd7c91b4d72d) gives the single-source threshold and objective conflict under an exact change of physical variables. The joint two-threshold diagram above concerns two **positive** inputs; in particular the separate peak activation and interior equalization do not occur in that source-free comparator. The inspected literature and comparisons are recorded in `AUDIT.json`; priority beyond them is not certified.
