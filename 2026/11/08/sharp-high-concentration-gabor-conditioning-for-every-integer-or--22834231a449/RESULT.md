# Sharp high-concentration Gabor conditioning for integer-order Matérn windows

## Finding
For every fixed integer \(m\ge2\), the optimal lower frame bound of the redundancy-two Gabor system associated with the origin-normalized, symmetric integer-order Matérn window obeys
\[
 A_m(\lambda)\sim 4\left(\frac{(m-1)!}{(2m-2)!}\right)^2\lambda^{2m-2}e^{-\lambda},\qquad \lambda\to\infty.
\]
Its upper frame bound satisfies \(B_m(\lambda)\to2\), and therefore
\[
 \frac{B_m(\lambda)}{A_m(\lambda)}\sim
 \frac{((2m-2)!)^2}{2((m-1)!)^2}\frac{e^\lambda}{\lambda^{2m-2}}.
\]
For any minimizing sequence of Zak fibers, the time coordinate converges to the midpoint \(1/2\) modulo integer translation. The power of \(\lambda\) and its factorial constant depend explicitly on the Matérn order.

## Assumptions and scope
Let \(m\in\{2,3,\ldots\}\), \(n=m-1\), and \(\lambda>0\). Write
\[
 P_n(s)=\frac{n!}{(2n)!}\sum_{j=0}^{n}\frac{(2n-j)!}{(n-j)!j!}(2s)^j,
 \qquad g_{m,\lambda}(t)=e^{-\lambda|t|}P_n(\lambda|t|).
\]
In particular, \(P_n(0)=1\), and its leading coefficient is \(2^nn!/(2n)!\). The Fourier transform of this window is a positive constant multiple of \((\lambda^2+4\pi^2\xi^2)^{-m}\); equivalently, it is the normalized \(m\)-fold convolution of a symmetric Laplace density. This identification motivates the designation integer-order Matérn or Bessel-potential window. We use the time translation \(T_kf(t)=f(t-k)\) and frequency modulation \(M_{j/2}f(t)=e^{\pi ijt}f(t)\), and the Fourier sign convention \(e^{2\pi i k\omega}\) for the Zak transform.

Precisely, \(A_m(\lambda)\) is the largest positive number, and \(B_m(\lambda)\) the smallest finite number, such that
\[
 A_m(\lambda)\|f\|_2^2\le \sum_{j,k\in\mathbb Z}|\langle f,M_{j/2}T_kg_{m,\lambda}\rangle|^2\le B_m(\lambda)\|f\|_2^2
\]
for every \(f\in L^2(\mathbb R)\). Here \(m\) remains fixed when \(\lambda\) diverges. The normalizations of both the window and the Gabor lattice are essential to the displayed constants.

## Proof
**1. Exact scalar Zak symbol.** The exponentially decaying window permits the absolutely and uniformly convergent Zak series
\[Z_{m,\lambda}(x,\omega)=\sum_{k\in\mathbb Z}g_{m,\lambda}(x-k)e^{2\pi i k\omega}.\]
The standard integer-oversampling Zak diagonalization (with translation step one and modulation step one-half) gives the *optimal*, not merely admissible, bounds
\[
 A_m(\lambda)=\min_{x,\omega\in[0,1]}S_{m,\lambda}(x,\omega),\qquad
 B_m(\lambda)=\max_{x,\omega\in[0,1]}S_{m,\lambda}(x,\omega),
\]
where
\[S_{m,\lambda}(x,\omega)=|Z_{m,\lambda}(x,\omega)|^2+|Z_{m,\lambda}(x,\omega+\tfrac12)|^2.\]
Writing \(E=\sum_{k\in2\mathbb Z}g(x-k)e^{2\pi i k\omega}\) and \(O=\sum_{k\in2\mathbb Z+1}g(x-k)e^{2\pi i k\omega}\) gives exactly
\[S_{m,\lambda}(x,\omega)=2(|E|^2+|O|^2).\]
Quasiperiodicity and the evenness of the real window permit restriction to \(0\le x\le1/2\). Existence of the frame for every \(\lambda>0\) also follows from total positivity and the density-two lattice, but it will follow directly from the symbol for sufficiently large \(\lambda\), the only regime needed here.

