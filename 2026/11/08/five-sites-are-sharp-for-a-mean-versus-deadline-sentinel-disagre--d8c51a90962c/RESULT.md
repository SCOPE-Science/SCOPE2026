# Five sites are sharp for a mean-versus-deadline sentinel disagreement in SI surveillance

## Finding

Consider the irreversible continuous-time susceptible--infected (SI) process with one uniformly random infected source on an unweighted path, independent rate-one transmission across each active infected--susceptible edge, and two distinct, perfect, continuously observed sentinel vertices. Write \(T_S\) for the first infection time of either sentinel in a pair \(S\). For every positive deadline \(t\), minimize \(Q_S(t)=\Pr(T_S>t)\), and separately minimize \(\mathbb E[T_S]\). Among paths with at least two vertices, the five-vertex path is the smallest for which a deadline-optimal two-sentinel pair is not mean-optimal.

For the five-vertex path \(0-1-2-3-4\), put \(x=t\) (or \(x=\lambda t\) for any homogeneous transmission rate \(\lambda>0\)). Let \(\xi\) and \(\eta\) be the unique strictly positive solutions of
\[
 e^{\xi}=1+2\xi,\qquad e^{\eta}=1+2\eta+2\eta^2.
\]
Then \(0<\xi<\eta\), with \(\xi\approx1.25643120862617\) and \(\eta\approx3.46288587294379\). The complete deadline-optimal placement classification for \(t>0\) is:

- \(0<x<\xi\): uniquely \(S=\{1,3\}\).
- \(x=\xi\): exactly \(S=\{1,3\},\{0,3\},\{1,4\}\).
- \(\xi<x<\eta\): exactly \(S=\{0,3\},\{1,4\}\).
- \(x=\eta\): exactly \(S=\{0,3\},\{1,4\},\{0,4\}\).
- \(x>\eta\): uniquely \(S=\{0,4\}\).

The complete mean-optimal set on that path is \(\{1,3\},\{0,3\},\{1,4\}\), each with mean delay \(1/2\). The eventual deadline-optimal pair \(\{0,4\}\) has mean delay \(3/5\), exceeding that minimum by \(1/10\), or \(20\%\). At four vertices, although the deadline-optimal pair switches, every deadline optimum is mean-optimal. Thus five vertices are sharp for the *different* criterion of disagreement with mean-optimality; switching of deadline-optimal placements alone occurs earlier.

## Assumptions and scope

Paths are simple, undirected, with vertices \(\{0,\ldots,n-1\}\), unit transmission rates on each infected--susceptible edge, no recovery or spontaneous infections, and exactly one initial infected source chosen uniformly and independently of the edge-clock processes. Sentinel infection is observed without delay, including detection at time zero when the source is monitored. All statements are exact for \(n\in\{2,3,4,5\}\), and the full deadline phase diagram is given only for \(n=5\). Other graph topologies, nonuniform source distributions, and recovery dynamics are not covered.

## Proof

**First-passage decomposition.** Fix a source \(i\notin S\). If there is a nearest sentinel \(a<i\) to the left, its arrival time is a sum of \(i-a\) independent \(\operatorname{Exp}(1)\) variables; similarly the right-nearest sentinel \(b>i\) is reached after a sum of \(b-i\) independent exponentials. The two passages use disjoint edges and independent clocks until detection. Their minimum gives \(T_S\). If a direction contains no sentinel, that direction contributes a survival factor of one. Writing
\[
 H_d(t)=e^{-t}\sum_{j=0}^{d-1}\frac{t^j}{j!}\quad(d\ge1),\qquad H_{\infty}(t)=1,
\]
we therefore have the exact all-time identity
\[
 Q_S(t)=\frac1n\sum_{i\notin S}H_{i-a(i)}(t)H_{b(i)-i}(t),
\]
where a missing nearest left or right sentinel means infinite distance. The expectation equals \(\int_0^\infty Q_S(t)\,dt\). This also follows from the first-event equations for the SI interval endpoints.

**Five-vertex exhaustive expressions.** Reflection leaves six pair types. Put \(z=e^{-t}\). Direct substitution in the identity gives:

| Representative pair | \(5e^{2t}Q_S(t)\) | \(\mathbb E[T_S]\) |
|---|---|---|
| \(\{1,3\}\) | \(2e^t+1\) | \(1/2\) |
| \(\{0,3\}\) | \(e^t+2t+2\) | \(1/2\) |
| \(\{0,4\}\) | \(2t^2+4t+3\) | \(3/5\) |
| \(\{0,2\}\) | \((t+2)e^t+1\) | \(7/10\) |
| \(\{1,2\}\) | \((t+3)e^t\) | \(4/5\) |
| \(\{0,1\}\) | \((t^2+4t+6)e^t/2\) | \(6/5\) |

The reflection of \(\{0,3\}\) is \(\{1,4\}\); the reflection of \(\{0,2\}\) is \(\{2,4\}\); the reflection of \(\{1,2\}\) is \(\{2,3\}\); and the reflection of \(\{0,1\}\) is \(\{3,4\}\).

