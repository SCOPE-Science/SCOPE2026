# Every-deadline rescue advantage of balanced colonization in a two-patch metapopulation

## Finding

For a closed, two-patch, continuous-time occupancy model starting with both patches occupied, a fixed total directional rescue budget is optimally balanced **for every finite deadline**, not merely for expected time to extinction. Increasing \(q=cd\) strictly increases survival \(\Pr(\tau_q>t)\) at every \(t>0\). In particular, \(c=d=C/2\) is the unique all-deadline optimal allocation, even with unequal local extinction rates. The exact separation between two allocations with \(q_2>q_1\) begins at fourth order:

\[
\Pr(\tau_{q_2}>t)-\Pr(\tau_{q_1}>t)
=\frac{ab(q_2-q_1)}{12}t^4+O(t^5),\qquad t\downarrow0.
\]

The result distinguishes a full stochastic ordering of extinction times from a weaker comparison of their means.

## Assumptions and scope

Let \(a,b,C>0\). The two habitat occupancies are binary. Independent exponential transition clocks govern local extinction at rates \(a,b\) and rescue of a missing population at directional rates \(c,d\ge0\), with \(c+d=C\). State \(00\) (both patches empty) is absorbing; there is no external recolonization. State \(11\) is the initial state. Write \(10\) for the first patch alone, \(01\) for the second patch alone, and \(\tau_{c,d}\) for the first hitting time of \(00\).

The transient generator in the order \((11,10,01)\) is

\[
Q=\begin{pmatrix}-a-b&b&a\\c&-a-c&0\\d&0&-b-d\end{pmatrix}.
\]

For every fixed \(a,b,C\), define \(q=cd\in[0,C^2/4]\). The distribution depends on \((c,d)\) only via \(q\): let \(\tau_q\) denote that distribution. No claim is made about initial singleton occupation, externally recolonized systems, demographic within-patch dynamics, or more than two patches.

## Proof

**1. The exact extinction-time transform.** Put \(S=a+b\) and \(P=ab\). The exit rates to absorption from the transient states are the vector \(r=(0,a,b)^\top\). The density of the absorption time is \(f_q(t)=e_{11}^{\top}e^{Qt}r\), and the Laplace transform \(F_q(z)=\mathbb E[e^{-z\tau_q}]\) is \(e_{11}^{\top}(zI-Q)^{-1}r\). Direct determinant and cofactor expansion gives

\[
F_q(z)=\frac{N(z)}{D_q(z)},\qquad
N(z)=P(S+C+2z),
\]
\[
D_q(z)=z^3+(2S+C)z^2+(S^2+P+SC+q)z+P(S+C).
\]

In particular, all allocation dependence is through \(q\), and \(F_q(0)=1\), showing almost-sure absorption. Equality of transforms proves equality of the entire laws whenever the products agree, including reversed directions \((c,d)\) and \((d,c)\), even if the patch extinction rates differ.

**2. A positive convolution proves strict stochastic order.** Let \(U_q(t)=\Pr(\tau_q>t)\). Its time-Laplace transform is \(\widehat U_q(z)=(1-F_q(z))/z\). Since \(\partial_q D_q(z)=z\), differentiation at fixed \(S,P,C\) yields

\[
\partial_q\widehat U_q(z)=\frac{N(z)}{D_q(z)^2}=F_q(z)\frac1{D_q(z)}.
\]

For \(0<q<C^2/4\), choose either positive \((c,d)\) realizing the product. The generator \(Q\) is reversible on its transient graph with weights \(\pi_{11}=1,\pi_{10}=b/c,\pi_{01}=a/d\). For every nonzero real vector \(v\),

\[
-\langle v,Qv\rangle_\pi
=b(v_{11}-v_{10})^2+a(v_{11}-v_{01})^2
+\frac{ab}{c}v_{10}^2+\frac{ab}{d}v_{01}^2>0.
\]

Thus the three eigenvalues of \(-Q\) are positive real numbers \(\lambda_1,\lambda_2,\lambda_3\), with multiplicity. Therefore \(D_q(z)=\prod_{j=1}^3(z+\lambda_j)\), and \(D_q(z)^{-1}\) is the time-Laplace transform of the strictly positive convolution

\[
g_q(t)=\bigl(e^{-\lambda_1\cdot}*e^{-\lambda_2\cdot}*e^{-\lambda_3\cdot}\bigr)(t),\qquad t>0.
\]

The absorption-time density \(f_q(t)\) is strictly positive for every \(t>0\): the event of two consecutive local extinctions before any rescue has a strictly positive smooth density. Standard finite-dimensional matrix-exponential differentiability and uniqueness of Laplace transforms now give

\[
\partial_q U_q(t)=(f_q*g_q)(t)>0\qquad(t>0,\ 0<q<C^2/4).
\]

