# Square-length dark-state resonance at the second interior detector of a perfect-transfer spin chain

## Finding
For a one-excitation perfect-transfer spin chain with \(d+1\) sites, a single irreversible detector at the second interior site can fail to capture the excitation *exactly when the number \(d\) of hopping links is a perfect square*. The failure is caused by two strictly undamped coherent eigenmodes. Adding an independent detector at the first interior site eliminates both modes and restores eventual capture for every initial state.

Precisely, for each integer \(d\ge3\) and real \(J\ne0\), let \(H_d\) act on the orthonormal vertex basis \(\{|j\rangle:0\le j\le d\}\) by
\[
H_d|j\rangle=J\sqrt{j(d-j+1)}|j-1\rangle+J\sqrt{(j+1)(d-j)}|j+1\rangle,
\]
where out-of-range terms are zero. For a set \(T\subseteq\{1,2\}\) of independent absorbing vertices with rates \(\gamma_a>0\), the no-jump generator is \(H_{\mathrm{eff}}=H_d-i\sum_{a\in T}\gamma_a|a\rangle\langle a|\). The capture probability of an initial density matrix \(\rho\) is
\[
\eta_T(\rho)=1-\operatorname{Tr}(P_T\rho),
\quad P_T=\sum_{k:\,K_a(k;d)=0\;\forall a\in T}|v_k\rangle\langle v_k|,
\]
with the eigenvectors and polynomials defined below.

For \(T=\{2\}\), \(\operatorname{rank}P_T=2\) if \(d=s^2\) for integer \(s\ge2\), and is zero otherwise. At a perfect square, the two undamped energy levels are \(\pm Js\), and the initially localized endpoint state has
\[
\eta_{\{2\}}(|0\rangle\langle0|)=1-\frac{2\binom{d}{(d-s)/2}}{2^d}.
\]
For \(T=\{1\}\), the rank is one for even \(d\), and zero for odd \(d\); at even \(d\), endpoint capture is \(1-2^{-d}\binom d{d/2}\). For \(T=\{1,2\}\), the dark projector is identically zero. All statements hold for arbitrary *strictly positive* independent detector strengths.

For example, with nine links (ten sites) and a sole detector at vertex two, endpoint capture is \(1-168/512=43/64\). The square-length endpoint survival fraction obeys
\[
\frac{2\binom{d}{(d-\sqrt d)/2}}{2^d}\sim 2e^{-1/2}\sqrt{\frac{2}{\pi d}}
\quad(d=s^2\to\infty).
\]

## Assumptions and scope
The model is the *one-excitation sector* of an engineered XX chain, or equivalently a single particle on a weighted path. All coherent hopping magnitudes are those given above; there are no extra position-dependent diagonal potentials, coherent jumps between detectors, dephasing, or unmodelled loss channels. Each detector in \(T\) couples to its own irreversible sink with a positive rate, represented by the no-jump Hamiltonian above. A common overall energy shift of \(H_d\) does not affect the conclusion. The claim concerns asymptotic capture as time tends to infinity, not finite-time collection rates.

## Proof
For integers \(0\le j,k\le d\), define the binary Krawtchouk polynomial
\[
K_j(k;d)=\sum_{a=0}^j(-1)^a\binom{k}{a}\binom{d-k}{j-a},
\]
using the convention that a binomial coefficient outside its natural range vanishes. The generating identity \(\sum_jK_j(k;d)z^j=(1-z)^k(1+z)^{d-k}\) yields the three-term recurrence
\[
(j+1)K_{j+1}(k;d)+(d-j+1)K_{j-1}(k;d)=(d-2k)K_j(k;d).
\]
By the binomial orthogonality identity, the vectors
\[
\langle j|v_k\rangle=\sqrt{\frac{\binom dk}{2^d\binom dj}}K_j(k;d)
\]
form an orthonormal basis. The recurrence proves \(H_d|v_k\rangle=J(d-2k)|v_k\rangle\), so the \(d+1\) eigenvalues are distinct when \(J\ne0\). The endpoint weight is \(|\langle0|v_k\rangle|^2=2^{-d}\binom dk\).