For \(t>0\), the \(\{1,3\}\) row strictly beats each of the last three rows. After multiplication by the common positive factor \(5e^{2t}\), their respective differences from the \(\{1,3\}\) row are \(te^t\), \((t+1)e^t-1\), and \((1+2t+t^2/2)e^t-1\), all strictly positive. Consequently, only the first three pair types can minimize the deadline tail.

Write \(B=\{1,3\}\), \(A=\{0,3\}\) or its reflection, and \(C=\{0,4\}\). The signs of the two relevant comparisons are
\[
 5e^{2t}(Q_A-Q_B)=1+2t-e^t,
 \qquad 5e^{2t}(Q_A-Q_C)=e^t-1-2t-2t^2.
\]
The function \(e^t-1-2t\) has derivative \(e^t-2\), which changes sign once from negative to positive, and hence exactly one positive zero \(\xi\). The function \(e^t-1-2t-2t^2\) has second derivative \(e^t-4\), increasing strictly from a negative value to positive; its first derivative starts negative and then has exactly one positive zero, so the function likewise has exactly one positive zero \(\eta\). At \(t=\xi\), the second function is \(-2\xi^2<0\), proving \(\xi<\eta\). The displayed comparisons then give the full five-case phase classification, including equality endpoints. Integrating the six displayed survival functions gives exactly the stated means.

**Sharpness for smaller paths.** On \(P_2\), both vertices are monitored and \(T_S=0\). On \(P_3\), the endpoint pair \(\{0,2\}\) has survival \(e^{-2t}/3\) and mean \(1/6\); either adjacent pair has survival \(e^{-t}/3\) and mean \(1/3\). Thus the endpoint pair is both the unique deadline optimum for \(t>0\) and unique mean optimum. On \(P_4\), reflection reduces the four pair types to
\[
 \begin{array}{c|c|c}
 S & 4e^{2t}Q_S(t)&\mathbb E[T_S]\\ \hline
 \{0,1\}&(t+2)e^t&3/4\\
 \{0,2\}&e^t+1&3/8\\
 \{0,3\}&2(t+1)&3/8\\
 \{1,2\}&2e^t&1/2
 \end{array}
\]
The first and last rows are strictly dominated by \(\{0,2\}\) at each \(t>0\), because their respective differences in the middle column are \((t+1)e^t-1>0\) and \(e^t-1>0\). The only deadline optima are therefore \(\{0,2\},\{1,3\},\{0,3\}\), which all minimize the mean. This proves the claimed minimality of five vertices.

## Verification

The accompanying `verify.py` uses a separate finite-state interval SI Markov recurrence, rather than the gamma-tail decomposition, to compute exact rational mean hitting times and rational Laplace transforms of the survival function. It compares every two-sentinel pair on \(P_2,P_3,P_4,P_5\) to the independent closed-form transform at four positive rational Laplace parameters, totaling 80 exact comparisons. It additionally checks the six rational mean classes and both lower-order sharpness conditions. The standalone command `python3 verify.py` produced `PASS 80 independent rational Laplace comparisons; all exact mean classes and sharp minima`. The all-continuum phase classification is proved by the sign arguments above, not by finite computations.

## Relationship to prior work

Leskovec, Krause, Guestrin, Faloutsos, VanBriesen and Glance (2007) formulate broadly applicable outbreak-detection objectives and near-optimal selection by submodularity. Their full technical report establishes the generic objective class and algorithm but not this exact rate-one SI five-path three-regime law or the minimal mean-versus-deadline separation. Zhou, Shi, Zang and Guo (2015) study efficient sensor placement for early outbreak detection on mobile networks using heuristic approaches; the accessible abstract does not imply an analytic exact path classification. The four-site deadline switch is directly recovered from the explicit smaller-path formulas above, and is not itself the claimed new distinction: it does not produce a mean-versus-deadline conflict or the three distinct \(P_5\) regimes. The present claim concerns precisely those additional distinctions, and is not a general novelty claim about objective tradeoffs, early warning, or sentinel-placement algorithms.

## Limitations

The five-site result is a sharply defined theoretical benchmark, not an empirical forecast or a claim of new generic approximation algorithms. The smallest-network conclusion concerns **path networks and two perfect sensors** only. Priority assessment is based on inspected accessible literature and records; relevant unpublished or unindexed exact small-path tables cannot be excluded. Full-text access to the plausible 2015 conference paper was unavailable, and its detailed examples remain a residual priority risk. The 2007 technical report gives only a month-level date (June 2007); the exact dated conference opening of August 12, 2007 serves as a documented day-level public-source anchor without inventing a day in June.

## References

1. J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen and N. Glance, *Cost-effective Outbreak Detection in Networks*, technical report CMU-ML-07-111, June 2007, and KDD 2007, August 12--15, 2007. https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf ; https://doi.org/10.1145/1281192.1281239
2. C. Zhou, R. Shi, W. Zang and L. Guo, *Efficient Sensor Placement Optimization for Early Detection of Contagious Outbreaks in Mobile Social Networks*, IEEE Mobile Services 2015, pp. 261--268. https://doi.org/10.1109/MobServ.2015.45
3. J. Heavey, J. Cui, C. Chen, B. A. Prakash and A. Vullikanti, *Provable Sensor Sets for Epidemic Detection over Networks with Minimum Delay*, AAAI 2022. https://doi.org/10.1609/aaai.v36i9.21260