Continuity in \((c,d)\) extends the strict ordering to either endpoint of the product interval by integrating the positive derivative across the nonempty interior. Since \(cd\le C^2/4\), with equality only at \(c=d=C/2\), balance is the unique maximum at every positive deadline.

**3. Sharp short-horizon order and boundaries.** The absorption probability is

\[
\Pr(\tau_q\le t)=\int_0^t e_{11}^{\top}e^{Qs}r\,ds
=\sum_{k\ge1}\frac{t^k}{k!}e_{11}^{\top}Q^{k-1}r.
\]

Exact multiplication shows that the quadratic coefficient is \(ab\), the cubic coefficient is \(-ab(C+3S)/6\), and the coefficient at degree four has \(q\)-derivative \(-ab/12\). As all earlier coefficients are independent of \(q\), the claimed difference is \(ab(q_2-q_1)t^4/12+O(t^5)\). The error is analytic in \(t\) for fixed rates. Hence a weaker claim merely comparing derivatives up to order three cannot detect the directional advantage.

**4. Mean-only corollary, not claimed as original.** Differentiating \(F_q\) at zero gives

\[
\mathbb E\tau_q=\frac{S^2-P+SC+q}{P(S+C)}.
\]

A mean-only balancing calculation is weaker than the all-deadline stochastic ordering just proved, since expectation inequalities do not imply survival inequalities. This mean criterion is supplied for reproducibility, not separately claimed as new.

**5. Why the initial condition matters.** Starting from state \(10\), the short-time absorption CDF is \(at-a(a+c)t^2/2+O(t^3)\); hence concentrating the rescue budget toward the initially vacant habitat can be better at sufficiently short deadlines. The all-horizon balanced optimum therefore is not asserted for arbitrary initial occupancy.

## Verification

The accompanying standalone `verify.py` recalculates the generator determinant, absorption transform, mean, product derivative and fourth-order coefficient with symbolic algebra. It separately checks many finite-time survival probabilities by matrix exponentials over heterogeneous rates, including zero directional rescue rates, and tests reflection-invariance of the full extinction-time law. All 541 supplied assertions pass in the recorded execution. These numerical checks do not replace the universal convolution proof.

For \(a=b=1\), \(C=2\), the endpoint allocation has mean extinction time \(7/4\), whereas balance has mean \(2\); at time \(t=1\), their survival probabilities are approximately \(0.6519728244\) and \(0.6651433194\), respectively.

## Relationship to prior work

Vuilleumier and Possingham [1] studied directional dispersal asymmetry and metapopulation persistence through a stochastic, many-patch simulation model. Their reported qualitative asymmetry effect motivates a rigorously exact all-deadline question, but their mechanism and conclusions do not supply the present two-patch CTMC stochastic-order formula. Etienne and Heesterbeek [2], and Ross and Pollett [3], focus on management via extinction-time/persistence-time optimization; the available abstracts do not state an all-positive-deadline stochastic dominance comparison. The first of those full articles and the second full article were not available for inspection, so equivalent historical coverage cannot be excluded. Eriksson and colleagues [4] give a more detailed rescue-effect framework that does not, in the inspected full text, establish the fixed-budget two-patch all-horizon law.

The displayed mean formula is a straightforward special-case mean optimization and is not the contribution. The substantive additional assertion is strict stochastic dominance at every \(t>0\), including its fourth-order onset; mean optimization alone logically cannot imply this assertion.

## Limitations

The result holds only for a closed two-habitat occupancy chain initially in state \(11\), with constant exponential transition rates and an exactly fixed sum of directional rescue rates. It is a theoretical benchmark rather than empirical advice. Some relevant classic management articles were accessible only as abstracts; a historical theorem equivalent under a different formulation remains possible. Neither independence from source-specific ecological assumptions nor extension to larger patch networks is proved.

## References

1. Vuilleumier, S., and Possingham, H. P. (2006). *Does colonization asymmetry matter in metapopulations?* Proceedings of the Royal Society B 273, 1637–1642. First public date 2006-03-29. https://doi.org/10.1098/rspb.2006.3469; https://pmc.ncbi.nlm.nih.gov/articles/PMC1634917/.
2. Etienne, R. S., and Heesterbeek, J. A. P. (2001). *Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model.* American Naturalist 158, 389–407. https://doi.org/10.1086/321986.
3. Ross, J. V., and Pollett, P. K. (2010). *Simple rules for ranking and optimally managing metapopulations.* Ecological Modelling 221, 2515–2520. https://doi.org/10.1016/j.ecolmodel.2010.02.016.
4. Eriksson, A., Elías-Wolff, F., Mehlig, B., and Manica, A. (2014). *The emergence of the rescue effect from explicit within- and between-patch dynamics in a metapopulation.* Proceedings of the Royal Society B 281, 20133127. https://doi.org/10.1098/rspb.2013.3127.
