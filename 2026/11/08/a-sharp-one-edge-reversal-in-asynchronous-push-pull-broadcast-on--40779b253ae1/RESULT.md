# A sharp one-edge reversal in asynchronous push–pull broadcast on stars

## Finding
Let \(m\ge 2\), let \(S_m=K_{1,m}\) be the star with hub \(0\) and leaves \(1,\ldots,m\), and let \(G_m=S_m+\{1,2\}\), obtained by adding an edge between leaves \(1\) and \(2\). Start the continuous-time asynchronous push–pull protocol with the rumour at leaf \(1\). Write \(T_m^{\rm star}\) and \(T_m^{\rm edge}\) for the corresponding times until every vertex knows the rumour.

**Theorem.** Put
\[
 \lambda_m=\frac{m+1}{m},\qquad h_m=\frac{m+2}{2m},\qquad c_m=\frac{3m+2}{2m},\qquad H_j=\sum_{i=1}^{j}\frac1i\quad (H_0=0),
\]
\[
 F_m=\prod_{i=1}^{m-2}\frac{2i(m+1)}{2i(m+1)+3m+2},\qquad F_2=1.
\]
Then
\[
 \mathbb E T_m^{\rm star}=\frac{1+H_{m-1}}{\lambda_m},
\]
\[
 \mathbb E T_m^{\rm edge}=
 \frac{1}{1+h_m}+\frac{H_{m-2}}{\lambda_m}
 +\frac{h_mF_m}{(1+h_m)c_m}
 +\frac{1}{(1+h_m)2h_m}.
\]
Consequently, the exact edge-addition difference \(\Delta_m=\mathbb E T_m^{\rm edge}-\mathbb E T_m^{\rm star}\) satisfies
\[
\Delta_m<0\quad(m=2,3,4),\qquad \Delta_m>0\quad(m\ge5),\qquad\lim_{m\to\infty}\Delta_m=\frac13.
\]
Thus adding an edge between the informed leaf and another leaf reduces expected completion time in stars with two through four leaves, but **increases** expected completion time for every star with at least five leaves. The first reversal *within this star family* is the six-vertex case \(m=5\), with
\[
\Delta_5=\frac{20155225}{3059601384}>0.
\]

## Assumptions and scope
All graphs are finite, undirected, simple, and unweighted. Each vertex carries an independent rate-one Poisson clock. When its clock rings, it calls a uniformly chosen neighbor; if exactly one knows the rumour, the other becomes informed. The rumour never disappears, and the source is always the specified leaf \(1\), rather than a uniformly sampled source. The completion time is measured in continuous time. The result holds for every integer \(m\ge2\). It is not a universal first-minimality claim over all connected graphs.

## Proof

**Independent crossing-edge clocks.** Splitting each vertex's rate-one calling clock into independent directed-edge Poisson processes shows that the undirected edge \(\{u,v\}\) produces information exchange at rate \(d(u)^{-1}+d(v)^{-1}\). Processes on distinct undirected edges are independent. At a newly infected state the unrevealed future of these clocks is independent and exponential. This is the established exponential-edge representation of the asynchronous push–pull protocol [2, Proposition 13].

**Star.** Every edge of \(S_m\) exchanges information at rate \(\lambda_m=1+1/m\). The source-to-hub transmission time is exponential of rate \(\lambda_m\). Afterward the other \(m-1\) leaves independently receive the rumour at the same rate. The maximum of \(j\) independent rate-\(\lambda_m\) exponential waiting times has mean \(H_j/\lambda_m\), by the standard order-statistic spacings identity. This gives the first displayed expectation formula.

**Added edge.** In \(G_m\), both distinguished leaves have degree two, the hub degree \(m\), and the remaining leaves degree one. Before the hub is informed, two possible infection events compete: hub infection across \(\{0,1\}\) at rate \(h_m=1/2+1/m\), and distinguished leaf \(2\) infection across \(\{1,2\}\) at rate \(1\). The first-event time is exponential of rate \(1+h_m\), and the respective first-event probabilities are \(h_m/(1+h_m)\) and \(1/(1+h_m)\).

If leaf \(2\) becomes informed first, both distinguished leaves then transmit to the hub independently at rate \(h_m\), giving an additional mean waiting time \(1/(2h_m)\). After hub infection, the other \(m-2\) ordinary leaves are informed in independent rate-\(\lambda_m\) times, whose maximum has mean \(H_{m-2}/\lambda_m\).

If the hub becomes informed first, the rate at which distinguished leaf \(2\) becomes informed is \(c_m=h_m+1\), contributed by the hub and source leaf. The \(m-2\) ordinary leaves have independent rate-\(\lambda_m\) completion times. Let \(Y\) be their maximum and \(Z\) an independent rate-\(c_m\) exponential. Conditional on \(Y\), the expected excess of \(Z\) over \(Y\) is \(e^{-c_mY}/c_m\). Thus
\[
\mathbb E\max(Y,Z)=\frac{H_{m-2}}{\lambda_m}+\frac{\mathbb E e^{-c_mY}}{c_m}.
\]
For \(j=m-2\), the maximum's Laplace transform is
\[
\mathbb E e^{-c_mY}=\prod_{i=1}^{j}\frac{i\lambda_m}{i\lambda_m+c_m}=F_m,
\]
including \(j=0\) by the empty-product convention. This follows either from the independent exponential spacings of the maximum, or by integrating its CDF \((1-e^{-\lambda_mt})^j\). Weighting both cases by their first-event probabilities and adding the initial wait proves the formula for \(\mathbb E T_m^{\rm edge}\).

