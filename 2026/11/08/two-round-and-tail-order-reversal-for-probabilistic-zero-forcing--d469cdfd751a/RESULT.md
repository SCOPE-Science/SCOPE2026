# Two-round and tail-order reversal for probabilistic zero forcing on \(K_{2,b}\)

## Finding

**Theorem.** Let \(b\ge3\) be an integer, and let \(G=K_{2,b}\) have parts \(A\) and \(B\) of sizes \(2\) and \(b\). In synchronous probabilistic zero forcing, start from a single blue vertex. Write \(T_A\) for the time to color all vertices when the starting vertex is in \(A\) (the smaller part), and \(T_B\) when it is in \(B\) (the larger part). Then

\[
\Pr(T_A\le2)>\Pr(T_B\le2),
\qquad
\lim_{t\to\infty}\Pr(T_A>t)^{1/t}=\left(1-\frac1b\right)^b>\frac14
=\lim_{t\to\infty}\Pr(T_B>t)^{1/t}.
\]

More precisely, there are finite positive constants \(c_A(b),c_B(b)\) with
\[
\Pr(T_A>t)\sim c_A(b)\left(1-\frac1b\right)^{bt},\qquad
\Pr(T_B>t)\sim c_B(b)4^{-t}.
\]

Consequently, the smaller-part start is **more** likely to finish by round two, but the larger-part start is **more** likely to finish by every sufficiently large round. Neither completion-time law stochastically dominates the other. The first inequality is strict for every \(b\ge3\); for \(b=2\) the two laws agree by graph symmetry. No claim is made about how many times their distribution functions cross.

## Assumptions and scope

All graphs are finite, simple, unweighted, and undirected. At every round, a blue vertex \(u\) independently attempts to turn each white neighbor \(v\) blue with probability
\[
 p_{u\to v}=\frac{|N[u]\cap C|}{\deg(u)},
\]
where \(C\) is the set of blue vertices before the round, \(N[u]\) is the closed neighborhood, and simultaneous attempts act independently. A white vertex becomes blue if at least one attempt succeeds. Blue vertices remain blue. The random variable \(T\) counts completed synchronous rounds until all vertices are blue; \(T=0\) only if all vertices were blue initially, which does not occur here.

For state \((x,y)\), where \(x\) of the two vertices in \(A\) and \(y\) of the \(b\) vertices in \(B\) are blue, different white vertices in the same part are independently colored with probabilities
\[
 q_A(x,y)=1-\left(1-\frac{x+1}{2}\right)^y,
\qquad
 q_B(x,y)=1-\left(1-\frac{y+1}{b}\right)^x.
\]
These formulas are applied only if that part has remaining white vertices. The two increments have independent binomial laws conditional on the state. All powers with zero exponent are interpreted as one.

## Proof

### 1. Exact probability of completion at round two

No one-vertex start finishes in one round when \(b\ge3\). For a start in \(A\), the number \(J\) of newly blue vertices of \(B\) in round one is \(\operatorname{Bin}(b,1/b)\). If \(J=0\), round-two completion is impossible. If \(J=j\ge1\), the last white vertex in \(A\) is forced in round two with probability one, and each of the remaining \(b-j\) white vertices in \(B\) is forced independently with probability \((j+1)/b\). Hence
\[
 P_A(b):=\Pr(T_A\le2)=
 \sum_{j=1}^b {b\choose j}b^{-j}
 \left(\frac{b-1}{b}\right)^{b-j}
 \left(\frac{j+1}{b}\right)^{b-j}.
 \tag{1}
\]

For a start in \(B\), the number of blue vertices of \(A\) after round one is \(J\sim\operatorname{Bin}(2,1/2)\). The cases \(J=1\) and \(J=2\) have respective probabilities \(1/2\) and \(1/4\). In the former case the other \(A\) vertex is forced certainly and each remaining \(B\) vertex is forced with probability \(2/b\). In the latter case, each remaining \(B\) vertex is forced with probability \(1-(1-2/b)^2=4(b-1)/b^2\). Thus
\[
 P_B(b):=\Pr(T_B\le2)
 =\frac12\left(\frac2b\right)^{b-1}
 +\frac14\left(\frac{4(b-1)}{b^2}\right)^{b-1}.
 \tag{2}
\]

