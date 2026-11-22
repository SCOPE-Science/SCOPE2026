# Pairwise independent outputs with a strict entropy-rate ceiling in a switched three-torus generator

## Finding

For the exact-real switched three-dimensional cat-map generator defined below, **every pair of distinct continuous outputs is independent uniform**, irrespective of the deterministic switching calendar. Every pair of its \(M\)-ary outputs is consequently independent and uniformly distributed. Nevertheless, under the natural stationary independent initialization, the output entropy rate has the strict cap

\[
h(d)\leq 1+\log_2\lambda_* =3.844829547729\ldots\text{ bits/sample},
\qquad \lambda_*=7.184210129198\ldots,
\]

where \(\lambda_*\) is the largest root of \(t^3-8t^2+6t-1\). For \(M=256\), each output has exactly eight bits of Shannon entropy, while the long-block entropy rate is **less than half** that amount. Further, any four selected continuous output coordinates at distinct times have a singular joint distribution on \([0,1)^4\), although every pair is independent uniform. This is a quantitative dependence phenomenon, not a claim of insecurity or a measurement of the exact output entropy rate.

## Assumptions and scope

The state space is \(\mathbb T^3\times[-1,1]\), with \(\mathbb T=\mathbb R/\mathbb Z\). The two independently evolving components are

\[
 X_{n+1}=AX_n\pmod{\mathbb Z^3},\qquad
 A=\begin{pmatrix}2&1&3\\3&2&5\\2&1&4\end{pmatrix},
 \qquad u_{n+1}=1-2u_n^2.
\]

The selector \(s_n\in\{0,1,2\}\) is the label of the partition of \([-1,1]\) at the two arcsine-law terciles, as in the generator's formula: three intervals each have invariant probability \(1/3\). Define \(b_n=(X_n)_{s_n}\in[0,1)\), and \(d_n=\lfloor M b_n\rfloor\), for any integer \(M\ge2\). Take \(X_0\) Haar uniform on \(\mathbb T^3\) and independent of \(u_0\); pairwise claims continue to hold for any fixed selector sequence independent of \(X_0\). For the entropy-rate bound choose \(u_0\) from the arcsine invariant measure \(du/(\pi\sqrt{1-u^2})\), independently of \(X_0\). Null endpoint ambiguities have no impact.

## Proof

**1. Integer matrix and stationary dynamics.** Direct integer expansion gives

\[
\det A=1,\qquad \det(tI-A)=t^3-8t^2+6t-1.
\]

The cubic has roots in \((0,3/10)\), \((1/2,3/5)\), and \((7,8)\), respectively, by signs and the intermediate value theorem. These are the only three roots, so \(A\) is hyperbolic with exactly one expanding eigenvalue \(\lambda_*\). The toral automorphism preserves Haar probability. The scalar quadratic map \(u\mapsto1-2u^2\) is conjugate, under \(u=-\cos(\pi t)\), to a full tent map up to orientation, so its arcsine probability is invariant and its metric entropy equals \(\log 2\).

**2. Exact two-time independence, for every selector calendar.** Fix \(0\le n<m\) and arbitrary prescribed labels \(i,j\in\{0,1,2\}\). The two observed coordinates are integer linear forms in \(X_0\), with row vectors \(e_i^{\mathsf T}A^n\) and \(e_j^{\mathsf T}A^m\). Multiplication on the right by the invertible integer matrix \(A^{-n}\) reduces their rank to that of \(e_i^{\mathsf T}\) and \(e_j^{\mathsf T}A^{m-n}\). Every entry of \(A\) is strictly positive, hence every entry of \(A^{m-n}\) is strictly positive, so the latter row is not proportional to the coordinate row \(e_i^{\mathsf T}\). Thus these two integer rows have rank two. Their torus homomorphism \(\mathbb T^3\to\mathbb T^2\) is surjective and pushes Haar measure to Haar measure. The corresponding coordinates are independent uniform. Conditioning on the independent selector calendar and then mixing identical product-uniform pair laws proves unconditional independence of \(b_n,b_m\); quantization gives the corresponding assertion for \(d_n,d_m\).

