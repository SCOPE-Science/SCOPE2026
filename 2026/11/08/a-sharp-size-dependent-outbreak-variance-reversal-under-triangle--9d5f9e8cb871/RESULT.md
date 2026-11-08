# A sharp size-dependent outbreak-variance reversal under triangle closure

## Finding

Let \(F_m\) be the friendship graph consisting of \(m\ge1\) triangles sharing one hub. Let \(S_{2m}\) be the star with the same hub and \(2m\) leaves, obtained by removing the \(m\) pairwise-disjoint leaf-to-leaf edges from \(F_m\). On either graph run the continuous-time Markovian susceptible–infectious–removed (SIR) process with infection at rate \(\lambda>0\) **along each infectious–susceptible edge** and recovery at rate one **per infectious vertex**, independently. Initially only the hub is infectious. Let \(Y_m^{\triangle}\) and \(Y_m^{\star}\) be the ultimate fractions of the \(2m\) leaves ever infected.

**Exact limit and mean.** If \(U\sim\operatorname{Beta}(1/\lambda,1)\), then, under a natural joint coupling,
\[
Y_m^{\triangle}\longrightarrow g_\lambda(U):=1-\frac{U+\lambda U^2}{1+\lambda},\qquad
Y_m^{\star}\longrightarrow 1-U\quad\text{almost surely}.
\]
The limiting random variables are nondegenerate for every finite \(\lambda>0\). Their mean difference equals
\[
\mathbb E[g_\lambda(U)]-\mathbb E[1-U]
=\frac{\lambda^2}{(1+\lambda)^2(1+2\lambda)}>0.
\]
Indeed, the coupled limiting difference is \(\lambda U(1-U)/(1+\lambda)>0\) almost surely.

**Sharp variance reversal, including every finite graph.** Put
\[
D_m(\lambda)=\operatorname{Var}(Y_m^{\triangle})-\operatorname{Var}(Y_m^{\star})
\]
and
\[
\begin{aligned}
Q_m(\lambda)={}&24m\lambda^5+(28m-26)\lambda^4-(30m+71)\lambda^3\\
 &-(26m+67)\lambda^2-(4m+25)\lambda-3.
\end{aligned}
\]
For all integers \(m\ge1\) and all real \(\lambda>0\),
\[
\boxed{
D_m(\lambda)=-\frac{\lambda^2Q_m(\lambda)}{2m(1+\lambda)^4(1+2\lambda)^2(1+3\lambda)(1+4\lambda)}.
}
\]
The polynomial \(Q_m\) has **exactly one positive root** \(\lambda_m\), and
\[
D_m(\lambda)>0\text{ for }0<\lambda<\lambda_m,\quad
D_m(\lambda_m)=0,\quad
D_m(\lambda)<0\text{ for }\lambda>\lambda_m.
\]
Thus adding leaf-to-leaf edges always raises the mean infection fraction but **increases its variance at low infection rates and decreases its variance at high rates**. The thresholds obey
\[
\lambda_1=1+\sqrt2,\qquad
\lambda_1>\lambda_2>\cdots>\lambda_\infty\approx1.07327153037648,
\]
where \(\lambda_\infty\) is the unique positive zero of
\[
P(\lambda)=12\lambda^4+14\lambda^3-15\lambda^2-13\lambda-2.
\]

**Complete finite law and fluctuations.** Let \(N_m=2mY_m^{\triangle}\). Conditionally on \(U=u\), the contributions of the \(m\) triangles are i.i.d. on \(\{0,1,2\}\) with probabilities
\[
p_0(u)=u^2,\quad
p_1(u)=\frac{2(u-u^2)}{1+\lambda},\quad
p_2(u)=1-p_0(u)-p_1(u).
\]
Hence the full finite-size probability-generating function is
\[
\mathbb E[z^{N_m}]=\frac1\lambda\int_0^1
  u^{1/\lambda-1}\bigl(p_0(u)+zp_1(u)+z^2p_2(u)\bigr)^m\,du.
\]
The integral is an exact finite rational-polynomial expression for rational \(\lambda\), since \(\mathbb E[U^k]=1/(1+k\lambda)\). If
\(\sigma_\lambda^2(u)=p_1(u)+4p_2(u)-[p_1(u)+2p_2(u)]^2\),
then, jointly with \(U\),
\[
\sqrt m\bigl(Y_m^{\triangle}-g_\lambda(U)\bigr)
\xrightarrow{d}\frac{\sigma_\lambda(U)}{2}Z,
\]
where \(Z\sim N(0,1)\) is independent of \(U\). The centering is **random**; ordinary centering by a constant does not yield a vanishing-variance limit.

## Assumptions and scope

All graph edges are undirected and have independent infectious-contact Poisson processes with rate \(\lambda\) **in each direction** when their tail is infectious and their head susceptible; equivalently, a susceptible vertex is infected at rate \(\lambda\) times its number of infectious neighbors. Infectious lifetimes are independent \(\operatorname{Exp}(1)\). Recovered vertices are immune permanently. The single initial infectious vertex is the common hub. The number \(m\) of triangles is any positive integer, and the infection rate \(\lambda\) is any positive real. The final fraction counts **only leaves**, not the hub.

