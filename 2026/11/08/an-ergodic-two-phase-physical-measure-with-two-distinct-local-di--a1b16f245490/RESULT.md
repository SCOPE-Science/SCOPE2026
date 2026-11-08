# An ergodic two-phase physical measure with two distinct local dimensions for an erasing interval map

## Finding

Let \(F:[0,1]\to[0,1]\) be the model-case binary erasing interval map associated to
\[\rho(00)=\varepsilon,\qquad \rho(01)=1,\qquad \rho(10)=0,\qquad \rho(11)=01.\]
Let \(\lambda\) be normalized Lebesgue measure, \(\nu=F_*\lambda\), and
\[\boxed{\mu=\tfrac12(\lambda+\nu).}\]
The following conclusions hold simultaneously.

1. The measure \(\nu\) is the binary Markov measure with initial law \(\Pr(Y_1=0)=2/3\), \(\Pr(Y_1=1)=1/3\), and transition probabilities
\[\Pr(Y_{j+1}=Y_j\mid Y_j)=\tfrac13,\qquad \Pr(Y_{j+1}\ne Y_j\mid Y_j)=\tfrac23.\]
For every nonempty binary word \(w=w_1\cdots w_n\), therefore,
\[\boxed{\nu([w])=\frac{2^{\mathbf1_{\{w_1=0\}}+\#\{j<n:w_j\ne w_{j+1}\}}}{3^n}.}\]
This expression agrees with an earlier inverse-cylinder formula; the novelty claimed below does **not** include invention of those cylinder probabilities.

2. The probability \(\mu\) is \(F\)-invariant, ergodic and physical, and its basin has full Lebesgue measure. More precisely, for \(\lambda\)-almost every initial state \(x\), the empirical measures of its even and odd iterates converge weakly to \(\lambda\) and \(\nu\), respectively, and the full empirical measure converges weakly to \(\mu\).

3. The invariant ergodic physical probability \(\mu\) is neither absolutely continuous nor singular relative to \(\lambda\). It is **not exact-dimensional**. Its Euclidean pointwise local dimension exists \(\mu\)-almost everywhere, and has the exact two-atom distribution
\[\boxed{\mu\!\left\{x:\lim_{r\downarrow0}\frac{\log\mu(B(x,r))}{\log r}=1\right\}=\frac12,}\]
\[\boxed{\mu\!\left\{x:\lim_{r\downarrow0}\frac{\log\mu(B(x,r))}{\log r}=\log_2 3-\frac23\right\}=\frac12.}\]
The noninteger value is \(\log_2 3-2/3=0.9182958340544897\ldots\). These are distinct and exhaust \(\mu\)-almost every point.

## Assumptions and scope

The map \(F\) acts on the canonical nonterminating binary expansion of each nonzero real, by reading successive two-digit blocks and concatenating their \(\rho\)-images; on the countable exceptional set where this convention requires special treatment, use the convention in Corona–Della Corte (2023), Definition 2.2. None of the claims about measures or almost-sure trajectories depends on modifications on the dyadic exceptional set. The notation \([w]\) denotes the dyadic interval with initial binary word \(w\), ignoring its endpoints when necessary. The pushed-forward measure is \(F_*\lambda(A)=\lambda(F^{-1}A)\) on Borel sets. All limits of measures are weak convergence against bounded continuous test functions on \([0,1]\). The local dimension uses ordinary Euclidean balls intersected with \([0,1]\).

Two *published premises* are used rather than reproved: (i) \(F^2_*\lambda=\lambda\); and (ii) \(F^2\) is strongly mixing, hence ergodic, for \(\lambda\). Both are Theorems 2.4 and 3.4 of Corona–Della Corte (2023), respectively. The new calculations use these premises with a direct renewal analysis of the one-step image and local dimensions.

## Proof

**1. The exact one-step image.** Let \((X_j)_{j\ge1}\) be the binary digits of a \(\lambda\)-distributed point. These are independent fair bits. Let \(K_1<K_2<\cdots\) be the positions of the successive digits equal to \(1\). Almost surely this sequence is infinite. By the defining erasure rule, the \(j\)-th output bit is \(Y_j=\mathbf1_{\{K_j\text{ is even}\}}\). The variables \(K_1,K_2-K_1,K_3-K_2,\ldots\) are independent, each with \(\Pr(K=k)=2^{-k}\), \(k\ge1\). Thus \(\Pr(K\text{ odd})=\sum_{j\ge0}2^{-(2j+1)}=2/3\), while \(\Pr(K\text{ even})=1/3\). The output bit changes exactly when the next gap is odd. Independent geometric gaps therefore give the displayed Markov law and cylinder formula. This step is consistent with the stronger earlier cylinder-probability identity (38) of Della Corte–Isola–Piergallini (2021/2022), rather than asserting a new calculation of preimage masses.

The chain has transition matrix \(\bigl(\begin{smallmatrix}1/3&2/3\\2/3&1/3\end{smallmatrix}\bigr)\), which is irreducible and aperiodic. Its stationary distribution is \((1/2,1/2)\), and the empirical frequency of a flip converges to \(2/3\) for \(\nu\)-almost every output sequence. For \(\lambda\)-almost every binary sequence the corresponding flip frequency is \(1/2\). Hence \(\nu\perp\lambda\). Both measures are atomless, since every length-\(n\) cylinder has \(\nu\)-mass at most \((2/3)^n\).

**2. Invariance and ergodicity.** The published identity \((F^2)_*\lambda=\lambda\) implies \(F_*\nu=(F^2)_*\lambda=\lambda\); therefore \(F_*\mu=\mu\). If \(A\) is an \(F\)-invariant measurable set modulo \(\mu\), then it is also invariant under \(F^2\) modulo \(\lambda\) (because \(\lambda\ll\mu\)). Ergodicity of \(F^2\) for \(\lambda\) gives \(\lambda(A)\in\{0,1\}\). Further, \(\nu(A)=\lambda(F^{-1}A)=\lambda(A)\), because the symmetric difference between \(F^{-1}A\) and \(A\) has zero \(\lambda\)-mass. Therefore \(\mu(A)=\lambda(A)\in\{0,1\}\), proving ergodicity.

**3. Physicality and phase-resolved limits.** Since \(F^2\) preserves and is ergodic for \(\lambda\), the Birkhoff theorem applied simultaneously to a countable uniformly dense family of continuous test functions \(\varphi\) and to the bounded measurable functions \(\varphi\circ F\) yields, for \(\lambda\)-almost every \(x\),
\[\frac1N\sum_{k=0}^{N-1}\varphi(F^{2k}(x))\longrightarrow\int\varphi\,d\lambda,\qquad
\frac1N\sum_{k=0}^{N-1}\varphi(F^{2k+1}(x))\longrightarrow\int\varphi\circ F\,d\lambda=\int\varphi\,d\nu.\]
By uniform approximation these hold for all continuous \(\varphi\) on a common full-measure set. Averaging even and odd iterates gives convergence of the full empirical measures to \(\mu\), proving a full-Lebesgue physical basin.
The 2021 map \(R\) differs from \(F\) only at \(0\). Because \(\mu(\{0\})=0\), it is invariant under \(R\) as well; since every phase measure is atomless, Lebesgue-almost every orbit avoids \(0\) at every time, and the same physicality conclusion holds for \(R\). This directly supplies a non-atomic measure for the published Question 8.2.

**4. Two local dimensions.** For a length-\(n\) word \(w\), let \(J_n(w)=\#\{j<n:w_j\ne w_{j+1}\}\). The exact law from Step 1 gives
\[-\log\nu([w])=n\log3-(\mathbf1_{\{w_1=0\}}+J_n(w))\log2.\]
For \(\nu\)-almost every \(x\), the Markov ergodic theorem gives \(J_n(w(x))/n\to2/3\), hence
\[-\tfrac1n\log\nu([w(x)|_n])\to\log3-\tfrac23\log2<\log2.\]
For \(\lambda\)-almost every \(x\), the independent fair-digit law gives \(J_n(w(x))/n\to1/2\), hence
\[-\tfrac1n\log\nu([w(x)|_n])\to\log3-\tfrac12\log2>\log2.\]
Since \(\mu([w])=2^{-n-1}+\nu([w])/2\), its typical dyadic-cylinder exponent is accordingly \(\log3-\tfrac23\log2\) on the \(\nu\)-generic set and \(\log2\) on the \(\lambda\)-generic set.

It remains to justify *Euclidean ball*, rather than only cylinder, dimensions. Under either measure, the probability that the last \(k\) digits of a length-\(n\) prefix are all equal is at most \(2(2/3)^{k-1}\) (for \(\lambda\) the sharper \(2^{1-k}\) bound holds). Choose \(k=\lceil C\log n\rceil\) with \(C\) sufficiently large. The Borel–Cantelli lemma shows that eventually all terminal runs have length \(O(\log n)\). The length-\(n\) dyadic interval containing a typical point, together with its at most two adjacent intervals, covers its radius-\(2^{-n}\) Euclidean ball; the ball contains its own dyadic interval. Adjacent length-\(n\) binary words differ only in the carry region of length at most the terminal-run length plus one. Each change of one transition in the positive Markov cylinder formula multiplies its mass by a factor bounded between \(1/2\) and \(2\); consequently adjacent \(\nu\)-cylinder masses differ by a factor \(e^{O(\log n)}\), and adjacent \(\lambda\)-cylinder masses are equal. Therefore \(\mu(B(x,2^{-n}))\) and the central \(\mu\)-cylinder mass agree up to a factor \(e^{o(n)}\) for almost every \(x\) under both components. Comparing arbitrary radii with dyadic radii establishes the claimed Euclidean local dimensions. Finally \(\lambda\perp\nu\) from Step 1 gives the two dimensions \(\mu\)-masses exactly \(1/2\) each.

## Verification

The included independent-style, ordinary Python checker `verify_markov.py` uses exact rational arithmetic to compare the renewal-law formula with the older minimum-preimage-length formula for all \(2^n\) words of lengths \(1\le n\le10\), verifying normalization at each length. It also exhaustively enumerates binary inputs of length \(15\) and obtains exact lower bounds for all output words of lengths \(1\le n\le4\); the missing tails are bounded by the exact binomial probability of fewer than \(n\) ones. It checks the strict entropy inequalities. The checker reported `PASS 2090 exact arithmetic and finite-input checks`, with the dimension \(0.9182958340544897\). The almost-sure and invariant-measure assertions are proven analytically above, not inferred from finite tests.

## Relationship to prior work

Della Corte–Isola–Piergallini, *The simplest erasing substitution* (first public preprint February 2, 2021; published 2022), introduced the map, established its singularity and computed all Lebesgue inverse-cylinder probabilities in their equation (38). Those exact cylinder probabilities already determine the one-step image, so the present Markov cylinder expression is a transparent reformulation of that precedent, **not** an independent novelty claim. Their Question 8.2 asks whether the map admits non-atomic invariant measures.

Corona–Della Corte, *Mixing properties of erasing interval maps* (author-posted preprint February 5, 2023; published online March 6, 2023), established Lebesgue preservation and strong mixing for the square. Those facts are essential published premises here. Their results do not themselves state a one-step physical ergodic probability with its two-phase time statistics or the exact two-component Euclidean local-dimension distribution. The distinctive conclusion here is that the **same ergodic physical measure has an absolutely continuous part and a singular part whose typical local dimensions differ**. The proof is a synthesis of existing dynamics with a precise symbolic metric calculation; its novelty and value are narrower than a new mixing theorem.

## Limitations

The result does not classify all invariant probabilities, establish uniqueness of physical measures for non-Lebesgue reference initial distributions, determine metric entropy of the interval map, or establish a singular-continuous *purely singular* invariant measure. The map is densely discontinuous, so the phenomenon should not be taken as a theorem for smooth or Lipschitz interval transformations. Numerical checks on finite words are not a replacement for published Lebesgue preservation or mixing of the square. The pre-existing cylinder formula and general ergodic arguments make independent priority assessment of the *combined* theorem important.

## References

1. A. Della Corte, S. Isola, R. Piergallini, *The simplest erasing substitution*. arXiv:2102.01674 (2021 preprint; Nonlinearity 35 (2022), 4317–4356). Free manuscript: https://mat.unicam.it/piergallini/home/papers/erasingmap.pdf . Especially §5, equation (38), and Question 8.2.
2. D. Corona, A. Della Corte, *Mixing properties of erasing interval maps*. Ergodic Theory and Dynamical Systems 44 (2024), 408–431; DOI:10.1017/etds.2023.16 (online 2023). Free version: https://pubblicazioni.unicam.it/retrieve/e891bb2f-11bb-4aa7-92a6-55751c8ff3e9/2023c-CoronaDellaCorte-ETDS.pdf . Theorems 2.4 and 3.4.