To show \(P_A(b)>P_B(b)\), first observe that
\[
 P_B(b)<\frac34\left(\frac4b\right)^{b-1}.
 \tag{3}
\]
For \(b=2m\), keep only the term \(j=m\) in (1). Since \({2m\choose m}\ge 2^{2m}/(2m+1)\) and \((2m-1)(m+1)/(2m)^2\ge1/2\),
\[
 P_A(2m)\ge \frac1{(2m+1)m^m}.
\]
Dividing by the right side of (3) gives the lower comparison
\[
 R_{\rm even}(m)=\frac{m^{m-1}}{3(2m+1)2^{2m-3}}.
\]
At \(m=7\), this exceeds one because \(7^6=117649>92160=3\cdot15\cdot2^{11}\). Moreover
\[
 \frac{R_{\rm even}(m+1)}{R_{\rm even}(m)}
 =\frac{m+1}{4}\left(1+\frac1m\right)^{m-1}\frac{2m+1}{2m+3}>1
 \qquad(m\ge7).
\]
Thus the desired strict inequality holds for all even \(b\ge14\).

For \(b=2m+1\), keep only \(j=m+1\) in (1). The central binomial coefficient is at least \(2^{2m+1}/(2m+2)\), while \(2m(m+2)/(2m+1)^2\ge1/2\). Therefore
\[
 P_A(2m+1)\ge\frac{2^m}{(m+1)(2m+1)^{m+1}}.
\]
Relative to (3) this gives
\[
 R_{\rm odd}(m)=\frac{4(2m+1)^{m-1}}{3(m+1)2^{3m}}.
\]
The value \(R_{\rm odd}(8)>1\), since \(4\cdot17^7>27\cdot2^{24}\). The ratio of successive lower bounds is
\[
 \frac{R_{\rm odd}(m+1)}{R_{\rm odd}(m)}
 =\frac{2m+3}{8}\left(1+\frac{2}{2m+1}\right)^{m-1}\frac{m+1}{m+2}>1
 \qquad(m\ge8).
\]
This proves the strict inequality for odd \(b\ge17\).

It remains to verify the finite range \(3\le b\le15\). Multiplication of (1) and (2) by \(b^{2b-1}\) yields the following integer difference:
\[
 \begin{split}
 D_b={}&\sum_{j=1}^{b}{b\choose j}
  ((b-1)(j+1))^{b-j}b^{j-1}\\
 &-2^{b-2}b^b-4^{b-2}(b-1)^{b-1}b.
 \end{split}
 \tag{4}
\]
The following exact values are all strictly positive (commas separate digits):

| \(b\) | \(D_b\) |
|---:|---:|
| 3 | 9 |
| 4 | 888 |
| 5 | 77,085 |
| 6 | 7,635,810 |
| 7 | 901,420,163 |
| 8 | 126,776,153,056 |
| 9 | 21,053,744,928,009 |
| 10 | 4,092,518,994,531,090 |
| 11 | 924,081,860,657,262,879 |
| 12 | 240,650,964,657,743,957,592 |
| 13 | 71,762,146,596,224,538,019,085 |
| 14 | 24,324,248,086,510,646,985,357,010 |
| 15 | 9,303,310,880,024,445,750,095,286,075 |

Together, the analytic bounds and this exact finite check prove \(P_A(b)>P_B(b)\) for every \(b\ge3\).

### 2. Exact late-time exponential rates

All nonabsorbing states accessible from either single-vertex start, apart from the starting state, have \(x\ge1\) and \(y\ge1\). If \(x=1\) and \(y\ge1\), the remaining \(A\) vertex is colored with probability one in the next round; hence that state's probability of remaining unchanged is zero. If \(x=2\) and \(1\le y<b\), put \(w=b-y\). Its no-change probability is
\[
 h_w=\left(\frac{w-1}{b}\right)^{2w},\qquad 1\le w\le b-1.
\]
For \(w=1\) this is zero. For \(2\le w<b/2\), \(h_w< (1/2)^{2w}\le1/16\). For \(w\ge b/2\), the base is at most \(1-2/b\), the exponent at least \(b\), and hence
\[
 h_w\le\left(1-\frac2b\right)^b\le e^{-2}<\frac14.
\]
Therefore **every** transient state reachable after leaving its initial singleton state has self-loop probability strictly below \(1/4\).

The singleton in \(A\) has self-loop probability
\[
 \lambda_A=\left(1-\frac1b\right)^b\ge\left(\frac23\right)^3=\frac8{27}>\frac14;
\]
the inequality follows because \((1-1/b)^b\) is increasing for integer \(b\ge2\). The singleton in \(B\) has self-loop probability \(\lambda_B=(1-1/2)^2=1/4\).