Let \(\Gamma=\sum_{a\in T}\gamma_a|a\rangle\langle a|\). The no-jump evolution is \(U(t)=e^{-i(H_d-i\Gamma)t}\). Its squared norm has derivative \(\frac{d}{dt}\|U(t)\psi\|^2=-2\langle U(t)\psi,\Gamma U(t)\psi\rangle\le0\). If a right eigenvector of \(H_d-i\Gamma\) has a real eigenvalue, taking the imaginary part of its expectation forces \(\langle\psi,\Gamma\psi\rangle=0\); since every \(\gamma_a\) is strictly positive, that eigenvector vanishes at every absorbing site and is a genuine eigenvector of \(H_d\). Conversely every such eigenvector of \(H_d\) is stationary up to a phase and is strictly dark. Because \(H_d\) has a simple real spectrum, its dark span is exactly the sum of those Krawtchouk eigenlines satisfying all detector zero conditions. The orthogonal complementary subspace has strictly negative imaginary spectrum for \(H_d-i\Gamma\) and hence decays to zero, also in the presence of Jordan blocks. This proves \(\eta_T(\rho)=1-\operatorname{Tr}(P_T\rho)\) for arbitrary density matrices.

The first two polynomials are \(K_1(k;d)=d-2k\) and \(K_2(k;d)=((d-2k)^2-d)/2\). Thus the first detector is blind to the central eigenvector exactly when \(d\) is even. The second is blind precisely when \((d-2k)^2=d\). For an integer spectral label \(k\in[0,d]\), this has exactly two solutions \(k=(d\pm s)/2\) if and only if \(d=s^2\); for every square \(d\ge4\), these labels are integral because \(s^2\equiv s\pmod2\). Their energies are \(\mp Js\). The two zero conditions cannot hold simultaneously because \(d-2k=0\) would make \(K_2=-d/2\ne0\). Therefore \(T=\{1,2\}\) has no dark eigenvectors.

The exact endpoint probability follows by summing the binomial weights of the dark indices. The square-limit estimate follows from the de Moivre–Laplace local limit formula for the binomial law at an offset of one standard deviation. This completes all stated cases.

## Verification
The accompanying `verify.py` independently constructs the integer Krawtchouk sums, checks their recurrence in rational arithmetic for all \(2\le d\le60\), tests binomial orthogonality for \(2\le d\le18\), and compares the zero sets and endpoint survival probabilities with the claimed closed forms. A separate numerical diagonalization of the complex dissipative matrix checks the dark-eigenvalue counts for eight dimensions, three loss strengths, and three detector sets. The calculation returns `EXACT_KRAWTCHOUK_OK`, `INDEPENDENT_DISSIPATIVE_SPECTRUM_OK`, and the predicted endpoint survival values. These finite tests are checks of—not replacements for—the all-dimension proof.

## Relationship to prior work
Christandl, Datta, Ekert and Landahl (2003/2004) introduce the engineered perfect-transfer chain; Vinet and Zhedanov (2011/2012, section V) explicitly identify its binomial spectral weights and Krawtchouk eigenvectors. Diaconis and Graham (1985, Example 2.3) already prove the integer-zero tests for the degree-one and degree-two Krawtchouk polynomials, including the *perfect-square* criterion in the context of finite Radon transforms. Krovi and Brun (2006), and Le, Donati, Severini and Caruso (2017, section II), establish the general dark-eigenstate principle for target-site absorption. **None of those general ingredients, polynomial root tests, or the original perfect-transfer Hamiltonian is claimed new.** The comparatively narrow contribution is their explicit synthesis into an exact length-dependent local-loss classification, endpoint capture law, and minimal two-detector protection remedy for this spin-transfer architecture. These conclusions are directly derivable using the credited results; any earlier source that already makes that synthesis would cover the claim.

## Limitations
Only a single excitation, coherent weighted-path hopping, and independent strictly positive Markovian absorption are treated. Different coupling profiles, dephasing, collective sink interference, finite-time rates, multiple excitations, and a detector at arbitrary internal sites are not classified here. The cubic and higher Krawtchouk zero problems are not solved. This is a precise application of established Krawtchouk and dark-state principles, so its novelty and priority are necessarily narrower than the algebraic root criteria and subject to independent bibliographic review.

## References
- M. Christandl, N. Datta, A. Ekert and A. J. Landahl, *Perfect State Transfer in Quantum Spin Networks*, arXiv:quant-ph/0309131v1 (2003-09-17), https://arxiv.org/abs/quant-ph/0309131 .
- P. Diaconis and R. L. Graham, *The Radon Transform on \(\mathbb Z_2^k\)*, Pacific Journal of Mathematics **118** (1985), 323–345, Example 2.3, https://fanchung.ucsd.edu/ron/papers/85_04_radon.pdf .
- L. Vinet and A. Zhedanov, *How to Construct Spin Chains with Perfect State Transfer*, arXiv:1110.6474 (2011), https://arxiv.org/abs/1110.6474 .
- T. Le, F. Donati, S. Severini and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (2017), https://arxiv.org/abs/1707.07482 .
- H. Krovi and T. Brun, *Hitting Time for Quantum Walks on the Hypercube*, arXiv:quant-ph/0606094 (2006), https://arxiv.org/abs/quant-ph/0606094 .
