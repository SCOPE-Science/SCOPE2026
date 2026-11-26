# Exact harmonic-sector action of Walsh sampling on the odd middle layer

## Finding

Let \(n=2k+1\) with \(k\ge0\), and let \(V_r\) be the space of real functions on the \(r\)-subsets of \([n]\), with the counting inner product. Consider the unnormalized Walsh restriction matrix from degree \(j\) to the middle layer of weight \(k\):
\[
(W_{k,j}f)(x)=\sum_{|T|=j}(-1)^{|x\cap T|} f(T),\qquad |x|=k.
\]
Write \(H_\ell\) for the functions \(h\in V_\ell\) satisfying \(\sum_{R\supset I,\ |R|=\ell}h(R)=0\) for every \((\ell-1)\)-subset \(I\); take \(H_0=V_0\). Let \(E_{r,\ell}h(X)=\sum_{R\subseteq X,\,|R|=\ell}h(R)\) for \(|X|=r\). Then for \(0\le\ell\le j\le k\),
\[
W_{k,j}E_{j,\ell}h=\alpha_{k,j,\ell}E_{k,\ell}h,
\qquad
\alpha_{k,j,\ell}=(-2)^\ell(-1)^{\lfloor(j-\ell)/2\rfloor}
\binom{k-\ell}{\lfloor(j-\ell)/2\rfloor}.
\]
In particular, for \(0\le j\le k\), the singular values (one for each column dimension) are
\[
\left|\alpha_{k,j,\ell}\right|
\sqrt{\frac{\binom{n-2\ell}{k-\ell}}{\binom{n-2\ell}{j-\ell}}},
\qquad
\text{with multiplicity }\binom n\ell-\binom n{\ell-1},\quad 0\le\ell\le j,
\]
with multiplicities added when values coincide and \(\binom n{-1}=0\). For \(k<j\le n\), the singular values are those at degree \(n-j\). These are counting-norm singular values for a matrix with entries \(\pm1\), without normalization by the number of vertices or rows.

## Proof

Let \(U_r:V_r\to V_{r+1}\) sum over the \(r\)-subsets of an \((r+1)\)-set. Let \(D_{r+1}=U_r^*\), with \(D_0=0\). The commutator \(D_{r+1}U_r-U_{r-1}D_r=(n-2r)I\) follows by counting incidences: both operators have the same off-diagonal adjacency on \(r\)-sets differing in one element, and their diagonal counts are \(n-r\) and \(r\), respectively. Hence \(U_r\) is injective for \(r<k\), since \(\|U_rf\|^2=\|D_rf\|^2+(n-2r)\|f\|^2\). Splitting \(V_r\) as the image of \(U_{r-1}\) plus \(H_r=\ker D_r\), and using \(U_{r-1}E_{r-1,\ell}=(r-\ell)E_{r,\ell}\), gives the decomposition into the lifted sectors for \(r\le k\).

For \(h\in H_\ell\) let \(F_\ell=h\) and \(F_r=U_{r-1}F_{r-1}\); thus \(F_r=(r-\ell)!E_{r,\ell}h\). Induction from the commutator gives \(D_rF_r=(r-\ell)(n-r-\ell+1)F_{r-1}\) for \(r>\ell\): at each step the multiplier increases by \(n-2(r-1)\). Taking inner products and dividing by the squared factorial yields \(\|E_{r,\ell}h\|^2=\binom{n-2\ell}{r-\ell}\|h\|^2\). The lifted sectors are orthogonal: induct through the layers, using that \(D_rU_{r-1}\) acts by a scalar on each lifted sector at level \(r-1\), and that the newly added \(\ker D_r\) is orthogonal to the image of \(U_{r-1}\). Injectivity of \(U_{\ell-1}\) gives \(\dim H_\ell=\binom n\ell-\binom n{\ell-1}\), with the stated convention for \(\ell=0\).

To compute the action, substitute the inclusion lift into \(W_{k,j}\). The coefficient of \(h(R)\) for a fixed \(\ell\)-set \(R\) with \(t=|x\cap R|\) is
\[
f(t)=(-1)^t[z^{j-\ell}](1-z)^{k-t}(1+z)^{k+1-\ell+t}.
\]
Indeed, the remaining \(j-\ell\) elements of the column set are chosen from the \(k-t\) remaining elements in \(x\) and the \(k+1-\ell+t\) remaining elements outside it. Expand \(f(t)=\sum_{i=0}^\ell (\Delta^i f)(0)\binom ti\), by finite-difference interpolation on \(0,\ldots,\ell\). Repeated lowering shows that for any \(i<\ell\) and any \(i\)-set \(I\), the sum of \(h(R)\) over \(R\supseteq I\) is zero (the iterated lowering counts each extension \((\ell-i)!\) times). Consequently the terms with \(i<\ell\) cancel when summed over \(R\) against \(h(R)\). The surviving term is \((\Delta^\ell f)(0)E_{k,\ell}h(x)\).

In the alternating sum for the last difference the signs from \((-1)^t\) and from taking differences combine to \((-1)^\ell\). Factoring \((1-z)^{k-\ell}(1+z)^{k+1-\ell}\) leaves the binomial sum of \((1-z)^{\ell-t}(1+z)^t\), equal to \(2^\ell\). Thus the multiplier is \((-2)^\ell[z^{j-\ell}](1-z^2)^{k-\ell}(1+z)\), which gives the displayed coefficient for both parities of \(j-\ell\). The singular values now follow by normalizing the lifted norms on source and target in their orthogonal sector decompositions. For \(j>k\), the bijection \(T\mapsto T^c\) on column labels changes the Walsh sign by the common factor \((-1)^k\), so it preserves singular values.

## Verification

The included `verify.py` has finite integer tests of the sector action using explicit harmonic vectors, and finite modular tests of restriction ranks. These are supplementary; the coefficient and norm calculations above establish the spectrum, which is not checked by an all-dimensional computational certificate.

## Relationship to prior work and limitations

The optimum actuator count and odd-layer controllability for the binary hypercube were already established in [*Sharp central-shell actuator placement for Boolean hypercube control*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-central-shell-actuator-placement-for-boolean-hypercube-con--876293fe84cf). Its odd-layer proof propagates vanishing via incidence-map injectivity; it does not give the response on individual harmonic sectors. No novelty for that count or for odd-layer injectivity is claimed here. The slice harmonic decomposition is prior framework; see Filmus [arXiv:1406.0142](https://arxiv.org/abs/1406.0142) and Filmus–Mossel [arXiv:1507.02713](https://arxiv.org/abs/1507.02713). The specific calculation here is the closed action of the Walsh sampling map between two distinct layers in that framework. The singular values quantify amplification of coefficient perturbations under sampling and, through the least singular value, the stability of inverting this full-column-rank restriction. The theorem concerns one odd middle row layer and one homogeneous Walsh degree at a time; it does not claim injectivity for arbitrary mixtures of degrees or give a spectrum for arbitrary layers or weighted sampling. Historical priority over equivalent transform formulas remains provisional.