**2. Monotonicity and scales.** The polynomial has positive coefficients \(a_j\), with
\[(j+1)a_{j+1}/a_j=2(n-j)/(2n-j)\le1\quad(0\le j<n).\]
Thus \(s\mapsto e^{-s}P_n(s)\) is nonincreasing, positive, and at most one. On any fixed compact interval of positive \(t\), as \(\lambda\to\infty\),
\[
 g_{m,\lambda}(t)=\frac{2^nn!}{(2n)!}(\lambda t)^ne^{-\lambda t}(1+O_{m,t}(\lambda^{-1})),
\]
with a *uniform* relative remainder when the interval stays away from zero. In particular,
\[h_\lambda:=g_{m,\lambda}(1/2)\sim\frac{n!}{(2n)!}\lambda^ne^{-\lambda/2}.\]
For the rest of the proof, constants in the asymptotic notation may depend on fixed \(m\), but not on the Zak parameters.

**3. Uniform separation of nearest lattice translates.** For \(0\le x\le1/4\), the nearest even translate has \(k=0\); all other even translates lie at distance at least \(7/4\). Uniform geometric tail estimation gives
\[
 E(x,\omega)=g(x)+O_m(\lambda^ne^{-7\lambda/4}).
\]
Consequently \(|E(x,\omega)|\ge g(1/4)-O_m(\lambda^ne^{-7\lambda/4})\), and
\[\inf_{0\le x\le1/4,\,\omega}S(x,\omega)/h_\lambda^2\to+\infty.\]
Here and below we omit the fixed subscripts on \(g,E,O,S\).

For \(1/4\le x\le1/2\), the nearest even and odd translates are respectively \(k=0\) and \(k=1\). All other even translates are at distance at least \(3/2\), and all other odd translates at distance at least \(5/4\). Thus, uniformly in both Zak parameters,
\[
 E(x,\omega)=g(x)+O_m(\lambda^ne^{-3\lambda/2}),
 \qquad O(x,\omega)=e^{2\pi i\omega}g(1-x)+O_m(\lambda^ne^{-5\lambda/4}).
\]
Because both leading terms are bounded on this interval by a fixed multiple of \(g(1/4)\), these estimates imply the additive expansion
\[
 S(x,\omega)=2\big(g(x)^2+g(1-x)^2\big)+o(h_\lambda^2)
\]
uniformly for \(x\in[1/4,1/2]\) and \(\omega\in[0,1]\). The error is exponentially smaller than \(h_\lambda^2\).

**4. The sharp minimum.** Let \(q_n(s)=e^{-2s}P_n(s)^2\). Direct differentiation shows
\[
 q_n''(s)=e^{-2s}\bigl(4P_n(s)^2-8P_n(s)P_n'(s)+2P_n'(s)^2+2P_n(s)P_n''(s)\bigr).
\]
Since \(P_n(s)\) has strictly positive leading coefficient and fixed degree, the expression in parentheses is \(4P_n(s)^2(1+O_n(s^{-1}))>0\) for all sufficiently large positive \(s\). Hence for sufficiently large \(\lambda\), the function \(t\mapsto g(t)^2=q_n(\lambda t)\) is convex on \([1/4,3/4]\). Jensen's inequality gives
\[g(x)^2+g(1-x)^2\ge2g(1/2)^2=2h_\lambda^2\qquad(1/4\le x\le1/2).\]
Combining this inequality with Step 3 and the divergent lower bound on \([0,1/4]\) establishes \(S\ge4h_\lambda^2+o(h_\lambda^2)\) uniformly on a Zak fundamental domain. At \(x=1/2\) the Step-3 estimate yields \(S(1/2,\omega)=4h_\lambda^2+o(h_\lambda^2)\) uniformly in \(\omega\). Therefore
\[A_m(\lambda)\sim 4h_\lambda^2\sim4\left(\frac{n!}{(2n)!}\right)^2\lambda^{2n}e^{-\lambda}.\]
Furthermore, for any fixed \(\varepsilon>0\), the nearest even translate when \(0\le x\le1/2-\varepsilon\) yields a lower symbol scale exponentially larger than \(h_\lambda^2\). The minimizing time coordinates must consequently approach \(1/2\), proving localization.