**3. Higher-order obstruction.** Condition on the four selector labels at any four distinct times. The map \(X_0\mapsto(b_{n_1},b_{n_2},b_{n_3},b_{n_4})\) is a torus homomorphism from dimension three to dimension four, so its image is a closed proper subtorus and has four-dimensional Haar measure zero. There are at most \(3^4\) possible label quadruples, hence their finite mixture is still singular. This argument concerns the unquantized observations only; it does not assert that every four-symbol quantized output is dependent.

**4. Entropy-rate ceiling.** Under independent Haar–arcsine initialization the product transformation is stationary. Its Kolmogorov–Sinai entropy is

\[
h_{\mathrm{KS}}(A\times T)=\sum_{|\lambda_i|>1}\log |\lambda_i|+\log2=\log\lambda_*+\log2.
\]

The \(M\)-ary output sequence is a stationary finite-partition factor of this product. Entropy monotonicity under factors yields

\[
\lim_{N\to\infty}\frac1N H(d_0,\ldots,d_{N-1})\le\log_2\lambda_*+1.
\]

As each \(d_n\) is uniform on \(M\) labels, \(H(d_n)=\log_2 M\). For \(M=256\), \(1+\log_2\lambda_*<4<8\). The eigenvalue enclosure and displayed numerical approximation are checked by the accompanying standalone arithmetic script. No finite simulation is used to infer a statement about arbitrarily long sequences.

## Verification

Run `python verify_cat.py` with Python 3 (standard library only). It reconstructs \(\det A\), \(\det(tI-A)\), positivity of the integer matrix, independent rank-two witness checks over prescribed times, rational root brackets and the numerical entropy ceiling. The infinite-time and all-calendar claims follow from Steps 1–4, not from finite checks. The script and text are distributed together.

## Relationship to prior work

Shi, Li, Jin and Li (2024) define precisely the displayed cat matrix, quadratic selector, equal-arcsine-mass partition, switched coordinate and integer quantizer, and investigate output uniformity, NIST tests and correlation numerically. Their accessible full article contains no proof of the pairwise-independence-for-all-calendars theorem or the strict entropy-rate ceiling. Theorems on entropy of hyperbolic toral automorphisms, entropy of the Chebyshev/tent map, and factor entropy monotonicity are standard; their use is not presented as a new general theorem.

Closest related published mathematical findings analyze quantized observations of a *different* two-dimensional trace-parameter cat map, and binary half-strip observations of a *different* three-torus matrix. Their mathematical conclusions are about different sensors and parameter-specific finite-block laws, not the stated switched-coordinate generator. None of the inspected accessible statements supplies the quantitative \(3.84483\)-bit limit for the 2024 generator. Since the underlying entropy method is classical, unindexed applications to precisely this system remain a publication-priority risk.

## Limitations

The claim is about ideal exact-real dynamics under a specified ensemble, not floating-point hardware, secret keys chosen adversarially, cryptanalytic security or the exact output entropy rate. The entropy bound need not be attained. Four-dimensional singularity applies to continuous coordinate outputs, not necessarily to four quantized labels. The published article's finite numerical examples do not independently certify the assumptions of the invariant ensemble. No independent mathematical audit has been performed.

## References

1. L. Shi, X. Li, B. Jin and Y. Li, *A Chaos-Based Encryption Algorithm to Protect the Security of Digital Artwork Images*, Mathematics **12** (2024), 3162, first published 2024-10-10, https://doi.org/10.3390/math12203162.
2. A. Katok and B. Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems*, Cambridge University Press (1995), chapters on toral automorphisms and metric entropy.
3. P. Walters, *An Introduction to Ergodic Theory*, Springer (1982), results on entropy of product transformations and measurable factors.