The star comparison has exactly the same \(2m\) leaves and the same hub-to-leaf edges and stochastic rates. Both graphs can be coupled through the same hub lifetime and the same hub-to-leaf transmission clocks.

## Proof

**1. Conditional triangle law.** Let \(T\sim\operatorname{Exp}(1)\) be the hub infectious duration and put \(u=e^{-\lambda T}\). Given \(T=t\), the probability no leaf of a given triangle is infected is \(e^{-2\lambda t}=u^2\). For exactly one eventual leaf infection, the first leaf must be infected by the hub at some time \(s<t\), with density \(2\lambda e^{-2\lambda s}\,ds\). After that event, the other leaf must avoid hub contact during the remaining interval of length \(t-s\), and must also avoid infection from the first leaf during its own independent \(\operatorname{Exp}(1)\) infectious lifetime \(E\). These avoidance probabilities multiply, giving
\[
\begin{aligned}
p_1(e^{-\lambda t})
 &=\int_0^t2\lambda e^{-2\lambda s}e^{-\lambda(t-s)}\mathbb E[e^{-\lambda E}]\,ds\\
 &=\frac{2}{1+\lambda}(e^{-\lambda t}-e^{-2\lambda t}).
\end{aligned}
\]
The remaining probability is \(p_2=1-p_0-p_1\). Conditional on \(T\), different triangles use disjoint recovery and contact clocks except for that fixed hub duration, so their final infection counts are independent and identically distributed. Since \(\Pr(e^{-\lambda T}\le u)=u^{1/\lambda}\) for \(0\le u\le1\), the mixing variable \(U=e^{-\lambda T}\) is \(\operatorname{Beta}(1/\lambda,1)\). This proves the conditional multinomial law and its integrated probability-generating function.

**2. Random limit and central limit theorem.** The expected infected fraction per triangle, conditional on \(U=u\), is
\[
g_\lambda(u)=\frac{p_1(u)+2p_2(u)}2=1-\frac{u+\lambda u^2}{1+\lambda}.
\]
An infinite coupling with one shared \(T\) and an independent collection of petal clocks makes the conditional strong law applicable, proving the almost-sure limit. The conditional classical central limit theorem for bounded, i.i.d. triangle counts, followed by dominated convergence of conditional characteristic functions, proves the stated joint mixed-Gaussian fluctuation limit. For the star, conditional on the same \(U\), each leaf is infected independently with probability \(1-U\), so its limiting infected fraction is \(1-U\). Subtracting the two limits yields \(\lambda U(1-U)/(1+\lambda)\), strictly positive on \(U\in(0,1)\).

**3. Exact mean and variances.** The moment identity
\[
\mathbb E[U^k]=\frac1{1+k\lambda}\qquad(k=0,1,2,\ldots)
\]
gives the claimed mean difference and the following rational functions:
\[
V_\triangle(\lambda)=\operatorname{Var}(g_\lambda(U))
=\frac{\lambda^2(12\lambda^5+60\lambda^4+100\lambda^3+58\lambda^2+13\lambda+1)}{(1+\lambda)^4(1+2\lambda)^2(1+3\lambda)(1+4\lambda)},
\]
\[
V_\star(\lambda)=\operatorname{Var}(1-U)=\frac{\lambda^2}{(1+\lambda)^2(1+2\lambda)}.
\]
Writing \(\sigma_\lambda^2(U)\) for the conditional variance of one triangle count, a direct use of the same moments gives
\[
\mathbb E[\sigma_\lambda^2(U)]
=\frac{2\lambda(6\lambda+1)(2\lambda^2+5\lambda+1)}{(1+\lambda)^2(1+2\lambda)(1+3\lambda)(1+4\lambda)}.
\]
The law of total variance yields, **exactly for every** \(m\),
\[
\begin{aligned}
\operatorname{Var}(Y_m^{\triangle})
 &=V_\triangle(\lambda)+\frac{\mathbb E[\sigma_\lambda^2(U)]}{4m},\\
\operatorname{Var}(Y_m^{\star})
 &=V_\star(\lambda)+\frac{\lambda}{2m(1+\lambda)(1+2\lambda)}.
\end{aligned}
\]
Subtracting and putting over a common denominator gives the announced formula in terms of \(Q_m\). Equivalently,
\[
\begin{aligned}
D_m(\lambda)&=D_\infty(\lambda)+\frac{B(\lambda)}m,\\
D_\infty(\lambda)&=-\frac{\lambda^3 P(\lambda)}{(1+\lambda)^4(1+2\lambda)^2(1+3\lambda)(1+4\lambda)},\\
B(\lambda)&=\frac{\lambda^2(13\lambda+3)}{2(1+\lambda)^2(1+2\lambda)(1+3\lambda)(1+4\lambda)}>0.
\end{aligned}
\]
These identities may also be checked by expanding \(g_\lambda(U)^2\) and \(p_1(U)+4p_2(U)\) using only moments through order four.