**Sharp sign boundary.** Subtract the star formula, noting \(H_{m-1}=H_{m-2}+1/(m-1)\). The difference may be written compactly as
\[
\Delta_m=\frac{1+(2h_m)^{-1}+h_mF_m/c_m}{1+h_m}
 -\frac{1+(m-1)^{-1}}{\lambda_m}.
\]
Clearing positive denominators gives the exact identity
\[
 \Delta_m=\frac{m\{P(m)+2F_mQ(m)\}}{(m-1)(m+1)(m+2)(3m+2)^2},
\]
where
\[
P(m)=3m^4-10m^3-32m^2-28m-8,\qquad
Q(m)=m^4+4m^3+3m^2-4m-4.
\]
For \(m\ge2\), \(Q(m)>0\) (its value at \(2\) is \(48\), its derivative is positive and increasing thereafter). For \(m\ge6\), \(P(m)>0\) because \(P(6)=400\), \(P'(6)=1100\), and \(P''(m)>0\) for \(m\ge6\). As \(F_m>0\), the difference is strictly positive for all \(m\ge6\). The four remaining values are determined exactly:
\[
\Delta_2=-\frac13,\quad
\Delta_3=-\frac{13599}{91960},\quad
\Delta_4=-\frac{226}{4165},\quad
\Delta_5=\frac{20155225}{3059601384}.
\]
This proves the sharp threshold.

**Asymptotic gap.** Since \(c_m/\lambda_m=(3m+2)/(2m+2)>1\), each factor of \(F_m=\prod_{i=1}^{m-2}i/(i+c_m/\lambda_m)\) is at most \(i/(i+1)\), whence \(0<F_m\le1/(m-1)\). The polynomial difference formula therefore has \(m^{-5}\) leading numerator and denominator coefficients \(3\) and \(9\), respectively, and its term containing \(F_m\) vanishes in the limit. Thus \(\Delta_m\to1/3\). This completes the proof.

## Verification
Run the standalone standard-library certificate `verify.py` using Python 3. It independently computes exact mean absorption times by enumerating informed-vertex subsets and solving the acyclic first-step recursion for **each labeled graph**, without assuming the displayed closed form. It compares the resulting rational means with the theorem for both graphs for all \(2\le m\le11\) (20 graph instances), checks the product and the polynomial identities for \(2\le m\le14\), checks the four boundary fractions and signs, and checks polynomial properties. The infinite claim is proved by the preceding algebra, not by finite verification.

Reproducible output includes \(\Delta_4=-226/4165\), \(\Delta_5=20155225/3059601384\), and the checker's `PASS` summary. A numerical approximation or simulation is unnecessary for these identities.

## Relationship to prior work
Daknama, Panagiotou, and Reisser [1] investigated *robustness under graph modifications* for the synchronous push, pull and push–pull processes, particularly deletions from expander sequences and transmission failures. Their round-based asymptotic resilience bounds neither evaluate this continuous-time star-with-one-added-edge model nor entail its exact mean-time sign transition. The present finding addresses a parallel finite-graph robustness question with a different update clock and a fully explicit sharp threshold.

Acan, Collevecchio, Mehrabian, and Wormald [2] establish the asynchronous Poisson-clock model, prove the independent exponential-edge representation (Proposition 13), and analyze ordinary stars and other families. Their general representation is used openly here; the two-case formula for a triangle-ended star, the nontrivial finite threshold and the limiting positive penalty are additional derived results, not quoted from [2]. Doerr and Kostrygin [3] analyze predominantly round-based protocols on complete networks, which does not imply the fixed sparse-graph comparison. Nearby deterministic burning/threshold-spreading comparisons concern different processes.

## Limitations
This result compares expected **full completion times**, not the entire completion-time distributions, high-probability runtimes, optimal source placement, or other graph-edit operations. The new edge must join the original source leaf to one other leaf. For the alternative initial source at an ordinary leaf or at the hub, the statement needs new analysis. Historical originality is assessed from accessible published material and search results, not certified by universal absence of prior work. No independent mathematical audit is claimed.

## References
[1] R. Daknama, K. Panagiotou, and S. Reisser, *Robustness of Randomized Rumour Spreading*, arXiv:1902.07618, initially public 20 February 2019, https://arxiv.org/abs/1902.07618 ; full text https://arxiv.org/html/1902.07618v2 .

[2] H. Acan, A. Collevecchio, A. Mehrabian, and N. Wormald, *On the push&pull protocol for rumour spreading*, arXiv:1411.0948, initially public 4 November 2014, https://arxiv.org/abs/1411.0948 .

[3] B. Doerr and A. Kostrygin, *Randomized Rumor Spreading Revisited (Long Version)*, arXiv:2303.11150, initially public 20 March 2023, https://arxiv.org/abs/2303.11150 .