**5. The sharp maximum.** On \([0,1/4]\), the same uniform tail separation gives \(E=g(x)+o(1)\) and \(O=o(1)\). Since \(0<g(x)\le1\), it follows that \(S\le2+o(1)\) there. On \([1/4,1/2]\), the uniform expansions of Step 3 give \(E=o(1)\) and \(O=o(1)\), hence \(S=o(1)\) on that interval. Therefore \(B_m(\lambda)\le2+o(1)\); evaluating at \((x,\omega)=(0,0)\) gives \(B_m(\lambda)\ge2+o(1)\). Thus \(B_m(\lambda)\to2\), and division by the positive lower-bound asymptotic completes the condition-number formula. \(\square\)

## Verification
The accompanying standalone `CHECK.py` evaluates the defining coefficients exactly using integer-rational arithmetic, verifies their monotonicity inequalities, and independently evaluates the two Zak channels by truncating the absolutely convergent translate sums. It tests degrees \(m=2,3,4,5,6\) and a range of positive \(\lambda\). Output `MATERN_GABOR_ASYMPTOTICS_CHECKS_PASSED 17300` was obtained from the extracted script. These numerical grids are finite consistency checks only: they do **not** establish the universal minimization, the exact sharp bound, or the asymptotic limits. Those statements follow from the full uniform estimates in the proof.

## Relationship to prior work
Pont, Gröchenig, Liehr, Shafkulovska, and Taylor (arXiv:2608.04992; first public 2026-08-05) solve the qualitative frame-set problem for continuous integrable totally positive windows. This guarantees positivity of the lower bound at every subcritical lattice density, but does not specify the sharp high-decay constant for the present integer-order Matérn family. Kloos and Stöckler (arXiv:1311.7359) give Zak methods and separate quantitative work for two-sided exponential windows. Faulhuber and Shafkulovska (arXiv:2204.02917) optimize frame bounds for other windows including two-sided exponentials; their stated model is the first-order exponential rather than the higher convolution powers studied here. Ghosh and Antony Selvan (arXiv:2304.11322) present sampling-theoretic sufficient regions and bounds, not these sharp fixed-lattice concentration limits. The Zak representation and its normalization are established tools and are not claimed to be new. The contribution is the evaluated all-integer-order sharp exponential-polynomial stability law and time-fiber localization.

## Limitations
The order \(m\) is fixed before taking \(\lambda\to\infty\); no joint-order uniformity is claimed. The constants use origin-normalized windows \(g(0)=1\); rescaling a window changes the frame bounds by the square of the scaling factor. The lattice has translation step exactly one and modulation step exactly one-half. No finite-\(\lambda\) exact extremizer classification or other-lattice optimization is established. A synonymous result could be hidden in earlier special-function frame-bound literature; priority has not undergone independent external audit.

## References
1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992 (first public 2026-08-05), https://arxiv.org/abs/2608.04992.
2. T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359.
3. M. Faulhuber, I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (2022/2023), https://arxiv.org/html/2204.02917v2.
4. R. Ghosh, A. Antony Selvan, *On Gabor frames generated by B-splines, totally positive functions, and Hermite functions*, arXiv:2304.11322 (2023), https://arxiv.org/abs/2304.11322.
