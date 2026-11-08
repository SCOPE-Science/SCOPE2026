# Exact two- and four-cycle spectra at the endpoint controls of a parity-hybrid skew tent map

## Finding

**Theorem.** Let \(m\ge 2\) be any integer and \(N=2^m\). For the parity-hybrid skew tent permutation \(C_a\) defined below, the two endpoint controls \(a=1\) and \(a=N-1\) have completely explicit, uniform cycle spectra:

* At \(a=1\) there are exactly **two primitive two-cycles**, namely \(\{0,N-1\}\) and \(\{N/2,N/2-1\}\), and exactly \((N-4)/4\) primitive four-cycles. There are no other cycles.
* At \(a=N-1\) there are exactly \(N/4\) primitive four-cycles, and no cycles of any other length.

In particular \(C_1^4=C_{N-1}^4=\mathrm{id}\): every unprocessed orbit of either endpoint hybrid has period at most four, independently of the number of state bits. At \(a=1\) the permutation has exact order two for \(m=2\) and exact order four for \(m\ge3\); at \(a=N-1\) it has exact order four for all \(m\ge2\).

Writing \(\zeta_C(t)=\exp\bigl(\sum_{k\ge1}\#\operatorname{Fix}(C^k)t^k/k\bigr)\) for the finite permutation's dynamical zeta function, the complete formulas are

\[
\zeta_{C_1}(t)=(1-t^2)^{-2}(1-t^4)^{-(N-4)/4},
\qquad
\zeta_{C_{N-1}}(t)=(1-t^4)^{-N/4}.
\]

## Assumptions and scope

For every integer \(a\) with \(1\le a\le N-1\), define the finite-state skew tent map on \(\mathcal D_N=\{0,1,\ldots,N-1\}\) by the exact integer operations

\[
S_a(z)=\begin{cases}
\left\lceil \dfrac{N(z+1)}a\right\rceil-1,&0\le z<a,\\[3pt]
\left\lfloor\dfrac{N(N-1-z)}{N-a}\right\rfloor,&a\le z<N.
\end{cases}
\]

The parity-hybrid map from Choi and collaborators is

\[
C_a(z)=\begin{cases}S_a(z),&z\text{ even},\\
S_{N-a}(z),&z\text{ odd}.
\end{cases}
\]

Powers of a map denote composition. All congruences in the proof are modulo \(N\) and are evaluated on the unique representative in \(\mathcal D_N\). An orbit's *primitive period* is its least positive return time. No rounding other than the displayed exact floor and ceiling operations is allowed.

## Proof

**Step 1: endpoint skew tents.** If \(a=1\), at \(z=0\) the first formula yields \(N-1\). For \(1\le z<N\), put \(k=N-1-z\), so \(0\le k\le N-2\); then \(\lfloor Nk/(N-1)\rfloor=k\). Hence, for *every* \(z\),

\[S_1(z)=N-1-z.\]

If \(a=N-1\), then for \(0\le z\le N-2\) put \(k=z+1\), so \(1\le k\le N-1\). The equality \(\lceil Nk/(N-1)\rceil-1=k\) holds, including \(k=N-1\); the remaining endpoint \(z=N-1\) maps to zero. Thus

\[S_{N-1}(z)\equiv z+1\pmod N.\]

Notice that the unhybridized permutation \(S_{N-1}\) has exact order \(N\). In contrast the hybrid at the same control has order four, as shown next.

**Step 2: explicit parity action and fourth powers.** Since \(N\) is divisible by four, applying the defining parity choice gives

\[
C_1(z)\equiv\begin{cases}-1-z,&z\text{ even},\\z+1,&z\text{ odd},\end{cases}
\qquad
C_{N-1}(z)\equiv\begin{cases}z+1,&z\text{ even},\\-1-z,&z\text{ odd}.\end{cases}
\]

Both maps swap even and odd residues; neither has a fixed point. Applying either map twice gives

\[
C_1^2(z)\equiv\begin{cases}-z,&z\text{ even},\\-2-z,&z\text{ odd},\end{cases}
\qquad
C_{N-1}^2(z)\equiv\begin{cases}-2-z,&z\text{ even},\\-z,&z\text{ odd}.\end{cases}
\]

Each two-step branch preserves parity and is an affine reflection; its square is the identity. Hence the fourth power of each hybrid is the identity. The only possible primitive periods are therefore one, two and four, and parity swapping already excludes period one.

**Step 3: count period-two points without omitted cases.** The congruence \(2z\equiv0\pmod N\) has precisely two solutions in \(\mathcal D_N\): \(z=0\) and \(z=N/2\), both even. The congruence \(2z\equiv-2\pmod N\) likewise has precisely \(z=N/2-1\) and \(z=N-1\), both odd. Thus the two parity branches of \(C_1^2\) contribute two fixed points each, exactly four in total. They form the two explicitly displayed two-cycles. The remaining \(N-4\) states must lie on primitive four-cycles, yielding \((N-4)/4\) such cycles.

For \(C_{N-1}^2\), the even branch requires \(2z\equiv-2\pmod N\), whose two solutions are **odd**, while the odd branch requires \(2z\equiv0\pmod N\), whose two solutions are **even**. Thus neither branch has a fixed point, and all \(N\) states lie on exactly \(N/4\) primitive four-cycles.

**Step 4: zeta functions and boundary cases.** A primitive cycle of length \(d\) contributes \((1-t^d)^{-1}\) to the finite permutation's dynamical zeta function. Multiplying these factors over the complete cycle censuses gives the stated rational formulas. At \(m=2\), \(N=4\) and the number of four-cycles for \(C_1\) is zero, giving exact order two; otherwise at least one four-cycle exists. The claimed orders follow. \(\square\)

## Verification

The packaged `verify.py` recomputes the original floor/ceiling definition using integer arithmetic, independently checks both endpoint skew tent identities and both two-step branch formulas for *every* state, enumerates disjoint cycles, checks the asserted cycle counts, and checks fixed-point counts for powers one through twelve. It completes for every \(m\in\{2,\ldots,14\}\), covering \(65{,}528\) endpoint/state pairs, with the output:

`VERIFY_OK m=2..14 endpoint_controls=26 checked_states=65528 cycle_counts_and_fixed_point_spectra=exact`

The all-\(m\) theorem follows from the elementary algebra above, not from extrapolation of these finite checks. Reproduce using `python verify.py` (standard Python, no third-party dependencies).

## Relationship to prior work

Choi et al. define exactly this parity-hybrid map (their Definition 1) and prove its bijectivity and asymptotically maximal discrete Lyapunov exponent (their Theorems 2 and 3). Their numerical sections examine general interior control parameters; their concluding discussion explicitly identifies the dependence of output periods on control and initial state as requiring further analysis. Those results do not entail the present endpoint cycle census: the fact that a map is bijective or has a large discrete Lyapunov exponent does not determine its finite permutation order. In particular, the pure endpoint skew tent \(S_{N-1}\) has order \(N\), while the hybrid \(C_{N-1}\) has order four. Related finite dynamical zeta and short-period results for other maps concern distinct systems and do not supply this classification.

## Limitations

Only the two admissible *endpoint* controls, \(a=1\) and \(a=N-1\), are classified. No assertion is made about intermediate controls, postprocessed bit streams, statistical properties of parameter mixtures, cryptographic security, or conventional infinite-state topological chaos. The source's discrete Lyapunov exponent is a distinct finite-state diagnostic and is not independently rederived here. The finite test does not replace the algebraic proof. Historical priority beyond the inspected sources has not been independently established.

## References

1. H. Choi, G. Kim, H.-Y. Song, S. Shin, C. Lee, and H. Noh, *Some New Maximally Chaotic Discrete Maps*, Entropy **28** (2026), 131, published 2026-01-22. DOI: 10.3390/e28010131. Definition 1, Theorems 2–3, Sections 4–5. https://doi.org/10.3390/e28010131
2. C. Fan and Q. Ding, *Analyzing the period distribution of digital chaos with graph theory* (2021), a comparison concerning finite-precision digital chaotic maps, not the parity-hybrid map defined by Choi et al. Bibliographic details require independent verification.