**4. Exactly one crossover for each size and monotone thresholds.** Expanding \(Q_m\) shows coefficient signs from highest degree to constant as \(+,+,-,-,-,-\) for every \(m\ge1\). By Descartes' rule there is at most one positive root. Since \(Q_m(0)=-3\) and its leading coefficient is \(24m>0\), it has exactly one. All denominators are positive for \(\lambda>0\), fixing the sign of \(D_m\) on either side. For \(m=1\), direct factorization gives
\[
Q_1(\lambda)=(2\lambda+3)(3\lambda+1)(4\lambda+1)(\lambda^2-2\lambda-1),
\]
so \(\lambda_1=1+\sqrt2\).

The limiting polynomial \(P\) likewise has one positive root by Descartes' rule (one sign change), with \(P(0)<0\) and positive leading term. Because \(B(\lambda)>0\), for each fixed positive \(\lambda\) the difference \(D_m(\lambda)\) decreases strictly in \(m\). At the unique root \(\lambda_m\), \(D_{m+1}(\lambda_m)<0\), hence \(\lambda_{m+1}<\lambda_m\). Moreover \(D_m(\lambda_\infty)=B(\lambda_\infty)/m>0\), so \(\lambda_m>\lambda_\infty\). The pointwise convergence \(D_m\to D_\infty\), together with the unique sign change, forces \(\lambda_m\downarrow\lambda_\infty\).

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The independent labeled-vertex SIR continuous-time Markov-chain first-step recursion enumerates reachable infection/recovery states without using the conditional-petal formula. It agrees coefficient-by-coefficient with the integrated finite generating function for all \(m=1,2,3,4\) and each \(\lambda\in\{1/2,1,2\}\): twelve exact rational distribution comparisons. It also checks normalization, means, finite variances, rational difference identities and representative crossover signs: 95 exact assertions in total. The calculation checks finite examples; the all-size and all-rate statements are proved by the preceding analytical argument, not by finite enumeration.

For illustration, at \(\lambda=1\) the limiting means are \(7/12\) (triangles) and \(1/2\) (star). The limiting variances are \(61/720\) and \(1/12\), respectively, so triangle closure increases both. At sufficiently high infection rates the variance ordering reverses, although the mean ordering does not.

## Relationship to prior work

Fransson and Trapman (first public arXiv version 2018-02-14) analyze SIR epidemics with clustering on *random configuration-model graphs* via branching-process approximations, including heterogeneous infectious periods. Their two-point large-population final-size theorem assumes the corresponding degree-distribution regime; it does not supply a continuous mixture limit for a deterministic friendship graph with a hub whose degree grows linearly with size, nor the star-versus-friendship variance threshold. The shared-infectiousness effect is established in that literature and is not claimed as new here.

McCulloch, Roberts and Laing (2019) derive final-size distributions for a **line of triangles**, using smaller network building blocks. Their earlier 2016 work already analyzes individual three- and four-vertex motifs. We do not claim novelty for the final-size law of a single triangle or for the general methodology of decomposing graphs into motifs. The distinguished statement is the all-size conditional mixture law on a **shared-hub** bouquet and the unique, strictly decreasing exact finite-size variance crossover. The 2019 paper's abstract and bibliographic record were accessible, but its full text was not successfully inspected, so possible stronger implicit coverage remains a priority risk. Other general exact Markov-chain methods can in principle compute each fixed graph but do not directly imply the stated all-size sign classification.

## Limitations

The comparison concerns a single initially infectious hub, a common infection rate on every edge, independent exponential recoveries of rate one, and disjoint pairs of leaves. The measure is the *final fraction ever infected*, not peak prevalence, extinction time or infection time. The limit holds for fixed \(\lambda>0\) as \(m\to\infty\), not for joint scaling of infection rate and graph size. The formulas are not asserted for other clustered graphs or infectious-period distributions. Historical novelty remains subject to independent literature review, especially the inaccessible 2019 full text. No independent mathematical audit is claimed.

## References

1. C. Fransson and P. Trapman, *SIR epidemics and vaccination on random graphs with clustering*, arXiv:1802.05011, first public version 2018-02-14, later *Journal of Mathematical Biology* **78** (2019), 2369–2398. https://arxiv.org/abs/1802.05011 ; https://doi.org/10.1007/s00285-019-01347-2
2. K. McCulloch, M. G. Roberts and C. R. Laing, *Generalised probability mass function for the final epidemic size of an SIR model on a line of triangles network*, *Mathematical Biosciences* **311** (2019), 49–61, first published online 2019-03-04. https://doi.org/10.1016/j.mbs.2019.02.003
3. K. McCulloch, M. G. Roberts and C. R. Laing, *Exact analytical expressions for the final epidemic size of an SIR model on small networks*, *ANZIAM Journal* **57** (2016), 429–444. https://doi.org/10.1017/S1446181116000043