The finite-state transition matrix can be ordered by the number of blue vertices. It is upper triangular, since blue counts never decrease, and its diagonal is precisely the list of no-change probabilities. Thus the descendants of either starting state have all transient eigenvalues of modulus strictly below their starting \(\lambda\). Let \(G\) be the number of rounds until the first positive increase in the blue set and let \(H\) be the subsequent time to absorption. The variable \(G\) is geometric with \(\Pr(G>t)=\lambda^t\), and is independent of the post-exit state and \(H\) by the memoryless independent-round construction. Upper-triangular finite-state matrix powers give \(\Pr(H>t)=O(t^M\rho^t)\) for some finite \(M\) and \(\rho<\lambda\). Consequently \(\mathbb E[\lambda^{-H}]<\infty\) and
\[
 \frac{\Pr(G+H>t)}{\lambda^t}
 =\mathbb E\big[\lambda^{-H}\mathbf1_{\{H\le t\}}\big]
 +\lambda^{-t}\Pr(H>t)
 \longrightarrow\mathbb E[\lambda^{-H}]\in(0,\infty).
\]
This yields both stated exact exponential bases and strictly positive leading constants. Since \(\lambda_A>\lambda_B\), the survival probability from \(A\) is eventually strictly larger than from \(B\), proving the claimed eventual reversal.

## Verification

The standard-library script `check_pzf.py` reproduces equation (4) with exact integers for each \(3\le b\le15\), verifies the formula against independent labeled-vertex (not merely part-count) two-round dynamics for \(3\le b\le7\), and checks representative rational spectral comparisons and central-binomial bounds over additional finite parameter ranges. Execution command: `python3 check_pzf.py`. Observed output ended with `All tests passed.` For example, at \(b=3\) the two exact two-round probabilities are \(37/81\) and \(34/81\). The infinite part is the argument above, not an extrapolation from these computations.

## Relationship to prior work

Chan, Curl, Geneson, Hogben, Liu, Odegard and Ross (2019), §2.3, Proposition 2.5, describe the general complete-bipartite Markov transitions and their Table 2.4 contains *expected* propagation times for part sizes up to ten. Their Conjecture 2.6 concerns which part minimizes expected propagation time. Here the observable is the *entire time distribution*: the explicit two-round comparison points opposite to the eventual exponential-tail comparison. This result does not decide their expectation conjecture or contradict the tabulated expected times. The general transition mechanism is prior work; the all-parameter opposing time-horizon inequalities, sharp early test, and spectral-tail comparison are the present finding.

Geneson and Hogben (2018 preprint, later 2022 journal article) give foundational process definitions, bounds and examples for paths, cycles and stars. Narayanan and Sun (2019) and Hu and Sun (2020) establish propagation-time bounds for other graph families. No claim of global stochastic ordering is inferred from their expectation bounds.

## Limitations

The proof is limited to ordinary synchronous probabilistic zero forcing on \(K_{2,b}\) with \(b\ge3\) and a singleton initial seed. It does not prove an analogous crossover for all \(K_{a,b}\), identify the first late round at which the CDF order reverses, establish a single-crossing property, or settle any conjecture comparing expectations. The prior-art conclusion is based on the named inspected texts and targeted searches; historical priority and any stronger unlocated result remain subject to independent assessment.

## References

1. Y. Chan, E. Curl, J. Geneson, L. Hogben, K. Liu, I. Odegard, M. S. Ross, *Using Markov chains to determine expected propagation time for probabilistic zero forcing*, arXiv:1906.11083, first version June 25, 2019, §2.3, Proposition 2.5, Table 2.4 and Conjecture 2.6. https://arxiv.org/abs/1906.11083
2. J. Geneson and L. Hogben, *Propagation time for probabilistic zero forcing*, arXiv:1812.10476, first version December 24, 2018. https://arxiv.org/html/1812.10476v1
3. S. Narayanan and A. Sun, *Bounds on expected propagation time of probabilistic zero forcing*, arXiv:1909.04482, first version September 10, 2019. https://arxiv.org/abs/1909.04482
4. D. Hu and A. Sun, *Probabilistic Zero Forcing on Grid, Regular, and Hypercube Graphs*, arXiv:2010.12343, first version October 22, 2020. https://arxiv.org/abs/2010.12343
